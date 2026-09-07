# Kapitel 1: Grundlagen & macOS-Einrichtung

Willkommen bei **ATBCmder**! ATBCmder wurde nativ für macOS 12+ auf Apple Silicon (M1/M2/M3/M4, ARM64-Architektur; Intel x86_64 wird derzeit nicht unterstützt) entwickelt und bringt die unübertroffene Geschwindigkeit, Tastaturagilität und Präzision der herkömmlichen Dual-Panel-Dateiverwaltung auf den Mac. 

Dieses Kapitel führt Sie durch die grundlegende Dual-Panel-Philosophie, beschreibt alle wichtigen Meilensteine ​​der Benutzeroberfläche, führt Sie durch das Onboarding von macOS App Sandbox-Berechtigungen und stellt die wesentlichen Systemkonfigurationen bereit, die für ein nahtloses Erlebnis erforderlich sind. 

---

## 1. Visueller Schnellstart: Die Dual-Panel-Philosophie

Wenn Sie macOS Finder verwendet haben, sind Sie es gewohnt, mehrere überlappende Fenster zu öffnen, Dateien über überfüllte Desktops zu ziehen und zu hoffen, dass die Dateien im vorgesehenen Zielordner landen und nicht in einem versehentlich angrenzenden Unterordner. 

ATBCmder ersetzt diese Reibung durch das bewährte **Orthodox File Manager (OFM)**-Paradigma: zwei unabhängige, komplementäre Verzeichnisfenster, die nebeneinander platziert sind. 

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

### Das aktive (Quelle) vs. inaktive (Ziel) Modell

In ATBCmder müssen Sie sich nie fragen, wo eine Operation wirksam wird: 

1. **Das aktive Panel (Quelle)**: 
– Dies ist das Bedienfeld, in dem sich derzeit Ihr Tastaturfokus und Ihr Cursor befinden. 
– Jede Auswahl, Navigation oder Aktion, die Sie ausführen, zielt direkt auf dieses Panel ab. 

- **Visueller Hinweis**: Das aktive Bedienfeld verfügt über einen markanten Fokusring (Akzentfarbe des MacOS-Systems), hervorgehobenen Tab-Text und eine deutliche aktive Cursor-Hervorhebung auf dem aktuell fokussierten Element. 

2. **Das inaktive Panel (Ziel)**: 
- Dies ist das gegenüberliegende Panel. Es bleibt vollständig sichtbar und zeigt eine unabhängige Ordnerhierarchie an. 
– Das inaktive Panel fungiert als **automatisches Ziel** für Dateivorgänge, die im aktiven Panel initiiert werden. 

- **Visueller Hinweis**: Das inaktive Bedienfeld zeigt einen gedämpften Rand, leicht abgeblendeten Text und gedämpfte Tab-Titel an.

### Richtungsoperationen: Immer Quelle ➔ Ziel

Wenn Sie einen Vorgang in ATBCmder starten, versteht die Anwendung automatisch die Richtung: 

- **Kopieren (`F5` / `Cmd+C` ➔ `Cmd+V`)**: Kopiert ausgewählte Dateien aus dem Bereich „Aktiv (Quelle)“ direkt in das Verzeichnis, das derzeit im Bereich „Inaktiv (Ziel)“ angezeigt wird. 
- **Verschieben (`F6` / `Cmd+C` ➔ `Opt+Cmd+V`)**: Verschiebt ausgewählte Dateien aus dem aktiven Bereich in den inaktiven Bereich, ohne dass das Zielverzeichnis eingegeben oder gesucht werden muss. 
- **Verzeichnissynchronisierung (`Shift+F12` / `cm_SyncDirs`)**: Vergleicht das Verzeichnis im aktiven Bereich mit dem Verzeichnis im inaktiven Bereich. 

> [!TIP] 
> **Kein Drag-and-Drop-Ratespiel erforderlich**: Sie müssen Elemente nicht über Bildschirmgrenzen ziehen. Wählen Sie einfach im aktiven Bereich aus, was Sie möchten, drücken Sie `F5` (Kopieren) oder `F6` (Verschieben), drücken Sie `Enter`, um die Eingabeaufforderung zu bestätigen, und ATBCmder überträgt die Dateien sofort.

### Panel-Navigation und Fokuswechsel

