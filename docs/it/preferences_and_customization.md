# Capitolo 7: Preferenze e personalizzazione

Un file manager veramente efficiente deve adattarsi al tuo flusso di lavoro, non costringerti ad adattarti alle sue impostazioni predefinite. Ogni ingegnere, amministratore di sistema, archivista digitale e professionista creativo possiede memoria muscolare, requisiti di visualizzazione e abitudini operative distinti: alcuni si affidano rigorosamente ai tasti funzione ortodossi di Norton Commander/Total Commander (`F1`–`F10`), mentre altri si aspettano scorciatoie native di macOS (`Cmd+C`, `Cmd+V`, `Cmd+O`); alcuni richiedono l'adattamento automatico dinamico delle colonne con metriche tipografiche sub-pixel, mentre altri necessitano di confini di colonna rigidi e fissi; alcuni richiedono un monitoraggio aggressivo degli eventi del file system in tempo reale, mentre altri vengono eseguiti su condivisioni di rete ad alta latenza dove il polling passivo è obbligatorio. 

ATBCmder è progettato da zero per una configurabilità totale. Attraverso la **finestra di dialogo Preferenze** modulare (`Cmd+,` / `⌘,` / `cm_Options`), l'intuitivo **editor di tasti di scelta rapida** con rilevamento dei conflitti in tempo reale, il **motore di adattamento automatico delle colonne** intelligente, le **associazioni di file** personalizzabili con macro token esterne e i **pacchetti di configurazione ZIP** portatili (`cm_ExportConfiguration`), ATBCmder ti consente di ottimizzare ogni dimensione del tuo ambiente a doppio pannello e portare la tua configurazione personalizzata senza problemi su tutti i tuoi sistemi Mac. 

---

## 1. Avvio rapido visivo: Centro preferenze e matrice dei comandi

ATBCmder centralizza tutte le impostazioni dell'utente in un'architettura di preferenze unificate composta da 16 pagine di configurazione specializzate, un motore di mappatura dei tasti di scelta rapida isolato e un livello di archiviazione XML atomico. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          ATBCMDER PREFERENCES CENTER (Cmd+,)                           │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  CATEGORY NAVIGATION │  ACTIVE CONFIGURATION PAGE                                      │
├──────────────────────┼─────────────────────────────────────────────────────────────────┤
│  • General           │  Column Auto-Fit Mode:                                          │
│  • Hotkeys           │  [ Average Mode (Smart Padding)                       ▼ ]       │
│  • Language          │                                                                 │
│  • File Views        │  Average Mode Padding Factor: [ 1.25x ]                         │
│  • Auto Refresh      │                                                                 │
│  • Operations        │  Sorting Behavior:                                              │
│  • Packer            │  [X] Natural (numeric) sorting: photo1.jpg < photo10.jpg        │
│  • Plugins           │  [X] Case-sensitive sorting                                     │
│  • Directory Hotlist │  Folder Position: [ Folders First                     ▼ ]       │
│  • Favorite Tabs     │                                                                 │
│  • Editor            │  Thumbnail Generation:                                          │
│  • Viewer            │  Default Size: [ 128 px ]   Cache: [~/.cache/atbcmder]          │
│  • Toolbar           │                                                                 │
│  • Middle Toolbar    │  Date/Time Format:                                              │
│  • Log               │  Long Format: [ %Y-%m-%d %H:%M:%S                             ] │
│  • Quick Search      │                                                                 │
│  • Semantic Filter   │  [ Revert Changes ]                   [ Apply ] [ OK ] [Cancel] │
├──────────────────────┴─────────────────────────────────────────────────────────────────┤
│  CONFIG BACKEND:  atbcmder.xml  |  atbcmder_hotkeys.xml  |  favtabs.xml  |  hotlist.xml│
│  PORTABILITY:     cm_ExportConfiguration (ZIP)  ➔  cm_ImportConfiguration (ZIP)        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Foglio informativo sulle preferenze e personalizzazione della doppia matrice

| Azione | Scorciatoia macOS | Chiave del comandante classico | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Apri Preferenze** | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | Apre la finestra di dialogo principale Preferenze multipagina. | 
| **Configura tasti di scelta rapida** | `Cmd+,` ➔ Tasti di scelta rapida | — | `cm_Options` (Tasti di scelta rapida) | Accesso diretto alla tabella di associazione delle scorciatoie da tastiera. | 
| **Configura associazioni file**| Menù: Configurazione | — | `cm_FileAssoc` | Mappa le estensioni dei file su visualizzatori/editor interni o esterni. | 
| **Impostazione della lista preferita delle directory** | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | Modifica i segnalibri delle cartelle salvate e i tasti di scelta rapida attivi (`Ctrl+D` per aprire la hotlist). | 
| **Configura le schede preferite** | Menù: Configurazione | — | `cm_ConfigFavoriteTabs`| Gestisce i set di schede di cartelle a doppio pannello salvati. | 
| **Configura archivisti** | Menù: Configurazione | — | `cm_ConfigArchivers` | Configura gli eseguibili dell'archiviatore esterno e le regole di compressione. | 
| **Esporta configurazione** | Menù: Configurazione | — | `cm_ExportConfiguration`| Esporta tutti i file XML di configurazione in un bundle `.zip` portatile. | 
| **Importa configurazione** | Menù: Configurazione | — | `cm_ImportConfiguration`| Ripristina i file XML di configurazione da un bundle `.zip`. | 
| **Apri directory di configurazione** | Menù: Configurazione | — | `cm_OpenConfigDirectory`| Naviga nel pannello attivo direttamente nella cartella di configurazione di ATBCmder. | 
| **Salva immediatamente le impostazioni** | Menù: Configurazione | — | `cm_ConfigSaveSettings`| Scarica immediatamente tutte le modifiche alla configurazione in memoria sul disco. | 
| **Salva posizione finestra** | Menù: Configurazione | — | `cm_ConfigSavePos` | Persiste la geometria corrente della finestra e le proporzioni di divisione. | 
| **Attiva/disattiva le descrizioni comandi dei file** | Preferenze: Visualizzazioni file | — | *(Preferenze)* | Abilita o disabilita le descrizioni comandi dettagliate dei metadati mobili. | 
| **Concedere autorizzazioni di sistema** | Menù: Configurazione | — | `cm_GrantFilesystemAccess`| Avvia la guida di onboarding per l'accesso completo al disco completo dell'app Sandbox per macOS. | 

---

## 2. La finestra di dialogo Preferenze Anatomia e navigazione (`Cmd+,` / `cm_Options`)

La sala di controllo centrale per ATBCmder è la **finestra di dialogo Preferenze**. Puoi evocarlo in qualsiasi momento premendo **`Cmd+,`** (`⌘,`) su macOS, scegliendo **ATBCmder ➔ Preferenze...** dal menu dell'applicazione o eseguendo `cm_Options` tramite la barra dei comandi semantica (`/`).

