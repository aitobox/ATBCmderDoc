# Capitolo 2: Navigazione e schede delle cartelle

Il movimento fluido e ad alta velocità attraverso le directory è la pietra angolare della gestione dei file ortodossa. In ATBCmder, non dovrai mai perdere tempo trascinando le barre di scorrimento, facendo ripetutamente clic sulle cartelle nidificate o lottando con dozzine di finestre del Finder frammentate. 

Questo capitolo tratta tutto ciò di cui hai bisogno per navigare nei file system locali e remoti con assoluta sicurezza: breadcrumb interattivi, salti nella gerarchia della tastiera, flussi di lavoro multi-scheda nativi di macOS, aree di lavoro persistenti con schede preferite a doppio pannello, segnalibri con ricerca fuzzy istantanea e cinque modalità di visualizzazione del pannello specializzate. 

---

## 1. Avvio rapido visivo: gerarchia semplice e organizzazione spaziale

In ATBCmder, ogni pannello funziona come un motore di navigazione autonomo dotato di una propria catena breadcrumb, tabstrip indipendente, stack cronologico e modalità di visualizzazione. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [PERCORSO]    🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [SCHEDE]      [★ Sorgente (Bloccato)] [Risorse] [Output Build] [+]              │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Nome                         Tipo      Dimens.   Modificato il      Permessi   │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Oggi, 14:22        drwxr-xr-x │
│  ▸ ui                         <DIR>               Oggi, 15:05        drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Oggi, 15:10        -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Ieri, 19:40        -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [RICERCA RAPIDA]  🔍 Cerca: mai_   (Corrispondenza: main.py)                    │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Foglio informativo sulla navigazione a doppia matrice

| Azione | Scorciatoia macOS | Chiave del comandante classico | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Directory principale** | `Backspace` / `⌘↑` | `Ctrl+PgUp` | `cm_ChangeDirToParent` | Sali di un livello nella directory (`..`). | 
| **Directory principale** | `Ctrl+\` / `⌃\` | `\` | `cm_ChangeDirToRoot` | Passa direttamente alla radice del sistema (`/`). | 
| **Directory principale** | `Ctrl+Shift+Home` / `⌃⇧Home` | `Alt+Home` | `cm_ChangeDirToHome` | Passa alla directory home dell'utente (`~`). | 
| **Apri elemento/Inserisci directory** | `Enter` / `⌘↓` | `Enter` | — | Entra nella directory selezionata o apri il file. | 
| **Nuova scheda** | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | Apri la cartella attiva in una nuova scheda. | 
| **Chiudi scheda** | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | Chiudi la scheda attualmente attiva. | 
| **Hotlist delle directory** | `Ctrl+D` / `⌃D` | `Ctrl+D` | `cm_DirHotList` | Apri il popup dei segnalibri fuzzy istantanei. | 
| **Storia indietro** | `Cmd+[` / `⌘[` | `Alt+Left` | `cm_ViewHistoryPrev` | Torna alla cartella visitata in precedenza. | 
| **Storia in avanti** | `Cmd+]` / `⌘]` | `Alt+Right` | `cm_ViewHistoryNext` | Andare avanti nella cronologia della directory. | 
| **Elenco a discesa della cronologia** | `Alt+F8` / `⌥F8` | `Ctrl+Down` | `cm_DirHistory` | Visualizza l'elenco a discesa della cronologia. | 
| **Elenco unità/volumi (sinistra/destra)** | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | `cm_LeftOpenDrives` / `cm_RightOpenDrives` (`cm_Drives`) | Aprire il menu dell'unità per il pannello sinistro o destro (`Alt+D` per il pannello attivo). | 
| **Ricerca rapida** | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_QuickSearch` | Apri l'overlay di ricerca in tempo reale nel pannello. | 

---

## 2. Navigazione di base nelle directory: percorsi, breadcrumb e scorciatoie

ATBCmder ti offre molteplici modi ridondanti ed ergonomici per muoverti nel tuo filesystem, sia che tu preferisca i gesti del mouse, i clic del trackpad o la pura velocità della tastiera.

### Navigazione tramite mouse e trackpad

- **Inserimento di cartelle**: fare doppio clic su qualsiasi riga della directory o premere `Enter` (`Return`). 
- **Gerarchie ascendenti**: fai doppio clic sulla riga superiore `[..]` per passare immediatamente alla cartella principale. 
- **Schede in background**: fai clic con il tasto centrale su qualsiasi riga di cartella per aprire la directory in una nuova scheda in background senza perdere la visualizzazione corrente (`cm_OpenDirInNewTab`).

### Barra breadcrumb interattiva in stile Finder

Posizionata direttamente sopra ciascun pannello dei file, la barra breadcrumb interattiva rappresenta il percorso UNIX corrente come una catena di segmenti cliccabili: 

```
🏠 / ▸ Users ▸ brain ▸ Projects ▸ ATBCmder ▸ docs
```
 

