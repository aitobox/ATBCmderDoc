# Capitolo 11: Download e installazione

Grazie per il tuo interesse per ATBCmder! Forniamo due diversi metodi di download e installazione per soddisfare le tue esigenze. 

> [!IMPORTANT] 
> **Requisiti di sistema e architettura** 
> 
> - **Sistema operativo**: macOS 12.0 (Monterey) o successivo (inclusi macOS 13 Ventura, macOS 14 Sonoma e macOS 15 Sequoia). 
> - **Architettura hardware supportata**: **Universale (Apple Silicon ARM64 & Intel x86_64)**. Supporto completo per computer Mac basati su Apple Silicon (M1 / M2 / M3 / M4) e Intel.  
> - **Compatibilità Intel (x86_64)**: Pienamente supportata a partire dalla versione 1.8.0 tramite pacchetti binari universali.

## 1. Mac App Store (consigliato)

Questo è il modo consigliato per installare ATBCmder. **ATBCmder è ora ufficialmente disponibile sul Mac App Store!** Il download tramite il Mac App Store ufficiale ti garantisce aggiornamenti automatici senza interruzioni, protezione sandbox nativa di macOS e la migliore integrazione di sistema. 

- **Mac App Store**: [Scarica ATBCmder dal Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. Scarica il programma di installazione DMG

Se non riesci ad accedere al Mac App Store o preferisci il download diretto, forniamo pacchetti di installazione DMG standalone creati nativamente per macOS con supporto a doppia architettura (Universale / ARM64 & Intel x86_64).

- **Link per il download del DMG**: [Fai clic qui per scaricare ATBCmder DMG](https://storage.aitobox.com/@s/atbcenter/ATBCmder) *(Universale: Apple Silicon & Intel x86_64)*

*Nota: durante l'installazione tramite DMG, le funzionalità di sicurezza di macOS potrebbero richiedere di consentire esplicitamente l'applicazione in "Impostazioni di sistema > Privacy e sicurezza" alla prima apertura.*

### ⚠️ Concedi l'accesso completo al disco

ATBCmder è uno strumento di gestione dei file e richiede autorizzazioni esplicite di gestione del disco da parte dell'utente. Si prega di seguire questi passaggi: 

1. Fai clic sull'icona Apple nell'angolo in alto a sinistra dello schermo e seleziona **Impostazioni di sistema** (o "Preferenze di Sistema" nelle versioni macOS precedenti). 
2. Vai a **Privacy e sicurezza** nel menu di sinistra o di destra. 
3. Scorri verso il basso e seleziona **Accesso completo al disco**. 
4. Trova l'applicazione (**ATBCmder**) nell'elenco e attiva l'interruttore per accenderla. Se l'applicazione non è nell'elenco, fare clic sul pulsante **++** in basso per aggiungerla manualmente. 
5. Il sistema ti chiederà di inserire la password di accesso del tuo Mac o di utilizzare Touch ID per confermare le modifiche.

## Note sulla versione

### 2.3.8 (20-10-2026)

- Rinnovamento dell'interazione nei pannelli file e gerarchia visiva: Riprogettati i delegati delle righe per visualizzare una sottile evidenziazione translucida al passaggio del mouse con bordi arrotondati, separando chiaramente lo stato di hover dalla selezione attiva dei file (Fixes #72); eliminati i ritardi nel clic destro assicurando che mantenga le selezioni correnti (Fixes #60); aggiunte le azioni «Nuovo file» (Shift+F4) e «Nuova cartella» (F7) direttamente nel menu contestuale del pannello file con supporto completo a 31 lingue (Fixes #61, #70); ripristino automatico delle selezioni al cambio di cartella per evitare operazioni accidentali tra directory diverse (Fixes #67)
- Esecuzione nel terminale da riga di comando e navigazione fluida dei percorsi: Premendo Invio su qualsiasi comando shell esterno nella riga di comando inferiore viene avviato automaticamente il terminale di sistema predefinito (Terminal.app / iTerm2) ed eseguito nella cartella del pannello corrente (Fixes #63); l'immissione di percorsi di directory o comandi `cd` consente la navigazione diretta con gestione corretta degli spazi e dei caratteri speciali
- Gestione profonda della memoria e buffer circolari per lo stato del sistema: Applicato `WA_DeleteOnClose` e la distruzione deterministica nel Visualizzatore universale (F3), nell'Editor (F4) e in tutte le finestre di dialogo modali per eliminare l'accumulo di memoria nei cicli di vita ripetuti; migrati i dispatcher i18n a `weakref.WeakMethod`, interrotti i cicli di riferimento in `DiskTreeNode` e introdotta una cache LRU per QIcon; aggiornati il Pannello di stato del sistema e AtbSysBridge con buffer circolari fissi a 120 campioni e riutilizzo dei widget sul posto per azzerare il sovraccarico di memoria e fogli di stile durante il polling telemetrico ad alta frequenza
- Correzione della configurazione della barra strumenti e allineamento della guida sandbox: Risolto un problema per cui i pulsanti appena aggiunti nella barra degli strumenti centrale potevano essere sovrascritti e persi al salvataggio delle impostazioni (Fixes #62); sincronizzati gli indicatori della barra di stato per l'Accesso completo al disco (FDA) della sandbox con le azioni del menu Configurazione

### 2.3.7 (16-10-2026)

- Integrità del runtime macOS e rafforzamento dell'uscita dall'applicazione: Corrette le importazioni mancanti di `os`, `sys` e `traceback` nei moduli di piattaforma e logging, eliminando del tutto il rischio di errori `NameError` all'avvio headless o standalone; ottimizzato `MainWindow.closeEvent` rimuovendo disconnessioni di segnali ridondanti per garantire una chiusura pulita dell'applicazione senza errori di segmentazione `SIGSEGV`
- Semplificazione della procedura per l'Accesso completo al disco (FDA) e fallback sicuro: Perfezionata la finestra di dialogo iniziale per nascondere automaticamente il pulsante ridondante «Apri impostazioni Accesso completo al disco» quando è supportato il trascinamento nativo (drag-to-grant), stabilendo un unico punto di ingresso chiaro che si aggiorna in «Accesso completo al disco concesso ✓» una volta attivo; aggiunto un fallback difensivo che mostra dinamicamente il pulsante delle impostazioni se il pannello Cocoa nativo non si apre, garantendo la concessione dei permessi in qualsiasi ambiente

### 2.3.6 (16-10-2026)

- Blocco della versione del compilatore Nuitka ed eliminazione dei crash su Apple Silicon (ARM64): Bloccata la versione del compilatore Nuitka alla release stabile 4.2.2 in tutti i workflow CI, prevenendo una grave corruzione della freelist del compilatore PySide6/Shiboken (`SIGSEGV / EXC_BAD_ACCESS`) introdotta da Nuitka 4.3; integrate le asserzioni di integrità per segnali/slot Qt e freelist del compilatore in `smoke_test.py`; allineati gli script di build locali con le pipeline di rilascio CI
- Rafforzamento del ciclo di vita per finestre e barra delle applicazioni su macOS 15 Sequoia: Riprogettati il ripristino delle finestre, l'attivazione (`activate_app`) e la commutazione dell'icona del Dock per prevenire invii non validi di `FocusWindowEvent` di WindowServer e crash in ambienti headless o di test; arrestati in sicurezza e isolati i thread di ascolto dei tasti di scelta rapida globali pynput per evitare leak di thread in background e hook `CGEventTap` pendenti; aggiunta la pulizia degli appunti alla chiusura per eliminare i crash del distruttore statico di `QMimeData`
- Stabilità della suite di test e ottimizzazione della pipeline CI: Risolti rari errori di segmentazione durante la chiusura di finestre e barra delle applicazioni nei test pytest, migliorando l'affidabilità dei test headless e offscreen; ottimizzati i workflow CI per saltare build ridondanti dei pacchetti in presenza di soli aggiornamenti alla documentazione

### 2.3.5 (15-10-2026)

- Integrazione VFS cloud nativa per Google Drive e Dropbox con OAuth 2.0: Introdotto il supporto nativo del file system virtuale per Google Drive (`gdrive://`) e Dropbox (`dropbox://`); aggiunti profili dedicati nel Gestore connessioni con supporto per credenziali personalizzate Client ID / Client Secret e autorizzazione OAuth 2.0 via browser con un solo clic; ottimizzati i percorsi rapidi di copia diretta in streaming, la memorizzazione nella cache TTL delle quote e l'elenco lazy delle cartelle con salvataggio automatico del profilo
- Sicurezza consolidata del Portachiavi ed esportazione/importazione crittografata delle credenziali: Riorganizzati i namespace del servizio Portachiavi per eliminare finestre ripetitive di autorizzazione all'avvio e garantire la persistenza affidabile di credenziali e licenze; introdotta l'esportazione e importazione crittografata delle credenziali salvate, protette da password definita dall'utente per una migrazione sicura tra dispositivi, supportata da localizzazione completa in 31 lingue
- Rafforzamento del runtime Nuitka e miglioramenti dello streaming Zip: Risolti rari crash di avvio nelle build Nuitka standalone ed estesa la copertura dello smoke test CI a tutti i pacchetti distribuiti; perfezionato il motore di streaming Zip per gli archivi e risolto il potenziale svuotamento del pannello file durante l'invalidazione della cache cloud
- Risoluzione della concorrenza nell'ordinamento e guida completa alla configurazione cloud: Risolte le race condition tra thread nei test di ordinamento naturale e cartelle in cima (Fixes #58); ampliato il Capitolo 6 della Guida utente con istruzioni passo-passo per la configurazione delle API di Google Drive e Dropbox, la schermata di consenso OAuth e le linee guida sulla sicurezza

### 2.3.4 (13-10-2026)

- Rinnovamento della procedura dei permessi della sandbox e flusso di autorizzazione unificato: Ripristinata e unificata l'autorizzazione per la cartella Home dell'utente (`~`) e le unità esterne (`/Volumes`) in una procedura semplificata con un solo pulsante «Concedi autorizzazioni»; introdotta la promozione intelligente dei percorsi che eleva automaticamente le richieste di accesso alle sottocartelle alla cartella home o alla radice del volume salvando segnalibri con ambito di sicurezza, eliminando del tutto le continue richieste di autorizzazione nella sandbox di macOS App Store
- Internazionalizzazione dei pulsanti di dialogo standard e approfondimento del catalogo in 31 lingue: Implementato `_GettextQtTranslator` per intercettare e tradurre dinamicamente tramite gettext i pulsanti standard di Qt (Sì, No, OK, Annulla, Salva, Elimina, Applica, Chiudi, Apri, Reimposta) con rimozione automatica degli acceleratori di scelta rapida (`&`); aggiunta la ritraduzione dinamica dell'interfaccia (`retranslate_ui`) nelle pagine delle preferenze (Barra degli strumenti, Tasti di scelta rapida, Schede preferite, Aggiornamento automatico), in Gestione connessioni e nel Visualizzatore code; aggiornati e compilati i cataloghi `.po`/`.mo` per tutte le 31 lingue supportate con nuovi test automatizzati

### 2.3.3 (10-10-2026)

- Riprogettazione dell'archiviatore, compressione separata e avanzamento in streaming: Aggiunta l'opzione «Crea un archivio separato per ogni elemento selezionato» nella finestra di dialogo dell'archivio per comprimere in batch i singoli elementi; implementato il monitoraggio dell'avanzamento in streaming per file di grandi dimensioni (≥1 MB) con i driver Zip, Tar e 7z; introdotta la gestione dei conflitti thread-safe (Sovrascrivi, Salta, Ridenomina automaticamente, Annulla), migliorata la tolleranza agli errori nei batch per elementi danneggiati, preservati in modo affidabile i collegamenti simbolici e sincronizzate le traduzioni in 31 lingue
- Ripristino della geometria dalla barra delle applicazioni e rafforzamento della scorciatoia globale di macOS: Ripristinati perfettamente la posizione, le dimensioni e lo stato massimizzato della finestra alla riattivazione dalla barra delle applicazioni; impedito ai menu contestuali della barra di portare involontariamente in primo piano la finestra principale; rinnovata la scorciatoia globale di macOS per mostrare/nascondere la finestra normalizzando i tasti Option e memorizzando nella cache del thread principale i contesti dei tasti per evitare asserzioni in background su macOS Sequoia; aggiunto l'interruttore dinamico nelle Preferenze per ridurre a icona nella barra
- Selettore unità e anteprime avanzate della capacità del disco: Aggiornata la barra di selezione delle unità con etichette di volume native e icone hardware del disco; arricchite le descrizioni comandi a comparsa con punto di montaggio, tipo di file system, spazio libero su disco e statistiche sulla capacità totale
- Integrità di build con Nuitka e smoke test automatizzati per il bundle: Aggiunto `--include-package=atbcmder` in tutti gli script di build Nuitka per eliminare gli errori `ModuleNotFoundError` a runtime causati dal caricamento differito delle finestre di dialogo; introdotta la verifica headless `--smoke-test` integrata nei flussi di lavoro DMG, Mac App Store PKG e CI per garantire pacchetti applicativi solidi e pronti all'uso
- Lancio della pagina ufficiale multilingue del prodotto: Pubblicato il sito web moderno di presentazione del prodotto con un router di lingua intelligente lato client (con supporto a italiano, inglese, cinese, giapponese, coreano e altri) evidenziando la produttività del doppio pannello e la cura nativa per macOS

### 2.3.2 (07-10-2026)

- Ottimizzazione avanzata della memoria runtime PySide6 e compattazione dell'heap su Darwin: Implementato il caricamento lazy proxy per finestre di dialogo secondarie pesanti (`_make_lazy_dialog`) ed esportazioni di moduli PEP 562 per ridurre drasticamente la memoria residente; incapsulate le chiamate Cocoa/PyObjC in `objc.autorelease_pool()` per eliminare l'accumulo di memoria durante il polling dei tag colore di Finder; integrata la compattazione nativa dell'heap Darwin tramite `malloc_zone_pressure_relief` nei tempi di inattività e alla chiusura delle finestre; limitato ThumbnailManager a 4 thread di lavoro con decodifica thread-safe e caching multilivello delle icone
- Ripristino del cursore lampeggiante e focus automatico nel visualizzatore F3 e nell'editor F4: Risolta la perdita di focus all'apertura del visualizzatore o dell'editor focalizzando automaticamente il buffer di testo all'attivazione per l'interazione immediata da tastiera; ripristinato il cursore lampeggiante da 1px ben visibile, disaccoppiate le impostazioni del cursore tra visualizzatore ed editor, abilitata la visualizzazione del cursore per impostazione predefinita e aggiunta la scorciatoia F6 (`cm_ShowCaret`) per alternare la visibilità del cursore nel Visualizzatore universale
- Rafforzamento del ciclo di vita delle risorse e aggiornamenti della documentazione: Aggiunto `WA_DeleteOnClose` al Visualizzatore universale per garantire la completa distruzione dei widget e il recupero della memoria alla chiusura; aggiornate le guide per l'utente e le immagini illustrative della documentazione

### 2.3.1 (06-10-2026)

- Guida ai permessi della sandbox e riposizionamento intelligente delle finestre: Quando si richiede l'accesso completo al disco (FDA) e si aprono le Impostazioni di Sistema, la finestra di dialogo si ridimensiona e si sposta automaticamente nella parte sinistra dello schermo, affiancandosi perfettamente alle Impostazioni di Sistema di macOS senza sovrapposizioni
- Guida passo-passo chiara e promemoria di riavvio: Riprogettata la finestra di notifica con una guida intuitiva in 4 passaggi (trovare o aggiungere ATBCmder, attivare l'interruttore, chiudere e riavviare l'applicazione) con promemoria chiari sul fatto che l'accesso FDA diventa effettivo dopo il riavvio
- Traduzione in 31 lingue e sincronizzazione del glossario: Aggiornato il glossario di localizzazione e ricompilati i cataloghi dei messaggi in tutte le 31 lingue supportate, garantendo notifiche di benvenuto chiare e naturali in tutto il mondo

### 2.3.0 (05-10-2026)

- Tag colore nativi di macOS Finder e sincronizzazione in tempo reale: Profonda integrazione con le API macOS Foundation (`NSURLTagNamesKey`) e `NSWorkspace` per visualizzare i tag a punti colorati di Finder nei pannelli file; supporta l'ordinamento in base all'ordine nativo dei colori di Finder con polling del viewport ogni 2 secondi per la sincronizzazione immediata; include la visibilità personalizzabile della colonna nelle Preferenze ed etichette dei colori completamente localizzate
- Revisione completa della sincronizzazione directory (`cm_SyncDirs`): Riprogettata integralmente la sincronizzazione directory per eliminare i deadlock dello stato dell'interfaccia utente con l'aggiunta di una finestra dedicata agli errori (`SyncErrorsDialog`); introdotti Scambia directory, eliminazione bidirezionale (`OP_DELETE_BOTH`), sintassi di esclusione con carattere pipe `|`, statistiche di selezione in tempo reale, esportazione CSV, sottomenu di selezione, «Mostra nel Finder» e memorizzazione della geometria della finestra e della larghezza delle colonne
- Tooltip interattivi in vetro smerigliato stile Apple HIG: Realizzata un'architettura centralizzata per i tooltip con schede in vetro smerigliato translucido all'80% perfettamente intonate all'aspetto Chiaro e Scuro di macOS; unificati i tooltip su barre degli strumenti, splitter, percorsi breadcrumb, tasti funzione Fx e finestre di dialogo con badge delle scorciatoie native di macOS sopprimendo i tooltip Qt duplicati
- Conformità alle convenzioni delle scorciatoie native di macOS e deduplicazione automatica: Descrizioni e simboli delle scorciatoie standardizzati per rispettare le convenzioni native di macOS, sincronizzando rigorosamente voci di menu e pulsanti della barra degli strumenti; eliminati i conflitti storici 1 a 1 con la deduplicazione automatica nelle finestre di impostazione, nel registro dei comandi e nella memorizzazione XML
- Copertura della traduzione al 100% in 31 lingue ed espansione delle presentazioni demo: Raggiunta la copertura di localizzazione al 100% e la corretta gestione delle forme plurali in tutte le 31 lingue supportate; potenziato il Visualizzatore file universale (F3) con la modalità di emergenza «Apri in modalità testo» e aggiunti tooltip al passaggio del mouse per i nomi di file troncati; ampliati gli script demo con dimostrazioni per Filtro rapido, Ridenominazione multipla, VFS trasparente per archivi, sincronizzazione directory e Vista ad albero

### 2.2.0 (03-10-2026)

- Ergonomia della barra degli strumenti principale e sfumature Apple HIG: Icone della barra principale ingrandite a 38px e altezza della barra portata a 42px per evitare elementi schiacciati e offrire comodi bersagli di clic sui display Retina; rinnovate le icone con vivaci sfumature colorate in stile Apple HIG e contrasto migliorato, armonizzando le proporzioni tra la barra principale e quella centrale
- Integrazione completa delle preferenze e impostazioni dell'editor di codice: Collegati completamente i parametri precedentemente disconnessi (zoom dei caratteri, impostazioni predefinite dell'archiviatore, rientro automatico, larghezza massima del testo nel visualizzatore); corretto il salvataggio della dimensione delle tabulazioni (`tab_size`) e del rientro in `CodeEditorWidget` tramite caricamento affidabile della configurazione a runtime
- Gestione globale della memoria e ottimizzazione profonda delle prestazioni: Revisione della cache delle icone e dei metadati dei file con inizializzazione differita (lazy loading) per i componenti pesanti; rafforzato il ciclo di vita dei widget e la pulizia dei riferimenti deboli per eliminare i memory leak, garantendo fluidità nella navigazione di directory molto grandi
- Prevenzione dei blocchi nei dialoghi modali e stabilità del focus nella vista ad albero: Risolti i potenziali blocchi modali alla chiusura di `ArchiveDialog` e `SplitLinkDialog`; garantito il mantenimento continuo del focus da tastiera sulla scheda attiva durante il passaggio alla modalità vista ad albero e la navigazione delle cartelle
- Ottimizzazioni del packaging Nuitka e prevenzione dei crash: Ottimizzate le pipeline di compilazione per app standalone e DMG per ridurre il picco di memoria di build e le dimensioni del bundle; perfezionati i flag del compilatore per eliminare i crash di avvio dovuti a importazioni di test nelle versioni distribuite

### 2.1.0 (02-10-2026)

- Riprogettazione Apple HIG per barra delle unità e schede: Riprogettata la barra delle unità e i pulsanti di navigazione con controlli senza bordi in stile Apple; modernizzate la barra del percorso breadcrumb e le schede dei file utilizzando superfici tonali Apple HIG per un'estetica raffinata e nativa per macOS
- Stepper moderni HIG, tooltip a capsula e paginazione: Aggiornati i controlli numerici (QSpinBox / QDoubleSpinBox) con stepper integrati secondo macOS HIG; introdotti tooltip a capsula traslucida in stile Apple posizionati in modo intelligente sotto le icone; adattate la paginazione e le icone delle impostazioni agli standard HIG
- Barra degli strumenti verticale e gerarchia delle miniature: Aggiunta un'icona dedicata per «Rendi la destinazione uguale all'origine (`cm_TargetEqualSource`)» sulla barra centrale verticale; corretto l'ordine z del badge di selezione delle miniature per garantire che venga visualizzato in primo piano sopra le immagini; risolto il trabocco dei pulsanti di zoom nella barra di stato dell'editor di immagini
- Revisione completa della terminologia e localizzazione in 31 lingue: Revisione e perfezionamento della terminologia dell'interfaccia utente, dei tooltip e delle finestre di dialogo in tutte le 31 lingue supportate, eliminando voci mancanti e formulazioni imprecise per un'esperienza naturale da madrelingua
- Miglioramenti agli strumenti e all'infrastruttura di automazione: Standardizzati i flussi di lavoro dei cataloghi di localizzazione (`atb-python-i18n`), semplificata la risoluzione dei token per gli helper di rilascio e rafforzato l'isolamento dei test per una pipeline CI/CD affidabile

### 2.0.0 (28-09-2026)

- 🎉 Traguardo architetturale fondamentale di ATBCmder 2.0: Celebra la piena maturità dell'architettura moderna del file manager a doppio pannello, combinando il leggendario flusso di lavoro orientato alla tastiera di Double Commander con prestazioni e design nativi moderni per macOS
- Localizzazione globale completa in 31 lingue: Traduzione nativa completa e naturale dell'intero flusso di concessione delle autorizzazioni e del pannello nativo «Trascina per autorizzare» (Drag-to-Grant) in tutte le 31 lingue supportate; ricompilati tutti i cataloghi .mo e aggiunti test di regressione multilingue automatici
- Concessione rivoluzionaria dell'Accesso completo al disco «Trascina per autorizzare»: Basato sul Cocoa NonactivatingPanel nativo per consentire agli utenti di trascinare l'icona dell'applicazione direttamente nelle Impostazioni di Sistema senza sottrarre il focus alla finestra; la finestra guida si aggancia intelligentemente a lato delle Impostazioni di Sistema con l'opzione fluida «Esci e riapri», eliminando i fastidiosi timer di riavvio automatico
- Perfezionamento del flusso a doppio pannello e interfaccia utente: Facendo doppio clic sulla barra centrale o sul divisore è possibile ripristinare istantaneamente i pannelli a un rapporto bilanciato 50:50 con tooltip localizzati; la barra degli strumenti principale include per impostazione predefinita una capsula di stato del sistema elegante con chiusura rapida e menu contestuale; perfezionato l'ordinamento misto delle cartelle su tutte le colonne
- Editor di testo moderno e suite ATBSys ad alte prestazioni: L'editor integrato offre ora la navigazione standard Home/End su macOS con posizionamento intelligente della riga Smart Home; perfettamente integrato con il daemon nativo in Go `atbsys` per la pulizia dei dati a 64 bit ad alta precisione e la disinstallazione approfondita dei residui delle applicazioni

### 1.9.9 (27-09-2026)

- Accesso completo al disco «Trascina per autorizzare» e procedura guidata rinnovata: Introdotto un innovativo pannello mobile basato su Cocoa NonactivatingPanel che consente di trascinare l'icona dell'app direttamente nelle Impostazioni di Sistema senza sottrarre il focus alla finestra; il dialogo esplicativo si posiziona automaticamente a lato delle Impostazioni di Sistema e offre l'opzione «Esci e riapri» alla concessione dell'autorizzazione FDA, eliminando i fastidiosi timer di riavvio forzato
- Pareggiamento 5:5 del doppio pannello e rifinitura del divisore centrale: Facendo doppio clic sulla barra centrale o sul divisore si ripristinano istantaneamente le dimensioni dei pannelli su un rapporto identico 50:50 con suggerimenti localizzati; risolti i problemi di leak nelle sottoscrizioni i18n, eliminati i cursori del mouse residui e migliorato lo stile del visualizzatore e dei dialoghi
- Ergonomia della tastiera nell'editor (Home/End e Smart Home): L'editor di testo integrato supporta ora pienamente i tasti Home ed End su macOS con comportamento Smart Home (alternando il cursore tra il primo carattere non vuoto e l'inizio assoluto della riga)
- Gestione della capsula di stato del sistema e menu contestuale: La capsula di stato del sistema sulla barra degli strumenti principale è ora abilitata per impostazione predefinita con pulsante di chiusura rapida (×); introdotto un menu contestuale con clic destro per attivare o disattivare agevolmente i singoli componenti della barra
- Parità nell'ordinamento misto delle cartelle e accelerazione del rendering: La modalità di ordinamento misto (`sort_folder_mode = mixed`) intercala fedelmente file e cartelle su tutte le colonne con applicazione immediata a runtime; rimosse le dichiarazioni di pseudo-font per eliminare l'overhead di CoreText, uniformate le altezze delle schede del tutorial e impedito il clic passante sui menu nativi

### 1.9.8 (24-09-2026)

- Precisione a 64 bit (>2 GB) negli strumenti di sistema e miglioramenti al disinstallatore: Risolto l'overflow dei segnali interi a 32 bit di Qt e la perdita di precisione a 64 bit durante il conteggio delle pulizie superiori a 2 GB; aggiunti la visualizzazione e l'ordinamento per data di installazione nel Disinstallatore di applicazioni
- Conformità alla sandbox del Mac App Store e propagazione della cartella Home reale: Propagata la directory iniziale reale dell'utente (`real_home`) al bridge `atbsys` per un'accurata pulizia del disco e rilevamento dei residui all'interno di App Sandbox; rafforzate le interfacce di elevazione dei privilegi, esecuzione del terminale e scripting per il rigoroso rispetto delle linee guida di revisione dell'App Store
- Controlli di layout nelle preferenze e correzioni della Directory Hotlist: Aggiunti i controlli di attivazione/disattivazione del layout della finestra principale nelle Preferenze Generali con sincronizzazione in tempo reale di `MainWindow` e `ThemeManager`, e disabilitata per impostazione predefinita la capsula di stato del sistema sulla barra degli strumenti principale per uno spazio di lavoro iniziale più pulito; corretti i menu a discesa vuoti e la ritraduzione dinamica della lingua nelle impostazioni della Directory Hotlist
- Uniformità terminologica e miglioramento del selettore della lingua: Standardizzata la traduzione cinese di "Directory Hotlist" in "路径收藏夹" su tutte le interfacce utente e migliorato il selettore della lingua nelle Preferenze con la doppia visualizzazione del nome in lingua nativa e tradotto
- Conservazione delle ACL del Portachiavi macOS e affidabilità della copia in streaming: Preservati gli elenchi di controllo degli accessi (ACL) esistenti del Portachiavi macOS ed eliminate le scritture ridondanti all'avvio per evitare ripetute richieste di autorizzazione del Portachiavi; garantita l'emissione deterministica del segnale `operation_completed` prima del completamento del thread in `StreamCopyWorker`

### 1.9.7 (23-09-2026)

- Applicazione immediata delle impostazioni in fase di esecuzione (Hot Reload): Tutte le impostazioni di configurazione nelle 7 pagine principali delle opzioni (Operazioni sui file, Editor, Visualizzatore, Ricerca rapida e filtro, Schede, Icone del pannello file e Ordinamento) ora hanno effetto immediato al salvataggio senza riavviare l'applicazione; aggiunto il parametro configurabile `sort_folder_mode` con supporto per Cartelle prima, File prima e Ordinamento misto
- Sicurezza e parità nella sincronizzazione delle directory: Audit completo della Sincronizzazione delle directory (`cm_SyncDirs`) per allineare il comportamento direttamente al classico Double Commander; rafforzati i controlli di sicurezza e la convalida dello stato bidirezionale per eliminare i rischi di sincronizzazione asimmetrica
- Suggerimenti intelligenti per i nomi di file troncati con precisione CJK: Aggiunti suggerimenti intelligenti al passaggio del mouse e alla selezione che compaiono esclusivamente quando i nomi di file lunghi vengono troncati con i puntini di sospensione, mantenendo l'interfaccia pulita per gli elementi completamente visibili; integrati calcoli ad alta precisione della larghezza dei caratteri CJK per eliminare discrepanze nelle metriche dei font
- Perfezionamento del flusso di lavoro a doppio pannello e delle interazioni: La compressione e l'estrazione di archivi tramite clic destro impostano per impostazione predefinita la directory del pannello opposto come destinazione con focus predefinito sul pulsante Avvia; perfezionato l'ordine dei pulsanti e il pulsante predefinito da tastiera nella finestra di conferma dell'eliminazione; ripristinati i cursori a mano per i pulsanti di azione della barra degli strumenti centrale
- Cartella Home reale nella sandbox del Mac App Store e rafforzamento FDA: Implementato il motore di risoluzione `real_home` per risolvere accuratamente le directory utente e le Directory Hotlist nei container App Sandbox; risolti i falsi allarmi dell'Accesso completo al disco (FDA) con chiusura automatica delle finestre di dialogo dopo l'autorizzazione; migrate le metriche CPU di sistema alle statistiche host Mach per la conformità alla sandbox

### 1.9.6 (21-09-2026)

- Modalità di ridimensionamento a dimensione personalizzata nell'editor di immagini: Introdotta la modalità "Dimensione personalizzata (Custom Size)" nella finestra di ridimensionamento delle immagini, che consente l'immissione diretta dei pixel per larghezza e altezza con blocco opzionale delle proporzioni, offrendo agli utenti un controllo preciso sul ridimensionamento
- Rafforzamento della sicurezza Sandbox e conformità alla revisione del Mac App Store: Conformità rigorosa alle linee guida per la revisione di Apple App Store 2.4.5(v) e 2.5.2; rimozione delle richieste di autorizzazione della directory principale nelle build sandbox e disabilitazione dell'interfaccia e della logica di terminazione dei processi (SIGKILL/SIGTERM) in modalità sandbox MAS, eliminando i rischi di violazione e rifiuto della sandbox
- Gestione adattiva del trabocco della barra degli strumenti e stabilità del visualizzatore Diff: Aggiunta la gestione automatica del trabocco nella barra degli strumenti principale per raggruppare i pulsanti in eccesso in un menu a discesa su schermi compatti; risolto un blocco intermittente nella suite di test del visualizzatore Diff su macOS x86
- Localizzazione del menu in 30 lingue: Completate traduzioni esaustive per il menu di primo livello "Strumenti (Tools)" e le relative azioni in tutte le 30 lingue supportate
- Prestazioni dell'interfaccia utente e resilienza della pipeline CI/CD: Pulizia dei riferimenti residui ai widget nel pannello di testo per velocizzare notevolmente il cambio di tema e la velocità di ridisegno; aggiornati i flussi di lavoro CI/CD per supportare la selezione parametrizzata dei runner ARM64 (self-hosted vs. cloud) con backoff esponenziale e nuovi tentativi per il trasferimento degli artefatti

### 1.9.5 (19-09-2026)

- Eredità della Sandbox per gli eseguibili helper del Mac App Store: Aggiunti permessi dedicati (`com.apple.security.app-sandbox` e `com.apple.security.inherit`) per tutti gli eseguibili figlio (come il binario degli strumenti di sistema `atbsys`) in `Contents/MacOS/`, garantendo che i processi helper ereditino correttamente il container App Sandbox e i criteri di sicurezza dell'applicazione principale per la totale conformità con il Mac App Store
- Firma del codice Hardened Runtime per gli helper DMG: Abilitato Hardened Runtime (`--options runtime`) con le autorizzazioni appropriate per tutti gli eseguibili ausiliari Mach-O nei bundle di distribuzione DMG, garantendo la totale conformità con i requisiti di firma del codice e notarizzazione di Apple Developer ID
- Pulizia della struttura del bundle e test di integrazione del packaging: Rimozione automatica delle directory binarie di risorse ridondanti (`Contents/Resources/bin`) per una struttura del bundle più pulita e conforme alle regole dell'App Store; aggiunti test di integrazione automatizzati del packaging per i permessi helper, Hardened Runtime e gli script di compilazione multi-architettura

### 1.9.4 (19-09-2026)

- Suite di strumenti di sistema e manutenzione ATBSys: Perfetta integrazione della suite nativa di utilità di sistema, con una Capsula di Stato del Sistema nella barra degli strumenti principale (monitoraggio in tempo reale di CPU, memoria, disco e larghezza di banda di rete con menu contestuale per pausa/intervallo/nascondi e selettore nelle preferenze), Pannello di Stato del Sistema completo (metriche hardware e gestione/arresto forzato dei processi tramite clic destro), Analizzatore dello Spazio su Disco (visualizzazione gerarchica Treemap a mappa ad albero, ordinamento interattivo delle colonne, azioni mostra nel Finder/sposta nel cestino ed esportazione di report CSV/TXT), Pulitore di Sistema sicuro a due fasi (scansione e pulizia di cache utente, registri delle applicazioni, file residui, categorie Homebrew, CocoaPods e Docker con protezione tramite whitelist `~/.config/mole/whitelist`) e Disinstallatore approfondito di applicazioni con rilevamento dei residui
- Motore bridge Go ad alte prestazioni e registro di controllo: Basato sul binario Go nativo, autonomo e leggero `atbsys`, che comunica tramite QProcess asincrono e non bloccante; pacchettizzato come Universal Binary con integrazione nell'assemblaggio automatico e nella pipeline CI/CD; tutte le operazioni di pulizia e disinstallazione sono strutturate e registrate nei log di audit nella directory dei log di ATBCmder
- Tutorial introduttivo interattivo ampliato a 27 passaggi: Aggiornato il percorso di apprendimento per principianti per includere esercitazioni pratiche per gli strumenti di monitoraggio e manutenzione del sistema; riprogettato il posizionamento dell'evidenziazione della barra dei menu per una precisione indipendente dalla lingua sulla barra dei menu nativa di macOS
- Localizzazione completa in 30 lingue e documentazione ufficiale: Traduzioni complete per tutti i componenti ATBSys, le opzioni della capsula di stato, le impostazioni e i passaggi del tutorial in tutte le 30 lingue supportate; guida utente ufficiale in inglese arricchita con il Capitolo 7: Strumenti di sistema e manutenzione
- Rifinitura dell'interfaccia utente e rafforzamento del packaging: Allargata la capsula della barra di stato e le etichette della velocità di rete per eliminare il troncamento del testo durante i trasferimenti di rete ad alta velocità; perfezionato il layout della capsula allineata a destra e la sincronizzazione dello scollegamento delle scorciatoie da tastiera; rafforzata la logica di iniezione di dylib e binari per architetture singole e universali su runner macOS 12 x86_64

### 1.9.3 (17-09-2026)

- Supporto per l'anteprima di file .ini nel visualizzatore universale: Aggiunto il supporto nativo per l'anteprima in testo normale dei file di configurazione `.ini` nel visualizzatore universale (F3) e in Quick View (`Ctrl+Q` / `⌘Q`), consentendo l'ispezione immediata delle impostazioni senza aprire editor esterni
- Packaging App Store e firma dei framework: Compilazione e iniezione automatizzata di `libATBLicenseKit.dylib` in `Contents/Frameworks/` per le build di rilascio del Mac App Store e DMG; aggiunte la firma rigorosa del codice e la notarizzazione per le librerie dinamiche, migliorata la ricerca del bundle a runtime e rafforzata l'unione dei file binari universali
- Stabilità del motore del tutorial interattivo: Risolti i timeout di navigazione dei passaggi nel percorso delle directory preferite (Hotlist), reimpostati correttamente i flag di transizione in sospeso durante il cambio di passaggio e scollegati i segnali di eventi pendenti per eliminare le perdite di segnale durante l'onboarding

### 1.9.2 (17-09-2026)

- Sistema di licenze e prova StoreKit 2: Sistema integrato di licenze e acquisto a vita basato su Swift StoreKit 2 per il Mac App Store, con monitoraggio del periodo di prova per giorni di calendario, convalida delle ricevute offline e ripristino degli acquisti; include badge della licenza nella barra degli strumenti, finestra di dialogo paywall e supporto per binari universali (macOS 12+, Apple Silicon e Intel)
- Esecuzione integrata di comandi Shell: La barra della riga di comando inferiore ora esegue direttamente comandi shell nel terminale di sistema (Terminal / iTerm2); supporta il completamento dei percorsi con Tab e i comandi `cd` puri navigano direttamente nei pannelli attivi
- Riorganizzazione della sincronizzazione directory e Diff in linea per parole: Riprogettata la sincronizzazione delle cartelle (`cm_SyncDirs`) con una classica griglia a 7 colonne e integrazione del Diff con doppio clic, eliminando i rischi di sincronizzazione asimmetrica; il visualizzatore Diff aggiunge l'evidenziazione dettagliata di parole/caratteri in linea e la navigazione tra prima e ultima differenza
- Allineamento con lo spazio di archiviazione nativo di macOS e rafforzamento VFS: Visualizzazione della capacità dell'unità e dello spazio disponibile allineata alle specifiche di "Spazio" nelle Impostazioni di Sistema di macOS; VFS di rete (SFTP/FTP/Samba/WebDAV) rafforzato con controlli di attività, riconnessione automatica e FTPS; icona della barra delle applicazioni aggiornata a un'icona modello monocromatica minimalista

### 1.9.1 (14-09-2026)

- Passaggio di ricerca rapida nel tutorial interattivo: Percorso formativo ampliato a 25 passaggi con esercitazione pratica di ricerca e filtro rapido (`⌘S` / `Ctrl+S`); aggiunta la voce di ricerca rapida nel menu Comandi e perfezionata la pulizia dell'overlay durante i cambi di passaggio
- Pipeline di pacchettizzazione CI e rafforzamento delle dipendenze: Ripristinata la dipendenza `ebooklib` nelle build di rilascio per garantire l'anteprima completa dei file EPUB; migliorata la pulizia dell'area di lavoro per evitare conflitti di permessi

### 1.9.0 (13-09-2026)

- Sistema di tutorial interattivo per nuovi utenti: Aggiunto un percorso introduttivo interattivo in 24 passaggi per i nuovi utenti con finestra di benvenuto al primo avvio (accessibile in qualsiasi momento da "Aiuto → Tutorial interattivo"); include overlay a riflettore (spotlight), schede informative fluttuanti adattive e doppio suggerimento con percorso di menu e scorciatoia nativa
- Aggiornamento della sicurezza di rete SFTP: Sostituita l'accettazione automatica non sicura della chiave host con una rigorosa politica di verifica TOFU (Trust-On-First-Use); la connessione a host SFTP sconosciuti ora mostra una finestra di dialogo interattiva per la conferma dell'impronta digitale SHA-256, salvando le chiavi in modo sicuro in `~/.ssh/known_hosts` contro gli attacchi MITM
- Scorciatoie native macOS e rifinitura della navigazione: Risolti i conflitti dei tasti modificatori per `Command+Su` (navigazione alla cartella superiore) e `Command+Shift+F1` (attivazione vista miniature), standardizzando tutte le indicazioni con i simboli nativi di macOS (⌘, ⌥, ⌃, ⇧)
- Prestazioni del core e pipeline di build: Ottimizzata la corrispondenza dei template semantici e la reattività dell'autocompletamento; ristrutturati i flussi di lavoro di rilascio automatizzati di GitHub Actions con protezioni anti-crash della sandbox AppKit

### 1.8.0 (11-09-2026)

- Supporto per pacchetti universali: Supporto per pacchetti universali con architetture x86_64 e ARM
- Pipeline di compilazione automatizzata: Compilazione e pacchettizzazione automatiche tramite GitHub Actions
- Associazioni intelligenti di file e app esterne: Introdotto un sistema di gestione delle associazioni (`extassoc.xml`) per personalizzare azioni, visualizzatori ed editor esterni per estensione; integrazione con fallback intelligente a macOS LaunchServices e finestra di dialogo dedicata "Apri con"
- Trasferimento di file di grandi dimensioni e protezione dall'overflow a 64 bit: Eliminati completamente i problemi di overflow degli interi a 32 bit nei segnali di avanzamento e nei cursori del pannello di testo, garantendo trasferimenti fluidi e un report accurato dell'avanzamento per file superiori a 2 GB su volumi montati e condivisioni di rete
- Gerarchia di navigazione ESC unificata nel visualizzatore: Gestione standardizzata del tasto ESC in tutti i pannelli di anteprima con chiusura a livelli (barra di ricerca → filtro attivo → schermo intero → chiudi finestra), eliminando i conflitti di scorciatoie e ottimizzando il cambio rapido di file
- Localizzazione dinamica in tempo reale: La barra dei tasti funzione inferiore (F3–F8) ora si ritraduce istantaneamente al cambio della lingua nelle Preferenze senza richiedere il riavvio dell'applicazione

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