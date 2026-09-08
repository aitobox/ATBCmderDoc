# Kapitel 2: Navigation & Ordner-Tabs

Flüssige, schnelle Bewegung durch Verzeichnisse ist der Grundstein der herkömmlichen Dateiverwaltung. In ATBCmder müssen Sie nie Zeit damit verschwenden, Bildlaufleisten zu ziehen, wiederholt durch verschachtelte Ordner zu klicken oder sich mit Dutzenden fragmentierter Finder-Fenster herumzuschlagen. 

In diesem Kapitel wird alles behandelt, was Sie zum sicheren Navigieren in lokalen und Remote-Dateisystemen benötigen: interaktive Breadcrumbs, Sprünge in der Tastaturhierarchie, native macOS-Arbeitsabläufe mit mehreren Registerkarten, beständige Arbeitsbereiche mit Favoritenregisterkarten mit zwei Bedienfeldern, sofortige Fuzzy-Such-Lesezeichen und fünf spezielle Bedienfeldansichtsmodi. 

---

## 1. Visueller Schnellstart: Mühelose Hierarchie und räumliche Organisation

In ATBCmder fungiert jedes Panel als autonome Browsing-Engine, die mit einer eigenen Breadcrumb-Kette, einer unabhängigen Registerkartenleiste, einem Verlaufsstapel und eigenen Ansichtsmodi ausgestattet ist. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [PFADZEILE]   🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [TAB-LEISTE]  [★ Quellcode (Gesperrt)] [Assets] [Build-Ausgabe] [+]             │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Name                         Typ       Größe     Geändert           Rechte     │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Heute, 14:22       drwxr-xr-x │
│  ▸ ui                         <DIR>               Heute, 15:05       drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Heute, 15:10       -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Gestern, 19:40     -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [SCHNELLSUCHE]  🔍 Suchen: mai_   (Treffer: main.py)                            │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Spickzettel für die Dual-Matrix-Navigation

| Aktion | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Übergeordnetes Verzeichnis** | `Backspace` / `⌘↑` | `Ctrl+PgUp` | `cm_ChangeDirToParent` | Eine Verzeichnisebene nach oben verschieben (`..`). | 
| **Stammverzeichnis** | `Ctrl+\` / `⌃\` | `\` | `cm_ChangeDirToRoot` | Springen Sie direkt zum Systemstammverzeichnis (`/`). | 
| **Home-Verzeichnis** | `Ctrl+Shift+Home` / `⌃⇧Home` | `Alt+Home` | `cm_ChangeDirToHome` | Wechseln Sie zum Benutzer-Home-Verzeichnis (`~`). | 
| **Artikel öffnen / Verzeichnis eingeben** | `Enter` / `⌘↓` | `Enter` | — | Geben Sie das ausgewählte Verzeichnis ein oder öffnen Sie die Datei. | 
| **Neuer Tab** | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | Aktiven Ordner in einem neuen Tab öffnen. | 
| **Tab schließen** | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | Schließen Sie die aktuell fokussierte Registerkarte. | 
| **Verzeichnis-Hotlist** | `Ctrl+D` / `⌃D` | `Ctrl+D` | `cm_DirHotList` | Öffnen Sie das Instant-Fuzzy-Lesezeichen-Popup. | 
| **Geschichte zurück** | `Cmd+[` / `⌘[` | `Alt+Left` | `cm_ViewHistoryPrev` | Gehen Sie zurück zum zuvor besuchten Ordner. | 
| **Geschichte weiterleiten** | `Cmd+]` / `⌘]` | `Alt+Right` | `cm_ViewHistoryNext` | Gehen Sie im Verzeichnisverlauf vorwärts. | 
| **Verlaufs-Dropdown-Liste** | `Alt+F8` / `⌥F8` | `Ctrl+Down` | `cm_DirHistory` | Dropdown-Liste „Verlauf anzeigen“. | 
| **Laufwerks-/Volume-Liste (Links/Rechts)** | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | `cm_LeftOpenDrives` / `cm_RightOpenDrives` (`cm_Drives`) | Öffnen Sie das Laufwerksmenü für das linke oder rechte Panel (`Alt+D` für das aktive Panel). | 
| **Schnellsuche** | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_QuickSearch` | Öffnen Sie das Overlay für die Echtzeitsuche im Bedienfeld. | 

---

## 2. Grundlegende Verzeichnisnavigation: Pfade, Breadcrumbs und Verknüpfungen

ATBCmder bietet Ihnen mehrere redundante, ergonomische Möglichkeiten, sich durch Ihr Dateisystem zu bewegen – unabhängig davon, ob Sie Mausgesten, Trackpad-Klicks oder reine Flüssiger Tastatur-Flow bevorzugen.

### Maus- und Trackpad-Navigation

- **Ordner eingeben**: Doppelklicken Sie auf eine beliebige Verzeichniszeile oder drücken Sie `Enter` (`Return`). 
- **Aufsteigende Hierarchien**: Doppelklicken Sie auf die oberste Zeile `[..]`, um sofort zum übergeordneten Ordner zu springen. 
- **Hintergrundregisterkarten**: Klicken Sie mit der mittleren Maustaste auf eine beliebige Ordnerzeile, um dieses Verzeichnis in einer neuen Hintergrundregisterkarte zu öffnen, ohne Ihre aktuelle Ansicht zu verlieren (`cm_OpenDirInNewTab`).

### Interaktive Breadcrumb-Leiste im Finder-Stil

Direkt über jedem Dateifenster positioniert, stellt die interaktive Breadcrumb-Leiste Ihren aktuellen UNIX-Pfad als Kette anklickbarer Segmente dar: 

```
🏠 / ▸ Users ▸ brain ▸ Projects ▸ ATBCmder ▸ docs
```
 

