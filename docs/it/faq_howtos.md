# Capitolo 9: Ricette pratiche e risoluzione dei problemi

Sebbene i file manager ortodossi a doppio pannello siano rinomati per la loro velocità pura e l'efficienza della tastiera, padroneggiare le attività del mondo reale spesso richiede la comprensione di come sottosistemi distinti, come la sincronizzazione delle directory, la ridenominazione di modelli batch, i file system virtuali remoti, il repacking degli archivi e la ricerca ricorsiva, lavorano insieme negli scenari quotidiani. Inoltre, operare all’interno dei moderni macOS introduce limiti di sicurezza, vincoli sandbox e intersezioni di scorciatoie di sistema che ogni utente incontra prima o poi. 

Questo capitolo è diviso in due sezioni generali: 

1. **Ricette pratiche per il mondo reale**: cinque procedure dettagliate complete che coprono flussi di lavoro di gestione dei file di alto valore con procedure dettagliate, rappresentazioni visive dell'interfaccia utente, scorciatoie da tastiera e suggerimenti per gli utenti esperti. 
2. **Guida alla risoluzione dei problemi e domande frequenti**: spiegazioni approfondite e risoluzioni diagnostiche per domande operative comuni, errori di autorizzazione, comportamenti di aggiornamento automatico, ripristini di configurazione, tasti funzione della tastiera Apple e meccanismi di trasferimento file tra volumi. 

---

## 1. Avvio rapido visivo: matrice per la risoluzione dei problemi quotidiani

La seguente matrice decisionale mappa gli obiettivi comuni di gestione dei file e le sfide tecniche direttamente sugli strumenti integrati e sugli identificatori di comando di ATBCmder: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              EVERYDAY TASK & DIAGNOSTIC ROUTER                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TASK / GOAL                               TOOL / METHOD            KEYSTROKE          │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Mirror local projects to backup       Directory Synchronizer   Shift+F12 (⇧F12)   │
│  [2] Reorganize photo libraries by date    Batch Multi-Rename Tool  Ctrl+M (⌃M)        │
│  [3] Mount home/office NAS or server       Network VFS Manager     cm_ManageConnections│
│  [4] Update config file in .zip archive    Archive VFS + Lister    Enter ➔ F4 ➔ Save   │
│  [5] Reclaim disk space from nested clutter Flat Branch View        Cmd+B (⌘B) / Alt+F7│
│                                                                                        │
│  ISSUE / SYMPTOM                           ROOT CAUSE              RESOLUTION          │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  "Operation not permitted" error           macOS Sandbox / TCC     cm_GrantAccess      │
│  Panels don't update external drives       FSEvents missing on FAT  attr_poll_interval │
│  Want to experiment without risk           Production XML safety    ATBCmder_test.sh   │
│  F-keys change brightness or volume        macOS hardware F-keys    Fn key or Settings │
│  Move takes long time across drives        Cross-volume Copy+Delete Verify free space  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Tabella di riferimento rapido a doppia matrice

