# Capitolo 1: Concetti fondamentali e configurazione di macOS

Benvenuto su **ATBCmder**! Progettato nativamente per macOS 12+ su Apple Silicon (M1/M2/M3/M4, architettura ARM64; Intel x86_64 non è attualmente supportato), ATBCmder porta sul Mac la velocità senza pari, l'agilità della tastiera e la precisione della gestione ortodossa dei file a doppio pannello. 

Questo capitolo ti illustra la filosofia principale del doppio pannello, descrive in dettaglio tutti i principali punti di riferimento dell'interfaccia, ti guida attraverso l'onboarding delle autorizzazioni di macOS App Sandbox e fornisce le configurazioni di sistema essenziali necessarie per un'esperienza senza interruzioni. 

---

## 1. Avvio rapido visivo: la filosofia del doppio pannello

Se hai utilizzato macOS Finder, sei abituato ad aprire più finestre sovrapposte, a trascinare file su desktop disordinati e a sperare che i file arrivino nella cartella di destinazione prevista anziché in una sottocartella adiacente accidentale. 

ATBCmder sostituisce questo attrito con il collaudato paradigma **Orthodox File Manager (OFM)**: due pannelli di directory indipendenti e complementari posizionati fianco a fianco. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE (SOURCE) PANEL                     INACTIVE (TARGET) PANEL              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Name               Size    Date    │   │  Name                Size     Date    │
│  ▸ [..]                     --:--   │ C │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Yesterday O │  ▸ 2025_Archive      <DIR>    May 12  │
│  ● release_notes.md 14.2 KB Today   │ P │  ▸ Website_V2        <DIR>    Aug 28  │
│  ● update_v1.7.pkg  84.5 MB Today   │ Y │  ● config.yaml       3.2 KB   Jun 04  │
│                                     │ ➔ │                                       │
│  [ Focused / Blue Accent Outline ]  │   │  [ Unfocused / Subdued Outline ]      │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘
```

### Il modello attivo (sorgente) e inattivo (destinazione).

In ATBCmder, non devi mai chiederti dove avrà effetto un'operazione: 

1. **Il pannello attivo (fonte)**: 
- Questo è il pannello in cui attualmente risiedono il focus della tastiera e il cursore. 
- Qualsiasi selezione, navigazione o azione eseguita ha come target direttamente questo pannello. 
- **Segnale visivo**: il pannello attivo presenta un anello di messa a fuoco prominente (colore in risalto del sistema macOS), testo della scheda evidenziato e un cursore attivo distinto evidenziato sull'elemento attualmente focalizzato. 

2. **Il pannello inattivo (target)**: 
- Questo è il pannello opposto. Rimane completamente visibile, mostrando una gerarchia di cartelle indipendente. 
- Il pannello inattivo funge da **destinazione automatica** per le operazioni sui file avviate nel pannello attivo. 
- **Segnale visivo**: il pannello inattivo mostra un bordo attenuato, testo leggermente attenuato e titoli delle schede disattivati.

### Operazioni direzionali: sempre Origine ➔ Obiettivo

Quando avvii un'operazione in ATBCmder, l'applicazione comprende automaticamente la direzione: 

- **Copia (`F5` / `Cmd+C` ➔ `Cmd+V`)**: copia i file selezionati dal pannello Attivo (Origine) direttamente nella directory attualmente visualizzata nel pannello Inattivo (Destinazione). 
- **Sposta (`F6` / `Cmd+C` ➔ `Opt+Cmd+V`)**: sposta i file selezionati dal pannello Attivo al pannello Inattivo senza dover digitare o cercare la directory di destinazione. 
- **Sincronizzazione delle directory (`Shift+F12` / `cm_SyncDirs`)**: confronta la directory nel pannello attivo con la directory nel pannello inattivo. 

> [!CONSIGLIO] 
> **Non sono necessarie congetture tramite trascinamento**: non è necessario trascinare gli elementi oltre i limiti dello schermo. Seleziona semplicemente ciò che desideri nel pannello attivo, premi `F5` (Copia) o `F6` (Sposta), premi `Enter` per confermare la richiesta e ATBCmder trasferisce immediatamente i file.

### Navigazione del pannello e cambio messa a fuoco

| Azione | Scorciatoia macOS | Chiave del comandante classico | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Cambia messa a fuoco** | `Tab` | `Tab` | `cm_FocusSwap` | Alterna lo stato attivo della tastiera tra i pannelli sinistro e destro (`cm_SwitchPanel`). | 
| **Messa a fuoco inversa** | `Shift+Tab` | `Shift+Tab` | `cm_FocusSwap` | Inverte l'ordine di messa a fuoco tra pannelli e controlli. | 
| **Scambia sinistra e destra** | `Ctrl+U` | `Ctrl+U` | `cm_Exchange` | Scambia i percorsi delle directory tra i pannelli sinistro e destro senza perdere schede o selezioni. | 
| **Rapporto di equalizzazione** | `Double-click splitter` | `Double-click splitter` | — | Ripristina automaticamente lo splitter centrale su un saldo pulito 50/50. | 

---

## 2. Tour dell'anatomia dell'interfaccia e dei punti di riferimento

ATBCmder fornisce un'interfaccia macOS nativa e pulita, realizzata con Qt6 e PySide6, progettata secondo le linee guida Apple Human Interface, rispettando i classici flussi di lavoro Commander incentrati sulla tastiera. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] NATIVE MACOS MENU BAR                                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] TOP MAIN TOOLBAR  [ ↺ Refresh ] [ 📋 Copy ] [ ✂ Move ] [ 🗑 Delete ] ...   │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] BREADCRUMB BAR (Left Panel)     │   │ [3] BREADCRUMB BAR (Right Panel)      │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] FOLDER TABS: [Dev] [Docs] [+]   │[6]│ [4] FOLDER TABS: [Photos] [Backup] [+]│
├─────────────────────────────────────┤MID│───────────────────────────────────────┤
│                                     │DLE│                                       │
│ [5] DUAL FILE PANEL (Left)          │   │ [5] DUAL FILE PANEL (Right)           │
│     - Virtualized table listing     │BAR│     - Virtualized table listing       │
│     - Name, Ext, Size, Date, Attr   │ & │     - Name, Ext, Size, Date, Attr     │
│     - Real-time sort & filter       │SPL│     - Real-time sort & filter         │
│                                     │IT-│                                       │
│                                     │TER│                                       │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] STATUS BAR & DRIVE STORAGE METER                                            │
│  3 of 28 files selected (42.8 MB / 1.2 GB)  |  Macintosh HD: 218.4 GB free      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### [1] Barra dei menu nativa di macOS

Completamente integrato nella barra dei menu superiore di macOS. Tutte le operazioni, i commutatori di visualizzazione, gli strumenti elettrici e le preferenze sono classificati logicamente: 

- **File**: Nuova scheda, Chiudi scheda, Proprietà file, Autorizzazioni sandbox, Esci. 
- **Segna**: Seleziona gruppo (`Num+`), Deseleziona gruppo (`Num-`), Inverti selezione (`Num*`), Seleziona tutto (`Cmd+A`). 
- **Comandi**: Hotlist directory (`Ctrl+D`), Unità sinistra/destra (`Alt+F1/F2`), Cerca (`Alt+F7`), Sincronizza directory (`Shift+F12`), Scambia pannelli (`Ctrl+U`), Terminalee (`Ctrl+J`). 
- **Mostra**: attiva/disattiva la modalità di visualizzazione (Breve, Colonne intere, Miniature, Albero, Vista ramo piatto), visibilità della barra degli strumenti, layout dei pannelli orizzontali. 
- **Configurazione**: Opzioni/Preferenze (`Cmd+,`), Salva posizione (`cm_ConfigSavePos`), Salva schede.

### [2] Barra degli strumenti principale in alto

Situato direttamente sotto la barra del titolo della finestra. Fornisce accesso istantaneo con un clic ai comandi globali: 

- **Azioni predefinite**: Aggiorna (`Ctrl+R`), Visualizzazione rapida (`Ctrl+Q`), Copia (`F5`), Sposta (`F6`), Nuova cartella (`F7`), Elimina (`F8`), Cerca (`Alt+F7`) e Opzioni (`Cmd+,`). 
- **Personalizzabile**: personalizza le dimensioni delle icone (da 16px a 48px), attiva/disattiva le etichette di testo dei pulsanti o nascondi completamente la barra degli strumenti tramite il menu **Mostra** → **Mostra barra degli strumenti** per massimizzare lo spazio sullo schermo.

### [3] Barra breadcrumb interattiva in stile Finder

Posizionata sopra ogni pannello di file, la barra del percorso breadcrumb consente salti gerarchici rapidissimi: 

- **Navigazione segmento**: fai clic su qualsiasi cartella antenata nella catena breadcrumb (ad esempio, facendo clic su `username` in `/Users/username/Projects/ATBCmder`) per navigare direttamente in quella directory. 
- **Elenchi a discesa dei fratelli**: passa il mouse o fai clic sulla freccia chevron tra i segmenti per visualizzare un menu a discesa che elenca tutte le cartelle dei fratelli a quel livello. 
- **Menu contestuale segmento**: fai clic con il pulsante destro del mouse su qualsiasi segmento breadcrumb per accedere a utilità contestuali rapide: 
- **Apri in una nuova scheda**: mantiene la visualizzazione corrente durante l'apertura della directory principale in una nuova scheda. 
- **Mostra nel Finder**: apre la directory nel Finder di macOS (`open -R`). 
- **Copia percorso**: copia il percorso UNIX assoluto del segmento negli appunti del sistema. 
- **Apri nel terminale**: avvia macOS Terminale direttamente all'interno della cartella (`open -a Terminale`). 
- **Modifica diretta del percorso (`BreadcrumbLineEdit`)**: fai doppio clic sullo spazio vuoto a destra della catena breadcrumb. La barra si converte istantaneamente in un campo di testo modificabile in cui puoi incollare o digitare qualsiasi percorso (ad esempio archivi `/var/log`, `~/Library` o `vfs://`). Premi `Enter` per navigare o `Esc` per annullare.