1. **Salto istantaneo dell'antenato**: fai clic su qualsiasi segmento dell'antenato (come `Projects` o `Users`) per passare direttamente a quel livello, ignorando la navigazione di più cartelle principali. 
2. **Elenchi a discesa delle directory di pari livello**: passa il mouse sopra o fai clic sulla freccia di espansione (`▸`) tra i segmenti per visualizzare un menu a discesa che elenca tutte le cartelle di pari livello a quel livello di gerarchia. Fai clic su qualsiasi fratello per accedervi direttamente. 
3. **Utilità contestuali**: fai clic con il pulsante destro del mouse su qualsiasi segmento breadcrumb per richiamare un menu contestuale dedicato: 
- **Apri in una nuova scheda**: apre la cartella specifica dell'antenato in una nuova scheda. 
- **Mostra nel Finder**: apre la directory nel Finder nativo di macOS (`open -R`). 
- **Copia percorso**: copia il percorso UNIX assoluto del segmento negli appunti di macOS. 
- **Apri nel terminale**: apre una finestra di terminale all'interno di quella directory esatta. 
4. **Modifica testo percorso diretto (`BreadcrumbLineEdit`)**: 
- Fai doppio clic sullo spazio vuoto a destra della catena breadcrumb (o premi `Shift+F2`). 
- I segmenti breadcrumb si trasformano istantaneamente in un campo di testo modificabile (`QLineEdit`). 
- Digita o incolla percorsi arbitrari (come `~/Library/Application Support`, `/var/log`, `/Volumes/ExternalDrive` o posizioni di archivio `vfs://`). 
- Premi `Enter` per saltare o `Esc` per annullare e tornare ai pulsanti breadcrumb.

### Salti rapidi sulla tastiera

Tieni le mani sulla riga home con questi comandi di navigazione dedicati: 