| Aktion | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Fokus wechseln** | `Tab` | `Tab` | `cm_FocusSwap` | Wechselt den Tastaturfokus zwischen dem linken und dem rechten Bedienfeld (`cm_SwitchPanel`). | 
| **Fokus umkehren** | `Shift+Tab` | `Shift+Tab` | `cm_FocusSwap` | Kehrt die Fokusreihenfolge über Bedienfelder und Steuerelemente hinweg um. | 
| **Links und rechts tauschen** | `Ctrl+U` | `Ctrl+U` | `cm_Exchange` | Tauscht Verzeichnispfade zwischen dem linken und dem rechten Bereich aus, ohne Tabs oder Auswahl zu verlieren. | 
| **Verhältnis ausgleichen** | `Double-click splitter` | `Double-click splitter` | — | Setzt den Mittelteiler automatisch auf ein sauberes 50/50-Verhältnis zurück. | 

---

## 2. Interface-Anatomie- und Wahrzeichen-Tour

ATBCmder bietet eine saubere, native macOS-Schnittstelle, die mit Qt6 und PySide6 erstellt wurde, gemäß den Apple Human Interface Guidelines entwickelt wurde und gleichzeitig klassische tastaturzentrierte Commander-Workflows berücksichtigt. 

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

### [1] Native macOS-Menüleiste

Vollständig in die obere Menüleiste von macOS integriert. Alle Vorgänge, Ansichtsumschaltungen, Elektrowerkzeuge und Einstellungen sind logisch kategorisiert: 

- **Datei**: Neuer Tab, Tab schließen, Dateieigenschaften, Sandbox-Berechtigungen, Beenden. 
- **Markieren**: Gruppe auswählen (`Num+`), Gruppe auswählen (`Num-`), Auswahl umkehren (`Num*`), Alle auswählen (`Cmd+A`). 
- **Befehle**: Verzeichnis-Hotlist (`Ctrl+D`), Linke/Rechte Laufwerke (`Alt+F1/F2`), Suche (`Alt+F7`), Verzeichnisse synchronisieren (`Shift+F12`), Panels austauschen (`Ctrl+U`), Terminal (`Ctrl+J`). 
- **Anzeigen**: Umschalten des Ansichtsmodus (Kurzansicht, vollständige Spalten, Miniaturansichten, Baumansicht, flache Zweigansicht), Sichtbarkeit der Symbolleiste, horizontale Panel-Layout. 
- **Konfiguration**: Optionen/Einstellungen (`Cmd+,`), Position speichern (`cm_ConfigSavePos`), Tabs speichern.

### [2] Obere Hauptsymbolleiste

Befindet sich direkt unter der Titelleiste des Fensters. Bietet sofortigen Ein-Klick-Zugriff auf globale Befehle: 

- **Standardaktionen**: Aktualisieren (`Ctrl+R`), Schnellansicht (`Ctrl+Q`), Kopieren (`F5`), Verschieben (`F6`), Neuer Ordner (`F7`), Löschen (`F8`), Suchen (`Alt+F7`) und Optionen (`Cmd+,`). 
- **Anpassbar**: Passen Sie die Symbolgrößen an (16 bis 48 Pixel), schalten Sie die Textbeschriftungen der Schaltflächen um oder blenden Sie die Symbolleiste über das Menü **Anzeigen** → **Symbolleiste anzeigen** vollständig aus, um die Bildschirmfläche zu maximieren.

### [3] Interaktive Breadcrumb-Leiste im Finder-Stil

Die über jedem Dateibereich positionierte Breadcrumb-Pfadleiste ermöglicht blitzschnelle Hierarchiesprünge: 

- **Segmentnavigation**: Klicken Sie auf einen beliebigen übergeordneten Ordner in der Breadcrumb-Kette (z. B. klicken Sie auf `username` in `/Users/username/Projects/ATBCmder`), um direkt zu diesem Verzeichnis zu navigieren. 
- **Geschwister-Dropdowns**: Bewegen Sie den Mauszeiger oder klicken Sie auf den Chevron-Pfeil zwischen den Segmenten, um ein Dropdown-Menü anzuzeigen, in dem alle Geschwisterordner auf dieser Ebene aufgeführt sind. 
- **Segment-Kontextmenü**: Klicken Sie mit der rechten Maustaste auf ein beliebiges Breadcrumb-Segment, um schnell auf kontextbezogene Dienstprogramme zuzugreifen: 
- **In neuem Tab öffnen**: Behält Ihre aktuelle Ansicht beim Öffnen des übergeordneten Verzeichnisses in einem neuen Tab bei. 
- **Im Finder anzeigen**: Öffnet das Verzeichnis im macOS Finder (`open -R`). 
- **Pfad kopieren**: Kopiert den absoluten UNIX-Pfad des Segments in die Zwischenablage Ihres Systems. 
- **Im Terminal öffnen**: Öffnet das macOS-Terminal direkt in diesem Ordner (`open -a Terminal`). 
- **Direkte Pfadbearbeitung (`BreadcrumbLineEdit`)**: Doppelklicken Sie auf die leere Stelle rechts neben der Breadcrumb-Kette. Die Leiste wird sofort in ein bearbeitbares Textfeld umgewandelt, in das Sie einen beliebigen Pfad einfügen oder eingeben können (z. B. `/var/log`, `~/Library` oder `vfs://` Archive). Drücken Sie `Enter` zum Navigieren oder `Esc` zum Abbrechen.