### [4] Barra delle schede delle cartelle

Ogni pannello mantiene una serie indipendente di schede: 

- Apri nuove schede con `Cmd+T` (`cm_NewTab`), chiudi le schede con `Cmd+W` (`cm_CloseTab`). 
- Trascina e rilascia per riordinare le schede all'interno di un pannello. 
- Fai clic con il pulsante destro del mouse sulle schede per bloccare percorsi, rinominare titoli, chiudere duplicati o duplicare schede nel pannello opposto.

### [5] Pannelli a doppio file

Elenchi di file virtualizzati ad alte prestazioni in grado di eseguire il rendering di cartelle con centinaia di migliaia di voci in modo fluido senza interruzioni dell'interfaccia utente: 

- Ordinamento delle colonne: fare clic su qualsiasi intestazione (Nome, Esteso, Dimensione, Data, Attributi) per ordinare in modo crescente o decrescente. 
- Modalità di visualizzazione multiple: visualizzazione dettagli completi, visualizzazione griglia breve, visualizzazione galleria miniature, visualizzazione albero e visualizzazione ricorsiva ramo piatto (`Cmd+B`).

### [6] Barra degli strumenti centrale e divisore trascinabile

Posizionata direttamente tra i pannelli dei file sinistro e destro, la barra degli strumenti centrale è una funzionalità unica di ATBCmder che combina la gestione dei file con un clic con un divisore del pannello regolabile: 

