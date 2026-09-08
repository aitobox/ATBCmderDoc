# Capitolo 8: Guida rapida alle scorciatoie da tastiera

ATBCmder è progettato da zero come un file manager basato sulla tastiera. Ogni operazione sui file, salto di directory, trasformazione di viste e utilità batch può essere eseguita senza alcuna interazione con il mouse. 

Per unire le tradizioni ortodosse di Commander con l'ergonomia nativa di Apple, ATBCmder utilizza un'**architettura di tastiera a doppia matrice**: ogni comando può essere richiamato utilizzando i classici tasti funzione di Commander (`F1`–`F12`, `Insert`, tastierino numerico) o accordi modificatori nativi di macOS (`⌘` Comando, `⌥` Opzione, `⇧` Maiusc, `⌃` Controllo). 

---

## 1. La filosofia della matrice duale e la notazione chiave

Che tu abbia vent'anni di memoria muscolare da Total Commander e Norton Commander o che tu viva interamente all'interno delle scorciatoie native del Finder di macOS, ATBCmder soddisfa i tuoi riflessi immediatamente senza richiedere la rimappatura manuale. 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  ARCHITETTURA TASTIERA A DOPPIA MATRICE                     │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  PARADIGMA CLASSICO COMMANDER        │  PARADIGMA NATIVO MACOS              │
│  • Tasti funzione al centro (F1–F12) │  • Modificatori di sistema (⌘, ⌥, ⇧) │
│  • Selezione tastierino (+, -, *)    │  • Piena parità con Finder (⌘C, ⌘V)  │
│  • Controllo rapido da tastiera      │  • Integrazione barra dei menu       │
│  Esempi:                             │  Esempi:                             │
│    F5        ➔ Copia file            │    ⌘C ➔ ⌘V   ➔ Copia file            │
│    F6        ➔ Sposta file           │    ⌘C ➔ ⌥⌘V  ➔ Sposta file           │
│    Shift+F4  ➔ Crea file di testo    │    ⇧⌘4       ➔ Crea file di testo    │
│    Alt+F7    ➔ Cerca file            │    ⌥⌘F       ➔ Cerca file            │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Simboli dei modificatori della tastiera Apple

In questa guida e nelle finestre di dialogo delle preferenze di ATBCmder, le combinazioni di tasti sono rappresentate utilizzando glifi tipografici standard di macOS: 

| Glifo | Nome modificatore | Equivalente a Windows/PC | Descrizione | 
| :---: | :--- | :--- | :--- | 
| **`⌘`** | **Comando** (`Cmd`) | `Win` / `Ctrl` | Chiave di modifica dell'azione primaria di macOS. | 
| **`⌥`** | **Opzione** (`Alt`) | `Alt` | Modificatore secondario per azioni alternative e caratteri speciali. | 
| **`⇧`** | **Maiusc** | `Shift` | Estende le selezioni, inverte le azioni o attiva le modalità maiuscole. | 
| **`⌃`** | **Controllo** (`Ctrl`) | `Ctrl` | Controllo del terminale e modificatore di accordi del comandante classico. | 
| **`⎋`** | **Fuga** (`Esc`) | `Esc` | Annulla le operazioni, cancella i filtri o chiude le finestre di dialogo. | 
| **`⏎`** | **Reso** (`Enter`) | `Enter` | Esegue azioni, apre elementi o conferma le richieste di dialogo. | 
| **`⌫`** | **Elimina/Backspace** | `Backspace` | Eliminazione dei caratteri all'indietro o navigazione nella directory principale. | 
| **`⌦`** | **Inoltra Elimina** | `Del` | Inoltra il carattere di eliminazione o elimina il file selezionato. | 
| **`⇥`** | **Tab** | `Tab` | Alterna il focus tra i pannelli di origine e di destinazione. | 
| **`⇞`** | **Pagina su** | `PgUp` | Scorre l'elenco del pannello in ordine di visualizzazione di una finestra. | 
| **`⇟`** | **Pagina giù** | `PgDn` | Scorre l'elenco del pannello verso il basso di una finestra. | 

---

## 2. Guida ai tasti funzione macOS (`Fn`).

