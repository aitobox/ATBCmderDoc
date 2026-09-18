# Capitolo 7: Strumenti di sistema e manutenzione

Un file manager professionale non opera nel vuoto: è il centro nevralgico per l'archiviazione, la memoria e le risorse del sistema operativo. Sebbene la classica gestione dei file a doppio pannello eccella nell'organizzare, spostare e sincronizzare le gerarchie di directory, gli utenti avanzati, gli sviluppatori e gli amministratori di sistema affrontano frequentemente sfide a livello di sistema: individuare quale directory nascosta ha consumato silenziosamente 50 GB di spazio su disco, identificare un processo in background anomalo che sovraccarica i core della CPU, ripulire gigabyte di cache di sviluppo e artefatti di compilazione abbandonati, e disinstallare completamente le applicazioni macOS senza lasciare file di preferenze orfani, launch daemon o cartelle di supporto applicazione sparse in `~/Library/`.

ATBCmder integra quattro strumenti dedicati di diagnostica e manutenzione del sistema direttamente nel menu **Strumenti**. Alimentati da un demone nativo di monitoraggio asincrono, questi strumenti operano senza problemi accanto ai tuoi pannelli dei file, senza bloccare l'interfaccia utente né richiedere pesanti utility di terze parti cariche di annunci pubblicitari.

---

## 1. Avvio rapido visivo: Strumenti di sistema e HUD di stato

ATBCmder suddivide la manutenzione del sistema in quattro strumenti operativi fondamentali affiancati da una capsula di monitoraggio sempre visibile sulla barra degli strumenti:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   SUITE STRUMENTI DI SISTEMA ATBCMDER                                  │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  [1] Capsula di stato HUD e popover     [2] Stato del sistema e diagnostica (⌘⇧M)                      │
│      • CPU, RAM e rete in tempo reale       • Barre per singolo core, tabella completa dei processi    │
│      • Stile soglie a colori                • Cerca/filtra processi, invio di SIGTERM/SIGKILL          │
│      • Clic per il popover multi-metrica    • Grafici di capacità del file system e interfacce di rete │
│                                                                                                        │
│  [3] Analizzatore spazio su disco (⌘⇧D) [4] Pulizia del sistema (⌘⇧C)                                  │
│      • Scanner directory multi-thread       • Pulizia sicura a due fasi: scansiona, verifica, pulisci  │
│      • Mappa ad albero (treemap) interattiva• 6 categorie: cache, log, Xcode, dev tool, cestino        │
│      • Navigazione breadcrumb approfondita  • 3 livelli di rischio (Sicuro, Avviso, Pericolo) + Liste  │
│                                                                                                        │
│  [5] Programma di disinstallazione applicazioni (⌘⇧U)                                                  │
│      • Rimozione completa dei bundle .app e dei residui profondi                                       │
│      • Pulisce Application Support, Preferenze, Cache, LaunchAgent e Container                         │
│      • Doppia modalità: Disinstallazione completa vs Solo residui (pulisce app già eliminate)          │
│                                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Matrice delle scorciatoie a doppia matrice per gli strumenti di sistema

| Strumento / Azione | Scorciatoia macOS | Tasto Commander classico | ID comando | Posizione nel menu |
| :--- | :--- | :--- | :--- | :--- |
| **Pannello di stato del sistema** | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` | **Strumenti ➔ Stato del sistema...** |
| **Analizzatore dello spazio su disco** | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` | **Strumenti ➔ Analizzatore dello spazio su disco...** |
| **Pulizia del sistema** | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` | **Strumenti ➔ Pulizia del sistema...** |
| **Disinstallazione applicazioni** | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` | **Strumenti ➔ Disinstalla applicazione...** |
| **Attiva/disattiva capsula di stato** | Preferenze ➔ Generale | — | *(Impostazioni)* | **Configurazione ➔ Opzioni ➔ Generale** |

---

## 2. Capsula di stato della barra degli strumenti e popover interattivo