![Middle Toolbar](images/middle_toolbar.png) 

- **Striscia di azione rapida**: ospita i pulsanti verticali per le operazioni comuni: 
- `cm_Copy` (Copia) 
- `cm_Move` (Sposta/Taglia) 
- `cm_Delete` (Elimina nel cestino) 
- `cm_MkDir` (Nuova directory) 
- `cm_Rename` (Rinomina rapida in linea) 
- `cm_View` (Elenco universale) 
- `cm_Edit` (Editor di testo/codice interno) 
- `cm_Exchange` (Scambia i pannelli sinistro e destro) 
- `cm_SyncDirs` (Sincronizzatore di cartelle) 
- `cm_FileSearch` (Ricerca avanzata) 
- **Trascinamento continuo con divisione**: spostando il cursore del mouse sulla barra centrale, il puntatore diventa un cursore diviso orizzontalmente (`SplitHCursor`). Fare clic e trascinare orizzontalmente per regolare uniformemente la proporzione della larghezza tra i due pannelli. 
- **Preimpostazioni rapporto tema elegante**: quando si utilizza il moderno tema "Elegante", la barra centrale mostra controlli segmentati che consentono l'aggancio istantaneo alla distribuzione della larghezza del pannello **50/50**, **70/30** o **30/70**. 
- **Preferenze barra degli strumenti centrale**: attiva o disattiva la barra degli strumenti centrale, regola le dimensioni delle icone o alterna tra i moderni pulsanti piatti e i classici separatori infossati in **Preferenze** (`Cmd+,`) → **Barre degli strumenti** → **Barra degli strumenti centrale**.