### [4] Ordner-Registerkartenleiste

Jedes Panel verfügt über einen unabhängigen Satz von Registerkarten: 

- Öffnen Sie neue Tabs mit `Cmd+T` (`cm_NewTab`), schließen Sie Tabs mit `Cmd+W` (`cm_CloseTab`). 
- Per Drag-and-Drop können Sie die Registerkarten innerhalb eines Panels neu anordnen. 
- Klicken Sie mit der rechten Maustaste auf Registerkarten, um Pfade zu sperren, Titel umzubenennen, Duplikate zu schließen oder Registerkarten im gegenüberliegenden Bereich zu duplizieren.

### [5] Dual-Datei-Panels

Leistungsstarke virtualisierte Dateilisten, die Ordner mit Hunderttausenden Einträgen reibungslos und ohne Ruckeln der Benutzeroberfläche wiedergeben können: 

- Spaltensortierung: Klicken Sie auf eine beliebige Überschrift (Name, Ext, Größe, Datum, Attribute), um aufsteigend oder absteigend zu sortieren. 
- Mehrere Ansichtsmodi: Vollständige Detailansicht, Kurzrasteransicht, Miniaturansichtsgalerieansicht, Baumansicht und rekursive flache Zweigansicht (`Cmd+B`).

### [6] Mittlere Symbolleiste und ziehbarer Splitter

Die mittlere Symbolleiste befindet sich direkt zwischen dem linken und dem rechten Dateibereich und ist eine einzigartige ATBCmder-Funktion, die Dateiverwaltung mit einem Klick mit einer anpassbaren Bereichstrennung kombiniert: 

![Middle Toolbar](images/middle_toolbar.png) 

- **Schnellaktionsleiste**: Enthält vertikale Schaltflächen für allgemeine Vorgänge: 
- `cm_Copy` (Kopie) 
- `cm_Move` (Verschieben / Ausschneiden) 
- `cm_Delete` (In den Papierkorb löschen) 
- `cm_MkDir` (Neues Verzeichnis) 
- `cm_Rename` (Inline-Schnellumbenennung) 
- `cm_View` (Universal Lister) 
- `cm_Edit` (Interner Text-/Code-Editor) 
- `cm_Exchange` (Linkes und rechtes Panel vertauschen) 
- `cm_SyncDirs` (Ordnersynchronisierer) 
- `cm_FileSearch` (Erweiterte Suche) 
- **Kontinuierliches Splitter-Ziehen**: Wenn Sie Ihren Mauszeiger über die mittlere Leiste bewegen, ändert sich der Zeiger in einen horizontalen Split-Cursor (`SplitHCursor`). Klicken und horizontal ziehen, um das Breitenverhältnis zwischen den beiden Panels stufenlos anzupassen. 
- **Stilvolle Theme-Verhältnis-Voreinstellungen**: Bei Verwendung des modernen „Stylish“-Themes werden in der mittleren Leiste segmentierte Steuerelemente angezeigt, die ein sofortiges Einrasten auf die Panelbreitenverteilung **50/50**, **70/30** oder **30/70** ermöglichen. 
- **Einstellungen für die mittlere Symbolleiste**: Aktivieren oder deaktivieren Sie die mittlere Symbolleiste, passen Sie die Symbolgrößen an oder wechseln Sie zwischen modernen flachen Schaltflächen und klassischen versenkten Splittern in **Einstellungen** (`Cmd+,`) → **Symbolleisten** → **Mittlere Symbolleiste**.

### [7] Statusleiste und Laufwerksspeicheranzeige

Ganz unten im Fenster verankert: 

- **Auswahlstatistik**: Zeigt Echtzeitmetriken für das aktive Panel an: 
- Gesamtzahl der Elemente und Gesamtgröße des Ordners. 
– Anzahl der ausgewählten Elemente und kombinierte ausgewählte Bytegröße. 

- **Laufwerkspeicheranzeige**: Visuelle Anzeige der Festplattennutzung, die den Namen des aktuell bereitgestellten Volumes (z. B. `Macintosh HD`), die Gesamtkapazität, den verwendeten Speicher und den Prozentsatz des verbleibenden freien Speicherplatzes anzeigt. 

