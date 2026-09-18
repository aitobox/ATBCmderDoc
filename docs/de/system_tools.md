# Kapitel 7: System-Tools & Wartung

Ein professioneller Dateimanager arbeitet nicht im luftleeren Raum – er ist die zentrale Schaltzentrale für Ihren Speicher, Arbeitsspeicher und Ihre Betriebssystemressourcen. Während das orthodoxe Dual-Panel-Dateimanagement beim Organisieren, Verschieben und Synchronisieren von Verzeichnishierarchien glänzt, stehen Power-User, Entwickler und Systemadministratoren häufig vor Herausforderungen auf Systemebene: das Lokalisieren versteckter Verzeichnisse, die unbemerkt 50 GB Festplattenspeicher belegen; das Identifizieren eines Amok laufenden Hintergrundprozesses, der CPU-Kerne auslastet; das Bereinigen gigabytelanger verwaister Entwickler-Caches und Build-Artefakte sowie das vollständige Deinstallieren von macOS-Anwendungen, ohne verwaiste Einstellungsdateien, Launch-Daemons oder Application-Support-Ordner über `~/Library/` verstreut zurückzulassen.

ATBCmder integriert vier spezialisierte Systemwartungs- und Diagnose-Tools direkt in das Menü **Werkzeuge** (Tools). Angetrieben von einem asynchronen, nativen Überwachungs-Daemon arbeiten diese Werkzeuge nahtlos neben Ihren Dateipanels – ohne die Benutzeroberfläche zu blockieren oder überladene Dienstprogramme von Drittanbietern zu erfordern.

---

## 1. Visueller Schnellstart: System-Tools & Status-HUD

ATBCmder unterteilt die Systemwartung in vier zentrale operative Instrumente, begleitet von einer stets sichtbaren Symbolleisten-Überwachungskapsel:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       ATBCMDER SYSTEM TOOLS SUITE                                      │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  [1] Status Capsule HUD & Popover       [2] System Status & Diagnostics (⌘⇧M)                         │
│      • Real-time CPU, RAM, and Network      • Per-core utilization bars, full process table            │
│      • Color-coded threshold styling        • Search/filter processes, send SIGTERM/SIGKILL            │
│      • Click for multi-metric popover       • Disk filesystem capacity and network interface graphs   │
│                                                                                                        │
│  [3] Disk Usage Analyzer (⌘⇧D)          [4] System Cleaner (⌘⇧C)                                      │
│      • Multi-threaded directory scanner     • Two-stage safe cleaner: scan first, review, then clean   │
│      • Interactive squarified treemap       • 6 categories: caches, logs, Xcode, dev tools, trash      │
│      • Breadcrumb drill-down navigation     • 3 risk levels (Safe, Warning, Danger) + Whitelist        │
│                                                                                                        │
│  [5] Application Uninstaller (⌘⇧U)                                                                     │
│      • Complete removal of .app bundles and deep remnant files                                         │
│      • Cleans Application Support, Preferences, Caches, LaunchAgents, and Containers                   │
│      • Dual mode: Complete Uninstall vs. Remnants Only (clean up previously deleted apps)              │
│                                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Spickzettel für Dual-Matrix-System-Tools

| Werkzeug / Aktion | macOS-Kurzbefehl | Klassische Commander-Taste | Befehls-ID | Menüpfad |
| :--- | :--- | :--- | :--- | :--- |
| **Systemstatus-Panel** | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` | **Werkzeuge ➔ Systemstatus...** |
| **Festplattenbelegungsanalyse** | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` | **Werkzeuge ➔ Festplattenanalyse...** |
| **Systemreiniger** | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` | **Werkzeuge ➔ Systemreiniger...** |
| **Anwendungs-Deinstallierer** | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` | **Werkzeuge ➔ Anwendung deinstallieren...** |
| **Statuskapsel umschalten** | Einstellungen ➔ Allgemein | — | *(Einstellungen)* | **Konfiguration ➔ Optionen ➔ Allgemein** |

---

## 2. Statuskapsel-HUD der Symbolleiste & Live-Popover