### [7] Barra di stato e misuratore di memoria dell'unità

Ancorato nella parte inferiore della finestra: 

- **Statistiche di selezione**: mostra le metriche in tempo reale per il pannello attivo: 
- Conteggio totale degli elementi e dimensione totale della cartella. 
- Numero di elementi selezionati e dimensione in byte selezionati combinati. 
- **Misuratore memoria unità**: indicatore visivo di utilizzo del disco che mostra il nome del volume attualmente montato (ad esempio, `Macintosh HD`), la capacità totale, la memoria utilizzata e la percentuale di spazio libero rimanente. 

---

## 3. Procedura dettagliata: sandbox dell'app macOS e autorizzazioni del file system

Il moderno macOS utilizza un rigoroso sandboxing di sicurezza delle applicazioni per proteggere i dati degli utenti da accessi non autorizzati. Quando si esegue ATBCmder (in particolare se installato tramite Mac App Store o distribuito con sandboxing abilitato), l'applicazione viene isolata nella propria directory contenitore sicura: 
`~/Library/Containers/com.aitobox.atbcmder/Data` 

Per impostazione predefinita, le applicazioni sandbox non possono ispezionare o modificare arbitrariamente i file all'esterno del loro contenitore a meno che l'utente non conceda esplicitamente l'autorizzazione tramite i pannelli aperti nativi di Apple. 

ATBCmder semplifica questo processo di onboarding con **Segnalibri con ambito di sicurezza**, consentendoti di concedere l'autorizzazione una volta e di usufruire di un accesso persistente e illimitato in tutte le sessioni future.

### Informazioni sui segnalibri con ambito di sicurezza

Quando autorizzi il percorso di una cartella utilizzando macOS `NSOpenPanel`: 

1. macOS emette un **segnalibro con ambito di sicurezza** crittografico (`NSURLBookmarkCreationWithSecurityScope`). 
2. ATBCmder serializza e salva questo segnalibro nella sua directory di configurazione: 
`~/Library/Application Support/ATBCmder/sandbox_bookmarks.plist` 

3. Ad ogni avvio dell'applicazione, ATBCmder risolve e attiva automaticamente questi segnalibri tramite `startAccessingSecurityScopedResource()`. 
4. Una volta concesso, non dovrai mai più autorizzare nuovamente queste directory.

### Procedura dettagliata per l'installazione guidata: utilizzo di `cm_GrantFilesystemAccess`

Per configurare le tue autorizzazioni al primo avvio o in qualsiasi momento successivo, segui questi passaggi:

#### Passaggio 1: aprire l'assistente per l'onboarding delle autorizzazioni

Dalla barra dei menu nativa, seleziona **File** (o **Guida**) → **Concedi accesso al filesystem…** o attiva il comando interno `cm_GrantFilesystemAccess`. Viene visualizzata la finestra di dialogo di onboarding: 

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

#### Passaggio 2: concedere l'accesso alla directory principale (`/`).

1. Fare clic su **"Concedi l'accesso alla directory principale (/)"**. 
2. ATBCmder richiama il foglio `NSOpenPanel` nativo di macOS, che punta al disco di root `Macintosh HD` (`/`). 
3. Fare clic su **"Concedi accesso"** (o **Apri**). 
4. Il pulsante viene aggiornato immediatamente a **"Accesso alla directory principale concesso ✓"** e viene disabilitato. 
5. **Cosa consente**: L'autorizzazione del percorso root `/` copre automaticamente tutte le directory utente (`~/Documents`, `~/Downloads`, `~/Desktop`, `~/Projects`, `/Applications`, ecc.) poiché i segnalibri con ambito di sicurezza ereditano automaticamente le autorizzazioni verso il basso per tutti i sottopercorsi secondari.

#### Passaggio 3: concedere l'accesso ai dischi esterni (`/Volumes`).