### 2.1 Layout della finestra di dialogo e modello di interazione

La finestra di dialogo Preferenze utilizza un layout suddiviso in dettagli principali progettato per chiarezza e accessibilità da tastiera: 

1. **Elenco di navigazione delle categorie (a sinistra)**: un selettore verticale con un carattere dell'interfaccia leggibile da 14 punti e una barra laterale fissa da 195 pixel. Naviga tra le categorie utilizzando i tasti freccia `Up` e `Down` oppure fai clic con il mouse. 
2. **Area di scorrimento della pagina in pila (a destra)**: un ampio pannello di configurazione racchiuso in un `QScrollArea` senza cornice. Quando si passa da una categoria all'altra, la pagina delle impostazioni corrispondente viene visualizzata senza problemi senza causare il ridimensionamento della finestra di dialogo o lo sfarfallio della finestra. 
3. **Matrice dei pulsanti di azione (in basso)**: 
- **OK**: convalida tutti i campi di input su tutte le pagine, scrive le impostazioni modificate sul disco (`atbcmder.xml`), attiva la ritraduzione e gli aggiornamenti del tema e chiude la finestra di dialogo. 
- **Applica**: conferma immediatamente tutti i parametri modificati senza chiudere la finestra di dialogo. Questo è l'ideale per testare i caratteri dell'interfaccia utente, le variazioni del tema, il riempimento delle colonne e gli intervalli di aggiornamento automatico in tempo reale. 
- **Annulla**: elimina eventuali modifiche non salvate apportate nella sessione corrente. Se hai visualizzato l'anteprima di un tema senza applicarlo, ATBCmder ripristina automaticamente l'interfaccia al tema precedente. 

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Preferences Dialog Sidebar Navigation                                      │
├────────────────────────────────────────────────────────────────────────────┤
│  [ General ]         Basic UI, file lists, confirmation prompts, theme     │
│  [ Hotkeys ]         Keyboard shortcuts, context scoping, conflict manager │
│  [ Language ]        30+ real-time GUI translations without restart        │
│  [ File Views ]      Sorting rules, column auto-fitting, datetime formats  │
│  [ Auto Refresh ]    File monitoring events, polling, background sleep     │
│  [ Operations ]      Collision defaults (overwrite/rename), permissions    │
│  [ Packer ]          Archive formats (ZIP, 7Z, TAR), external binaries     │
│  [ Directory Hotlist]Bookmarks management, target panels, drag-and-drop    │
│  [ Favorite Tabs ]   Dual-panel workspace sets, layout persistence         │
│  [ Editor ]          Internal code editor typography, external editor CLI  │
│  [ Viewer ]          Universal Lister fonts, image rendering, external CLI │
│  [ Toolbar ]         Main button bar layout, custom commands, icon picker  │
│  [ Middle Toolbar ]  Middle splitter button bar, quick actions             │
│  [ Log ]             Operation audit trails, file logging, rotation        │
│  [ Quick Search ]    In-panel letter search, matching algorithms           │
│  [ Semantic Filter ] Natural language command input, spotlight integration │
│  [ Tabs ]            Folder tab bar styling, close buttons, locking rules  │
└────────────────────────────────────────────────────────────────────────────┘
```
 

---

### 2.2 Directory completa delle pagine di configurazione

Ogni pagina nella finestra di dialogo Preferenze indirizza un dominio funzionale specifico:

| Pagina | Modulo di implementazione | Controlli di configurazione primari | 
| :--- | :--- | :--- | 
| **Generale** | `page_general.py` | Visibilità dei file nascosti, icone dei file, finestre di dialogo di conferma dell'eliminazione/sovrascrittura, integrazione del cestino di sistema, dimensione del buffer di copia/spostamento (4 KB–10 MB), selezione del tema, dimensione del carattere globale, commutazione minimizza nel vassoio e tasto di scelta rapida globale mostra/nascondi finestra (`Cmd+Opt+H`). | 
| **Tasti di scelta rapida** | `page_hotkeys.py` | Ricerca di comandi multi-contesto, associazione di accordi di scorciatoie primarie e secondarie, avvisi automatici di collisione di scorciatoie e ripristino delle impostazioni di fabbrica. | 
| **Lingua** | `page_language.py` | Selettore di localizzazione dinamico che supporta oltre 30 lingue (inglese, tedesco, francese, cinese semplificato, giapponese, russo, spagnolo, ecc.) con traduzione istantanea dell'interfaccia utente dal vivo. | 
| **Visualizzazioni file** | `page_fileview.py` | Ordinamento numerico naturale e con distinzione tra maiuscole e minuscole, posizionamento dell'ordinamento delle cartelle (prima le cartelle, prima i file, misto), posizionamento dei file nuovi/aggiornati, modalità di adattamento automatico delle colonne (fissa, media, massima), dispositivo di scorrimento del fattore di riempimento e formati data/ora personalizzati. | 
| **Aggiornamento automatico** | `page_auto_refresh.py` | Monitoraggio della creazione/eliminazione/rinomina del file system, monitoraggio della modifica degli attributi dei file, intervallo di fallback del polling del timer, attivazione/disattivazione della disattivazione in background ed elenco dei filtri di esclusione delle directory. | 
| **Operazioni** | `page_operations.py` | Policy predefinite di collisione di file (Chiedi, Sovrascrivi, Salta, Sovrascrivi meno recenti, Rinomina automaticamente destinazione), policy di collisione di directory (Chiedi, Unisci, Sovrascrivi, Salta), preallocazione dello spazio libero, gestione dei collegamenti simbolici, conservazione di autorizzazioni/timestamp e verifica. | 
| **Imballatore** | `page_packer.py` | Formato di archivio di compressione predefinito (`zip`, `7z`, `tar.gz`, `tar.bz2`, `tar.xz`, `tar`), percorsi eseguibili esterni per 7-Zip, Utilità GNU Tar, Gzip, Bzip2 e XZ. | 
| **Lista delle directory**| `page_hotlist.py` | Gestore interattivo dei segnalibri: aggiungi, rimuovi e riordina (`Drag & Drop`) directory preferite, specifica percorsi di destinazione a doppio pannello e assegna tasti di accesso rapido. | 
| **Schede preferite** | `page_favorite_tabs.py` | Gestore istantanee dell'area di lavoro: salva, rinomina, riordina e ripristina i layout di directory a doppio pannello multischeda. | 
| **Redattore** | `page_editor.py` | Attiva/disattiva la famiglia di caratteri dell'editor del codice interno, la dimensione del carattere, la larghezza del punto di tabulazione, il ritorno a capo automatico e il numero di riga; percorso eseguibile dell'editor esterno e argomenti della riga di comando. | 
| **Visualizzatore** | `page_viewer.py` | Tipografia del testo Universal Lister, tabulazioni, margini, ritorno a capo, visibilità del cursore, opzioni di rendering delle immagini (rotazione automatica EXIF, modalità zoom, griglia di trasparenza) e strumento CLI visualizzatore esterno. | 
| **Barra degli strumenti** | `page_toolbar.py` | Personalizzazione della barra dei pulsanti superiore: dispositivo di scorrimento delle dimensioni delle icone (16-64 px), dispositivo di scorrimento delle dimensioni della barra, stile dei pulsanti piatti, attivazione/disattivazione delle didascalie, albero della gerarchia dei comandi e finestra di dialogo di selezione delle icone personalizzata. | 
| **Barra degli strumenti centrale** | `page_toolbar.py` | Configurazione della barra degli strumenti con divisione verticale centrale: dimensioni delle icone, pulsanti di azione e riordino del layout. | 
| **Registro** | `page_log.py` | Registrazione di controllo operativo: destinazione del file di registro, sostituzione del percorso del token, dimensione massima del file di registro, comportamento di rotazione del registro e filtri eventi operativi specifici (copia, spostamento, eliminazione, decompressione). | 
| **Ricerca rapida** | `page_quicksearch.py` | Modalità di ricerca rapida da tastiera (corrispondenza esatta, inizio, fine, caratteri jolly), distinzione tra maiuscole e minuscole e timeout di chiusura automatica. | 
| **Filtro semantico** | `page_semantic_filter.py` | Comportamento della barra dei comandi in linguaggio naturale incorporato (`/`), backend del provider di ricerca e rimbalzo dei suggerimenti. | 
| **Schede** | `page_tabs.py` | Aspetto della scheda della cartella: visibilità del pulsante di chiusura, layout della scheda su più righe rispetto alle schede a scorrimento, comportamento di navigazione della scheda bloccata e conferme di chiusura della scheda. |

---

### 2.3 Tema in tempo reale e cambio dinamico della lingua

A differenza delle utilità legacy che richiedono la chiusura e il riavvio dell'applicazione dopo aver modificato le impostazioni dell'aspetto, ATBCmder offre **Temi e localizzazione hot-swappable**: 

1. **Anteprime temi**: apri **Generale**, scegli tra `Classic`, `Light`, `Dark` o `macOS Native (Stylish)` e osserva immediatamente la modifica dello stile della finestra tramite l'iniezione del foglio di stile Qt. Se premi **Annulla**, il tema precedente verrà ripristinato senza problemi. 
2. **Traduzione istantanea**: apri **Lingua**, seleziona il tuo dialetto preferito dall'elenco di oltre 30 lingue tradotte e fai clic su **Applica**. Il titolo della finestra, la barra laterale della categoria, i menu, i pulsanti, le barre di stato e le richieste di dialogo vengono nuovamente visualizzati immediatamente nella lingua di destinazione attraverso la pipeline di traduzione dinamica `tr()` di ATBCmder. 

![Language Settings](images/language_settings.png) 
*Figura 7.1: La pagina Preferenze lingua che consente la localizzazione istantanea e con riavvio zero in oltre 30 lingue supportate.* 

---

## 3. Personalizzazione delle scorciatoie da tastiera e gestione dei conflitti

L'efficienza della tastiera è la filosofia fondamentale della gestione dei file a doppio pannello. L'**Hotkey Editor** di ATBCmder (`page_hotkeys.py`) fornisce il pieno controllo sugli accordi di scelta rapida applicando al contempo un rigoroso isolamento del contesto e la prevenzione delle collisioni. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              HOTKEY CONFIGURATION PAGE                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Hotkey Context: [ FilePanel                                                 ▼ ]       │
│  Filter Commands: [ copy                                                     ] ⌧       │
├──────────────────────┬────────────────────────┬───────────────────┬────────────────────┤
│ Command ID           │ Description            │ Primary Shortcut  │ Secondary Shortcut │
├──────────────────────┼────────────────────────┼───────────────────┼────────────────────┤
│ cm_Copy              │ Copy Files or Folders  │ F5                │ Cmd+C              │
│ cm_CopySamePanel     │ Duplicate File in Pane │ Shift+F5          │ Cmd+D              │
│ cm_CopyRightPanel     │ Copy to Right Panel    │ Alt+F5            │                   │
│ cm_CopyFullNamesToClip│ Copy Full Path Names   │ Ctrl+Shift+C      │ Cmd+Opt+C         │
├──────────────────────┴────────────────────────┴───────────────────┴────────────────────┤
│  [ Edit Shortcut... ]           [ Clear Shortcuts ]            [ Reset to Defaults ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Isolamento e ambito del contesto

Per evitare l'esaurimento delle scorciatoie, ATBCmder separa le combinazioni di tasti in **Ambiti di contesto**. Una scorciatoia definita in un contesto non interferisce con tasti identici in finestre non correlate: 

- **Principale**: scorciatoie globali dell'applicazione disponibili in tutte le finestre (ad esempio, `Cmd+,` per Preferenze, `Cmd+Q` per Esci). 
- **FilePanel**: attivo ogni volta che l'elenco dei file di sinistra o di destra ha il focus della tastiera (ad esempio, `F5` copia, `Space` calcola la dimensione della directory, `Backspace` passa alla directory principale). 
- **Visualizzatore**: attivo all'interno di Universal Lister (`F3`): controlla le codifiche del testo, la visualizzazione esadecimale (`2` / Modalità esadecimale), lo zoom delle immagini e la riproduzione multimediale. 
- **Editor**: attivo all'interno dell'editor di testo integrato (`F4`): controlla l'evidenziazione della sintassi, il rientro, la ricerca/sostituzione (`Cmd+F`) e il salvataggio dei file (`Cmd+S`). 
- **Differisce**: attivo all'interno di Diff. file affiancati: navigazione di blocchi (`F7`/`F8`), sincronizzazione di linea e operazioni di unione. 
- **FindFiles**: attivo nella finestra di dialogo Ricerca multi-filtro: attivazione di nuove ricerche, navigazione dei risultati e inserimento nella casella di riepilogo. 
- **MultiRename**: attivo nello strumento Batch Multi-Rename: manipolazione del contatore, inserimento di token ed esecuzione. 

---

### 3.2 Architettura a doppia associazione (scorciatoie primarie e secondarie)

ATBCmder ti permette di assegnare **due distinte combinazioni di scorciatoie** ad ogni singolo comando: 

- **Scorciatoia primaria**: il tuo accordo di memoria muscolare principale (ad esempio, `F5` per gli utenti di Commander classico). 
- **Scorciatoia secondaria**: un accordo alternativo (ad esempio, `Cmd+C` per l'ergonomia nativa di macOS). 

Entrambe le scorciatoie rimangono attive contemporaneamente nel contesto specificato. Durante la navigazione nei menu, ATBCmder visualizza automaticamente la scorciatoia principale accanto al testo della voce di menu per un chiaro riferimento visivo. 

---

### 3.3 Procedura dettagliata: personalizzare una scorciatoia da tastiera

Segui questa pratica procedura dettagliata per associare nuovamente un comando esistente o assegnare una scorciatoia secondaria: 

1. Premi **`Cmd+,`** (`⌘,`) per aprire Preferenze e seleziona **Tasti di scelta rapida** nella barra laterale sinistra. 
2. Selezionare il **Contesto tasto di scelta rapida** appropriato dal menu a discesa (ad esempio, `FilePanel`). 
3. Digitare il nome del comando o una parola chiave nella casella **Comandi filtro** (ad esempio, `Wipe` o `Terminale`). La tabella filtra le voci corrispondenti in tempo reale. 
4. Fare doppio clic sulla riga di comando oppure selezionare la riga e fare clic su **Modifica...**. 
5. Nella finestra di dialogo **Modifica tasto di scelta rapida**: 
- Fai clic all'interno della casella **Scorciatoia primaria** e premi la combinazione di tasti desiderata (ad esempio, `Ctrl+Alt+T`). ATBCmder cattura l'accordo in modo pulito, limitando le sequenze a un singolo accordo simultaneo. 
- (Facoltativo) Fai clic all'interno della casella **Scorciatoia secondaria** e premi una combinazione alternativa (ad esempio, `Cmd+Shift+T`). 
6. Fare clic su **Salva**. 

```
┌────────────────────────────────────────────────────┐
│ Edit Hotkey Dialog                                 │
├────────────────────────────────────────────────────┤
│ Command:             cm_RunTerm - Run Terminal     │
│ Primary Shortcut:    [ Ctrl+J                    ] │
│ Secondary Shortcut:  [ Cmd+Opt+T                 ] │
│                                                    │
│                           [ Cancel ]    [ Save ]   │
└────────────────────────────────────────────────────┘
```
 

---

### 3.4 Rilevamento automatico delle collisioni e avvisi di conflitto

Se si tenta di assegnare un accordo di tonalità già richiesto da un altro comando nello stesso contesto, il motore di rilevamento delle collisioni di ATBCmder interviene immediatamente. Una finestra di dialogo di avviso visualizza l'assegnazione in conflitto: 

> [!WARNING] 
> **Rilevato conflitto di scorciatoie** 
> La scorciatoia `Ctrl+M` è già assegnata a `cm_MultiRename` nel contesto `FilePanel`. 
> Vuoi sovrascriverlo e riassegnare `Ctrl+M` a `cm_MarkCurrentExtension`? 

- Facendo clic su **Sì** si separa automaticamente `Ctrl+M` dal vecchio comando e lo si applica al comando appena selezionato. 
- Facendo clic su **No** si annulla la modifica, preservando le associazioni esistenti senza modifiche. 

---

### 3.5 Tasto di scelta rapida globale Mostra/Nascondi finestra (`Cmd+Opt+H` / `Ctrl+Alt+H`)

Per gli utenti esperti che preferiscono mantenere ATBCmder in esecuzione discretamente in background: 

1. Apri **Preferenze ➔ Generali**. 
2. Selezionare **Riduci a icona nella barra delle applicazioni**. 
3. Individua **Mostra/Nascondi tasto di scelta rapida finestra** (impostazione predefinita: `Ctrl+Alt+H` / `⌘⌥H`). 
4. Fare clic sulla casella della sequenza per registrare qualsiasi accordo di tasti di scelta rapida globale personalizzato. 
5. Fare clic su **Applica**. 

Ora puoi richiamare immediatamente ATBCmder in primo piano o spostarlo in background da qualsiasi punto di macOS, anche quando lavori all'interno di altre applicazioni a schermo intero. 

---

## 4. Visualizzazioni file, modalità colonna e gestione miniature

La pagina **Visualizzazioni file** (`page_fileview.py`) regola il modo in cui le directory vengono visualizzate, misurate, ordinate e presentate nei doppi pannelli. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              FILE VIEWS CONFIGURATION                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Sorting Rules:                                                                        │
│  [X] Case-sensitive sorting             [X] Natural (numeric) sorting                  │
│  [ ] Special sorting rules                                                             │
│  Folder sort mode:        [ Folders first                                    ▼ ]       │
│  New files position:      [ Sorted                                           ▼ ]       │
│  Updated files position:  [ Top                                              ▼ ]       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Column Widths & Auto-Fit Engine:                                                      │
│  Column auto-fit mode:    [ Average mode                                     ▼ ]       │
│  Average mode padding:    [ 1.20x ]  (Range: 1.00x - 5.00x)                            │
│  Hint: In Fixed mode, drag column dividers to save exact pixel widths per side.        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Date/Time Formatting:                                                                 │
│  Long datetime format:    [ %Y-%m-%d %H:%M:%S                                ]         │
│  Sync dirs format:        [ %Y.%m.%d %H:%M:%S                                ]         │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Motore di adattamento automatico delle colonne: le tre modalità

I file manager a doppio pannello spesso hanno problemi con le diverse lunghezze dei nomi dei file: colonne troppo larghe causano lo scorrimento orizzontale, mentre colonne troppo strette troncano le estensioni di file critiche. ATBCmder risolve questo problema con tre distinti comportamenti di adattamento automatico: 

1. **Modalità fissa (`fixed`)**: 
- Disabilita il ricalcolo automatico. 
- Le larghezze delle colonne rimangono esattamente dove le posizioni. 
- **Trascinamento manuale**: quando trascini il bordo verticale tra le intestazioni delle colonne (ad esempio, tra `Name` e `Ext`), ATBCmder cattura l'esatta larghezza in pixel e la mantiene separatamente per ciascun lato del pannello (`column_widths_left` e `column_widths_right` in `atbcmder.xml`). 
2. **Modalità media (`average` — impostazione predefinita consigliata)**: 
- Valuta la larghezza tipografica media (`QFontMetrics`) di tutti i nomi di file visibili nella directory. 
- Moltiplica la larghezza media per il **Fattore di riempimento** configurato (cursore regolabile da `1.0x` a `5.0x`, predefinito `1.0x`–`1.25x`), aggiungendo 40 pixel per le icone del tipo di file e il respiro visivo. 
- Impedisce che nomi di file estremi (come un singolo nome di file di registro di 120 caratteri) spingano tutte le altre colonne fuori dallo schermo. 
3. **Modalità larghezza massima (`max`)**: 
- Esegue la scansione delle voci della directory ed espande la colonna in modo che corrisponda al nome file singolo più ampio più il riempimento di sicurezza (+50 px). 
- Garantisce che zero nomi di file vengano troncati con i puntini di sospensione (`...`), ideale per archivi multimediali e set di dati scientifici. 

> [!TIP] 
> **Ottimizzazione di directory di grandi dimensioni**: 
> Nelle directory contenenti decine di migliaia di elementi, la misurazione di ogni singola stringa bloccherebbe l'interfaccia. ATBCmder applica automaticamente il campionamento a passi intelligente (`_MAX_SAMPLE = 200`), valutando un sottoinsieme di righe distribuito uniformemente per calcolare le metriche tipografiche in meno di 2 millisecondi ignorando i marcatori della directory principale (`..`). 

---

### 4.2 Opzioni di ordinamento dei file

Perfeziona il modo in cui gli elementi si ordinano all'interno delle visualizzazioni tabella: 

- **Ordinamento naturale (numerico)**: se abilitato, i numeri all'interno delle stringhe vengono confrontati matematicamente: `file1.txt`, `file2.txt`, `file10.txt` (invece di alfabetico `file1.txt`, `file10.txt`, `file2.txt`). 
- **Ordinamento con distinzione tra maiuscole e minuscole**: se selezionato, i caratteri maiuscoli precedono i caratteri minuscoli in base ai valori ordinali ASCII/Unicode (`File.txt` ordina prima di `apple.txt`). Se deselezionato, l'ordinamento non fa distinzione tra maiuscole e minuscole. 
- **Modalità di ordinamento delle cartelle**: 
- `Folders first`: le directory sono raggruppate nella parte superiore del pannello sopra tutti i file. 
- `Files first`: i file vengono elencati per primi, con le directory posizionate in fondo. 
- `Mixed`: file e cartelle vengono ordinati insieme in ordine alfabetico in una sequenza unificata. 
- **Posizione file nuovi e aggiornati**: controlla dove vengono visualizzati i file appena creati o modificati di recente durante gli aggiornamenti live del file system (`Sorted`, `Top` o `Bottom`). 

---

### 4.3 Visualizzazione griglia di miniature e meccanica della cache

Per fotografi, designer ed editor video, ATBCmder fornisce una **visualizzazione griglia di miniature** (`cm_ThumbnailsView`) integrata, che sostituisce le righe tabulari con anteprime visive delle immagini. 

![Thumbnail Grid View](images/thumbnails_grid_view.png) 
*Figura 7.2: Visualizzazione miniature ad alte prestazioni con anteprime delle immagini con spaziatura della griglia personalizzata.*

#### Ridimensionamento e zoom dinamico

- **Dimensione miniatura predefinita**: configurabile da 48 px fino a 512 px (predefinito: 128 px). 
- **Pizzica per zoomare interattiva**: sui trackpad Apple, utilizza i gesti standard per pizzicare con due dita o tieni premuto **`Ctrl`** mentre scorri la rotellina del mouse per ridimensionare dinamicamente le miniature in tempo reale.

#### Architettura di memorizzazione nella cache multilivello

La generazione di miniature per foto RAW ad alta risoluzione da 48 megapixel o SVG vettoriali complessi richiede un utilizzo intensivo della CPU. ATBCmder utilizza una robusta architettura di caching a due livelli: 

1. **Cache LRU in memoria**: conserva 500 oggetti `QPixmap` decompressi nella RAM per uno scorrimento istantaneo e fluido a 60 fps. 
2. **Cache del disco permanente**: archiviato localmente nella directory della cache dell'utente: 
-percorso macOS/Linux: `~/.cache/atbcmder/thumbnails/` 

- Le chiavi della cache vengono generate tramite hash crittografici SHA-256 che combinano il percorso del file, il timestamp di modifica del file (`mtime`), la dimensione in pixel richiesta e la versione dello schema della cache: 
$$\text{Chiave cache} = \text{SHA256}(\text{percorso file} + \text{mtime} + \text{dimensione} + \text{versione})$$ 

- Se un file immagine viene modificato o aggiornato sul disco, il suo timestamp cambia, invalidando immediatamente le voci della cache non aggiornate e attivando il nuovo rendering automatico in background. 
3. **Thread di lavoro in background**: l'elaborazione delle immagini viene scaricata su un pool di lavoro dedicato `QThread` utilizzando Pillow (PIL) o pipeline `QImage` con accelerazione hardware, garantendo che l'interfaccia a doppio pannello non si blocchi mai durante importazioni batch pesanti. 

---

### 4.4 Formattazione personalizzata di data e ora

ATBCmder ti consente di definire stringhe di formattazione timestamp personalizzate utilizzando la sintassi standard Python `strftime`: 

- **Formato data/ora lungo** (predefinito: `%Y-%m-%d %H:%M:%S`): controlla la visualizzazione della data nella vista a colonna intera (`2026-09-06 14:30:00`). 
- **Formato di sincronizzazione delle cartelle** (predefinito: `%Y.%m.%d %H:%M:%S`): controlla la presentazione del timestamp nella finestra di dialogo Directory Synchronizer. 

| Gettone | Descrizione | Esempio di output | 
| :--- | :--- | :--- | 
| `%Y` | Anno a 4 cifre | `2026` | 
| `%m` | Mese a 2 cifre (`01`–`12`) | `09` | 
| `%d` | Giorno del mese a 2 cifre (`01`–`31`) | `06` | 
| `%H` | Ora a 2 cifre nel formato 24 ore (`00`–`23`) | `14` | 
| `%I` | Ora a 2 cifre nel formato 12 ore (`01`–`12`) | `02` | 
| `%p` | Designazione AM/PM | `PM` | 
| `%M` | Minuti a 2 cifre (`00`–`59`) | `30` | 
| `%S` | Secondo a 2 cifre (`00`–`59`) | `15` | 

---

## 5. Aggiornamento automatico del file system e sensibilità del monitoraggio

Quando si collabora su codebase condivise, si scaricano risorse del browser o si eseguono attività di compilazione in background, i contenuti della directory cambiano costantemente. La pagina **Aggiornamento automatico** (`page_auto_refresh.py`) bilancia la precisione dell'interfaccia utente in tempo reale con il consumo di CPU e batteria. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              AUTO-REFRESH CONFIGURATION                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [X] Refresh file list:                                                                │
│      [X] When files are created, deleted or renamed                                    │
│      [X] When size, date or attributes change                                          │
│      Polling interval (seconds): [ 5 ]                                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Disable auto-refresh:                                                                 │
│      [X] When application is in the background                                         │
│      [X] For the following paths and their subdirectories:                             │
│          ┌──────────────────────────────────────────────────────────────────────────┐  │
│          │ /Volumes/NetworkShare/LargeMediaArchive                                  │  │
│          │ /Users/username/Developer/linux-kernel/                                  │  │
│          │ /Users/username/work/heavy_project/node_modules/                         │  │
│          └──────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Trigger di eventi e fallback del polling

ATBCmder combina il monitoraggio degli eventi nativi del sistema operativo con un fallback di polling intelligente: 

- **Monitoraggio eventi (`watch_file_name_change`)**: sfrutta le notifiche del kernel del sistema operativo nativo (macOS `FSEvents` / `kqueue`) per rilevare creazioni, eliminazioni e ridenominazioni di file con zero sovraccarico della CPU. 
- **Monitoraggio attributi (`watch_attributes_change`)**: tiene traccia delle espansioni delle dimensioni dei file, degli aggiornamenti del timestamp e delle modifiche alla modalità di autorizzazione. 
- **Intervallo di fallback polling (`attr_poll_interval`)**: configurabile da 1 a 60 secondi (impostazione predefinita: 5 secondi). 
*Perché è necessario il polling?* I montaggi di archiviazione di rete remota (SMB, CIFS, NFS, SFTP VFS) spesso non riescono a emettere eventi del file system del sistema operativo nativo quando i client remoti apportano modifiche. Il timer di polling in background garantisce che gli elenchi dei pannelli remoti non diventino mai obsoleti. 

---

### 5.2 Conservazione della batteria e della CPU: disabilita quando in background

Sui laptop macOS alimentati a batteria, gli osservatori attivi del filesystem possono consumare energia non necessaria. 

- Selezionando **Quando l'applicazione è in background** (`watch_only_foreground`) si sospendono automaticamente tutti i timer di polling attivi e gli osservatori di eventi nel momento in cui ATBCmder perde il focus della finestra. 
- Quando torni ad ATBCmder, i pannelli eseguono immediatamente un unico aggiornamento coordinato, aggiornando istantaneamente tutti gli elenchi delle directory. 

---

### 5.3 Filtri di esclusione del percorso

Le directory ad alto tasso di abbandono, come `node_modules`, repository di metadati Git (`.git`), cache degli artefatti di compilazione (`target/`, `build/`) e file di database locali, generano migliaia di eventi del disco al minuto. 

1. Selezionare **Per i seguenti percorsi e le relative sottodirectory** (`watch_exclude_dirs`). 
2. Immettere un percorso di directory assoluto per riga nell'area di testo di esclusione: 
   ```text
   /Users/username/Developer/project/node_modules
   /Users/username/Developer/linux/.git
   /Volumes/ProductionNAS/RenderingQueue
   ```
 

3. Fare clic su **Applica**. ATBCmder ignora gli eventi del file system che si verificano all'interno di questi alberi di percorsi, eliminando aggiornamenti indesiderati dell'interfaccia utente e picchi di CPU. 

---

## 6. Associazioni di file personalizzate e integrazione di strumenti esterni

Facendo doppio clic su un file o premendo **`Enter`** normalmente lo si apre utilizzando l'applicazione di sistema predefinita. Il **Sistema di associazioni file** di ATBCmder (`cm_FileAssoc` / `file_associations.py`) consente di definire azioni personalizzate per modelli di file specifici, mappandoli su comandi interni o applicazioni terminali/GUI esterne.

### 6.1 Architettura e specificità del modello

Le associazioni di file vengono valutate in ordine di specificità del modello: il modello glob più lungo e specifico viene abbinato per primo: 

$$\text{Ordine di specificità: } \texttt{*.min.js} \longrightarrow \texttt{*.js} \longrightarrow \texttt{text/*} \longrightarrow \texttt{*}$$ 

Ogni associazione può contenere più azioni (ad esempio, "Apri in VS Code", "Visualizza esadecimale", "Esegui in Python"), di cui una designata come azione predefinita principale attivata su `Enter`. 

---

### 6.2 Sostituzioni macro token per comandi esterni

Quando si avviano strumenti esterni o script da riga di comando, ATBCmder sostituisce automaticamente le macro token con i metadati del file attivo: 

| Gettone macro | Significato | Esempio Valore | 
| :--- | :--- | :--- | 
| **`%f`** | Percorso assoluto completo del file selezionato | `/Users/username/Documents/report.pdf` | 
| **`%d`** | Percorso della directory contenente il file | `/Users/username/Documents` | 
| **`%n`** | Nome file di base senza estensione | `report` | 
| **`%e`** | Estensione del file senza punto iniziale | `pdf` | 

---

### 6.3 Ricette pratiche di associazione

#### Soluzione 1: aprire gli script Python in Visual Studio Code

- **Modello**: `*.py` 
- **Etichetta**: `Edit in VS Code` 
- **Comando**: `code %f` 
- **Tipo di azione**: comando shell esterno

#### Ricetta 2: esegui lo script Python nel terminale

- **Modello**: `*.py` 
- **Etichetta**: `Execute Script` 
- **Comando**: `python3 %f` 
- **Tipo di azione**: comando shell esterno

#### Soluzione 3: visualizza Markdown nel visualizzatore di anteprima dedicato

- **Modello**: `*.md` 
- **Etichetta**: `Preview in Typora` 
- **Comando**: `open -a Typora %f` 
- **Tipo di azione**: comando shell esterno

#### Soluzione 4: confronta il file con il pannello opposto in Beyond Compare

- **Modello**: `*` 
- **Etichetta**: `Compare with Target` 
- **Comando**: `bcomp %f %d` 
- **Tipo di azione**: comando shell esterno 

---

## 7. Personalizzazione della barra degli strumenti e della barra degli strumenti centrale

ATBCmder fornisce due barre degli strumenti personalizzabili: la **Barra degli strumenti principale** situata sotto la barra dei menu e la **Barra degli strumenti centrale** incorporata verticalmente nello splitter che separa i due pannelli dei file. 

![Middle Toolbar](images/middle_toolbar.png) 
*Figura 7.3: La pagina delle opzioni della barra degli strumenti centrale che configura i pulsanti di divisione e i trigger di azione rapida.*

### 7.1 Personalizzazione dell'aspetto della barra degli strumenti

Apri **Preferenze ➔ Barra degli strumenti** o **Preferenze ➔ Barra degli strumenti centrale**: 

- **Cursore dimensione barra**: regola l'altezza/larghezza della barra degli strumenti da 16 px a 64 px. 
- **Cursore dimensione icona**: ridimensiona le icone dei pulsanti da 16 px a 64 px (impostazione predefinita: 24 px). 
- **Pulsanti piatti**: alterna i moderni pulsanti piatti senza bordi con i classici pulsanti in rilievo. 
- **Mostra didascalie**: visualizza le etichette di testo sotto o accanto alle icone della barra degli strumenti. 

---

### 7.2 Aggiunta di elementi e selettore di icone integrato

Gli elementi della barra degli strumenti sono organizzati in un albero gerarchico che supporta tre tipi di elementi: 

1. **Separatore**: inserisce una linea di divisione visiva o uno spaziatore tra i gruppi di pulsanti. 
2. **Comando interno**: seleziona uno qualsiasi degli oltre 230 comandi `cm_*` di ATBCmder utilizzando il campo del comando di completamento automatico. 
3. **Comando esterno**: specificare un comando shell esterno, una directory di lavoro e token di parametro (`%f`, `%d`).

#### Il selettore di icone integrato (`IconPickerDialog`)

Quando configuri i pulsanti personalizzati, fai clic sul pulsante di anteprima dell'icona per aprire il **Selettore icone** integrato: 

- Dispone di un filtro di ricerca istantaneo tra centinaia di icone SVG e PNG in bundle. 
- Visualizza le icone in una griglia uniforme con anteprima ad alta risoluzione e nomi delle risorse. 

```
┌────────────────────────────────────────────────────────────────────────┐
│ Icon Picker Dialog                                                     │
├────────────────────────────────────────────────────────────────────────┤
│ Search: [ terminal                                                   ] │
├──────────────────────────────────────────────────────┬─────────────────┤
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐ │ PREVIEW:        │
│  │ 💻 │   │ 🖥️ │   │ ⌨️ │   │ ⚙️ │   │ 📁 │   │ 🔍 │ │                  │
│  └────┘   └────┘   └────┘   └────┘   └────┘   └────┘ │      💻         │
│  cm_RunTerm  console  terminal  bash   sh      zsh   │                 │
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐ │ Name: cm_RunTerm│
│  │ 📄 │   │ ✏️ │   │ ✂️ │   │ 📋 │   │ 🗑️ │   │ 🔒 │ │ Size: 48x48     │
│  └────┘   └────┘   └────┘   └────┘   └────┘   └────┘ │ Format: SVG/PNG │
├──────────────────────────────────────────────────────┴─────────────────┤
│                                                [ Cancel ]  [ Select ]  │
└────────────────────────────────────────────────────────────────────────┘
```
 

---

### 7.3 Personalizzazione della hotlist delle directory e delle schede preferite

- **Hotlist directory (`page_hotlist.py`)**: gestisci i tuoi segnalibri `Ctrl+D`. Aggiungi percorsi correnti, riordina i segnalibri utilizzando il trascinamento della selezione, configura la sincronizzazione del pannello di destinazione e assegna chiavi di accesso. 
- **Schede preferite (`page_favorite_tabs.py`)**: salva i layout completi dell'area di lavoro multischeda a doppio pannello. Ripristina i tuoi esatti set di directory di sviluppo o di fotoritocco con un clic. 

![Directory Hotlist](images/quick_access_paths.png) 
*Figura 7.4: Gestione dei segnalibri e dei percorsi delle hotlist delle directory.* 

---

## 8. Portabilità della configurazione e modalità di test isolata

Che si tratti di eseguire la migrazione a un nuovo Mac, di fornire una flotta di macchine di sviluppo o di condividere combinazioni di tasti personalizzate con i colleghi, ATBCmder semplifica il backup e l'implementazione della configurazione.

### 8.1 Configurazione dell'architettura di archiviazione

ATBCmder memorizza tutte le impostazioni dell'utente in file XML strutturati in modo chiaro e leggibili dall'uomo situati nella directory di configurazione standard del sistema operativo: 

- **Percorso standard macOS**: 
`~/Library/Preferenze/atbcmder/` 

- **Percorso sandbox dell'app macOS**: 
`~/Library/Containers/com.aitobox.atbcmder/Data/Library/Preferenze/atbcmder/` 

- **Percorso Linux/UNIX**: 
`~/.config/atbcmder/` 

- **Comando di accesso diretto**: 
Esegui **`cm_OpenConfigDirectory`** (o scegli **Configurazione ➔ Apri directory di configurazione** dal menu) per navigare immediatamente nel pannello attivo direttamente in questa cartella. 

```
~/Library/Preferences/atbcmder/
├── atbcmder.xml          # Core application configuration, geometry, themes, view rules
├── atbcmder_hotkeys.xml  # User keyboard shortcut overrides and custom bindings
├── favtabs.xml           # Saved favorite folder tab layouts and paths
├── hotlist.xml           # Directory Hotlist (Ctrl+D) bookmarks hierarchy
└── history.xml           # Recent directory jumps, command line history, search history
```
 

---

### 8.2 Esportazione dei pacchetti di configurazione (`cm_ExportConfiguration`)

Per creare un backup portatile all-in-one del tuo ambiente ATBCmder: 

1. Scegli **Configurazione ➔ Esporta configurazione...** dalla barra dei menu (o esegui `cm_ExportConfiguration`). 
2. Seleziona la directory di destinazione e scegli un nome file (predefinito: `atbcmder-config.zip`). 
3. Fare clic su **Salva**. 

ATBCmder scarica tutte le modifiche di memoria in sospeso sul disco, raccoglie tutti i file XML di configurazione (`atbcmder.xml`, `atbcmder_hotkeys.xml`, `favtabs.xml`, `hotlist.xml`) e li inserisce in un archivio ZIP atomico e compresso. 

---

### 8.3 Importazione dei bundle di configurazione (`cm_ImportConfiguration`)

Per ripristinare un backup della configurazione su una nuova macchina o ripristinare uno stato valido noto: 

1. Scegli **Configurazione ➔ Importa configurazione...** dalla barra dei menu (o esegui `cm_ImportConfiguration`). 
2. Seleziona l'archivio `atbcmder-config.zip` precedentemente esportato. 
3. Confermare la richiesta di avviso: 
> L'importazione sostituirà tutte le impostazioni correnti con il contenuto del file selezionato. Continuare? 
4. Fare clic su **Sì**. 

ATBCmder decomprime in modo sicuro l'archivio, verifica che tutti i file estratti siano configurazioni XML valide, sostituisce i file del disco attivi, ricarica il singleton interno `Config()` e aggiorna immediatamente sia i pannelli dei file che i layout delle colonne, il tutto senza richiedere il riavvio dell'applicazione. 

> [!IMPORTANT] 
> **Sicurezza aziendale: protezione anti-trasversale** 
> ATBCmder applica una rigorosa convalida del percorso trasversale durante l'importazione della configurazione (`zipfile` sanitizzazione). Qualsiasi membro dell'archivio contenente separatori di percorso (`/`, `\`), attraversamenti di directory (`..`) o estensioni di file non XML viene rifiutato immediatamente, proteggendo il sistema operativo da manomissioni dannose dell'archivio. 

---

### 8.4 Modalità test isolata (`ATBCmder_test.sh`)

Quando sviluppi plug-in personalizzati, sperimenti riassociazioni aggressive di tasti di scelta rapida o test configurazioni beta, dovresti evitare di modificare la configurazione quotidiana dei driver. 

ATBCmder supporta il reindirizzamento completo della configurazione tramite la variabile di ambiente `ATBCMDER_CONFIG_PATH`. Uno script di test dedicato è incluso nel repository del progetto: 

```bash
# Launch ATBCmder in completely isolated test mode:
./scripts/ATBCmder_test.sh
```

#### Come funziona la modalità test isolata:

1. Fornisce una directory di test pulita e temporanea in `tests/.test_config/`. 
2. Copia le impostazioni di base di fabbrica da `src/atbcmder/resources/test_config.xml` a `tests/.test_config/atbcmder.xml`. 
3. Imposta `export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"`. 
4. Genera ATBCmder in Python. Qualsiasi impostazione modificata o eliminata durante la sessione influisce solo sulla directory temporanea del test, lasciando intatti al 100% i tuoi file personali `~/Library/Preferenze/atbcmder/`. 