ATBCmder include una **Capsula di stato del sistema** integrata direttamente sul lato destro della barra degli strumenti principale. Questa fornisce una consapevolezza immediata e periferica dell'integrità del sistema senza dover passare a Monitoraggio Attività o aprire una finestra separata del Terminale.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Schede pannello sinistro]          [Schede pannello destro]    [ CPU 18% | RAM 44% | ↓1.2M ↑340K ]│
└───────────────────────────────────────────────────────────────────────────┬────────────┘
                                                                            │ Clic sulla capsula
                                                                            ▼
                                                ┌───────────────────────────────────────┐
                                                │ RIEPILOGO METRICHE DI SISTEMA         │
                                                ├───────────────────────────────────────┤
                                                │ Utilizzo CPU:  [████░░░░░░░░░░]   18% │
                                                │ Memoria:       [████████░░░░░░]   44% │
                                                │ Carico GPU:    [██░░░░░░░░░░░░]   12% │
                                                │ Batteria:      [████████████░░]   88% │
                                                ├───────────────────────────────────────┤
                                                │ Spazio disco:                         │
                                                │  Macintosh HD:  312.4 GB / 994.6 GB   │
                                                │  SSD esterno:   842.1 GB / 2.0 TB     │
                                                ├───────────────────────────────────────┤
                                                │ Processi principali:                  │
                                                │  • ATBCmder         PID: 54102  CPU: 2%│
                                                │  • WindowServer     PID: 284    CPU: 8%│
                                                │  • Xcode            PID: 88120  CPU: 4%│
                                                ├───────────────────────────────────────┤
                                                │ [ Apri diagnostica di sistema (⌘⇧M) ➔] │
                                                └───────────────────────────────────────┘