1. Fare clic su **"Concedi l'accesso ai dischi esterni (/Volumi)"**. 
2. Quando il pannello nativo visualizza `/Volumes`, fare clic su **"Concedi accesso"**. 
3. Il pulsante viene aggiornato a **"Accesso ai dischi esterni concesso ✓"**. 
4. **Cosa consente**: accesso in lettura/scrittura illimitato a unità USB esterne, unità Thunderbolt, schede SD, supporti di immagini disco DMG e volumi SMB/NFS/AFP montati in rete.

#### Passaggio 4: accesso selettivo cartella per cartella (alternativa)

Se preferisci non concedere un ampio accesso root ad ATBCmder, non è necessario fare clic su accesso root: 

- Quando navighi in una cartella non autorizzata (come una cartella esterna o un repository di progetto), ATBCmder rileva il limite dei permessi e visualizza un messaggio su richiesta: 
`ATBCmder requires your permission to access: /Users/username/SecretProject` 

- Fai clic su **"Concedi l'accesso alla cartella"**, approva la finestra di dialogo nativa e la directory specifica verrà inserita permanentemente nei segnalibri.

#### Passaggio 5: accesso completo al disco (FDA) per i dati di sistema protetti

> [!IMPORTANTE] 
> **Segnalibri Sandbox e accesso completo al disco (FDA)**: 
> 
> - **Segnalibri Sandbox** garantiscono l'accesso generale al filesystem a cartelle utente standard, file e unità esterne. 
> - **Accesso completo al disco (FDA)** è un'ulteriore autorizzazione alla privacy di macOS Transparency, Consent and Control (TCC) necessaria per ispezionare i dati personali sensibili di macOS (come cronologia di Safari, allegati di posta, messaggi, backup di Time Machine e cache di sistema). 
> 
> Se hai bisogno di gestire queste cartelle protette: 
> 
> 1. Fai clic su **"Apri impostazioni di accesso completo al disco…"** nella finestra di dialogo di onboarding. 
> 2. macOS apre **Impostazioni di sistema** → **Privacy e sicurezza** → **Accesso completo al disco**. 
> 3. Fare clic sul lucchetto o autenticarsi con Touch ID/password. 
> 4. Assicurati che l'interruttore accanto a **ATBCmder** sia impostato su **ON**.

### Revoca e ripristino delle autorizzazioni

Se mai avessi bisogno di reimpostare o revocare i segnalibri sandbox: 

1. Aprire la directory di configurazione di ATBCmder tramite il menu **Configurazione** → **Apri directory di configurazione** (`cm_OpenConfigDirectory`). 
2. Eliminare il file `sandbox_bookmarks.plist`. 
3. Riavviare ATBCmder. 
4. Per reimpostare le autorizzazioni TCC a livello di sistema macOS, esegui il comando seguente in macOS Terminale: 
   ```bash
   tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder
   ```
 

---

## 4. Impostazioni della lingua e personalizzazione dell'aspetto

ATBCmder è localizzato per flussi di lavoro globali e si integra perfettamente con le preferenze di aspetto di macOS.

### Internazionalizzazione e sostituzioni linguistiche

ATBCmder supporta **oltre 30 lingue**, tra cui inglese, cinese semplificato (简体中文), cinese tradizionale (繁體中文), tedesco (Deutsch), francese (Français), spagnolo (Español), russo (Русский), giapponese (日本語), italiano, polacco, coreano e altro ancora. 

![Language Settings](images/language_settings.png) 

- **Segui automaticamente la lingua del sistema**: per impostazione predefinita, ATBCmder rileva le impostazioni internazionali del tuo sistema macOS (`AppleLanguages`) all'avvio e applica automaticamente la traduzione corrispondente. 
- **Selezione manuale della lingua**: 
1. Apri Preferenze premendo `Cmd+,` o eseguendo `cm_Options`. 
2. Nel riquadro di navigazione a sinistra, seleziona **Lingua**. 
3. Scegli la lingua preferita dall'elenco a discesa. 
- **Ricarica in tempo reale (non è necessario riavviare)**: a differenza della maggior parte delle tradizionali utilità Mac che richiedono l'uscita e il riavvio dell'applicazione, ATBCmder ritraduce dinamicamente l'intera interfaccia (menu, barre degli strumenti, finestre di dialogo, descrizioni dei pulsanti e messaggi di stato) in tempo reale nel momento in cui selezioni una nuova lingua.

### Aspetto e temi

ATBCmder supporta pienamente le modalità di aspetto Chiaro e Scuro di macOS: 

