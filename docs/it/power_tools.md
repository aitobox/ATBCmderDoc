# Capitolo 5: Strumenti avanzati e automazione

Nella gestione di file di grandi volumi, la manipolazione di base dei file (copia, spostamento ed eliminazione di singoli elementi) è solo l'inizio. Ingegneri professionisti, amministratori di sistema, creatori di contenuti e analisti di dati incontrano spesso sfide operative complesse: ristrutturare migliaia di risorse digitali con nomi incoerenti, isolare sottili regressioni del codice tra rami di rilascio paralleli, mantenere mirror sincronizzati su array di archiviazione di rete, individuare file di configurazione profondamente sepolti e verificare crittograficamente l'integrità dei file. 

ATBCmder trasforma questi compiti ad alta intensità di manodopera in operazioni rapide e deterministiche. Invece di richiedere script da riga di comando esterni, utilità batch di terze parti o goffe applicazioni diff autonome, ATBCmder integra una suite di automazione completa direttamente nel suo core ortodosso a doppio pannello. Che tu abbia bisogno di eseguire sostituzioni di espressioni regolari in un intero archivio fotografico, eseguire una sincronizzazione di directory bidirezionale con hashing a livello di contenuto o inserire risultati di ricerca multi-filtro in uno spazio di lavoro virtuale, ATBCmder fornisce gli strumenti di cui hai bisogno con la completa efficienza della tastiera. 

---

## 1. Avvio rapido visivo: Automation Engine e Command Matrix

ATBCmder divide gli utensili elettrici e l'automazione in sei domini funzionali specializzati che interagiscono perfettamente con l'interfaccia a doppio pannello: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                DUAL FILE PANELS                                        │
│     Left Panel (Source / Directory A)        Right Panel (Target / Directory B)        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Batch Multi-Rename (Ctrl+M)         │  [2] Side-by-Side File Diff (Meta+Shift+F12)│
│      Tokens, RegEx, Counters, Preview    │      Line highlights, Hunk sync, In-place   │
│                                          │                                             │
│  [3] Directory Sync (Shift+F12)          │  [4] Advanced Search (Alt+F7)               │
│      Content/Date compare, Asym mirror   │      Spotlight / Deep scan ➔ Feed to Listbox│
│                                          │                                             │
│  [5] Semantic Command Bar (/)            │  [6] File Utilities & Security              │
│      Spotlight queries, AI intent, NLP   │      Split/Link, Checksum, Wipe (Alt+Del)   │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Feed to Listbox] ➔ Populates virtual panel tab for bulk operations across directories│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Foglio informativo sull'automazione a doppia matrice

| Azione | Scorciatoia macOS | Chiave del comandante classico | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Rinominazione multipla batch** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Apre la finestra di dialogo dello strumento Rinomina multipla batch. | 
| **Differenze file affiancati** | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | Confronta due file selezionati affiancati (`Shift+F3` per `cm_CompareContents`). | 
| **Sincronizzazione directory** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Confronta e sincronizza le directory a doppio pannello. | 
| **Ricerca avanzata dei file** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | Apre la finestra di dialogo di ricerca multi-filtro. | 
| **Ricerca rapida Spotlight** | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menu Comandi)* | Avvia la ricerca istantanea dei metadati Spotlight. | 
| **Inserimento di comandi semantici**| `/` | `/` | `cm_VisSemanticCommand` | Attiva la barra dei comandi incorporata in linguaggio naturale. | 
| **Dividi file di grandi dimensioni** | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | Divide file di grandi dimensioni in blocchi numerati. | 
| **Combina file divisi** | Menu: File ➔ Combina file | — | `cm_FileLinker` / `cm_Combine` | Riassembla i blocchi `.001`, `.002` in un singolo file. | 
| **Calcola il checksum** | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | Calcola gli hash MD5, SHA-1, SHA-256 o SHA-512. | 
| **Verifica file checksum** | Menu Strumenti | — | `cm_CheckSumVerify` / `cm_VerifyChecksum` | Verifica i file rispetto a `.md5`, `.sha256` o `.sfv`. | 
| **Cancellazione sicura (distruggi)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Sovrascrive ed elimina i file in modo sicuro. | 
| **Esegui terminale di sistema** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Genera macOS Terminale nel percorso corrente del pannello. | 

---

## 2. Strumento di ridenominazione multipla batch (`Ctrl+M` / `⌃M` / `cm_MultiRename`)