---

## 3. Schritt-für-Schritt-Anleitung: macOS-App-Sandbox- und Dateisystemberechtigungen

Modernes macOS verwendet striktes Sandboxing für die Anwendungssicherheit, um Benutzerdaten vor unbefugtem Zugriff zu schützen. Beim Ausführen von ATBCmder (insbesondere bei der Installation über den Mac App Store oder der Verteilung mit aktiviertem Sandboxing) wird die Anwendung in ihrem eigenen sicheren Containerverzeichnis isoliert: 
`~/Library/Containers/com.aitobox.atbcmder/Data` 

Standardmäßig können Sandbox-Anwendungen Dateien außerhalb ihres Containers nicht willkürlich prüfen oder ändern, es sei denn, der Benutzer erteilt ausdrücklich die Erlaubnis über die nativen offenen Bedienfelder von Apple. 

ATBCmder optimiert diesen Onboarding-Prozess mit **Sicherheitsbezogenen Lesezeichen**, sodass Sie die Berechtigung einmal erteilen und in allen zukünftigen Sitzungen dauerhaften, uneingeschränkten Zugriff genießen können.

### Grundlegendes zu sicherheitsbezogenen Lesezeichen

Wenn Sie einen Ordnerpfad mit macOS `NSOpenPanel` autorisieren: 

1. macOS gibt ein kryptografisches **Sicherheitsbezogenes Lesezeichen** (`NSURLBookmarkCreationWithSecurityScope`) aus. 
2. ATBCmder serialisiert und speichert dieses Lesezeichen in seinem Konfigurationsverzeichnis: 
`~/Library/Application Support/ATBCmder/sandbox_bookmarks.plist` 

3. Bei jedem Anwendungsstart löst ATBCmder diese Lesezeichen automatisch auf und aktiviert sie über `startAccessingSecurityScopedResource()`. 
4. Nach der Erteilung müssen Sie diese Verzeichnisse nie wieder erneut autorisieren.

### Anleitung zur Einrichtung: Verwendung von `cm_GrantFilesystemAccess`

Führen Sie die folgenden Schritte aus, um Ihre Berechtigungen beim ersten Start oder jederzeit später zu konfigurieren:

#### Schritt 1: Öffnen Sie den Permission Onboarding Assistant

Wählen Sie in der nativen Menüleiste **Datei** (oder **Hilfe**) → **Dateisystemzugriff gewähren…** oder lösen Sie den internen Befehl `cm_GrantFilesystemAccess` aus. Der Onboarding-Dialog erscheint: 

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

#### Schritt 2: Gewähren Sie Zugriff auf das Stammverzeichnis (`/`).

1. Klicken Sie auf **"Zugriff auf Stammverzeichnis gewähren (/)"**. 
2. ATBCmder ruft das native `NSOpenPanel`-Blatt von macOS auf und zeigt auf die Root-Festplatte `Macintosh HD` (`/`). 
3. Klicken Sie auf **"Zugriff gewähren"** (oder **Öffnen**). 
4. Die Schaltfläche wird sofort auf **„Stammverzeichniszugriff gewährt ✓“** aktualisiert und deaktiviert. 
5. **Was dies ermöglicht**: Die Autorisierung des Stammpfads `/` deckt automatisch alle Benutzerverzeichnisse ab (`~/Documents`, `~/Downloads`, `~/Desktop`, `~/Projects`, `/Applications` usw.), weil Sicherheitsbezogene Lesezeichen erben automatisch Abwärtsberechtigungen für alle untergeordneten Unterpfade.

#### Schritt 3: Gewähren Sie Zugriff auf externe Festplatten (`/Volumes`).

1. Klicken Sie auf **"Zugriff auf externe Festplatten (/Volumes) gewähren"**. 
2. Wenn im nativen Bereich `/Volumes` angezeigt wird, klicken Sie auf **"Zugriff gewähren"**. 
3. Die Schaltfläche wird zu **„Zugriff auf externe Festplatten gewährt ✓“** aktualisiert. 
4. **Was dies ermöglicht**: Uneingeschränkter Lese-/Schreibzugriff auf externe USB-Laufwerke, Thunderbolt-Laufwerke, SD-Karten, DMG-Disk-Image-Mounts und im Netzwerk bereitgestellte SMB/NFS/AFP-Volumes.

#### Schritt 4: Selektiver Ordner-für-Ordner-Zugriff (Alternative)

Wenn Sie ATBCmder keinen umfassenden Root-Zugriff gewähren möchten, müssen Sie nicht auf Root-Zugriff klicken: 