| Azione/Diagnostica | Scorciatoia macOS | Chiave del comandante classico | ID comando | Scopo primario | 
| :--- | :--- | :--- | :--- | :--- | 
| **Sincronizzazione directory** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Confronta e sincronizza alberi di directory a doppio pannello. | 
| **Rinominazione multipla batch** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Rinomina più file utilizzando token, contatori e RegEx. | 
| **Connessioni di rete** | Menù: Rete | `cm_ManageConnections`| `cm_ManageConnections`| Gestisce i profili server SMB, SFTP, WebDAV e FTP salvati. | 
| **Connessione di rete rapida** | Menù: Rete | `cm_NetworkConnect` | `cm_NetworkConnect` | Finestra di dialogo di connessione ad hoc per server remoti. | 
| **Modifica sul posto dell'archivio** | `F4` / `Fn+F4` | `F4` | `cm_Edit` | Modifica il membro dell'archivio; attiva `RepackWorker` al salvataggio. | 
| **Vista ramo piatto** | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | Visualizza ricorsivamente tutti i file nidificati in un unico elenco semplice. | 
| **Ricerca avanzata** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` | Ricerca di file multi-filtro con output "Feed to Listbox". | 
| **Concedi l'accesso al filesystem**| Menu: File / Aiuto | — | `cm_GrantFilesystemAccess`| Avvia l'assistente per le autorizzazioni di macOS App Sandbox. | 
| **Aggiornamento manuale del pannello** | `Ctrl+R` / `⌃R` o `Cmd+R` / `⌘R` | `Ctrl+R` | `cm_Refresh` | Forza una rilettura immediata della directory dal disco. | 
| **Avvia terminale di sistema** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Genera macOS Terminale nel percorso corrente del pannello. | 
| **Calcola lo spazio della cartella** | `Alt+Shift+Enter` (`Space`) | `Alt+Shift+Enter` (`Space`) | `cm_CountDirContent` / `cm_CalculateSpace` | Calcola la dimensione in byte ricorsiva aggregata (`Space` per singolo, `Ctrl+L` per il totale selezionato). | 
| **Cancellazione sicura (distruggi)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Sovrascrittura multi-passaggio ed eliminazione permanente dei file. | 

---

## 2. Ricette pratiche nel mondo reale

### 2.1 Soluzione 1: confronto e sincronizzazione di due cartelle di backup

**Obiettivo**: garantire che un'unità di backup esterna o una cartella di rete contenga una replica esatta e aggiornata della directory del progetto attivo, con visibilità completa sui file aggiunti, modificati o eliminati prima di apportare modifiche. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figura 9.1: La finestra di dialogo Sincronizzazione delle directory che mostra confronti di directory affiancate, frecce di copia direzionali e opzioni di mirroring asimmetrico.*

#### Procedura passo dopo passo

1. **Allinea sorgente e destinazione nei doppi pannelli**: 
- Nel **pannello sinistro**, vai alla directory di lavoro locale principale (ad esempio, `~/Documents/Projects/AppAlpha`). 
- Premi **`Tab`** per passare al **pannello destro** e vai alla destinazione del backup di destinazione (ad esempio, `/Volumes/BackupDrive/Backups/AppAlpha`). 
2. **Avvia la sincronizzazione della directory**: 
- Premi **`Shift+F12`** (`⇧F12`) o seleziona **Comandi ➔ Sincronizza cartelle...** dalla barra dei menu. 
- La finestra di dialogo Sincronizza directory si apre con il Percorso sinistro e il Percorso destro popolati automaticamente. 
3. **Configura i parametri di confronto**: 
- Seleziona **Confronta sottodirectory** per attraversare ricorsivamente tutte le cartelle nidificate. 
- Seleziona **Confronta per contenuto** se hai bisogno di certezza crittografica (verifica dei byte dei file tramite `filecmp`) anziché fare affidamento esclusivamente sulle dimensioni dei file e sui timestamp di modifica. 
- Assicurati che la **Tolleranza timestamp FAT/SMB (2,0 sec)** sia abilitata se la destinazione del backup utilizza FAT32, exFAT o una condivisione di rete SMB, evitando falsi flag di mancata corrispondenza causati dall'arrotondamento del timestamp del file system di 2 secondi. 
4. **Avvia il confronto**: 
- Fai clic su **Confronta** (o premi `Alt+C` / `⌥C`). 
- ATBCmder esegue un operatore di confronto in background (`SyncCompareWorker`) e popola la tabella di confronto con indicatori di azione direzionale: 
* **`->` (da sinistra a destra)**: il file locale è più recente o esiste solo a sinistra. Azione: copia da sinistra a destra. 
* **`<-` (Right to Left)**: The backup file is newer, or only exists on the right. Action: copy right to left.
     * **`=` (Equal)**: Both files are identical in size and timestamp/content. These are hidden from the pending action list by default.
     * **`!=` (Conflict)**: Incompatible directory-versus-file collision or timestamp mismatch requiring manual inspection.
5. **Select Your Synchronization Strategy**:
   - **Two-Way Symmetric Sync (Default)**: Copies newer files in both directions (`->` e `<-`). No files are deleted on either side. Ideal for syncing collaborative folders between machines.
   - **Asymmetric Mirroring (`Asymmetric` Checkbox Enabled)**: Makes the Right directory an exact binary replica of the Left directory. Any file on the Right that does not exist on the Left is **permanently deleted from the backup target**.
6. **Review and Execute**:
   - Inspect the summary count at the bottom: *e.g., "Left to Right: 42 files (128.4 MB) | Right to Left: 0 files | Deletes: 3 files"*.
   - Click **Synchronize** to launch the non-blocking background transfer queue. Progress bars reflect active transfer volume and remaining item counts.

> [!ATTENZIONE] 
> **Pericolo di perdita di dati del mirroring asimmetrico**: 
> Quando è selezionata la modalità **Asimmetrica**, i file presenti sull'unità di destinazione che sono stati eliminati o rinominati nell'origine verranno **rimossi permanentemente** senza essere spostati nel Cestino di macOS. Rivedi sempre la tabella di confronto direzionale prima di fare clic su Sincronizza! 

> [!CONSIGLIO] 
> **⚡ Suggerimento professionale: verifica a livello di contenuto per contenuti multimediali e codice**: 
> Quando si esegue il backup di riprese video o repository Git, le dimensioni dei file potrebbero corrispondere mentre esistono sottili corruzioni interne dei byte. Controlla sempre **Confronta per contenuto** per gli archivi mission-critical. Sebbene il confronto byte per byte richieda più tempo su USB o Wi-Fi, garantisce l'integrità dei dati al 100%. 

---

### 2.2 Soluzione 2: rinominare in batch le foto della fotocamera con date e numeri di sequenza

**Obiettivo**: trasformare centinaia di file di telecamere non organizzati (ad esempio, `DSC_0012.JPG`, `DSC_0013.JPG`, `IMG_4901.CR3`) in nomi di file puliti e ordinabili come `2026-09-06_Vacation_001.jpg` con contatori di sequenza con riempimento zero e anteprime di sicurezza in tempo reale. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figura 9.2: Lo strumento Batch Multi-Rename con righe di anteprima in tempo reale, token di metadati, controlli del contatore numerico e rilevamento delle collisioni.*

#### Procedura passo dopo passo

1. **Seleziona le foto**: 
- Naviga nella directory di importazione della fotocamera nel pannello attivo. 
- Seleziona tutte le foto utilizzando **`Cmd+A`** (`⌘A`) oppure premi **`+`** sulla tastiera per inserire una maschera con caratteri jolly come `*.jpg;*.jpeg;*.cr3;*.arw`. 
2. **Avvia lo strumento di ridenominazione multipla batch**: 
- Premi **`Ctrl+M`** (`⌃M`) o **`Cmd+M`** (`⌘M`), oppure scegli **File ➔ Strumento di ridenominazione multipla...** dalla barra dei menu. 
3. **Definisci la maschera del nome file**: 
- Nel campo **Maschera nome file**, inserisci la struttura desiderata utilizzando i token di metadati: 
     ```
     [Y]-[M]-[D]_Vacation_[C]
     ```


- **Spiegazione del token**: 
* `[Y]`: Anno di modifica del file a 4 cifre (ad esempio, `2026`). 
* `[M]`: mese a 2 cifre (ad esempio, `09`). 
* `[D]`: giorno a 2 cifre (ad esempio, `06`). 
* `Vacation`: Testo descrittivo statico. 
* `[C]`: Contatore numerico sequenziale. 
4. **Configura la sequenza dei contatori**: 
- Nella scheda **Impostazioni contatore**: 
* **Inizio alle**: `1` 
* **Passaggio**: `1` 
* **Cifre**: `3` (applica il riempimento zero: `001`, `002`, `003`... fino a `999`). 
5. **Elimina i prefissi della fotocamera con Trova e sostituisci (opzionale)**: 
- Se desideri preservare parte del nome file originale senza il prefisso della fotocamera (ad esempio, mantenendo il numero di sequenza della fotocamera da `DSC_8941.JPG`): 
* Imposta **Maschera nome file** su: `[YMD]_[N5-]` 
* `[N5-]` estrae i caratteri dall'indice 5 alla fine del nome, eliminando completamente `DSC_`. 
- In alternativa, utilizza i campi **Cerca e sostituisci**: 
* **Trova**: `DSC_` 
* **Sostituisci**: `Photo_` 
* Seleziona **RegEx** se utilizzi modelli di espressione complessi come `^IMG_(\d+)`. 
6. **Ispeziona la tabella di anteprima dal vivo**: 
- La tabella a 3 colonne (`Old Name`, `New Name`, `Directory`) si aggiorna istantaneamente ad ogni pressione di un tasto. 
- Controlla la colonna **Stato**: ATBCmder evidenzia i nomi di destinazione duplicati in grassetto rosso con un indicatore di collisione, impedendo sovrascritture accidentali. 
7. **Esegui la ridenominazione**: 
- Premi **`Enter`** o fai clic su **Avvia rinomina**. ATBCmder esegue le ridenominazioni atomicamente sul disco e aggiorna la visualizzazione del pannello. 

> [!NOTA] 
> **Sicurezza dell'estensione**: 
> Per impostazione predefinita, la **Maschera estensione** è impostata su `[E]`, preservando l'estensione del file originale senza modifiche. Non eliminare mai `[E]` a meno che tu non intenda esplicitamente rimuovere le estensioni dai tuoi file.

> [!CONSIGLIO] 
> **⚡ Suggerimento professionale: flusso di lavoro dell'editor esterno (`⌘I`)**: 
> Se disponi di un elenco irregolare di nomi di clienti o titoli di tracce, premi **`Cmd+I`** (`⌘I` / Modifica nell'editor esterno) all'interno dello strumento Rinomina multipla. ATBCmder esporta i nomi di destinazione nel tuo editor di testo predefinito. Modifica l'elenco in Vim, VS Code o TextEdit, salva il documento e ATBCmder importa immediatamente i nomi modificati nella griglia di anteprima. 

---

### 2.3 Soluzione 3: connessione a un NAS domestico/ufficio tramite SMB, SFTP o WebDAV

**Obiettivo**: montare uno storage pool TrueNAS o Synology in sede, un server AWS EC2 Linux o un repository cloud Nextcloud WebDAV in una scheda a doppio pannello senza destreggiarsi tra comandi terminali separati o fogli di connessione del Finder. 

![Remote VFS Connection](images/smb_sftp_ftp_remote_access.png) 
*Figura 9.3: Configurazione di condivisioni di rete remote sicure tra protocolli SMB, SFTP e WebDAV.*

#### Procedura passo dopo passo

1. **Apri Gestione connessione di rete**: 
- Scegli **Rete ➔ Gestisci connessioni di rete...** dalla barra dei menu nativa o esegui il comando **`cm_ManageConnections`**. 
2. **Crea un nuovo profilo di connessione**: 
- Clicca sul pulsante **`➕ New`** in basso a sinistra. 
- Nel campo **Etichetta**, inserisci un identificatore riconoscibile (ad esempio, `Synology Office NAS` o `AWS Production Web`). 
3. **Configura protocollo e dettagli host**: 
- **Protocollo**: seleziona il protocollo di destinazione dal menu a discesa: 
* **SMB/CIFS**: Porta `445` (standard per Synology, QNAP, Windows Server, TrueNAS). 
* **SFTP (trasferimento file SSH)**: porta `22` (standard per istanze cloud Linux/UNIX). 
* **WebDAV / WebDAVS**: Porta `80` o `443` (standard per Nextcloud, ownCloud). 
* **FTP/FTPS**: Porta `21` o `990` (host di file legacy). 
- **Host**: inserisci l'indirizzo IP o il nome del dominio (ad esempio, `192.168.1.100` o `sftp.mycompany.com`). 
- **Porta**: impostata automaticamente quando viene scelto il protocollo; modificalo se il tuo server utilizza una porta non standard. 
- **Nome utente**: inserisci il nome utente dell'account del sistema remoto. 
- **Percorso remoto**: imposta la directory di destinazione predefinita (ad esempio, `/volume1/Media` o `/var/www/html`). 
4. **Archiviazione sicura delle credenziali**: 
- Inserisci la tua password o passkey. 
- Seleziona **Ricorda la password nel portachiavi macOS**. 
- **Garanzia di sicurezza**: ATBCmder non memorizza mai le credenziali in testo normale nei file di configurazione XML. Tutti i segreti sono sigillati crittograficamente all'interno del portachiavi Apple nativo (`com.aitobox.atbcmder.vfs`). 
5. **Testare la connessione**: 
- Fare clic su **`🔍 Test Connection`**. 
- ATBCmder invia un operatore in background (`ConnectionTestWorker`) che convalida la raggiungibilità della rete, verifica le chiavi host SSH o i certificati TLS, controlla le credenziali e visualizza un avviso di operazione riuscita senza chiudere la finestra di dialogo. 
6. **Connetti e naviga**: 
- Fare clic su **`🔗 Connect`** (o premere `Enter`). 
- Nel pannello attivo si apre una nuova scheda cartella, che visualizza il percorso remoto formattato come URI VFS unificato: 
     ```
     vfs://smb://admin@192.168.1.100/volume1/Media/
     vfs://sftp://ubuntu@aws.prod.internal:22/var/www/html/
     ```


- Ora puoi sfogliare, cercare, copiare (`F5`), spostare (`F6`) ed eliminare (`F8`) file su dischi locali e server remoti con la stessa agilità del doppio pannello. 
7. **Riconnessione rapida dalla barra dei menu**: 
- Tutti i profili salvati vengono visualizzati automaticamente in **Rete ➔ Connessioni salvate**. Basta fare clic su qualsiasi server salvato per montarlo immediatamente. 

> [!CONSIGLIO] 
> **⚡ Suggerimento professionale: autenticazione basata su chiave SSH per SFTP**: 
> Per l'accesso automatizzato al server cloud, configurare l'autenticazione con chiave pubblica. Nel tuo profilo di connessione SFTP, lascia vuoto il campo della password e punta alla tua chiave privata locale (ad esempio, `~/.ssh/id_ed25519`). Se la chiave è protetta da una passphrase, ATBCmder la richiede una volta e la salva in modo sicuro nel portachiavi macOS. 

---

### 2.4 Soluzione 4: modificare un file direttamente all'interno di un archivio senza estrarlo

**Obiettivo**: modificare un file di configurazione annidato (`settings.json` o `config.yaml`) all'interno di un archivio multi-gigabyte `.zip`, `.tar.gz` o `.7z` su storage locale o su un server remoto senza decomprimere l'intero archivio in il tuo disco rigido. 

![Archive VFS](images/archive_vfs.png) 
*Figura 9.4: Navigazione e modifica all'interno di archivi compressi tramite il filesystem virtuale `vfs://` unificato.*