> [!IMPORTANT] 
> ### Come utilizzare i tasti funzione sulle tastiere Mac 
> 
> Per impostazione predefinita, le tastiere Apple (incluse le tastiere MacBook integrate, le tastiere Magic e i Mac Touch Bar) assegnano la riga fisica superiore (da`F1` a `F12`) ai controlli hardware come luminosità del display, Mission Control, Spotlight, Dettatura, riproduzione multimediale e volume degli altoparlanti. 
> 
> Poiché i flussi di lavoro classici di Commander fanno molto affidamento su `F1`–`F12`, hai due opzioni: 
> 
> #### Metodo A: Tieni premuto l'accordo di chiave `Fn` (predefinito pronto all'uso) 
> Tieni premuto il tasto fisico **`Fn`** (o il tasto Globo 🌐) situato nell'angolo in basso a sinistra della tastiera del Mac mentre premi un tasto funzione qualsiasi: 
> 
> * **`Fn + F3`**: Visualizza il file in Lister 
> * **`Fn + F4`**: Modifica file 
> * **`Fn + F5`**: copia i file nel pannello di destinazione 
> * **`Fn + F6`**: sposta i file nel pannello di destinazione 
> * **`Fn + F7`**: Crea una nuova directory 
> * **`Fn + F8`**: Elimina file 
> * **`Fn + Shift + F4`**: crea e modifica un nuovo file di testo 
> * **`Fn + Alt + F7`**: apre Ricerca file 
> 
> #### Metodo B: abilitare "Tasti funzione standard" nelle Impostazioni macOS (consigliato) 
> Se usi ATBCmder regolarmente, cambia la riga delle funzioni in modo che premendo `F1`–`F12` si attivino direttamente i comandi funzione, mentre tenendo premuto `Fn` si attivino le regolazioni di luminosità e volume: 
> 
> 1. **macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia**: 
> - Apri ** Menu Apple ➔ Impostazioni di sistema...** 
> - Nella barra laterale sinistra, seleziona **Tastiera**. 
> - Fai clic sul pulsante **Scorciatoie da tastiera...**. 
> - Nella barra laterale della finestra di dialogo, seleziona **Tasti funzione**. 
> - Imposta **"Utilizza i tasti F1, F2, ecc. come tasti funzione standard"** su **ON**. 
> - Fare clic su **Fine**. 
> 
> 2. **macOS 12 Monterey e macOS 11 Big Sur**: 
> - Apri ** Menu Apple ➔ Preferenze di Sistema... ➔ Tastiera**. 
> - Nella scheda **Tastiera**, seleziona la casella denominata **"Utilizza i tasti F1, F2, ecc. come tasti funzione standard"**. 
> 
> #### Modelli di MacBook Pro con Touch Bar 
> 
> * Tieni premuto il tasto fisico **`Fn`** in basso a sinistra per visualizzare immediatamente la riga virtuale `F1`–`F12` sulla Touch Bar. 
> * In alternativa, configura **Impostazioni di sistema ➔ Tastiera ➔ Impostazioni Touch Bar...** e imposta **"Visualizza Touch Bar"** su **"Tasti F1, F2, ecc."** quando ATBCmder è l'applicazione attiva in primo piano. 
> 
> #### Tastiere compatte senza riga di funzioni dedicata 
> 
> * Se utilizzi una tastiera meccanica al 60% o al 65% senza tasti `F` dedicati, non è necessario contorcere le dita. Utilizza gli accordi modificatori macOS nativi di ATBCmder (`⌘C`, `⌥⌘V`, `⇧⌘N`, `⌘⌫`, `⌥⏎`) che forniscono parità operativa al 100%.

---

## 3. Architettura di scorciatoie con ambito contestuale