- Wenn Sie in einen nicht autorisierten Ordner navigieren (z. B. einen externen Ordner oder ein Projekt-Repository), erkennt ATBCmder die Berechtigungsgrenze und zeigt bei Bedarf eine Eingabeaufforderung an: 
`ATBCmder requires your permission to access: /Users/username/SecretProject` 

- Klicken Sie auf **„Zugriff auf Ordner gewähren“**, genehmigen Sie den nativen Dialog und das spezifische Verzeichnis wird dauerhaft mit einem Lesezeichen versehen.

#### Schritt 5: Vollständiger Festplattenzugriff (FDA) für geschützte Systemdaten

> [!IMPORTANT] 
> **Sandbox-Lesezeichen vs. Full Disk Access (FDA)**: 
> 
> - **Sandbox-Lesezeichen** gewähren allgemeinen Dateisystemzugriff auf Standardbenutzerordner, -dateien und externe Laufwerke. 
> - **Full Disk Access (FDA)** ist eine zusätzliche macOS Transparency, Consent, and Control (TCC)-Datenschutzberechtigung, die erforderlich ist, um sensible persönliche macOS-Daten (wie Safari-Verlauf, E-Mail-Anhänge, Nachrichten, Time Machine-Backups und System-Caches) zu prüfen. 
> 
> Wenn Sie diese geschützten Ordner verwalten müssen: 
> 
> 1. Klicken Sie im Onboarding-Dialog auf **„Einstellungen für den vollständigen Festplattenzugriff öffnen…“**. 
> 2. macOS öffnet **Systemeinstellungen** → **Datenschutz und Sicherheit** → **Vollständiger Festplattenzugriff**. 
> 3. Klicken Sie auf das Schloss oder authentifizieren Sie sich mit Touch ID/Passwort. 
> 4. Stellen Sie sicher, dass der Kippschalter neben **ATBCmder** auf **ON** steht.

### Widerrufen und Zurücksetzen von Berechtigungen

Wenn Sie Ihre Sandbox-Lesezeichen jemals zurücksetzen oder widerrufen müssen: 

1. Öffnen Sie das Konfigurationsverzeichnis von ATBCmder über das Menü **Konfiguration** → **Konfigurationsverzeichnis öffnen** (`cm_OpenConfigDirectory`). 
2. Löschen Sie die Datei `sandbox_bookmarks.plist`. 
3. Starten Sie ATBCmder neu. 
4. Um die TCC-Berechtigungen auf macOS-Systemebene zurückzusetzen, führen Sie den folgenden Befehl im macOS-Terminal aus: 
   ```bash
   tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder
   ```
 

---

## 4. Spracheinstellungen und Erscheinungsbildanpassung

ATBCmder ist für globale Arbeitsabläufe lokalisiert und lässt sich nahtlos in die Darstellungseinstellungen von macOS integrieren.

### Internationalisierung und Sprachüberschreibungen

ATBCmder unterstützt **über 30 Sprachen**, darunter Englisch, vereinfachtes Chinesisch (简体中文), traditionelles Chinesisch (繁體中文), Deutsch (Deutsch), Französisch (Français), Spanisch (Español), Russisch (Русский), Japanisch (日本語), Italienisch, Polnisch, Koreanisch und mehr. 

![Language Settings](images/language_settings.png) 

- **Auto-Follow der Systemsprache**: Standardmäßig erkennt ATBCmder beim Start Ihr macOS-Systemgebietsschema (`AppleLanguages`) und wendet die passende Übersetzung automatisch an. 
- **Manuelle Sprachauswahl**: 
1. Öffnen Sie die Einstellungen, indem Sie `Cmd+,` drücken oder `cm_Options` ausführen. 
2. Wählen Sie im linken Navigationsbereich **Sprache** aus. 
3. Wählen Sie Ihre bevorzugte Sprache aus der Dropdown-Liste. 
- **Live-Neuladen (kein Neustart erforderlich)**: Im Gegensatz zu den meisten herkömmlichen Mac-Dienstprogrammen, die das Beenden und Neustarten der Anwendung erfordern, übersetzt ATBCmder die gesamte Benutzeroberfläche (Menüs, Symbolleisten, Dialoge, Schaltflächen-Tooltips und Statusmeldungen) dynamisch in Echtzeit neu, sobald Sie eine neue Sprache auswählen.

### Aussehen und Themen

ATBCmder unterstützt die hellen und dunklen Darstellungsmodi von macOS vollständig: 