#### Procedura passo dopo passo

1. **Inserisci l'archivio come directory virtuale**: 
- Evidenziare il file di archivio (ad esempio, `production_backup.zip`) nel pannello attivo. 
- Premi **`Enter`** (o fai doppio clic). 
- ATBCmder intercetta la navigazione e monta l'archivio come filesystem virtuale: 
     ```
     vfs:///Users/brain/Downloads/production_backup.zip/
     ```
 

2. **Vai al file di destinazione**: 
- Sfoglia le directory virtuali nidificate (`etc`, `nginx`, `conf.d`) proprio come faresti su un volume fisico. 
- Individua il file che desideri aggiornare (ad esempio, `nginx.conf` o `app_settings.json`). 
3. **Apri nell'editor di testo integrato**: 
- Premere **`F4`** (`Fn+F4` / `cm_Edit`). 
- ATBCmder trasmette il membro compresso in un buffer temporaneo isolato e lo apre direttamente nell'editor di testo con sintassi evidenziata. 
4. **Apporta modifiche e salva**: 
- Apportare le modifiche di configurazione richieste. 
- Premere **`Cmd+S`** (`⌘S`) per salvare il buffer. 
5. **Ciclo di vita del reimballaggio automatico (`RepackWorker`)**: 
- Quando salvi o chiudi l'editor, il motore di repack in background di ATBCmder (`RepackWorker`) si attiva automaticamente: 
1. Calcola il delta tra il membro compresso originale e il buffer modificato. 
2. Controlla la dimensione complessiva dell'archivio rispetto alla soglia di avviso configurata (`ArchiveRepackWarningMB`). 
3. Ricomprime il file modificato e ricostruisce la struttura dell'archivio in un file temporaneo. 
4. Sostituisce atomicamente il file di archivio originale sul disco, garantendo che non si verifichi alcun danneggiamento se il sistema perde potenza durante la scrittura. 
5. La visualizzazione del pannello attivo si aggiorna automaticamente per visualizzare le dimensioni in byte e i timestamp aggiornati dei membri.

