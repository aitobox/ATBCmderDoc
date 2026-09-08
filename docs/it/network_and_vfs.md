# Capitolo 6: File system virtuali e rete

La moderna gestione dei file raramente si ferma al confine di un singolo disco rigido fisico. Gli sviluppatori di software mantengono ambienti di gestione temporanea remoti su SFTP; gli amministratori di sistema gestiscono le condivisioni di file aziendali su SMB/CIFS; i creatori di contenuti accedono allo storage cloud e ai server multimediali tramite WebDAV; e gli utenti esperti ispezionano, modificano e impacchettano regolarmente archivi compressi su scala gigabyte. 

Gli ambienti desktop tradizionali costringono gli utenti a destreggiarsi tra applicazioni disgiunte: un'utilità di archivio autonoma per decomprimere e ricomprimere archivi zip, un client FTP/SFTP esterno per gestire le risorse del server e finestre di dialogo di montaggio del sistema operativo che spargono volumi remoti su finestre del Finder disconnesse. 

ATBCmder elimina questa frammentazione attraverso il suo motore **Virtual File System (VFS)**. Basato su un livello di astrazione URI `vfs://` unificato, ATBCmder tratta i server remoti e gli archivi compressi esattamente come cartelle locali standard. È possibile navigare in un archivio `.tar.gz`, visualizzare in anteprima i file di codice con `F3`, modificare un file di configurazione nidificato con `F4` (con repacking automatico in tempo reale al salvataggio) e copiare le risorse direttamente attraverso una sessione SFTP sicura su un NAS per PMI in sede utilizzando la chiave standard `F5`, il tutto senza estrarre file intermedi su disco o passare da uno strumento separato all'altro. 

---

## 1. Avvio rapido visivo: l'architettura VFS e la matrice dei comandi