- **System Appearance Sync**: Wechselt automatisch zwischen Hell- und Dunkelmodus, wenn sich das Erscheinungsbild Ihres macOS-Systems ändert (z. B. bei Sonnenuntergang oder über das Kontrollzentrum). 
- **Themenoptionen**: 
- **Fusion / Natives macOS**: Klassische, klare Desktop-Ästhetik, die die Akzentfarben von macOS und die Lebendigkeit der Fenster berücksichtigt. 
- **Stilvolles Thema**: Moderne Ästhetik mit abgerundeten segmentierten Steuerelementen, subtilen Farbverlaufstrennern und pillenförmigen Tab-Leisten. 
- **Dark Mode Palette**: Verwendet dunkle Kohleoberflächen (`#2C2C2E` / `#242426`) mit kontrastreichem Text und benutzerdefinierten Ordnersymbolen, um die Belastung der Augen in Umgebungen mit wenig Licht zu reduzieren. 
- **Lichtmodus-Palette**: Klarer weißer Hintergrund mit weichen grauen Trennlinien (`#FAFBFD` / `#EEF2F7`) und klaren Kontrasträndern. 

---

## 5. ⚡ Profi-Tipps und erweiterte Layout-Konfigurationen

Nutzen Sie die flexible Layout-Engine von ATBCmder voll aus, um Ihren Arbeitsbereich für Multi-Monitor-, Ultra-Wide- oder spezielle Datenverwaltungskonfigurationen anzupassen.

### Tipp 1: Fensterposition und Layoutverhältnisse speichern (`cm_ConfigSavePos`)

Wenn Sie Ihren Arbeitsbereich anordnen – Fensterabmessungen anpassen, auf einem externen Display maximieren oder ein bestimmtes mittleres Teilerverhältnis festlegen – können Sie diese Konfiguration sperren, sodass sie jedes Mal identisch wiederhergestellt wird: 

1. Ordnen Sie das ATBCmder-Hauptfenster an und stellen Sie den mittleren Teiler auf Ihr bevorzugtes Verhältnis ein. 
2. Wählen Sie das Menü **Konfiguration** → **Position und Layout speichern** oder führen Sie den internen Befehl aus: 
   ```
   cm_ConfigSavePos
   ```
 

3. Ihre Fenstergröße, Bildschirmkoordinaten, maximierter Zustand und Panelverhältnisse werden direkt in `atbcmder.xml` geschrieben. 
4. Stellen Sie unter **Einstellungen** → **Layout** sicher, dass **„Fensterposition beim Beenden speichern“** für automatische kontinuierliche Aktualisierungen aktiviert ist.

### Tipp 2: Horizontales Dual-Panel-Layout umschalten (`cm_HorizontalFilePanels`)

Während nebeneinander angeordnete vertikale Paneele für Dateivorgänge Standard sind, sind gestapelte horizontale Paneele (oberes Paneel und unteres Paneel) außerordentlich nützlich, wenn: 

- Arbeiten mit extrem langen Dateinamen, die die volle Bildschirmbreite erfordern. 
- Vergleich breiter Dateimetadatenspalten (Berechtigungen, Besitzer, Prüfsummen, Dimensionen). 
- Arbeiten an gedrehten vertikalen Monitoren oder Tablets. 

So wechseln Sie das Layout: 

1. Wählen Sie das Menü **Anzeigen** → **Horizontale Panels** oder lösen Sie einen internen Befehl aus: 
   ```
   cm_HorizontalFilePanels
   ```
 

2. Wenn der horizontale Modus aktiv ist: 
- Die Paneele werden vertikal gestapelt (oberes Paneel und unteres Paneel). 
- Die mittlere Symbolleiste dreht sich automatisch in einen horizontalen Streifen zwischen der oberen und unteren Leiste. 
- Der Ziehcursor passt sich an einen vertikalen Teilungszeiger (`SplitVCursor`) an, sodass Sie die Größe des Höhenverhältnisses zwischen Ober- und Unterteil mühelos ändern können.

### Tipp 3: Einrasten des mittleren Splitters mit einem Klick

- **Sofortige 50/50-Balance**: Doppelklicken Sie irgendwo auf den mittleren Teilerbalken oder die Trennlinie. Die Paneele schnappen sofort wieder auf eine exakte 50 % / 50 %-Trennung zurück. 
- **Verhältnisvoreinstellungen**: Im Design „Stilvoll“ wird durch Klicken auf die mittleren segmentierten Schaltflächen das Layout auf `50:50`, `70:30` (Hervorhebung des Quellfensters) oder `30:70` (Hervorhebung des Zielfensters) ausgerichtet.

### Tipp 4: Automatische Sitzungswiederherstellung und Workspace-Persistenz

ATBCmder verfügt über ein intelligentes Sitzungsverwaltungssubsystem (`SessionManager`), das sicherstellt, dass Ihre Arbeitsumgebung immer erhalten bleibt: 

