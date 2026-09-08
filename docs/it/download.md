# Capitolo 10: Download e installazione

Grazie per il tuo interesse per ATBCmder! Forniamo due diversi metodi di download e installazione per soddisfare le tue esigenze. 

> [!IMPORTANT] 
> **Requisiti di sistema e architettura** 
> 
> - **Sistema operativo**: macOS 12.0 (Monterey) o successivo (inclusi macOS 13 Ventura, macOS 14 Sonoma e macOS 15 Sequoia). 
> - **Architettura hardware supportata**: **Apple Silicon (M1 / M2 / M3 / M4, ARM64)**. 
> - **Compatibilità Intel (x86_64)**: i Mac basati su Intel **non sono supportati** al momento.

## 1. Mac App Store (consigliato)

Questo è il modo consigliato per installare ATBCmder. **ATBCmder è ora ufficialmente disponibile sul Mac App Store!** Il download tramite il Mac App Store ufficiale ti garantisce aggiornamenti automatici senza interruzioni, protezione sandbox nativa di macOS e la migliore integrazione di sistema. 

- **Mac App Store**: [Scarica ATBCmder dal Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. Scarica il programma di installazione DMG

Se non riesci ad accedere al Mac App Store o preferisci i download diretti, forniamo un pacchetto di installazione DMG autonomo creato nativamente per Apple Silicon (ARM64). 

- **Link per il download di DMG**: [Fai clic qui per scaricare ATBCmder DMG](https://storage.aitobox.com/@s/bNAshV6G/ATBCmder) *(Solo Apple Silicon/ARM64)* 

*Nota: durante l'installazione tramite DMG, le funzionalità di sicurezza di macOS potrebbero richiedere di consentire esplicitamente l'applicazione in "Impostazioni di sistema > Privacy e sicurezza" la prima volta che la apri. I Mac Intel (x86_64) non sono supportati.*

### ⚠️ Concedi l'accesso completo al disco

ATBCmder è uno strumento di gestione dei file e richiede autorizzazioni esplicite di gestione del disco da parte dell'utente. Si prega di seguire questi passaggi: 

1. Fai clic sull'icona Apple nell'angolo in alto a sinistra dello schermo e seleziona **Impostazioni di sistema** (o "Preferenze di Sistema" nelle versioni macOS precedenti). 
2. Vai a **Privacy e sicurezza** nel menu di sinistra o di destra. 
3. Scorri verso il basso e seleziona **Accesso completo al disco**. 
4. Trova l'applicazione (**ATBCmder**) nell'elenco e attiva l'interruttore per accenderla. Se l'applicazione non è nell'elenco, fare clic sul pulsante **++** in basso per aggiungerla manualmente. 
5. Il sistema ti chiederà di inserire la password di accesso del tuo Mac o di utilizzare Touch ID per confermare le modifiche.

## Note sulla versione

### 1.7.0 (06-09-2026)

- Universal File Viewer e Office Preview Suite: aggiunti motori di anteprima nativi per fogli di calcolo Excel (con caricamento virtuale lento), documenti Word (con impaginazione e rendering di immagini incorporato) e presentazioni PowerPoint (visualizzazione scheda diapositiva); aggiunte anteprime per database SQLite, Markdown (con sommario), Jupyter Notebooks, caratteri, archivi, audio ed EML; implementato lo streaming infinito con streaming istantaneo per file di testo di grandi dimensioni 
- Visualizzatore di differenze di file affiancati: strumento di confronto bidirezionale integrato in stile vimdiff con evidenziazione delle differenze a livello di carattere, copia di blocchi, modifica dal vivo, annulla/ripeti e conservazione della codifica 
- Motore di ricerca file avanzato: sottosistema di ricerca riscritto con corrispondenza di sottostringhe fuzzy predefinita, supporto regex e modalità scheda "Feed to Listbox"; la limitazione dell'interfaccia utente in batch elimina i blocchi dell'interfaccia utente sui risultati di ricerca di grandi dimensioni 
- Operazioni sui file e rafforzamento dell'interfaccia utente: risolti i prompt di sovrascrittura duplicati durante gli spostamenti tra dispositivi e i blocchi della coda di trasferimento; aggiunti i timestamp di creazione dei file nella finestra di dialogo delle proprietà; barra degli strumenti centrale verticale abilitata per impostazione predefinita e indicatori visivi del riquadro attivo perfezionati

### 1.6.2 (03-09-2026)

- Selezione e interazione con trascinamento dell'elastico: aggiunta la selezione del trascinamento dell'elastico del mouse sia nella visualizzazione tabella file che nella visualizzazione miniature, oltre alla possibilità di fare clic su uno spazio vuoto per deselezionare tutto 
- Tasto di scelta rapida globale della finestra e input di scelta rapida: aggiunto un tasto di scelta rapida globale configurabile per mostrare/nascondere la finestra dell'applicazione; Risolto il problema relativo all'inserimento delle combinazioni di modificatori a 4 tasti nelle impostazioni dei tasti di scelta rapida 
- Correzione del ripristino del Dock e del vassoio di macOS: risolto un problema per cui facendo clic sull'icona del Dock mentre era ridotta a icona nel vassoio non si riusciva a ripristinare la finestra principale o a mostrare un fotogramma vuoto 
- Miglioramenti del rafforzamento del core e della stabilità: risolti potenziali segfault del ciclo di vita, backend VFS rafforzati e smontaggio dei thread stabilizzato e suite di test

### 1.6.1 (27-08-2026)

- Revisione completa dell'interfaccia utente/UX di macOS: basata su Apple HIG con tavolozze Chiaro/Scuro perfezionate, contrasto evidenziato nel riquadro in stile Finder, descrizioni comandi native delle schede e animazioni di controllo segmentate fluide 
- Motore icone vettoriali e widget moderni: aggiunto un generatore di icone vettoriali indipendente dalla risoluzione ispirato ai simboli SF e barre di guida, breadcrumb e caselle combinate modernizzate 
- Interazione e layout polacco: ridenominazione multipla riprogettata con un layout a 2 colonne e rilevamento delle collisioni dei nomi in tempo reale; La visualizzazione miniature supporta lo zoom dinamico `Cmd + Wheel`; aggiunte visualizzazioni unificate dello stato vuoto

### 1.6.0 (27-08-2026)

- Pipeline a doppia distribuzione: stabiliti flussi di lavoro di compilazione automatizzati separati su misura per la distribuzione DMG autonoma e il rilascio del Mac App Store (MAS) 
- Conformità alle policy dell'App Store: regola dinamicamente i menu dell'interfaccia utente nelle build MAS rimuovendo gli elementi di controllo degli aggiornamenti esterni per soddisfare rigorosamente le linee guida per la revisione di Apple, preservando i controlli manuali degli aggiornamenti nelle build DMG 
- `itms-services` Binary Patcher: aggiunto uno scanner binario automatizzato e un patcher sicuro per eliminare le stringhe di protocollo private negli artefatti PySide6/Qt compilati, garantendo una convalida automatizzata impeccabile di App Store Connect

### 1.5.6 (22-08-2026)

- Modalità di visualizzazione indipendenti per scheda: ogni scheda ora mantiene il proprio layout di visualizzazione indipendente (visualizzazione piatta/modalità albero), sincronizzando automaticamente lo stato del menu e persistendo senza interruzioni tra i ripristini della sessione 
- Apertura intelligente dei file e fallback del sistema: aggiunto un rilevatore di tipi di file multilivello (byte magici/MIME/estensione) per aprire supporti e documenti supportati nel visualizzatore/editor integrato tornando in modo pulito alle app predefinite del sistema operativo per i file non supportati

### 1.5.5 (21-08-2026)

- Ottimizzazione della politica di controllo degli aggiornamenti: controlli automatici degli aggiornamenti disabilitati all'avvio dell'applicazione per impostazione predefinita; gli aggiornamenti ora possono essere controllati manualmente tramite `Help` -> `Check for Updates...`, migliorando la velocità di avvio e la privacy offline

### 1.5.4 (21-08-2026)

- Messa a fuoco del pannello e lucidatura della selezione: risolti i contorni del focus persistenti sui pannelli divisi inattivi quando si cambia riquadro; logica di ripristino della selezione migliorata dopo lo spostamento dei file tra i pannelli per evitare operazioni accidentali

### 1.5.3 (19-08-2026)

- Lucidatura del sottomenu a cascata breadcrumb: allineata con precisione la posizione verticale dei menu delle sottocartelle a cascata con la riga evidenziata, eliminando i salti di layout e uniformando l'attraversamento profondo delle cartelle

### 1.5.2 (19-08-2026)

- Correzione delle note di avvio e di rilascio: risolto un problema per cui la finestra di dialogo delle note di rilascio appariva ripetutamente a ogni avvio dell'app; gestione fallback predefinita `Config.get` migliorata per garantire che le note di rilascio vengano richieste solo al lancio iniziale o agli aggiornamenti di versione

### 1.5.1 (19-08-2026)

- Note di rilascio multilingue: aggiunte 7 nuove note di rilascio nelle lingue principali (zh_TW, ja, ko, de, fr, ru, es) con rilevamento dinamico e fallback gerarchico a 5 livelli 
- MacOS Code Signing & Build Polish: script di packaging refactoring con targeting binario Mach-O e wrapper di tentativi con timestamp, eliminando errori di firma e limitazioni

### 1.5.0 (17-08-2026)

- Global Session Manager: implementata la persistenza della sessione a livello di applicazione che ripristina perfettamente tutte le schede, i percorsi, le modalità di visualizzazione (piatta/ad albero) del pannello sinistro/destro, i rapporti del pannello e i limiti delle finestre multi-monitor al riavvio 
- Importazione/esportazione delle impostazioni: aggiunta l'esportazione e l'importazione ZIP con 1 clic per tutte le configurazioni e i dati delle applicazioni, semplificando la migrazione tra dispositivi 
- Miglioramenti all'editor di immagini: aggiunto il ridimensionamento personalizzato delle immagini con blocco delle proporzioni e risoluzioni preimpostate rapide

### 1.4.9 (17-08-2026)

- Editor di immagini avanzato: aggiunto il ritaglio delle immagini, la rotazione fine, la regolazione dei filtri e un modulo per la rimozione e l'inserimento della filigrana AI basato su OpenCV 
- Visualizzatore di immagini migliorato: supporto completo per GIF animate, zoom, panoramica, rotazione, estrazione di metadati EXIF e modalità presentazione 
- Integrazione della ricerca Spotlight: Spotlight nativo di macOS profondamente integrato per la ricerca istantanea di file e una migliore navigazione nel focus dei risultati di ricerca

### 1.4.8 (16-08-2026)

- Localizzazione completa (i18n): controllo completo e completamento della traduzione nell'interfaccia utente, nel visualizzatore F3 e nell'editor F4, migliorando significativamente la localizzazione dei lettori multimediali e dei componenti di anteprima 
- Ottimizzazioni del visualizzatore F3: gestione migliorata dei collegamenti esterni e logica di ricerca wrap-around nel lettore EPUB fallback (SimpleEpubPanel); semplificata la barra degli strumenti del visualizzatore PDF rimuovendo i pulsanti di rotazione ridondanti

### 1.4.7 (16-08-2026)

- Miglioramenti del lettore multimediale: UI, UX e stabilità dei lettori audio e video integrati notevolmente migliorati 
- Compila il refactoring del sistema: rinominato il flag env `BUILD_EPUB` in `BUILD_WEBENGINE` per riflettere accuratamente il comportamento del packaging 
- Correzione delle dipendenze del packaging: garantito che `ebooklib` sia sempre incluso in build DMG leggere per il lettore EPUB fallback

### 1.4.6 (16-08-2026)

- Lettore EPUB leggero (SimpleEpubPanel): aggiunto un lettore EPUB fallback senza WebEngine con navigazione e ricerca dei capitoli, oltre a un argomento CLI `--epub-reader` per sovrascrivere il motore predefinito 
- Menu breadcrumb a cascata: refactoring del menu a discesa breadcrumb in un layout scorrevole a colonna singola con infiniti sottomenu a cascata, risolvendo problemi di sovrapposizione e blocco del mouse

### 1.4.5 (15-08-2026)

- Visualizzatore codice avanzato (F3): aggiunta evidenziazione della sintassi (Pygments), coda di file live, ricerca regex e numeri di riga 
- Editor di codice avanzato (F4): aggiunta codifica dinamica/conversione EOL, salvataggio sicuro atomico, rientro intelligente e trova/sostituisci 
- Drag & Drop esterno globale: trascina facilmente i file, inclusi i contenuti di archivio profondamente annidati, direttamente sul desktop macOS o su editor di terze parti (ad esempio VSCode)

### 1.4.4 (15-08-2026)

- Miglioramenti alla tipografia: dimensioni dei caratteri aumentate nei menu, nei pulsanti, nelle descrizioni comandi e nella finestra di dialogo delle impostazioni per una migliore leggibilità 
- Correzioni del ridimensionamento del cursore: ripristinati i cursori di ridimensionamento del mouse mancanti sui bordi delle finestre, sui divisori e sulle intestazioni delle colonne delle tabelle 
- Correzioni dell'interfaccia utente di macOS: risolti gli sfondi neri di selezione nei menu a discesa e risolti gli overflow dei titoli nelle caselle di gruppo

### 1.4.3 (14-08-2026)

- Nuova interfaccia utente nativa di macOS (tema Aqua Blue): introdotto come nuovo tema predefinito, con navigazione breadcrumb interattiva (con drilldown delle sottocartelle a cascata), misuratore di spazio di archiviazione in stile Mac (overflow TB fisso) e selezione di capsule arrotondate 
- Miglioramento dell'interfaccia utente: layout perfezionato del pulsante di chiusura della scheda, corretta sovrapposizione del prompt dei comandi e sfondi della barra degli strumenti, divisori e bordi del pannello unificati in tutti i temi 
- i18n & App Upgrade: completato l'audit di copertura dell'intero progetto i18n; aggiunto il supporto API di condivisione AList/OpenList nel modulo di aggiornamento automatico

### 1.4.2 (13-08-2026)

- Filtro semantico AI migliorato: supporta l'analisi di estensioni più comuni, forme plurali e completamente integrato con i18n 
- UX di ricerca semantica: sostituito il cursore di attesa con QProgressBar e migliorato il comportamento del tasto Invio per i completamenti 
- Core Semantic Parsing: miglioramento del rilevamento del tipo di target e dell'eliminazione delle parole chiave per una ricerca in linguaggio naturale più accurata

### 1.4.1 (13-08-2026)

- Revisione e refactoring completi della base di codice (batch A-D) 
- Miglioramenti della sicurezza: risolto il potenziale attraversamento del percorso e le vulnerabilità di accesso 
- Concorrenza e prestazioni: sicurezza dei thread in background ed efficienza di esecuzione migliorate 
- Architettura: stabilità e gestione delle risorse migliorate nei componenti principali

### 1.4.0 (12-08-2026)

- Correzioni approfondite della rete VFS: supporto multi-codifica, driver di protocollo, montaggio di archivi concatenati e risoluzione dei conflitti 
- Modulo di aggiornamento dell'app migliorato: correzioni per la verifica SSL, convalida del download DMG e integrazione dell'interfaccia utente 
- Interfaccia utente della nota di rilascio: visualizza la cronologia completa delle versioni durante gli aggiornamenti automatici

### 1.3.9 (12-08-2026)

- Aggiunto lettore EPUB integrato (visualizzazione rapida F3) 
- Meccanismo di rilevamento dell'aggiornamento dell'app implementato 
- Risolto il problema del blocco del lavoratore VFS durante la risoluzione dei conflitti di file

### 1.3.8 (08-08-2026)

- Perfezionamento dell'interfaccia utente della visualizzazione ad albero 
- Integrazione di rete fsspec rifattorizzata 
- Migliorata la gestione dei caratteri dei file non validi

### 1.3.7 (06-08-2026)

- Architettura VFS di rete: revisione dei file system di rete (FTP/WebDAV/SMB) utilizzando `fsspec`, implementazione asincrona `VfsTableModel`, streaming `StreamCopyWorker`, operazioni su file remoti (mkdir/rinomina/eliminazione/sovrascrittura) e visualizzazione/modifica remota F3/F4 
- Vassoio di sistema e tasti di scelta rapida: supporto per la riduzione a icona nella barra delle applicazioni, scorciatoia globale (`Option+Cmd+H`), attivazione/disattivazione dell'icona del Dock di macOS e integrazione dell'icona del modello nativo 
- Configurazione LLM: introduzione della risorsa `default_llm.xml` e del singleton per il filtro semantico AI e le opzioni dell'interfaccia utente 
- Miglioramenti alla navigazione: supporto delle scorciatoie di navigazione Pagina su / Pagina giù / Home / Fine / Fn nei pannelli dei file e nei popup delle hotlist 
- Internazionalizzazione: racchiudere tutti i messaggi di errore VFS, le etichette dei pannelli Quick View e le stringhe dei menu della barra delle applicazioni con i cataloghi di traduzione i18n

### 1.3.6 (04-08-2026)

- Miglioramenti VFS di rete: aggiunta del rilevamento automatico UTF-8/GBK, aggiornamento dinamico della codifica makefile, gestione del fallback e reimpostazione del socket per FTP; risolvere il timeout e rispondere alla desincronizzazione 
- Correzioni WebDAV e SMB: corretti l'eliminazione del percorso root WebDAV/SMB, la propagazione dell'ultimo errore, l'affidabilità della connessione, le icone VFS e la visualizzazione dei titoli delle schede 
- Navigazione in miniatura: implementa una navigazione fluida con freccia sulla griglia 2D per la visualizzazione in miniatura 
- i18n e qualità del codice: correggi le traduzioni danneggiate della scheda Chiudi nei cataloghi zh_CN/zh_TW e completa il controllo dell'ottimizzazione della base di codice

### 1.3.5 (03-08-2026)

- Pannello Visualizzazione rapida: implementa la funzionalità Visualizzazione rapida (`cm_QuickView`, `Cmd+Q`/`Ctrl+Q`) che supporta anteprime multiformato, proprietà dei file di fallback, capovolgimento simmetrico, integrazione del menu Mostra e i18n completo 
- Widget di visualizzazione rapida: aggiungi `QuickViewContainer` e `QuickViewPropertiesWidget` integrati in FilePanel 
- Polacco dell'interfaccia utente: corretto l'allineamento dell'intestazione della scheda e i problemi di schiacciamento della pagina di dialogo delle opzioni nel tema chiaro

### 1.3.4 (02-08-2026)

- Interfaccia utente del pannello File: aggiunta della selezione batch Maiusc+Pagina su/Maiusc+Pagina giù nelle visualizzazioni del pannello file 
- Operazioni sui file: corretti i difetti di copia F5 e spostamento di file/directory F6 
- Crea script: imposta nomi esatti di identità del certificato, aggiungi timestamp al codesign e gestisci con garbo lo stato non valido dell'autenticazione

### 1.3.3 (01-08-2026)

- Transfer Engine: calcola la velocità di trasferimento in tempo reale e l'ETA in ProcessTransferWorker 
- Autorizzazioni e Sandbox: controlli sandbox macOS separati dal flusso di rilevamento dell'accesso completo al disco 
- Script di build: aggiorna la configurazione dello script di build per le build firmate DMG 1.3.3

### 1.3.2 (01-08-2026)

- Subprocess Transfer Worker: risolto l'errore di blocco/avvio in modalità bundle autonomo dell'App Store di Nuitka 
- Competenze dell'agente: aggiungi il controllo di verifica della completezza di i18n alla competenza di revisione del codice, ottimizzazione e controllo

### 1.3.1 (01-08-2026)

- Sandbox macOS: corretto il falso stato "Accesso completo al disco concesso" causato dal controllo `os.access` 
- Attività simultanee: risolve il cross-talk di stato per operazioni in background simultanee 
- i18n: aggiunta la traduzione cinese per la casella di controllo batch nella finestra di dialogo di eliminazione permanente 
- Competenze dell'agente: aggiungi e aggiorna la capacità di controllo dell'ottimizzazione della revisione del codice

### 1.3.0 (01-08-2026)

- Motore di trasferimento isolato dal processo: implementa ProcessTransferWorker e ProcessIOEngine per scaricare la copia/spostamento dei file I/O dal thread dell'interfaccia utente 
- Prestazioni di trasferimento e reattività: limitazione della velocità IPC a 10 Hz, buffering adattivo e ottimizzazione `F_NOCACHE` macOS per prevenire lo stuttering della GUI 
- Verifica e rafforzamento del codice: refactoring in 4 fasi inclusi blocchi mutex di concorrenza, rafforzamento della sicurezza e pulizia dell'architettura 
- Correzioni dell'interfaccia utente: correzione dell'errore di eliminazione di Shiboken C++, layout della modalità pannello orizzontale e segnali dell'indicatore di avanzamento delle attività in background

### 1.2.0 (30-07-2026)

- Implementare il pool di processi I/O globale (IoWorkerPool) per isolare il blocco delle operazioni di I/O dei file e impedire il blocco della GUI 
- Controllo delle versioni di configurazione: leggi/scrivi app_version sul nodo root XML e aggiungi il registro del runner di migrazione automatizzato 
- Trascina e rilascia/Appunti: integra il bridge Finder nativo di macOS, cartelle a molla e macchina a stati degli appunti 
- Espansione del percorso: aggiunta dell'utilità `expand_path` condivisa che supporta `~`, `$VAR`, `%VAR%` e `%COMMANDER_PATH%` 
- Hotlist: implementa il singleton HotlistConfig autonomo e la configurazione della hotlist predefinita

### 1.1.0 (29-07-2026)

- Correzione dell'ordine di immissione delle note di rilascio per garantire l'ordinamento cronologico inverso sotto l'intestazione della nota di rilascio 
- Correzione dello script del gestore versione per supportare il nodo XML System/LastVersion in default_config.xml 
- Tasti di scelta rapida: aggiungi scorciatoie predefinite Meta+Tab e Meta+Shift+Tab per la navigazione tra schede 
- Schede preferite: aggiungi la migrazione automatica e la pulizia delle schede preferite legacy dalla configurazione principale 
- Visualizzatore file: ottimizza le prestazioni di caricamento di file di grandi dimensioni e l'utilizzo della memoria

### 1.0.1 (22-07-2026)

> Correzione dell'errore di anteprima del testo F3 negli ambienti sandbox dell'App Store

### 1.0.0 (18-07-2026)

> Implementazione iniziale del port Python di TotalCommander.