> [!IMPORTANTE] 
> **Protezione reimballaggio archivio grande (`ArchiveRepackWarningMB`)**: 
> L'aggiornamento di un singolo file di testo da 2 KB all'interno di un archivio da 15 GB richiede la riscrittura dell'intero file di archivio su disco. Per evitare picchi imprevisti della CPU e usura dell'SSD, ATBCmder controlla la dimensione dell'archivio. Se l'archivio supera `ArchiveRepackWarningMB` (impostazione predefinita: 500 MB), viene visualizzata una finestra di dialogo di avviso: *"Questo archivio è di 1,4 GB. La ricompressione riscriverà l'intero file. Vuoi continuare?"* È possibile personalizzare questa soglia in **Configurazione ➔ Opzioni ➔ Archivi**. 

---

### 2.5 Soluzione 5: ricerca ed eliminazione di file di grandi dimensioni in directory nidificate

**Obiettivo**: recuperare preziosa capacità SSD individuando rapidamente e rimuovendo in modo sicuro rendering video 4K abbandonati, cartelle `node_modules` gonfie, immagini di dischi virtuali Docker o programmi di installazione DMG obsoleti sparsi all'interno di strutture di directory multilivello. 

![Flat Branch View](images/branch_view.png) 
*Figura 9.5: Vista ramo piatto (`Cmd+B`) che mostra contenuti profondamente annidati in un'unica tabella appiattita per l'ordinamento istantaneo delle dimensioni.*

#### Metodo A: appiattimento istantaneo tramite vista ramo piatto (`Cmd+B`)

1. **Vai alla cartella principale principale**: 
- Evidenzia la cartella principale di livello superiore che desideri controllare (ad esempio, `~/Projects` o `~/Downloads`). 
2. **Attiva vista ramo piatto**: 
- Premi **`Cmd+B`** (`⌘B`) o **`Ctrl+B`** (`cm_FlatView`), oppure seleziona **Mostra ➔ Vista ramo (Vista piatta)**. 
- ATBCmder esegue la scansione ricorsiva di tutte le sottodirectory e visualizza ogni file nidificato in un **singolo elenco piatto**, eliminando i confini delle cartelle delle directory. 
3. **Ordina per dimensione decrescente**: 
- Fai clic sull'intestazione della colonna **Dimensione** o premi **`Ctrl+F6`** (`cm_SortBySize`) per ordinare i file più grandi in alto. 
- File ISO giganti, dump di database e immagini di macchine virtuali vengono immediatamente visualizzati nella parte superiore del pannello. 
4. **Calcola lo spazio della directory**: 
- Per le sottocartelle visibili nelle visualizzazioni standard, posiziona il cursore su qualsiasi cartella e premi **`Space`** (`␣` / `cm_CalculateSpace`). ATBCmder calcola l'impronta di byte ricorsiva totale e la visualizza al posto dell'etichetta `<DIR>` predefinita. 
5. **Esci dalla vista ramo**: 
- Premere di nuovo **`Cmd+B`** oppure premere `Esc` / `Backspace` su `..` per tornare alla normale navigazione gerarchica delle directory. 

---

#### Metodo B: filtraggio mirato tramite ricerca avanzata (`Alt+F7`) e "Inserisci nella casella di riepilogo"

![Advanced Search](images/advanced_search_dialog.png) 
*Figura 9.6: Finestra di dialogo Ricerca avanzata con criteri di filtro delle dimensioni e pulsante "Inserisci nella casella di riepilogo".* 