- **Session XML Storage**: Der Sitzungsstatus wird automatisch unter `atbcmder_session.xml` in Ihrem Konfigurationsverzeichnis (`~/Library/Application Support/ATBCmder/`) beibehalten. 
- **Fenstergeometriespeicher**: Stellt die genauen Fensterkoordinaten (`x`, `y`), die Abmessungen (`width`, `height`), den maximierten Zustand und den mittleren Teileranteil (`splitter_ratio`) wieder her. 
- **Dual-Panel-Tab-Wiederherstellung**: 
- Stellt beim Start alle geöffneten Registerkarten sowohl im linken als auch im rechten Bereich wieder her. 
- Merkt sich den aktiven Tab-Index in jedem Panel. 
- Lädt automatisch das genaue Arbeitsverzeichnis für jede Registerkarte, sodass die manuelle Neunavigation zu tiefen Projektordnern entfällt. 
- **Standardpositionssperre**: Sie können Ihre aktuelle Fenstergeometrie und Ihr Teilerverhältnis auch dauerhaft als Standard-Startkonfiguration sperren, indem Sie **Konfiguration ➔ Position speichern** (`cm_ConfigSavePos`) verwenden. 

---

## 6. Sicherheits- und Systemwarnungen: Einrichtung der macOS-Funktionstaste (Fn).

Wenn Sie Total Commander, Double Commander oder Norton Commander auf einer PC-Tastatur verwendet haben, sind Ihre Finger darauf trainiert, die Funktionstasten der obersten Reihe zu verwenden (`F3` Ansicht, `F4` Bearbeiten, `F5` Kopieren, `F6` Verschieben, `F7` MkDir, `F8` Löschen). 

Allerdings handhaben Apple-Tastaturen die Funktionszeile standardmäßig anders. 

> [!WARNUNG] 
> ### 🍎 macOS-Funktionstasten-Hardwarekonflikt 
> Auf Apple-Tastaturen (eingebaute MacBook-Tastaturen, Apple Magic Keyboard) sind die Tasten der oberen Reihe standardmäßig auf **macOS-spezifische Hardwarefunktionen** (Anzeigehelligkeit, Mission Control, Spotlight, Diktieren, Nicht stören, Mediensteuerung und Audiolautstärke) eingestellt. 
> 
> Wenn Sie auf einem MacBook ohne Konfiguration `F5` drücken, versucht macOS, die Tastaturbeleuchtung anzupassen oder das Diktat auszulösen, anstatt Ihre Dateien zu kopieren!

### Option A: Halten Sie die Taste `Fn` (Globe 🌐) gedrückt (Standard-MacOS-Setup)

Wenn Sie lieber die Standard-Medientasten von Apple beibehalten möchten: 

- Halten Sie die Taste **`Fn`** (oder Globe 🌐) gedrückt, während Sie eine beliebige Funktionstaste drücken: 
- `Fn+F3`: Universeller Lister 
- `Fn+F4`: Interner Redakteur 
- `Fn+F5`: Dateien kopieren 
- `Fn+F6`: Dateien verschieben 
- `Fn+F7`: Ordner erstellen 
- `Fn+F8`: In den Papierkorb löschen

### Option B: Standardfunktionstasten systemweit aktivieren (empfohlen)

Wenn Sie authentische, schnelle Commander-Reflexe mit nur einer Taste wünschen, ohne den Modifikator `Fn` gedrückt zu halten: 

1. Öffnen Sie **Systemeinstellungen** im Apple-Menü (). 
2. Klicken Sie in der Seitenleiste auf **Tastatur**. 
3. Klicken Sie auf die Schaltfläche **Tastaturkürzel…**. 
4. Wählen Sie in der linken Navigationsliste **Funktionstasten** aus. 
5. Aktivieren Sie den Umschalter: **„Tasten F1, F2 usw. als Standardfunktionstasten verwenden“**. 

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
 

Nach der Aktivierung: 

- Durch direktes Drücken von `F1`–`F12` werden sofort ATBCmder-Befehle ausgelöst. 
- Um Helligkeits- oder Lautstärkeregler zu verwenden, halten Sie einfach `Fn` gedrückt, während Sie die Taste drücken. 

---

## 7. Kurzreferenz zu Dual-Matrix Essential Shortcuts

ATBCmder bietet vollständige Dual-Matrix-Tastaturunterstützung: Verwenden Sie native macOS-Tastenkombinationen (`Cmd ⌘`), klassische Commander-Tasten (`Fn`) oder beide austauschbar.