ATBCmder verfügt über eine integrierte **Systemstatuskapsel**, die direkt auf der rechten Seite der Hauptsymbolleiste eingebettet ist. Sie bietet einen unmittelbaren Überblick über den Systemzustand, ohne dass Sie zur Aktivitätsanzeige wechseln oder ein separates Terminal öffnen müssen.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Left Panel Tabs]                   [Right Panel Tabs]          [ CPU 18% | RAM 44% | ↓1.2M ↑340K ]│
└───────────────────────────────────────────────────────────────────────────┬────────────┘
                                                                            │ Click Capsule
                                                                            ▼
                                                ┌───────────────────────────────────────┐
                                                │ SYSTEM METRICS SUMMARY                │
                                                ├───────────────────────────────────────┤
                                                │ CPU Usage:     [████░░░░░░░░░░]   18% │
                                                │ Memory:        [████████░░░░░░]   44% │
                                                │ GPU Load:      [██░░░░░░░░░░░░]   12% │
                                                │ Battery:       [████████████░░]   88% │
                                                ├───────────────────────────────────────┤
                                                │ Storage:                              │
                                                │  Macintosh HD:  312.4 GB / 994.6 GB   │
                                                │  External SSD:  842.1 GB / 2.0 TB     │
                                                ├───────────────────────────────────────┤
                                                │ Top Processes:                        │
                                                │  • ATBCmder         PID: 54102  CPU: 2%│
                                                │  • WindowServer     PID: 284    CPU: 8%│
                                                │  • Xcode            PID: 88120  CPU: 4%│
                                                ├───────────────────────────────────────┤
                                                │ [ Open Full System Monitor (⌘⇧M) ➔ ] │
                                                └───────────────────────────────────────┘