ATBCmder instrada tutto l'accesso al filesystem attraverso un livello di astrazione unificato. Sia che un percorso punti a una partizione SSD APFS Apple, a un membro all'interno di un archivio nidificato `.zip` o a una directory remota ospitata su un server SFTP Linux dall'altra parte del mondo, l'interfaccia a doppio pannello fornisce un modello operativo identico. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              ATBCMDER DUAL-PANEL GUI                                   │
│            Left Panel (Active)                  Right Panel (Inactive / Target)        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Local File System                   │  [2] Archive Virtual File System (VFS)      │
│      file:///Users/brain/projects/       │      vfs:///Users/brain/backup.tar.gz/src/  │
│      Direct POSIX / APFS access          │      In-place browse, F3 view, F4 live edit │
│                                          │                                             │
│  [3] Remote Network VFS (SFTP/SSH)       │  [4] Remote Storage VFS (SMB / WebDAV)      │
│      vfs://sftp://deploy@aws.prod/app/   │      vfs://smb://admin@truenas/Pool/Media/  │
│      Paramiko / SSH Keys / Keychain      │      Kernel mount_smbfs / WebDAVClient3     │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                          UNIFIED VFS DISPATCH ENGINE (vfs://)                          │
│     FileSystemModel ➔ VFSManager ➔ SessionCache ➔ StreamCopyWorker / RepackWorker      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### VFS a doppia matrice e foglio informativo di rete

| Azione | Scorciatoia macOS | Chiave del comandante classico | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Comprimi i file nell'archivio** | `Alt+F5` / `⌥F5` | `Alt+F5` | `cm_PackFiles` | Apre la finestra di dialogo Pacchetto archivio con le opzioni di formato, compressione e password. | 
| **Estrai file dall'archivio** | `Alt+F9` / `⌥F9` | `Alt+F9` | `cm_ExtractFiles` | Decomprime gli archivi selezionati con risoluzione delle collisioni. | 
| **Connessione di rete rapida** | Menù: Rete | `cm_NetworkConnect` | `cm_NetworkConnect` | Apre la finestra di dialogo di connessione veloce ad hoc. | 
| **Gestione connessione** | Menù: Rete | `cm_ManageConnections`| `cm_ManageConnections`| Apre il gestore di rete CRUD completo con i profili di connessione salvati. | 
| **Connessione FTP** | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_FTPConnect` | Scorciatoia rapida per attivare la sessione di connessione FTP. | 
| **Inserisci archivio/cartella** | `Enter` / `⏎` | `Enter` | `cm_Open` | Naviga direttamente all'interno di una directory `.zip`, `.tar`, `.7z` o remota. | 
| **Sali alla cartella principale** | `Backspace` / `⌫` | `Backspace` | `cm_GoToParent` | Esce dall'archivio o dalla directory remota e torna al livello principale. | 
| **Visualizza file virtuale/remoto**| `F3` / `Fn+F3` | `F3` | `cm_View` | Trasmette file remoti o di archivio in Universal Lister. | 
| **Modifica file virtuale/remoto**| `F4` / `Fn+F4` | `F4` | `cm_Edit` | Apre il file nell'editor; si ricompone automaticamente o si carica nuovamente al momento del salvataggio. | 
| **Copia tra pannelli/VFS** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia gli elementi selezionati sugli endpoint locali, di archivio o di rete. | 
| **Pannello delle operazioni in background**| Menù: Mostra | `cm_OperationsPanel` | `cm_OperationsPanel` | Monitora le code di trasferimento in background, le velocità e i thread attivi. | 

---

## 2. L'astrazione URI unificata `vfs://`

I file manager tradizionali trattano i server e gli archivi remoti come cittadini di seconda classe, richiedendo utilità di montaggio esterne, cartelle di estrazione temporanee o client di trasferimento di terze parti. ATBCmder unifica ogni origine file sotto un'unica specifica URI ben definita: 

```
vfs://[protocol]://[user]@[host]:[port]/[remote_path]
```

### 2.1 Anatomia dei percorsi virtuali

A seconda del dominio operativo, gli URI `vfs://` assumono una delle due forme standard: 

1. **Archivia percorsi virtuali**: 
   ```
   vfs:///Users/brain/Documents/release_v1.7.zip/src/main.py
   ```
 

- **Prefisso esterno**: `vfs://` indica a `FileSystemModel` di intercettare l'attraversamento del percorso. 
- **Percorso contenitore**: `/Users/brain/Documents/release_v1.7.zip` identifica l'archivio del contenitore fisico nello spazio di archiviazione locale. 
- **Membro interno**: `src/main.py` individua la risorsa virtuale annidata all'interno dell'archivio. 

2. **Percorsi del server di rete**: 
   ```
   vfs://sftp://developer@staging.internal.net:2222/var/www/html/index.php
   vfs://smb://admin@192.168.1.50/StoragePool/Backups/2026/
   vfs://webdavs://user@cloud.mycompany.com:443/remote.php/dav/files/user/
   ```
 

- **Scheme Specifier**: identifica il driver di trasporto (`sftp`, `ftp`, `ftps`, `smb`, `webdav`, `webdavs`, `gdrive`). 
- **Autenticazione**: codifica le credenziali dell'utente e la porta di destinazione. 
- **Target remoto**: risolve la directory assoluta e i percorsi dei file sull'host remoto. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              VFS URI ROUTING IN ACTION                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Input URI: vfs://sftp://deploy@aws.infra:22/var/log/nginx/access.log                 │
│                 │      │        │        │   └────────────────────► Remote Path        │
│                 │      │        │        └────────────────────────► Port (Default 22)  │
│                 │      │        └─────────────────────────────────► Host / Server      │
│                 │      └──────────────────────────────────────────► Username           │
│                 └─────────────────────────────────────────────────► Protocol Scheme    │
│                                                                                        │
│   Input URI: vfs:///Volumes/Data/Archive.zip/docs/manual.pdf                           │
│                 │                      │        └─────────────────► Archive Member     │
│                 │                      └──────────────────────────► Physical Archive   │
│                 └─────────────────────────────────────────────────► Virtual Scheme     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Integrazione perfetta del doppio pannello

Poiché i percorsi virtuali sono conformi alle strutture di directory standard all'interno di ATBCmder, puoi usufruire della piena parità a doppio pannello: 

- **Aree di lavoro virtuali a schede**: apri una cartella SFTP remota nella Scheda 1, un archivio ZIP locale crittografato nella Scheda 2 e la cartella `~/Downloads` locale nella Scheda 3. 
- **Copia direzionale (`F5`)**: seleziona i file nel pannello attivo locale e premi `F5` per caricarli direttamente nel server remoto o nell'archivio compresso visualizzato nel pannello inattivo. 
- **Interoperabilità drag-and-drop**: trascina gli elementi tra pannelli tra dischi locali, condivisioni di rete e gerarchie di archivio senza gestione temporanea intermedia. 
- **Barra breadcrumb interattiva**: la barra del percorso breadcrumb analizza gli URI virtuali in segmenti selezionabili. Fai clic su qualsiasi cartella principale o sul badge del server root per saltare immediatamente sull'albero. 

---

## 3. Archivio VFS: navigazione e ispezione sul posto

L'apertura di un archivio in ATBCmder non richiede l'estrazione manuale o uno strumento di decompressione di terze parti. Evidenzia semplicemente qualsiasi archivio supportato e premi **`Enter`** (o fai doppio clic). ATBCmder monta l'archivio sul posto, trasformando il pannello in un browser di directory virtuale ad alta velocità. 

![Archive VFS In-Place Navigation](images/archive_vfs.png) 
*Figura 6.1: Navigazione all'interno di un archivio compresso multi-nidificato come una cartella virtuale, che mostra dimensioni, timestamp e sottodirectory non compressi.*

### 3.1 Formati di archivio supportati

ATBCmder dispone di driver integrati per tutti i formati di archiviazione e compressione standard del settore: 

| Formato | Estensioni file | Leggi Supporto | Scrivi / Imballa | Supporto per la crittografia | 
| :--- | :--- | :---: | :---: | :--- | 
| **CAP** | `.zip` | Sì | Sì | Standard e AES-256 (`pyzipper`) | 
| **GZip Tarball** | `.tar.gz`, `.tgz` | Sì | Sì | Streaming tar standard POSIX | 
| **BZip2 Tarball**| `.tar.bz2`, `.tbz2` | Sì | Sì | Compressione del blocco bzip2 ad alto rapporto | 
| **XZ Tarball** | `.tar.xz`, `.txz` | Sì | Sì | Compressione LZMA2 ad alta efficienza | 
| **TAR semplice** | `.tar` | Sì | Sì | Archivio su nastro UNIX non compresso | 
| **7-Zip** | `.7z` | Sì | Sì (tramite `py7zr`)| Compressione solida LZMA / LZMA2 |

### 3.2 Flussi di lavoro di navigazione sul posto

Durante la navigazione all'interno di un archivio: 

1. **Entra nelle sottodirectory**: premi `Enter` su qualsiasi cartella all'interno dell'archivio per esplorare gli alberi nidificati. 
2. **Sali a principale (`..`)**: premi `Backspace` (`⌫`) o fai doppio clic sulla voce `.. [Parent Directory]` per salire. Una volta raggiunta la radice dell'archivio, premendo `Backspace` si ritorna direttamente alla directory fisica contenente il file di archivio. 
3. **Anteprima istantanea (`F3` / `Fn+F3`)**: evidenzia qualsiasi documento, immagine o file di origine all'interno dell'archivio e premi `F3`. ATBCmder estrae automaticamente il file di destinazione in una sandbox temporanea sicura e lo esegue il rendering all'interno dell'Universal Lister. 
4. **Copia selettiva (`F5` / `Fn+F5`)**: invece di decomprimere un intero archivio multi-gigabyte solo per recuperare uno o due file, seleziona i membri specifici di cui hai bisogno e premi `F5`. ATBCmder decomprime solo gli elementi scelti direttamente nel pannello inattivo. 

> [!NOTE] 
> Durante l'anteprima o la copia di singoli file da un archivio, ATBCmder trasmette solo i byte di file richiesti direttamente dal flusso del contenitore. Non spreca spazio su disco o tempo decomprimendo i file di pari livello non selezionati. 

---

## 4. Repacking in tempo reale: modifica sul posto all'interno degli archivi

Uno dei flussi di lavoro più potenti in ATBCmder è **Live Repacking**. Storicamente, la modifica di un singolo file annidato all'interno di un archivio compresso richiedeva una noiosa sequenza di sei passaggi: estrarre l'intero archivio, individuare il file di destinazione, modificarlo e salvarlo, ricomprimere la directory in un nuovo archivio, eliminare l'archivio originale e ripulire le cartelle temporanee. 

ATBCmder rende la modifica dei file all'interno degli archivi altrettanto semplice quanto la modifica dei file locali standard. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              LIVE REPACKING LIFECYCLE                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  1. User presses F4 on "config.json" inside "package.zip"                              │
│     │                                                                                  │
│     ├──► ATBCmder extracts "config.json" to sandbox: /tmp/dc_repack_xyz/config.json    │
│     └──► Opens internal EditorDialog with window title: "config.json — Editor"         │
│                                                                                        │
│  2. User modifies file and presses Cmd+S (Save)                                        │
│     │                                                                                  │
│     ├──► Editor emits file_saved signal                                                │
│     └──► RepackWorker checks original archive size vs ArchiveRepackWarningMB threshold │
│                                                                                        │
│  3. Atomic Repack Execution                                                            │
│     │                                                                                  │
│     ├──► Writes modified stream to staging archive: /tmp/package.zip.tmp               │
│     ├──► Validates container integrity via archive driver                              │
│     ├──► Atomic swap: os.replace("/tmp/package.zip.tmp", "/original/package.zip")      │
│     └──► Refreshes active file panel and cleans up sandbox /tmp/dc_repack_xyz/         │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Passo dopo passo: modifica di un file di configurazione archiviato

1. Navigare nell'archivio (ad esempio, `application_bundle.zip`) premendo `Enter`. 
2. Individua il file che desideri modificare (ad esempio, `settings.yaml`). 
3. Premere **`F4`** (`Fn+F4`). ATBCmder estrae il file in una cache temporanea e avvia l'editor integrato. 
4. Apporta le modifiche nell'editor. 
5. Premere **`Cmd+S`** (`⌘S`) per salvare. 
6. Chiudere l'editor con `Cmd+W` (`⌘W`) o `Esc`. 
7. `RepackWorker` di ATBCmder aggiorna automaticamente il membro interno, comprime la struttura aggiornata in un file temporaneo, sostituisce atomicamente l'archivio originale e aggiorna la visualizzazione del pannello. 

> [!WARNING] 
> **Protezione di sicurezza per archivio grande (`ArchiveRepackWarningMB`)** 
> Il repacking di un archivio compresso richiede la decompressione e la ricodifica dei flussi del contenitore. La modifica di un file da 10 KB all'interno di un archivio video `.tar.gz` da 20 GB costringerebbe il computer a riscrivere tutti i 20 GB di dati. 
> 
> Per evitare blocchi accidentali del disco, ATBCmder include una soglia di sicurezza protettiva (`ArchiveRepackWarningMB`, impostazione predefinita: **100 MB** in `atbcmder.xml`). Se tenti di modificare o eliminare un file all'interno di un archivio più grande di questo limite, ATBCmder visualizza una richiesta di conferma: 
> *"La modifica di questo archivio richiede il reimballaggio dell'intero file, operazione che potrebbe richiedere molto tempo. Vuoi continuare?"* 

---

## 5. Creazione ed estrazione di archivi (`Alt+F5` / `Alt+F9`)

ATBCmder fornisce operatori in background dedicati per la creazione e l'estrazione di archivi, garantendo che i pannelli dei file rimangano reattivi anche durante processi di compressione di lunga durata. 

![Pack and Extract Archives](images/archive_pack_extract.png) 
*Figura 6.2: La finestra di dialogo Parametri archivio (Alt+F5 / cm_PackFiles) che mostra il percorso di destinazione, la selezione del formato, i livelli di compressione e la crittografia della password.*

### 5.1 Compressione di file (`Alt+F5` / `⌥F5` / `cm_PackFiles`)

Per creare un nuovo archivio: 

1. Nel pannello attivo, seleziona i file o le directory che desideri raggruppare. 
2. Premere **`Alt+F5`** (`⌥F5`) o scegliere **File ➔ Pacchetto...** dalla barra dei menu. 
3. Viene visualizzata la finestra di dialogo **Comprimi file**: 
- **Crea file di archivio**: percorso file di destinazione. Per impostazione predefinita, ATBCmder suggerisce di posizionare l'archivio nella directory del pannello inattivo, che prende il nome dall'elemento focalizzato. 
- **Formato archivio**: scegli tra `ZIP`, `TAR`, `TAR.GZ`, `TAR.BZ2`, `TAR.XZ` o `7Z`. 
- **Livello di compressione**: 
- `Store`: compressione zero; confezionamento istantaneo per supporti precompressi (MP4, JPEG). 
- `Fast`: basso sovraccarico della CPU; ideale per trasferimenti veloci. 
- `Normal (Deflated)`: Rapporto di velocità e compressione bilanciato (consigliato per uso generale). 
- `Maximum`: compressione a densità più elevata (utilizza LZMA/Bzip2 ove applicabile). 
- **Password (solo ZIP)**: inserisci una passphrase segreta per crittografare l'archivio. 
4. Fare clic su **Start** (o premere `Enter`). L'operazione viene eseguita in un thread in background non bloccante con una barra di avanzamento e un indicatore di stato file per file.

#### Crittografia password AES-256 di livello militare

La crittografia ZIP standard (legacy ZipCrypto) è crittograficamente compromessa e vulnerabile agli attacchi del dizionario di testo normale. Quando specifichi una password per un archivio ZIP, ATBCmder utilizza la **crittografia AES-256** fornita da `pyzipper` (`pyzipper.AESZipFile` con `WZ_AES` standard). Ciò garantisce la compatibilità con macOS, WinZip e 7-Zip proteggendo al tempo stesso i dati sensibili dalla decrittografia a forza bruta.

#### Suddivisione di archivi enormi su set multivolume

Se devi distribuire un archivio tra allegati e-mail, unità FAT32 o limiti di caricamento nel cloud con limiti di dimensione file: 

1. Raggruppa i tuoi file utilizzando `Alt+F5` (`cm_PackFiles`). 
2. Evidenziare l'archivio `.zip` o `.tar` risultante e attivare il File Splitter tramite **`Alt+F6`** (`cm_FileSpliter`). 
3. Selezionare una dimensione di suddivisione preimpostata (ad esempio, `100 MB`, `4.7 GB DVD`, `CD 700 MB` o dimensione in byte personalizzata). 
4. ATBCmder genera parti divise numerate (`archive.zip.001`, `archive.zip.002`, ecc.) insieme a un manifest di verifica CRC32. I destinatari possono rimontare il contenitore originale in qualsiasi momento utilizzando **`cm_FileLinker`** (`cm_Combine`). 

---

### 5.2 Estrazione degli archivi (`Alt+F9` / `⌥F9` / `cm_ExtractFiles`)

Per estrarre gli archivi su disco: 

1. Evidenzia uno o più archivi nel pannello attivo. 
2. Premere **`Alt+F9`** (`⌥F9`) o scegliere **File ➔ Estrai...** dalla barra dei menu. 
3. Viene visualizzata la finestra di dialogo **Estrai file**: 
- **Archivio da estrarre**: percorso di origine del contenitore selezionato. 
- **Estrai nella directory**: directory di destinazione (per impostazione predefinita è il pannello inattivo). 
- **Anteprima dei contenuti**: una casella di riepilogo interattiva che carica i membri dell'archivio in tempo reale. 
- **Password**: campo di immissione per archivi protetti da password. 
4. Fare clic su **Avvia**. Se un file di destinazione esiste già nella cartella di destinazione, ATBCmder mette in pausa il lavoratore e presenta una finestra di dialogo interattiva di collisione: 
- **Sovrascrivi**: sostituisce il file di destinazione in conflitto. 
- **Salta**: lascia intatto il file esistente e procede all'elemento successivo. 
- **Sovrascrivi tutto**: sovrascrive silenziosamente tutti i conflitti successivi. 
- **Salta tutto**: ignora automaticamente tutti i file di destinazione esistenti. 
- **Annulla**: interrompe in modo sicuro il processo di estrazione. 

---

## 6. VFS di rete remota: protocolli e archiviazione remota

ATBCmder include un motore client di rete multiprotocollo in grado di montare, esplorare e manipolare server remoti direttamente all'interno dell'area di lavoro a doppio pannello. 

![Network VFS Client](images/network_vfs.png) 
*Figura 6.3: Navigazione nelle directory del server Linux remoto su SFTP sicuro con attributi di file attivi, autorizzazioni di proprietà e trasferimento a doppio pannello.* 

![Remote Connection Overview](images/smb_sftp_ftp_remote_access.png) 
*Figura 6.4: Tipi di connessione di rete supportati: FTP/FTPS, SFTP sicuro, archiviazione cloud WebDAV e condivisioni di rete SMB.*

### 6.1 Protocolli di rete supportati

| Schema del protocollo | Porta predefinita | Livello di trasporto | Modalità di autenticazione | Ideale per | 
| :--- | :---: | :--- | :--- | :--- | 
| **`sftp://`** | `22` | SSH-2 (Paramiko) | Password, chiave SSH (`id_rsa`, `id_ed25519`) | Server Linux, istanze cloud, host di staging | 
| **`ftp://`** | `21` | RFC semplice 959 | Nome utente e password anonimi e in chiaro | Hosting web legacy, dispositivi di laboratorio locali | 
| **`ftps://`** | `990` | FTP crittografato TLS | Nome utente e password con SSL/TLS | Server FTP commerciali sicuri | 
| **`smb://`** | `445` | CIFS/SMB3 | Windows NT/Kerberos/Account locale | Condivisioni Windows, apparecchi NAS, server Samba | 
| **`webdav://`** | `80` | WebDAV HTTP | Autenticazione di base e digest | Server Web, archiviazione di rete locale | 
| **`webdavs://`** | `443` | WebDAV HTTPS | Autenticazione base/digest crittografata SSL | Nextcloud, ownCloud, archiviazione cloud commerciale | 
| **`gdrive://`** | `443` | API di Google Drive | Autorizzazione token OAuth2 | Unità cloud e cartelle condivise di Google Drive | 

---

### 6.2 Funzionalità del protocollo e approfondimento

#### SFTP (protocollo di trasferimento file SSH)

Supportato dal motore SSH `paramiko` standard del settore, il driver SFTP di ATBCmder stabilisce tunnel crittografati sulla porta 22: 

- **Sicurezza chiave host (`WarningPolicy`)**: in conformità con severi requisiti di sicurezza, ATBCmder consulta automaticamente il tuo file `~/.ssh/known_hosts` locale. Quando ci si connette a un host conosciuto, le chiavi dell'host vengono verificate crittograficamente. Se viene rilevato un server sconosciuto, ATBCmder emette un avviso di sicurezza anziché fidarsi silenziosamente di chiavi pubbliche inaspettate. 
- **Autenticazione chiave SSH**: oltre all'autenticazione con password standard, ATBCmder supporta i file di chiave privata SSH (`~/.ssh/id_rsa`, `~/.ssh/id_ed25519`). 
- **Mappatura attributi UNIX**: preserva le modalità file ottali remoti (`chmod`), le stringhe di proprietà dell'utente/gruppo e i timestamp esatti di modifica POSIX.

#### FTP e FTPS (SSL esplicito/implicito)

Gestito da `ftplib` di Python, il driver FTP supporta: 

- **Modalità passiva (PASV)**: abilitata per impostazione predefinita per garantire connessioni affidabili tramite router NAT restrittivi e firewall consumer. 
- **Codifiche configurabili**: risolve i problemi di visualizzazione dei nomi file non ASCII consentendo di alternare tra i set di caratteri `UTF-8`, `ISO-8859-1`, `GB18030` e `Windows-1252`.

#### PMI/Samba (condivisioni Windows e dispositivi NAS)

A differenza delle ingenue librerie SMB Python per lo spazio utente che soffrono di velocità di trasferimento lente, ATBCmder utilizza un'architettura ibrida: 

- **Accelerazione kernel nativa di macOS (`mount_smbfs`)**: su macOS, `SambaMounter` di ATBCmder sfrutta il sottosistema `/sbin/mount_smbfs` nativo di Apple. Monta la condivisione remota direttamente nell'albero VFS di macOS (`/Volumes/` o una directory di montaggio isolata), sbloccando il throughput di lettura/scrittura SMB3 completo con accelerazione hardware. 
- **Rilevamento montaggio esistente**: se macOS Finder o uno script di sistema ha già montato la condivisione SMB di destinazione, ATBCmder rileva automaticamente il punto di montaggio attivo dalla tabella `mount` del sistema operativo e vi accede immediatamente, evitando connessioni di rete ridondanti. 

> [!IMPORTANT] 
> **Requisito nome condivisione PMI** 
> Non è possibile esplorare un server SMB a livello del semplice nome host. Un URI SMB **deve** includere la condivisione di destinazione o il nome di esportazione nel percorso: 
> 
> - ❌ Non valido: `vfs://smb://nas.local/` 
> - ✅ Valido: `vfs://smb://nas.local/StoragePool` o `vfs://smb://192.168.1.100/Media`

#### WebDAV e WebDAVS (Nextcloud/Archiviazione sul cloud)

Basato su `webdavclient3`, questo driver fornisce la sincronizzazione bidirezionale dei file con le moderne soluzioni di archiviazione cloud: 

- **Verifica del certificato SSL**: supporta la rigorosa convalida del certificato SSL per host WebDAVS pubblici, con un'attivazione/disattivazione dell'override per i certificati autofirmati nelle configurazioni di laboratori domestici privati. 
- **Creazione di directory ricorsiva (`makedirs`)**: crea automaticamente percorsi di directory remote nidificate mancanti durante le operazioni di caricamento in blocco. 

---

## 7. Connessione rapida e Gestione connessione

ATBCmder fornisce due meccanismi flessibili per la connessione a host remoti: **Quick Connect** per sessioni temporanee veloci e **Connection Manager** per segnalibri server persistenti e categorizzati.

### 7.1 Connessione rapida (`cm_NetworkConnect`)

Quando devi accedere rapidamente a un server senza ingombrare la tua configurazione permanente: 

1. Scegli **Rete ➔ Connessione rapida...** (o esegui il comando `cm_NetworkConnect`). 
2. Viene visualizzata la richiesta di connessione leggera: 
- **Protocollo**: Selezionare `sftp`, `ftp`, `ftps`, `smb`, `webdav`, `webdavs` o `gdrive`. 
- **Host e porta**: inserisci l'indirizzo del server (la porta compila automaticamente i valori predefiniti). 
- **Nome utente e password**: inserisci le credenziali di connessione. 
- **Percorso remoto**: avvio della directory remota (impostazione predefinita: `/`). 
- **Ricorda password**: lascia deselezionato per una connessione temporanea a sessione singola. 
3. Fare clic su **Verifica connessione** per verificare l'handshake e le credenziali della rete prima della connessione. 
4. Fare clic su **Connetti**. ATBCmder apre immediatamente una nuova scheda nel pannello attivo che punta al server remoto. 

---

### 7.2 Gestore connessione (`cm_ManageConnections`)

Per i server a cui accedi regolarmente, **Connection Manager** fornisce un dashboard di configurazione completo: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              CONNECTION MANAGER DIALOG                                 │
├──────────────────────────────┬─────────────────────────────────────────────────────────┤
│  Saved Connections           │  Connection Details                                     │
│  ┌────────────────────────┐  │  Label:        [ Staging Web Server (AWS)             ] │
│  │ 🔐 AWS Staging Server  │  │  Protocol:     [ SFTP (port 22)                     ▼ ] │
│  │ 🖧 Synology Office NAS │  │  Host:         [ ec2-54-210-10-2.compute.amazonaws.com] │
│  │ 🌐 Nextcloud Personal  │  │  Port:         [ 22                                   ] │
│  │ 📂 Legacy Archive FTP  │  │  Username:     [ ubuntu                               ] │
│  │                        │  │  Password:     [ ••••••••••••••••••                   ] │
│  │                        │  │  Remote Path:  [ /var/www/production                  ] │
│  │                        │  │  [✓] Remember password in macOS Keychain                │
│  └────────────────────────┘  │                                                         │
│  [➕ New] [⧉ Dup] [🗑 Del]    │  [🔍 Test Connection]          [💾 Save]  [🔗 Connect] │
└──────────────────────────────┴─────────────────────────────────────────────────────────┘
```

#### Gestione dei profili del server

- **Crea nuovo (`➕ New`)**: cancella il modulo a destra per definire una nuova configurazione del server. 
- **Duplica (`⧉ Duplicate`)**: clona il profilo di connessione selezionato. Ideale quando si gestiscono più ambienti (sviluppo, staging, produzione) su configurazioni host identiche. 
- **Elimina (`🗑 Delete`)**: rimuove il profilo di connessione ed elimina le credenziali associate dal portachiavi di sistema. 
- **Test connessione (`🔍 Test Connection`)**: invia un operatore in background (`ConnectionTestWorker`) per connettersi, autenticarsi e disconnettersi correttamente, verificando la reattività del server senza allontanarsi. 
- **Connetti (`🔗 Connect`)**: salva eventuali modifiche ai campi in sospeso, stabilisce la sessione remota e carica la directory remota in una nuova scheda del pannello attivo.

#### Menu Connessioni salvate dinamiche

Le connessioni salvate vengono automaticamente integrate nella barra dei menu in alto in **Rete ➔ Connessioni salvate**. Puoi montare qualsiasi server con segnalibro con un solo clic: 

- `Network ➔ Saved Connections ➔ 🔐 AWS Staging Server` 
- `Network ➔ Saved Connections ➔ 🖧 Synology Office NAS` 

---

## 8. Sicurezza delle credenziali e integrazione del portachiavi

I file di configurazione del file manager sono un obiettivo primario per il malware di raccolta delle credenziali. Molti file manager legacy memorizzano le password FTP/SFTP in file di configurazione XML o INI in testo semplice situati nella directory home dell'utente. 

**ATBCmder garantisce zero archiviazione di credenziali in chiaro.**

### 8.1 L'architettura di sicurezza

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           CREDENTIAL STORAGE ARCHITECTURE                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Connection Configuration XML                    Apple System Keychain                │
│   (~/.config/atbcmder/atbcmder.xml)               (service: "ATBCmder_VFS")            │
│   ┌─────────────────────────────────────┐         ┌──────────────────────────────────┐ │
│   │ <connection>                        │         │ Label: "AWS Staging Server"      │ │
│   │   <label>AWS Staging</label>        │         │ Key:   Encrypted Secret          │ │
│   │   <scheme>sftp</scheme>             │         │ Access: Controlled by macOS      │ │
│   │   <host>aws.infra.net</host>        │         │         Hardware Security Enclave│ │
│   │   <user>deploy</user>               │         └──────────────────────────────────┘ │
│   │   <password></password>             │                           ▲                  │
│   │ </connection>                       │                           │                  │
│   └─────────────────────────────────────┘                           │                  │
│         ▲                                                           │                  │
│         │ Password stripped on save                                 │ Stored via       │
│         └─────────────────── ConnectionManager ─────────────────────┘ Python keyring   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

1. **Scrubbing XML in chiaro**: ogni volta che i profili di connessione vengono serializzati sul disco (`atbcmder.xml`), la routine `ConnectionManager.save()` forza esplicitamente `d["password"] = ""` prima della scrittura. Anche se una parte non autorizzata controlla l'XML di configurazione, nessuna password del server verrà mai rivelata. 
2. **Crittografia portachiavi di sistema macOS**: quando la casella di controllo **Ricorda password** è selezionata, le password vengono salvate direttamente nel portachiavi macOS tramite l'API di sistema `keyring` con l'identificatore del servizio sicuro `ATBCmder_VFS`. La derivazione e l'archiviazione delle chiavi sono protette dall'hardware Secure Enclave di Apple. 
3. **Sessioni in memoria temporanee**: se "Ricorda password" è deselezionato, le credenziali vengono conservate rigorosamente nella memoria dinamica (`VFSSessionCache`) durante il ciclo di vita dell'applicazione corrente e vengono cancellate nel momento in cui ATBCmder termina. 

---

## 9. ⚡ Suggerimenti degli esperti: operazioni remote ad alte prestazioni

### Suggerimento 1: coda di trasferimento in background non bloccante (`cm_OperationsPanel`)

Quando copi directory di grandi dimensioni su server remoti o scarichi ISO multi-gigabyte su SFTP, non bloccare mai il tuo spazio di lavoro. Tutte le operazioni sui file di rete in ATBCmder si integrano automaticamente con la **Coda delle operazioni in background**: 

- Premi **`F5`** per avviare un trasferimento, quindi fai clic su **Sfondo** (o lascialo in coda automaticamente). 
- Apri il pannello delle operazioni tramite **Mostra ➔ Pannello delle operazioni** (`cm_OperationsPanel`) per monitorare i grafici della larghezza di banda in tempo reale, i conteggi di byte per file e le stime di trasferimento rimanenti. 
- Puoi mettere in pausa, riprendere o riordinare i trasferimenti di rete in coda continuando a sfogliare i file locali in entrambi i pannelli.

### Suggerimento 2: copiare in streaming su protocolli eterogenei

Il motore `stream_copy_file` di ATBCmder consente lo **streaming diretto da server a server**. Se trascini una cartella da un server SFTP nel pannello di sinistra a una condivisione di rete SMB nel pannello di destra: 

- ATBCmder **non** scarica l'intera directory sul disco rigido del tuo Mac locale prima di ricaricarla. 
- I dati vengono suddivisi in blocchi attraverso un anello buffer in memoria, trasmettendo byte dal socket di origine direttamente al socket di destinazione. Ciò elimina l'usura del disco locale e consente trasferimenti più grandi della capacità SSD locale disponibile.

### Suggerimento 3: mantenimento della rete attiva e prevenzione delle interruzioni della connessione

I firewall di rete con stato e i gateway NAT spesso interrompono le connessioni TCP inattive dopo 60-300 secondi di inattività. Per evitare sessioni disconnesse durante l'esplorazione di grandi alberi remoti: 

- Il livello `BaseNetworkVFS` di ATBCmder mantiene automaticamente gli heartbeat della sessione attraverso le connessioni inattive. 
- Se si verifica un'interruzione temporanea della rete, il meccanismo interno `_retry()` esegue fino a **3 tentativi** utilizzando il backoff esponenziale (intervalli di `2^attempt` secondi) prima di segnalare un errore di connessione.

### Suggerimento 4: modifica di file remoti con ciclo di vita di caricamento automatico

Hai bisogno di modificare uno script `nginx.conf` o Python direttamente su un server remoto? 

1. Evidenziare il file remoto nella visualizzazione del pannello SFTP o WebDAV. 
2. Premere **`F4`** (`Fn+F4`). 
3. ATBCmder scarica il file in un sandbox temporaneo isolato (`/tmp/`) e lo apre nell'editor integrato. 
4. Ogni volta che si preme **`Cmd+S`** (`⌘S`), ATBCmder attiva `_upload_vfs_temp()`, trasmettendo il file aggiornato al server remoto in modo asincrono e visualizzando una conferma nella barra di stato. 
5. Quando chiudi l'editor, il file temporaneo viene scollegato in modo sicuro da `/tmp/`. 

---

## 10. Avvisi di sistema e sicurezza

> [!WARNING] 
> **Mancata corrispondenza nella verifica della chiave host SSH** 
> Se un server SFTP rigenera le sue chiavi host (ad esempio, dopo una reinstallazione del sistema operativo) o se viene tentata un'intercettazione di rete man-in-the-middle, ATBCmder rileva che la chiave del server non corrisponde all'impronta digitale registrata in `~/.ssh/known_hosts`. 
> Non ignorare mai gli avvisi relativi alla chiave host su reti Wi-Fi pubbliche non attendibili senza verificare in modo indipendente l'impronta digitale della chiave pubblica del server con l'amministratore di sistema. 

> [!IMPORTANT] 
> **Spazio cache temporaneo per file remoti di grandi dimensioni** 
> Durante la visualizzazione (`F3`) o la modifica (`F4`) di file multi-gigabyte archiviati su server VFS remoti, ATBCmder trasmette l'elemento di destinazione al volume `/tmp` locale. Assicurati che il contenitore APFS primario del tuo Mac disponga di spazio di archiviazione libero sufficiente prima di aprire enormi file video o database remoti. 

> [!WARNING] 
> **Smontaggio delle condivisioni di rete remote** 
> Per le condivisioni SMB montate tramite macOS `mount_smbfs`, l'interruzione della connettività di rete senza disconnessione può lasciare handle di montaggio obsoleti in `/Volumes/`. Utilizzare sempre il menu dell'unità del pannello o l'azione di disconnessione prima di chiudere il laptop o cambiare rete Wi-Fi. 

---

## 11. Tabella di riferimento della tastiera master a doppia matrice

| Categoria | Azione Descrizione | Scorciatoia macOS | Chiave del comandante classico | ID comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Operazioni di archiviazione** | Comprimi file/cartelle selezionati | `Alt+F5` / `⌥F5` | `Alt+F5` | `cm_PackFiles` | 
| **Operazioni di archiviazione** | Estrai gli archivi selezionati | `Alt+F9` / `⌥F9` | `Alt+F9` | `cm_ExtractFiles` | 
| **Operazioni di archiviazione** | Sfoglia il contenitore dell'archivio interno| `Enter` / `⏎` | `Enter` | `cm_Open` | 
| **Operazioni di archiviazione** | Esci dall'archivio nella directory principale| `Backspace` / `⌫` | `Backspace` | `cm_ChangeDirToParent` | 
| **Operazioni di archiviazione** | Anteprima del file all'interno dell'archivio | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Operazioni di archiviazione** | Modifica file all'interno dell'archivio (Live)| `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Operazioni di archiviazione** | Estrai solo gli elementi selezionati | `F5` / `Fn+F5` | `F5` | `cm_Copy` | 
| **Operazioni di archiviazione** | Suddividi archivi di grandi dimensioni in volumi| `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Operazioni di archiviazione** | Riassemblare i pezzi del volume diviso | Menu: File ➔ Combina file | — | `cm_FileLinker` / `cm_Combine` | 
| **Connessioni di rete**| Finestra di dialogo Connessione rapida alla rete | Menù: Rete | — | `cm_NetworkConnect` | 
| **Connessioni di rete**| Gestisci connessioni di rete | Menù: Rete | — | `cm_ManageConnections` | 
| **Connessioni di rete**| Connessione rapida al server FTP | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_FTPConnect` | 
| **Connessioni di rete**| Disconnetti condivisione di rete remota| Menù: Rete | — | `cm_NetworkDisconnect` | 
| **Gestione dei trasferimenti**| Apri coda di trasferimento operazioni | Menù: Mostra | — | `cm_OperationsPanel` | 
| **Gestione dei trasferimenti**| Pausa/Riprendi coda attiva | `Space` (in coda)| `Space` | — |

--- 

<div align="center"> 
<p>Pronto a personalizzare i tasti di scelta rapida, le visualizzazioni dei pannelli e il comportamento dell'applicazione?</p> 
<p><strong><a href="preferences_and_customization.md">Procedi al capitolo 7: Preferenze e personalizzazione &rarr;</a></strong></p> 
</div>