- **Directory principale (`Backspace` / `⌘↑` / `Ctrl+PgUp` / `cm_ChangeDirToParent`)**: sale istantaneamente alla directory principale. Quando sali, ATBCmder posiziona automaticamente il cursore sulla cartella appena uscita, assicurandoti di non perdere mai la posizione. 
- **Directory principale (`Ctrl+\` / `cm_ChangeDirToRoot`)**: passa direttamente alla radice del volume di avvio di macOS (`/`). 
- **Directory home (`Ctrl+Shift+Home` / `cm_ChangeDirToHome`)**: passa direttamente alla directory home dell'utente (`/Users/username` o `~`). 
- **Prima e ultima voce**: premi `Home` (`cm_GoToFirst`) per posizionare il cursore sulla voce principale (`..`) o `End` (`cm_GoToLast`) per passare al file finale nel pannello corrente. 

---

## 3. Schede delle cartelle: multitasking all'interno di ciascun pannello

Lavorare su progetti software complessi, librerie di foto o backup di server spesso richiede di destreggiarsi tra più cartelle contemporaneamente. Invece di aprire dozzine di finestre, ATBCmder incorpora strisce multi-tab indipendenti per entrambi i pannelli. 

![Folder Tabs and Splitters](images/quick_access_paths.png) 
*Gestione multi-scheda e navigazione rapida in ATBCmder*

### Design nativo della barra delle schede di macOS

Costruita con `MacNativeTabBar`, la barra delle schede corrisponde all'estetica moderna di macOS: 

- **Design visivo**: angoli delle schede arrotondati, stati fluidi al passaggio del mouse e chiari indicatori di accento delle schede attive. 
- **Pulsanti di chiusura al passaggio del mouse**: ogni scheda presenta un pulsante di chiusura `✕` integrato che appare al passaggio del mouse o alla selezione. 
- **Fai clic con il pulsante centrale per chiudere**: fai clic su qualsiasi scheda con il pulsante centrale del mouse o fai clic con tre dita sul trackpad per chiuderla immediatamente. 
- **Fai doppio clic per aggiungere**: fai doppio clic su uno spazio vuoto sulla tabstrip per generare immediatamente una nuova scheda clonata dal percorso attivo.

### Operazioni sulle schede e tasti di scelta rapida

| Azione | Scorciatoia macOS | Chiave classica | ID comando | Descrizione | 
| :--- | :--- | :--- | :--- | :--- | 
| **Nuova scheda** | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | Apre la directory corrente in una nuova scheda. | 
| **Chiudi scheda** | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | Chiude la scheda attiva (minimo 1 scheda conservata). | 
| **Scheda successiva** | `Ctrl+Tab` / `⌃⇥` | `Ctrl+Tab` | `cm_NextTab` | I cicli si concentrano sulla scheda successiva a destra. | 
| **Scheda precedente** | `Ctrl+Shift+Tab` / `⌃⇧⇥` | `Ctrl+Shift+Tab` | `cm_PrevTab` | I cicli si concentrano sulla scheda precedente a sinistra. | 
| **Elenco schede rapide** | `Ctrl+Shift+L` / `⌃⇧L` | `Ctrl+Shift+L` | `cm_ShowTabsList` | Viene visualizzato un menu numerato di tutte le schede aperte. | 
| **Rinomina scheda** | *Fare clic con il pulsante destro del mouse sulla scheda* | — | `cm_RenameTab` | Assegna un'etichetta personalizzata personalizzata alla scheda. | 
| **Chiudi altre schede** | *Fare clic con il pulsante destro del mouse sulla scheda* | — | `cm_CloseOtherTabs` | Chiude tutte le schede tranne quella selezionata. | 
| **Chiudi duplicati** | *Fare clic con il pulsante destro del mouse sulla scheda* | — | `cm_CloseDuplicateTabs` | Rileva e chiude le schede duplicate con percorsi identici. | 
| **Chiudi tutte le schede** | *Schede menu* | — | `cm_CloseAllTabs` | Ripristina il pannello a una singola scheda. | 
| **Copia nella pagina accanto** | *Schede menu* | — | `cm_CopyAllTabsToOpposite` | Copia tutte le schede del pannello attivo nel pannello di destinazione. |

### Modalità di blocco delle schede

Previeni modifiche accidentali della directory nelle cartelle critiche configurando le opzioni di blocco delle schede. Fare clic con il pulsante destro del mouse su qualsiasi scheda per scegliere la modalità di blocco: 

1. **Normale (sbloccato)**: 
- Comportamento predefinito della scheda. 
- La navigazione tra le cartelle aggiorna direttamente il percorso della scheda corrente. 
2. **Bloccato (`cmd_SetTabOptionLock`)**: 
- Il percorso della scheda è rigorosamente congelato nella posizione di ancoraggio iniziale. 
- Sul titolo della scheda viene visualizzata l'icona di un lucchetto (`🔒` o `★`). 
- Se fai doppio clic su una sottodirectory o navighi, ATBCmder lascia automaticamente invariata la scheda bloccata e apre la cartella di destinazione in una **nuova scheda adiacente**. 
3. **Bloccato con sottodirectory consentite (`cmd_SetTabOptionLockWithSubdirs`)**: 
- Ti consente di navigare liberamente nelle cartelle secondarie e nelle sottodirectory all'interno di questo albero. 
- Ti impedisce di salire più in alto della cartella base bloccata. 
- Se allontani o ricarichi, la scheda viene ripristinata in modo sicuro alla sua radice di ancoraggio. 

---

## 4. Schede preferite: aree di lavoro a doppio pannello denominate

Mentre le singole schede offrono flessibilità locale, le **Schede preferite** consentono di acquisire e ripristinare ambienti operativi completi a doppio pannello in un unico comando. 

```
┌────────────────────────────────────────┐
│ FAVORITE TAB SET: "Client Release"     │
├───────────────────┬────────────────────┤
│ LEFT PANEL TABS   │ RIGHT PANEL TABS   │
│ 1. [★ src/api]    │ 1. [build/dist]    │
│ 2. [docs/guides]  │ 2. [vfs://sftp/nas]│
│ 3. [tests/unit]   │ 3. [~/Downloads]   │
└───────────────────┴────────────────────┘
```
 

Un set di schede preferite incapsula: 

- Tutte le schede aperte nel pannello sinistro (inclusi percorsi e stati di blocco). 
- Tutte le schede aperte nel pannello di destra (inclusi percorsi e stati di blocco). 
- La selezione della scheda attiva per entrambi i pannelli.

### Comandi delle schede preferite

- **Salva schede correnti (`cm_SaveFavoriteTabs`)**: 
- Accessibile tramite il menu **Preferiti** → **Salva le schede correnti in una nuova scheda preferita** o facendo clic con il pulsante destro del mouse sulla tabstrip. 
- Richiede di nominare l'area di lavoro (ad esempio, `Rust Web Backend`, `Photo Editing 2026` o `Server Deployment`). 
- Memorizza la definizione dell'area di lavoro in modo persistente in `fav_tab_config.xml`. 
- **Carica schede preferite (`cm_LoadFavoriteTabs`)**: 
- Accessibile tramite il menu **Preferiti** → **Carica le schede dalle schede preferite**. 
- Apre una finestra di dialogo modale che elenca i set di schede salvate. Seleziona un set ed entrambi i pannelli ricostruiranno immediatamente l'intero layout multischeda. 
- **Salva nuovamente le schede preferite (`cm_ResaveFavoriteTabs`)**: 
- Aggiorna il set di aree di lavoro attualmente attivo con tutte le schede appena aperte, chiuse o esplorate senza richiedere un nuovo nome. 
- **Ricarica le schede preferite (`cm_ReloadFavoriteTabs`)**: 
- Ripristina entrambi i pannelli allo stato salvato pulito dell'area di lavoro attiva, eliminando eventuali schede esplorative aperte durante la sessione. 
- **Scorri le aree di lavoro (schede preferite successive/precedenti)**: 
- Passa rapidamente tra le diverse aree di lavoro del progetto salvato in sequenza dal menu Preferiti. 
- **Configurazione (`cm_ConfigFavoriteTabs`)**: 
- Apri **Preferenze** → **Schede preferite** per riordinare i set, rinominare gli spazi di lavoro, modificare manualmente i percorsi delle singole schede o eliminare i set obsoleti. 

---

## 5. Hotlist delle directory (segnalibri)

La **Hotlist delle directory** fornisce accesso globale e istantaneo alle cartelle utilizzate più frequentemente su unità locali, dischi esterni e supporti di rete remoti. 

![Directory Hotlist](images/quick_access_paths.png) 
*Popup della hotlist delle directory con ricerca fuzzy in tempo reale*

### Popup hotlist istantaneo (`Ctrl+D` / `⌃D` / `cm_DirHotList`)

Premendo `Ctrl+D` viene richiamata una finestra di ricerca leggera e mobile centrata proprio sotto i tuoi occhi: 

1. **Ricerca fuzzy in tempo reale**: 
- Inizia a digitare immediatamente. La barra di ricerca filtra tutti i nomi dei segnalibri e i percorsi di destinazione in tempo reale. 
- Ad esempio, digitando `down` corrisponderà immediatamente a `Downloads — /Users/username/Downloads`. 
2. **Attraversamento della tastiera**: 
- Utilizzare i tasti freccia `Up` e `Down` per evidenziare il segnalibro desiderato. 
- Premi `Enter` per navigare nel pannello attivo direttamente su quel percorso. 
- Premi `Esc` per chiudere il popup senza modificare la directory. 
3. **Creazione rapida di segnalibri**: 
- Fai clic sul pulsante **Aggiungi directory corrente** (o premi `Alt+A`) all'interno del popup. 
- ATBCmder popola automaticamente il percorso della cartella corrente e suggerisce un nome visualizzato pulito.

### Configurazione hotlist (`Ctrl+Shift+D` / `⌃⇧D` / `cm_ConfigDirHotList`)

Apri **Preferenze** → **Hotlist directory** (o attiva `cm_ConfigDirHotList`) per organizzare i tuoi segnalibri: 

- **Sottomenu gerarchici**: raggruppa i segnalibri correlati in categorie (ad esempio `Work`, `Personal`, `Cloud Storage`, `Network Shares`). 
- **Etichette visualizzate personalizzate**: assegna nomi descrittivi come `Work Documents` invece di percorsi lunghi come `/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Work`. 
- **Riordino tramite trascinamento**: riorganizza l'ordine dei segnalibri per mantenere le directory con la massima priorità in cima all'elenco. 

---

## 6. Cronologia e unità: navigazione nel tempo e nei volumi di archiviazione

ATBCmder mantiene una traccia di controllo completa delle tue sessioni di navigazione, permettendoti di ripercorrere i tuoi passi attraverso l'archiviazione locale e i volumi montati.

### Cronologia della navigazione

Ogni pannello registra il proprio stack cronologico del percorso cronologico: 

- **Indietro (`Cmd+[` / `⌘[` o `Alt+Left` / `cm_ViewHistoryPrev`)**: torna indietro di un passo nella cronologia dei percorsi del pannello attivo. 
- **Avanti (`Cmd+]` / `⌘]` o `Alt+Right` / `cm_ViewHistoryNext`)**: Va avanti di un passo dopo essere tornati indietro. 
- **Popup cronologia directory (`Alt+F8` / `⌥F8` o `Ctrl+Down` / `⌃↓` / `cm_DirHistory`)**: 
- Visualizza un menu popup scorrevole che mostra le ultime 20+ directory visitate nel pannello attivo. 
- Fare clic o premere la freccia verso il basso su qualsiasi directory precedente per passare direttamente ad essa, saltando le ripetitive pressioni Indietro.

### Selettore unità e volume

Su macOS, tutte le partizioni interne, le unità USB-C/Thunderbolt esterne, i DMG montati e le condivisioni di rete risiedono in `/Volumes`. ATBCmder fornisce comandi dedicati per passare tra questi target: 

![Drive and Volume Switcher Menu](images/driver_select.png) 
*Unità montata istantaneamente e selettore del volume attivati tramite Alt+F1 (pannello sinistro), Alt+F2 (pannello destro) o Alt+D* 

- **Selettore unità pannello sinistro (`Alt+F1` / `⌥F1` / `cm_LeftOpenDrives`)**: collegamento principale del Classic Commander che apre il menu di selezione dell'unità e del volume destinato al pannello sinistro. 
- **Selettore unità pannello destro (`Alt+F2` / `⌥F2` / `cm_RightOpenDrives`)**: collegamento principale del Classic Commander che apre il menu di selezione dell'unità e del volume destinato al pannello destro. 
- **Menu Unità pannello attivo (`Alt+D` / `⌥D` / `cm_Drives`)**: apre un menu popup che elenca tutti i volumi montati, il file system root `/`, la home utente `~` e gli endpoint di rete connessi per l'utente attualmente selezionato pannello. 

> [!NOTE] 
> **Autorizzazioni unità esterne macOS**: quando si naviga su unità esterne in `/Volumes` per la prima volta, macOS App Sandbox potrebbe richiedere l'autorizzazione. ATBCmder visualizzerà una finestra di dialogo di autorizzazione per creare un segnalibro persistente con ambito di sicurezza per quell'unità. 

---

## 7. Modalità di visualizzazione del pannello: personalizzazione del display

ATBCmder dispone di 5 modalità di visualizzazione specializzate progettate per ottimizzare lo spazio sullo schermo e la densità delle informazioni per diversi flussi di lavoro di gestione dei file.

### 1. Visualizzazione completa delle colonne (`Ctrl+F2` / `⌃F2` / `cm_ColumnsView`)

La modalità di visualizzazione standard e più completa. Visualizza i file in un ricco formato tabellare con intestazioni configurabili: 

| Colonna | Descrizione | Allineamento | 
| :--- | :--- | :--- | 
| **Nome** | Nome del file o della directory con l'icona del tipo macOS nativo. | Sinistra | 
| **Est** | Estensione del file (ad esempio, `py`, `png`, `zip`). | Sinistra | 
| **Taglia** | Dimensione formattata (B, KB, MB, GB). Le cartelle mostrano `<DIR>`. | Giusto | 
| **Data di modifica** | Timestamp formattato in base alle impostazioni locali di macOS. | Sinistra | 
| **Attributi** | Autorizzazioni UNIX (ottale `0755` e simbolico `rwxr-xr-x`). | Centro | 
| **Proprietario/Gruppo** | Nomi di proprietà di utenti e gruppi UNIX. | Sinistra | 

- **Ordinamento delle intestazioni**: fai clic su qualsiasi intestazione di colonna per alternare l'ordinamento ascendente o discendente. Fare clic tenendo premuto `Cmd` per eseguire l'ordinamento secondario.

### 2. Visualizzazione breve (`Ctrl+F1` / `⌃F1` / `cm_BriefView`)

Brief View rimuove le colonne di metadati, organizzando i file in più colonne verticali compatte che riempiono l'intera larghezza del pannello. 

- **Navigazione ad alta densità**: visualizza contemporaneamente da 3 a 5 volte più elementi sullo schermo. 
- **Ideale per**: scansione rapida di elenchi di directory di grandi dimensioni (come caratteri, dump di foto o archivi di registri) in cui è necessario identificare solo i nomi dei file.

### 3. Visualizzazione miniature (`Ctrl+Shift+F1` / `⌃⇧F1` / `cm_ThumbnailsView`)

La visualizzazione miniature converte l'elenco dei file in una griglia di immagini e icone multimediali. 

![Thumbnails View](images/thumbnails_grid_view.png) 
*Visualizzazione miniature che mostra le anteprime multimediali nel pannello attivo* 

- **Media supportati**: anteprime istantanee di foto (JPEG, PNG, HEIC, TIFF, WebP, GIF), formati vettoriali (SVG), documenti PDF e miniature video (MP4, MOV, MKV). 
- **Generazione asincrona dello sfondo**: il rendering delle miniature avviene nei thread in background senza bloccare l'interazione dell'utente. 
- **Dimensione regolabile**: configura le dimensioni delle icone delle miniature (da 64px fino a 256px) in **Preferenze** → **Visualizzazioni file**.

### 4. Visualizzazione ad albero (`cm_TreeView`, `cm_TreeViewSplit`, `cm_TreeViewBoth`)

La visualizzazione ad albero mostra un albero di directory gerarchico espandibile, facilitando la comprensione immediata delle strutture delle cartelle. 

![Tree View and Thumbnails View](images/treeview+thumbview.png) 
*Visualizzazione ad albero integrata insieme a elenchi di file e miniature* 

ATBCmder supporta tre distinti layout di visualizzazione ad albero tramite il menu **Mostra**: 

- **Vista ad albero (Sostituisci) (`cm_TreeView`)**: la tabella dei file del pannello attivo viene sostituita interamente con un albero di directory espandibile. 
- **Vista ad albero (divisa) (`cm_TreeViewSplit`)**: il pannello attivo è diviso verticalmente in due sottoriquadri: un albero di directory a sinistra e l'elenco dei file standard per la cartella dell'albero selezionata a destra. 
- **Visualizzazione ad albero (entrambi i pannelli) (`cm_TreeViewBoth`)**: abilita l'albero delle directory diviso contemporaneamente nei pannelli sinistro e destro. 
- **Mostra file attiva/disattiva**: fai clic con il pulsante destro del mouse all'interno della visualizzazione ad albero e attiva **Mostra file** per scegliere se i file devono essere visualizzati nell'albero accanto alle directory o nascosti per visualizzare solo le directory.

### 5. Vista ramo/piatta (`Cmd+B` / `⌘B` o `Ctrl+B` / `⌃B` / `cm_FlatView`)

Flat View (noto anche come Branch View) è una delle funzionalità più potenti di ATBCmder. Attraversa ricorsivamente tutte le sottodirectory e sottocartelle all'interno della cartella corrente, unendo tutti i file nidificati in un **singolo elenco unificato**. 

![Branch View](images/branch_view.png) 
*Vista ramo piatto (`Cmd+B`) che mostra i contenuti nidificati in tutte le sottodirectory* 

- **La colonna del percorso**: nella vista piatta, ATBCmder aggiunge automaticamente una colonna **Percorso** che mostra il percorso relativo della cartella nidificata di ciascun file (ad esempio, `assets/icons/` o `src/core/`). 
- **Ordinamento globale**: ordina tutti i file nidificati contemporaneamente nell'intero albero del progetto per dimensione, data di modifica o estensione del file. 
- **Elaborazione batch**: seleziona file provenienti da una dozzina di sottodirectory diverse e copiali, spostali, confrontali o rinominali tutti in una volta. 
- **Streaming trasversale**: ATBCmder trasmette i risultati della ricerca nella vista in modo incrementale utilizzando i lavoratori in background, garantendo che progetti di grandi dimensioni (con decine di migliaia di file nidificati) vengano caricati senza problemi senza bloccare l'interfaccia utente. 
- **Uscita rapida**: premi nuovamente `Cmd+B` (`Ctrl+B`) per uscire dalla visualizzazione piatta e tornare alla normale visualizzazione gerarchica della directory. 

---

## 8. ⚡ Suggerimenti degli esperti e approfondimento: controllo di precisione

Per gli utenti avanzati e i tastieristi esperti, ATBCmder offre meccanismi di accordatura a grana fine e di ricerca rapida.

### Overlay di ricerca rapida nel pannello (`Ctrl+S` / `⌃S` / `cm_QuickSearch`)

La ricerca rapida ti consente di passare direttamente a qualsiasi file digitandone il nome senza aprire una finestra di dialogo di ricerca completa. 

```
┌─────────────────────────────────────────────────────────────────┐
│  main.py            py      8.4 KB    Today, 15:10   -rw-r--r-- │
│  main_window.py     py     72.1 KB    Today, 15:18   -rw-r--r-- │
├─────────────────────────────────────────────────────────────────┤
│ 🔍 Quick Search: main_                 [ Next: ↓ ] [ Prev: ↑ ]  │
└─────────────────────────────────────────────────────────────────┘
```
 

1. **Ricerca incrementale**: 
- Premi `Ctrl+S` (o inizia semplicemente a digitare se configurato nelle Preferenze). 
- Una barra in sovrapposizione appare ancorata nella parte inferiore del pannello attivo. 
- Mentre digiti i caratteri, il cursore del pannello salta in tempo reale alla prima voce corrispondente. 
2. **Partite ciclistiche**: 
- Premere `Down Arrow` (`↓`) per passare al file corrispondente successivo. 
- Premi `Up Arrow` (`↑`) per passare alla partita precedente. 
- Premi `Enter` per aprire o eseguire l'elemento abbinato. 
- Premi `Esc` per chiudere la barra di ricerca mantenendo il cursore sul file trovato. 
3. **Il trucco del punto finale**: 
- Digita un punto finale (ad esempio, `config.`) per corrispondere specificamente alla fine del nome di un file, distinguendo `config.xml` da `configuration_guide.md`. 
4. **Ricerca rapida, filtro e filtro semantico**: 
- **Ricerca rapida (`Ctrl+S` / `cm_QuickSearch`)**: sposta il cursore tra le corrispondenze mantenendo tutti i file visibili. 
- **Filtro rapido (`cm_QuickFilter`)**: nasconde temporaneamente tutti i file non corrispondenti, visualizzando solo le righe corrispondenti nella tabella. 
- **Filtro semantico (`Ctrl+F` / `cm_SemanticFilter`)**: utilizza query in linguaggio naturale (ad esempio, `/larger than 10MB`, `//today modified pdf`) tramite macOS Spotlight.

### Modalità di colonna con adattamento automatico

Stanco del ridimensionamento manuale delle colonne o dei nomi file troncati? ATBCmder dispone di un motore di dimensionamento intelligente delle colonne configurato in **Preferenze** → **Visualizzazioni file**: 

1. **Larghezza massima del testo (`mode="max"`)**: 
- Esegue la scansione di tutti i nomi di file visibili e allunga la colonna Nome in modo che il nome di file visibile più lungo sia completamente leggibile senza puntini di sospensione (`...`). 
2. **Larghezza media del testo (`mode="average"`, predefinita)**: 
- Valuta la larghezza media statistica dei caratteri tra i file moltiplicata per un fattore di riempimento configurabile (`auto_fit_padding`, predefinito `1.0`) più i margini delle icone. 
- **Vantaggio**: impedisce a un singolo nome file anomalo di 150 caratteri di spingere tutte le colonne secondarie (dimensione, data, permessi) fuori dal bordo dello schermo. 
3. **Larghezze fisse (`mode="fixed"`)**: 
- Mantiene le dimensioni esatte dei pixel della colonna. 
- Attivato automaticamente ogni volta che trascini manualmente un separatore di colonna nell'intestazione della tabella, rispettando le modifiche manuali del layout.

### Modalità a doppio pannello orizzontale (`Ctrl+Shift+H` / `⌃⇧H` / `cm_HorizontalFilePanels`)

Per impostazione predefinita, ATBCmder posiziona i due pannelli dei file uno accanto all'altro (divisione verticale). Sui monitor ultra-wide o sui display verticali, puoi passare ai pannelli orizzontali impilati: 

![Horizontal Dual Panels Mode](images/horizontal_panels_view.png) 
*Orientamento orizzontale dei pannelli impilati con pannelli superiore e inferiore* 

- Seleziona tramite Menu **Mostra** → **Modalità pannelli orizzontali** o premi `Ctrl+Shift+H` (`cm_HorizontalFilePanels`). 
- Il paradigma Attivo/Inattivo rimane identico: le operazioni scorrono senza intoppi tra i pannelli Superiore (Sorgente) e Basso (Destinazione).

### Persistenza delle impostazioni di visualizzazione per scheda

Nella maggior parte dei file manager, la modifica della colonna di ordinamento o il passaggio dalle colonne dettagliate alle miniature forzano la modifica globale dell'intera finestra. 

ATBCmder isola e ricorda le preferenze di visualizzazione a livello di **scheda** individuale (`TabState`), automaticamente persistenti durante i riavvii tramite `SessionManager` (`atbcmder_session.xml`): 

- **Modalità di visualizzazione indipendenti**: puoi mantenere la Scheda 1 nella **Visualizzazione colonne complete** per le revisioni del codice, la Scheda 2 nella **Visualizzazione griglia miniature** per le risorse grafiche e la Scheda 3 nella **Visualizzazione breve** per una rapida scrematura. 
- **Ordinamento indipendente**: ciascuna scheda ricorda la propria colonna di ordinamento (Nome, Estensione, Dimensione, Data o Autorizzazioni) e la direzione di ordinamento (ascendente o discendente). Il passaggio da una scheda all'altra non reimposta mai le priorità di ordinamento. 
- **Stati flat e albero indipendenti**: una scheda impostata su **Vista ramo piatto** (`Cmd+B` / `cm_FlatView`) o **Modalità visualizzazione albero** mantiene l'appiattimento ricorsivo della directory senza alterare lo stato di visualizzazione di qualsiasi altra scheda in entrambi i pannelli. 

---

## 9. Ricette pratiche passo dopo passo

Ecco tre ricette del mondo reale che mostrano come la navigazione, le schede e le hotlist si combinano per semplificare le attività quotidiane.

### Soluzione 1: creazione di un'area di lavoro di sviluppo persistente

**Obiettivo**: configurare un'area di lavoro a doppio pannello per lo sviluppo full-stack che può essere ripristinata con un clic in qualsiasi momento. 

1. **Configura pannello sinistro (codice sorgente)**: 
- Vai a `~/Projects/MyApp/src`. 
- Apri una seconda scheda (`Cmd+T`) e vai a `~/Projects/MyApp/tests`. 
- Fai clic con il pulsante destro del mouse sulla scheda `src` e seleziona **Blocca scheda** (`cmd_SetTabOptionLock`). 
2. **Configura pannello destro (build e registri)**: 
- Fare clic sul pannello di destra per focalizzarlo (`Tab`). 
- Vai a `~/Projects/MyApp/dist`. 
- Apri una seconda scheda (`Cmd+T`) e vai a `/var/log`. 
3. **Salva area di lavoro preferita**: 
- Scegli il menu **Preferiti** → **Salva le schede correnti in una nuova scheda preferita** (`cm_SaveFavoriteTabs`). 
- Inserisci `MyApp FullStack` e premi `Enter`. 
4. **Ripristino istantaneo**: 
- Ogni volta che lavori su questo progetto, seleziona semplicemente **Preferiti** → **Carica schede dalle schede preferite** (`cm_LoadFavoriteTabs`) e scegli `MyApp FullStack`. Entrambi i pannelli configureranno immediatamente tutte e quattro le schede con i percorsi esatti e le impostazioni di blocco. 

---

### Soluzione 2: appiattimento degli alberi di directory profondi per trovare risorse gonfiate

**Obiettivo**: trovare e ripulire dispositivi di test di grandi dimensioni e dump di log sparsi in dozzine di sottocartelle nidificate. 

1. Passare alla parte superiore del progetto o della directory multimediale nel pannello attivo. 
2. Premere `Cmd+B` (`⌘B`) o `Ctrl+B` (`cm_FlatView`) per attivare la **Vista ramo piatto**. 
3. Osserva come tutte le sottodirectory vengono appiattite ricorsivamente in un unico elenco nel pannello. 
4. Fare clic una o due volte sull'intestazione della colonna **Dimensione** per ordinare tutti i file dal più grande al più piccolo. 
5. I file più grandi nell'intero albero delle directory vengono visualizzati immediatamente nella parte superiore del pannello, con la colonna **Percorso** che mostra le loro esatte posizioni nidificate. 
6. Ispeziona o elimina direttamente i file gonfiati. 
7. Premere di nuovo `Cmd+B` per disattivare la visualizzazione piatta e tornare alla navigazione delle cartelle standard. 

---

### Soluzione 3: creazione di segnalibri rapidissima su volumi interni e di rete

**Obiettivo**: aggiungere ai segnalibri una cartella di backup NAS remota e accedervi in ​​meno di due secondi. 

1. Passare all'unità di rete montata (ad esempio, `/Volumes/BackupShare/Archives`). 
2. Premere `Ctrl+D` (`⌃D`) per richiamare il popup **Directory Hotlist**. 
3. Fare clic sul pulsante **Aggiungi directory corrente** (`btn_add` / `cm_AddDirToHotlist`). 
4. Immettere un nome descrittivo come `NAS Archives`. 
5. Domani, quando ti troverai in qualsiasi punto del tuo filesystem locale, premi semplicemente `Ctrl+D`, digita `nas` e premi `Enter`. ATBCmder ti trasporta istantaneamente attraverso la rete in quella cartella esatta. 

---

## 10. Avvisi di sicurezza e di sistema

> [!NOTE] 
> **Archiviazione esterna e condivisioni di rete**: 
> Quando si accede a unità USB esterne o condivisioni di rete (`/Volumes/...`) all'interno di schede o segnalibri, assicurarsi che il volume sia attualmente montato. Se un'unità viene smontata all'avvio di ATBCmder, le schede che puntano ad essa visualizzeranno in modo sicuro un avviso "Posizione non disponibile" anziché arrestarsi in modo anomalo o rimuovere la scheda. 

> [!TIP] 
> **Mirroring delle schede sui pannelli**: 
> Vuoi che il pannello di destra rispecchi immediatamente tutte le schede aperte del pannello di sinistra? Utilizza il menu **Schede** → **Copia tutte le schede nel pannello opposto** (`cm_CopyAllTabsToOpposite`) per replicare il layout delle schede su entrambi i lati. 

> [!WARNING] 
> **Attenzione con le operazioni in visualizzazione piatta (`Cmd+B`)**: 
> Nella vista Ramo semplice, i file provenienti da più rami di directory distinti vengono visualizzati fianco a fianco in un unico elenco. Fai attenzione quando usi `Cmd+A` (Seleziona tutto) seguito da `F8` (Elimina) o `F6` (Sposta), poiché l'azione verrà applicata in modo ricorsivo a tutte le sottodirectory nidificate. 

---

## 11. Tabella di riferimento della tastiera a doppia matrice

| Categoria | Azione | Scorciatoia macOS | Chiave classica | ID comando interno | 
| :--- | :--- | :--- | :--- | :--- | 
| **Navigazione nelle directory** | Directory principale | `Backspace` / `⌘↑` | `Ctrl+PgUp` | `cm_ChangeDirToParent` | 
| | Directory principale | `Ctrl+\` / `⌃\` | `\` | `cm_ChangeDirToRoot` | 
| | Directory principale | `Ctrl+Shift+Home` / `⌃⇧Home` | `Alt+Home` | `cm_ChangeDirToHome` | 
| | Prima voce | `Home` | `Home` | `cm_GoToFirst` | 
| | Ultima voce | `End` | `End` | `cm_GoToLast` | 
| **Schede cartella** | Nuova scheda | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | 
| | Chiudi scheda | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | 
| | Chiudi le schede duplicate | *Menu contestuale scheda* | — | `cm_CloseDuplicateTabs` | 
| | Chiudi tutte le schede | *Menu Schede* | — | `cm_CloseAllTabs` | 
| | Rinomina scheda | *Menu contestuale scheda* | — | `cm_RenameTab` | 
| | Copia le schede nella parte opposta | *Menu Schede* | — | `cm_CopyAllTabsToOpposite` | 
| | Scheda successiva | `Ctrl+Tab` / `⌃⇥` | `Ctrl+Tab` | `cm_NextTab` | 
| | Scheda precedente | `Ctrl+Shift+Tab` / `⌃⇧⇥` | `Ctrl+Shift+Tab` | `cm_PrevTab` | 
| | Mostra elenco schede | `Ctrl+Shift+L` / `⌃⇧L` | `Ctrl+Shift+L` | `cm_ShowTabsList` | 
| **Schede preferite** | Salva schede preferite | *Menù Preferiti* | — | `cm_SaveFavoriteTabs` | 
| | Carica schede preferite | *Menù Preferiti* | — | `cm_LoadFavoriteTabs` | 
| | Salva nuovamente il preferito attivo | *Menù Preferiti* | — | `cm_ResaveFavoriteTabs` | 
| | Ricarica preferito attivo | *Menù Preferiti* | — | `cm_ReloadFavoriteTabs` | 
| | Configura le schede preferite| *Preferenze* | — | `cm_ConfigFavoriteTabs` | 
| **Hotlist e cronologia** | Lista calda della directory | `Ctrl+D` / `⌃D` | `Ctrl+D` | `cm_DirHotList` | 
| | Configura hotlist | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| | Aggiungi Dir alla Hotlist | *Popup della lista preferita* | — | `cm_AddDirToHotlist` | 
| | Storia all'indietro | `Cmd+[` / `⌘[` | `Alt+Left` | `cm_ViewHistoryPrev` | 
| | Storia avanti | `Cmd+]` / `⌘]` | `Alt+Right` | `cm_ViewHistoryNext` | 
| | Elenco a discesa della cronologia | `Alt+F8` / `⌥F8` | `Ctrl+Down` | `cm_DirHistory` | 
| **Unità e volumi** | Unità del pannello sinistro | `Alt+F1` / `⌥F1` | `Alt+F1` | `cm_LeftOpenDrives` | 
| | Unità del pannello destro | `Alt+F2` / `⌥F2` | `Alt+F2` | `cm_RightOpenDrives` | 
| | Menu unità pannello attivo | `Alt+D` / `⌥D` | `Alt+D` | `cm_Drives` | 
| **Modalità di visualizzazione** | Visualizzazione colonne complete | `Ctrl+F2` / `⌃F2` | `Ctrl+F2` | `cm_ColumnsView` | 
| | Vista breve | `Ctrl+F1` / `⌃F1` | `Ctrl+F1` | `cm_BriefView` | 
| | Visualizzazione miniature | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| | Visualizzazione ad albero (Sostituisci) | *Mostra Menù* | `Ctrl+Shift+F8` | `cm_TreeView` | 
| | Visualizzazione ad albero (divisa) | *Mostra Menù* | — | `cm_TreeViewSplit` | 
| | Visualizzazione ad albero (entrambi i pannelli)| *Mostra Menù* | — | `cm_TreeViewBoth` | 
| | Vista ramo piatto | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | 
| | Modalità Pannelli Orizzontali | `Ctrl+Shift+H` / `⌃⇧H` | `Ctrl+Shift+H` | `cm_HorizontalFilePanels` | 
| **Ricerca e filtri** | Sovrapposizione di ricerca rapida | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_QuickSearch` | 
| | Filtro semantico | `Ctrl+F` / `⌃F` | `Ctrl+F` | `cm_SemanticFilter` |

--- 

<div align="center"> 
<p>Ora che hai imparato la navigazione nelle directory, le schede e le visualizzazioni dei pannelli:</p> 
<p><strong><a href="file_operations.md">Procedi al capitolo 3: Operazioni giornaliere sui file e coda &rarr;</a></strong></p> 
</div>