```

### 2.1 Kapselkomponenten & visuelle Gestaltung

Die Statuskapsel (`320px` breit) zeigt drei Echtzeit-Telemetriemetriken an, die einmal pro Sekunde aktualisiert werden:

1. **CPU-Auslastung**: Prozentualer Gesamtprozessorverbrauch in Echtzeit mit dynamischer Farbcodierung:
   - **Normal (< 75 %)**: Akzentblau / Design-Vordergrundfarbe.
   - **Erhöht (75 % – 90 %)**: Warnorange.
   - **Kritisch (> 90 %)**: Alarmrot.
2. **Speicherauslastung (RAM)**: Aktueller aktiver und reservierter Speicherdruck, ausgedrückt als Prozentsatz des physischen Arbeitsspeichers.
3. **Netzwerkdurchsatz**: Gesamte Upload- und Download-Geschwindigkeiten aller aktiven Netzwerkadapter in Echtzeit im kompakten Format (z. B. `↓2.4 MB/s ↑512 KB/s`).

### 2.2 Interaktives Popover (`StatusPopup`)

Ein Klick auf eine beliebige Stelle der Statuskapsel öffnet ein nicht-modales, schwebendes **Status-Popover**:

- **Hardware-Telemetrie**: Kombinierte Prozentwerte für CPU-, Arbeitsspeicher-, GPU- und Batteriestatus (einschließlich Ladestand in Prozent und Ladestatus).
- **Dateisystem-Mounts**: Listet alle gemounteten lokalen APFS-Container und externen Laufwerke mit Balkenanzeigen für freien Speicherplatz und Gesamtkapazität auf.
- **Top-5-Prozesse**: Hebt die fünf ressourcenintensivsten Prozesse nach CPU-Anteil und Speicherbedarf hervor.
- **Vertiefungs-Schaltfläche**: Klicken Sie auf **„Vollständigen Systemmonitor öffnen“** (oder drücken Sie `⌘⇧M`), um das umfassende Diagnosefenster aufzurufen.

### 2.3 Konfiguration der Kapselsichtbarkeit

Wenn Sie eine ablenkungsfreie Symbolleiste bevorzugen, die ausschließlich Steuerelemente zur Dateinavigation enthält:

1. Öffnen Sie die **Einstellungen** (`⌘,` / **Konfiguration ➔ Optionen...**).
2. Wählen Sie in der linken Seitenleiste **Allgemein** aus.
3. Aktivieren oder deaktivieren Sie unter **Anzeige & Layout** das Markierungsfeld:
   `[X] Systemstatuskapsel in Symbolleiste anzeigen`
4. Klicken Sie auf **Anwenden** oder **OK**. Die Kapsel wird sofort in der Hauptsymbolleiste ein- oder ausgeblendet.

---

## 3. Systemstatus & Diagnose (`cm_SystemStatus` / `⌘⇧M`)

Das Drücken von **`⌘⇧M`** (oder **`Ctrl+Shift+M`**) öffnet das vollständige **Systemstatus-Panel**. Dieses Dienstprogramm dient als integrierte Diagnosekonsole, die speziell auf Systemadministratoren, Entwickler und die Leistungsfehlersuche zugeschnitten ist.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             SYSTEM STATUS & DIAGNOSTICS                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CPU USAGE: Apple M3 Max (14 Cores)                                                     │
│ Core 01: [██████░░░░] 60%    Core 05: [██░░░░░░░░] 20%    Core 09: [███░░░░░░░] 30%    │
│ Core 02: [████░░░░░░] 40%    Core 06: [████░░░░░░] 42%    Core 10: [█░░░░░░░░░] 10%    │
│ Core 03: [████████░░] 80%    Core 07: [█░░░░░░░░░] 12%    Core 11: [░░░░░░░░░░]  5%    │
│ Core 04: [███░░░░░░░] 30%    Core 08: [██░░░░░░░░] 18%    Core 12: [░░░░░░░░░░]  4%    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ MEMORY: Total 36.0 GB  |  Used: 16.2 GB (45%)  |  App: 9.4 GB  |  Wired: 4.1 GB       │
│ SWAP:   Total 2.0 GB   |  Used: 0 MB (0%)                                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PROCESS LIST                                 Filter: [ node                     ] [x]  │
│ PID      Name             User           CPU %       Memory      Threads    Action     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ 72841    node (dev-srv)   brain          48.2%       612.4 MB    28         [ Kill ✕ ] │
│ 72910    node (esbuild)   brain          12.1%       184.2 MB    14         [ Kill ✕ ] │
│ 73104    node (lsp)       brain           1.4%        98.5 MB     8         [ Kill ✕ ] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Update Interval: [ 1.0s ▼ ]       [ Pause Monitoring ]              [ Close (Esc) ]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Diagnosefunktionen & Metrikbereiche

1. **Multi-Core-Prozessormonitor**:
   - Visualisiert die Gesamtsystemauslastung sowie die Aufteilung auf einzelne Performance- und Efficiency-Kerne (Leistungs- und Effizienzkerne).
   - Fortschrittsbalken pro Kern heben die Kernsättigung während Multithreading-Kompilierungen oder Rendering-Vorgängen hervor.
2. **Speicheraufteilung & Swap-Druck**:
   - Kategorisiert die physische Speicherbelegung in App-Speicher, reservierten Speicher (Wired Memory), komprimierten Speicher und Cache-Dateien.
   - Überwacht die Nutzung des virtuellen Auslagerungsspeichers (Swap), um festzustellen, ob Speicherlecks Festplatten-Paging verursachen.
3. **Speicher- & Mount-Übersicht**:
   - Echtzeit-Metriken zum Lese- und Schreibdurchsatz der Festplatte zusammen mit Kapazitätsdaten zu Einhängepunkten (Mount Points).
4. **Interaktiver Prozess-Manager**:
   - Sortierbare Echtzeittabelle aller laufenden System- und Benutzerprozesse.
   - **Suchen & Filtern**: Geben Sie einen beliebigen Prozessnamen oder eine PID in das Suchfeld ein, um die Ergebnisse sofort zu filtern.
   - **Prozessbeendigung**:
     - Klicken Sie auf **Beenden (Kill)** oder wählen Sie einen Prozess aus und drücken Sie `Delete` (`⌫`).
     - Ein Bestätigungsdialog bietet **Beenden (`SIGTERM`)** für ein reguläres Herunterfahren oder **Sofort beenden (`SIGKILL`)** für nicht mehr reagierende Aufgaben an.

---

## 4. Festplattenbelegungsanalyse (`cm_DiskUsageAnalyzer` / `⌘⇧D`)

Wenn der freie Speicherplatz auf einem Solid-State-Laufwerk knapp wird, kann das Aufspüren versteckter Gigabytes mühsam und zeitaufwendig sein. Standard-Dateilisten im Finder berechnen Ordnergrößen nicht automatisch, und eine manuelle Inspektion erfordert mühsames Navigieren durch verschachtelte Hierarchien.

Die **Festplattenbelegungsanalyse** (`cm_DiskUsageAnalyzer`, Tastaturkurzbefehl **`⌘⇧D`** / **`Ctrl+Shift+D`**) scannt gesamte Verzeichnisbäume asynchron über einen Multi-Thread-Scanner und visualisiert Ihren Speicher sowohl in einer traditionellen hierarchischen Baumstruktur als auch in einer interaktiven **kachelbasierten Treemap (Squarified Treemap)**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DISK USAGE ANALYZER: /Users/brainzhang                                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Path: /Users/brainzhang ➔ Developer ➔ Projects                                        │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ DIRECTORY HIERARCHY                  │ INTERACTIVE SQUARIFIED TREEMAP                  │
│ Folder Name      Size       Percent  │ ┌───────────────────────────┬─────────────────┐ │
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
│ [ Zoom Out (..) ]  [ Reveal in Dual Panel ]  [ Move to Trash (⌘⌫) ]  [ Export CSV... ]  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Wichtigste Architekturmerkmale & Fähigkeiten

- **Asynchrones Multi-Thread-Scannen**: Scannt Hunderttausende von Dateien in APFS-Containern, ohne die Hauptoberfläche von ATBCmder zu blockieren. Ein Fortschrittsbalken zeigt die pro Sekunde gescannten Verzeichnisse an.
- **Squarified-Treemap-Visualisierung**:
  - Ordner und Dateien werden als verschachtelte rechteckige Blöcke dargestellt, deren 2D-Fläche streng proportional zu ihrer Größe auf dem Datenträger ist.
  - Farben spiegeln automatisch die Verzeichnistiefe wider, sodass massive Speicherverbraucher auf einen Blick erkennbar sind.
- **Bidirektionale Synchronisation**:
  - Die Auswahl eines Elements im Verzeichnisbaum hebt den entsprechenden Block in der Treemap hervor.
  - Das Anklicken eines Rechtecks in der Treemap hebt die entsprechende Zeile in der Strukturansicht hervor und zeigt den vollständigen Dateipfad sowie die exakte Byte-Größe an.

### 4.2 Interaktive Navigation & Workflows

1. **Hineinzoomen (Drill-Down)**: Doppelklicken Sie auf eine beliebige Ordnerzeile oder einen Treemap-Block, um in dieses Unterverzeichnis zu zoomen und die Ansicht relativ zum neuen Stammverzeichnis neu zu berechnen.
2. **Herauszoomen**: Klicken Sie auf die Schaltfläche **Herauszoomen (Zoom Out)** in der Symbolleiste oder auf ein beliebiges Segment in der Breadcrumb-Leiste oben, um zu übergeordneten Verzeichnissen zurückzukehren.
3. **Im Dual-Panel inspizieren**: Klicken Sie auf **Im Dual-Panel anzeigen (Reveal in Dual Panel)**, um Ihr aktives ATBCmder-Dateipanel sofort zum ausgewählten Verzeichnis zu navigieren.
4. **Sofortige Bereinigung**: Wählen Sie einen großen, veralteten Ordner oder eine Datei aus und drücken Sie **`⌘⌫`** (oder klicken Sie auf **In den Papierkorb legen**). Das Element wird sicher in den macOS-Papierkorb verschoben, und der Scanbaum wird automatisch aktualisiert.
5. **Speicherberichte exportieren**: Klicken Sie auf **Exportieren**, um umfassende Speicherbelegungsprüfungen zu erstellen – formatiert als strukturierte CSV-Datei oder als Nur-Text-Zusammenfassung für die Speicherplanung.

---

## 5. Systemreiniger (`cm_CleanSystem` / `⌘⇧C`)

Über Monate der täglichen Nutzung hinweg sammeln sich unter macOS Gigabytes an temporären Daten an: veraltete Anwendungs-Caches, Xcode-Build-Artefakte, Downloads von Paketmanagern, verwaiste Diagnoseprotokolle und Browser-Caches. Während einige Caches Arbeitsabläufe beschleunigen, verschwenden veraltete Elemente wertvollen Hochgeschwindigkeits-SSD-Speicherplatz.

Der **Systemreiniger** (`cm_CleanSystem`, Tastaturkurzbefehl **`⌘⇧C`** / **`Ctrl+Shift+C`**) bietet ein deterministisches, zweistufiges Bereinigungswerkzeug mit unternehmensweiten Sicherheitsgarantien.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM CLEANER: DRY RUN AUDIT                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Scan System ]  Scanned: 48,192 items in 2.1s        Total Reclaimable: 34.8 GB        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CATEGORY                          ITEMS       SIZE        RISK LEVEL     SELECTION     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ [X] Application Caches            12,410      14.2 GB     Safe (Green)   [ Select All] │
│ [X] System & User Logs             4,218       1.8 GB     Safe (Green)   [ Select All] │
│ [X] Xcode Derived Data             8,940      12.4 GB     Warning (Org)  [ Select All] │
│ [ ] Homebrew & CocoaPods Caches    1,420       3.6 GB     Warning (Org)  [ Select All] │
│ [ ] Web Browser Caches            21,200       2.8 GB     Safe (Green)   [ Select All] │
│ [ ] Trash Bin Container                4       8.2 GB     Danger (Red)   [ Unselected] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Selected for Cleanup: 28.4 GB across 25,568 files                                     │
│ Whitelist: ~/.config/atbsys/whitelist (4 rules active)                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Whitelist Editor... ]      [ Export Log ]       [ Clean Selected Items (28.4 GB) ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Die zweistufige Sicherheitsarchitektur

Im Gegensatz zu leichtfertigen „Ein-Klick-Reinigern“, die Dateien stillschweigend im Hintergrund löschen, erzwingt ATBCmder ein striktes **zweistufiges Sicherheitsprotokoll**:

1. **Stufe 1: Trockenlauf-Scan & Bewertung (Dry-Run Scan & Assessment)**:
   - Der Reiniger führt eine rein lesende Analyse standardisierter Systemspeicherorte durch.
   - Berechnet exakte Dateienzahlen und Bytegrößen, ohne auch nur ein einziges Byte zu verändern oder zu löschen.
   - Gruppiert die Ergebnisse in transparente Kategorien mit expliziten Risikobewertungen.
2. **Stufe 2: Benutzergeprüfte selektive Löschung (User-Reviewed Selective Deletion)**:
   - Sie prüfen die kategorisierte Liste und wählen einzelne Elemente oder ganze Kategorien gezielt aus oder ab.
   - Ein Klick auf **„Ausgewählte Elemente bereinigen“** führt den Löschvorgang ausschließlich für die explizit markierten Ziele aus.
   - Jeder Löschvorgang wird in einem atomaren Revisionsprotokoll unter `~/Library/Preferences/atbcmder/operations.log` dokumentiert.

### 5.2 Sechs zentrale Bereinigungsbereiche

| Kategorie | Typischer Speicherort | Risikostufe | Beschreibung |
| :--- | :--- | :---: | :--- |
| **Anwendungs-Caches** | `~/Library/Caches/` | **Sicher** | Veraltete, von Desktop-Anwendungen erstellte Caches, die bei Bedarf automatisch neu generiert werden. |
| **System- & Benutzerprotokolle** | `~/Library/Logs/`, `/var/log/` | **Sicher** | Ältere Absturzberichte, Diagnose-Dumps und Software-Aktualisierungsprotokolle, die nicht mehr benötigt werden. |
| **Browser-Caches** | Safari, Chrome, Edge, Firefox | **Sicher** | Zwischengespeicherte Webseiten, Medienpuffer und Skript-Artefakte aller installierten Desktop-Browser. |
| **Xcode Derived Data** | `~/Library/Developer/Xcode/DerivedData` | **Warnung** | Temporäre Objektdateien, Modul-Caches und Indexdaten vergangener Apple-Entwickler-Builds. |
| **Paketmanager-Caches** | Homebrew, CocoaPods, NPM, Yarn | **Warnung** | Heruntergeladene Tarballs, Formel-Archive und Cache-Verzeichnisse für Abhängigkeiten. |
| **Papierkorb** | `~/.Trash`, `.Trashes` | **Gefahr** | Zuvor in den macOS-Papierkorb verschobene Elemente, die noch nicht dauerhaft gelöscht wurden. |

### 5.3 Risikostufen & Sicherheits-Whitelist

- 🟢 **Sicher (Grün / Safe)**: Temporäre Caches und verworfene Metadaten, die ohne Konfigurationsverlust oder Arbeitsablaufunterbrechung entfernt werden können.
- 🟡 **Warnung (Orange / Warning)**: Entwickler-Artefakte oder Paket-Caches. Das Löschen ist sicher, jedoch verlängern sich nachfolgende Projektkompilierungen oder Paket-Downloads, da Elemente neu geladen werden müssen.
- 🔴 **Gefahr (Rot / Danger)**: Enthält Dateien, die eine ausdrückliche Bestätigung erfordern (z. B. das endgültige Entleeren des Papierkorbs).
- **Benutzerdefinierte Whitelist-Regeln**:
  - Fügen Sie Pfade, Dateierweiterungen oder Ordnernamen, die ATBCmder **niemals** antasten darf, der Datei `~/.config/atbsys/whitelist` hinzu.
  - Integrierte Schutzregeln verhindern automatisch das Scannen kritischer macOS-Betriebssystemdateien, Benutzer-Schlüsselbund-Verzeichnisse (Keychains) sowie Offline-Synchronisierungsordner von Cloud-Speicherdiensten.

---

## 6. Anwendungs-Deinstallierer (`cm_UninstallApp` / `⌘⇧U`)

Unter macOS entfernt das Ziehen einer Anwendung aus dem Ordner `/Applications` in den Papierkorb lediglich das `.app`-Bundle selbst. Moderne Programme verteilen häufig Hunderte Hilfsdateien über Ihr gesamtes Laufwerk: Voreinstellungs-Plists, Application-Support-Datenbanken, Hintergrund-Launch-Agents, Sandbox-Container und zwischengespeicherte Medien. Im Laufe der Zeit verbrauchen diese verwaisten Überreste Gigabytes an Speicherplatz und können unnötige Hintergrundprozesse beim Anmelden hinterlassen.

Der **Anwendungs-Deinstallierer** (`cm_UninstallApp`, Tastaturkurzbefehl **`⌘⇧U`** / **`Ctrl+Shift+U`**) führt einen tiefgehenden Abhängigkeitsscan durch, um Anwendungen samt allen zugehörigen Überresten vollständig zu beseitigen.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             APPLICATION DEEP UNINSTALLER                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Filter: Docker                     ]  Found: 142 Applications (Total: 48.2 GB)       │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ INSTALLED APPLICATIONS               │ ASSOCIATED REMNANTS & SUPPORT FILES             │
│ App Name          Version    Size    │ File Path / Component               Size        │
│ ──────────────────────────────────── │ ─────────────────────────────────────────────── │
│ [X] Docker.app    4.28.0     1.8 GB  │ [X] /Applications/Docker.app        1.8 GB (.app│
│ [ ] Figma.app     116.15     240 MB  │ [X] ~/Library/Application Support/Docker 14.2 GB│
│ [ ] Slack.app     4.36.0     310 MB  │ [X] ~/Library/Caches/com.docker.docker   2.1 GB │
│ [ ] Visual Studio 1.87.0     450 MB  │ [X] ~/Library/Preferences/com.docker...  12 KB  │
│ [ ] Xcode.app     15.3      12.4 GB  │ [X] ~/Library/LaunchAgents/com.docker...  4 KB  │
│                                      │ [X] ~/Library/Containers/com.docker...  380 MB  │
├──────────────────────────────────────┴─────────────────────────────────────────────────┤
│ Mode: (•) Complete Uninstall (.app + remnants)     ( ) Remnants Only (clean orphans)   │
│ Total Selected for Removal: 18.48 GB across 6 items                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Refresh Applications ]       [ Cancel ]              [ Uninstall Application (18.5G)│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Fundorte für Anwendungsüberreste

Beim Scannen nach Anwendungskomponenten durchsucht ATBCmder die folgenden Standard-Subsysteme von macOS unter Verwendung eines exakten Abgleichs der Bundle-ID (Bundle Identifier):

1. **Anwendungs-Bundle (Application Bundle)**: `/Applications/<Name>.app` und `~/Applications/<Name>.app`.
2. **Application Support**: `~/Library/Application Support/<Name>` und `<BundleID>`.
3. **Anwendungs-Caches**: `~/Library/Caches/<BundleID>`.
4. **Einstellungen & Voreinstellungen (Preferences & Defaults)**: `~/Library/Preferences/<BundleID>.plist`.
5. **Gespeicherter Programmzustand (Saved Application State)**: `~/Library/Saved Application State/<BundleID>.savedState`.
6. **Launch-Daemons & Agents**: `~/Library/LaunchAgents/<BundleID>.plist`.
7. **Sandbox-Container**: `~/Library/Containers/<BundleID>/` und `~/Library/Group Containers/`.
8. **Anwendungsprotokolle (Logs)**: `~/Library/Logs/<Name>/`.

### 6.2 Zwei Betriebsmodi

- **Vollständige Deinstallation (Standard / Complete Uninstall)**:
  - Vorgesehen zum Entfernen einer derzeit auf Ihrem Mac installierten Anwendung.
  - Löscht sowohl das ausführbare `.app`-Bundle aus `/Applications` als auch alle zugehörigen Hilfs- und Supportdateien in einer einzigen atomaren Aktion.
- **Nur Überreste (Remnants Only)**:
  - Dient dem Bereinigen verwaister Dateien von Anwendungen, die zuvor manuell über den Finder oder Hilfsprogramme von Drittanbietern gelöscht wurden.
  - Durchsucht `~/Library/` nach verwaisten Support-Ordnern, deren übergeordnetes `.app`-Bundle auf dem System nicht mehr existiert.

### 6.3 Apple-Systemintegrität & Sicherheitsleitplanken

Um eine versehentliche Destabilisierung des Systems zu verhindern:

- **Schutz von System-Apps**: Integrierte macOS-Systemprogramme (Safari, Finder, Vorschau, Musik, Systemeinstellungen usw.) sind durch ein schreibgeschütztes Schlosssymbol geschützt und können nicht deinstalliert werden.
- **Erkennung laufender Prozesse**: Wenn eine Anwendung oder ihr Hilfs-Daemon derzeit aktiv ist, fordert ATBCmder Sie auf, das Programm ordnungsgemäß zu beenden, bevor die Deinstallation fortgesetzt wird.
- **Papierkorb-Zuerst-Protokoll (Trash-First)**: Alle deinstallierten Elemente werden standardmäßig in den macOS-Papierkorb verschoben, anstatt sofort unwiderruflich von der Festplatte gelöscht zu werden. Dies ermöglicht bei Bedarf eine vollständige Wiederherstellung.

---

## 7. System- & Wartungshinweise

> [!NOTE]
> **Minimaler Systemressourcen-Overhead**  
> Der Hintergrund-Statusüberwachungs-Daemon wurde in nativem, kompiliertem Maschinencode entwickelt und arbeitet mit einem Abfrageintervall von 1,0 Sekunden. Während des aktiven Durchsuchens von Dateien verbraucht er weniger als 0,1 % CPU-Leistung und setzt die Abfragen automatisch aus, wenn ATBCmder minimiert oder ausgeblendet ist.

> [!TIP]
> **Kombination der Festplattenanalyse mit der flachen Zweigansicht (Branch View)**  
> Wenn die Festplattenbelegungsanalyse ein Verzeichnis mit Tausenden verstreuter temporärer Dateien meldet, wählen Sie dieses Verzeichnis aus und klicken Sie auf **Im Dual-Panel anzeigen**. Drücken Sie anschließend **`Cmd+B`** (`cm_DirBranch`), um den gesamten verschachtelten Baum in einer einzigen flachen Listenansicht darzustellen, in der Sie Elemente mit Tastaturpräzision sortieren, auswählen und stapelweise löschen können.

> [!IMPORTANT]
> **Reinigungsauswahl vor dem Bestätigen stets prüfen**  
> Obwohl der Systemreiniger Caches als **Sicher (Grün)** einstuft, können einige Entwickler-Tools (wie Xcode DerivedData oder lokale Docker-Volumes) beim nächsten Projektstart zusätzliche Zeit zum Neukompilieren oder erneuten Herunterladen benötigen. Überprüfen Sie die ausgewählten Kategorien, um sicherzustellen, dass Sie keine Caches für einen aktiven Sprint löschen.

> [!CAUTION]
> **Sofortiges Beenden von Systemprozessen erzwingen (`SIGKILL`)**  
> Im Prozess-Manager des Systemstatus stoppt das Senden von `SIGKILL` (Sofort beenden) den Zielprozess unmittelbar, ohne geöffnete Dateipuffer zu leeren oder Dokumentzustände zu sichern. Versuchen Sie stets zuerst eine reguläre Beendigung über `SIGTERM`.

> [!WARNING]
> **Entfernen von App-Sandbox-Containern**  
> Beim Deinstallieren von Programmen aus dem Mac App Store enthalten die unter `~/Library/Containers/<BundleID>` gespeicherten Hilfsdateien häufig Sandbox-Dokumentdatenbanken. Stellen Sie sicher, dass Sie alle wichtigen lokalen Projektdateien exportiert haben, bevor Sie das Löschen von Containern bestätigen.

---

## 8. Master-Dual-Matrix-Referenztabelle für System-Tools

| Kategorie | Aktionsbeschreibung | macOS-Kurzbefehl | Klassische Commander-Taste | Befehls-ID |
| :--- | :--- | :--- | :--- | :--- |
| **System-Monitor** | Vollständiges Systemdiagnose-Panel öffnen | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` |
| **System-Monitor** | Leichtgewichtiges Status-Popover öffnen | Klick auf Symbolleistenkapsel | — | *(UI-Aktion)* |
| **System-Monitor** | Prozess-Manager-Liste filtern | `Cmd+F` (im Panel) | `F7` | — |
| **System-Monitor** | Prozess beenden (`SIGTERM`) | `Delete` / `⌫` | `Delete` | — |
| **System-Monitor** | Prozess sofort beenden (`SIGKILL`) | `Shift+Delete` / `⇧⌫` | `Shift+Delete` | — |
| **Festplattenanalyse** | Festplattenbelegungsanalyse-Dialog öffnen | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` |
| **Festplattenanalyse** | In ausgewählten Ordner hineinzoomen (Drill-Down) | `Enter` / `Return` | `Enter` | — |
| **Festplattenanalyse** | Zum übergeordneten Verzeichnis herauszoomen | `Backspace` / `⌫` | `Backspace` | — |
| **Festplattenanalyse** | Markiertes Element in den Papierkorb legen | `Cmd+Delete` / `⌘⌫` | `F8` / `Delete` | — |
| **Festplattenanalyse** | Ausgewähltes Element im Dual-Panel anzeigen | `Cmd+Return` / `⌘⏎` | `Ctrl+Enter` | — |
| **Systemreiniger** | Dialog des sicheren Systemreinigers öffnen | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` |
| **Systemreiniger** | Schreibgeschützten Trockenlauf-Scan starten | `Cmd+R` / `⌘R` | `Ctrl+R` | — |
| **Systemreiniger** | Kategorieauswahl umschalten | `Space` | `Space` | — |
| **Anwendungs-Deinstallierer** | Anwendungs-Deinstallierer öffnen | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` |
| **Anwendungs-Deinstallierer** | In den Modus „Nur Überreste“ wechseln | `Cmd+2` / `⌘2` | `Alt+2` | — |
| **Einstellungen** | Statuskapsel-HUD in Symbolleiste ein-/ausblenden | Einstellungen ➔ Allgemein | — | *(Konfiguration)* |

---

<div align="center">
  <p>Bereit, Tastaturkurzbefehle, Panelansichten und Anwendungsverhalten anzupassen?</p>
  <p><strong><a href="preferences_and_customization.md">Weiter zu Kapitel 8: Einstellungen & Anpassung &rarr;</a></strong></p>
</div>
