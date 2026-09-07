# Capitolo 3: Operazioni quotidiane sui file e coda in background

Ogni giorno, i file manager vengono giudicati in base a un parametro: quanto velocemente, accuratamente e in sicurezza puoi manipolare i dati. In ATBCmder, non dovrai mai destreggiarti tra più finestre sovrapposte, sopportare errori di rilascio accidentali o aspettare pigramente mentre trasferimenti di file di grandi dimensioni bloccano lo schermo. 

Questo capitolo copre lo spettro completo delle operazioni sui file: flussi di lavoro di copia e spostamento direzionali, ridenominazione in linea sul posto, powermarking con caratteri jolly, interoperabilità drag-and-drop del sistema, gestione granulare delle collisioni, autorizzazioni e collegamenti simbolici UNIX e coda delle operazioni in background multi-thread. 

---

## 1. Quickstart visivo: il modello operativo direzionale

I file manager ortodossi utilizzano un modello direzionale **Sorgente ➔ Destinazione**. Quando avvii un trasferimento di file o la creazione di un collegamento, ATBCmder prende gli elementi selezionati nel **Pannello attivo** (Sorgente) ed esegue l'operazione direttamente nella directory aperta nel **Pannello inattivo** (Destinazione). 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE PANEL (Source)                              INACTIVE PANEL (Target)            │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Date    │   │  Name                        Size   │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ C │  ▸ client_portal            <DIR>   │
│  ✔ schema_migration.sql      42 KB   14:12   │ O │  ▸ microservices            <DIR>   │
│  ● notes.txt                  4 KB   09:30   │ P │  ● .env.production          2.1 KB  │
│                                              │ Y │                                     │
│  [2 files selected: 1.8 GB]                  │ ➔ │  [Destination ready for ingest]     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│                         ▼ Press F5 (Copy) or F6 (Move) ▼                               │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Copy file(s)                                                                     │  │
│  │ Copy selected 2 files?                                                           │  │
│  │ To: [/Volumes/ExternalSSD/Projects                                          ] […]│  │
│  │ [Options ▼]        [Add To Queue #1 ▾]       [Cancel]               [Start (⏎)]  │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Foglio informativo sulle operazioni core a doppia matrice

| Azione | Scorciatoia macOS | Chiave del comandante classico | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Copia nella destinazione** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia gli elementi selezionati nel pannello opposto. | 
| **Copia nello stesso pannello** | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Duplica gli elementi nel pannello attivo con la richiesta di rinomina. | 
| **Sposta nella destinazione** | `F6` / `Fn+F6` | `F6` | `cm_Move` | Sposta gli elementi selezionati nel pannello opposto. | 
| **Nuova cartella (MkDir)** | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Crea una nuova directory nel pannello attivo. | 
| **Elimina nel cestino** | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Sposta gli elementi selezionati nel Cestino di macOS. | 
| **Eliminazione definitiva** | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Ignora il cestino e scollega permanentemente i file. | 
| **Rinomina rapida in linea**| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Rinomina l'elemento attivo direttamente all'interno della riga della tabella. | 
| **Proprietà file** | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Apre le autorizzazioni UNIX, i timestamp e la finestra di dialogo dei metadati. | 
| **Calcola lo spazio della cartella**| `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcola i byte ricorsivi per le directory (`Ctrl+L` / `cm_CalculateSpace` per il totale selezionato). | 
| **Coda in background** | `Toolbar ⚡` | — | `cm_OperationsPanel` | Apre il monitor di trasferimento in background a 3 code. |

### Punto di riferimento visivo: la barra degli strumenti centrale

ATBCmder è dotato di una barra degli strumenti verticale dedicata ad azione rapida incorporata direttamente sul divisore centrale che separa i due pannelli: 

![Middle Toolbar](images/middle_toolbar.png) 
*La barra degli strumenti centrale centrale fornisce accesso immediato con il mouse a Visualizza (F3), Modifica (F4), Copia (F5), Sposta (F6), Nuova cartella (F7), Elimina (F8) e Scambia pannello.* 

---

## 2. Operazioni principali: Copia, Sposta, MkDir ed Elimina

La gestione quotidiana dei file ruota attorno a quattro azioni principali: copia, spostamento, creazione di directory ed eliminazione di file indesiderati.

### 2.1 Copia di file (`F5` / `cm_Copy`)

Per copiare file o directory: 

1. **Seleziona** uno o più elementi nel pannello attivo utilizzando la tastiera o il mouse. 
2. **Premi `F5`** (o `Fn+F5` sulle tastiere Apple oppure fai clic su **Copia** sulla barra degli strumenti centrale). 
3. Viene visualizzata la **finestra di dialogo Copia**: 
- **Linea di destinazione**: popolata automaticamente con il percorso della directory corrente del pannello opposto. Puoi modificare questo percorso manualmente, aggiungere un nuovo nome di sottocartella da copiare e creare contemporaneamente oppure fare clic su `...` per sfogliare. 
- **Avvia (`Enter`)**: avvia la copia immediata in primo piano con una finestra di dialogo di avanzamento in tempo reale. 
- **Aggiungi alla coda (`F2`)**: mette in coda il trasferimento per eseguirlo in background (vedere [Sezione 7.4](#74-background-operations-queue-cm_operationspanel)). 
- **Opzioni**: espande le regole di conflitto avanzate, la conservazione degli attributi e le verifiche del checksum. 

```
┌────────────────────────────────────────────────────────┐
│ Copy file(s)                                           │
│ Copy selected 3 files?                                 │
│ To: [/Volumes/Backup/Assets                          ] │
│ [Options ▼]   [Add To Queue #1 ▾]   [Cancel]   [Start] │
└────────────────────────────────────────────────────────┘
```

#### Duplicazione nel pannello (`Shift+F5` / `cm_CopySamePanel`)

Per clonare rapidamente un file nella directory corrente (ad esempio, creando un backup prima di modificare `nginx.conf`): 

- Evidenzia l'elemento e premi `Shift+F5` (o `⇧F5`). 
- ATBCmder richiede un percorso di destinazione nella *stessa* directory, consentendoti di inserire un nuovo nome (ad esempio, `nginx.conf.bak`).

#### Appunti standard di macOS (`Cmd+C` ➔ `Cmd+V`)

ATBCmder si integra completamente con le scorciatoie degli appunti del sistema macOS: 

- **`Cmd+C` (`⌘C`)**: copia i percorsi dei file selezionati negli appunti (`cm_CopyToClipboard`). 
- **`Cmd+V` (`⌘V`)**: incolla i file dagli appunti nel pannello attivo (`cm_PasteFromClipboard`). 
- **`Cmd+Option+V` (`⌥⌘V`)**: sposta i file degli appunti nel pannello attivo (`cm_PasteAsMove`). 

---

### 2.2 Spostamento di file (`F6` / `cm_Move`)

Lo spostamento trasferisce i file dalla directory di origine alla directory di destinazione: 

1. Seleziona gli elementi e premi **`F6`** (o `Fn+F6` / fai clic su **Sposta** sulla barra degli strumenti centrale). 
2. Si apre la **finestra di dialogo Sposta**, che mostra il percorso del pannello di destinazione. 
3. Premere **`Enter`** per eseguire: 
- **Spostamento dello stesso filesystem**: istantaneo e atomico sui volumi APFS/HFS+ aggiornando i riferimenti del catalogo del filesystem senza spostare i blocchi del disco non elaborato. 
- **Spostamento tra file system**: trasmette i dati tra volumi alla destinazione, verifica il completamento dei byte e rimuove in modo sicuro l'origine all'arrivo verificato. 
4. Se un file esistente con lo stesso nome risiede nella destinazione, ATBCmder mette in pausa e richiama la **Finestra di dialogo Sovrascrittura** (vedere [Sezione 6](#6-collision-handling-conflict-resolution)). 

---

### 2.3 Creazione di nuove directory (`F7` / `cm_MkDir`)

Hai bisogno di creare una struttura di cartelle al volo? 

1. Premere **`F7`** (o `Fn+F7` / `Shift+Cmd+N` / `cm_MkDir`). 
2. Viene visualizzato un messaggio semplice: `Enter folder name:`. 
3. Digitare il nome della cartella e premere `Enter`. 

```
┌──────────────────────────────────────────────┐
│ Create Directory                             │
│ Enter folder name:                           │
│ [2026-09-Q3_Reports                        ] │
│                      [Cancel]      [OK (⏎)]  │
└──────────────────────────────────────────────┘
```

#### Concatenamento di sottodirectory

Puoi creare gerarchie di cartelle nidificate in un unico passaggio. Digitando `deep/nested/project/assets` vengono creati immediatamente tutti e quattro i livelli della gerarchia (equivalente a `mkdir -p`).

#### Posizionamento della messa a fuoco automatica

Al momento della creazione, ATBCmder posiziona automaticamente il cursore del pannello direttamente sulla nuova cartella, pronta per l'inserimento immediato (`Enter`) o il trasferimento del file. 

---

### 2.4 Eliminazione di file: Cestino di macOS e Eliminazione permanente

La sicurezza e la recuperabilità sono fondamentali. ATBCmder supporta flussi di lavoro a doppia eliminazione: 

```
                  ┌────────────────────────────────────────┐
                  │          File Deletion Trigger         │
                  └───────────────────┬────────────────────┘
                                      │
                 ┌────────────────────┴───────────────────┐
                 ▼                                        ▼
    [ F8 / Delete / Cmd+Backspace ]             [ Shift+Delete / Shift+F8 ]
                 │                                        │
                 ▼                                        ▼
    macOS System Trash (.Trash)                  Permanent Unlink
      • Fully recoverable                         • Bypasses Trash
      • Put Back support in Finder                • Zero disk footprint
      • Volume .Trashes directory                 • Unrecoverable without deep carve
```

#### Eliminazione nel cestino di macOS (`F8` / `Delete` / `Cmd+Backspace`)

- I file selezionati vengono instradati tramite le API `send2trash` di macOS nel cestino del sistema. 
- I file possono essere controllati o ripristinati in qualsiasi momento tramite macOS Finder ("Rimetti indietro"). 
- Le finestre di dialogo di conferma possono essere abilitate o soppresse in **Preferenze** (`operations.confirm_delete`).

#### Cancellazione immediata permanente (`Shift+Delete` / `Shift+F8`)

- Ignora completamente il Cestino, scollegando immediatamente i file e liberando spazio di archiviazione. 
- Ideale per cancellare macchine virtuali multi-gigabyte o immagini disco in cui i limiti del buffer del cestino o l'esaurimento del disco impedirebbero la gestione temporanea.

#### Volumi senza supporto cestino (`trash_unavailable` rilevamento)

Quando si eliminano elementi da determinate condivisioni di rete (SMB, NFS), file system virtuali (`vfs://`) o unità esterne formattate con file system FAT/exFAT legacy privi di una directory `.Cestinoes`, macOS non può inviare elementi nel Cestino. 

In questi casi, ATBCmder attiva un avviso di sicurezza intelligente: 
```
┌────────────────────────────────────────────────────────┐
│ Trash Unavailable                                      │
│ The volume containing '/Volumes/NAS/backup.iso' does   │
│ not support Trash.                                     │
│ Would you like to permanently delete this file?        │
│                                                        │
│ [✔] Apply to all remaining items                       │
│              [Skip]               [Delete Permanently] │
└────────────────────────────────────────────────────────┘
```
 
Puoi scegliere di **Eliminare definitivamente**, **Salta** o selezionare **Applica a tutti gli elementi rimanenti** per gestire eliminazioni batch di grandi dimensioni in modo automatico.

#### Distruzione sicura multi-passaggio (`Alt+Delete` / `cm_Wipe`)

Per documenti sensibili, credenziali o chiavi private che non devono rimanere recuperabili tramite strumenti di ripristino flash raw: 

- Evidenzia l'elemento e seleziona **Menu File** → **Cancella** (`Alt+Delete` / `cm_Wipe`). 
- ATBCmder esegue una sovrascrittura multi-pass con pattern di bit e zeri casuali prima di scollegare l'inode. 

---

## 3. Rinomina rapida e modifica del nome in linea

Rinominare un singolo file non dovrebbe richiedere menu complessi o finestre di dialogo a comparsa. ATBCmder fornisce la modifica rapida delle righe della tabella sul posto. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Name                                  Ext      Size      Date Modified         │
│  ▸ [..]                                         --:--     drwxr-xr-x            │
│  ● Annual_Financial_Report_2025        .pdf     4.2 MB    Today, 11:20          │
│    ▲                                                                            │
│    └── [Editable Text Box: Stem highlighted, .pdf extension preserved]          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Attivazione della ridenominazione in linea

1. Evidenziare qualsiasi file o directory nel pannello. 
2. Premere **`F2`** o **`Shift+F6`** (`cm_RenameOnly`), oppure fare clic una volta sul nome del file già evidenziato. 
3. La cella della tabella si trasforma in un editor in linea (`QLineEdit`).

### Conservazione intelligente delle estensioni

Quando si rinomina un file come `invoice_september.pdf`: 

- ATBCmder preseleziona automaticamente solo il nome file di base (`invoice_september`). 
- L'estensione del file (`.pdf`) rimane non selezionata e intatta, impedendo la rimozione accidentale dell'estensione che interromperebbe le associazioni di file macOS. 
- Se desideri modificare l'estensione, utilizza semplicemente i tasti freccia o premi `Cmd+A` all'interno della casella di modifica.

### Scorciatoie da tastiera all'interno di Rinomina in linea

- **`Enter` (`Return`)**: conferma il nuovo nome e reindicizza il pannello. 
- **`Esc`**: Annulla la modifica e ripristina il nome originale senza modifiche. 
- **`Tab`**: conferma il nome corrente e inizia immediatamente a rinominare il file *successivo* nell'elenco, consentendo una rapida ridenominazione sequenziale dei file senza lasciare la tastiera. 

---

## 4. Tecniche di selezione: file di marcatura elettrica

Nei file manager tradizionali, la posizione del cursore e la selezione sono strettamente collegate: lo spostamento del cursore deseleziona i file precedenti a meno che non si tenga premuto `Cmd`. In ATBCmder, il **fuoco del cursore** e le **selezioni contrassegnate** sono disaccoppiati, consentendo una gestione batch di precisione. 

```
  Status Column:
  [ ]  Unselected (cursor may or may not be on row)
  [✔]  Marked / Selected (accumulated into operation payload)
```

### 4.1 Azioni di selezione globale

| Azione | Scorciatoia macOS | Chiave classica | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Seleziona tutto** | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Contrassegna ogni file e cartella nel pannello attivo. | 
| **Deseleziona tutto** | `Cmd+Shift+A` / `⇧⌘A`| `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Cancella tutti i contrassegni nel pannello attivo. | 
| **Inverti selezione**| `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Inverte lo stato di selezione: da contrassegnato diventa non contrassegnato e viceversa. | 

---

### 4.2 Selezione di modelli e caratteri jolly

La selezione dei caratteri jolly ti consente di scegliere come target centinaia di file specifici in una directory di migliaia con pochi tasti. 

```
┌────────────────────────────────────────────────────────┐
│ Mark Files by Pattern                                  │
│ Pattern: [*.jpg;*.png;*.webp                        ]  │
│                                                        │
│ [✔] Case sensitive       [ ] Regular expression        │
│                      [Cancel]                 [OK (⏎)] │
└────────────────────────────────────────────────────────┘
```

#### Seleziona gruppo (`Num+` / `cm_MarkPlus`)

- Premi **`Num+`** (Tastiera Plus o attiva il pulsante dal menu **Segna** → **Seleziona gruppo**). 
- Inserisci i caratteri jolly della shell standard: 
- `*.log`: contrassegna tutti i file che terminano con `.log`. 
- `*.jpg;*.png;*.webp`: elenco separato da punto e virgola per abbinare più estensioni contemporaneamente. 
- `data_2026_??.csv`: corrisponde ai file mensili a due cifre (da `01` a `12`). 
- `*draft*`: corrisponde a qualsiasi file contenente la parola "bozza". 
- Premi `Enter` per selezionare immediatamente tutte le voci corrispondenti.

#### Deseleziona gruppo (`Num-` / `cm_MarkMinus`)

- Premere **`Num-`** (Tastiera Meno). 
- Inserisci uno schema per rimuovere gli elementi corrispondenti da una selezione esistente (ad esempio, `*test*`).

#### Seleziona tutto con la stessa estensione (`Shift+Num+` / `cm_MarkCurrentExtension`)

- Posiziona il cursore su qualsiasi file (ad esempio, `app.tsx`). 
- Premere **`Shift+Num+`**. 
- Ogni singolo file `.tsx` nella directory corrente viene immediatamente selezionato. 

---

### 4.3 Selezione della portata e del punto

- **Selezione continua del blocco (`Shift+Up` / `Shift+Down`)**: tenendo premuto `Shift` mentre si naviga con i tasti freccia si espande un blocco di selezione contiguo verso l'alto o verso il basso. 
- **Attiva/disattiva elemento singolo (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: 
- Premendo `Space` contrassegna o deseleziona l'elemento sotto il cursore e calcola immediatamente la dimensione della directory se si trova su una cartella. 
- Premendo `Insert` (o `Fn+Return` su alcune tastiere Mac) contrassegna l'elemento e sposta automaticamente il cursore alla riga successiva, consentendo rapidi passaggi di selezione con un dito. 
- **Mouse e trackpad**: 
- `Cmd+Click`: attiva/disattiva la selezione su singole righe senza alterare le altre selezioni. 
- `Shift+Click`: estende la selezione dalla riga di ancoraggio corrente alla riga su cui si è fatto clic.

### Telemetria della selezione in tempo reale nella barra di stato

Ogni volta che i file vengono contrassegnati, la barra di stato inferiore si aggiorna immediatamente: 
```
[ 48 items | 12 selected (284.6 MB) ]   [ Volume Free: 184.2 GB / 494.3 GB ]
```
 
Ottieni informazioni situazionali in tempo reale sui payload esatti dei byte prima di impegnarti in copie di grandi dimensioni o eliminazioni. 

---

## 5. Interoperabilità drag-and-drop

ATBCmder tratta il drag-and-drop come un cittadino di prima classe, pur mantenendo la completa compatibilità con i flussi di lavoro ortodossi e l'ecosistema desktop macOS. 

```
       Dual-Panel Transfer                       External macOS Desktop
 ┌──────────────┐   ┌──────────────┐       ┌──────────────┐   ┌──────────────┐
 │ Left Panel   │══►│ Right Panel  │       │ ATBCmder     │══►│ Finder / App │
 │ (Source)     │   │ (Target)     │       │ Panel        │   │ (Desktop)    │
 └──────────────┘   └──────────────┘       └──────────────┘   └──────────────┘
```

### Trascinamento tra i pannelli

- Fare clic e trascinare gli elementi contrassegnati dal pannello attivo attraverso lo splitter centrale nel pannello inattivo. 
- Rilascia ovunque nella tabella dei file per avviare il trasferimento nella cartella di destinazione. 
- **Trascinamento in una sottocartella**: Se si rilascia direttamente in una riga di sottodirectory specifica, ATBCmder instrada il carico utile in quella sottocartella anziché nella radice del pannello.

### Interazione con macOS Finder, desktop e app esterne

- **Trascinamento in ATBCmder**: trascina i file dal Finder, dal desktop o dai download AirDrop direttamente nel pannello ATBCmder per copiarli o spostarli. 
- **Trascinamento fuori da ATBCmder**: trascina i file fuori da ATBCmder direttamente in VS Code, Terminalee (che incolla il percorso del file), Slack, Apple Mail o nelle caselle di caricamento del browser web.

### Tasti modificatori durante il trascinamento

| Tasto modificatore | Trascina Azione | Icona cursore del mouse | Descrizione | 
| :--- | :--- | :--- | :--- | 
| **Nessun modificatore** | Azione predefinita | Freccia standard | Copie tra volumi; si muove all'interno dello stesso volume. | 
| **Opzione (`⌥`)** | **Copia forzata** | Distintivo `+` verde | Copia sempre gli elementi, lasciando intatti i file di origine. | 
| **Comando (`⌘`)** | **Movimento forzato** | Distintivo con freccia curva | Sposta sempre gli elementi, scollegando i file di origine all'arrivo. |

### Cartelle caricate a molla

Quando si trascinano file su una directory nidificata in ATBCmder: 

- Passa il cursore del mouse sulla cartella di destinazione per **750 millisecondi**. 
- La cartella lampeggia automaticamente e si apre, navigando all'interno. 
- Puoi navigare su più livelli in profondità nelle sottodirectory nidificate senza rilasciare il pulsante del mouse, quindi rilasciare il carico utile esattamente dove desideri. 

---

## 6. Gestione delle collisioni e risoluzione dei conflitti

Le collisioni dei nomi sono il momento più pericoloso nella gestione dei file. Sovrascrivere il file sbagliato può distruggere ore di lavoro. ATBCmder implementa un motore di risoluzione dei conflitti di livello aziendale che ispeziona i file prima di sovrascriverli e fornisce controlli di sicurezza granulari. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Confirm File Overwrite                                                                 │
│                                                                                        │
│ File already exists at the destination.                                                │
│                                                                                        │
│ Source:      /Users/brain/Downloads/build_artifacts.zip                                │
│ Source info: 124,518,400 bytes, 2026-09-06 14:15                                       │
│                                                                                        │
│ Destination: /Volumes/Backup/build_artifacts.zip                                       │
│ Dest info:   118,204,112 bytes, 2026-09-01 09:30                                       │
│                                                                                        │
│ Would you like to overwrite it?                                                        │
│                                                                                        │
│ [Skip All]   [Overwrite All]   [Rename]   [Auto-rename]                                │
│                                                                                        │
│ [Cancel]                                        [Skip]               [Overwrite (⏎)]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### La suddivisione della finestra di dialogo di sovrascrittura

Quando si verifica una collisione del target, ATBCmder visualizza la finestra di dialogo **Conferma sovrascrittura file**: 

1. **Ispezione affiancata dei metadati**: 
- Confronta le dimensioni esatte dei file fino al singolo byte. 
- Confronta le date di modifica e i timestamp. Evidenzia in modo evidente se il file sorgente è più recente, più vecchio o di dimensioni identiche. 
2. **Pulsanti decisionali sull'elemento corrente**: 
- **Sovrascrivi (`Enter`)**: sostituisce il file di destinazione in conflitto con il file di origine. 
- **Salta**: lascia intatto il file di destinazione esistente e continua con l'elemento successivo nel batch di trasferimento. 
- **Annulla (`Esc`)**: interrompe immediatamente l'operazione rimanente, preservando tutti i file già trasferiti. 
3. **Azioni batch e di sicurezza**: 
- **Sovrascrivi tutto**: sovrascrive silenziosamente tutti i successivi file in conflitto in questo processo di trasferimento. 
- **Salta tutto**: salta silenziosamente tutti i file rimanenti in conflitto senza chiedere nuovamente conferma. 
- **Rinomina**: richiede di inserire un nuovo nome personalizzato per il file copiato prima della scrittura. 
- **Rinomina automatica**: aggiunge automaticamente un contatore incrementale (ad esempio, `build_artifacts_1.zip`, `build_artifacts_2.zip`), garantendo che entrambe le versioni vengano conservate fianco a fianco senza intervento manuale. 

---

### Criteri di collisione preconfigurati nella finestra di dialogo Copia

Per processi batch automatizzati di grandi dimensioni o backup non presidiati, è possibile preconfigurare in anticipo il comportamento dei conflitti nel pannello espandibile **Opzioni** della finestra di dialogo Copia/Sposta: 

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Copy Options Panel                                                           │
│ ┌─ Conflict Resolution ─────────────────┐ ┌─ Attributes & Behaviors ──────┐  │
│ │ When file exists:      [Ask          ▾]│ │ [✔] Check free space          │ │
│ │ When directory exists: [Merge        ▾]│ │ [✔] Copy date/time            │ │
│ │ When cannot set attr:  [Skip         ▾]│ │ [✔] Copy attributes           │ │
│ └───────────────────────────────────────┘ │ [ ] Drop readonly flag        │  │
│ ┌─ Filters ─────────────────────────────┐ │ [✔] Copy ownership (POSIX)     │ │
│ │ [ ] Exclude empty directories         │ │ [✔] Verify after copy: [SHA256]│ │
│ └───────────────────────────────────────┘ └───────────────────────────────┘  │
│ [Save these options as default]                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```
 

- **Quando il file esiste**: 
- `Ask`: Apre la finestra di dialogo di sovrascrittura ad ogni collisione (impostazione predefinita). 
- `Overwrite`: sovrascrive automaticamente i file esistenti. 
- `Skip`: salta automaticamente i file in conflitto. 
- `Overwrite older`: sovrascrive la destinazione solo se l'ora di modifica dell'origine è più recente. 
- `Rename copied`: aggiunge il suffisso del contatore (`_1`, `_2`) ai file copiati. 
- `Auto-rename target`: rinomina il file di destinazione esistente e scrive il nuovo file con il nome originale. 
- **Quando la directory esiste**: 
- `Merge`: unisce ricorsivamente il contenuto della cartella. I file secondari non in conflitto vengono copiati nelle cartelle esistenti. 
- `Ask` / `Overwrite` / `Skip`. 
- **Verifica avanzata e attributi**: 
- **Verifica spazio libero/Riserva spazio**: precalcola i byte di origine e garantisce che il volume di destinazione abbia una capacità adeguata prima dell'avvio. 
- **Verifica dopo la copia**: calcola i checksum crittografici (`SHA-256`, `MD5`, `SHA-1`, `CRC32`) sia sui file di origine che su quelli di destinazione scritti per garantire l'integrità dei dati al 100% contro la corruzione silenziosa dell'archiviazione. 
- **Segui collegamenti**: controlla se i collegamenti simbolici vengono copiati come riferimenti a puntatori o dereferenziati in copie fisiche complete. 
- **Copia data/ora e proprietà**: conserva le date di creazione POSIX, i timestamp di modifica e gli ID di proprietà di utenti/gruppi. 

---

## 7. ⚡ Suggerimenti degli esperti e approfondimento: potenza avanzata del file system

Padroneggiare la gestione a doppio pannello significa comprendere il substrato UNIX sottostante di macOS. Ecco le funzionalità avanzate progettate per sviluppatori, amministratori di sistema e professionisti dello storage.

### 7.1 Collegamenti simbolici e collegamenti reali (`cm_SymLink`, `cm_HardLink`)

macOS è basato su Darwin UNIX e fornisce due tipi di collegamento distinti: 

```
  Symbolic Link (Symlink):
  [ Symlink File ] ──(Path Pointer)──► [ Target File / Directory ]
  • Can cross volume boundaries
  • Can point to directories
  • Breaks if target is moved

  Hard Link:
  [ Hard Link Entry ] ──┐
                        ├──(Direct Inode Reference)──► [ Raw Disk Blocks ]
  [ Original Entry  ] ──┘
  • Cannot cross filesystem boundaries (same APFS container)
  • Files only (no directory hard links on macOS)
  • Data persists until all hard links are deleted
```

#### Creazione di collegamenti simbolici (`cm_SymLink`)

1. Evidenziare uno o più file/cartelle nel pannello attivo. 
2. Selezionare **Menu File** → **Crea collegamento simbolico...** (`cm_SymLink`). 
3. ATBCmder genera automaticamente un collegamento simbolico nel pannello opposto che punta al percorso assoluto dell'elemento sorgente. 
4. I collegamenti simbolici mostrano un flag di attributo `l` distinto (ad esempio, `lrwxr-xr-x`) nel pannello.

#### Creazione di collegamenti reali (`cm_HardLink`)

1. Evidenziare i file su un volume APFS/HFS+ locale. 
2. Selezionare **File menu** → **Crea collegamento reale...** (`cm_HardLink`). 
3. ATBCmder crea una voce di directory aggiuntiva nel pannello di destinazione condividendo esattamente lo stesso inode. 
4. Le modifiche scritte su uno dei file si riflettono immediatamente su entrambi. L'eliminazione di un file non elimina i dati finché il conteggio dei collegamenti non raggiunge lo zero. 

> [!NOTA] 
> **Restrizioni sui limiti dei collegamenti**: i collegamenti reali non possono oltrepassare i limiti del volume o essere creati su condivisioni di rete (`vfs://`). I collegamenti simbolici dovrebbero essere utilizzati ogni volta che si effettua il collegamento tra diverse unità o punti di montaggio remoti. 

---

### 7.2 Autorizzazioni e attributi dei file (`Alt+Enter` / `cm_SetFileProperties`)

Ispeziona e modifica gli attributi del file POSIX utilizzando la **finestra di dialogo Proprietà** completa: 

```
┌────────────────────────────────────────────────────────┐
│ Properties - production_api.py                         │
│ ┌─ Metadata ─────────────────────────────────────────┐ │
│ │ Full Path:     /Users/brain/work/production_api.py │ │
│ │ Size:          84,210 bytes                        │ │
│ │ Created:       2026-03-12 10:14:22                 │ │
│ │ Last Modified: 2026-09-06 13:45:01                 │ │
│ │ Last Accessed: 2026-09-06 15:30:10                 │ │
│ └────────────────────────────────────────────────────┘ │
│ ┌─ Permissions (UNIX) ───────────────────────────────┐ │
│ │ Octal Mode: [ 755 ]                                │ │
│ │ ┌─ Owner ──┐   ┌─ Group ──┐   ┌─ Others ─┐         │ │
│ │ │ [✔] Read │   │ [✔] Read │   │ [✔] Read │         │ │
│ │ │ [✔] Write│   │ [ ] Write│   │ [ ] Write│         │ │
│ │ │ [✔] Exec │   │ [✔] Exec │   │ [✔] Exec │         │ │
│ │ └──────────┘   └──────────┘   └──────────┘         │ │
│ └────────────────────────────────────────────────────┘ │
│                             [Cancel]         [OK (⏎)]  │
└────────────────────────────────────────────────────────┘
```
 

1. **Trigger**: evidenziare qualsiasi file o directory e premere **`Alt+Enter`** (`⌥⏎` / `cm_SetFileProperties`). 
2. **Revisione metadati**: visualizza il percorso completo del file, i byte esatti, l'ora di creazione (`btime`), l'ora di modifica (`mtime`) e l'ora dell'ultimo accesso (`atime`). 
3. **Matrice dei permessi UNIX**: 
- **Caselle di controllo interattive**: attiva/disattiva le autorizzazioni di lettura (`r`), scrittura (`w`) ed esecuzione (`x`) in modo indipendente per **Proprietario**, **Gruppo** e **Altri**. 
- **Input ottale bidirezionale**: digita i numeri ottali direttamente nel campo **Modalità ottale** (ad esempio, `755` per gli eseguibili, `644` per documenti standard, `600` per chiavi SSH private). Le caselle di controllo si aggiornano in tempo reale e viceversa. 
4. Premere `OK` (`Enter`) per applicare le modifiche tramite POSIX `chmod`. 

---

### 7.3 Calcolo dello spazio occupato (`cm_CountDirContent` / `cm_CalculateSpace` / `Space`)

Per impostazione predefinita, i file manager mostrano le dimensioni delle directory come `<DIR>` o `--` perché il calcolo ricorsivo delle dimensioni delle cartelle su milioni di file peggiorerebbe le prestazioni del file system. ATBCmder ti offre calcoli istantanei su richiesta: 

- **Dimensione cartella singola (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: premi `Space` mentre ti trovi su una cartella qualsiasi. ATBCmder calcola i byte ricorsivi totali della cartella in background e sostituisce `<DIR>` con la dimensione esatta (ad esempio, `14.2 GB`). 
- **Tutte le cartelle nel pannello attivo (`Alt+Shift+Enter` / `⌥⇧⏎` / `cm_CountDirContent`)**: 
- Esegue la scansione di ogni directory visibile nel pannello corrente. 
- Aggiorna le righe della tabella con totali di byte precisi. 
- **Dimensione cumulativa della directory selezionata (`Ctrl+L` / `⌃L` / `cm_CalculateSpace`)**: 
- Accumula byte ricorsivi totali per le cartelle selezionate e riepiloga il conteggio dei file, il conteggio delle cartelle e le dimensioni di archiviazione nella barra di stato. 

---

### 7.4 Coda delle operazioni in background (`cm_OperationsPanel`)

La copia di grandi riprese video da 50 GB o il trasferimento di centinaia di migliaia di piccoli file di codice sorgente non dovrebbero mai bloccare il tuo file manager. ATBCmder incorpora un **motore di trasferimento asincrono a 3 code**. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Background Operations                                                                  │
│ ┌─ [Queue #1 (Active)] ───────────┬─ [Queue #2 (Idle)] ───┬─ [Queue #3 (Idle)] ──────┐ │
│ │                                                                                    │ │
│ │ [RUNNING] Copy: 14 items -> /Volumes/BackupDrive/Media                             │ │
│ │   Current: RED_4K_Clip_0042.r3d (2.4 GB / 8.6 GB)                                  │ │
│ │   Speed: 428.5 MB/s | ETA: 00:01:14                                                │ │
│ │   [████████████████████████████████░░░░░░░░░░░░░░░░░░] 64%                         │ │
│ │                                                                                    │ │
│ │ [QUEUED] Move: 4 items -> /Volumes/BackupDrive/RAW_Audio                           │ │
│ │ [COMPLETED] Copy: 28 items -> /Users/brain/Projects/Website                        │ │
│ │                                                                                    │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
│                                         [Cancel Task]   [Clear Completed]   [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Perché tre code indipendenti?

- **Serializzato all'interno di ogni coda**: le attività all'interno della **coda n. 1** vengono eseguite una dopo l'altra in rigoroso ordine FIFO. Ciò impedisce lo sbattimento della testina del disco sui dischi rigidi meccanici ed evita i colli di bottiglia dei conflitti. 
- **Parallelo tra code**: **Queue #1**, **Queue #2** e **Queue #3** funzionano contemporaneamente su thread in background separati (`QThread`). È possibile assegnare trasferimenti destinati a **NVMe SSD A** alla Coda n. 1, trasferimenti destinati a **Unità USB esterna B** alla Coda n. 2 e caricamenti NAS di rete alla Coda n. 3, ottenendo il massimo throughput del bus aggregato.

#### Invio di lavori alla coda

1. Nel pannello attivo, seleziona i tuoi file e premi `F5` (Copia) o `F6` (Sposta). 
2. Invece di fare clic su Start, fare clic su **Aggiungi alla coda n. 1** (o fare clic sulla freccia a discesa per selezionare **Coda n.2** o **Coda n.3**). 
3. La finestra di dialogo si chiude immediatamente, liberando la finestra principale per continuare la navigazione e la navigazione.

#### Gestione della finestra della coda (`cm_OperationsPanel`)

- Fai clic sul pulsante **⚡ Coda** sulla barra degli strumenti principale o seleziona **Comandi del menu** → **Operazioni in background** (`cm_OperationsPanel`). 
- **Telemetria in tempo reale**: ispeziona le attività attive, i file attualmente in trasferimento, le velocità di trasferimento in streaming (ad esempio, `428.5 MB/s`) e i conti alla rovescia ETA calcolati. 
- **Stati codificati a colori**: 
- `[QUEUED]`: In attesa in fila. 
- `[RUNNING]`: trasferimento dati attivo. 
- `[COMPLETED]`: completato con successo con i conteggi di byte verificati. 
- `[FAILED]`: rilevato un errore I/O (messaggio di errore visualizzato in linea). 
- `[CANCELLED]`: interrotto dall'utente. 
- **Azioni di controllo**: 
- **Annulla attività**: termina in modo sicuro il trasferimento selezionato in coda o in esecuzione. 
- **Cancella completati**: elimina i lavori completati, non riusciti e annullati dall'elenco. 
- **Risoluzione dei conflitti in background**: se un'attività in background incontra un conflitto di sovrascrittura, ATBCmder genera una notifica consentendoti di risolverlo senza interrompere altre attività simultanee. 

---

## 8. Ricette pratiche passo dopo passo

### Soluzione 1: backup sicuro di più volumi con verifica del checksum

**Obiettivo**: eseguire il backup di un archivio fotografico di alto valore dal tuo Mac su un'unità APFS esterna, garantendo zero corruzione silenziosa e risolvendo potenziali duplicati in modo sicuro. 

```
Step 1: Open source in Left Panel (~/Pictures/2026_Photos).
Step 2: Open backup destination in Right Panel (/Volumes/SanDiskPro/Photo_Backup).
Step 3: Press Cmd+A (Select All) in Left Panel.
Step 4: Press F5 (Copy).
Step 5: Click [Options ▼] to expand advanced parameters:
        • Set 'When file exists' to: [Auto-rename target]
        • Check [✔] Verify after copy: [SHA-256]
        • Check [✔] Copy date/time
        • Check [✔] Check free space
Step 6: Click [Start].
```
 
*Risultato: ATBCmder calcola gli hash SHA-256 durante il flusso di copia, conferma l'esatta integrità del blocco sul disco esterno e numera automaticamente eventuali snapshot in conflitto senza intervento umano.* 

---

### Soluzione 2: Staging di precisione: selezione di caratteri jolly, inversione e distribuzione dei collegamenti simbolici

**Obiettivo**: in un repository misto contenente codice e artefatti compilati, selezionare tutti i file JavaScript, TypeScript e JSON ignorando gli output `.map` e `.log` compilati, quindi collegarli simbolicamente in una cartella testbed. 

```
Step 1: Navigate Left Panel to /Users/brain/dev/app/src.
Step 2: Navigate Right Panel to /Users/brain/dev/testbed/lib.
Step 3: Press Num+ (Select Group).
Step 4: Enter pattern: *.ts;*.tsx;*.js;*.json and press Enter.
Step 5: Notice you also matched *.test.ts files. Press Num- (Unmark Group).
Step 6: Enter pattern: *.test.ts and press Enter.
Step 7: Check your status bar: 84 files selected.
Step 8: Select Menu File → Create Symbolic Link... (cm_SymLink).
```
 
*Risultato: ottantaquattro collegamenti simbolici vengono creati istantaneamente nella cartella del banco di prova, puntando in modo chiaro ai file sorgente attivi.* 

---

### Soluzione 3: acquisizione parallela a throughput elevato utilizzando le code in background

**Obiettivo**: trasferire contemporaneamente due schede per fotocamere multimediali di grandi dimensioni sul RAID della workstation senza bloccare l'interfaccia utente o rallentare i lettori di schede. 

```
Step 1: Mount Card A (/Volumes/CFexpress_A) in Left Panel.
Step 2: Select all raw footage (Cmd+A), press F5 (Copy).
Step 3: Click [Add To Queue #1]. Transfer begins streaming in background.
Step 4: Open Card B (/Volumes/SD_Card_B) in Left Panel (Cmd+T for a new tab).
Step 5: Select all audio tracks (Cmd+A), press F5 (Copy).
Step 6: Click the queue dropdown chevron and choose [Queue #2].
Step 7: Press Toolbar ⚡ (cm_OperationsPanel) to watch both queues stream concurrently.
```
 
*Risultato: entrambe le schede vengono acquisite contemporaneamente alla piena saturazione del bus hardware mentre si continua a sfogliare file, modificare note o rinominare risorse.* 

---

## 9. Avvisi di sicurezza e sistema

> [!ATTENZIONE] 
> **Eliminazione permanente su unità esterne e di rete**: 
> Le unità esterne formattate con FAT32, exFAT o NTFS (tramite driver di terze parti) e le condivisioni di rete remote (SMB/SFTP) spesso non dispongono di una directory `.Cestinoes` del sistema macOS. Quando elimini elementi da questi volumi, ATBCmder ti avviserà che il Cestino non è disponibile. Confermando questa azione **elimina permanentemente** i file. Controlla sempre le intestazioni del percorso prima di confermare. 

> [!ATTENZIONE] 
> **Sovrascrittura di file in operazioni batch**: 
> Quando si utilizza **Sovrascrivi tutto** nella finestra di dialogo delle collisioni, ATBCmder sopprime ulteriori avvisi di collisione per l'intero lavoro. Se la directory di origine contiene nomi di file duplicati accidentalmente, i file di destinazione esistenti verranno sostituiti in modo irreversibile. Prendi in considerazione l'utilizzo della **Rinomina automatica** o **Sovrascrivi le versioni precedenti** per le copie batch automatiche. 

> [!IMPORTANTE] 
> **Limitazioni del collegamento reale APFS**: 
> I collegamenti reali non possono estendersi su diversi volumi APFS, partizioni del disco o immagini del disco. Se tenti di creare un collegamento reale tra due diversi punti di montaggio (come da `/Users/...` a `/Volumes/ExternalDrive/...`), l'operazione fallirà. Utilizza i **Collegamenti simbolici** (`cm_SymLink`) ogni volta che ti colleghi a diversi volumi di archiviazione. 

> [!CONSIGLIO] 
> **Ottimizzazione delle velocità di trasferimento NVMe**: 
> ATBCmder è ottimizzato per la moderna memoria unificata Apple Silicon e gli SSD PCIe 4.0/5.0 NVMe. Per impostazione predefinita, le operazioni sui file utilizzano un **buffer di copia da 1 MB** ad alte prestazioni (`operations.copy_buffer_size`). È possibile ottimizzare questo buffer in **Preferenze** → **Operazioni sui file** per adattarlo alle interfacce di rete 10GbE di fascia alta o agli array di archiviazione specializzati. 

---

## 10. Tabella di riferimento della tastiera a doppia matrice

| Categoria | Azione | Scorciatoia macOS | Chiave classica | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | :--- | 
| **Operazioni file principali** | Copia nella destinazione | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia gli elementi selezionati nel pannello inattivo. | 
| | Copia nello stesso pannello | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Clona il file nel pannello attivo con la richiesta di rinomina. | 
| | Sposta nella destinazione | `F6` / `Fn+F6` | `F6` | `cm_Move` | Sposta gli elementi selezionati nel pannello inattivo. | 
| | Nuova directory | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Crea una nuova directory o albero nidificato. | 
| | Elimina nel cestino | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Invia gli elementi selezionati al Cestino di macOS. | 
| | Eliminazione permanente | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Scollega immediatamente i file senza Cestino. | 
| | Cancellazione sicura | `Alt+Delete` / `⌥⌦` | `Alt+Delete` | `cm_Wipe` | Sovrascrive i file con dati casuali prima di scollegarli. | 
| **Rinomina** | Rinomina rapida in linea| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Rinomina l'elemento attivo direttamente nella riga della tabella. | 
| | Finestra di dialogo Rinomina | *Menu File* | — | `cm_Rename` | Apre la finestra di dialogo modale del testo per la ridenominazione. | 
| **Selezione** | Seleziona tutto | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Seleziona tutti i file e le cartelle. | 
| | Deseleziona tutto | `Cmd+Shift+A` / `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Cancella tutte le selezioni. | 
| | Inverti selezione | `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Inverte lo stato di selezione di tutti gli elementi. | 
| | Segna Gruppo | `Num+` | `Num+` | `cm_MarkPlus` | Seleziona gli elementi in base al carattere jolly o al modello RegEx. | 
| | Deseleziona gruppo | `Num-` | `Num-` | `cm_MarkMinus` | Deseleziona gli elementi in base al modello di caratteri jolly. | 
| | Stessa estensione | `Shift+Num+` | `Shift+Num+` | `cm_MarkCurrentExtension`| Seleziona tutti gli elementi con la stessa estensione di file. | 
| | Attiva/disattiva selezione | `Space` / `Insert` | `Insert` / `Space` | `cm_SelectOrDeselectFile` | Attiva/disattiva la selezione dell'elemento e scende. | 
| **Appunti** | Copia negli appunti | `Cmd+C` / `⌘C` | `Ctrl+C` | `cm_CopyToClipboard` | Copia i percorsi dei file negli appunti di sistema. | 
| | Taglia negli appunti | `Cmd+X` / `⌘X` | `Ctrl+X` | `cm_CutToClipboard` | Taglia i percorsi dei file negli appunti di sistema. | 
| | Incolla Appunti | `Cmd+V` / `⌘V` | `Ctrl+V` | `cm_PasteFromClipboard` | Incolla i file degli appunti nel pannello attivo. | 
| | Incolla come Sposta | `Cmd+Option+V` / `⌥⌘V`| `Ctrl+Alt+V` | `cm_PasteAsMove` | Sposta i file degli appunti nel pannello attivo. | 
| | Copia percorso completo | *Menu Modifica* | — | `cm_CopyFullPath` | Copia il percorso UNIX assoluto negli appunti. | 
| | Copia nome file | *Menu Modifica* | — | `cm_CopyFileNameToClip` | Copia il nome del file negli appunti. | 
| **Link e spazio** | Crea collegamento simbolico | *Menu File* | — | `cm_SymLink` | Crea un collegamento simbolico nel pannello di destinazione. | 
| | Crea collegamento reale | *Menu File* | — | `cm_HardLink` | Crea un collegamento reale nel pannello di destinazione. | 
| | Proprietà / Chmod | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Apre autorizzazioni, chmod ottale e timestamp. | 
| | Calcola lo spazio | `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcola le dimensioni della directory ricorsiva (`Ctrl+L` / `cm_CalculateSpace` per il totale selezionato). | 
| **Coda di trasferimento**| Coda in background | `Toolbar ⚡` | — | `cm_OperationsPanel` | Apre il monitor di trasferimento in background a 3 code. |

--- 

<div align="center"> 
<p>Ora che hai imparato le operazioni quotidiane sui file, le tecniche di selezione e i trasferimenti in background:</p> 
<p><strong><a href="viewers_and_editors.md">Procedi al capitolo 4: Lister universale ed editor integrati &rarr;</a></strong></p> 
</div>