- **Sincronizzazione dell'aspetto del sistema**: passa automaticamente dalla modalità Chiaro a quella Buio ogni volta che cambia l'aspetto del sistema macOS (ad esempio al tramonto o tramite Centro di Controllo). 
- **Opzioni tema**: 
- **Fusion / MacOS nativo**: estetica desktop classica e pulita che rispetta i colori accentati di macOS e la vivacità delle finestre. 
- **Tema elegante**: estetica moderna con controlli segmentati arrotondati, separatori sfumati sottili e barre delle schede a forma di pillola. 
- **Tavolozza modalità scura**: utilizza superfici color carbone scuro (`#2C2C2E` / `#242426`) con testo ad alto contrasto e icone di cartelle personalizzate, riducendo l'affaticamento degli occhi in ambienti con scarsa illuminazione. 
- **Tavolozza modalità luce**: sfondo bianco nitido con divisori grigi tenui (`#FAFBFD` / `#EEF2F7`) e bordi a contrasto chiaro. 

---

## 5. ⚡ Suggerimenti professionali e configurazioni di layout avanzate

Sfrutta appieno il motore di layout flessibile di ATBCmder per personalizzare il tuo spazio di lavoro per configurazioni di gestione dei dati multi-monitor, ultra-wide o specializzate.

### Suggerimento 1: salvataggio della posizione della finestra e dei rapporti di layout (`cm_ConfigSavePos`)

Quando organizzi il tuo spazio di lavoro, personalizzando le dimensioni della finestra, massimizzando su un display esterno o impostando una proporzione specifica del divisore centrale, puoi bloccare questa configurazione in modo che venga ripristinata in modo identico ogni volta: 

1. Organizza la finestra principale di ATBCmder e regola lo splitter centrale sul rapporto preferito. 
2. Selezionare il menu **Configurazione** → **Salva posizione e layout** o eseguire il comando interno: 
   ```
   cm_ConfigSavePos
   ```
 

3. Le dimensioni della finestra, le coordinate dello schermo, lo stato ingrandito e i rapporti del pannello vengono scritti direttamente in `atbcmder.xml`. 
4. In **Preferenze** → **Layout**, assicurati che **"Salva la posizione della finestra all'uscita"** sia selezionato per gli aggiornamenti continui automatici.

### Suggerimento 2: attivazione/disattivazione del layout a doppio pannello orizzontale (`cm_HorizontalFilePanels`)

Mentre i pannelli verticali affiancati sono standard per le operazioni sui file, i pannelli orizzontali impilati (pannello superiore e pannello inferiore) sono eccezionalmente utili quando: 

- Lavorare con nomi di file ultra lunghi che richiedono la larghezza dello schermo intero. 
- Confronto di colonne di metadati di file di grandi dimensioni (autorizzazioni, proprietari, checksum, dimensioni). 
- Lavorare su monitor o tablet verticali ruotati. 

Per cambiare layout: 

1. Selezionare il menu **Mostra** → **Pannelli orizzontali** o attivare il comando interno: 
   ```
   cm_HorizontalFilePanels
   ```
 

2. Quando la modalità orizzontale è attiva: 
- I pannelli sono impilati verticalmente (pannello superiore e pannello inferiore). 
- La barra degli strumenti centrale ruota automaticamente in una striscia orizzontale tra i pannelli superiore e inferiore. 
- Il cursore di trascinamento si adatta a un puntatore diviso verticalmente (`SplitVCursor`), consentendoti di ridimensionare facilmente il rapporto di altezza tra i pannelli superiore e inferiore.

### Suggerimento 3: Snap della divisione centrale con un clic

- **Saldo istantaneo 50/50**: fai doppio clic in un punto qualsiasi della barra di divisione centrale o della linea di separazione. I pannelli ritornano immediatamente alla divisione esatta del 50%/50%. 
- **Preimpostazioni rapporto**: nel tema "Elegante", facendo clic sui pulsanti segmentati al centro si aggancia il layout a `50:50`, `70:30` (enfatizzando il pannello di origine) o `30:70` (enfatizzando il pannello di destinazione).

### Suggerimento 4: ripristino automatico della sessione e persistenza dell'area di lavoro

ATBCmder dispone di un sottosistema di gestione delle sessioni intelligente (`SessionManager`) che garantisce che il tuo ambiente di lavoro sia sempre preservato: 