1. **Avvia la ricerca avanzata**: 
- Premi **`Alt+F7`** (`⌥F7`) o seleziona **Comandi ➔ Cerca...**. 
2. **Definisci filtri per dimensioni e tipo**: 
- Nel campo **Cerca in**, conferma la tua directory principale. 
- Controlla il filtro **Taglia**: seleziona **`>`** e inserisci `100` con unità **`MB`** (o `1` **`GB`**). 
- Nel campo **Maschera file**, specifica le estensioni di destinazione (ad esempio, `*.dmg;*.iso;*.mp4;*.mov;*.zip`) o lascia come `*` per trovare eventuali elementi gonfiati. 
- Nella scheda **Data**, facoltativamente limita i risultati ai file non modificati negli ultimi 180 giorni. 
3. **Esegui la ricerca**: 
- Fai clic su **Avvia ricerca**. 
4. **Inserisci i risultati in una scheda del pannello virtuale ("Inserisci nella casella di riepilogo")**: 
- Una volta compilati i risultati, fai clic sul pulsante **Inserisci nella casella di riepilogo**. 
- L'intero set di risultati della ricerca viene trasferito in una **scheda virtuale dedicata** nel pannello attivo. 
- A differenza di una finestra di dialogo modale statica, i file in questa scheda si comportano come normali elementi del pannello file: puoi visualizzarli in anteprima con Visualizzazione rapida (`Ctrl+Q` / `⌘Q`), esaminarli in Universal Lister (`F3`) o contrassegnare più file con `Insert` / `Space`. 
5. **Rivedi ed elimina**: 
- Seleziona i file indesiderati e premi **`F8`** (`Fn+F8` / `cm_Delete`) per spostarli in modo sicuro nel Cestino di macOS. 
- Se hai bisogno della cancellazione permanente e irrecuperabile dei dati (ad esempio, cancellazione dei dati riservati del cliente), premi **`Alt+Delete`** (`⌥⌫` / `cm_Wipe`) per attivare la distruzione sicura dei file a più passaggi. 

> [!CONSIGLIO] 
> **⚡ Suggerimento professionale: identificare file duplicati identici tramite checksum**: 
> Se sospetti che più file di grandi dimensioni siano duplicati esatti, selezionali e premi **`Ctrl+X`** (`⌃X` / `cm_CheckSumCalc`). Scegli **SHA-256** e fai clic su Calcola. I digest di hash corrispondenti confermano i duplicati binari al 100%, consentendoti di eliminare le copie superflue in totale sicurezza. 

---

## 3. Guida alla risoluzione dei problemi e domande frequenti (FAQ)

### 3.1 Errori "Operazione non consentita"/Autorizzazione negata su macOS

#### Causa ultima

Nei moderni macOS (da macOS 12 Monterey a macOS 15 Sequoia), Apple applica rigidi limiti di privacy **App Sandbox** e **TCC (Trasparenza, consenso e controllo)**. Le applicazioni in modalità sandbox non possono accedere a unità esterne, cartelle di sistema o anche directory utente standard (`~/Documents`, `~/Downloads`, `~/Desktop`) senza un token di autorizzazione crittografica esplicito concesso dall'utente noto come **Segnalibro con ambito di sicurezza**. 

Se ad ATBCmder non è stato concesso l'accesso al filesystem, potresti riscontrare: 

- Finestre di dialogo per le operazioni sui file visualizzate: `"Error: Operation not permitted"`. 
- Le directory appaiono vuote anche se i file esistono nel Finder. 
- Unità USB o Thunderbolt esterne in `/Volumes` che mostrano errori di accesso negato.

#### Soluzione 1: utilizzare l'assistente onboarding sandbox dell'app (`cm_GrantFilesystemAccess`)

ATBCmder include un assistente di onboarding integrato progettato per registrare segnalibri di sicurezza persistenti con macOS: 

```
┌─────────────────────────────────────────────────────────────┐
│  Grant Filesystem Access                                [x] │
├─────────────────────────────────────────────────────────────┤
│  Because this version of ATBCmder runs inside a secure      │
│  macOS Sandbox, it needs your permission to access          │
│  critical folders.                                          │
│                                                             │
│  [  Grant Access to Root Directory (/)  ]                   │
│                                                             │
│  [  Grant Access to External Disks (/Volumes)  ]            │
│                                                             │
│  [  Open Full Disk Access Settings…  ]                      │
│                                                             │
│  Root directory access is required by the App Sandbox.      │
│  Full Disk Access is a separate macOS permission for        │
│  protected user data.                                       │
│                                                   [ Done ]  │
└─────────────────────────────────────────────────────────────┘
```
 

1. Dalla barra dei menu, selezionare **File** (o **Guida**) ➔ **Concedi accesso al filesystem…** o attivare il comando **`cm_GrantFilesystemAccess`**. 
2. Fare clic su **"Concedi l'accesso alla directory principale (/)"**. 
* Quando viene visualizzato il foglio nativo Apple `NSOpenPanel` che punta a `Macintosh HD` (`/`), fare clic su **Concedi accesso** (o **Apri**). 
* **Perché funziona**: l'autorizzazione di `/` genera un segnalibro root con ambito di sicurezza archiviato in `sandbox_bookmarks.plist`. Poiché i percorsi secondari ereditano i token di sicurezza verso il basso, la concessione dell'accesso a `/` sblocca permanentemente tutte le cartelle utente standard (`~/Documents`, `~/Downloads`, `/Applications`, `~/Projects`). 
3. Fare clic su **"Concedi l'accesso ai dischi esterni (/Volumi)"**. 
* Nel foglio aperto, fai clic su **Concedi accesso** per `/Volumes`. 
* Ciò autorizza tutte le unità flash USB, gli SSD esterni, le schede SD, le immagini disco (DMG) e i supporti SMB di rete collegati. 
4. Fare clic su **Fine**. Le tue autorizzazioni vengono salvate in modo permanente al riavvio dell'applicazione.

#### Soluzione 2: concedere l'accesso completo al disco (FDA) nelle Impostazioni di sistema macOS

Se devi gestire posizioni di sistema protette, come `~/Library/Mail`, `~/Library/Messages`, cache di navigazione di Safari o alberi di backup di Time Machine, macOS TCC richiede un diritto aggiuntivo a livello di sistema: 

1. Apri **Impostazioni di sistema** (menu Apple  ➔ Impostazioni di sistema). 
2. Passare a **Privacy e sicurezza ➔ Accesso completo al disco**. 
3. Individua **ATBCmder** nell'elenco delle applicazioni e sposta l'interruttore su **On**. 
4. Se ATBCmder non è elencato: 
* Fai clic sul pulsante **`+`** in basso. 
* Autenticati con la password del tuo Mac o Touch ID. 
* Seleziona `/Applications/ATBCmder.app` e fai clic su **Apri**. 
5. Quando viene richiesto di riavviare l'applicazione, fare clic su **Esci e riapri**.

#### Soluzione 3: reimpostazione delle autorizzazioni sulla privacy TCC danneggiate tramite terminale