| Kernaktion | Befehls-ID | macOS Native (`Cmd ⌘`) | Klassischer Kommandant (`Fn`) | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Verzeichnis-Hotlist** | `cm_DirHotList` | `Cmd+D` / `⌘D` | `Ctrl+D` / `⌃D` | Öffnet das Verzeichnis-Lesezeichen-Popup mit sofortiger Fuzzy-Suche. | 
| **Laufwerksliste (Links/Rechts)** | `cm_LeftOpenDrives` / `cm_RightOpenDrives` | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | Öffnet das Laufwerks- und Lautstärkemenü für den linken oder rechten Bereich (`Alt+D` für den aktiven Bereich). | 
| **Dateien kopieren** | `cm_Copy` | `Cmd+C` ➔ `Cmd+V` | `F5` (oder `Fn+F5`) | Kopiert ausgewählte Elemente vom aktiven Bereich in den inaktiven Bereich. | 
| **Dateien verschieben** | `cm_Move` | `Cmd+C` ➔ `Opt+Cmd+V` | `F6` (oder `Fn+F6`) | Verschiebt ausgewählte Elemente vom aktiven Bereich in den inaktiven Bereich. | 
| **Im Lister anzeigen** | `cm_View` | `Space` / `Cmd+Y` | `F3` (oder `Fn+F3`) | Öffnet eine Datei im Universal Lister (Code, Hex, Bild, PDF, Audio). | 
| **Schnellansicht** | `cm_QuickView` | `Cmd+Q` / `Ctrl+Q` | `Ctrl+Q` | Zeigt eine sofortige Live-Vorschau im gegenüberliegenden Bereich an. | 
| **Datei bearbeiten** | `cm_Edit` | `Cmd+E` | `F4` (oder `Fn+F4`) | Öffnet die Datei im integrierten Code-/Texteditor. | 
| **Neues Verzeichnis** | `cm_MkDir` | `Shift+Cmd+N` | `F7` (oder `Fn+F7`) | Erstellt einen neuen Ordner im aktiven Bereich. | 
| **In den Papierkorb löschen** | `cm_Delete` | `Cmd+Backspace` | `F8` (oder `Fn+F8`) | Verschiebt ausgewählte Dateien sicher in den macOS-Papierkorb. | 
| **Inline-Umbenennung** | `cm_Rename` | `Return` | `F2` / `Shift+F6` | Benennt die markierte Datei direkt um. | 
| **Schalttafel** | `cm_FocusSwap` | `Tab` | `Tab` | Verschiebt den Tastaturfokus auf das gegenüberliegende Bedienfeld (`cm_SwitchPanel`). | 
| **Links/Rechts tauschen** | `cm_Exchange` | `Ctrl+U` | `Ctrl+U` | Tauscht Verzeichnispfade zwischen linkem und rechtem Bereich aus. | 
| **Neuer Tab** | `cm_NewTab` | `Cmd+T` | `Ctrl+T` | Öffnet eine neue Ordnerregisterkarte im aktuellen Bereich. | 
| **Tab schließen** | `cm_CloseTab` | `Cmd+W` | `Ctrl+W` | Schließt die aktive Registerkarte. | 
| **Horizontaler Modus** | `cm_HorizontalFilePanels` | Menü: Anzeigen ➔ Horizontal | Menü: Anzeigen ➔ Horizontal | Schaltet zwischen dem nebeneinanderliegenden und dem oben und unten gestapelten Layout um. | 
| **Layout speichern** | `cm_ConfigSavePos` | Menü: Konfig ➔ Pos. speichern | Menü: Konfig ➔ Pos. speichern | Speichert die aktuellen Fensterabmessungen und Panelproportionen. | 
| **Sandbox-Zugriff** | `cm_GrantFilesystemAccess` | Menü: Datei ➔ Berechtigungen | Menü: Datei ➔ Berechtigungen | Startet den Onboarding-Assistenten für die macOS App Sandbox. | 
| **Einstellungen** | `cm_Options` | `Cmd+,` | `Alt+O` | Öffnet den ATBCmder-Konfigurationsdialog. |

---

## Nächste Schritte

Nachdem Sie nun die Dual-Panel-Grundlage beherrschen und Ihre macOS-Umgebung konfiguriert haben, fahren Sie mit **[Kapitel 2: Navigation und Ordnerregisterkarten](navigation_and_tabs.md)** fort, um zu erfahren, wie Sie schnell durch Verzeichnisbäume navigieren, Arbeitsbereiche mit mehreren Registerkarten beherrschen, bevorzugte Verzeichnissätze speichern, sofortige Hotlists verwenden und rekursive flache Zweigansichten nutzen.