---

## 9. ⚡ Suggerimenti degli esperti e approfondimento: personalizzazione avanzata

### Suggerimento professionale 1: provisioning automatizzato di Dotfile tramite Chezmoi/Ansible

Poiché ATBCmder serializza tutto lo stato in file XML UTF-8 standard, puoi controllare la tua configurazione in un repository Git dotfiles e gestirla tramite strumenti come Chezmoi, GNU Stow o Ansible: 

```bash
# Example: Adding ATBCmder configuration to Chezmoi dotfiles manager
chezmoi add ~/Library/Preferences/atbcmder/atbcmder.xml
chezmoi add ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml
```

### Suggerimento 2 degli esperti: ottimizzazione del Network Watcher ad alte prestazioni

Quando si lavora su file server SMB/NFS aziendali contenenti milioni di file, il monitoraggio attivo degli eventi ricorsivi può causare congestione della rete. 

1. Apri **Preferenze ➔ Aggiornamento automatico**. 
2. Deseleziona **Quando cambiano dimensioni, data o attributi**. 
3. Impostare **Intervallo di polling** su `15` o `30` secondi. 
4. Aggiungere la root di montaggio di rete (`/Volumes/EnterpriseShare`) all'**Elenco di esclusione percorsi**. 
5. Utilizzare l'aggiornamento manuale del pannello (**`Ctrl+R`** / `⌘R`) quando è richiesta la sincronizzazione immediata.