Rinominare manualmente decine o centinaia di file è noioso e soggetto a errori. Lo **Strumento di ridenominazione multipla batch** (`cm_MultiRename`, mappato su `fmultirename.pas` nell'architettura classica) consente di definire modelli di denominazione flessibili, applicare contatori di sequenze dinamiche, eseguire conversioni di maiuscole e minuscole ed eseguire potenti regole di ricerca e sostituzione di espressioni regolari (RegEx) con garanzie di sicurezza visiva in tempo reale. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figura 5.1: Lo strumento di ridenominazione multipla batch con righe di anteprima in tempo reale, maschere di token, parametri del contatore numerico e rilevamento di duplicati.*

### 2.1 Il flusso di lavoro di ridenominazione multipla

1. **Seleziona file**: nel pannello dei file attivi, seleziona i file o le directory che desideri rinominare utilizzando `Space`, `Insert` o la selezione con caratteri jolly (`+`). Se non è selezionato nulla, viene utilizzato l'elemento sotto il cursore. 
2. **Strumento di avvio**: premi **`Ctrl+M`** (`⌃M`) o scegli **File ➔ Strumento di ridenominazione multipla...** dalla barra dei menu. 
3. **Configura modelli e regole**: inserisci le maschere del nome file/estensione, imposta le opzioni del contatore o definisci le stringhe di ricerca e sostituzione. 
4. **Ispeziona l'anteprima dal vivo**: la tabella a 3 colonne (`Old Name`, `New Name`, `Directory`) si aggiorna istantaneamente a ogni pressione di un tasto. 
5. **Esegui**: fare clic su **Avvia Rinomina** (o premere `Enter`). ATBCmder esegue le rinominazioni in modo atomico e aggiorna i pannelli dei file. 

---

### 2.2 Token modello e suddivisione dell'intervallo

ATBCmder utilizza token intuitivi tra parentesi per fare riferimento a parti dei metadati del file originale: 

| Gettone | Descrizione | Esempio di input | Valore risultante | 
| :--- | :--- | :--- | :--- | 
| **`[N]`** | Nome file originale senza estensione | `report_2026.pdf` | `report_2026` | 
| **`[E]`** | Estensione del file originale (senza punto) | `archive.tar.gz` | `gz` | 
| **`[C]`** | Contatore numerico sequenziale | *(File 3 nell'elenco)* | `003` (dipende dall'impostazione delle cifre) | 
| **`[Y]`** | Anno di modifica del file a 4 cifre | `2026-09-06` | `2026` | 
| **`[M]`** | Mese di modifica del file a 2 cifre | `September` | `09` | 
| **`[D]`** | 2 cifre Giorno di modifica del file | `6th` | `06` | 
| **`[h]`** | Ora a 2 cifre (orologio a 24 ore) | `14:30:15` | `14` | 
| **`[m]`** | Minuti a 2 cifre | `14:30:15` | `30` | 
| **`[s]`** | Secondo a 2 cifre | `14:30:15` | `15` |

#### Suddivisione dell'intervallo di caratteri (`[Na-b]` / `[Ea-b]`)

Puoi estrarre intervalli di caratteri specifici dal nome o dall'estensione originale utilizzando la suddivisione dell'indice in base 1: 

- **`[N1-4]`**: Estrae i primi 4 caratteri del nome. Per `Document_Final.txt`, questo restituisce `Docu`. 
- **`[N5-]`**: Estratto dal 5° carattere alla fine del nome. Per `DSC_0982.jpg`, questo restituisce `0982`. 
- **`[N-5]`**: Estrae fino al 5° carattere. 
- **`[E1-2]`**: Estrae i primi 2 caratteri dell'estensione. Per `archive.html`, questo restituisce `ht`. 

---

### 2.3 Controlli del contatore e sequenze numeriche

Il gruppo **Impostazioni contatore** consente il controllo granulare sull'indicizzazione numerica: 

- **Inizia alle**: il numero intero iniziale per la sequenza del contatore (impostazione predefinita: `1`). 
- **Passo**: il valore di incremento aggiunto per ogni file successivo (predefinito: `1`). Impostando Passo su `2` si genera `1, 3, 5, 7...`. 
- **Cifre**: la larghezza di riempimento zero (intervallo: da `1` a `10`). Impostando le cifre su `3` i numeri vengono formattati come `001`, `002`, `003`. L'impostazione delle cifre su `1` disabilita gli zeri iniziali (`1`, `2`, `3`). 

---

### 2.4 Trova e sostituisci ed espressioni regolari

Il gruppo **Trova e sostituisci** consente la sostituzione del testo in tutti gli elementi selezionati: 

- **Trova**: sottostringa di destinazione o modello di espressione regolare. 
- **Sostituisci con**: stringa sostitutiva. Quando RegEx è abilitato, i riferimenti all'indietro (`$1`, `$2` o `\1`, `\2`) si riferiscono ai gruppi di acquisizione. 
- **Utilizza espressioni regolari (Regex)**: attiva/disattiva l'analisi delle espressioni regolari della libreria standard Python. 
- **Case Sensitive**: se deselezionata, la corrispondenza ignora le maiuscole e minuscole (ad esempio, corrisponde sia a `.JPG` che a `.jpg`).

#### Potenti esempi di sostituzione RegEx

```
Example 1: Strip unwanted tracking or release tags from filenames
Input File:      Album_Artist_-_Track_01_[Lossless_24bit_96kHz].flac
Find Pattern:    \s*\[.*?\]
Replace with:    (leave empty)
Output File:     Album_Artist_-_Track_01.flac

Example 2: Reorder dates from YYYY-MM-DD to DD-MM-YYYY
Input File:      Invoice_2026-09-06_Acme.pdf
Find Pattern:    (\d{4})-(\d{2})-(\d{2})
Replace with:    $3-$2-$1
Output File:     Invoice_06-09-2026_Acme.pdf

Example 3: Convert spaces and underscores to standardized hyphens
Input File:      my new blog post_draft.md
Find Pattern:    [ _]+
Replace with:    -
Output File:     my-new-blog-post-draft.md
```
 

---

### 2.5 Modalità di conversione dei casi

ATBCmder fornisce la normalizzazione istantanea dell'involucro senza richiedere modelli complessi: 

- **Nessuna modifica**: preserva le maiuscole originali. 
- **minuscolo**: converte l'intero nome file e l'estensione in minuscolo (`PHOTO_001.JPG` ➔ `photo_001.jpg`). 
- **MAIUSCOLO**: Converte tutti i caratteri in maiuscolo (`readme.txt` ➔ `README.TXT`). 
- **Prima lettera maiuscola**: Rende maiuscolo il carattere iniziale di ogni parola (`war and peace.epub` ➔ `War And Peace.epub`). 

---

### 2.6 Griglia di anteprima in tempo reale e protezione anticollisione

Rinominare centinaia di file senza visualizzarne l'anteprima può comportare disastrose sovrascritture dei dati. ATBCmder implementa un'**Architettura di sicurezza a zero incidenti**: 

1. **Anteprima antirimbalzo istantanea**: mentre digiti gli input del modello o regoli le caselle di selezione, la tabella calcola immediatamente i nomi dei file risultanti. 
2. **Rilevamento target duplicati**: ATBCmder esegue la scansione di tutti i nomi di file di output calcolati all'interno della cartella di destinazione. Se due o più file si risolvono con lo stesso nome o se il nome di un file si risolve in una stringa vuota: 
- Le righe in collisione vengono immediatamente evidenziate in rosso (`#FFEBEB` / `#D70000` in modalità luce, `#4A1515` / `#FF8080` in modalità buio). 
- Il pulsante **Avvia ridenominazione** viene automaticamente **disabilitato**. 
- Un suggerimento avverte: *"Rilevate collisioni di nomi. Risolvi i duplicati prima di rinominare."* 
3. **Autorizzazione collisioni**: una volta modificato il contatore, il modello o l'espressione regolare per rendere univoci tutti i nomi dei file di destinazione, l'avviso viene cancellato e il pulsante **Avvia ridenominazione** si riattiva. 

---

### 2.7 Ricette pratiche passo dopo passo

#### Ricetta A: rinominare le foto delle fotocamere digitali con timestamp

Trasforma i nomi criptici delle telecamere (`IMG_4092.JPG`, `IMG_4093.JPG`) in risorse organizzate cronologicamente: 

1. Selezionare i file di foto e premere **`Ctrl+M`**. 
2. Impostare **Modello nome file** su: `Photo_[Y][M][D]_[C]`. 
3. Imposta **Modello di estensione** su: `[E]`. 
4. Impostare **Cifre** su `3`, **Inizia da** su `1`. 
5. Impostare **Conversione caso** su `lowercase`. 
6. Visualizza l'anteprima del risultato: `photo_20260906_001.jpg`, `photo_20260906_002.jpg`. 
7. Premere `Enter` per applicare.

#### Soluzione B: aggiungere un prefisso preservando nome ed estensione

Anteporre a un batch di documenti un codice di progetto: 

1. Selezionare i documenti e premere **`Ctrl+M`**. 
2. In **Modello nome file**, inserire: `PRJ-ALPHA_[N]`. 
3. Lasciare **Modello di estensione** come `[E]`. 
4. Fare clic su **Avvia ridenominazione**. 

---

## 3. Differenza file visivi affiancati (`Meta+Shift+F12` / `⌘⇧F12` / `cm_FileDiff`)

Rilevare le differenze tra revisioni della configurazione, file di codice sorgente o dump dei dati è un compito quotidiano per gli utenti esperti. ATBCmder include un **Visualizzatore di differenze di file visivi** integrato e affiancato (`DiffViewerDialog`) che elimina la necessità di avviare strumenti esterni pesanti. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Side-by-side Diff: config.py (Left)  vs.  config.py.new (Right)                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [💾 Save Left] [💾 Save Right] | [Copy to Right →] [← Copy to Left] | [Prev] [Next]    │
│ [🔄 Re-compare] | [✔] Ignore whitespace  [ ] Ignore case  [ ] Ignore blank lines       │
├─────────────────────────────────────────────┬──────────────────────────────────────────┤
│ config.py (Left)                            │ config.py.new (Right)                    │
├─────────────────────────────────────────────┼──────────────────────────────────────────┤
│ 12: DEBUG = False                           │ 12: DEBUG = False                        │
│ 13: LOG_LEVEL = "INFO"                      │ 13: LOG_LEVEL = "DEBUG"      [CHANGED]   │
│ 14: PORT = 8080                             │ 14: PORT = 8080                          │
│ 15: # Deprecated database setting           │ 15:                                      │
│ 16: DB_TIMEOUT = 30              [REMOVED]  │ 16: DB_TIMEOUT = 10          [CHANGED]   │
│ 17:                                         │ 17: SSL_ENABLED = True       [ADDED]     │
├─────────────────────────────────────────────┴──────────────────────────────────────────┤
│  Difference 2 of 4  │  Ln 16, Col 1 (Left)  │  Ln 16, Col 1 (Right)                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Avviare File Diff

- **Confronta due file selezionati**: in un unico pannello, seleziona esattamente due file e premi **`Meta+Shift+F12`** (`⌘⇧F12`) o scegli **Comandi ➔ Confronta per contenuto...**. 
- **Confronta file opposti**: evidenzia un file nel pannello di sinistra, evidenzia il file corrispondente nel pannello di destra e attiva `cm_CompareContents`. 
- **Comandi supportati**: `cm_CompareContents`, `cm_FileDiff` e `cm_CompareByContent` vengono tutti indirizzati al motore di confronto affiancato. 

---

### 3.2 Evidenziazione delle differenze visive e codici colore

Il motore delle differenze analizza il testo riga per riga utilizzando un algoritmo LCS Hunt-Szymanski ottimizzato (`TextDiffer`), dividendo le differenze in blocchi codificati a colori: 

| Tipo differenziale | Evidenziazione del tema chiaro | Evidenziazione tema scuro | Descrizione | 
| :--- | :--- | :--- | :--- | 
| **Righe aggiunte** | Smeraldo Tenue (`#e6ffed`) | Verde foresta scuro (`#234b2d`) | Righe presenti solo nel file Right. | 
| **Righe rimosse** | Cremisi Tenue (`#ffeef0`) | Rosso cremisi scuro (`#552328`) | Righe presenti nel file Left ma mancanti in Right. | 
| **Righe modificate** | Ambra morbida (`#fff5b1`) | Oro ambrato scuro (`#50461e`) | Linee modificate tra le versioni sinistra e destra. | 
| **Fusto attivo** | Tonalità a contrasto vivido | Tonalità a contrasto vivido | Il blocco differenza attualmente focalizzato dal cursore. | 

Ogni riquadro presenta un margine sinistro dedicato (`LineNumberArea`) che mostra i numeri di riga in base 1 sincronizzati con le posizioni differenziali. 

---

### 3.3 Scorrimento sincronizzato e sicurezza di rientro

Quando si confrontano file sorgente lunghi contenenti migliaia di righe, la navigazione nel codice richiede un coordinamento graduale: 

- Lo scorrimento della barra di scorrimento verticale o orizzontale di uno degli editor regola istantaneamente l'editor opposto con lo stesso offset di pixel. 
- ATBCmder implementa un **blocco di rientro** interno (`_syncing_vscroll`, `_syncing_hscroll`) che impedisce cicli di feedback degli eventi, balbuzie o deriva del cursore. 

---

### 3.4 Navigazione di blocchi e fusione bidirezionale

Puoi navigare tra le differenze senza usare il mouse: 

- **Differenza successiva**: premi **`Alt+Down`** / `⌥↓` (o `Ctrl+Down`). 
- **Differenza precedente**: Premi **`Alt+Up`** / `⌥↑` (o `Ctrl+Up`). 
- **Vai al blocco**: facendo clic direttamente su qualsiasi riga evidenziata in uno dei riquadri, il blocco viene impostato automaticamente come attivo.

#### Unione bidirezionale (compatibilità Vimdiff `dp` / `do`)

Unisci le differenze tra i file con singole sequenze di tasti: 

- **Copia da sinistra a destra (`→`)**: premi **`Alt+Right`** / `⌥→` (o `Ctrl+Alt+Right` o Vimdiff `dp` tramite **`Alt+P`**). Il pezzo attivo nell'editor di sinistra sostituisce la sezione corrispondente nell'editor di destra. 
- **Copia da destra a sinistra (`←`)**: premi **`Alt+Left`** / `⌥←` (o `Ctrl+Alt+Left` o Vimdiff `do` tramite **`Alt+O`**). Il pezzo attivo nell'editor di destra sostituisce la sezione corrispondente nell'editor di sinistra. 

---

### 3.5 Modifica sul posto e salvataggio atomico

A differenza dei visualizzatori di differenze che trattano il testo come di sola lettura, entrambi i riquadri di ATBCmder sono editor di codice completamente funzionali: 

- Digita, incolla o elimina il testo direttamente all'interno di uno degli editor. 
- Ogni volta che le modifiche manuali alterano le righe, premere **`F5`** (o `Ctrl+R`) per rieseguire il calcolo della differenza sui buffer aggiornati. 
- Salva file a sinistra: fai clic su **💾 Salva a sinistra** (o premi `Cmd+S` / `Ctrl+S` mentre l'editor di sinistra è attivo). 
- Salva file destro: fai clic su **💾 Salva file destro** (o premi `Cmd+S` / `Ctrl+S` mentre l'editor destro è attivo). 

---

### 3.6 Opzioni di filtraggio del confronto

La barra degli strumenti del visualizzatore di differenze ti consente di isolare le modifiche logiche autentiche dal rumore di formattazione: 

- **Ignora gli spazi bianchi (`_cb_ws`)**: ignora le modifiche nelle tabulazioni, negli spazi finali e nel rientro spazi/tabulazioni. 
- **Ignora maiuscole e minuscole (`_cb_case`)**: esegue confronti di caratteri senza distinzione tra maiuscole e minuscole. 
- **Ignora righe vuote (`_cb_blank`)**: comprime le aggiunte e le eliminazioni di righe vuote, concentrandosi esclusivamente sulle modifiche sostanziali del codice. 

---

### 3.7 Rilevamento differenze file binari

Se uno dei file selezionati per il confronto contiene byte null o firme MIME binarie (ad esempio immagini, eseguibili, archivi compilati), ATBCmder richiama automaticamente `BinaryDiffer`: 

- Visualizza le dimensioni dei file e gli hash crittografici SHA-256 fianco a fianco. 
- Indica chiaramente se i file binari sono identici in byte o divergenti. 

---

## 4. Sincronizzazione della directory (`Shift+F12` / `⇧F12` / `cm_SyncDirs`)

Mantenere gli alberi di directory sincronizzati tra dischi locali, unità di backup e storage di rete è la pietra angolare di sistemi affidabili. Il **Sincronizzatore di directory** di ATBCmder (`SyncDirsDialog`, mappato su `fsyncdirsdlg.pas`) confronta intere gerarchie di cartelle, determina le operazioni direzionali esatte e visualizza in anteprima ogni copia ed eliminazione di file prima di toccare lo spazio di archiviazione. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figura 5.2: Finestra di dialogo di sincronizzazione delle directory che mostra lo stato del confronto ricorsivo, le frecce di sincronizzazione direzionali e i controlli dello specchio asimmetrico.*

### 4.1 Avvio della sincronizzazione della directory

1. Aprire la **directory di origine** nel pannello di sinistra e la **directory di destinazione** nel pannello di destra. 
2. Premi **`Shift+F12`** (`⇧F12`) o scegli **Comandi ➔ Sincronizza cartelle...**. 
3. Viene visualizzata la finestra di dialogo Sincronizza directory con entrambi i percorsi precompilati nelle schede di intestazione. 

---

### 4.2 Metodi di confronto e precisione

Prima della sincronizzazione, configura i criteri di confronto nella scheda **Impostazioni di sincronizzazione**: 

| Impostazione | Predefinito | Descrizione | 
| :--- | :--- | :--- | 
| **Confronta sottodirectory** | `Enabled` | Attraversa ricorsivamente tutte le directory nidificate. | 
| **Confronta per contenuto** | `Disabled` | Legge e verifica i byte del file direttamente utilizzando `filecmp.cmp`. Garantisce una precisione del 100% per file con timestamp identici ma dati modificati. | 
| **Ignora data** | `Disabled` | Confronta i file esclusivamente in base alla dimensione in byte, ignorando i timestamp di modifica del filesystem. | 
| **Tolleranza timestamp FAT/SMB** | `2.0 sec` | Tiene conto automaticamente delle risoluzioni del timestamp FAT/FAT32/exFAT di 2 secondi, prevenendo falsi flag di mancata corrispondenza durante la sincronizzazione su macOS e unità esterne. | 

---

### 4.3 Analisi direzionale e indicatori di stato

Fare clic su **Confronta** per avviare un operatore di confronto in background non bloccante (`SyncCompareWorker`). La tabella di confronto viene popolata con righe direzionali codificate a colori: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Relative Path             │ Operation │ Reason            │ Details                    │
├───────────────────────────┼───────────┼───────────────────┼────────────────────────────┤
│ assets/banner.png         │    ->     │ Left is newer     │ 2026-09-06 > 2026-08-15    │
│ docs/manual.pdf           │    ->     │ Right missing     │ File exists only on left   │
│ config/settings.json      │    <-     │ Right is newer    │ 2026-09-06 > 2026-09-01    │
│ vendor/legacy_lib.so      │    <-     │ Left missing      │ File exists only on right  │
│ build/cache.db            │    !=     │ Conflict          │ Timestamp / type mismatch  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

- **`->` (da sinistra a destra)**: il file a sinistra è più recente o esiste solo a sinistra. Azione predefinita: copia a destra. 
- **`<-` (da destra a sinistra)**: il file a destra è più recente o esiste solo a destra. Azione predefinita: copia a sinistra (in modalità bidirezionale). 
- **`=` (Uguale)**: i file corrispondono per dimensioni e timestamp/contenuto. Filtrato dall'elenco di sincronizzazione attiva per risparmiare tempo. 
- **`!=` (Conflitto)**: collisione tra directory e file incompatibile o conflitto di timestamp irrisolvibile. Saltato durante la sincronizzazione collettiva automatizzata per la sicurezza dei dati. 

---

### 4.4 Mirroring asimmetrico e sincronizzazione simmetrica bidirezionale

ATBCmder supporta due filosofie di sincronizzazione fondamentalmente diverse:

#### 1. Sincronizzazione simmetrica bidirezionale (predefinita)

- **Obiettivo**: allineare entrambe le directory in modo che entrambe dispongano delle versioni più recenti di ogni file. 
- **Azione**: i file contrassegnati `->` vengono copiati a sinistra ➔ destra. I file contrassegnati con `<-` vengono copiati a destra ➔ sinistra. 
- **Sicurezza**: nessun file viene eliminato su entrambi i lati.

#### 2. Mirroring asimmetrico (`Asymmetric` casella di controllo abilitata)

- **Obiettivo**: rendere la directory di destra una replica esatta e identica della directory di sinistra. 
- **Azione**: i file contrassegnati `->` vengono copiati a sinistra ➔ destra. I file a destra che *non* esistono a sinistra (`<- Right missing on Left`) vengono **rimossi permanentemente dalla directory destra**. 
- **Caso d'uso**: creazione di mirror di backup incontaminati su dischi di backup esterni o condivisioni NAS. 

---

### 4.5 Sicurezza pre-esecuzione e registrazione di controllo

- **Ispeziona prima della sincronizzazione**: esamina attentamente la tabella popolata. Puoi vedere i percorsi relativi esatti e le ragioni operative di ogni trasferimento. 
- **Interrompi controllo**: se è necessario interrompere un processo di confronto o sincronizzazione di grandi dimensioni, fare clic su **Interrompi**. Il thread in background termina in modo sicuro senza lasciare file parziali danneggiati. 
- **Registro di controllo automatizzato**: ogni copia, sovrascrittura ed eliminazione eseguita durante la sincronizzazione viene registrata nel **Registro delle operazioni** interno di ATBCmder (`LogCategory.COPY_MOVE_LINK`, `LogCategory.DELETE`). 

---

## 5. Ricerca avanzata dei file e inserimento nella casella di riepilogo (`Alt+F7` / `⌥F7` / `cm_Search`)

L'individuazione di file specifici nelle strutture di cartelle nidificate rappresenta un collo di bottiglia amministrativo comune. ATBCmder fornisce una **finestra di dialogo di ricerca avanzata dei file** ad alte prestazioni (`SearchDialog`, mappata su `fFindDlg.pas`), che combina l'indicizzazione nativa di macOS Spotlight con un motore di scansione approfondito del file system e l'indispensabile funzionalità **Feed to Listbox**. 

![Advanced File Search](images/advanced_search_dialog.png) 
*Figura 5.3: Finestra di dialogo Ricerca file avanzata con parametri multi-filtro, controlli di scansione approfondita e pulsante Feed to Listbox.*

### 5.1 Avvio della ricerca

- Premi **`Alt+F7`** (`⌥F7`) in qualsiasi pannello o scegli **Comandi ➔ Cerca file...**. 
- La finestra di dialogo di ricerca si apre con il campo **Cerca nella directory** precompilato con il percorso corrente del pannello attivo. 

---

### 5.2 Doppio backend di ricerca: Spotlight vs. Deep Scan

ATBCmder dispone di due motori di ricerca specializzati: 

```
                  ┌───────────────────────────────────────────────┐
                  │          Search Query Triggered               │
                  └───────────────────────┬───────────────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
    ┌───────────────────────────┐                   ┌───────────────────────────┐
    │  Spotlight Engine         │                   │  Deep Scan Engine         │
    │  (SpotlightSearchWorker)  │                   │  (DeepScanWorker)         │
    ├───────────────────────────┤                   ├───────────────────────────┤
    │ • Uses macOS mdfind       │                   │ • Recursive os.scandir    │
    │ • Millisecond results     │                   │ • Scans unindexed drives  │
    │ • APFS metadata indexed   │                   │ • Network shares (SMB/NFS)│
    │ • Standard local storage  │                   │ • Raw text/regex parsing  │
    └───────────────────────────┘                   └───────────────────────────┘
```
 

1. **Motore di ricerca Spotlight (`SpotlightSearchWorker`)**: su macOS, facendo clic su **Avvia ricerca** (o premendo `Enter`) viene utilizzato l'indice dei metadati Spotlight del sistema (`mdfind`). Recupera migliaia di percorsi corrispondenti su gigabyte di spazio di archiviazione in una frazione di secondo. 
2. **Deep Scan Engine (`DeepScanWorker`)**: facendo clic su **Deep Scan** si ignora l'indicizzazione del sistema ed si esegue un attraversamento diretto e ricorsivo del filesystem. Questo è essenziale durante la ricerca: 
- Unità USB esterne o schede SD con indicizzazione Spotlight disabilitata. 
- Condivisioni di file di rete remota (SMB, SFTP, FTP, WebDAV). 
- Directory di build dello sviluppatore escluse tramite `.metadata_never_index`. 

---

### 5.3 Criteri di ricerca multi-filtro

Perfeziona le query di ricerca utilizzando parametri granulari nei gruppi **Generale** e **Filtri avanzati**: 

- **Schema nomi file**: 
- *Caratteri jolly*: caratteri jolly standard della shell come `*.py`, `invoice_2026_*.pdf` o `test_??.go`. 
- *Sottostringhe*: inserendo `draft` verrà trovato qualsiasi file o cartella contenente "bozza". 
- *Espressioni regolari*: seleziona **Espressione regolare** per abilitare la sintassi regex completa (ad esempio `^v\d+\.\d+\.(json|xml)$`). 
- **Cerca testo (ricerca nel file)**: 
- Cerca il contenuto delle stringhe UTF-8 e ASCII all'interno di testo, codice sorgente e file di documenti. 
- Controlla la **Ricerca di contenuti con distinzione tra maiuscole e minuscole** per le corrispondenze esatte tra maiuscole e minuscole. 
- **Intervallo dimensioni file**: 
- Imposta la **dimensione minima** e la **dimensione massima** in kilobyte (`KB`). L'impostazione della dimensione massima su `0` lascia i limiti superiori illimitati. 
- **Intervallo di date**: 
- Specifica **Modificato negli ultimi N giorni** (ad esempio, `7` giorni per trovare lavoro della settimana scorsa). 

---

### 5.4 Ispezione rapida nei risultati della ricerca

Durante la navigazione dei risultati di ricerca nell'elenco dei risultati: 

- **Visualizza file (`F3`)**: apre istantaneamente il risultato della ricerca evidenziato nel Lister universale. 
- **Modifica file (`F4`)**: apre il file direttamente nell'editor di testo integrato. 
- **Vai al file (`Enter` / `Go to File`)**: chiude la finestra di dialogo di ricerca, naviga nel pannello principale fino alla directory principale del file e posiziona il cursore direttamente sul file. 

---

### 5.5 Il potere del "feed alla casella di riepilogo"

La caratteristica più trasformativa dei file manager ortodossi è **Alimenta alla casella di riepilogo**: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ SEARCH RESULTS (Flat Virtual Panel Tab)             OPPOSING PANEL (Destination)       │
│ [Search: *.log modified < 30 days]                 /Volumes/ArchiveStorage/Logs        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Folder  │   │  Name                        Size   │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ app_server.log            14 MB   /var/log│ C │  ▸ archive_2025             <DIR>   │
│  ✔ auth_audit.log             2 MB   /etc/sec│ O │                                     │
│  ✔ worker_3.log              88 KB   /opt/app│ P │                                     │
│  ● access.log               512 KB   /var/log│ Y │                                     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [3 items selected] ➔ Press F5 to copy all matching files into destination folder!     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

1. Nella finestra di dialogo Cerca, una volta trovati i file corrispondenti, fare clic sul pulsante **Inserisci nella casella di riepilogo**. 
2. ATBCmder chiude la finestra di dialogo e apre una nuova **scheda virtuale dei risultati della ricerca** nel pannello attivo. 
3. Invece di navigare in ciascuna cartella individualmente, tutti i file corrispondenti di diverse profondità di directory vengono visualizzati in un'unica tabella piatta. 
4. **Esegui qualsiasi azione del comandante**: 
- Seleziona tutti gli elementi o elementi specifici (`Space`, `+`, `Cmd+A`). 
- **Copia (`F5`)** o **Sposta (`F6`)** file corrispondenti in diverse cartelle in un'unica cartella di destinazione nel pannello opposto. 
- **Rinomina multipla in batch (`Ctrl+M`)** tutti i risultati di ricerca corrispondenti contemporaneamente. 
- **Elimina in modo sicuro (`F8` o `Alt+Delete`)** file temporanei indesiderati in un'intera gerarchia di progetti in un colpo solo. 

---

## 6. Integrazione Spotlight e sistema di comando semantico (`/` e `Ctrl+Shift+F`)

I flussi di lavoro moderni richiedono query agili che vanno oltre le rigide finestre di dialogo dei filtri. ATBCmder integra l'indicizzazione di macOS Spotlight direttamente con un **Sistema di comandi semantici in linguaggio naturale** accessibile dalla barra dei comandi incorporata nella parte inferiore della finestra principale. 

![Semantic Command Bar](images/semantic_command.png) 
*Figura 5.4: La barra dei comandi semantici che analizza una query in linguaggio naturale con modelli di completamento automatico in tempo reale.* 

![Semantic Search](images/semantic_search_bar.png) 
*Figura 5.5: Risultati della ricerca semantica visualizzati direttamente all'interno del pannello attivo.*

### 6.1 Attivazione dei comandi semantici

- **Premi `/`**: nel pannello dei file attivi, premi semplicemente il tasto barra (`/`). ATBCmder focalizza immediatamente la barra di modifica del comando in basso, precompilandola con `/`. 
- **Scorciatoia per la ricerca Spotlight**: premi **`Ctrl+Shift+F`** (`⌃⇧F`) o `Cmd+Shift+F` per aprire l'interfaccia del filtro semantico. 
- **Ignora**: premi `Escape` per cancellare il filtro e ripristinare l'elenco delle directory standard. 

---

### 6.2 Ambiti: locale (`/`) e globale (`//`)

ATBCmder distingue tra filtraggio a livello di cartella e rilevamento a livello di sistema utilizzando convenzioni di prefisso:

#### 1. Ambito della directory locale (`/<query>`)

Le query che iniziano con una singola barra funzionano esclusivamente sulla directory aperta nel pannello attivo (e sulle sue sottocartelle se sono specificate opzioni ricorsive): 

- `/larger than 10MB`: mostra solo i file più grandi di 10 megabyte nella cartella corrente. 
- `/> 50MB`: abbreviazione numerica per il filtraggio delle dimensioni. 
- `/today modified pdf`: filtri per i documenti PDF modificati nelle ultime 24 ore. 
- `/images`: visualizza solo i formati di immagine raster e vettoriale. 
- `/source code`: mostra Python, C++, Rust, Go, JavaScript e altri file sorgente. 
- `/contains "API_KEY"`: Filtri per file di testo contenenti la stringa "API_KEY". 
- `/hide *.log`: nasconde i file di registro dal display attivo.

#### 2. Ambito del sistema globale (`//<query>`)

Le query che iniziano con una doppia barra interrogano l'intero volume del sistema macOS tramite Spotlight: 

- `//today modified pdf`: trova tutti i documenti PDF modificati oggi sull'intero Mac. 
- `//larger than 1GB dmg`: individua tutti i programmi di installazione di immagini disco superiori a 1 GB. 
- `//code contains "OAuth2Handler"`: trova tutti i file sorgente a livello di sistema contenenti "OAuth2Handler". 

---

### 6.3 Query semantiche assistite da AI (`?` o `/?`)

Se configurato con un provider AI (Google Gemini, OpenAI, Anthropic Claude o Ollama locale) in *Preferenze ➔ Filtro semantico*: 

- Prefissando una query con `?` o `/?` instrada l'istruzione in linguaggio naturale attraverso un parser LLM. 
- Esempio: `/? find all final invoices sent to client Acme last quarter over $5000` 
- L'intelligenza artificiale traduce le complesse frasi umane in precisi attributi dei metadati Spotlight (`kMDItemFSSize`, `kMDItemContentModificationDate`, `kMDItemTextContent`), visualizzando immediatamente i file corrispondenti nel pannello. 

---

### 6.4 Completamento automatico, Catalogo (`/help`) e Cronologia (`/history`)

Mentre digiti nella casella di modifica del comando semantico: 

- **Popup di completamento interattivo**: un menu a discesa (`SemanticCompletionPopup`) mostra suggerimenti di modelli contestuali basati sul catalogo integrato (`semantic-command-templates.xml`). Utilizza le frecce `Down` e `Up` per evidenziare i suggerimenti e premi `Tab` o `Enter` per accettare. 
- **Catalogo della guida (`/help`)**: digitando `/help` si apre la **finestra di dialogo della guida dei comandi semantici**, che elenca dozzine di esempi ricercabili in categorie (dimensioni, data, tipo di file, contenuto, tag). Facendo doppio clic su qualsiasi voce la si inserisce nella riga di comando. 
- **Cronologia comandi (`/history`)**: digitando `/history` viene visualizzato un registro cronologico di tutti i comandi semantici eseguiti in precedenza con timestamp di esecuzione, consentendo il richiamo immediato. 

---

### 6.5 Modificatori delle azioni del pannello istantaneo

La barra dei comandi semantica può anche manipolare le selezioni e l'ordinamento dei pannelli senza toccare il mouse: 

| Comando semantico | Azione eseguita | 
| :--- | :--- | 
| `/select all visible` | Seleziona tutti gli elementi attualmente visualizzati dopo il filtraggio. | 
| `/clear selection` | Deseleziona tutti gli elementi nel pannello. | 
| `/invert selection` | Inverte lo stato corrente di selezione del file. | 
| `/select images` | Aggiunge tutti i file di immagine nel pannello alla selezione corrente. | 
| `/sort by size descending` | Ordina la tabella dei file in base alla dimensione, dal più grande al più piccolo. | 
| `/reset sort` | Ripristina l'ordinamento alfabetico predefinito dei nomi. | 
| `/group by date` | Raggruppa i file in modo dinamico in base alle parentesi della data di modifica. | 
| `/clear filter` | Rimuove tutti i filtri semantici attivi e ripristina l'elenco completo delle directory. | 

---

## 7. Utilità file essenziali e integrità dei dati

Oltre alla ricerca e alla ridenominazione in batch, ATBCmder integra una suite di utilità di sistema essenziali progettate per gestire file di grandi dimensioni, controllare la sicurezza e verificare l'integrità crittografica.

### 7.1 Separatore di file di grandi dimensioni (`cm_FileSpliter` / `cm_Split` / `Alt+F6`)

Quando si trasferiscono immagini di dischi di grandi dimensioni, archivi video o contenitori di macchine virtuali su dispositivi di archiviazione con limiti di dimensioni del file system (come il limite di 4 GB di FAT32) o limiti di allegati e-mail, il **File Splitter** (`SplitWorker`) divide i file in segmenti sequenziali numerati: 

1. Selezionare il file di grandi dimensioni nel pannello attivo. 
2. Scegli **File ➔ Dividi file...** (o attiva `cm_Split`). 
3. Scegliere la directory di destinazione (per impostazione predefinita è il pannello opposto). 
4. Seleziona una dimensione di blocco standard preimpostata o inserisci una dimensione di byte personalizzata: 
- **1,44 MB**: disco floppy legacy da 3,5". 
- **700 MB**: capacità CD-R standard. 
- **4,7 GB**: capacità DVD-R a strato singolo. 
- **100 MB**: blocco di caricamento standard. 
- **Dimensione personalizzata**: soglia in byte, KB, MB o GB definita dall'utente. 
5. Fare clic su **OK**. ATBCmder divide il file sorgente in un thread di lavoro in background, creando file di sequenza `.001`, `.002`, `.003`.... 

---

### 7.2 Collegatore e combinatore di file (`cm_FileLinker` / `cm_Combine` / `Alt+F7`)

Il riassemblaggio di blocchi di file divisi nel file originale intatto è semplice: 

1. Nel pannello dei file, evidenzia la **prima parte divisa** (deve terminare con l'estensione `.001`). 
2. Scegli **File ➔ Combina file...** (o attiva `cm_Combine`). 
3. ATBCmder rileva automaticamente tutte le parti sequenziali (`.001`, `.002`, `.003`... fino a `.999`). 
4. Selezionare il nome del file di output e la directory di destinazione. 
5. Fare clic su **OK**. L'operatore in background (`CombineWorker`) concatena in sequenza le parti in una replica binaria esatta byte per byte. 

---

### 7.3 Checksum crittografici e verifica (`cm_CheckSumCalc`, `cm_CheckSumVerify`)

Verificare che i file scaricati, le immagini disco o i backup di archivio non siano stati danneggiati o manomessi è fondamentale per l'integrità dei dati. ATBCmder include un **Calcolatore e verificatore di checksum** integrato (`ChecksumDialog`). 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Checksum Calculator                                                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Hash Algorithm: [ SHA256           ▾]                                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3a491d90bc1f42013149db82a890471b67823f40d12e8424e6a00a120894fe83  arch_linux.iso       │
│ 8f14e45fceea167a5a36dedd4bea25431846b9a898492efd727402c3ef30b65a  rootfs.tar.gz        │
│ e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  empty_manifest.txt   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Progress: 100%] Hashing completed.                                                   │
│  [Calculate]    [Stop]    [💾 Save to File]                                 [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Calcolo degli hash (`cm_CheckSumCalc` / `Ctrl+X`)

1. Seleziona uno o più file nel pannello. 
2. Scegli **File ➔ Calcola checksum...** (o premi `Ctrl+X`). 
3. Seleziona l'algoritmo desiderato: **MD5**, **SHA1**, **SHA256** o **SHA512**. 
4. Fare clic su **Calcola**. Il lavoratore trasmette i file in blocchi da 64 KB in background senza bloccare l'interfaccia. 
5. Fare clic su **Salva su file** per esportare gli hash in un file manifest standard `.sha256` o `.md5`.

#### Verifica dei manifesti di checksum (`cm_CheckSumVerify`)

1. Scegli **File ➔ Verifica checksum...**. 
2. Selezionare un file di checksum esistente (`.sha256`, `.md5`, `.sha1`, `.sha512` o `.sfv`). 
3. ATBCmder analizza automaticamente il manifest, individua i file corrispondenti nella stessa directory, ricalcola gli hash sul disco e presenta un rapporto sullo stato codificato a colori: 
- **`OK`**: il file corrisponde perfettamente al checksum. 
- **`FAILED`**: rilevata corruzione o modifica dei dati! 
- **`MISSING`**: file di riferimento non trovato nella directory. 

---

### 7.4 Distruzione/cancellazione sicura dei file (`cm_Wipe` / `Alt+Delete` / `⌥⌫`)

L'eliminazione standard dei file scollega semplicemente le voci della directory, lasciando intatti i blocchi di dati grezzi sul disco dove le utilità di ripristino possono estrarli. Quando gestisci chiavi riservate, credenziali o codice sorgente proprietario, utilizza **Eliminazione/cancellazione sicura** (`cm_Wipe`): 

1. Selezionare i file o le directory riservate. 
2. Premere **`Alt+Delete`** (`⌥⌫`) o scegliere **File ➔ Eliminazione sicura (Cancella)...**. 
3. Confermare la richiesta di avviso di sicurezza. 
4. **La sequenza di distruzione crittografica multi-passaggio (`wipe_path`)**: 
- **Passato 1**: sovrascrive l'intera lunghezza in byte del file con byte pseudo-casuali crittograficamente sicuri (`os.urandom`). 
- **Passa 2**: sovrascrive l'intero file con byte nulli (`\x00`). 
- **Passa 3**: sovrascrive con nuovi byte casuali. 
- **Sincronizzazione hardware**: richiama `os.fsync()` sul descrittore di file sottostante per forzare il sistema operativo e la cache del controller di archiviazione a scrivere i dati su un supporto fisico. 
- **Troncamento e scollegamento**: tronca il file a 0 byte prima di chiamare `os.unlink()`. 
- **Scrubbing directory**: cancella ricorsivamente tutti i file contenuti prima di scollegare le directory principali. 

---

### 7.5 Terminalee di sistema integrato (`Ctrl+J` / `⌃J` / `cm_RunTerm`)

Sebbene ATBCmder eccelle nei flussi di lavoro grafici a doppio pannello, l'accesso alla shell è spesso richiesto per la compilazione, i rami git o la gestione del server: 

- Premi **`Ctrl+J`** (`⌃J`) o scegli **Comandi ➔ Esegui terminale**. 
- ATBCmder apre immediatamente macOS **Terminale.app** (o l'emulatore di terminale predefinito configurato) con la sua directory di lavoro inizializzata sul percorso esatto aperto nel pannello attivo. 
- Non è necessario digitare `cd /Users/...` o trascinare le cartelle nelle finestre del terminale. 

---

## 8. ⚡ Suggerimenti degli esperti e flussi di lavoro di automazione approfondita

### 8.1 Procedura: Ricerca ricorsiva ➔ Feed nella casella di riepilogo ➔ Rinomina multipla

**Obiettivo**: eliminare i numeri di versione da centinaia di file di risorse sparsi in 50 sottocartelle nidificate. 

1. Aprire la radice del progetto nel pannello sinistro. 
2. Premere **`Alt+F7`** per aprire Cerca. 
3. In Modello nomi file, immettere: `*_v[0-9]*.png`. 
4. Fare clic su **Avvia ricerca**. Una volta visualizzate le risorse corrispondenti, fai clic su **Inserisci nella casella di riepilogo**. 
5. Nella scheda del pannello virtuale risultante, selezionare tutti i file con **`Cmd+A`**. 
6. Premere **`Ctrl+M`** per avviare lo strumento di ridenominazione multipla. 
7. In **Trova**, inserisci: `_v\d+`. Abilita **Utilizza espressioni regolari (Regex)**. 
8. Lascia vuoto **Sostituisci con**. 
9. Verificare che la tabella di anteprima dal vivo mostri nomi di file puliti senza suffissi di versione. 
10. Fare clic su **Avvia ridenominazione**. ATBCmder rinomina istantaneamente ogni file in tutte le 50 sottocartelle! 

---

### 8.2 Soluzione: mirroring sicuro del backup su cloud e NAS con sincronizzazione asimmetrica

**Obiettivo**: mantenere un mirroring esterno identico dei tuoi documenti su un'unità SSD esterna o NAS per PMI senza l'accumulo di file duplicati. 

1. Apri `~/Documents` locale nel pannello di sinistra. 
2. Apri `/Volumes/BackupSSD/Documents` nel pannello di destra. 
3. Premere **`Shift+F12`** (`cm_SyncDirs`). 
4. In Impostazioni, assicurati che **Confronta sottodirectory** sia selezionato. 
5. Seleziona **Asimmetrico (Elimina destinazione se manca nell'origine)**. 
6. Fare clic su **Confronta**. 
7. Esamina l'elenco: 
- Le frecce blu/verdi (`->`) indicano i file che verranno copiati nel backup. 
- Le eliminazioni rosse (`<-`) indicano file obsoleti sul disco di backup che hai eliminato localmente. 
8. Fare clic su **Sincronizza**. L'unità di backup ora è uno specchio della cartella locale. 

---

### 8.3 Soluzione: manifest di hash forense prima dell'archiviazione a lungo termine

**Obiettivo**: calcolare e archiviare i checksum crittografici per un progetto multi-terabyte prima di spostarlo su Cold Tape o Cloud Glacier Storage. 

1. Passare alla directory contenente i risultati finali del progetto. 
2. Seleziona tutti gli elementi (`Cmd+A`) e premi **`Ctrl+X`** (`cm_CheckSumCalc`). 
3. Imposta l'algoritmo su **SHA256**. 
4. Fare clic su **Calcola**. Lo streaming hashworker elabora i file in background. 
5. Fare clic su **Salva su file** e denominarlo `MANIFEST-SHA256.txt`. 
6. Ogni volta che recuperi i file anni dopo, seleziona semplicemente `MANIFEST-SHA256.txt` ed esegui **Verifica checksum** per garantire zero bit rot o corruzione silenziosa. 

---

### 8.4 Soluzione: combinazione del filtro semantico del linguaggio naturale con la visualizzazione del ramo piatto (`Cmd+B`)

**Obiettivo**: trovare e organizzare tutti i file multimediali in una struttura di directory complessa e profonda senza aprire finestre di dialogo di ricerca. 

1. Evidenzia la cartella del progetto di livello superiore e premi **`Cmd+B`** (`cm_FlatView`) per unire tutti i contenuti della sottocartella in un unico elenco. 
2. Premi **`/`** per attivare la barra dei comandi semantici. 
3. Digitare: `/images larger than 5MB`. 
4. L'elenco appiattito isola istantaneamente le immagini ad alta risoluzione in ogni directory nidificata. 
5. Premi `/select all visible`, quindi premi **`F5`** per copiarli tutti in una directory di destinazione organizzata nel pannello opposto. 
6. Premere nuovamente `Cmd+B` per ripristinare la normale navigazione nell'albero gerarchico. 

---

## 9. Avvisi su sicurezza, prestazioni e sistema

> [!ATTENZIONE] 
> **Irreversibilità della sincronizzazione asimmetrica della directory** 
> L'abilitazione dell'opzione **Asimmetrica** nella sincronizzazione delle directory (`Shift+F12`) fa sì che i file nella directory di destinazione che non esistono nell'origine vengano **eliminati permanentemente**. Esegui sempre un'ispezione visiva della tabella di anteprima del confronto prima di fare clic su **Sincronizza**. 

> [!ATTENZIONE] 
> **Sostituzioni RegEx multi-rinomina** 
> Quando esegui sostituzioni di espressioni regolari con riferimenti all'indietro (`$1`, `$2`), assicurati che i numeri del gruppo di acquisizione corrispondano alle parentesi nel modello. Metti alla prova il tuo pattern rispetto alle righe della tabella di anteprima dal vivo prima di fare clic su **Avvia rinomina**. Se vengono visualizzati nomi duplicati di destinazione, ATBCmder blocca l'esecuzione per proteggerti dalla perdita di dati. 

> [!IMPORTANTE] 
> **Limiti di distruzione delle unità a stato solido (SSD)** 
> L'utilità Secure Wipe (`cm_Wipe` / `Alt+Delete`) sovrascrive i dati del file con più passaggi di byte casuali e zero byte, seguiti da una chiamata `fsync`. Tuttavia, le moderne unità a stato solido (SSD) utilizzano algoritmi di livellamento dell'usura e overprovisioning a livello di controller che possono reindirizzare le scritture su blocchi flash alternativi. Per uno smaltimento SSD ad alta sicurezza, combina la distruzione dei file con la crittografia dell'intero disco di macOS FileVault. 

> [!NOTA] 
> **Disponibilità Spotlight su volumi di rete e FAT** 
> Fast Spotlight Search (`Ctrl+Shift+F`) si basa sugli indici dei metadati di macOS, che sono attivi per impostazione predefinita sulle unità APFS interne. I montaggi di rete remoti (SMB, SFTP) e le unità exFAT esterne potrebbero non essere indicizzati da Spotlight. Se una query Spotlight non restituisce risultati su un'unità esterna, utilizzare **Scansione profonda** (`Alt+F7`) o abilitare la scansione ricorsiva della directory. 

> [!CONSIGLIO] 
> **Compatibilità tasti funzione Apple (`Fn`)** 
> Su Apple Magic Keyboards e MacBook, i tasti funzione (`F1`-`F12`) impostano per impostazione predefinita le azioni hardware (luminosità, volume). Per premere `Shift+F12` o `Alt+F7`, tieni premuto il tasto **`Fn`**: `Fn+Shift+F12`, `Fn+Alt+F7`. In alternativa, abilita **"Utilizza i tasti F1, F2, ecc. come tasti funzione standard"** in macOS *Impostazioni di sistema ➔ Tastiera ➔ Scorciatoie da tastiera ➔ Tasti funzione*. 

---

## 10. Tabella di riferimento della tastiera master a doppia matrice

| Area Funzionale | Azione Descrizione | Scorciatoia macOS | Chiave del comandante classico | ID comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Rinomina multipla** | Avvia lo strumento di ridenominazione multipla batch | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | 
| **Rinomina multipla** | Esegui / Avvia Rinomina | `Enter` / `⏎` | `Enter` | — | 
| **Rinomina multipla** | Strumento Annulla/Chiudi | `Esc` | `Esc` | — | 
| **Differenza file** | Confronta file/riquadri selezionati | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | 
| **Differenza file** | Vai alla differenza successiva | `Alt+Down` / `⌥↓` | `Ctrl+Down` | — | 
| **Differenza file** | Vai alla differenza precedente | `Alt+Up` / `⌥↑` | `Ctrl+Up` | — | 
| **Differenza file** | Copia pezzo da sinistra a destra | `Alt+Right` / `⌥→` / `Alt+P` | `Ctrl+Alt+Right` | — | 
| **Differenza file** | Copia pezzo da destra a sinistra | `Alt+Left` / `⌥←` / `Alt+O` | `Ctrl+Alt+Left` | — | 
| **Differenza file** | Salva modifiche nell'editor selezionato | `Cmd+S` / `⌘S` | `Ctrl+S` | — | 
| **Differenza file** | Ricalcola le differenze | `F5` / `Fn+F5` | `Ctrl+R` | — | 
| **Sincronizzazione directory**| Apri Sincronizza directory | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | 
| **Sincronizzazione directory**| Avvia confronto directory | `Alt+C` / `⌥C` | `Enter` | — | 
| **Sincronizzazione directory**| Annulla confronto/sincronizzazione | Fare clic su `Stop` | `Esc` | — | 
| **Ricerca file** | Apri la finestra di dialogo Ricerca avanzata | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | 
| **Ricerca file** | Visualizza risultato in Lister universale | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Ricerca file** | Modifica risultato nell'editor di testo | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Ricerca file** | Vai a File nel pannello attivo | `Enter` / `⏎` | `Enter` | — | 
| **Ricerca file** | Inserisci i risultati nel pannello virtuale | Fare clic su `Feed to listbox` | Fare clic su `Feed to listbox` | — *(Azione finestra di dialogo)* | 
| **Riflettori e PNL**| Ricerca veloce Spotlight | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menu Comandi)* | 
| **Riflettori e PNL**| Attiva la barra dei comandi semantici | `/` | `/` | `cm_VisSemanticCommand` | 
| **Riflettori e PNL**| Ignora filtro semantico | `Esc` | `Esc` | — | 
| **Utilità file**| Dividi file in blocchi | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Utilità file**| Combina pezzi divisi numerati | Menu: File ➔ Combina file | — | `cm_FileLinker` / `cm_Combine` | 
| **Utilità file**| Calcola checksum (Hash) | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | 
| **Utilità file**| Verifica il file manifest del checksum | Menu Strumenti | Menu Strumenti | `cm_CheckSumVerify` / `cm_VerifyChecksum` | 
| **Utilità file**| Cancellazione multi-pass sicura (frantumazione)| `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | 
| **Utilità file**| Apri il terminale macOS nativo | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` |

--- 

<div align="center"> 
<p>Pronto per connetterti a server remoti ed esplorare archivi virtuali?</p> 
<p><strong><a href="network_and_vfs.md">Procedere al capitolo 6: File system virtuali e rete &rarr;</a></strong></p> 
</div>