1. **Instant Ancestor Leaping**: Klicken Sie auf ein beliebiges Vorgängersegment (z. B. `Projects` oder `Users`), um direkt zu dieser Ebene zu springen und die Navigation mehrerer übergeordneter Ordner zu umgehen. 
2. **Dropdown-Menüs für Geschwisterverzeichnisse**: Bewegen Sie den Mauszeiger über das Chevron (`▸`) zwischen den Segmenten oder klicken Sie darauf, um ein Dropdown-Menü anzuzeigen, das alle Geschwisterordner auf dieser Hierarchieebene auflistet. Klicken Sie auf ein beliebiges Geschwisterelement, um direkt dorthin zu navigieren. 
3. **Kontextbezogene Dienstprogramme**: Klicken Sie mit der rechten Maustaste auf ein beliebiges Breadcrumb-Segment, um ein spezielles Kontextmenü aufzurufen: 
- **In neuem Tab öffnen**: Öffnet den spezifischen Vorgängerordner in einem neuen Tab. 
- **Im Finder anzeigen**: Öffnet das Verzeichnis im nativen macOS Finder (`open -R`). 
- **Pfad kopieren**: Kopiert den absoluten UNIX-Pfad des Segments in Ihre macOS-Zwischenablage. 
- **Im Terminal öffnen**: Erzeugt ein Terminalfenster in genau diesem Verzeichnis. 
4. **Direkte Pfadtextbearbeitung (`BreadcrumbLineEdit`)**: 
- Doppelklicken Sie auf die leere Stelle rechts neben der Breadcrumb-Kette (oder drücken Sie `Shift+F2`). 
- Die Breadcrumb-Segmente verwandeln sich sofort in ein bearbeitbares Textfeld (`QLineEdit`). 
- Geben oder fügen Sie beliebige Pfade ein (z. B. `~/Library/Application Support`, `/var/log`, `/Volumes/ExternalDrive` oder `vfs://` Archivspeicherorte). 
- Drücken Sie `Enter`, um zu springen, oder `Esc`, um abzubrechen und zu den Breadcrumb-Schaltflächen zurückzukehren.

### Schnelle Tastatursprünge

Mit diesen speziellen Navigationsbefehlen behalten Sie die Startreihe im Griff: 

