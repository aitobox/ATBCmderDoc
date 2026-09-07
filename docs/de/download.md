# Kapitel 10: Download & Installation

Vielen Dank für Ihr Interesse an ATBCmder! Wir bieten zwei verschiedene Download- und Installationsmethoden an, um Ihren Anforderungen gerecht zu werden. 

> [!IMPORTANT] 
> **System- und Architekturanforderungen** 
> 
> - **Betriebssystem**: macOS 12.0 (Monterey) oder höher (einschließlich macOS 13 Ventura, macOS 14 Sonoma und macOS 15 Sequoia). 
> - **Unterstützte Hardwarearchitektur**: **Apple Silicon (M1 / M2 / M3 / M4, ARM64)**. 
> - **Intel (x86_64)-Kompatibilität**: Intel-basierte Macs werden derzeit **nicht unterstützt**.

## 1. Mac App Store (empfohlen)

Dies ist die empfohlene Methode zur Installation von ATBCmder. **ATBCmder ist jetzt offiziell im Mac App Store erhältlich!** Durch das Herunterladen über den offiziellen Mac App Store erhalten Sie nahtlose automatische Updates, nativen macOS-Sandbox-Schutz und die beste Systemintegration. 

- **Mac App Store**: [ATBCmder im Mac App Store herunterladen](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. DMG-Installationsprogramm herunterladen

Wenn Sie keinen Zugriff auf den Mac App Store haben oder direkte Downloads bevorzugen, bieten wir ein eigenständiges DMG-Installationspaket an, das nativ für Apple Silicon (ARM64) erstellt wurde. 

- **DMG-Download-Link**: [Klicken Sie hier, um ATBCmder DMG herunterzuladen](https://storage.aitobox.com/@s/bNAshV6G/ATBCmder) *(nur Apple Silicon / ARM64)* 

*Hinweis: Bei der Installation über DMG erfordern die Sicherheitsfunktionen von macOS möglicherweise, dass Sie die Anwendung beim ersten Öffnen unter „Systemeinstellungen > Datenschutz und Sicherheit“ explizit zulassen. Intel (x86_64) Macs werden nicht unterstützt.*

### ⚠️ Gewähren Sie vollen Festplattenzugriff

ATBCmder ist ein Dateiverwaltungstool und erfordert vom Benutzer explizite Berechtigungen zur Datenträgerverwaltung. Bitte folgen Sie diesen Schritten: 

1. Klicken Sie auf das Apple-Symbol in der oberen linken Ecke Ihres Bildschirms und wählen Sie **Systemeinstellungen** (oder „Systemeinstellungen“ bei älteren macOS-Versionen). 
2. Navigieren Sie im linken oder rechten Menü zu **Datenschutz und Sicherheit**. 
3. Scrollen Sie nach unten und wählen Sie **Vollständiger Festplattenzugriff**. 
4. Suchen Sie die Anwendung (**ATBCmder**) in der Liste und schalten Sie den Schalter um, um sie einzuschalten. Wenn die Anwendung nicht in der Liste enthalten ist, klicken Sie unten auf die Schaltfläche ***, um sie manuell hinzuzufügen. 
5. Das System fordert Sie auf, Ihr Mac-Anmeldekennwort einzugeben oder Touch ID zu verwenden, um die Änderungen zu bestätigen.

## Versionshinweise

### 1.7.0 (06.09.2026)

- Universal File Viewer & Office Preview Suite: Native Vorschau-Engines für Excel-Tabellen (mit Lazy Virtual Loading), Word-Dokumente (mit Paginierung und eingebetteter Bildwiedergabe) und PowerPoint-Präsentationen (Diakartenansicht) hinzugefügt; Vorschauen für SQLite-Datenbanken, Markdown (mit Inhaltsverzeichnis), Jupyter-Notizbücher, Schriftarten, Archive, Audio und EML hinzugefügt; Instant Streaming Infinite Scroll für große Textdateien implementiert 
- Side-by-Side File Diff Viewer: Integriertes Zwei-Wege-Vergleichstool im Vimdiff-Stil mit Diff-Hervorhebung auf Zeichenebene, Hunk-Kopieren, Live-Bearbeitung, Rückgängigmachen/Wiederherstellen und Erhaltung der Codierung 
- Erweiterte Dateisuchmaschine: Neu geschriebenes Suchsubsystem mit standardmäßigem Fuzzy-Teilstring-Matching, Regex-Unterstützung und einem Tab-Modus „Feed to Listbox“; Durch die Batch-Drosselung der Benutzeroberfläche wird das Einfrieren der Benutzeroberfläche bei umfangreichen Suchergebnissen verhindert 
- Dateioperationen und UI-Härtung: Doppelte Aufforderungen zum Überschreiben bei geräteübergreifenden Verschiebungen und Deadlocks in der Übertragungswarteschlange behoben; Zeitstempel für die Dateierstellung im Eigenschaftendialog hinzugefügt; Die vertikale mittlere Symbolleiste ist standardmäßig aktiviert und die visuellen Indikatoren im aktiven Bereich wurden verfeinert

### 1.6.2 (03.09.2026)

- Gummiband-Ziehauswahl und Interaktion: Maus-Gummiband-Ziehauswahl sowohl in der Dateitabellenansicht als auch in der Miniaturansicht hinzugefügt, zusammen mit der Möglichkeit, auf eine leere Stelle zu klicken, um die Auswahl aufzuheben 
- Globaler Fenster-Hotkey und Shortcut-Eingabe: Es wurde ein konfigurierbarer globaler Hotkey zum Ein-/Ausblenden des Anwendungsfensters hinzugefügt. Die Eingabe von 4-Tasten-Modifikatorkombinationen in den Hotkey-Einstellungen wurde korrigiert 
- macOS Dock & Tray Restore Fix: Es wurde ein Problem behoben, bei dem das Klicken auf das Dock-Symbol, während es auf die Taskleiste minimiert war, dazu führen konnte, dass das Hauptfenster nicht wiederhergestellt wurde oder ein leerer Rahmen angezeigt wurde 
- Kernhärtung und Stabilitätsverbesserungen: Potenzielle Segfaults im Lebenszyklus behoben, VFS-Backends gestärkt und Thread-Teardown und Testsuiten stabilisiert

### 1.6.1 (27.08.2026)

- Umfassende macOS UI/UX-Überarbeitung: Basierend auf Apple HIG mit verfeinerten Hell/Dunkel-Paletten, Hervorhebungskontrast im Finder-Stil, nativen Karten-Tooltips und glatten, segmentierten Steuerungsanimationen 
- Vektor-Icon-Engine und moderne Widgets: Ein von SF Symbols inspirierter, auflösungsunabhängiger Vektor-Icon-Generator sowie modernisierte Laufwerksleisten, Breadcrumbs und Kombinationsfelder wurden hinzugefügt 
- Interaction & Layout Polish: Multi-Rename neu gestaltet mit einem 2-Spalten-Layout und Echtzeit-Namenskollisionserkennung; Die Miniaturansicht unterstützt `Cmd + Wheel` dynamisches Zoomen; Einheitliche leere Zustandsansichten hinzugefügt

### 1.6.0 (27.08.2026)

- Dual-Distribution-Pipeline: Etablierte separate automatisierte Build-Workflows, die auf die eigenständige DMG-Distribution und die Veröffentlichung im Mac App Store (MAS) zugeschnitten sind 
- Einhaltung der App Store-Richtlinien: Passt UI-Menüs in MAS-Builds dynamisch an, indem externe Update-Prüfelemente entfernt werden, um die Apple-Überprüfungsrichtlinien strikt einzuhalten, während manuelle Update-Prüfungen in DMG-Builds beibehalten werden 
- `itms-services` Binärer Patcher: Ein automatisierter Binärscanner und ein sicherer Patcher wurden hinzugefügt, um private Protokollzeichenfolgen in kompilierten PySide6/Qt-Artefakten zu entfernen und so eine einwandfreie automatisierte App Store Connect-Validierung sicherzustellen

### 1.5.6 (22.08.2026)

- Unabhängige Ansichtsmodi pro Registerkarte: Jede Registerkarte behält jetzt ihr eigenes unabhängiges Ansichtslayout (flache Ansicht / Baummodus), synchronisiert den Menüstatus automatisch und bleibt über Sitzungswiederherstellungen hinweg nahtlos bestehen 
- Smart File Open & System Fallback: Es wurde ein mehrschichtiger Dateityp-Detektor (Magic Bytes/MIME/Erweiterung) hinzugefügt, um unterstützte Medien und Dokumente im integrierten Viewer/Editor zu öffnen und gleichzeitig für nicht unterstützte Dateien sauber auf die Standard-Apps des Betriebssystems zurückzugreifen

### 1.5.5 (21.08.2026)

- Richtlinienoptimierung für Update-Überprüfung: Automatische Update-Überprüfungen beim Anwendungsstart standardmäßig deaktiviert; Updates können jetzt manuell über `Help` -> `Check for Updates...` überprüft werden, was die Startgeschwindigkeit und den Offline-Datenschutz verbessert

### 1.5.4 (21.08.2026)

- Polieren von Panel-Fokus und -Auswahl: Verbleibende Fokuskonturen auf inaktiven geteilten Panels beim Wechseln der Panels wurden korrigiert; Verbesserte Logik zum Zurücksetzen der Auswahl nach dem Verschieben von Dateien über Panels, um versehentliche Vorgänge zu verhindern

### 1.5.3 (19.08.2026)

- Breadcrumb Cascading Submenu Polish: Die vertikale Position der kaskadierenden Unterordnermenüs wurde genau an der hervorgehobenen Zeile ausgerichtet, wodurch Layoutsprünge vermieden und das Durchlaufen tiefer Ordner geglättet wurden

### 1.5.2 (19.08.2026)

- Fehlerbehebung bei Start und Versionshinweisen: Es wurde ein Problem behoben, bei dem das Dialogfeld „Versionshinweise“ bei jedem App-Start wiederholt angezeigt wurde. Verbesserte `Config.get` Standard-Fallback-Behandlung, um sicherzustellen, dass Versionshinweise nur beim ersten Start oder bei Versions-Upgrades angezeigt werden

### 1.5.1 (19.08.2026)

- Mehrsprachige Versionshinweise: 7 neue Versionshinweise für Mainstream-Sprachen (zh_TW, ja, ko, de, fr, ru, es) mit dynamischer Erkennung und 5-stufigem hierarchischem Fallback hinzugefügt 
- macOS Code Signing & Build Polish: Überarbeitete Paketierungsskripte mit Mach-O-Binär-Targeting und Zeitstempel-Wiederholungs-Wrappern, wodurch Signierungsfehler und Drosselung vermieden werden

### 1.5.0 (17.08.2026)

- Globaler Sitzungsmanager: Sitzungspersistenz auf Anwendungsebene implementiert, die beim Neustart alle linken/rechten Panel-Registerkarten, Pfade, Ansichtsmodi (Flach/Baum), Panel-Verhältnisse und Fenstergrenzen für mehrere Monitore nahtlos wiederherstellt 
- Import/Export der Einstellungen: 1-Klick-ZIP-Export und -Import für alle Anwendungskonfigurationen und Daten hinzugefügt, um die geräteübergreifende Migration zu optimieren 
- Verbesserungen des Bildeditors: Benutzerdefinierte Bildgrößenänderung mit Seitenverhältnissperre und schnellen voreingestellten Auflösungen hinzugefügt

### 1.4.9 (17.08.2026)

- Erweiterter Bildeditor: Bildzuschnitt, Feindrehung, Filteranpassungen und ein OpenCV-basiertes KI-Modul zum Entfernen und Inpainting von Wasserzeichen hinzugefügt 
- Verbesserter Bildbetrachter: Volle Unterstützung für animierte GIFs, Zoomen, Schwenken, Drehen, EXIF-Metadatenextraktion und Diashow-Modus 
- Spotlight-Suchintegration: Tief integriertes natives macOS-Spotlight für sofortige Dateisuche und verbesserte Fokusnavigation in Suchergebnissen

### 1.4.8 (16.08.2026)

- Umfassende Lokalisierung (i18n): Vollständige Prüfung und Übersetzungsabschluss über die Benutzeroberfläche, den F3-Viewer und den F4-Editor, wodurch die Lokalisierung von Mediaplayern und Vorschaukomponenten erheblich verbessert wird 
- F3-Viewer-Optimierungen: Verbesserte Handhabung externer Links und Suchumlauflogik im Fallback-EPUB-Reader (SimpleEpubPanel); Die PDF-Viewer-Symbolleiste wurde optimiert, indem überflüssige Rotationsschaltflächen entfernt wurden

### 1.4.7 (16.08.2026)

- Verbesserungen des Media Players: Deutlich verbesserte Benutzeroberfläche, Benutzerfreundlichkeit und Stabilität der integrierten Audio- und Videoplayer 
- Build-System-Refactoring: Env-Flag `BUILD_EPUB` in `BUILD_WEBENGINE` umbenannt, um das Verpackungsverhalten genau wiederzugeben 
– Korrektur von Verpackungsabhängigkeiten: sichergestellt, dass `ebooklib` immer in einfachen DMG-Builds für den Fallback-EPUB-Reader gebündelt ist

### 1.4.6 (16.08.2026)

- Leichter EPUB-Reader (SimpleEpubPanel): Ein WebEngine-freier Fallback-EPUB-Reader mit Kapitelnavigation und -suche sowie ein `--epub-reader` CLI-Argument zum Überschreiben der Standard-Engine hinzugefügt 
- Kaskadierende Breadcrumb-Menüs: Das Breadcrumb-Dropdown wurde in ein einspaltiges, scrollbares Layout mit unendlich vielen kaskadierenden Untermenüs umgestaltet, wodurch Überlappungs- und Mausklick-Blockaden behoben wurden

### 1.4.5 (15.08.2026)

- Erweiterter Code-Viewer (F3): Syntaxhervorhebung (Pygments), Live-Datei-Tailing, Regex-Suche und Zeilennummern hinzugefügt 
- Erweiterter Code-Editor (F4): Dynamische Codierung/EOL-Konvertierung, atomar sicheres Speichern, intelligente Einrückung und Suchen/Ersetzen hinzugefügt 
- Globales externes Drag & Drop: Ziehen Sie Dateien, einschließlich tief verschachtelter Archivinhalte, nahtlos direkt auf den macOS-Desktop oder auf Editoren von Drittanbietern (z. B. VSCode).

### 1.4.4 (15.08.2026)

- Verbesserungen der Typografie: Erhöhte Schriftgrößen in Menüs, Schaltflächen, Tooltips und Einstellungsdialogen für bessere Lesbarkeit 
- Korrekturen zur Größenänderung des Cursors: Fehlende Mauszeiger zur Größenänderung an Fensterrändern, Splittern und Tabellenspaltenüberschriften wurden wiederhergestellt 
- Korrekturen an der macOS-Benutzeroberfläche: Schwarze Auswahlhintergründe in Dropdown-Menüs behoben und Titelüberläufe in Gruppenfeldern behoben

### 1.4.3 (14.08.2026)

- Neue native macOS-Benutzeroberfläche (Aqua Blue Theme): als neues Standarddesign eingeführt, mit interaktiver Breadcrumb-Navigation (mit kaskadierendem Unterordner-Drilldown), Speicheranzeige im Mac-Stil (behobener TB-Überlauf) und abgerundeter Kapselauswahl 
- Tiefenpolierte Benutzeroberfläche: verfeinertes Layout der Schaltflächen zum Schließen von Tabs, korrigierte Überlappung der Eingabeaufforderung und einheitliche Symbolleisten-Hintergründe, Trennwände und Panel-Ränder für alle Themen 
- i18n- und App-Upgrade: Prüfung der vollständigen i18n-Abdeckung des Projekts abgeschlossen; AList/OpenList-Freigabe-API-Unterstützung im automatischen Update-Modul hinzugefügt

### 1.4.2 (13.08.2026)

- Verbesserter AI-Semantikfilter: Unterstützt das Parsen häufigerer Erweiterungen und Pluralformen und ist vollständig in i18n integriert 
- Semantische Suche UX: Wartecursor durch QProgressBar ersetzt und Verhalten der Eingabetaste für Vervollständigungen verbessert 
- Core Semantic Parsing: Verbesserte Zieltyperkennung und Schlüsselwortentfernung für eine genauere Suche in natürlicher Sprache

### 1.4.1 (13.08.2026)

- Umfassende Überprüfung und Umgestaltung der Codebasis (Batches A-D) 
- Sicherheitsverbesserungen: Potenzielle Path-Traversal- und Zugriffsschwachstellen wurden behoben 
- Parallelität und Leistung: Verbesserte Hintergrund-Thread-Sicherheit und Ausführungseffizienz 
- Architektur: Verbesserte Stabilität und Ressourcenverwaltung in Kernkomponenten

### 1.4.0 (12.08.2026)

- Umfassende VFS-Netzwerkkorrekturen: Multi-Codierungsunterstützung, Protokolltreiber, verkettete Archivmontage und Konfliktlösung 
- Erweitertes App-Upgrade-Modul: SSL-Überprüfungskorrekturen, DMG-Download-Validierung und UI-Integration 
- Versionshinweis-Benutzeroberfläche: Vollständigen Versionsverlauf bei automatischen Updates anzeigen

### 1.3.9 (12.08.2026)

- Integrierter EPUB-Reader hinzugefügt (F3-Schnellansicht) 
- Mechanismus zur Erkennung von App-Upgrades implementiert 
– Das Einfrieren des VFS-Workers während der Lösung von Dateikonflikten wurde behoben

### 1.3.8 (08.08.2026)

- Verfeinerung der Benutzeroberfläche der Baumansicht 
- Überarbeitete fsspec-Netzwerkintegration 
- Verbesserte Handhabung ungültiger Dateizeichen

### 1.3.7 (06.08.2026)

- Netzwerk-VFS-Architektur: Überarbeitung von Netzwerkdateisystemen (FTP/WebDAV/SMB) mit `fsspec`, Implementierung von asynchronem `VfsTableModel`, Streaming `StreamCopyWorker`, Remote-Dateioperationen (mkdir/umbenennen/löschen/überschreiben) und F3/F4-Remote-Anzeige/Bearbeitung 
- Taskleiste und Hotkeys: Unterstützt das Minimieren in die Taskleiste, eine globale Verknüpfung (`Option+Cmd+H`), das Umschalten des macOS Dock-Symbols und die Integration nativer Vorlagensymbole 
- LLM-Konfiguration: Einführung der Ressource `default_llm.xml` und Singleton für semantische AI-Filterung und Optionen-Benutzeroberfläche 
- Navigationsverbesserungen: Unterstützt PageUp-/PageDown-/Home-/Ende-/Fn-Navigationsverknüpfungen in Dateifenstern und Hotlist-Popups 
- Internationalisierung: Umschließen Sie alle VFS-Fehlermeldungen, Schnellansicht-Panel-Beschriftungen und Taskleistenmenüzeichenfolgen mit i18n-Übersetzungskatalogen

### 1.3.6 (04.08.2026)

- Netzwerk-VFS-Verbesserungen: Automatische UTF-8/GBK-Erkennung, dynamische Aktualisierung der Makefile-Kodierung, Fallback-Behandlung und Socket-Reset für FTP hinzufügen; Zeitüberschreitung beheben und Desynchronisation antworten 
- WebDAV- und SMB-Korrekturen: WebDAV/SMB-Root-Pfad-Stripping, Last_error-Weitergabe, Verbindungszuverlässigkeit, VFS-Symbole und Registerkartentitelanzeigen behoben 
- Miniaturansicht-Navigation: Implementieren Sie eine reibungslose 2D-Rasterpfeilnavigation für die Miniaturansicht 
- i18n & Codequalität: Korrigieren Sie beschädigte Close-Tab-Übersetzungen in zh_CN/zh_TW-Katalogen und schließen Sie die Prüfung der Codebasisoptimierung ab

### 1.3.5 (03.08.2026)

- Schnellansichtsbereich: Implementieren Sie die Schnellansichtsfunktion (`cm_QuickView`, `Cmd+Q`/`Ctrl+Q`), die Multiformat-Vorschauen, Fallback-Dateieigenschaften, symmetrisches Umdrehen, Menüintegration anzeigen und vollständiges i18n unterstützt 
- Schnellansicht-Widgets: Fügen Sie `QuickViewContainer` und `QuickViewPropertiesWidget` hinzu, die in FilePanel integriert sind 
- Polierte Benutzeroberfläche: Behebung von Problemen mit der Ausrichtung von Tab-Headern und dem Quetschen von Optionsdialogseiten im Light-Theme

### 1.3.4 (02.08.2026)

- Dateibedienfeld-Benutzeroberfläche: Hinzufügen von Umschalt+Bild-nach-oben/Umschalt+Bild-nach-unten-Stapelauswahl in Dateibedienfeldansichten 
- Dateioperationen: Fehler beim Kopieren mit F5 und beim Verschieben von Dateien/Verzeichnissen mit F6 behoben 
- Erstellen von Skripten: Legen Sie genaue Zertifikatidentitätsnamen fest, fügen Sie Zeitstempel zum Codesign hinzu und behandeln Sie den Status „Ungültig bei Beglaubigung“ ordnungsgemäß

### 1.3.3 (01.08.2026)

- Transfer Engine: Berechnen Sie die genaue Echtzeit-Übertragungsgeschwindigkeit und ETA in ProcessTransferWorker 
- Berechtigungen und Sandbox: Trennen Sie die macOS-Sandbox-Prüfungen vom Erkennungsablauf für den vollständigen Festplattenzugriff 
- Build-Skripte: Aktualisieren Sie die Build-Skript-Konfiguration für 1.3.3 DMG-signierte Builds

### 1.3.2 (01.08.2026)

- Subprocess Transfer Worker: Einfrierungs-/Startfehler im Nuitka-Standalone-App-Store-Bundle-Modus behoben 
- Agentenfähigkeiten: i18n-Vollständigkeitsprüfung zur Codeüberprüfung-Optimierungsprüfung hinzufügen

### 1.3.1 (01.08.2026)

- macOS Sandbox: Behebung des falschen Status „Vollständiger Festplattenzugriff gewährt“, der durch die `os.access`-Prüfung verursacht wurde 
- Gleichzeitige Aufgaben: Zustandsübersprechen für gleichzeitige Hintergrundoperationen auflösen 
- i18n: Chinesische Übersetzung für Stapel-Kontrollkästchen im permanenten Löschdialog hinzufügen 
- Agentenfähigkeiten: Hinzufügen und Aktualisieren der Auditfähigkeit zur Optimierung der Codeüberprüfung

### 1.3.0 (01.08.2026)

- Prozessisolierte Übertragungs-Engine: Implementieren Sie ProcessTransferWorker und ProcessIOEngine, um E/A zum Kopieren/Verschieben von Dateien vom UI-Thread auszulagern 
- Übertragungsleistung und Reaktionsfähigkeit: 10-Hz-IPC-Ratenbegrenzung, adaptive Pufferung und macOS `F_NOCACHE`-Optimierung zur Vermeidung von GUI-Rucklern 
- Code-Audit und -Härtung: 4-Phasen-Refactoring, einschließlich Parallelitäts-Mutex-Sperren, Sicherheitshärtung und Architekturbereinigungen 
- Korrekturen an der Benutzeroberfläche: Behebung des Shiboken C++-Löschfehlers, des horizontalen Panel-Modus-Layouts und der Statusanzeigesignale für Hintergrundaufgaben

### 1.2.0 (30.07.2026)

- Implementieren Sie einen globalen I/O-Prozesspool (IoWorkerPool), um blockierende Datei-I/O-Vorgänge zu isolieren und ein Einfrieren der GUI zu verhindern 
- Versionierung konfigurieren: app_version auf XML-Root-Knoten lesen/schreiben und automatische Migrations-Runner-Registrierung hinzufügen 
- Drag & Drop / Zwischenablage: Integrieren Sie die native macOS Finder Bridge, gefederte Ordner und die Zwischenablage-Statusmaschine 
- Pfaderweiterung: Gemeinsames Dienstprogramm `expand_path` hinzufügen, das `~`, `$VAR`, `%VAR%` und `%COMMANDER_PATH%` unterstützt. 
- Hotlist: Implementieren Sie den eigenständigen HotlistConfig-Singleton und die Standard-Hotlist-Konfiguration

### 1.1.0 (29.07.2026)

- Korrigieren Sie die Eintragsreihenfolge der Versionshinweise, um eine umgekehrte chronologische Sortierung unterhalb der Kopfzeile der Versionshinweise sicherzustellen 
– Korrektur des Versionsmanager-Skripts zur Unterstützung des XML-Knotens „System/LastVersion“ in „default_config.xml“. 

- Hotkeys: Fügen Sie die Standardverknüpfungen Meta+Tab und Meta+Umschalt+Tab für die Tab-Navigation hinzu 
- Lieblingsregisterkarten: Automatische Migration und Bereinigung für ältere Lieblingsregisterkarten aus der Hauptkonfiguration hinzufügen 
- Datei-Viewer: Optimieren Sie die Leistung beim Laden großer Dateien und die Speichernutzung

### 1.0.1 (22.07.2026)

> Fehler bei der F3-Textvorschau in App Store-Sandbox-Umgebungen behoben

### 1.0.0 (18.07.2026)

> Erste Implementierung der Python-Portierung von TotalCommander.