Per evitare collisioni di tasti di scelta rapida tra diverse aree di applicazione (ad esempio, la ricerca all'interno dell'elenco di file principale rispetto alla ricerca all'interno di un visualizzatore di file di testo), ATBCmder segmenta tutte le scorciatoie in contesti gerarchici distinti: 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       AMBITO APPLICAZIONE: Main                             │
│  Comandi globali, navigazione pannelli, schede, barra strumenti, strumenti  │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  AMBITO PANNELLO: FilePanel   │  AMBITI STRUMENTI MODALI                    │
│  Attivo durante l'esplorazione│  • Viewer      (Finestra Universal Lister)  │
│  di tabelle file e miniature  │  • Editor      (Editor di codice integrato) │
│  (selezione, filtri,          │  • Differ      (Confronto file affiancato)  │
│  rinomina diretta, calcolo)   │  • FindFiles   (Ricerca avanzata file)      │
│                               │  • MultiRename (Ridenominazione in blocco)  │
└───────────────────────────────┴─────────────────────────────────────────────┘
```
 

Quando premi un accordo chiave, il motore **`HotkeyManager`**: 

1. Valuta il contesto focalizzato attivo (ad esempio, `Viewer` o `FilePanel`). 
2. Se un'associazione esatta corrisponde, il comando `cm_*` associato viene eseguito immediatamente. 
3. Se non esiste alcuna associazione nel contesto locale, la sequenza di tasti ritorna con garbo al contesto `Main`. 
4. Se ancora non associato, subentra la modifica del testo standard o la gestione della sequenza di tasti del sistema. 

---

## 4. Tabelle principali categorizzate a doppia matrice

Le seguenti tabelle di riferimento documentano tutti i comandi supportati da ATBCmder, classificati in base al flusso di lavoro funzionale.

### 4.1 Operazioni sui file

Le operazioni sui file costituiscono la spina dorsale del lavoro quotidiano. Per impostazione predefinita, ogni operazione utilizza il paradigma **Sorgente ➔ Destinazione**: gli elementi selezionati nel pannello attivo vengono elaborati nella directory aperta nel pannello opposto inattivo.

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_View` | Visualizza il file utilizzando Universal Lister (anteprima di sola lettura) | `⌘3` / `Space` *(Visualizzazione rapida)* | `F3` / `Shift+F3` | Principale | 
| `cm_Edit` | Apri il file nell'editor di testo integrato | `⌘4` | `F4` | Principale | 
| `cm_EditNew` | Crea e modifica immediatamente un nuovo file di testo | `⇧⌘4` / `⇧F4` | `Shift+F4` | Principale | 
| `cm_Copy` | Copia i file selezionati dal pannello attivo a quello di destinazione | `⌘C` *(negli appunti)* / `F5` | `F5` | Principale | 
| `cm_CopySamePanel` | Duplica/clona il file selezionato nella stessa directory | `⇧F5` | `Shift+F5` | Principale | 
| `cm_Move` | Sposta i file selezionati dal pannello attivo a quello di destinazione | `⌥⌘V` *(incolla spostamento)* / `F6` | `F6` | Principale | 
| `cm_RenameOnly` | Rinomina rapida in linea del file sotto il cursore | `⏎` *(Ritorno)* / `F2` | `F2` / `Shift+F6` | Principale | 
| `cm_Rename` | Rinominare il file selezionato tramite la finestra di dialogo | `⇧F6` | `Shift+F6` | Principale | 
| `cm_MkDir` | Crea una nuova directory/cartella | `⇧⌘N` / `F7` | `F7` | Principale | 
| `cm_Delete` | Elimina gli elementi selezionati nel Cestino di macOS | `⌘⌫` *(Cmd+Canc)* / `⌦` | `F8` / `Delete` | Principale | 
| `cm_Wipe` | Elimina i file in modo sicuro (ignora il Cestino in modo permanente) | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | Pannello file | 
| `cm_Open` | Apri il file con l'app predefinita o inserisci la directory | `⌘↓` / `⏎` *(Ritorno)* | `Enter` | Principale | 
| `cm_SetFileProperties` | Ispeziona e modifica metadati, date e autorizzazioni UNIX dei file | `⌥⏎` *(Opzione+Invio)* / `⌘I` | `Alt+Enter` | Principale | 
| `cm_CountDirContent` | Calcola la dimensione in byte della directory sotto il cursore | `⌥⇧⏎` *(Opzione+Maiusc+Invio)* | `Alt+Shift+Enter` | Pannello file | 
| `cm_CalculateSpace` | Calcola la dimensione totale di tutte le directory selezionate | `⌃L` / `⌘L` | `Ctrl+L` | Principale | 
| `cm_SymLink` | Crea collegamento simbolico nel pannello di destinazione | `⌥⌘S` | *(Menu: File ➔ Collegamento simbolico)* | Principale | 
| `cm_HardLink` | Crea un collegamento reale al file system nel pannello di destinazione | `⌥⌘H` | *(Menu: File ➔ Collegamento fisso)* | Principale | 
| `cm_PackFiles` | Comprimi/comprimi i file selezionati nell'archivio (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Principale | 
| `cm_ExtractFiles` | Estrai i contenuti dell'archivio direttamente nel pannello di destinazione | `⌥F9` / `⌥⌘E` | `Alt+F9` | Principale | 
| `cm_ArchiveView` | Inserisci l'archivio come directory del filesystem virtuale (`vfs://`) | `⌃⇟` *(Ctrl+PagGiù)* / `⌘↓` | `Ctrl+PgDn` | Principale | 
| `cm_CompareContents` | Confronta il contenuto di due file selezionati | `⇧F3` | `Shift+F3` | Principale |

---

### 4.2 Selezione e marcatura

I file manager ortodossi eccellono nella rapida selezione di più file. ATBCmder consente di selezionare singoli elementi, modelli di caratteri jolly, gruppi di estensioni o blocchi continui senza utilizzare il mouse.

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_MarkMarkAll` | Seleziona tutti i file e le cartelle nel pannello attivo | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Principale | 
| `cm_MarkUnmarkAll` | Deseleziona tutti i file e le cartelle nel pannello attivo | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Principale | 
| `cm_MarkInvert` | Inverte lo stato di selezione corrente nel pannello attivo | `⌘I` / `⌃I` | `Num*` *(Tastiera `*`)* | Pannello file | 
| `cm_MarkPlus` | Seleziona il modello di carattere jolly corrispondente al gruppo (ad esempio `*.ts`) | `⌘+` / `⌃+` | `Num+` *(Tastiera `+`)* | Pannello file | 
| `cm_MarkMinus` | Deseleziona il modello di carattere jolly corrispondente al gruppo (ad esempio `*.log`) | `⌘-` / `⌃-` | `Num-` *(Tastiera `-`)* | Pannello file | 
| `cm_MarkCurrentExtension` | Seleziona tutti i file che condividono l'estensione file del cursore | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Principale | 
| `cm_UnmarkCurrentExt` | Deseleziona tutti i file che condividono l'estensione file del cursore | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Principale | 
| `cm_MarkCurrentName` | Seleziona tutti i file che condividono il nome file di base del cursore | `⌥⌘N` | *(Menu: Seleziona ➔ Stesso nome)* | Principale | 
| `cm_SelectOrDeselectFile` | Attiva/disattiva la selezione degli elementi e fai avanzare il cursore verso il basso | `Space` | `Insert` / `Space` | Pannello file | 
| `Shift+Up / Shift+Down` | Ampliare o contrarre la gamma di selezione continua | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | Pannello file | 
| `Shift+PageUp / Shift+PageDown` | Espandi la selezione continua per pagina con visualizzazione completa | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | Pannello file | 
| `cm_ClearAll` | Cancella tutti i segni di selezione e gli evidenziazioni della ricerca | `⌃L` | `Ctrl+L` | Principale | 
| `cm_CopyToClipboard` | Copia i file selezionati negli appunti del sistema macOS | `⌘C` | `Ctrl+C` | Principale | 
| `cm_CutToClipboard` | Taglia i file selezionati negli appunti del sistema macOS | `⌘X` | `Ctrl+X` | Principale | 
| `cm_PasteFromClipboard` | Incolla i file dagli appunti nella directory attiva | `⌘V` | `Ctrl+V` | Principale | 
| `cm_PasteAsMove` | Incolla file dagli appunti come operazione di spostamento | `⌥⌘V` | `Ctrl+Alt+V` | Principale | 
| `cm_CopyNamesToClip` | Copia i nomi dei file solo negli appunti | `⇧⌘X` | `Ctrl+Shift+X` | Principale | 
| `cm_CopyFullNamesToClip` | Copia i percorsi assoluti completi negli appunti | `⇧⌘C` | `Ctrl+Shift+C` | Principale | 
| `cm_CompareDirectories` | Contrassegna i file che esistono in un pannello ma non nell'altro | `⌥⇧C` | *(Menu: Seleziona ➔ Confronta Dirs)* | Principale |

---

### 4.3 Navigazione nel pannello e segnalibri

Spostati facilmente tra cartelle, volumi locali, montaggi di rete e cronologia di navigazione.

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FocusSwap` / `cm_SwitchPanel` | Focus tastiera alternativo tra i pannelli sinistro e destro | `⇥` *(Tab)* | `Tab` | Principale | 
| `cm_Refresh` | Aggiorna/rileggi il contenuto della directory attiva | `⌘R` / `⌃R` | `Ctrl+R` | Principale | 
| `cm_ChangeDirToParent` | Passare alla directory principale (`..`) | `⌘↑` / `⌫` *(Backspace)* | `Backspace` / `Ctrl+PgUp` | Principale | 
| `cm_ChangeDirToRoot` | Passa direttamente alla radice del filesystem (`/`) | `⌘\` | `Ctrl+\` | Principale | 
| `cm_ChangeDirToHome` | Passa direttamente alla cartella principale dell'utente (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | Pannello file | 
| `cm_ViewHistoryPrev` | Torna indietro nella cronologia di navigazione della directory | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Principale | 
| `cm_ViewHistoryNext` | Andare avanti nella cronologia di navigazione della directory | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Principale | 
| `cm_DirHistory` | Apri il menu a discesa della cronologia della directory interattiva | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Principale | 
| `cm_Drives` | Apri il popup dell'unità e del selettore del volume montato | `⌥D` | `Alt+D` | Principale | 
| `cm_LeftOpenDrives` | Aprire il menu di selezione dell'unità per il pannello sinistro | `⌥F1` | `Alt+F1` | Principale | 
| `cm_RightOpenDrives` | Aprire il menu di selezione dell'unità per il pannello destro | `⌥F2` | `Alt+F2` | Principale | 
| `cm_Exchange` | Scambia i pannelli sinistro e destro (directory, schede, stati) | `⌘U` | `Ctrl+U` | Principale | 
| `cm_TargetEqualSource` | Imposta la directory del pannello inattivo in modo che corrisponda alla directory attiva | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Principale | 
| `cm_SyncSlaveDir` | Blocca la navigazione del pannello di destinazione per eseguire il mirroring del pannello di origine | `⌥S` | *(Menu: Comandi ➔ Sincronizza Navigazione)* | Principale | 
| `cm_DirHotList` | Apri il menu Hotlist/Segnalibri della directory | `⌘D` | `Ctrl+D` | Principale | 
| `cm_ConfigDirHotList` | Apri la finestra di dialogo di configurazione della hotlist della directory | `⇧⌘D` | `Ctrl+Shift+D` | Principale | 
| `cm_GoToFirst` | Passa il cursore al primo elemento nel pannello attivo | `⌘↑` / `Fn+←` *(Casa)* | `Home` | Principale | 
| `cm_GoToLast` | Passa il cursore all'ultimo elemento nel pannello attivo | `⌘↓` / `Fn+→` *(Fine)* | `End` | Principale | 
| `PageUp / PageDown` | Scorrere il pannello attivo verso l'alto o verso il basso di una finestra intera | `⇞` *(Fn+↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | Pannello file |

---

### 4.4 Modalità di visualizzazione e ordinamento

Passa senza problemi tra elenchi compatti, colonne di metadati dettagliate, griglie visive di miniature, appiattimento ricorsivo delle directory e visualizzazioni ad albero sincronizzate.

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_BriefView` | Passa alla visualizzazione breve (nomi compatti a più colonne) | `⌃F1` | `Ctrl+F1` | Principale | 
| `cm_ColumnsView` | Passa alla visualizzazione colonne/dettagli (nome, dimensione, data, permanenti) | `⌃F2` | `Ctrl+F2` | Principale | 
| `cm_ThumbnailsView` | Passa alla visualizzazione griglia delle miniature (immagini, contenuti multimediali, PDF) | `⌃⇧F1` | `Ctrl+Shift+F1` | Principale | 
| `cm_FlatView` | Attiva/disattiva visualizzazione piatta/ramo (elenco di directory ricorsivo) | `⌘B` | `Ctrl+B` | Principale | 
| `cm_FlatViewSel` | Visualizzazione semplice/diramata solo delle directory selezionate | `⇧⌘B` | `Ctrl+Shift+B` | Principale | 
| `cm_TreeView` | Visualizzazione ad albero (Sostituisci il pannello attivo con l'albero delle directory) | `⌃⇧F8` | `Ctrl+Shift+F8` | Principale | 
| `cm_TreeViewSplit` | Visualizzazione ad albero (pannello diviso: albero in alto/a sinistra, file in basso/a destra) | `cm_TreeViewSplit` | *(Menu: Mostra ➔ Divisione vista ad albero)* | Principale | 
| `cm_TreeViewBoth` | Visualizzazione ad albero (entrambi i pannelli mostrano alberi di directory) | `cm_TreeViewBoth` | *(Menu: Mostra ➔ Visualizza entrambi ad albero)* | Principale | 
| `cm_QuickView` | Attiva/disattiva il pannello Visualizzazione rapida (anteprima dal vivo nel pannello opposto) | `⌘Q` / `⌃Q` | `Ctrl+Q` | Principale | 
| `cm_SortByName` | Ordina gli elementi per nome (attiva/disattiva ascendente/discendente) | `⌃F3` | `Ctrl+F3` | Principale | 
| `cm_SortByExt` | Ordina gli elementi per estensione | `⌃F4` | `Ctrl+F4` | Principale | 
| `cm_SortByDate` | Ordina gli elementi per data/ora di modifica | `⌃F5` | `Ctrl+F5` | Principale | 
| `cm_SortBySize` | Ordina gli elementi per dimensione file | `⌃F6` | `Ctrl+F6` | Principale | 
| `cm_SortByAttr` | Ordina gli elementi per attributi/autorizzazioni UNIX | `cm_SortByAttr` | *(Menu: Ordina ➔ Attributi)* | Principale | 
| `cm_ShowHiddenFiles` | Attiva/disattiva la visibilità dei file nascosti (`.` dotfiles) | `⌘H` / `⇧⌘.` | `Ctrl+H` | Principale | 
| `cm_ShowSysFiles` | Attiva/disattiva la visibilità del sistema macOS e dei file protetti | `⇧⌘.` | `Ctrl+.` | Principale | 
| `cm_QuickSearch` | Apri la barra di ricerca rapida nel pannello (digita le lettere per filtrare) | `⌥S` / `⌃S` *(o digitando)* | `Ctrl+S` / *(Digitazione lettere)* | Principale | 
| `cm_SemanticFilter` | Aprire la barra del filtro intelligente semantico del linguaggio naturale | `⌘F` | `Ctrl+F` | Principale | 
| `cm_HorizontalFilePanels` | Attiva/disattiva il layout orizzontale a doppio pannello (impilato verticalmente) | `⇧⌘H` | `Ctrl+Shift+H` | Principale |

---

### 4.5 Schede e gestione delle finestre

ATBCmder consente di aprire schede illimitate in entrambi i pannelli, bloccare le posizioni di lavoro preferite e gestire sessioni multischeda a doppio pannello.

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_NewTab` | Apri la nuova scheda della cartella nel pannello attivo | `⌘T` | `Ctrl+T` | Principale | 
| `cm_CloseTab` | Chiudi la scheda della cartella attualmente attiva | `⌘W` | `Ctrl+W` | Principale | 
| `cm_NextTab` / `cm_NextTabCtrl` | Passa alla scheda successiva a destra | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Principale | 
| `cm_PrevTab` / `cm_PrevTabCtrl` | Passa alla scheda precedente a sinistra | `⌃⇧⇥` *(Ctrl+Maiusc+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Principale | 
| `cm_ShowTabsList` | Mostra il menu a comparsa di tutte le schede aperte nel pannello attivo | `⇧⌘L` | `Ctrl+Shift+L` | Principale | 
| `cm_CloseAllTabs` | Chiudi tutte le schede nel pannello attivo tranne l'ultima | `⌥⌘W` | *(Menu contestuale scheda: Chiudi tutto)* | Principale | 
| `cm_CloseOtherTabs` | Chiudi tutte le schede diverse da quella attualmente attiva | `⇧⌘W` | *(Menu contestuale scheda: Chiudi altri)* | Principale | 
| `cm_Duplicatetab` | Scheda cartella attiva duplicata | `⌘D` / `cm_Duplicatetab` | *(Menu contestuale scheda: Duplica)* | Principale | 
| `cm_MoveTabLeft` | Sposta la scheda attiva di una posizione a sinistra | `⌃⇧←` | *(Menu contestuale scheda: sposta a sinistra)* | Principale | 
| `cm_MoveTabRight` | Sposta la scheda attiva di una posizione a destra | `⌃⇧→` | *(Menu contestuale scheda: sposta a destra)* | Principale | 
| `cm_CopyTabToOtherPanel` | Clona la scheda attiva direttamente nel pannello opposto | `⌥⌘T` | *(Menu contestuale scheda: Copia in altro)* | Principale | 
| `cm_SaveTab` / `cm_SaveTabs` | Salva il layout della scheda corrente nella configurazione | `cm_SaveTab` | *(Menu: Schede ➔ Salva Schede)* | Principale | 
| `cm_LoadTab` / `cm_LoadTabs` | Ripristina il layout della scheda salvato dalla configurazione | `cm_LoadTab` | *(Menu: Schede ➔ Carica schede)* | Principale | 
| `cm_OptionsFavorites` | Configura set di schede preferite e aree di lavoro persistenti | `cm_OptionsFavorites` | *(Menu: Schede ➔ Schede preferite)* | Principale | 
| `cm_FullScreen` | Attiva/disattiva la finestra dell'applicazione a schermo intero | `⌃⌘F` / `F11` | `F11` | Principale |

---

### 4.6 Utensili elettrici e utilità

Avvia strumenti di automazione avanzati, utilità batch e strumenti di sistema integrati direttamente dagli accordi della tastiera.

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FileSearch` / `cm_Search` | Apri la finestra di dialogo Ricerca avanzata multifiltro | `⌥F7` / `⌥⌘F` | `Alt+F7` | Principale | 
| `cm_FileDiff` / `cm_CompareFiles` | Apri visualizzatore differenze file visivi affiancati | `⌘⇧F12` | `Meta+Shift+F12` | Principale | 
| `cm_SyncDirs` | Apri lo strumento di sincronizzazione della directory bidirezionale | `⇧F12` | `Shift+F12` | Principale | 
| `cm_MultiRename` | Strumento di ridenominazione in blocco (Multi-Rename) batch aperto (RegEx e token) | `⌘M` | `Ctrl+M` | Principale | 
| `cm_Split` | Dividi file di grandi dimensioni in segmenti uniformi | `⌥F6` | `Alt+F6` | Principale | 
| `cm_Combine` | Combina nuovamente i segmenti numerati divisi nel file originale | `⌥F7` | `Alt+F7` | Principale | 
| `cm_CalculateChecksum` | Calcola l'hash crittografico (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Principale | 
| `cm_VerifyChecksum` | Verifica i file rispetto al file di checksum (`.md5`, `.sha256`) | `cm_VerifyChecksum` | *(Menu: File ➔ Verifica checksum)* | Principale | 
| `cm_RunTerm` | Avvia il terminale di sistema nella directory del pannello attivo | `⌃J` / `F9` | `Ctrl+J` / `F9` | Principale | 
| `cm_FocusCmdLine` | Sposta il focus della tastiera direttamente sulla riga di comando inferiore | `⇧F2` | `Shift+F2` | Principale | 
| `cm_ShowCmdLineHistory` | Apri il menu a discesa della cronologia dei comandi shell precedenti | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Principale | 
| `cm_AddPathToCmdLine` | Aggiungi il percorso della directory attiva alla riga di comando | `⌘P` | `Ctrl+P` | Principale | 
| `cm_ShowCommandLine` | Attiva/disattiva la riga di comando inferiore/barra di input della console | `⌘O` | `Ctrl+O` | Principale | 
| `cm_DiskBenchmark` | Eseguire il benchmark delle prestazioni di lettura/scrittura dell'unità di archiviazione | `cm_DiskBenchmark` | *(Menu: Comandi ➔ Benchmark)* | Principale | 
| `cm_VisSemanticCommand` | Apri la barra dei comandi di ricerca semantica e linguaggio naturale | `/` / `⇧⌘P` | `/` | Principale |

---

### 4.7 Sistema, configurazione e guida

Accedi alle preferenze dell'applicazione, alla gestione della configurazione, agli aggiornamenti software e alla documentazione utente. 

| ID comando | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_Options` | Apri Preferenze applicazione/Finestra di dialogo Impostazioni | `⌘,` | `Ctrl+,` | Principale | 
| `cm_HelpContents` / `cm_HelpIndex` | Apri documentazione e guida interattive per l'utente | `⌘?` / `F1` | `F1` | Principale | 
| `cm_HelpKeyboard` | Apri la scheda di riferimento delle scorciatoie da tastiera rapide | `cm_HelpKeyboard` | *(Menu: Aiuto ➔ Tastiera)* | Principale | 
| `cm_Exit` | Esci/Esci da ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Principale | 
| `cm_About` | Visualizza versione, licenza e crediti di ATBCmder | `cm_About` | *(Menu: ATBCmder ➔ Informazioni)* | Principale | 
| `cm_OpenConfigDirectory` | Rivela la cartella di configurazione (`atbcmder.xml`) nel pannello | `cm_OpenConfigDirectory` | *(Menu: Configurazione ➔ Apri Configurazione)* | Principale | 
| `cm_ExportConfiguration` | Esporta tutte le preferenze nel pacchetto ZIP portatile | `cm_ExportConfiguration` | *(Menu: Configurazione ➔ Esporta)* | Principale | 
| `cm_ImportConfiguration` | Importa le preferenze dal pacchetto ZIP portatile | `cm_ImportConfiguration` | *(Menu: Configurazione ➔ Importa)* | Principale | 
| `cm_CheckForUpdate` | Verifica la disponibilità di aggiornamenti del software applicativo | `cm_CheckForUpdate` | *(Menu: Aiuto ➔ Controlla aggiornamenti)* | Principale | 

---

## 5. Scorciatoie di contesto dello strumento modale

Quando si aprono strumenti specializzati come Universal Lister, l'editor di testo integrato, le differenze affiancate o le finestre di dialogo batch, ATBCmder attiva mappe di tasti specifiche del contesto. Questi collegamenti funzionano direttamente all'interno di ciascuna finestra degli strumenti anziché tramite comandi di registro `cm_*` globali a livello di applicazione.

### 5.1 Lister universale (`Viewer` Contesto)

Attivo durante l'anteprima di documenti, testo, codice, immagini, audio, video o byte esadecimali grezzi.

| Azione/Caratteristica | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| Seleziona tutto | Seleziona tutto il testo/contenuto nel visualizzatore | `⌘A` | `Ctrl+A` | Visualizzatore | 
| Modalità testo normale | Passa alla modalità Testo normale | `1` | `1` | Visualizzatore | 
| Modalità binaria | Passa alla modalità binaria | `2` | `2` | Visualizzatore | 
| Modalità esadecimale grezza | Passa alla modalità di ispezione dei byte esadecimali grezzi | `3` | `3` | Visualizzatore | 
| Modalità decimale | Passa alla modalità decimale | `4` | `4` | Visualizzatore | 
| Visualizza libro | Passa alla modalità Libro impaginato | `5` | `5` | Visualizzatore | 
| Visualizzazione immagine | Passa alla modalità visualizzatore immagini | `6` | `6` | Visualizzatore | 
| Plugin personalizzati | Passa al visualizzatore plug-in personalizzato | `7` | `7` | Visualizzatore | 
| PDF / Visualizzazione ufficio | Passa alla modalità lettore documenti PDF/Office | `8` | `8` | Visualizzatore | 
| Modalità codice | Passa alla modalità codice evidenziato dalla sintassi | `9` | `9` | Visualizzatore | 
| Immagine centrale | Centra l'immagine nella finestra del visualizzatore | `C` | `C` | Visualizzatore | 
| Adatta alla finestra | Adatta l'immagine alle dimensioni della finestra | `F` | `F` | Visualizzatore | 
| Vestibilità solo grande | Ridimensiona solo se l'immagine supera le dimensioni della finestra | `L` | `L` | Visualizzatore | 
| Attiva/disattiva Avvolgi | Attiva/disattiva l'avvolgimento della riga | `W` | `W` | Visualizzatore | 
| Attiva/disattiva il cursore | Attiva/disattiva il cursore del testo visibile | `F6` | `F6` | Visualizzatore | 
| Trova testo | Trova testo all'interno del documento | `⌘F` / `F7` | `F7` | Visualizzatore | 
| Trova successivo | Passa alla corrispondenza di ricerca successiva | `⌘G` / `F3` | `F3` | Visualizzatore | 
| Trova precedente | Passa alla corrispondenza di ricerca precedente | `⇧⌘G` / `⇧F3` | `Shift+F3` | Visualizzatore | 
| Zoom avanti | Ingrandisci l'immagine o il PDF | `⌘+` / `Num+` | `Num+` | Visualizzatore | 
| Riduci lo zoom | Rimpicciolisci immagine o PDF | `⌘-` / `Num-` | `Num-` | Visualizzatore | 
| Schermo intero | Attiva/disattiva la modalità di visualizzazione a schermo intero | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Visualizzatore | 
| Chiudi Visualizzatore | Chiudi la finestra del visualizzatore Lister | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Visualizzatore |

---

### 5.2 Editor di testo integrato (`Editor` Contesto)

Attivo durante la creazione o la modifica di file di testo e di codice sorgente. 

| Azione/Caratteristica | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| Salva file | Salva il file modificato su disco | `⌘S` / `F2` | `F2` | Redattore | 
| Trova testo | Trova il testo nel documento dell'editor | `⌘F` / `F7` | `F7` | Redattore | 
| Trova successivo | Passa alla corrispondenza di ricerca successiva | `⌘G` / `F3` | `F3` | Redattore | 
| Trova precedente | Passa alla corrispondenza di ricerca precedente | `⇧⌘G` / `⇧F3` | `Shift+F3` | Redattore | 
| Taglia | Taglia il testo selezionato negli appunti | `⌘X` | `Ctrl+X` | Redattore | 
| Copia | Copia il testo selezionato negli appunti | `⌘C` | `Ctrl+C` | Redattore | 
| Incolla | Incolla il testo dagli appunti | `⌘V` | `Ctrl+V` | Redattore | 
| Annulla | Annulla l'ultima azione di digitazione | `⌘Z` | `Ctrl+Z` | Redattore | 
| Rifare | Ripeti l'ultima azione annullata | `⇧⌘Z` | `Ctrl+Shift+Z` | Redattore | 
| Seleziona tutto | Seleziona il testo dell'intero documento | `⌘A` | `Ctrl+A` | Redattore | 
| Chiudi Editor | Chiudi la finestra dell'editor di testo | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Redattore | 

---

### 5.3 Differenza visiva affiancata (`Differ` Contesto)

Attivo all'interno dello strumento di confronto delle differenze visive. 

| Azione/Caratteristica | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| Trova testo | Cerca testo nei riquadri delle differenze | `⌘F` / `F7` | `F7` | Differire | 
| Trova successivo | Passa alla occorrenza di ricerca successiva | `⌘G` / `F3` | `F3` | Differire | 
| Trova precedente | Passa all'occorrenza di ricerca precedente | `⇧⌘G` / `⇧F3` | `Shift+F3` | Differire | 
| Differenza successiva | Salta il cursore al blocco differenza successivo | `⌥↓` *(Opzione+Giù)* | `Alt+Down` | Differire | 
| Differenza precedente | Salta il cursore al blocco differenza precedente | `⌥↑` *(Opzione+Su)* | `Alt+Up` | Differire | 
| Prima differenza | Passa direttamente alla prima differenza nei file | `⌥Fn+←` *(Opz+Home)* | `Alt+Home` | Differire | 
| Ultima differenza | Passa direttamente all'ultima differenza nei file | `⌥Fn+→` *(Opz+Fine)* | `Alt+End` | Differire | 
| Copia da destra a sinistra | Copia il blocco differenza dal riquadro destro al riquadro sinistro | `⌥←` *(Opzione+Sinistra)* | `Alt+Left` | Differire | 
| Copia da sinistra a destra | Copia il blocco differenza dal riquadro sinistro al riquadro destro | `⌥→` *(Opzione+Destra)* | `Alt+Right` | Differire | 
| Aggiorna/Riesegui scansione | Rileggere i file dal disco ed eseguire nuovamente il confronto delle differenze | `⌘R` | `Ctrl+R` | Differire | 
| Chiudi Differisce | Finestra di confronto delle differenze ravvicinate | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | Differire | 

---

### 5.4 Finestra di dialogo Ricerca file avanzata (contesto`FindFiles`)

Attivo all'interno della finestra di dialogo di ricerca multi-thread in background. 

| Azione/Caratteristica | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| Inizia la ricerca | Avvia l'esecuzione della ricerca | `⏎` *(Ritorno)* / `F9` | `F9` | TrovaFile | 
| Annulla / Chiudi | Annulla la ricerca in corso o chiudi la finestra di dialogo | `⎋` *(Esc)* | `Esc` | TrovaFile | 
| Visualizza selezionati | Visualizza il risultato della ricerca selezionato in Lister | `⌘3` / `F3` | `F3` | TrovaFile | 
| Modifica selezionati | Apri il risultato della ricerca selezionato in Editor | `⌘4` / `F4` | `F4` | TrovaFile | 
| Nuova ricerca | Reimposta la query di ricerca e prepara una nuova ricerca | `⌘N` | `Ctrl+N` | TrovaFile | 
| Cancella filtri | Nuova ricerca con tutti i filtri di data/dimensione/attributo deselezionati | `⇧⌘N` | `Ctrl+Shift+N` | TrovaFile | 
| Richiama precedente | Richiama parametri dalla ricerca precedente | `⌘L` | `Ctrl+L` | TrovaFile | 

---

### 5.5 Strumento di ridenominazione in blocco (Multi-Rename) batch (contesto`MultiRename`)

Attivo all'interno dell'area di lavoro di ridenominazione batch. 

| Azione/Caratteristica | Descrizione | Scorciatoia macOS principale (con glifi ⌘/⌥/⇧/⌃) | Scorciatoia Commander classica (con tasti Fn) | Contesto | 
| :--- | :--- | :---: | :---: | :---: | 
| Reimposta regole | Ripristina le regole di ridenominazione della maschera e del modello sui valori predefiniti | `⌘R` | `Ctrl+R` | MultiRinomina | 
| Modifica nomi nell'editor | Apri l'elenco dei nomi dei file di destinazione nell'editor esterno per la modifica manuale | `⌘I` | `Ctrl+I` | MultiRinomina | 
| Carica file nomi | Carica i nomi sostitutivi da un file di testo esterno | `F3` | `F3` | MultiRinomina | 

---

## 6. Suggerimenti professionali e ottimizzazione dei tasti di scelta rapida del sistema

### 6.1 Risoluzione delle collisioni di scorciatoie globali macOS

Alcuni tasti di scelta rapida predefiniti del sistema macOS intercettano la pressione dei tasti prima che raggiungano le applicazioni desktop. Per sbloccare la piena agilità di Commander, puoi personalizzare o disabilitare le scorciatoie macOS in conflitto: 

1. **Ricerca Spotlight (`⌘Space` rispetto a Ricerca rapida)**: 
- Per impostazione predefinita, `⌘Space` attiva Spotlight. Se preferisci utilizzare `⌘Space` per contrassegnare i file o per la ricerca nel pannello, rimappa Spotlight su `⌥Space` in **Impostazioni di sistema ➔ Tastiera ➔ Scorciatoie da tastiera... ➔ Spotlight**. 
2. **Controllo missione (`⌃↑`) ed esposizione app (`⌃↓`)**: 
- macOS utilizza `⌃↑` e `⌃↓` per Mission Control. In ATBCmder, `⌃↓` apre il menu a discesa Cronologia directory. Puoi riassegnare Mission Control in **Impostazioni di sistema ➔ Tastiera ➔ Scorciatoie da tastiera... ➔ Mission Control**. 
3. **Nascondi applicazione (`⌘H`)**: 
- In macOS, `⌘H` nasconde l'applicazione in primo piano. ATBCmder utilizza `⌘H` o `⇧⌘.` per attivare/disattivare i dotfile nascosti. Se desideri che `⌘H` attivi o meno i file nascosti, disabilita "Nascondi applicazione" in macOS o utilizza lo standard Finder `⇧⌘.` (`Cmd+Shift+Period`). 
4. **Riduzione a icona della finestra (`⌘M`)**: 
- macOS assegna `⌘M` per ridurre a icona la finestra nel Dock. ATBCmder assegna `⌘M` allo strumento di ridenominazione multipla batch (`cm_MultiRename`). ATBCmder cattura `⌘M` nella sua finestra principale, ma puoi anche attivare la ridenominazione multipla tramite `Ctrl+M` o la barra degli strumenti. 

---

### 6.2 Ergonomia del trackpad e del mouse

Per gli utenti di laptop senza tastiera esterna, ATBCmder abbina le scorciatoie da tastiera con gesti intuitivi sul trackpad: 

* **Pizzica per ingrandire le miniature**: nella visualizzazione miniature (`cm_ThumbnailsView`), pizzica dentro o fuori sul trackpad del tuo MacBook (o tieni premuto `⌃` e scorri) per ridimensionare continuamente le anteprime delle miniature da `48 px` fino a `512 px`. 
* **Scorri indietro/avanti con due dita**: scorri verso sinistra o verso destra con due dita sulla tabella dei file per navigare indietro (`cm_ViewHistoryPrev`) e avanti (`cm_ViewHistoryNext`) nella cronologia delle cartelle. 
* **Divisore con doppio clic**: fai doppio clic in un punto qualsiasi della barra divisoria centrale verticale per reimpostare i pannelli su una divisione orizzontale esatta 50/50. 
* **Fare clic con il pulsante centrale sulle schede**: fare clic con il pulsante centrale (o toccare con tre dita) su qualsiasi scheda di una cartella per chiuderla immediatamente senza premere `⌘W`. 

---

### 6.3 Personalizzazione delle combinazioni di tasti nelle Preferenze

Ogni scorciatoia documentata sopra può essere personalizzata o ripristinata: 

1. Premi **`⌘,`** (o seleziona **Configurazione ➔ Opzioni...**) per aprire la finestra di dialogo Preferenze. 
2. Seleziona **Tasti di scelta rapida** dalla barra laterale. 
3. Utilizza il menu a discesa **Contesto** per scegliere quale area desideri configurare (`Main`, `FilePanel`, `Viewer`, ecc.). 
4. Utilizzare la casella del filtro di ricerca per individuare qualsiasi comando in base al nome o all'ID `cm_*`. 
5. Fare clic sulla casella di scelta rapida e premere la combinazione di tasti desiderata. Il rilevatore di collisioni integrato ti avviserà immediatamente se quell'accordo è già assegnato altrove. 
6. Fare clic su **Applica** per attivare immediatamente le modifiche senza riavviare l'applicazione. 

Le combinazioni di tasti dell'utente vengono salvate in `~/.config/atbcmder/atbcmder_hotkeys.xml` (o `~/Library/Preferenze/atbcmder/` su macOS). Puoi esportare e trasferire questo file su più computer utilizzando **`cm_ExportConfiguration`**. 

--- 

<div align="center"> 
<p>Cerchi ricette pratiche per tutti i giorni, flussi di lavoro per il montaggio del NAS o suggerimenti per la risoluzione dei problemi?</p> 
<p><strong><a href="faq_howtos.md">Procedi al capitolo 9: Ricette reali e risoluzione dei problemi &rarr;</a></strong></p> 
</div>