### Suggerimento 3: variabili di ambiente dei comandi esterni

Quando si configurano i pulsanti personalizzati della barra degli strumenti esterna o le associazioni di file, ATBCmder eredita automaticamente l'ambiente della shell utente (`PATH`, `HOME`, `USER`). È possibile richiamare direttamente le utilità della riga di comando installate tramite Homebrew (`/opt/homebrew/bin/`) senza fornire percorsi eseguibili assoluti completi.

### Suggerimento professionale 4: configurazione delle descrizioni comandi dei file mobili

ATBCmder include descrizioni comandi di metadati mobili che mostrano le dimensioni del file, i dati EXIF, il bitrate audio e il conteggio dei membri dell'archivio quando si passa con il mouse sugli elementi. Puoi attivare o disattivare le descrizioni comandi in **Preferenze ➔ Visualizzazioni file**. 

![Helpful Tooltips](images/helpful_tooltips.png) 
*Figura 7.5: descrizioni comandi ricche di metadati che mostrano le proprietà dettagliate del file al passaggio del mouse.* 

---

## 10. Avvisi di sicurezza e di sistema

> [!WARNING] 
> **Verifica sovrascrittura scorciatoia** 
> La sovrascrittura di una scorciatoia primaria nel contesto `Main` o `FilePanel` la separa immediatamente dal comando originale. Se svincoli accidentalmente comandi essenziali come `F5` (Copia) o `Enter` (Apri), utilizza il pulsante **Ripristina impostazioni predefinite** nell'editor dei tasti di scelta rapida per ripristinare le associazioni di tasti di fabbrica. 