Se le autorizzazioni vengono danneggiate dopo un aggiornamento del sistema operativo macOS o un evento di nuova firma dell'applicazione, reimpostare il database TCC utilizzando lo strumento da riga di comando `tccutil` di macOS: 

```bash
# Reset all Full Disk Access permissions for ATBCmder
tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder

# Reset Desktop, Documents, and Downloads folder permissions
tccutil reset SystemPolicyDocumentsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDownloadsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDesktopFolder com.aitobox.atbcmder
```
 

Dopo aver eseguito questi comandi, riavvia ATBCmder ed esegui nuovamente **`cm_GrantFilesystemAccess`**. 

---

### 3.2 L'aggiornamento automatico non rileva le modifiche ai file sul disco

#### Causa ultima

ATBCmder utilizza un motore di monitoraggio dei file a più livelli: 

1. **Kernel `FSEvents`**: sui volumi nativi Apple APFS e HFS+, il kernel macOS emette eventi istantanei di mutazione della directory quando i file vengono aggiunti, modificati o eliminati da strumenti esterni. 
2. **Limitazioni del file system**: file system non Apple (ad esempio, chiavette USB esterne formattate come **FAT32** o **exFAT**) e montaggi di rete remoti (**SMB**, **NFS**, **SFTP**, **WebDAV**) **non supportano le notifiche del kernel `FSEvents`**. Quando un'app di terze parti crea o elimina un file su una condivisione SMB, il kernel macOS riceve zero eventi di notifica.

#### Passaggi di risoluzione

1. **Regolare l'intervallo di fallback del polling (`attr_poll_interval`)**: 
- Apri Preferenze tramite **`Cmd+,`** (`⌘,`) o **Configurazione ➔ Opzioni...**. 
- Vai alla pagina **Aggiornamento automatico**. 
- Verificare che **Visualizza modifica nome file** e **Visualizza modifica attributi** siano abilitati. 
- Modifica l'**Intervallo di polling (`attr_poll_interval`)**: 
* Predefinito: `5 seconds`. 
* Per test locali rapidi o sviluppo di rete attivo: diminuire a `1` o `2 seconds`. 
* Per condivisioni Wi-Fi a latenza elevata: aumentare a `10` o `15 seconds` per ridurre al minimo il sovraccarico della rete. 
2. **Controlla l'elenco delle directory escluse**: 
- Nella stessa pagina delle preferenze di **Aggiornamento automatico**, esamina la tabella **Directory escluse**. 
- Se il tuo percorso attivo (o una cartella principale) è stato aggiunto all'elenco di esclusione, ATBCmder sopprimerà deliberatamente il monitoraggio dei file per conservare i cicli della CPU. Rimuovi il percorso se desideri riattivare il monitoraggio. 
3. **Verifica le impostazioni di aggiornamento in background**: 
- Se i pannelli dei file non si aggiornano solo quando ATBCmder è ridotto a icona o dietro altre finestre, seleziona l'opzione: 
`[ ] Disable auto-refresh when ATBCmder is in the background` 

- Deseleziona questa opzione se desideri che ATBCmder rifletta continuamente gli output di build in background e i download esterni. 
4. **Forza un aggiornamento manuale immediato**: 
- In qualsiasi momento, premere **`Ctrl+R`** (`⌃R`) o **`Cmd+R`** (`⌘R`) (`cm_Refresh`). 
- Questo ignora tutti i livelli di memorizzazione nella cache, svuota i modelli di directory interni e rilegge immediatamente il contenuto della directory dal controller di archiviazione. 

---

### 3.3 Ripristino sicuro della configurazione o test in modalità test isolato

#### Testare nuove configurazioni in sicurezza con `scripts/ATBCmder_test.sh`

Quando provi layout sperimentali di scorciatoie da tastiera, nuovi temi di colore o comandi di scripting automatizzati, dovresti evitare di modificare il codice XML della configurazione di produzione. 

ATBCmder fornisce uno script di avvio del test in modalità sandbox: 
```bash
# Run ATBCmder in an isolated test environment
./scripts/ATBCmder_test.sh
```
 

**Come funziona**: 

1. Lo script crea una directory temporanea dedicata: `tests/.test_config/`. 
2. Copia la configurazione del test di base pulito (`src/atbcmder/resources/test_config.xml`) in `tests/.test_config/atbcmder.xml`. 
3. Esporta la variabile d'ambiente: 
   ```bash
   export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"
   ```
 

4. Una volta avviato, ATBCmder legge tutte le impostazioni esclusivamente da questa cartella di test. Eventuali modifiche, modifiche alle schede o esperimenti con i tasti di scelta rapida sono contenuti interamente in `tests/.test_config/`, lasciando le tue preferenze personali completamente intatte.

#### Ripristino della configurazione predefinita di fabbrica

Se la configurazione di produzione viene danneggiata o desideri iniziare da zero: 

1. **Esci completamente da ATBCmder** (**`Cmd+Q`** / `⌘Q`). 
2. Apri macOS Terminale e individua la directory di configurazione: 
* Installazione standard: `~/Library/Preferenze/atbcmder/` 
* Fallback Linux/XDG: `~/.config/atbcmder/` 
3. Eseguire il backup o rimuovere i file di configurazione attivi: 
   ```bash
   # Move configuration files to a backup location
   mv ~/Library/Preferences/atbcmder/atbcmder.xml ~/Library/Preferences/atbcmder/atbcmder.xml.bak
   mv ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml.bak
   ```
 

4. Riavviare ATBCmder. 
5. All'avvio, ATBCmder rileva i file di configurazione mancanti e rigenera automaticamente configurazioni XML pulite e convalidate popolate con le impostazioni predefinite ufficiali di fabbrica.

#### Esportazione e importazione di configurazioni portatili

Per migrare la tua configurazione su più Mac o creare un backup esterno: 

- **Esporta**: scegli **Configurazione ➔ Esporta configurazione...** (comando **`cm_ExportConfiguration`**) per salvare un'istantanea consolidata `.zip` o `.xml` contenente i tasti di scelta rapida, le colonne, le schede preferite e le tavolozze dei colori. 
- **Importa**: scegli **Configurazione ➔ Importa configurazione...** (comando **`cm_ImportConfiguration`**) sul tuo computer di destinazione per ripristinare immediatamente le impostazioni. 