```

### 2.1 Componenti della capsula e stile visivo

La capsula di stato (larga `320px`) visualizza tre metriche di telemetria in tempo reale, aggiornate una volta al secondo:

1. **Utilizzo CPU**: percentuale di utilizzo aggregata del processore in tempo reale con codifica cromatica dinamica:
   - **Normale (< 75%)**: blu accento / primo piano del tema.
   - **Elevato (75% – 90%)**: arancione di avviso.
   - **Critico (> 90%)**: rosso di allarme.
2. **Utilizzo della memoria (RAM)**: pressione della memoria attuale attiva e cablata (wired), espressa come percentuale della RAM fisica.
3. **Throughput di rete**: velocità aggregate di upload e download in tempo reale su tutti gli adattatori di rete attivi, formattate in modo compatto (ad es. `↓2.4 MB/s ↑512 KB/s`).

### 2.2 Popover interattivo (`StatusPopup`)

Facendo clic in un punto qualsiasi della capsula di stato si apre un **Popover di stato** mobile non modale:

- **Telemetria hardware**: visualizza le percentuali combinate di CPU, memoria, GPU e stato della batteria (inclusi percentuale di carica e stato dell'alimentazione).
- **Punti di montaggio del file system**: elenca tutti i container APFS locali montati e le unità esterne con barre dello spazio disponibile e della capacità totale.
- **Top 5 processi**: evidenzia i cinque processi che consumano più risorse per percentuale di CPU e footprint di memoria.
- **Pulsante di approfondimento**: fai clic su **"Apri diagnostica di sistema"** (o premi `⌘⇧M`) per avviare la finestra completa di diagnostica.

### 2.3 Configurazione della visibilità della capsula

Se preferisci una barra degli strumenti essenziale e priva di distrazioni con i soli controlli di navigazione dei file:

1. Apri le **Preferenze** (`⌘,` / **Configurazione ➔ Opzioni...**).
2. Seleziona **Generale** nella barra laterale sinistra.
3. In **Visualizzazione e layout**, attiva/disattiva la casella di controllo:
   `[X] Mostra capsula stato di sistema sulla barra strumenti`
4. Fai clic su **Applica** o **OK**. La capsula apparirà o scomparirà immediatamente dalla barra degli strumenti principale.

---

## 3. Stato del sistema e diagnostica (`cm_SystemStatus` / `⌘⇧M`)

Premendo **`⌘⇧M`** (o **`Ctrl+Shift+M`**) si apre il **Pannello di stato del sistema** completo. Questa utility funge da console diagnostica integrata, progettata su misura per amministratori di sistema, sviluppatori e analisi delle prestazioni.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              STATO DEL SISTEMA E DIAGNOSTICA                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ UTILIZZO CPU: Apple M3 Max (14 Core)                                                   │
│ Core 01: [██████░░░░] 60%    Core 05: [██░░░░░░░░] 20%    Core 09: [███░░░░░░░] 30%    │
│ Core 02: [████░░░░░░] 40%    Core 06: [████░░░░░░] 42%    Core 10: [█░░░░░░░░░] 10%    │
│ Core 03: [████████░░] 80%    Core 07: [█░░░░░░░░░] 12%    Core 11: [░░░░░░░░░░]  5%    │
│ Core 04: [███░░░░░░░] 30%    Core 08: [██░░░░░░░░] 18%    Core 12: [░░░░░░░░░░]  4%    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ MEMORIA: Totale 36.0 GB |  Usata: 16.2 GB (45%) |  App: 9.4 GB |  Wired: 4.1 GB        │
│ SWAP:    Totale 2.0 GB  |  Usata: 0 MB (0%)                                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ ELENCO PROCESSI                              Filtro: [ node                     ] [x]  │
│ PID      Nome             Utente         CPU %       Memoria     Thread     Azione     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ 72841    node (dev-srv)   brain          48.2%       612.4 MB    28         [ Kill ✕ ] │
│ 72910    node (esbuild)   brain          12.1%       184.2 MB    14         [ Kill ✕ ] │
│ 73104    node (lsp)       brain           1.4%        98.5 MB     8         [ Kill ✕ ] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Intervallo aggiornamento: [ 1.0s ▼ ] [ Sospendi monitoraggio ]      [ Chiudi (Esc) ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Funzionalità diagnostiche e sezioni delle metriche

1. **Monitor del processore multi-core**:
   - Visualizza il carico complessivo del sistema e la ripartizione tra i singoli Performance core ed Efficiency core.
   - Gli indicatori di avanzamento per singolo core evidenziano la saturazione dei core durante compilazioni multi-thread o rendering intensivi.
2. **Dettaglio memoria e pressione dello swap**:
   - Classifica l'allocazione della memoria fisica in Memoria app, Memoria cablata (Wired), Memoria compressa e File memorizzati nella cache.
   - Monitora l'utilizzo dello swap virtuale per identificare rapidamente se i memory leak stanno provocando paging continuo su disco.
3. **Panoramica archiviazione e volumi montati**:
   - Metriche di throughput di lettura/scrittura su disco in tempo reale insieme ai dati di capacità dei punti di montaggio.
4. **Gestore interattivo dei processi**:
   - Tabella ordinabile in tempo reale contenente tutte le attività in esecuzione, di sistema e utente.
   - **Cerca e filtra**: digita qualsiasi nome di processo o PID nella casella di ricerca per filtrare istantaneamente i risultati.
   - **Terminazione dei processi**:
     - Fai clic su **Kill** o seleziona un processo e premi `Canc` (`Delete`).
     - Viene visualizzata una finestra di dialogo di conferma che propone **Termina (`SIGTERM`)** per un arresto regolare o **Forza chiusura (`SIGKILL`)** per i processi non reattivi.

---

## 4. Analizzatore dello spazio su disco (`cm_DiskUsageAnalyzer` / `⌘⇧D`)

Quando un'unità a stato solido (SSD) inizia a esaurire lo spazio disponibile, scoprire dove sono nascosti gigabyte di dati può essere estenuante. Gli elenchi standard dei file del Finder non calcolano automaticamente le dimensioni delle cartelle, e l'ispezione manuale richiede una noiosa navigazione attraverso gerarchie annidate.

L'**Analizzatore dello spazio su disco** (`cm_DiskUsageAnalyzer`, scorciatoia **`⌘⇧D`** / **`Ctrl+Shift+D`**) scansiona in modo asincrono interi alberi di directory tramite uno scanner multi-thread e visualizza lo spazio di archiviazione sia attraverso un elenco ad albero gerarchico tradizionale sia mediante una **Mappa ad albero (squarified treemap)** interattiva.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ ANALIZZATORE SPAZIO SU DISCO: /Users/brainzhang                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Percorso: /Users/brainzhang ➔ Developer ➔ Projects                                    │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ GERARCHIA DIRECTORY                  │ MAPPA AD ALBERO (TREEMAP) INTERATTIVA           │
│ Nome cartella    Dimens.    Percent. │ ┌───────────────────────────┬─────────────────┐ │
│ ──────────────────────────────────── │ │                           │ node_modules    │ │
│ ▼ Developer      142.6 GB   58.2%    │ │ target/debug              │ 28.4 GB         │ │
│   ► Projects     118.2 GB   48.2%    │ │ 64.2 GB                   │ (Rust build)    │ │
│   ► Caches        24.4 GB   10.0%    │ │                           ├─────────────────┤ │
│ ▼ Library         64.2 GB   26.2%    │ │                           │ DerivedData     │ │
│   ► Caches        38.1 GB   15.5%    │ │                           │ 18.2 GB         │ │
│   ► App Support   22.4 GB    9.1%    │ ├───────────────────────────┴─────────────────┤ │
│ ► Downloads       24.1 GB    9.8%    │ │ Video Footage (4K Prores)                   │ │
│ ► Pictures        14.2 GB    5.8%    │ │ 31.8 GB                                     │ │
├──────────────────────────────────────┴─┴───────────────────────────────────────────────┤
│ [ Livello sup. (..) ] [ Mostra nel pannello ] [ Sposta nel Cestino (⌘⌫) ] [ Esporta ] │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Architettura chiave e funzionalità

- **Scansione multi-thread asincrona**: scansiona centinaia di migliaia di file attraverso container APFS senza bloccare l'interfaccia principale di ATBCmder. Una barra di avanzamento mostra il numero di directory scansionate al secondo.
- **Visualizzazione con mappa ad albero (squarified treemap)**:
  - Cartelle e file sono rappresentati come blocchi rettangolari nidificati la cui area superficiale bidimensionale è strettamente proporzionale alla loro dimensione effettiva su disco.
  - I colori riflettono automaticamente la profondità della directory, consentendo di individuare all'istante e con un solo colpo d'occhio gli elementi più pesanti.
- **Sincronizzazione bidirezionale**:
  - Selezionando un elemento nell'albero delle directory viene evidenziato il blocco corrispondente nella treemap.
  - Facendo clic su qualsiasi rettangolo nella treemap viene evidenziata la riga corrispondente nella vista ad albero e vengono visualizzati il percorso completo del file e la dimensione esatta in byte.

### 4.2 Navigazione interattiva e flussi di lavoro

1. **Navigazione approfondita**: fai doppio clic sulla riga di una cartella o su un blocco della treemap per ingrandire quella sottodirectory e ricalcolare la vista rispetto alla nuova radice.
2. **Livello superiore**: fai clic sul pulsante **Livello superiore** nella barra degli strumenti o su qualsiasi segmento della barra breadcrumb in alto per tornare alle directory superiori.
3. **Mostra nei doppi pannelli**: fai clic su **Mostra nel pannello** per aprire istantaneamente la directory selezionata nel pannello attivo di ATBCmder.
4. **Pulizia istantanea**: seleziona qualsiasi file o cartella voluminosa obsoleta e premi **`⌘⌫`** (oppure fai clic su **Sposta nel Cestino**). L'elemento viene inviato in sicurezza al Cestino di macOS e l'albero di scansione si aggiorna automaticamente.
5. **Esportazione report di archiviazione**: fai clic su **Esporta** per generare un controllo completo dell'utilizzo del disco formattato come file CSV strutturato o riepilogo in testo normale per la pianificazione dello spazio.

---

## 5. Pulizia del sistema (`cm_CleanSystem` / `⌘⇧C`)

Nel corso di mesi di utilizzo quotidiano, macOS accumula gigabyte di dati temporanei: cache obsolete delle applicazioni, artefatti di compilazione di Xcode, download dei gestori di pacchetti, log diagnostici orfani e cache dei browser. Sebbene alcune cache velocizzino i flussi di lavoro, gli elementi obsoleti sprecano prezioso spazio di archiviazione SSD ad alta velocità.

Lo strumento di **Pulizia del sistema** (`cm_CleanSystem`, scorciatoia **`⌘⇧C`** / **`Ctrl+Shift+C`**) offre una pulizia del sistema deterministica a due fasi, progettata con garanzie di sicurezza di livello aziendale.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              PULIZIA SISTEMA: AUDIT PREVENTIVO                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Scansiona ]  Elementi analizzati: 48.192 in 2,1s    Spazio recuperabile: 34,8 GB     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CATEGORIA                         ELEMENTI    DIMENS.     LIVELLO RISCHIO SELEZIONE    │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ [X] Cache delle applicazioni      12.410      14,2 GB     Sicuro (Verde) [Selez. tutto]│
│ [X] Log utente e di sistema        4.218       1,8 GB     Sicuro (Verde) [Selez. tutto]│
│ [X] Xcode Derived Data             8.940      12,4 GB     Avviso (Aranc) [Selez. tutto]│
│ [ ] Cache Homebrew e CocoaPods     1.420       3,6 GB     Avviso (Aranc) [Selez. tutto]│
│ [ ] Cache dei browser web         21.200       2,8 GB     Sicuro (Verde) [Selez. tutto]│
│ [ ] Cestino di sistema                 4       8,2 GB     Pericolo (Ros) [Deselez.]    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Selezionati per la pulizia: 28,4 GB in 25.568 file                                     │
│ Whitelist: ~/.config/atbsys/whitelist (4 regole attive)                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Editor whitelist... ]      [ Esporta log ]       [ Pulisci selezionati (28,4 GB) ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Architettura di sicurezza a due fasi

A differenza delle pericolose utility di "pulizia con un clic" che cancellano i file silenziosamente in background, ATBCmder impone un rigoroso **Protocollo di sicurezza a due fasi**:

1. **Fase 1: Scansione preventiva e valutazione (Dry-Run)**:
   - Lo strumento di pulizia esegue una ricognizione in sola lettura nelle posizioni standardizzate di sistema.
   - Calcola il conteggio esatto dei file e le dimensioni in byte senza modificare o eliminare un singolo byte.
   - Raggruppa i risultati in categorie trasparenti con valutazioni di rischio esplicite.
2. **Fase 2: Eliminazione selettiva verificata dall'utente**:
   - L'utente esamina l'elenco categorizzato e seleziona o deseleziona singoli elementi o intere categorie.
   - Facendo clic su **"Pulisci selezionati"** viene eseguita l'eliminazione unicamente degli elementi esplicitamente contrassegnati.
   - Ogni evento di eliminazione viene registrato in un log di audit atomico in `~/Library/Preferences/atbcmder/operations.log`.

### 5.2 Sei domini di pulizia principali

| Categoria | Percorso tipico | Livello di rischio | Descrizione |
| :--- | :--- | :---: | :--- |
| **Cache delle applicazioni** | `~/Library/Caches/` | **Sicuro** | Cache obsolete generate dalle applicazioni desktop che vengono ricreate automaticamente all'occorrenza. |
| **Log utente e di sistema** | `~/Library/Logs/`, `/var/log/` | **Sicuro** | Vecchi log di crash, dump diagnostici e log di aggiornamento software non più necessari per la risoluzione dei problemi. |
| **Cache dei browser** | Safari, Chrome, Edge, Firefox | **Sicuro** | Pagine web memorizzate nella cache, buffer multimediali e script tra i vari browser desktop installati. |
| **Xcode Derived Data** | `~/Library/Developer/Xcode/DerivedData` | **Avviso** | File oggetto intermedi, cache dei moduli e dati di indicizzazione di precedenti compilazioni degli sviluppatori Apple. |
| **Cache gestori di pacchetti** | Homebrew, CocoaPods, NPM, Yarn | **Avviso** | Tarball scaricati, archivi di formule e directory di cache dei pacchetti. |
| **Cestino** | `~/.Trash`, `.Trashes` | **Pericolo** | Elementi precedentemente spostati nel Cestino di macOS che non sono stati ancora svuotati definitivamente. |

### 5.3 Livelli di rischio e whitelist di sicurezza

- 🟢 **Sicuro (Verde)**: cache temporanee e metadati eliminati che possono essere rimossi senza alcuna perdita di configurazione o interruzione del flusso di lavoro.
- 🟡 **Avviso (Arancione)**: artefatti di sviluppo o cache dei gestori di pacchetti. La loro eliminazione è sicura, ma la successiva compilazione del progetto o il download dei pacchetti richiederà più tempo per riscaricare i file necessari.
- 🔴 **Pericolo (Rosso)**: include file che richiedono conferma esplicita (ad esempio lo svuotamento definitivo del Cestino).
- **Regole personalizzate per la whitelist**:
  - Aggiungi percorsi specifici, estensioni o nomi di cartelle che ATBCmder non deve **mai** toccare nel file `~/.config/atbsys/whitelist`.
  - Le regole di protezione integrate impediscono automaticamente la scansione dei file critici del sistema operativo macOS, delle directory del portachiavi (keychain) utente e delle cartelle di sincronizzazione offline dei servizi cloud.

---

## 6. Programma di disinstallazione applicazioni (`cm_UninstallApp` / `⌘⇧U`)

Su macOS, trascinare un'applicazione da `/Applications` al Cestino rimuove unicamente il bundle `.app`. Le applicazioni moderne disperdono frequentemente centinaia di file ausiliari sul disco: file plist delle preferenze, database in Application Support, launch agent in background, sandbox container e file multimediali memorizzati nella cache. Con il passare del tempo, questi residui orfani consumano gigabyte di spazio e possono lasciare processi in background non necessari avviati automaticamente al login.

Il **Programma di disinstallazione applicazioni** (`cm_UninstallApp`, scorciatoia **`⌘⇧U`** / **`Ctrl+Shift+U`**) offre una scansione approfondita delle dipendenze per eliminare completamente le applicazioni e tutti i relativi file residui.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   DISINSTALLAZIONE APPROFONDITA DELLE APPLICAZIONI                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Filtro: Docker                     ]  Trovate: 142 applicazioni (Totale: 48,2 GB)    │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ APPLICAZIONI INSTALLATE              │ RESIDUI ASSOCIATI E FILE DI SUPPORTO            │
│ Nome app          Versione   Dimens. │ Percorso file / Componente          Dimens.     │
│ ──────────────────────────────────── │ ─────────────────────────────────────────────── │
│ [X] Docker.app    4.28.0     1,8 GB  │ [X] /Applications/Docker.app        1,8 GB (.app│
│ [ ] Figma.app     116.15     240 MB  │ [X] ~/Library/Application Support/Docker 14,2 GB│
│ [ ] Slack.app     4.36.0     310 MB  │ [X] ~/Library/Caches/com.docker.docker   2,1 GB │
│ [ ] Visual Studio 1.87.0     450 MB  │ [X] ~/Library/Preferences/com.docker...  12 KB  │
│ [ ] Xcode.app     15.3      12,4 GB  │ [X] ~/Library/LaunchAgents/com.docker...  4 KB  │
│                                      │ [X] ~/Library/Containers/com.docker...  380 MB  │
├──────────────────────────────────────┴─────────────────────────────────────────────────┤
│ Modalità: (•) Disinstallaz. completa (.app + residui)  ( ) Solo residui (orfani)       │
│ Totale selezionato per la rimozione: 18,48 GB in 6 elementi                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Aggiorna elenco ]            [ Annulla ]             [ Disinstalla app (18,5 GB) ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Percorsi di rilevamento dei residui

Durante la ricerca dei componenti dell'applicazione, ATBCmder esamina i seguenti percorsi standard dei sottosistemi di macOS utilizzando una corrispondenza esatta del bundle identifier:

1. **Bundle dell'applicazione**: `/Applications/<Nome>.app` e `~/Applications/<Nome>.app`.
2. **Supporto applicazione (Application Support)**: `~/Library/Application Support/<Nome>` e `<BundleID>`.
3. **Cache dell'applicazione**: `~/Library/Caches/<BundleID>`.
4. **Preferenze e impostazioni predefinite**: `~/Library/Preferences/<BundleID>.plist`.
5. **Stato salvato (Saved State)**: `~/Library/Saved Application State/<BundleID>.savedState`.
6. **Launch Daemon e Agent**: `~/Library/LaunchAgents/<BundleID>.plist`.
7. **Sandbox Container**: `~/Library/Containers/<BundleID>/` e `~/Library/Group Containers/`.
8. **Log dell'applicazione**: `~/Library/Logs/<Nome>/`.

### 6.2 Doppia modalità operativa

- **Disinstallazione completa (predefinita)**:
  - Progettata per rimuovere un'applicazione attualmente installata e presente sul Mac.
  - Elimina sia il bundle eseguibile `.app` da `/Applications` sia tutti i file di supporto ausiliari associati in una singola operazione atomica.
- **Solo residui**:
  - Progettata per ripulire i residui di applicazioni che sono state precedentemente eliminate manualmente tramite il Finder o con utility di terze parti.
  - Esegue una scansione in `~/Library/` alla ricerca di cartelle di supporto orfane il cui bundle `.app` genitore non è più presente nel sistema.

### 6.3 Integrità del sistema Apple e barriere di sicurezza

Per prevenire l'instabilità accidentale del sistema:

- **Protezione delle app di sistema**: le applicazioni di sistema integrate di macOS (Safari, Finder, Anteprima, Musica, Impostazioni di Sistema, ecc.) sono protette da un'icona a lucchetto in sola lettura e non possono essere disinstallate.
- **Rilevamento dei processi in esecuzione**: se un'applicazione o il suo demone di supporto è attualmente attivo, ATBCmder richiede di chiudere regolarmente l'applicazione prima di procedere con la disinstallazione.
- **Protocollo basato sul Cestino (Trash-First)**: per impostazione predefinita, tutti gli elementi disinstallati vengono spostati nel Cestino di macOS invece di essere eliminati definitivamente dal disco, consentendo un ripristino completo in caso di necessità.

---

## 7. Avvisi di sistema e manutenzione

> [!NOTE]
> **Impatto minimo sulle risorse di sistema**  
> Il demone di monitoraggio dello stato in background è sviluppato in codice compilato nativo ed è eseguito con un intervallo di polling di 1,0 secondi. Consuma meno dello 0,1% di CPU durante la normale navigazione dei file e sospende automaticamente il polling quando ATBCmder viene ridotto a icona o nascosto.

> [!TIP]
> **Abbinare l'Analizzatore dello spazio su disco con la vista diramata piatta (Branch View)**  
> Se l'Analizzatore dello spazio su disco individua una directory contenente migliaia di file temporanei sparsi, seleziona tale directory e fai clic su **Mostra nel pannello**. Quindi premi **`Cmd+B`** (`cm_DirBranch`) per appiattire l'intero albero nidificato in un unico elenco in cui ordinare, selezionare ed eliminare in blocco gli elementi con precisione da tastiera.

> [!IMPORTANT]
> **Verifica sempre le selezioni prima di confermare la pulizia**  
> Sebbene lo strumento di pulizia del sistema contrassegni le cache come **Sicuro (Verde)**, alcuni strumenti per sviluppatori (come Xcode DerivedData o volumi Docker locali) potrebbero richiedere tempo per ricompilare o riscaricare i dati al successivo avvio del progetto. Esamina le categorie selezionate per assicurarti di non cancellare cache necessarie per uno sprint di lavoro attivo.

> [!CAUTION]
> **Forzare la chiusura dei processi di sistema (`SIGKILL`)**  
> Nel Gestore processi dello Stato del sistema, l'invio di `SIGKILL` (Forza chiusura) arresta immediatamente il processo di destinazione senza consentirgli di scaricare i buffer dei file aperti o di salvare lo stato dei documenti. Tenta sempre prima una chiusura regolare con `SIGTERM`.

> [!WARNING]
> **Rimozione dei container sandbox delle applicazioni**  
> Durante la disinstallazione delle applicazioni scaricate dal Mac App Store, i file ausiliari memorizzati in `~/Library/Containers/<BundleID>` spesso includono database di documenti sandbox. Assicurati di aver esportato tutti i file di progetto locali essenziali prima di confermare l'eliminazione dei container.

---

## 8. Tabella di riferimento principale degli strumenti di sistema a doppia matrice

| Categoria | Descrizione azione | Scorciatoia macOS | Tasto Commander classico | ID comando |
| :--- | :--- | :--- | :--- | :--- |
| **Monitor di sistema** | Apri pannello completo di diagnostica del sistema | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` |
| **Monitor di sistema** | Apri popover di stato leggero | Clic sulla capsula della barra | — | *(Azione interfaccia)* |
| **Monitor di sistema** | Filtra elenco del gestore processi | `Cmd+F` (nel pannello) | `F7` | — |
| **Monitor di sistema** | Termina processo (`SIGTERM`) | `Delete` / `⌫` | `Delete` | — |
| **Monitor di sistema** | Forza chiusura del processo (`SIGKILL`) | `Shift+Delete` / `⇧⌫` | `Shift+Delete` | — |
| **Analizzatore disco** | Apri finestra di dialogo Analizzatore spazio su disco | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` |
| **Analizzatore disco** | Approfondisci nella cartella selezionata | `Invio` / `Return` | `Enter` | — |
| **Analizzatore disco** | Torna alla directory superiore | `Backspace` / `⌫` | `Backspace` | — |
| **Analizzatore disco** | Sposta l'elemento evidenziato nel Cestino | `Cmd+Delete` / `⌘⌫` | `F8` / `Delete` | — |
| **Analizzatore disco** | Mostra l'elemento selezionato nel doppio pannello | `Cmd+Return` / `⌘⏎` | `Ctrl+Enter` | — |
| **Pulizia di sistema** | Apri finestra di dialogo Pulizia sicura del sistema | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` |
| **Pulizia di sistema** | Esegui scansione preventiva di sola lettura | `Cmd+R` / `⌘R` | `Ctrl+R` | — |
| **Pulizia di sistema** | Attiva/disattiva selezione della categoria | `Spazio` | `Space` | — |
| **Disinstallatore app** | Apri disinstallatore applicazioni | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` |
| **Disinstallatore app** | Passa alla modalità Solo residui | `Cmd+2` / `⌘2` | `Alt+2` | — |
| **Preferenze** | Attiva/disattiva capsula HUD di stato sulla barra | Preferenze ➔ Generale | — | *(Configurazione)* |

---

<div align="center">
  <p>Pronto a personalizzare le scorciatoie da tastiera, le viste dei pannelli e il comportamento dell'applicazione?</p>
  <p><strong><a href="preferences_and_customization.md">Procedi al Capitolo 8: Preferenze e personalizzazione &rarr;</a></strong></p>
</div>