- **Übergeordnetes Verzeichnis (`Backspace` / `⌘↑` / `Ctrl+PgUp` / `cm_ChangeDirToParent`)**: Steigt sofort zum übergeordneten Verzeichnis auf. Wenn Sie aufsteigen, positioniert ATBCmder den Cursor automatisch auf dem Ordner, den Sie gerade verlassen haben, sodass Sie nie den Überblick verlieren. 
- **Stammverzeichnis (`Ctrl+\` / `cm_ChangeDirToRoot`)**: Springt direkt zum Stammverzeichnis Ihres macOS-Startvolumes (`/`). 
- **Home-Verzeichnis (`Ctrl+Shift+Home` / `cm_ChangeDirToHome`)**: Springt direkt zu Ihrem Benutzer-Home-Verzeichnis (`/Users/username` oder `~`). 
- **Erster und letzter Eintrag**: Drücken Sie `Home` (`cm_GoToFirst`), um den Cursor-Fokus auf den obersten Eintrag (`..`) zu setzen, oder `End` (`cm_GoToLast`), um zur letzten Datei im aktuellen Bereich zu springen. 

---

## 3. Ordnerregisterkarten: Multitasking in jedem Bereich

Die Arbeit an komplexen Softwareprojekten, Fotobibliotheken oder Server-Backups erfordert oft das gleichzeitige Jonglieren mit mehreren Ordnern. Anstatt Dutzende von Fenstern zu öffnen, verfügt ATBCmder über unabhängige Multi-Tab-Strips für beide Panels. 

![Folder Tabs and Splitters](images/quick_access_paths.png) 
*Multi-Tab-Verwaltung und schnelle Navigation in ATBCmder*

### Natives macOS-Tab-Bar-Design

Die mit `MacNativeTabBar` erstellte Tab-Leiste entspricht der modernen macOS-Ästhetik: 

- **Visuelles Design**: Abgerundete Tab-Ecken, sanfte Hover-Zustände und klare aktive Tab-Akzentanzeigen. 
- **Hover-Schaltflächen zum Schließen**: Jede Registerkarte verfügt über eine integrierte Schaltfläche zum Schließen `✕`, die beim Bewegen des Mauszeigers oder bei Auswahl angezeigt wird. 
- **Zum Schließen mit der mittleren Maustaste**: Klicken Sie mit der mittleren Maustaste bzw. dem Dreifingerklick auf das Trackpad auf eine beliebige Registerkarte, um sie sofort zu schließen. 
- **Zum Hinzufügen doppelklicken**: Doppelklicken Sie auf eine leere Stelle in der Registerkartenleiste, um sofort eine neue Registerkarte zu erzeugen, die aus dem aktiven Pfad geklont wurde.

### Tab-Operationen und Hotkeys

| Aktion | macOS-Verknüpfung | Klassischer Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Neuer Tab** | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | Öffnet das aktuelle Verzeichnis in einem neuen Tab. | 
| **Tab schließen** | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | Schließt die aktive Registerkarte (mindestens 1 Registerkarte bleibt erhalten). | 
| **Nächster Tab** | `Ctrl+Tab` / `⌃⇥` | `Ctrl+Tab` | `cm_NextTab` | Wechselt den Fokus zur nächsten Registerkarte rechts. | 
| **Vorheriger Tab** | `Ctrl+Shift+Tab` / `⌃⇧⇥` | `Ctrl+Shift+Tab` | `cm_PrevTab` | Wechselt den Fokus zur vorherigen Registerkarte nach links. | 
| **Quick-Tab-Liste** | `Ctrl+Shift+L` / `⌃⇧L` | `Ctrl+Shift+L` | `cm_ShowTabsList` | Öffnet ein nummeriertes Menü aller geöffneten Registerkarten. | 
| **Registerkarte umbenennen** | *Rechtsklick auf die Registerkarte* | — | `cm_RenameTab` | Weist der Registerkarte eine benutzerdefinierte benutzerfreundliche Bezeichnung zu. | 
| **Andere Tabs schließen** | *Rechtsklick auf die Registerkarte* | — | `cm_CloseOtherTabs` | Schließt alle Registerkarten außer der ausgewählten. | 
| **Duplikate schließen** | *Rechtsklick auf die Registerkarte* | — | `cm_CloseDuplicateTabs` | Erkennt und schließt doppelte Tabs mit identischen Pfaden. | 
| **Alle Tabs schließen** | *Menüregisterkarten* | — | `cm_CloseAllTabs` | Setzt das Bedienfeld auf eine einzelne Registerkarte zurück. | 
| **Auf Gegenseite kopieren** | *Menüregisterkarten* | — | `cm_CopyAllTabsToOpposite` | Kopiert alle Registerkarten im aktiven Bereich in den Zielbereich. |

### Tab-Sperrmodi

Verhindern Sie versehentliche Verzeichnisänderungen in wichtigen Ordnern, indem Sie Tab-Sperroptionen konfigurieren. Klicken Sie mit der rechten Maustaste auf eine beliebige Registerkarte, um den Sperrmodus auszuwählen: 

1. **Normal (entsperrt)**: 
- Standard-Tab-Verhalten. 
- Beim Navigieren durch Ordner wird der aktuelle Tab-Pfad direkt aktualisiert. 
2. **Gesperrt (`cmd_SetTabOptionLock`)**: 
– Der Tab-Pfad ist strikt an seiner ursprünglichen Ankerposition eingefroren. 
– Ein visuelles Sperrsymbol (`🔒` oder `★`) erscheint im Titel der Registerkarte. 

- Wenn Sie auf ein Unterverzeichnis doppelklicken oder navigieren, lässt ATBCmder die gesperrte Registerkarte automatisch unverändert und öffnet den Zielordner in einer **neuen angrenzenden Registerkarte**. 
3. **Gesperrt mit zulässigen Unterverzeichnissen (`cmd_SetTabOptionLockWithSubdirs`)**: 
- Ermöglicht das freie Durchsuchen der untergeordneten Ordner und Unterverzeichnisse in diesem Baum. 
- Verhindert, dass Sie über den gesperrten Basisordner hinaus aufsteigen. 
- Wenn Sie wegschalten oder neu laden, wird die Registerkarte sicher auf ihren Ankerstamm zurückgesetzt. 

---

## 4. Bevorzugte Registerkarten: Benannte Dual-Panel-Arbeitsbereiche

Während einzelne Registerkarten lokale Flexibilität bieten, ermöglichen Ihnen **Favorite Tabs** die Erfassung und Wiederherstellung vollständiger Dual-Panel-Betriebsumgebungen mit einem einzigen Befehl. 

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
 

Ein Favoriten-Tab-Set umfasst Folgendes: 

- Alle geöffneten Registerkarten im linken Bereich (einschließlich Pfade und Sperrstatus). 
- Alle geöffneten Registerkarten im rechten Bereich (einschließlich Pfade und Sperrstatus). 
– Die aktive Registerkartenauswahl für beide Panels.

### Befehle für bevorzugte Tabs

- **Aktuelle Tabs speichern (`cm_SaveFavoriteTabs`)**: 
- Zugriff über das Menü **Favoriten** → **Aktuelle Tabs unter „Neue Favoriten-Tabs speichern“** oder durch Rechtsklick auf die Tableiste. 
– Fordert Sie auf, den Arbeitsbereich zu benennen (z. B. `Rust Web Backend`, `Photo Editing 2026` oder `Server Deployment`). 
– Speichert die Arbeitsbereichsdefinition dauerhaft in `fav_tab_config.xml`. 

- **Lieblingsregisterkarten laden (`cm_LoadFavoriteTabs`)**: 
- Zugriff über das Menü **Favoriten** → **Registerkarten aus Favoriten-Registerkarten laden**. 
– Öffnet einen modalen Dialog, in dem Ihre gespeicherten Tab-Sets aufgelistet sind. Wählen Sie einen Satz aus und beide Panels stellen sofort das vollständige Multi-Tab-Layout wieder her. 

- **Favoriten-Tabs erneut speichern (`cm_ResaveFavoriteTabs`)**: 
– Aktualisiert den aktuell aktiven Arbeitsbereichssatz mit allen neu geöffneten, geschlossenen oder navigierten Registerkarten, ohne dass Sie zur Eingabe eines neuen Namens aufgefordert werden. 

- **Favoriten-Tabs neu laden (`cm_ReloadFavoriteTabs`)**: 
– Setzt beide Bedienfelder auf den sauberen, gespeicherten Zustand des aktiven Arbeitsbereichs zurück und verwirft alle während der Sitzung geöffneten Erkundungsregisterkarten. 

- **Arbeitsbereiche wechseln (nächste/vorherige Favoriten-Registerkarten)**: 
- Wechseln Sie über das Favoritenmenü schnell und nacheinander zwischen verschiedenen gespeicherten Projektarbeitsbereichen. 
- **Konfiguration (`cm_ConfigFavoriteTabs`)**: 
- Öffnen Sie **Einstellungen** → **Lieblings-Tabs**, um Sätze neu anzuordnen, Arbeitsbereiche umzubenennen, einzelne Tab-Pfade manuell zu bearbeiten oder veraltete Sätze zu löschen. 

---

## 5. Verzeichnis-Hotlists (Lesezeichen)

Die **Verzeichnis-Hotlist** bietet globalen, sofortigen Zugriff auf Ihre am häufigsten verwendeten Ordner über lokale Laufwerke, externe Festplatten und Remote-Netzwerk-Mounts. 

![Directory Hotlist](images/quick_access_paths.png) 
*Verzeichnis-Hotlist-Popup mit Echtzeit-Fuzzy-Suche*

### Sofortiges Hotlist-Popup (`Ctrl+D` / `⌃D` / `cm_DirHotList`)

Durch Drücken von `Ctrl+D` wird ein leichter, schwebender Suchdialog direkt unter Ihren Augen angezeigt: 

1. **Fuzzy-Suche in Echtzeit**: 
- Beginnen Sie sofort mit der Eingabe. Die Suchleiste filtert alle Ihre Lesezeichennamen und Zielpfade in Echtzeit. 
- Wenn Sie beispielsweise `down` eingeben, wird sofort `Downloads — /Users/username/Downloads` gefunden. 
2. **Tastaturdurchlauf**: 
- Markieren Sie mit den Pfeiltasten `Up` und `Down` das gewünschte Lesezeichen. 
- Drücken Sie `Enter`, um im aktiven Panel direkt zu diesem Pfad zu navigieren. 
- Drücken Sie `Esc`, um das Popup zu schließen, ohne Ihr Verzeichnis zu ändern. 
3. **Schnelle Lesezeichenerstellung**: 
- Klicken Sie im Popup auf die Schaltfläche **Aktuelles Verzeichnis hinzufügen** (oder drücken Sie `Alt+A`). 
– ATBCmder füllt automatisch den aktuellen Ordnerpfad und schlägt einen sauberen Anzeigenamen vor.

### Hotlist-Konfiguration (`Ctrl+Shift+D` / `⌃⇧D` / `cm_ConfigDirHotList`)

Öffnen Sie **Einstellungen** → **Verzeichnis-Hotlist** (oder lösen Sie `cm_ConfigDirHotList` aus), um Ihre Lesezeichen zu organisieren: 

- **Hierarchische Untermenüs**: Gruppieren Sie verwandte Lesezeichen in Kategorien (z. B. `Work`, `Personal`, `Cloud Storage`, `Network Shares`). 
- **Benutzerdefinierte Anzeigebezeichnungen**: Weisen Sie benutzerfreundliche Namen wie `Work Documents` anstelle langer Pfade wie `/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Work` zu. 
- **Neuordnung per Drag-and-Drop**: Ordnen Sie die Reihenfolge der Lesezeichen neu, damit die Verzeichnisse mit der höchsten Priorität ganz oben auf Ihrer Liste bleiben. 

---

## 6. Verlauf und Laufwerke: Navigieren durch Zeit und Speichervolumes

ATBCmder verwaltet einen umfassenden Prüfpfad Ihrer Browsersitzungen, sodass Sie Ihre Schritte über lokale Speicher und bereitgestellte Volumes hinweg nachverfolgen können.

### Navigationsverlauf

Jedes Panel zeichnet seinen eigenen chronologischen Pfadverlaufsstapel auf: 

- **Zurück (`Cmd+[` / `⌘[` oder `Alt+Left` / `cm_ViewHistoryPrev`)**: Geht im Pfadverlauf des aktiven Panels einen Schritt zurück. 
- **Vorwärts (`Cmd+]` / `⌘]` oder `Alt+Right` / `cm_ViewHistoryNext`)**: Geht einen Schritt vorwärts, nachdem zurück navigiert wurde. 
- **Verzeichnisverlaufs-Popup (`Alt+F8` / `⌥F8` oder `Ctrl+Down` / `⌃↓` / `cm_DirHistory`)**: 
- Zeigt ein scrollbares Popup-Menü mit den zuletzt über 20 besuchten Verzeichnissen im aktiven Bereich an. 
- Klicken Sie auf oder mit der Pfeiltaste nach unten auf ein beliebiges vorheriges Verzeichnis, um direkt dorthin zu springen und wiederholtes Drücken der Zurück-Taste zu überspringen.

### Laufwerks- und Lautstärkeumschalter

Unter macOS befinden sich alle internen Partitionen, externen USB-C-/Thunderbolt-Laufwerke, gemounteten DMGs und Netzwerkfreigaben unter `/Volumes`. ATBCmder bietet dedizierte Befehle zum Wechseln zwischen diesen Zielen: 

![Drive and Volume Switcher Menu](images/driver_select.png) 
*Sofort gemountete Laufwerks- und Lautstärkeauswahl, ausgelöst über Alt+F1 (linkes Panel), Alt+F2 (rechtes Panel) oder Alt+D* 

- **Linker Laufwerksumschalter (`Alt+F1` / `⌥F1` / `cm_LeftOpenDrives`)**: Klassische Commander-Kernverknüpfung, die das Laufwerks- und Volume-Auswahlmenü für den linken Bereich öffnet. 
- **Laufwerksumschalter auf der rechten Seite (`Alt+F2` / `⌥F2` / `cm_RightOpenDrives`)**: Klassische Commander-Kernverknüpfung, die das Laufwerks- und Volume-Auswahlmenü für die rechte Seite öffnet. 
- **Aktives Panel-Laufwerksmenü (`Alt+D` / `⌥D` / `cm_Drives`)**: Öffnet ein Popup-Menü, in dem alle bereitgestellten Volumes, das Root-Dateisystem `/`, das Benutzer-Home `~` und die verbundenen Netzwerkendpunkte für das aktuell fokussierte Panel aufgelistet sind. 

> [!NOTE] 
> **Berechtigungen für externe macOS-Laufwerke**: Wenn Sie zum ersten Mal zu externen Laufwerken unter `/Volumes` navigieren, werden Sie möglicherweise von macOS App Sandbox um Erlaubnis gebeten. ATBCmder zeigt ein Autorisierungsdialogfeld zum Erstellen eines dauerhaften sicherheitsbezogenen Lesezeichens für dieses Laufwerk an. 

---

## 7. Panel-Ansichtsmodi: Anpassen der Anzeige

ATBCmder verfügt über 5 spezielle Ansichtsmodi, die darauf ausgelegt sind, den Platz auf dem Bildschirm und die Informationsdichte für verschiedene Dateiverwaltungs-Workflows zu optimieren.

### 1. Vollständige Spaltenansicht (`Ctrl+F2` / `⌃F2` / `cm_ColumnsView`)

Der umfassendste Standardansichtsmodus. Es zeigt Dateien in einem umfangreichen Tabellenformat mit konfigurierbaren Kopfzeilen an: 

| Spalte | Beschreibung | Ausrichtung | 
| :--- | :--- | :--- | 
| **Name** | Datei- oder Verzeichnisname mit nativem macOS-Typsymbol. | Links | 
| **Ext** | Dateierweiterung (z. B. `py`, `png`, `zip`). | Links | 
| **Größe** | Formatierte Größe (B, KB, MB, GB). Ordner zeigen `<DIR>`. | Richtig | 
| **Änderungsdatum** | Zeitstempel entsprechend dem macOS-Gebietsschema formatiert. | Links | 
| **Attribute** | UNIX-Berechtigungen (oktal `0755` und symbolisch `rwxr-xr-x`). | Zentrum | 
| **Eigentümer / Gruppe** | UNIX-Benutzer- und Gruppeneigentumsnamen. | Links | 

- **Kopfzeilensortierung**: Klicken Sie auf eine beliebige Spaltenüberschrift, um die Sortierreihenfolge aufsteigend oder absteigend umzuschalten. Klicken Sie, während Sie `Cmd` gedrückt halten, um eine sekundäre Sortierung durchzuführen.

### 2. Kurzansicht (`Ctrl+F1` / `⌃F1` / `cm_BriefView`)

Die Kurzansicht entfernt Metadatenspalten und organisiert Dateien in mehreren kompakten vertikalen Spalten, die die gesamte Panelbreite ausfüllen. 

- **High-Density-Browsing**: Zeigt 3x bis 5x mehr Elemente gleichzeitig auf dem Bildschirm an. 
- **Best für**: Schnelles Scannen großer Verzeichnislisten (z. B. Schriftarten, Foto-Dumps oder Protokollarchive), bei denen Sie nur Dateinamen identifizieren müssen.

### 3. Miniaturansichten (`Ctrl+Shift+F1` / `⌃⇧F1` / `cm_ThumbnailsView`)

Die Miniaturansicht wandelt die Dateiliste in ein Bild- und Mediensymbolraster um. 

![Thumbnails View](images/thumbnails_grid_view.png) 
*Miniaturansicht mit Medienvorschau im aktiven Bereich* 

- **Unterstützte Medien**: Sofortige Vorschau für Fotos (JPEG, PNG, HEIC, TIFF, WebP, GIF), Vektorformate (SVG), PDF-Dokumente und Video-Miniaturansichten (MP4, MOV, MKV). 
- **Asynchrone Hintergrundgenerierung**: Das Rendern von Miniaturansichten erfolgt in Hintergrundthreads, ohne die Benutzerinteraktion zu blockieren. 
- **Anpassbare Größe**: Konfigurieren Sie die Größe der Miniaturbildsymbole (von 64 bis 256 Pixel) unter **Einstellungen** → **Dateiansichten**.

### 4. Baumansicht (`cm_TreeView`, `cm_TreeViewSplit`, `cm_TreeViewBoth`)

Die Baumansicht zeigt einen erweiterbaren hierarchischen Verzeichnisbaum an, sodass tiefe Ordnerstrukturen auf einen Blick leicht zu verstehen sind. 

![Tree View and Thumbnails View](images/treeview+thumbview.png) 
*Baumansicht neben Dateilisten und Miniaturansichten integriert* 

ATBCmder unterstützt drei verschiedene Strukturansicht-Layouts über das Menü **Anzeigen**: 

- **Baumansicht (Ersetzen) (`cm_TreeView`)**: Die Dateitabelle des aktiven Panels wird vollständig durch einen erweiterbaren Verzeichnisbaum ersetzt. 
- **Baumansicht (geteilt) (`cm_TreeViewSplit`)**: Das aktive Bedienfeld ist vertikal in zwei Unterbereiche unterteilt: einen Verzeichnisbaum auf der linken Seite und die Standarddateiliste für den ausgewählten Baumordner auf der rechten Seite. 
- **Baumansicht (beide Bereiche) (`cm_TreeViewBoth`)**: Aktiviert den geteilten Verzeichnisbaum gleichzeitig im linken und rechten Bereich. 
- **Umschalten „Dateien anzeigen“: Klicken Sie mit der rechten Maustaste in die Baumansicht und aktivieren Sie die Option „Dateien anzeigen“, um auszuwählen, ob Dateien im Baum neben Verzeichnissen gerendert oder ausgeblendet werden sollen, um nur Verzeichnisse anzuzeigen.

### 5. Zweig-/Flachansicht (`Cmd+B` / `⌘B` oder `Ctrl+B` / `⌃B` / `cm_FlatView`)

Die flache Ansicht (auch als Zweigansicht bekannt) ist eine der leistungsstärksten Funktionen in ATBCmder. Es durchläuft rekursiv alle Unterverzeichnisse und Unterordner im aktuellen Ordner und fasst alle verschachtelten Dateien in einer **einzelnen einheitlichen Liste** zusammen. 

![Branch View](images/branch_view.png) 
*Flat Branch View (`Cmd+B`) zeigt verschachtelte Inhalte in allen Unterverzeichnissen an* 

- **Die Pfadspalte**: In der flachen Ansicht fügt ATBCmder automatisch eine **Pfad**-Spalte hinzu, die den relativen verschachtelten Ordnerpfad jeder Datei anzeigt (z. B. `assets/icons/` oder `src/core/`). 
- **Globale Sortierung**: Sortieren Sie alle verschachtelten Dateien gleichzeitig im gesamten Projektbaum nach Größe, Änderungsdatum oder Dateierweiterung. 
- **Stapelverarbeitung**: Wählen Sie Dateien aus einem Dutzend verschiedener Unterverzeichnisse aus und kopieren, verschieben, vergleichen oder benennen Sie sie alle auf einmal um. 
- **Streaming Traversal**: ATBCmder streamt Suchergebnisse mithilfe von Hintergrundarbeitern inkrementell in die Ansicht und stellt so sicher, dass große Projekte (mit Zehntausenden verschachtelten Dateien) reibungslos geladen werden, ohne dass die Benutzeroberfläche einfriert. 
- **Schnelles Beenden**: Drücken Sie erneut `Cmd+B` (`Ctrl+B`), um die flache Ansicht zu verlassen und zur normalen hierarchischen Verzeichnisansicht zurückzukehren. 

---

## 8. ⚡ Profi-Tipps und tiefer Einblick: Präzisionskontrolle

Für fortgeschrittene Benutzer und erfahrene Keyboarder bietet ATBCmder eine fein abgestimmte Abstimmung und schnelle Suchmechanismen.

### In-Panel-Schnellsuch-Overlay (`Ctrl+S` / `⌃S` / `cm_QuickSearch`)

Mit der Schnellsuche können Sie direkt zu jeder Datei springen, indem Sie ihren Namen eingeben, ohne einen vollständigen Suchdialog zu öffnen. 

```
┌─────────────────────────────────────────────────────────────────┐
│  main.py            py      8.4 KB    Today, 15:10   -rw-r--r-- │
│  main_window.py     py     72.1 KB    Today, 15:18   -rw-r--r-- │
├─────────────────────────────────────────────────────────────────┤
│ 🔍 Quick Search: main_                 [ Next: ↓ ] [ Prev: ↑ ]  │
└─────────────────────────────────────────────────────────────────┘
```
 

1. **Inkrementelle Suche**: 
- Drücken Sie `Ctrl+S` (oder beginnen Sie einfach mit der Eingabe, sofern dies in den Einstellungen konfiguriert ist). 
– Am unteren Rand des aktiven Bedienfelds wird eine Überlagerungsleiste angedockt angezeigt. 

- Während Sie Zeichen eingeben, springt der Panel-Cursor in Echtzeit zum ersten passenden Eintrag. 
2. **Radsportwettkämpfe**: 
- Drücken Sie `Down Arrow` (`↓`), um zur nächsten passenden Datei zu springen. 
- Drücken Sie `Up Arrow` (`↑`), um zum vorherigen Spiel zu springen. 
- Drücken Sie `Enter`, um das übereinstimmende Element zu öffnen oder auszuführen. 
- Drücken Sie `Esc`, um die Suchleiste zu schließen, während der Cursor auf der gefundenen Datei bleibt. 
3. **Der Trailing-Dot-Trick**: 
- Geben Sie einen abschließenden Punkt ein (z. B. `config.`), um das Ende einer Dateinamenbasis genau anzupassen und `config.xml` von `configuration_guide.md` zu unterscheiden. 
4. **Schnellsuche vs. Filter vs. semantischer Filter**: 
- **Schnellsuche (`Ctrl+S` / `cm_QuickSearch`)**: Navigiert mit dem Cursor zwischen Treffern, während alle Dateien sichtbar bleiben. 
- **Schnellfilter (`cm_QuickFilter`)**: Versteckt vorübergehend alle nicht übereinstimmenden Dateien und zeigt nur übereinstimmende Zeilen in der Tabelle an. 
- **Semantischer Filter (`Ctrl+F` / `cm_SemanticFilter`)**: Verwendet natürliche Sprachabfragen (z. B. `/larger than 10MB`, `//today modified pdf`) über macOS Spotlight.

### Automatisch anpassende Spaltenmodi

Haben Sie genug von der manuellen Größenänderung von Spalten oder abgeschnittenen Dateinamen? ATBCmder verfügt über eine intelligente Spaltengrößen-Engine, die unter **Einstellungen** → **Dateiansichten** konfiguriert wird: 

1. **Maximale Textbreite (`mode="max"`)**: 
– Scannt alle sichtbaren Dateinamen und streckt die Namensspalte, sodass der längste sichtbare Dateiname ohne Auslassungspunkte vollständig lesbar ist (`...`). 

2. **Durchschnittliche Textbreite (`mode="average"`, Standard)**: 
– Wertet die statistische mittlere Zeichenbreite über Dateien hinweg multipliziert mit einem konfigurierbaren Füllfaktor (`auto_fit_padding`, Standard `1.0`) plus Symbolrändern aus. 

- **Vorteil**: Verhindert, dass ein einzelner ungewöhnlicher Dateiname mit 150 Zeichen alle sekundären Spalten (Größe, Datum, Berechtigungen) über den Bildschirmrand schiebt. 
3. **Feste Breiten (`mode="fixed"`)**: 
- Behält die exakten Spaltenpixelabmessungen bei. 
– Wird automatisch aktiviert, wenn Sie manuell ein Spaltentrennzeichen im Tabellenkopf ziehen, wobei Ihre manuellen Layoutanpassungen berücksichtigt werden.

### Horizontaler Dual-Panel-Modus (`Ctrl+Shift+H` / `⌃⇧H` / `cm_HorizontalFilePanels`)

Standardmäßig platziert ATBCmder die beiden Dateibereiche nebeneinander (vertikal geteilt). Auf Ultra-Wide-Monitoren oder vertikalen Hochformat-Displays können Sie zu gestapelten horizontalen Panels wechseln: 

![Horizontal Dual Panels Mode](images/horizontal_panels_view.png) 
*Horizontal gestapelte Paneelausrichtung mit Ober- und Unterpaneelen* 

- Wechseln Sie über das Menü **Anzeigen** → **Horizontale Panels-Modus** oder drücken Sie `Ctrl+Shift+H` (`cm_HorizontalFilePanels`). 
- Das Aktiv/Inaktiv-Paradigma bleibt identisch: Die Vorgänge fließen reibungslos zwischen den oberen (Quelle) und unteren (Ziel) Panels.

### Persistenz der Tab-Ansichtseinstellungen

In den meisten Dateimanagern erzwingt das Ändern der Sortierspalte oder der Wechsel von detaillierten Spalten zu Miniaturansichten eine globale Änderung des gesamten Fensters. 

ATBCmder isoliert und merkt sich die Ansichtseinstellungen auf der einzelnen **Tab-Ebene** (`TabState`), die über `SessionManager` (`atbcmder_session.xml`) automatisch über Neustarts hinweg beibehalten werden: 

- **Unabhängige Ansichtsmodi**: Sie können Tab 1 in der **Vollspaltenansicht** für Codeüberprüfungen, Tab 2 in der **Miniaturansicht-Rasteransicht** für Grafikelemente und Tab 3 in der **Kurzansicht** zum schnellen Überfliegen behalten. 
- **Unabhängige Sortierung**: Jede Registerkarte merkt sich ihre eigene Sortierspalte (Name, Erweiterung, Größe, Datum oder Berechtigungen) und Sortierrichtung (aufsteigend vs. absteigend). Durch das Wechseln zwischen Registerkarten werden Ihre Sortierprioritäten nie zurückgesetzt. 
- **Unabhängige Flat- und Tree-Zustände**: Eine Registerkarte, die auf **Flat Branch View** (`Cmd+B` / `cm_FlatView`) oder **Tree View Mode** eingestellt ist, behält ihre rekursive Verzeichnisreduzierung bei, ohne den Ansichtsstatus einer anderen Registerkarte in einem der Panels zu ändern. 

---

## 9. Praktische Schritt-für-Schritt-Rezepte

Hier sind drei Rezepte aus der Praxis, die zeigen, wie Navigation, Tabs und Hotlists kombiniert werden, um tägliche Aufgaben zu optimieren.

### Rezept 1: Aufbau eines persistenten Entwicklungsarbeitsbereichs

**Ziel**: Richten Sie einen Dual-Panel-Arbeitsbereich für die Full-Stack-Entwicklung ein, der jederzeit mit einem Klick wiederhergestellt werden kann. 

1. **Linkes Panel konfigurieren (Quellcode)**: 
- Navigieren Sie zu `~/Projects/MyApp/src`. 
- Öffnen Sie eine zweite Registerkarte (`Cmd+T`) und navigieren Sie zu `~/Projects/MyApp/tests`. 
- Klicken Sie mit der rechten Maustaste auf die Registerkarte `src` und wählen Sie **Registerkarte sperren** (`cmd_SetTabOptionLock`). 
2. **Rechtes Panel konfigurieren (Build & Logs)**: 
- Klicken Sie auf das rechte Feld, um es zu fokussieren (`Tab`). 
- Navigieren Sie zu `~/Projects/MyApp/dist`. 
- Öffnen Sie eine zweite Registerkarte (`Cmd+T`) und navigieren Sie zu `/var/log`. 
3. **Lieblingsarbeitsbereich speichern**: 
- Wählen Sie Menü **Favoriten** → **Aktuelle Tabs in neuen Favoriten-Tabs speichern** (`cm_SaveFavoriteTabs`). 
- Geben Sie `MyApp FullStack` ein und drücken Sie `Enter`. 
4. **Sofortige Wiederherstellung**: 
- Whenever you work on this project, simply select **Favorites** → **Load tabs from Favorite Tabs** (`cm_LoadFavoriteTabs`) and pick `MyApp FullStack`. Beide Panels konfigurieren sofort alle vier Registerkarten mit Ihren genauen Pfaden und Sperreinstellungen. 

---

### Rezept 2: Tiefe Verzeichnisbäume reduzieren, um aufgeblähte Assets zu finden

**Ziel**: Übergroße Testvorrichtungen und Protokollspeicherauszüge finden und bereinigen, die über Dutzende verschachtelter Unterordner verstreut sind. 

1. Navigieren Sie im aktiven Bereich zum Anfang Ihres Projekt- oder Medienverzeichnisses. 
2. Drücken Sie `Cmd+B` (`⌘B`) oder `Ctrl+B` (`cm_FlatView`), um **Flat Branch View** zu aktivieren. 
3. Beobachten Sie, wie alle Unterverzeichnisse im Panel rekursiv zu einer einzigen Liste zusammengefasst werden. 
4. Klicken Sie ein- oder zweimal auf die Spaltenüberschrift **Größe**, um alle Dateien vom größten zum kleinsten zu sortieren. 
5. Die größten Dateien im gesamten Verzeichnisbaum werden sofort oben im Bedienfeld angezeigt, wobei die Spalte **Pfad** ihre genauen verschachtelten Speicherorte anzeigt. 
6. Überprüfen oder löschen Sie die aufgeblähten Dateien direkt. 
7. Drücken Sie erneut `Cmd+B`, um die flache Ansicht zu deaktivieren und zur Standard-Ordnersuche zurückzukehren. 

---

### Rezept 3: Blitzschnelles Lesezeichen auf internen und Netzwerk-Volumes

**Ziel**: Setzen Sie ein Lesezeichen für einen Remote-NAS-Sicherungsordner und springen Sie in weniger als zwei Sekunden dorthin. 

1. Navigieren Sie zu Ihrem bereitgestellten Netzlaufwerk (z. B. `/Volumes/BackupShare/Archives`). 
2. Drücken Sie `Ctrl+D` (`⌃D`), um das Popup **Directory Hotlist** aufzurufen. 
3. Klicken Sie auf die Schaltfläche **Aktuelles Verzeichnis hinzufügen** (`btn_add` / `cm_AddDirToHotlist`). 
4. Geben Sie einen benutzerfreundlichen Namen ein, z. B. `NAS Archives`. 
5. Wenn Sie sich morgen irgendwo in Ihrem lokalen Dateisystem befinden, drücken Sie einfach `Ctrl+D`, geben Sie `nas` ein und drücken Sie `Enter`. ATBCmder transportiert Sie sofort über das Netzwerk zu genau diesem Ordner. 

---

## 10. Sicherheits- und Systemwarnungen

> [!NOTE] 
> **Externer Speicher und Netzwerkfreigaben**: 
> Stellen Sie beim Zugriff auf externe USB-Laufwerke oder Netzwerkfreigaben (`/Volumes/...`) über Registerkarten oder Lesezeichen sicher, dass das Volume derzeit bereitgestellt ist. Wenn beim Start von ATBCmder die Bereitstellung eines Laufwerks aufgehoben wird, wird auf Registerkarten, die darauf verweisen, sicher die Meldung „Speicherort nicht verfügbar“ angezeigt, anstatt dass es zum Absturz kommt oder die Registerkarte entfernt wird. 

> [!TIP] 
> **Tabs bereichsübergreifend spiegeln**: 
> Möchten Sie, dass Ihr rechter Bereich sofort alle geöffneten Registerkarten Ihres linken Bereichs widerspiegelt? Verwenden Sie das Menü **Tabs** → **Alle Tabs in den gegenüberliegenden Bereich kopieren** (`cm_CopyAllTabsToOpposite`), um Ihr Tab-Layout auf beiden Seiten zu reproduzieren. 

> [!WARNING] 
> **Achtung bei Vorgängen in der flachen Ansicht (`Cmd+B`)**: 
> In der flachen Zweigansicht werden Dateien aus mehreren unterschiedlichen Verzeichniszweigen nebeneinander in einer Liste angezeigt. Seien Sie vorsichtig, wenn Sie `Cmd+A` (Alle auswählen) gefolgt von `F8` (Löschen) oder `F6` (Verschieben) verwenden, da Ihre Aktion rekursiv auf alle verschachtelten Unterverzeichnisse angewendet wird. 

---

## 11. Referenztabelle für Dual-Matrix-Tastaturen

| Kategorie | Aktion | macOS-Verknüpfung | Klassischer Schlüssel | Interne Befehls-ID | 
| :--- | :--- | :--- | :--- | :--- | 
| **Verzeichnisnavigation** | Übergeordnetes Verzeichnis | `Backspace` / `⌘↑` | `Ctrl+PgUp` | `cm_ChangeDirToParent` | 
| | Stammverzeichnis | `Ctrl+\` / `⌃\` | `\` | `cm_ChangeDirToRoot` | 
| | Home-Verzeichnis | `Ctrl+Shift+Home` / `⌃⇧Home` | `Alt+Home` | `cm_ChangeDirToHome` | 
| | Erster Eintrag | `Home` | `Home` | `cm_GoToFirst` | 
| | Letzter Eintrag | `End` | `End` | `cm_GoToLast` | 
| **Ordnerregisterkarten** | Neuer Tab | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | 
| | Tab schließen | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | 
| | Doppelte Tabs schließen | *Tab-Kontextmenü* | — | `cm_CloseDuplicateTabs` | 
| | Alle Tabs schließen | *Tabs-Menü* | — | `cm_CloseAllTabs` | 
| | Registerkarte umbenennen | *Tab-Kontextmenü* | — | `cm_RenameTab` | 
| | Tabulatoren auf Gegenseite kopieren | *Tabs-Menü* | — | `cm_CopyAllTabsToOpposite` | 
| | Nächste Registerkarte | `Ctrl+Tab` / `⌃⇥` | `Ctrl+Tab` | `cm_NextTab` | 
| | Vorheriger Tab | `Ctrl+Shift+Tab` / `⌃⇧⇥` | `Ctrl+Shift+Tab` | `cm_PrevTab` | 
| | Registerkartenliste anzeigen | `Ctrl+Shift+L` / `⌃⇧L` | `Ctrl+Shift+L` | `cm_ShowTabsList` | 
| **Lieblings-Tabs** | Favoriten-Tabs speichern | *Favoritenmenü* | — | `cm_SaveFavoriteTabs` | 
| | Favoriten-Tabs laden | *Favoritenmenü* | — | `cm_LoadFavoriteTabs` | 
| | Aktiven Favoriten erneut speichern | *Favoritenmenü* | — | `cm_ResaveFavoriteTabs` | 
| | Aktiven Favoriten neu laden | *Favoritenmenü* | — | `cm_ReloadFavoriteTabs` | 
| | Favoriten-Tabs konfigurieren| *Einstellungen* | — | `cm_ConfigFavoriteTabs` | 
| **Hotlists & Verlauf** | Verzeichnis-Hotlist | `Ctrl+D` / `⌃D` | `Ctrl+D` | `cm_DirHotList` | 
| | Hotlist konfigurieren | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| | Verzeichnis zur Hotlist hinzufügen | *Hotlist-Popup* | — | `cm_AddDirToHotlist` | 
| | Geschichte rückwärts | `Cmd+[` / `⌘[` | `Alt+Left` | `cm_ViewHistoryPrev` | 
| | Geschichte vorwärts | `Cmd+]` / `⌘]` | `Alt+Right` | `cm_ViewHistoryNext` | 
| | Dropdown-Liste „Verlauf“ | `Alt+F8` / `⌥F8` | `Ctrl+Down` | `cm_DirHistory` | 
| **Laufwerke und Volumes** | Laufwerke auf der linken Seite | `Alt+F1` / `⌥F1` | `Alt+F1` | `cm_LeftOpenDrives` | 
| | Laufwerke auf der rechten Seite | `Alt+F2` / `⌥F2` | `Alt+F2` | `cm_RightOpenDrives` | 
| | Aktives Panel-Laufwerksmenü | `Alt+D` / `⌥D` | `Alt+D` | `cm_Drives` | 
| **Ansichtsmodi** | Vollständige Spaltenansicht | `Ctrl+F2` / `⌃F2` | `Ctrl+F2` | `cm_ColumnsView` | 
| | Kurzansicht | `Ctrl+F1` / `⌃F1` | `Ctrl+F1` | `cm_BriefView` | 
| | Miniaturansichten | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| | Baumansicht (Ersetzen) | *Menü anzeigen* | `Ctrl+Shift+F8` | `cm_TreeView` | 
| | Baumansicht (geteilt) | *Menü anzeigen* | — | `cm_TreeViewSplit` | 
| | Baumansicht (beide Panels)| *Menü anzeigen* | — | `cm_TreeViewBoth` | 
| | Flache Zweigansicht | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | 
| | Horizontaler Panel-Modus | `Ctrl+Shift+H` / `⌃⇧H` | `Ctrl+Shift+H` | `cm_HorizontalFilePanels` | 
| **Suche & Filter** | Schnellsuche-Overlay | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_QuickSearch` | 
| | Semantischer Filter | `Ctrl+F` / `⌃F` | `Ctrl+F` | `cm_SemanticFilter` |

--- 

<div align="center"> 
<p>Jetzt beherrschen Sie die Verzeichnisnavigation, Registerkarten und Bedienfeldansichten:</p> 
<p><strong><a href="file_operations.md">Fahren Sie mit Kapitel 3 fort: Tägliche Dateioperationen und Warteschlange &rarr;</a></strong></p> 
</div>