- **Archiviazione XML della sessione**: lo stato della sessione viene mantenuto automaticamente su `atbcmder_session.xml` all'interno della directory di configurazione (`~/Library/Application Support/ATBCmder/`). 
- **Memoria della geometria della finestra**: ripristina le coordinate esatte della finestra (`x`, `y`), le dimensioni (`width`, `height`), lo stato massimizzato e la proporzione del divisore centrale (`splitter_ratio`). 
- **Ripristino della scheda a doppio pannello**: 
- Ripristina tutte le schede aperte nei pannelli sinistro e destro all'avvio. 
- Ricorda l'indice della scheda attiva in ciascun pannello. 
- Carica automaticamente la directory di lavoro esatta per ogni scheda, eliminando l'attrito della navigazione manuale nelle cartelle di progetto più profonde. 
- **Blocco della posizione predefinita**: puoi anche bloccare in modo permanente la geometria della finestra corrente e il rapporto di divisione come configurazione di avvio predefinita utilizzando **Configurazione ➔ Salva posizione** (`cm_ConfigSavePos`). 

---

## 6. Avvisi di sicurezza e sistema: impostazione del tasto funzione macOS (Fn).

Se hai utilizzato Total Commander, Double Commander o Norton Commander sulla tastiera di un PC, le tue dita sono addestrate a utilizzare i tasti funzione della riga superiore (`F3` Visualizza, `F4` Modifica, `F5` Copia, `F6` Sposta, `F7` MkDir, `F8` Elimina). 

Tuttavia, le tastiere Apple gestiscono la riga delle funzioni in modo diverso di default. 

> [!ATTENZIONE] 
> ### 🍎 Conflitto hardware del tasto funzione macOS 
> Sulle tastiere Apple (tastiere integrate MacBook, Apple Magic Keyboard), i tasti della fila superiore sono impostati su **Funzioni hardware speciali macOS** (Luminosità display, Controllo missione, Spotlight, Dettatura, Non disturbare, Controlli multimediali e Volume audio). 
> 
> Se premi `F5` su un MacBook senza configurazione, macOS tenterà di regolare l'illuminazione della tastiera o attivare la dettatura invece di copiare i tuoi file!

### Opzione A: tieni premuto il tasto `Fn` (Globo 🌐) (configurazione macOS predefinita)

Se preferisci mantenere intatte le chiavi multimediali predefinite di Apple: 

- Tieni premuto il tasto **`Fn`** (o Globo 🌐) mentre premi un tasto funzione qualsiasi: 
- `Fn+F3`: Lister universale 
- `Fn+F4`: redattore interno 
- `Fn+F5`: copia file 
- `Fn+F6`: sposta i file 
- `Fn+F7`: Crea cartella 
- `Fn+F8`: elimina nel cestino

### Opzione B: abilitare i tasti funzione standard a livello di sistema (consigliato)

Se desideri riflessi Commander autentici e ad alta velocità a tasto singolo senza tenere premuto il modificatore `Fn`: 