---

### 3.4 Tasti funzione che attivano la luminosità/volume di macOS invece dei comandi

#### Causa ultima

Per impostazione predefinita, le tastiere Apple (tastiere integrate nei MacBook, tastiere Magic) assegnano funzioni hardware speciali alla fila di tasti superiore: 

- `F1` / `F2`: luminosità del display giù/su 
- `F3`: Controllo missione 
- `F4`: Spotlight / Launchpad 
- `F7` / `F8` / `F9`: controlli di riproduzione multimediale (riavvolgimento, riproduzione/pausa, avanzamento veloce) 
- `F10` / `F11` / `F12`: disattivazione audio, volume giù, volume su 

Quando premi `F5` sperando di copiare un file, macOS intercetta la sequenza di tasti e non fa nulla (o regola l'illuminazione della tastiera).

#### Soluzione 1: utilizzare il modificatore `Fn`

Tieni premuto il tasto **`Fn`** (Funzione) o **Globo (`🌐`)** nell'angolo in basso a sinistra della tastiera mentre premi il tasto funzione: 

- **`Fn+F3`**: Lister universale (`cm_View`) 
- **`Fn+F4`**: Editor di testo (`cm_Edit`) 
- **`Fn+F5`**: Copia file (`cm_Copy`) 
- **`Fn+F6`**: sposta/rinomina file (`cm_Rename`) 
- **`Fn+F7`**: Crea nuova cartella (`cm_MakeDir`) 
- **`Fn+F8`**: Elimina nel cestino (`cm_Delete`) 
- **`Fn+Shift+F12`**: Sincronizza directory (`cm_SyncDirs`)

#### Soluzione 2: abilita i tasti funzione standard a livello di sistema nelle impostazioni di macOS

Se utilizzi ATBCmder regolarmente, la configurazione consigliata di macOS per trattare i tasti funzione come tasti `F1`-`F12` standard è: 

1. Apri **Impostazioni di sistema** (menu Apple  ➔ Impostazioni di sistema). 
2. Seleziona **Tastiera** nella barra laterale sinistra. 
3. Fare clic sul pulsante **Scorciatoie da tastiera...**. 
4. Selezionare **Tasti funzione** nell'elenco a sinistra della scheda modale. 
5. Attiva l'interruttore a levetta: 
**"Utilizza i tasti F1, F2, ecc. come tasti funzione standard"** 

6. Fare clic su **Fine**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Keyboard Shortcuts                                         │
├──────────────────────────────┬──────────────────────────────┤
│  Keyboard Navigation         │  Use F1, F2, etc. keys as    │
│  Modifier Keys               │  standard function keys  [ON]│
│  Function Keys          ◄─── │                              │
│  Spotlight                   │  When this option is on,     │
│  Mission Control             │  press the Fn key to use the │
│  App Shortcuts               │  special features printed    │
│                              │  on each key.                │
│                              │                     [ Done ] │
└──────────────────────────────┴──────────────────────────────┘
```
 

*Risultato*: premendo `F5` ora si attiva direttamente la copia in ATBCmder. Per regolare la luminosità o il volume, tieni premuto `Fn` mentre premi il tasto.

#### Soluzione 3: utilizzare gli equivalenti chiave `Cmd` macOS nativi

Se preferisci non modificare le impostazioni della tastiera di sistema, ATBCmder fornisce scorciatoie da tastiera native di macOS per ogni operazione principale: 

- **Copia**: `Cmd+C` / `Cmd+V` (o standard `F5`) 
- **Sposta**: `Cmd+C` ➔ `Cmd+Option+V` (`⌥⌘V` sposta incolla) 
- **Elimina**: `Cmd+Delete` (`⌘⌫`) 
- **Nuova cartella**: `Shift+Cmd+N` (`⇧⌘N`) 
- **Rinomina**: `F2` o `Return` 
- **Rinominazione multipla batch**: `Ctrl+M` (`⌃M`) o `Cmd+M` (`⌘M`) 
- **Preferenze**: `Cmd+,` (`⌘,`) 
- **Chiudi scheda**: `Cmd+W` (`⌘W`) 

---

### 3.5 Spostamento di file su unità diverse rispetto alla stessa unità

Una domanda frequente da parte degli utenti è perché lo spostamento di un file da 20 GB all'interno della stessa cartella richiede una frazione di secondo, mentre lo spostamento dello stesso file su un'unità esterna o su una condivisione di rete richiede diversi minuti.

#### Spostamento all'interno del volume (stessa unità/partizione APFS)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              INTRA-VOLUME MOVE (SAME PARTITION)                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso   ➔ Target: /Users/brain/Movies/          │
│                                                                                        │
│   1. POSIX rename() system call updates filesystem inode directory table.              │
│   2. Physical data blocks on the SSD are NEVER touched or copied.                      │
│   3. Execution time: < 5 milliseconds. Free disk space required: 0 bytes.              │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Quando i percorsi di origine e destinazione risiedono sullo **stesso volume fisico del filesystem**, ATBCmder emette una chiamata di sistema POSIX atomica `rename()`. Il sistema operativo aggiorna semplicemente le voci dei puntatori nel catalogo di directory del filesystem. I cluster di dati fisici sul tuo SSD non si spostano.

#### Spostamento di più volumi (diverse unità/partizioni/montaggi di rete)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              CROSS-VOLUME MOVE (ACROSS DRIVES)                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso   ➔ Target: /Volumes/ExternalSSD/Movie/   │
│                                                                                        │
│   Stage 1: Binary Stream Copy (Read from Source SSD ➔ Write to Target External SSD)    │
│   Stage 2: Verification and Flush (fsync ensures complete write to external media)     │
│   Stage 3: Source Deletion (Source file is unlinked only after Stage 2 succeeds)       │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Durante il trasferimento oltre i diversi limiti del file system (ad esempio, dall'SSD interno del Mac a un'unità USB esterna, una condivisione SMB di rete o un'immagine disco), un aggiornamento del puntatore atomico è fisicamente impossibile. ATBCmder esegue una pipeline a più fasi **Copia-Verifica-Elimina**: 

1. **Lettura/scrittura flusso binario**: i dati vengono trasmessi in blocchi dal controller di archiviazione di origine attraverso la memoria di sistema e scritti nel controller di archiviazione di destinazione. La durata del trasferimento dipende interamente dalla velocità del bus fisico (ad esempio, USB 3.0 a ~100 MB/s contro Thunderbolt 4 a ~2.800 MB/s). 
2. **Buffer Flush e verifica**: ATBCmder chiama `fsync()` sull'handle del file di destinazione per garantire che tutti i dati memorizzati nella cache siano stati scritti sul supporto fisico e controlla l'equivalenza del conteggio dei byte. 
3. **Eliminazione sicura dell'origine**: solo dopo che il file di destinazione è stato completamente scritto e verificato, ATBCmder elimina il file di origine dal disco originale.

#### Implicazioni critiche e garanzie di sicurezza

* **Requisiti di spazio libero**: l'unità di destinazione **deve avere capacità libera sufficiente** per archiviare il payload completo del file *prima* dell'inizio dell'operazione. Se tenti di spostare un file da 30 GB su un'unità esterna con solo 10 GB liberi, il trasferimento fallirà. 
* **Garanzia zero perdita di dati**: se un'unità esterna viene scollegata accidentalmente o se lo spazio di archiviazione di destinazione esaurisce lo spazio durante il trasferimento, ATBCmder interrompe immediatamente l'operazione, lascia il file di origine **completamente intatto e illeso**, rimuove qualsiasi file di destinazione parziale e segnala una chiara finestra di dialogo di errore. 
* **Monitoraggio della coda in background (`cm_OperationsPanel`)**: gli spostamenti tra volumi a esecuzione prolungata vengono eseguiti su thread di lavoro in background asincroni (`FileOpWorker`). È possibile monitorare le velocità di trasferimento in tempo reale, i tempi rimanenti, mettere in pausa/riprendere i trasferimenti o accodare le operazioni successive senza bloccare l'interfaccia utente. 

---

### 3.6 Ulteriori domande frequenti

#### Q1: Come posso spostare lo stato attivo tra i pannelli sinistro e destro?

Premere il tasto **`Tab`** (`⇥`). Il focus alterna istantaneamente tra le tabelle di file attive e inattive. Il pannello attivo visualizza un bordo evidenziato e un testo della barra di stato focalizzato.

#### Q2: Come posso scambiare il contenuto dei pannelli sinistro e destro?

Premi **`Ctrl+U`** (`⌃U`) o esegui il comando **`cm_Exchange`**. Le directory, le schede delle cartelle e le posizioni del cursore dei pannelli sinistro e destro si scambiano istantaneamente. Per equalizzare le larghezze del pannello con una divisione esatta 50/50, fare doppio clic in un punto qualsiasi della barra di divisione centrale verticale.

#### Q3: Come seleziono i file utilizzando i modelli con caratteri jolly?

Premi il tasto **`+`** sulla tastiera (o scegli **Segna ➔ Seleziona gruppo...** / `cm_MarkPlus`). Inserisci un modello di carattere jolly come `*.pdf` o `photo_2026_*.jpg`. Per deselezionare i file che corrispondono a un modello, premere il tasto **`-`** (`cm_MarkMinus`). Per invertire la selezione corrente, premi **`*`** (`cm_MarkInvert`).

#### Q4: Come posso attivare/disattivare la visibilità dei dotfile nascosti?

Premi **`Cmd+H`** (`⌘H`) o **`Cmd+Shift+Period`** (`⇧⌘.`) o esegui il comando **`cm_ShowSysFiles`**. I file Unix nascosti (file che iniziano con un punto, come `.zshrc`, `.gitignore`, `.env`) alternano immediatamente lo stato visibile e quello nascosto.

#### Q5: Come posso aprire una finestra di terminale macOS nella directory corrente?

Premi **`Ctrl+J`** (`⌃J`) o esegui il comando **`cm_RunTerm`**. ATBCmder genera una nuova sessione macOS Terminale (o iTerm2) con la sua directory di lavoro corrente impostata sul percorso esatto del pannello dei file attivi.

#### Q6: ATBCmder supporta i Mac Intel (x86_64)?

Attualmente, ATBCmder è compilato in modo nativo ed esclusivamente per i Mac **Apple Silicon (M1/M2/M3/M4, architettura ARM64)** per sfruttare appieno la memoria unificata di Apple, l'accelerazione hardware Metal e i sottosistemi Neural Engine. **I Mac Intel (x86_64) non sono al momento supportati.** 

---

## 4. Suggerimenti professionali e lista di controllo per la manutenzione del sistema

Per mantenere ATBCmder performante alla massima velocità nei flussi di lavoro aziendali: 

- **Manutenzione settimanale della cache**: se sfogli spesso le schede della fotocamera ad alta risoluzione, cancella periodicamente le cache temporanee delle miniature tramite **Configurazione ➔ Opzioni ➔ Miniature ➔ Cancella cache delle miniature** per recuperare spazio su disco. 
- **Controllo portachiavi**: se ruoti le password su server SFTP o SMB remoti, aggiorna le tue credenziali in ATBCmder tramite **Rete ➔ Gestisci connessioni di rete...**. La modifica e il salvataggio aggiornano senza problemi l'elemento credenziale corrispondente nel portachiavi macOS. 
- **Ottimizzazione della coda in background**: per trasferimenti multi-gigabyte su reti da 1 Gbps o 10 Gbps, regola le dimensioni del buffer dei blocchi in **Configurazione ➔ Opzioni ➔ Operazioni sui file** per massimizzare la saturazione del bus. 
- **Preserva autorizzazioni UNIX**: quando si copiano script o file binari compilati tra unità APFS macOS, assicurarsi che **Preserva attributi e autorizzazioni file** sia selezionato nella finestra di dialogo Copia (`F5`), mantenendo automaticamente i flag di esecuzione (`chmod +x`). 

--- 

<div align="center"> 
<p><strong>Guida per l'utente e portale della documentazione di ATBCmder</strong></p> 
<p> 
<a href="index.md">&larr; Ritorna al portale della documentazione</a> &nbsp;&bull;&nbsp; 
<a href="getting_started.md">Capitolo 1: Nozioni fondamentali</a> &nbsp;&bull;&nbsp; 
<a href="keyboard_shortcuts.md">Capitolo 8: Scorciatoie</a> &nbsp;&bull;&nbsp; 
<a href="download.md">Capitolo 10: Download e installazione &rarr;</a> 
</p> 
</div>