> [!WARNING] 
> **L'importazione della configurazione sostituisce tutte le impostazioni** 
> Il ripristino di un pacchetto di configurazione tramite `cm_ImportConfiguration` sovrascrive completamente i file `atbcmder.xml`, `favtabs.xml` e `hotlist.xml` correnti. Esporta sempre un backup della configurazione esistente prima di importare un archivio esterno. 

> [!IMPORTANT] 
> **Sandbox dell'app macOS e accesso completo al disco** 
> Se ATBCmder è in esecuzione nella sandbox dell'app macOS, non può leggere file di configurazione o directory all'esterno del suo contenitore senza l'autorizzazione esplicita dell'utente. Se riscontri errori di autorizzazione durante l'accesso alle unità esterne, esegui **`cm_GrantFilesystemAccess`** per completare il flusso di onboarding Accesso completo al disco macOS. 

---

## 11. Riferimento ai comandi Master per la personalizzazione e le preferenze della matrice doppia

| Categoria | Azione Descrizione | Scorciatoia macOS | Chiave del comandante classico | ID comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Preferenze** | Apri la finestra di dialogo Preferenze principali | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | 
| **Preferenze** | Salva le impostazioni in XML adesso | Menù: Configurazione | — | `cm_ConfigSaveSettings` | 
| **Preferenze** | Salva posizione e dimensione della finestra | Menù: Configurazione | — | `cm_ConfigSavePos` | 
| **Preferenze** | Attiva/disattiva le descrizioni comandi dei file | Preferenze ➔ Visualizzazioni file | — | *(Preferenze)* | 
| **Preferenze** | Concedere autorizzazioni per disco completo | Menù: Configurazione | — | `cm_GrantFilesystemAccess` | 
| **Tasti di scelta rapida** | Apri la pagina dell'editor dei tasti di scelta rapida | `Cmd+,` ➔ Tasti di scelta rapida | — | `cm_Options` | 
| **Tasti di scelta rapida** | Tasto di scelta rapida globale Mostra/Nascondi finestra | `Ctrl+Alt+H` / `⌘⌥H` | `Ctrl+Alt+H` | *(Tasto di scelta rapida del sistema globale)* | 
| **Associazioni** | Apri Gestione associazioni file | Menù: Configurazione | — | `cm_FileAssoc` | 
| **Segnalibri** | Gestore della lista calda della directory | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| **Segnalibri** | Aggiungi la directory corrente alla hotlist | Menu: Segnalibri | — | `cm_AddDirToHotlist` | 
| **Schede cartella** | Gestore schede cartelle preferite | Menù: Configurazione | — | `cm_ConfigFavoriteTabs` | 
| **Schede cartella** | Salva le schede correnti come set preferito| Menù: Schede | — | `cm_SaveFavoriteTabs` | 
| **Archiviatori** | Configurare i file binari dell'archiver | Menù: Configurazione | — | `cm_ConfigArchivers` | 
| **Portabilità** | Esporta configurazione in ZIP | Menù: Configurazione | — | `cm_ExportConfiguration` | 
| **Portabilità** | Importa configurazione da ZIP | Menù: Configurazione | — | `cm_ImportConfiguration` | 
| **Portabilità** | Apri la cartella di configurazione | Menù: Configurazione | — | `cm_OpenConfigDirectory` | 
| **Modalità di visualizzazione** | Attiva/disattiva la visualizzazione griglia delle miniature | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| **Modalità di visualizzazione** | Aggiorna elenco pannelli attivi | `Ctrl+R` / `⌃R` | `Ctrl+R` | `cm_Refresh` |

--- 

<div align="center"> 
<p>Pronto a padroneggiare tutte le scorciatoie da tastiera e le matrici di comandi nell'intera applicazione?</p> 
<p><strong><a href="keyboard_shortcuts.md">Procedi al capitolo 8: Scorciatoie da tastiera principali &rarr;</a></strong></p> 
</div>