1. Apri **Impostazioni di sistema** dal menu Apple (). 
2. Fai clic su **Tastiera** nella barra laterale. 
3. Fare clic sul pulsante **Scorciatoie da tastiera…**. 
4. Nell'elenco di navigazione a sinistra, seleziona **Tasti funzione**. 
5. Abilita l'interruttore: **"Utilizza i tasti F1, F2, ecc. come tasti funzione standard"**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Keyboard Shortcuts                                         │
├──────────────────┬──────────────────────────────────────────┤
│  Launchpad & Dock│  Use F1, F2, etc. keys as standard       │
│  Display         │  function keys                           │
│  Mission Control │                                          │
│  Keyboard        │  [ ON ───● ]                             │
│  Input Sources   │                                          │
│  Screenshots     │  When this option is selected, press the │
│ ▸ Function Keys  │  Fn key to use the special features      │
│  App Shortcuts   │  printed on each key.                    │
└──────────────────┴──────────────────────────────────────────┘
```
 

Una volta abilitato: 

- Premendo `F1`–`F12` si attivano direttamente i comandi ATBCmder immediatamente. 
- Per utilizzare i controlli di luminosità o volume, tieni semplicemente premuto `Fn` mentre premi il tasto. 

---

## 7. Riferimento rapido per i collegamenti essenziali a doppia matrice

ATBCmder fornisce il supporto completo per la tastiera a doppia matrice: utilizza le scorciatoie native di macOS (`Cmd ⌘`), i tasti Commander classici (`Fn`) o entrambi in modo intercambiabile.

| Azione principale | ID comando | macOS nativo (`Cmd ⌘`) | Comandante classico (`Fn`) | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Hotlist delle directory** | `cm_DirHotList` | `Cmd+D` / `⌘D` | `Ctrl+D` / `⌃D` | Apre il popup dei segnalibri della directory con ricerca fuzzy istantanea. | 
| **Elenco unità (sinistra/destra)** | `cm_LeftOpenDrives` / `cm_RightOpenDrives` | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | Apre il menu unità e volume per il pannello sinistro o destro (`Alt+D` per il pannello attivo). | 
| **Copia file** | `cm_Copy` | `Cmd+C` ➔ `Cmd+V` | `F5` (o `Fn+F5`) | Copia gli elementi selezionati dal pannello attivo al pannello inattivo. | 
| **Sposta file** | `cm_Move` | `Cmd+C` ➔ `Opt+Cmd+V` | `F6` (o `Fn+F6`) | Sposta gli elementi selezionati dal pannello attivo al pannello inattivo. | 
| **Visualizza nel Lister** | `cm_View` | `Space` / `Cmd+Y` | `F3` (o `Fn+F3`) | Apre il file in Universal Lister (codice, esadecimale, immagine, pdf, audio). | 
| **Visualizzazione rapida** | `cm_QuickView` | `Cmd+Q` / `Ctrl+Q` | `Ctrl+Q` | Visualizza l'anteprima dal vivo istantanea nel pannello opposto. | 
| **Modifica file** | `cm_Edit` | `Cmd+E` | `F4` (o `Fn+F4`) | Apre il file nell'editor di codice/testo integrato. | 
| **Nuova directory** | `cm_MkDir` | `Shift+Cmd+N` | `F7` (o `Fn+F7`) | Crea una nuova cartella nel pannello attivo. | 
| **Elimina nel cestino** | `cm_Delete` | `Cmd+Backspace` | `F8` (o `Fn+F8`) | Sposta in modo sicuro i file selezionati nel Cestino di macOS. | 
| **Rinomina in linea** | `cm_Rename` | `Return` | `F2` / `Shift+F6` | Rinomina il file evidenziato sul posto. | 
| **Pannello interruttori** | `cm_FocusSwap` | `Tab` | `Tab` | Sposta lo stato attivo della tastiera sul pannello opposto (`cm_SwitchPanel`). | 
| **Scambia sinistra/destra** | `cm_Exchange` | `Ctrl+U` | `Ctrl+U` | Scambia i percorsi delle directory tra i pannelli sinistro e destro. | 
| **Nuova scheda** | `cm_NewTab` | `Cmd+T` | `Ctrl+T` | Apre una nuova scheda di cartella nel pannello corrente. | 
| **Chiudi scheda** | `cm_CloseTab` | `Cmd+W` | `Ctrl+W` | Chiude la scheda attiva. | 
| **Modalità orizzontale** | `cm_HorizontalFilePanels` | Menu: Mostra ➔ Orizzontale | Menu: Mostra ➔ Orizzontale | Alterna il layout affiancato o impilato in alto e in basso. | 
| **Salva layout** | `cm_ConfigSavePos` | Menu: Configurazione ➔ Salva Pos | Menu: Configurazione ➔ Salva Pos | Salva le dimensioni correnti della finestra e le proporzioni del pannello. | 
| **Accesso alla sandbox** | `cm_GrantFilesystemAccess` | Menu: File ➔ Autorizzazioni | Menu: File ➔ Autorizzazioni | Avvia l'assistente di onboarding Sandbox dell'app macOS. | 
| **Preferenze** | `cm_Options` | `Cmd+,` | `Alt+O` | Apre la finestra di dialogo di configurazione di ATBCmder. |

---

## Passaggi successivi

Ora che hai imparato le basi del doppio pannello e configurato il tuo ambiente macOS, procedi al **[Capitolo 2: Schede di navigazione e cartelle](navigation_and_tabs.md)** per imparare come navigare rapidamente negli alberi di directory, padroneggiare aree di lavoro con più schede, salvare set di directory preferite, utilizzare hotlist istantanee e sfruttare visualizzazioni ricorsive di rami piatti.