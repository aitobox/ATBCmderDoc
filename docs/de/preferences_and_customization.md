# Kapitel 7: Einstellungen & Anpassung

Ein wirklich effizienter Dateimanager muss sich an Ihren Arbeitsablauf anpassen und Sie nicht dazu zwingen, sich an seine Standardeinstellungen anzupassen. Jeder Ingenieur, Systemadministrator, digitale Archivar und Kreativprofi bringt unterschiedliche Muskelgedächtnis-, Anzeigeanforderungen und Betriebsgewohnheiten mit: Einige verlassen sich strikt auf die herkömmlichen Norton Commander/Total Commander-Funktionstasten (`F1`–`F10`), während andere native macOS-Verknüpfungen erwarten (`Cmd+C`, `Cmd+V`, `Cmd+O`); Einige erfordern eine dynamische automatische Spaltenanpassung mit typografischen Subpixelmetriken, während andere starre, feste Spaltengrenzen benötigen. Einige erfordern eine aggressive Echtzeitüberwachung von Dateisystemereignissen, während andere über Netzwerkfreigaben mit hoher Latenz laufen, bei denen passives Polling obligatorisch ist. 

ATBCmder ist von Grund auf auf vollständige Konfigurierbarkeit ausgelegt. Durch seinen modularen **Präferenzdialog** (`Cmd+,` / `⌘,` / `cm_Options`), den intuitiven **Hotkey-Editor** mit Echtzeit-Konflikterkennung, die intelligente **Column Auto-Fitting Engine**, anpassbare **Dateizuordnungen** mit externen Token-Makros und tragbare **ZIP-Konfigurationspakete** (`cm_ExportConfiguration`), Mit ATBCmder können Sie jede Dimension Ihrer Dual-Panel-Umgebung optimieren und Ihr maßgeschneidertes Setup nahtlos auf alle Ihre Mac-Systeme übertragen. 

---

## 1. Visueller Schnellstart: Das Einstellungscenter und die Befehlsmatrix

ATBCmder zentralisiert alle Benutzereinstellungen in einer einheitlichen Präferenzarchitektur, die aus 16 speziellen Konfigurationsseiten, einer isolierten Hotkey-Mapping-Engine und einer atomaren XML-Speicherebene besteht. 

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

### Spickzettel für Dual-Matrix-Einstellungen und -Anpassungen

| Aktion | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Einstellungen öffnen** | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | Öffnet das Hauptdialogfeld für mehrseitige Einstellungen. | 
| **Hotkeys konfigurieren** | `Cmd+,` ➔ Hotkeys | — | `cm_Options` (Hotkeys) | Direkter Zugriff auf die Tastaturkürzel-Bindungstabelle. | 
| **Dateizuordnungen konfigurieren**| Menü: Konfiguration | — | `cm_FileAssoc` | Ordnet Dateierweiterungen internen oder externen Viewern/Editoren zu. | 
| **Verzeichnis-Hotlist-Einrichtung** | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | Bearbeitet gespeicherte Ordner-Lesezeichen und aktive Hotkeys (`Ctrl+D` zum Öffnen der Hotlist). | 
| **Favoriten-Tabs konfigurieren** | Menü: Konfiguration | — | `cm_ConfigFavoriteTabs`| Verwaltet gespeicherte Dual-Panel-Ordner-Registerkartensätze. | 
| **Archiver konfigurieren** | Menü: Konfiguration | — | `cm_ConfigArchivers` | Konfiguriert externe Archiver-Ausführungsdateien und Komprimierungsregeln. | 
| **Konfiguration exportieren** | Menü: Konfiguration | — | `cm_ExportConfiguration`| Exportiert alle XML-Konfigurationsdateien in ein portables `.zip`-Bundle. | 
| **Konfiguration importieren** | Menü: Konfiguration | — | `cm_ImportConfiguration`| Stellt Konfigurations-XML-Dateien aus einem `.zip`-Bundle wieder her. | 
| **Konfigurationsverzeichnis öffnen** | Menü: Konfiguration | — | `cm_OpenConfigDirectory`| Navigiert vom aktiven Panel direkt zum Konfigurationsordner von ATBCmder. | 
| **Einstellungen sofort speichern** | Menü: Konfiguration | — | `cm_ConfigSaveSettings`| Löscht alle speicherinternen Konfigurationsänderungen sofort auf die Festplatte. | 
| **Fensterposition speichern** | Menü: Konfiguration | — | `cm_ConfigSavePos` | Behält die aktuelle Fenstergeometrie und die Teilerproportionen bei. | 
| **Datei-Tooltips umschalten** | Einstellungen: Dateiansichten | — | *(Einstellungen)* | Aktiviert oder deaktiviert detaillierte QuickInfos für schwebende Metadaten. | 
| **Systemberechtigungen erteilen** | Menü: Konfiguration | — | `cm_GrantFilesystemAccess`| Startet den Onboarding-Leitfaden für macOS App Sandbox Full Disk Access. | 

---

## 2. Anatomie und Navigation des Einstellungsdialogs (`Cmd+,` / `cm_Options`)

Der zentrale Kontrollraum für ATBCmder ist der **Einstellungsdialog**. Sie können es jederzeit aufrufen, indem Sie unter macOS **`Cmd+,`** (`⌘,`) drücken, im Anwendungsmenü **ATBCmder ➔ Einstellungen...** wählen oder `cm_Options` über die semantische Befehlsleiste (`/`) ausführen.

### 2.1 Dialoglayout und Interaktionsmodell

Das Dialogfeld „Einstellungen“ verwendet ein Master-Detail-Split-Layout, das auf Übersichtlichkeit und Tastaturzugänglichkeit ausgelegt ist: 

1. **Kategorie-Navigationsliste (links)**: Ein vertikaler Selektor mit einer lesbaren 14pt-Schnittstellenschriftart und einer festen 195-Pixel-Seitenleiste. Navigieren Sie zwischen den Kategorien mit den Pfeiltasten `Up` und `Down` oder klicken Sie mit der Maus. 
2. **Gestapelter Seiten-Bildlaufbereich (rechts)**: Ein weitläufiges Konfigurationsfenster, das in einem rahmenlosen `QScrollArea` eingeschlossen ist. Wenn Sie zwischen den Kategorien wechseln, wird die entsprechende Einstellungsseite reibungslos angezeigt, ohne dass sich die Dialoggröße ändert oder das Fenster flackert. 
3. **Aktionsschaltflächenmatrix (unten)**: 
- **OK**: Validiert alle Eingabefelder auf allen Seiten, schreibt geänderte Einstellungen auf die Festplatte (`atbcmder.xml`), löst eine Neuübersetzung und Designaktualisierungen aus und schließt den Dialog. 
- **Anwenden**: Übernimmt alle geänderten Parameter sofort, ohne den Dialog zu schließen. Dies ist ideal zum Testen von UI-Schriftarten, Designvariationen, Spaltenauffüllungen und automatischen Aktualisierungsintervallen in Echtzeit. 
- **Abbrechen**: Verwirft alle nicht gespeicherten Änderungen, die in der aktuellen Sitzung vorgenommen wurden. Wenn Sie eine Vorschau eines Themes ohne Anwendung angezeigt haben, setzt ATBCmder die Benutzeroberfläche automatisch auf Ihr vorheriges Theme zurück. 

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

### 2.2 Umfassendes Konfigurationsseitenverzeichnis

Jede Seite im Dialogfeld „Einstellungen“ befasst sich mit einer bestimmten Funktionsdomäne:

| Seite | Implementierungsmodul | Primäre Konfigurationskontrollen | 
| :--- | :--- | :--- | 
| **Allgemein** | `page_general.py` | Sichtbarkeit versteckter Dateien, Dateisymbole, Bestätigungsdialoge zum Löschen/Überschreiben, Integration in den Systempapierkorb, Puffergröße zum Kopieren/Verschieben (4 KB–10 MB), Themenauswahl, globale Schriftgröße, Umschalten zum Minimieren in die Taskleiste und globaler Hotkey zum Ein-/Ausblenden von Fenstern (`Cmd+Opt+H`). | 
| **Hotkeys** | `page_hotkeys.py` | Multikontext-Befehlssuche, primäre und sekundäre Shortcut-Akkordbindung, automatische Shortcut-Kollisionswarnungen und Zurücksetzen auf Werkseinstellungen. | 
| **Sprache** | `page_language.py` | Dynamischer Lokalisierungsselektor, der mehr als 30 Sprachen (Englisch, Deutsch, Französisch, vereinfachtes Chinesisch, Japanisch, Russisch, Spanisch usw.) mit sofortiger Live-Übersetzung der Benutzeroberfläche unterstützt. | 
| **Dateiansichten** | `page_fileview.py` | Groß-/Kleinschreibung berücksichtigende und natürliche numerische Sortierung, Ordnersortierung (Ordner zuerst, Dateien zuerst, gemischt), Platzierung neuer/aktualisierter Dateien, Modi für die automatische Spaltenanpassung (Fest, Durchschnitt, Max), Schieberegler für Auffüllfaktor und benutzerdefinierte Datums-/Uhrzeitformate. | 
| **Automatische Aktualisierung** | `page_auto_refresh.py` | Überwachung der Dateisystemerstellung/-löschung/-umbenennung, Überwachung von Dateiattributänderungen, Timer-Polling-Fallback-Intervall, Deaktivierung bei Hintergrundumschaltung und Verzeichnisausschlussfilterliste. | 
| **Operationen** | `page_operations.py` | Standardrichtlinien für Dateikollisionen (Fragen, Überschreiben, Überspringen, Ältere überschreiben, Ziel automatisch umbenennen), Richtlinien für Verzeichniskollisionen (Fragen, Zusammenführen, Überschreiben, Überspringen), Vorabzuweisung von freiem Speicherplatz, Handhabung von Symlinks, Beibehaltung von Berechtigungen/Zeitstempeln und Überprüfung. | 
| **Packer** | `page_packer.py` | Standardkomprimierungsarchivformat (`zip`, `7z`, `tar.gz`, `tar.bz2`, `tar.xz`, `tar`), externe ausführbare Pfade für 7-Zip, GNU Tar, Gzip, Bzip2- und XZ-Dienstprogramme. | 
| **Verzeichnis-Hotlist**| `page_hotlist.py` | Interaktiver Lesezeichen-Manager: Lieblingsverzeichnisse hinzufügen, entfernen und neu anordnen (`Drag & Drop`), Dual-Panel-Zielpfade angeben und Schnellzugriffstasten zuweisen. | 
| **Lieblings-Tabs** | `page_favorite_tabs.py` | Arbeitsbereich-Snapshot-Manager: Speichern, Umbenennen, Neuanordnen und Wiederherstellen von Verzeichnislayouts mit mehreren Registerkarten und zwei Bedienfeldern. | 
| **Herausgeber** | `page_editor.py` | Umschalten zwischen Schriftartfamilie, Schriftgröße, Tabstoppbreite, Zeilenumbruch und Zeilennummer im internen Code-Editor; Ausführbarer Pfad des externen Editors und Befehlszeilenargumente. | 
| **Zuschauer** | `page_viewer.py` | Universal Lister-Texttypografie, Tabstopps, Ränder, Zeilenumbruch, Caret-Sichtbarkeit, Bildwiedergabeoptionen (EXIF-Autorotation, Zoommodi, Transparenzraster) und externes Viewer-CLI-Tool. | 
| **Symbolleiste** | `page_toolbar.py` | Anpassung der oberen Schaltflächenleiste: Schieberegler für Symbolgröße (16–64 px), Schieberegler für Balkengröße, Stil für flache Schaltflächen, Umschalten von Beschriftungen, Befehlshierarchiebaum und benutzerdefiniertes Dialogfeld zur Symbolauswahl. | 
| **Mittlere Symbolleiste** | `page_toolbar.py` | Konfiguration der vertikalen Splitter-Symbolleiste in der Mitte: Symbolgrößen, Aktionsschaltflächen und Neuordnung des Layouts. | 
| **Protokoll** | `page_log.py` | Betriebsüberwachungsprotokollierung: Protokolldateiziel, Token-Pfad-Ersetzung, maximale Protokolldateigröße, Protokollrotationsverhalten und spezifische Vorgangsereignisfilter (Kopieren, Verschieben, Löschen, Entpacken). | 
| **Schnellsuche** | `page_quicksearch.py` | Tastatur-Schnellsuchmodus (genaue Übereinstimmung, Anfang, Ende, Platzhalter), Berücksichtigung der Groß-/Kleinschreibung und Zeitüberschreitung beim automatischen Schließen. | 
| **Semantischer Filter** | `page_semantic_filter.py` | Verhalten der eingebetteten Befehlsleiste in natürlicher Sprache (`/`), Suchanbieter-Backends und Entprellen von Vorschlägen. | 
| **Registerkarten** | `page_tabs.py` | Erscheinungsbild der Ordnerregisterkarte: Sichtbarkeit der Schaltfläche „Schließen“, mehrzeiliges Registerkartenlayout im Vergleich zu scrollenden Registerkarten, Navigationsverhalten bei gesperrten Registerkarten und Bestätigungen zum Schließen von Registerkarten. |

---

### 2.3 Echtzeit-Design und dynamische Sprachumschaltung

Im Gegensatz zu älteren Dienstprogrammen, die das Schließen und Neustarten der Anwendung nach dem Ändern der Darstellungseinstellungen erfordern, bietet ATBCmder **Hot-Swap-fähige Theming und Lokalisierung**: 

1. **Themenvorschau**: Öffnen Sie **Allgemein**, wählen Sie zwischen `Classic`, `Light`, `Dark` oder `macOS Native (Stylish)` und beobachten Sie die Änderung des Fensterstils sofort über die Qt-Stylesheet-Injection. Wenn Sie **Abbrechen** drücken, wird das vorherige Design nahtlos wiederhergestellt. 
2. **Sofortübersetzung**: Öffnen Sie **Sprache**, wählen Sie Ihren bevorzugten Dialekt aus der Liste von über 30 übersetzten Gebietsschemata aus und klicken Sie auf **Übernehmen**. Der Fenstertitel, die Kategorieseitenleiste, Menüs, Schaltflächen, Statusleisten und Dialogaufforderungen werden über die dynamische `tr()`-Übersetzungspipeline von ATBCmder sofort in die Zielsprache neu gerendert. 

![Language Settings](images/language_settings.png) 
*Abbildung 7.1: Die Seite „Spracheinstellungen“ ermöglicht eine sofortige Lokalisierung ohne Neustart in über 30 unterstützten Sprachen.* 

---

## 3. Anpassung von Tastaturkürzeln und Konfliktmanagement

Tastatureffizienz ist die Kernphilosophie der Dual-Panel-Dateiverwaltung. Der **Hotkey-Editor** (`page_hotkeys.py`) von ATBCmder bietet vollständige Kontrolle über Shortcut-Akkorde und erzwingt gleichzeitig eine strikte Kontextisolierung und Kollisionsverhinderung. 

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

### 3.1 Kontextisolation und Scoping

Um eine Erschöpfung der Tastenkombinationen zu vermeiden, unterteilt ATBCmder Tastenkombinationen in **Kontextbereiche**. Eine in einem Kontext definierte Tastenkombination beeinträchtigt nicht identische Tasten in unabhängigen Fenstern: 

- **Haupt**: Globale Anwendungsverknüpfungen, die in allen Fenstern verfügbar sind (z. B. `Cmd+,` für Einstellungen, `Cmd+Q` für Beenden). 
- **FilePanel**: Aktiv, wenn die linke oder rechte Dateiliste den Tastaturfokus hat (z. B. `F5` kopiert, `Space` berechnet die Verzeichnisgröße, `Backspace` navigiert zum übergeordneten Verzeichnis). 
- **Viewer**: Aktiv im Universal Lister (`F3`): Steuert Textkodierungen, Umschalten der Hex-Ansicht (`2` / Hex-Modus), Bildzoom und Medienwiedergabe. 
- **Editor**: Aktiv im integrierten Texteditor (`F4`): Steuert Syntaxhervorhebung, Einrückung, Suchen/Ersetzen (`Cmd+F`) und Dateispeicherung (`Cmd+S`). 
- **Unterschied**: Aktiv innerhalb des Side-by-Side-Dateiunterschieds: Hunk-Navigation (`F7`/`F8`), Zeilensynchronisierung und Zusammenführungsvorgänge. 
- **FindFiles**: Aktiv im Dialogfeld „Multifilter-Suche“: Auslösen neuer Suchen, Navigieren in den Ergebnissen und Einspeisen in die Listbox. 
- **MultiRename**: Aktiv im Batch Multi-Rename-Tool: Zählermanipulation, Token-Einfügung und Ausführung. 

---

### 3.2 Dual-Binding-Architektur (primäre und sekundäre Verknüpfungen)

Mit ATBCmder können Sie jedem einzelnen Befehl **zwei unterschiedliche Tastenkombinationen** zuweisen: 

- **Primärer Kurzbefehl**: Ihr primärer Muskelgedächtnisakkord (z. B. `F5` für klassische Commander-Benutzer). 
- **Sekundäre Tastenkombination**: Ein alternativer Akkord (z. B. `Cmd+C` für native macOS-Ergonomie). 

Beide Tastenkombinationen bleiben im angegebenen Kontext gleichzeitig aktiv. Beim Navigieren in Menüs zeigt ATBCmder automatisch die primäre Verknüpfung neben dem Text des Menüelements an, um eine klare visuelle Referenz zu gewährleisten. 

---

### 3.3 Schritt-für-Schritt-Anleitung: Anpassen einer Tastenkombination

Befolgen Sie diese praktische Anleitung, um einen vorhandenen Befehl erneut zu binden oder eine sekundäre Verknüpfung zuzuweisen: 

1. Drücken Sie **`Cmd+,`** (`⌘,`), um die Einstellungen zu öffnen, und wählen Sie in der linken Seitenleiste **Hotkeys** aus. 
2. Wählen Sie den entsprechenden **Hotkey-Kontext** aus der Dropdown-Liste aus (z. B. `FilePanel`). 
3. Geben Sie den Befehlsnamen oder ein Schlüsselwort in das Feld **Filterbefehle** ein (z. B. `Wipe` oder `Terminal`). Die Tabelle filtert passende Einträge in Echtzeit. 
4. Doppelklicken Sie auf die Befehlszeile oder wählen Sie die Zeile aus und klicken Sie auf **Bearbeiten...**. 
5. Im Dialogfeld **Hotkey bearbeiten**: 
- Klicken Sie in das Feld **Primäre Verknüpfung** und drücken Sie die gewünschte Tastenkombination (z. B. `Ctrl+Alt+T`). ATBCmder erfasst den Akkord sauber und beschränkt die Sequenzen auf einen einzelnen gleichzeitigen Akkord. 
- (Optional) Klicken Sie in das Feld **Sekundäre Verknüpfung** und drücken Sie eine alternative Kombination (z. B. `Cmd+Shift+T`). 
6. Klicken Sie auf **Speichern**. 

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

### 3.4 Automatische Kollisionserkennung und Konfliktwarnungen

Wenn Sie versuchen, einen Schlüsselakkord zuzuweisen, der bereits von einem anderen Befehl im selben Kontext beansprucht wird, greift die Kollisionserkennungs-Engine von ATBCmder sofort ein. Ein Warndialog zeigt die widersprüchliche Zuweisung an: 

> [!WARNING] 
> **Verknüpfungskonflikt erkannt** 
> Die Verknüpfung `Ctrl+M` ist `cm_MultiRename` im Kontext `FilePanel` bereits zugewiesen. 
> Möchten Sie es überschreiben und `Ctrl+M` zu `cm_MarkCurrentExtension` neu zuweisen? 

- Wenn Sie auf **Ja** klicken, wird `Ctrl+M` automatisch vom alten Befehl entbunden und auf Ihren neu ausgewählten Befehl angewendet. 
- Wenn Sie auf **Nein** klicken, wird die Bearbeitung abgebrochen und vorhandene Bindungen bleiben ohne Änderung erhalten. 

---

### 3.5 Globaler Hotkey zum Ein-/Ausblenden von Fenstern (`Cmd+Opt+H` / `Ctrl+Alt+H`)

Für Power-User, die ATBCmder lieber unauffällig im Hintergrund laufen lassen möchten: 

1. Öffnen Sie **Einstellungen ➔ Allgemein**. 
2. Aktivieren Sie **In Taskleiste minimieren**. 
3. Suchen Sie nach **Fenster-Hotkey anzeigen/ausblenden** (Standard: `Ctrl+Alt+H` / `⌘⌥H`). 
4. Klicken Sie auf das Sequenzfeld, um einen benutzerdefinierten globalen Hotkey-Akkord zu registrieren. 
5. Klicken Sie auf **Übernehmen**. 

Sie können ATBCmder jetzt von überall in macOS sofort in den Vordergrund rufen oder in den Hintergrund verdrängen, selbst wenn Sie in anderen Vollbildanwendungen arbeiten. 

---

## 4. Dateiansichten, Spaltenmodi und Miniaturansichtsverwaltung

Die Seite **Dateiansichten** (`page_fileview.py`) regelt, wie Verzeichnisse gerendert, gemessen, sortiert und in den Doppelfenstern dargestellt werden. 

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

### 4.1 Column Auto-Fitting Engine: Die drei Modi

Dateimanager mit zwei Bedienfeldern haben oft Probleme mit unterschiedlichen Dateinamenlängen: Zu breite Spalten verursachen horizontales Scrollen, während zu schmale Spalten wichtige Dateierweiterungen abschneiden. ATBCmder löst dieses Problem mit drei unterschiedlichen automatischen Anpassungsverhalten: 

1. **Fester Modus (`fixed`)**: 
- Deaktiviert die automatische Neuberechnung. 
- Die Spaltenbreiten bleiben genau dort, wo Sie sie positionieren. 
- **Manuelles Ziehen**: Wenn Sie den vertikalen Rand zwischen Spaltenüberschriften ziehen (z. B. zwischen `Name` und `Ext`), erfasst ATBCmder die genaue Pixelbreite und speichert sie separat für jede Panel-Seite (`column_widths_left` und `column_widths_right` in). `atbcmder.xml`). 
2. **Durchschnittsmodus (`average` – empfohlene Standardeinstellung)**: 
– Wertet die mittlere typografische Breite (`QFontMetrics`) aller im Verzeichnis sichtbaren Dateinamen aus. 

- Multipliziert die durchschnittliche Breite mit Ihrem konfigurierten **Padding-Faktor** (Schieberegler einstellbar von `1.0x` bis `5.0x`, Standard `1.0x`–`1.25x`) und fügt 40 Pixel für Dateitypsymbole und visuellen Freiraum hinzu. 
– Verhindert, dass extreme Ausreißer-Dateinamen (z. B. ein einzelner Protokolldateiname mit 120 Zeichen) alle anderen Spalten aus dem Bildschirm verdrängen. 

3. **Maximaler Breitenmodus (`max`)**: 
– Scannt Verzeichniseinträge und erweitert die Spalte, sodass sie dem breitesten einzelnen Dateinamen plus Sicherheitsabstand (+50 Pixel) entspricht. 
– Garantiert, dass null Dateinamen mit Auslassungspunkten (`...`) gekürzt werden, ideal für Medienarchive und wissenschaftliche Datensätze. 

> [!TIP] 
> **Optimierung großer Verzeichnisse**: 
> In Verzeichnissen mit Zehntausenden von Elementen würde die Messung jeder einzelnen Zeichenfolge die Schnittstelle einfrieren. ATBCmder wendet automatisch die intelligente Schrittstichprobe (`_MAX_SAMPLE = 200`) an und wertet eine gleichmäßig verteilte Teilmenge von Zeilen aus, um Typografiemetriken in weniger als 2 Millisekunden zu berechnen, während übergeordnete Verzeichnismarkierungen (`..`) ignoriert werden. 

---

### 4.2 Dateisortieroptionen

Passen Sie die Reihenfolge der Elemente in den Tabellenansichten genau an: 

- **Natürliche (numerische) Sortierung**: Wenn diese Option aktiviert ist, werden Zahlen innerhalb von Zeichenfolgen mathematisch verglichen: `file1.txt`, `file2.txt`, `file10.txt` (anstelle der alphabetischen `file1.txt`, `file10.txt`, `file2.txt`). 
- **Sortierung nach Groß-/Kleinschreibung**: Wenn diese Option aktiviert ist, stehen Großbuchstaben vor Kleinbuchstaben entsprechend den ASCII-/Unicode-Ordinalwerten (`File.txt` sortiert vor `apple.txt`). Wenn diese Option deaktiviert ist, wird bei der Sortierung die Groß-/Kleinschreibung nicht beachtet. 
- **Ordnersortiermodus**: 
- `Folders first`: Verzeichnisse werden oben im Panel über allen Dateien gruppiert. 
- `Files first`: Dateien werden zuerst aufgelistet, Verzeichnisse ganz unten. 
- `Mixed`: Dateien und Ordner werden alphabetisch in einer einheitlichen Reihenfolge sortiert. 
- **Position neuer und aktualisierter Dateien**: Steuern Sie, wo neu erstellte oder kürzlich geänderte Dateien während Live-Dateisystemaktualisierungen angezeigt werden (`Sorted`, `Top` oder `Bottom`). 

---

### 4.3 Miniaturbild-Rasteransicht und Cache-Mechanik

Für Fotografen, Designer und Videobearbeiter bietet ATBCmder eine integrierte **Thumbnail Grid View** (`cm_ThumbnailsView`), die tabellarische Zeilen durch visuelle Bildvorschauen ersetzt. 

![Thumbnail Grid View](images/thumbnails_grid_view.png) 
*Abbildung 7.2: Hochleistungs-Miniaturansicht mit Bildvorschau mit benutzerdefiniertem Rasterabstand.*

#### Größenanpassung und dynamisches Zoomen

- **Standard-Miniaturbildgröße**: Konfigurierbar von 48 px bis 512 px (Standard: 128 px). 
- **Interaktives Pinch-to-Zoom**: Verwenden Sie auf Apple-Trackpads standardmäßige Pinch-Gesten mit zwei Fingern oder halten Sie **`Ctrl`** gedrückt, während Sie mit dem Mausrad scrollen, um Miniaturansichten dynamisch in Echtzeit zu skalieren.

#### Mehrschichtige Caching-Architektur

Das Generieren von Miniaturansichten für hochauflösende 48-Megapixel-RAW-Fotos oder komplexe Vektor-SVGs ist rechenintensiv. ATBCmder verwendet eine robuste zweistufige Caching-Architektur: 

1. **In-Memory LRU Cache**: Behält 500 dekomprimierte `QPixmap`-Objekte im RAM für sofortiges, seidenweiches Scrollen mit 60 Bildern pro Sekunde. 
2. **Persistenter Festplatten-Cache**: Lokal in Ihrem Benutzer-Cache-Verzeichnis gespeichert: 
- macOS-/Linux-Pfad: `~/.cache/atbcmder/thumbnails/` 
– Cache-Schlüssel werden über kryptografische SHA-256-Hashes generiert, die Dateipfad, Dateiänderungszeitstempel (`mtime`), angeforderte Pixelgröße und Cache-Schema-Version kombinieren: 
$$\text{Cache-Schlüssel} = \text{SHA256}(\text{Dateipfad} + \text{mtime} + \text{Größe} + \text{Version})$$ 
– Wenn eine Bilddatei auf der Festplatte bearbeitet oder aktualisiert wird, ändert sich ihr Zeitstempel, wodurch veraltete Cache-Einträge sofort ungültig werden und ein automatisches Neu-Rendering im Hintergrund ausgelöst wird. 

3. **Hintergrund-Worker-Threads**: Die Bildverarbeitung wird mithilfe von Pillow (PIL) oder hardwarebeschleunigten `QImage`-Pipelines auf einen dedizierten `QThread`-Worker-Pool ausgelagert, wodurch gewährleistet wird, dass die Dual-Panel-Schnittstelle bei umfangreichen Batch-Importen nie ins Stocken gerät. 

---

### 4.4 Benutzerdefinierte Formatierung von Datum und Uhrzeit

Mit ATBCmder können Sie benutzerdefinierte Zeitstempel-Formatierungszeichenfolgen mithilfe der Standard-Python-Syntax `strftime` definieren: 

- **Langes Datum/Uhrzeit-Format** (Standard: `%Y-%m-%d %H:%M:%S`): Steuert die Datumsanzeige in der Vollspaltenansicht (`2026-09-06 14:30:00`). 
- **Format der Synchronisierungsverzeichnisse** (Standard: `%Y.%m.%d %H:%M:%S`): Steuert die Zeitstempeldarstellung im Dialogfeld „Directory Synchronizer“. 

| Token | Beschreibung | Beispielausgabe | 
| :--- | :--- | :--- | 
| `%Y` | 4-stelliges Jahr | `2026` | 
| `%m` | 2-stelliger Monat (`01`–`12`) | `09` | 
| `%d` | 2-stelliger Tag des Monats (`01`–`31`) | `06` | 
| `%H` | 2-stellige Stunde im 24-Stunden-Format (`00`–`23`) | `14` | 
| `%I` | 2-stellige Stunde im 12-Stunden-Format (`01`–`12`) | `02` | 
| `%p` | AM/PM-Bezeichnung | `PM` | 
| `%M` | 2-stellige Minute (`00`–`59`) | `30` | 
| `%S` | 2-stellige Sekunde (`00`–`59`) | `15` | 

---

## 5. Automatische Aktualisierung des Dateisystems und Überwachung der Empfindlichkeit

Bei der Zusammenarbeit an gemeinsam genutzten Codebasen, beim Herunterladen von Browser-Assets oder beim Ausführen von Kompilierungsaufgaben im Hintergrund ändern sich die Verzeichnisinhalte ständig. Die Seite **Auto Refresh** (`page_auto_refresh.py`) gleicht die Genauigkeit der Benutzeroberfläche in Echtzeit mit dem CPU- und Batterieverbrauch ab. 

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

### 5.1 Ereignisauslöser vs. Polling-Fallback

ATBCmder kombiniert die native Ereignisüberwachung des Betriebssystems mit einem intelligenten Polling-Fallback: 

- **Ereignisüberwachung (`watch_file_name_change`)**: Nutzt native Betriebssystem-Kernel-Benachrichtigungen (macOS `FSEvents` / `kqueue`), um das Erstellen, Löschen und Umbenennen von Dateien ohne CPU-Overhead zu erkennen. 
- **Attributüberwachung (`watch_attributes_change`)**: Verfolgt Dateigrößenerweiterungen, Zeitstempelaktualisierungen und Anpassungen des Berechtigungsmodus. 
- **Polling-Fallback-Intervall (`attr_poll_interval`)**: Konfigurierbar von 1 bis 60 Sekunden (Standard: 5 Sekunden). 
*Warum ist eine Abfrage erforderlich?* Remote-Netzwerkspeicher-Mounts (SMB, CIFS, NFS, SFTP VFS) geben häufig keine nativen Betriebssystem-Dateisystemereignisse aus, wenn Remote-Clients Änderungen vornehmen. Der Hintergrundabfrage-Timer stellt sicher, dass Ihre Remote-Panel-Listen nie veraltet sind. 

---

### 5.2 Batterie- und CPU-Einsparung: Bei Hintergrundbetrieb deaktivieren

Auf macOS-Laptops, die mit Batteriestrom betrieben werden, können aktive Dateisystem-Watcher unnötig Strom verbrauchen. 

- Durch Aktivieren von **Wenn die Anwendung im Hintergrund läuft** (`watch_only_foreground`) werden automatisch alle aktiven Abfrage-Timer und Ereignisbeobachter angehalten, sobald ATBCmder den Fensterfokus verliert. 
- Wenn Sie zurück zu ATBCmder wechseln, führen die Panels sofort eine einzige koordinierte Aktualisierung durch, wodurch alle Verzeichnislisten sofort auf den neuesten Stand gebracht werden. 

---

### 5.3 Pfadausschlussfilter

Verzeichnisse mit hoher Fluktuation – wie `node_modules`, Git-Metadaten-Repositorys (`.git`), Kompilierungsartefakt-Caches (`target/`, `build/`) und lokale Datenbankdateien – generieren Tausende von Festplattenereignissen pro Minute. 

1. Überprüfen Sie **Für die folgenden Pfade und ihre Unterverzeichnisse** (`watch_exclude_dirs`). 
2. Geben Sie im Ausschlusstextbereich einen absoluten Verzeichnispfad pro Zeile ein: 
   ```text
   /Users/username/Developer/project/node_modules
   /Users/username/Developer/linux/.git
   /Volumes/ProductionNAS/RenderingQueue
   ```
 

3. Klicken Sie auf **Übernehmen**. ATBCmder ignoriert Dateisystemereignisse, die in diesen Pfadbäumen auftreten, und verhindert so unerwünschte Aktualisierungen der Benutzeroberfläche und CPU-Spitzen. 

---

## 6. Benutzerdefinierte Dateizuordnungen und externe Tool-Integration

Wenn Sie auf eine Datei doppelklicken oder **`Enter`** drücken, wird sie normalerweise mit der Standardsystemanwendung geöffnet. Mit dem **Dateizuordnungssystem** (`cm_FileAssoc` / `file_associations.py`) von ATBCmder können Sie benutzerdefinierte Aktionen für bestimmte Dateimuster definieren und diese internen Befehlen oder externen Terminal-/GUI-Anwendungen zuordnen.

### 6.1 Architektur und Musterspezifität

Dateizuordnungen werden in der Reihenfolge der Musterspezifität ausgewertet: Das längste und spezifischste Glob-Muster wird zuerst abgeglichen: 

$$\text{Spezifitätsreihenfolge: } \texttt{*.min.js} \longrightarrow \texttt{*.js} \longrightarrow \texttt{text/*} \longrightarrow \texttt{*}$$ 

Jede Zuordnung kann mehrere Aktionen enthalten (z. B. „In VS-Code öffnen“, „Hex anzeigen“, „In Python ausführen“), wobei eine davon als primäre Standardaktion festgelegt ist, die am `Enter` ausgelöst wird. 

---

### 6.2 Token-Makro-Ersetzungen für externe Befehle

Beim Starten externer Tools oder Befehlszeilenskripts ersetzt ATBCmder automatisch Token-Makros durch die Metadaten der aktiven Datei: 

| Makro-Token | Bedeutung | Beispielwert | 
| :--- | :--- | :--- | 
| **`%f`** | Vollständiger absoluter Pfad der ausgewählten Datei | `/Users/username/Documents/report.pdf` | 
| **`%d`** | Verzeichnispfad, der die Datei | enthält `/Users/username/Documents` | 
| **`%n`** | Basisdateiname ohne Erweiterung | `report` | 
| **`%e`** | Dateierweiterung ohne führenden Punkt | `pdf` | 

---

### 6.3 Praktische Assoziationsrezepte

#### Rezept 1: Öffnen Sie Python-Skripte in Visual Studio Code

- **Muster**: `*.py` 
- **Etikett**: `Edit in VS Code` 
- **Befehl**: `code %f` 
- **Aktionstyp**: Externer Shell-Befehl

#### Rezept 2: Python-Skript im Terminal ausführen

- **Muster**: `*.py` 
- **Etikett**: `Execute Script` 
- **Befehl**: `python3 %f` 
- **Aktionstyp**: Externer Shell-Befehl

#### Rezept 3: Markdown im dedizierten Previewer anzeigen

- **Muster**: `*.md` 
- **Etikett**: `Preview in Typora` 
- **Befehl**: `open -a Typora %f` 
- **Aktionstyp**: Externer Shell-Befehl

#### Rezept 4: Vergleichen Sie die Datei mit dem gegenüberliegenden Panel in Beyond Compare

- **Muster**: `*` 
- **Etikett**: `Compare with Target` 
- **Befehl**: `bcomp %f %d` 
- **Aktionstyp**: Externer Shell-Befehl 

---

## 7. Anpassung der Symbolleiste und der mittleren Symbolleiste

ATBCmder bietet zwei anpassbare Symbolleisten: die **Hauptsymbolleiste** unterhalb der Menüleiste und die **mittlere Symbolleiste**, die vertikal in den Splitter eingebettet ist und die beiden Dateibereiche trennt. 

![Middle Toolbar](images/middle_toolbar.png) 
*Abbildung 7.3: Die Optionsseite der mittleren Symbolleiste zum Konfigurieren von Splitterschaltflächen und Schnellaktionsauslösern.*

### 7.1 Anpassen des Erscheinungsbilds der Symbolleiste

Öffnen Sie **Einstellungen ➔ Symbolleiste** oder **Einstellungen ➔ Mittlere Symbolleiste**: 

- **Leistengrößen-Schieberegler**: Passt die Höhe/Breite der Symbolleiste von 16 px bis 64 px an. 
- **Schieberegler für die Symbolgröße**: Skaliert Schaltflächensymbole von 16 px auf 64 px (Standard: 24 px). 
- **Flache Knöpfe**: Schaltet zwischen modernen flachen randlosen Knöpfen und klassischen erhabenen Knöpfen um. 
- **Untertitel anzeigen**: Zeigt Textbeschriftungen unter oder neben Symbolleistensymbolen an. 

---

### 7.2 Elemente hinzufügen und die integrierte Symbolauswahl

Symbolleistenelemente sind in einer hierarchischen Baumstruktur organisiert, die drei Elementtypen unterstützt: 

1. **Trennzeichen**: Fügt eine visuelle Trennlinie oder einen Abstandshalter zwischen Schaltflächengruppen ein. 
2. **Interner Befehl**: Wählen Sie mithilfe des automatisch vervollständigenden Befehlsfelds einen der über 230 `cm_*`-Befehle von ATBCmder aus. 
3. **Externer Befehl**: Geben Sie einen externen Shell-Befehl, ein Arbeitsverzeichnis und Parametertokens an (`%f`, `%d`).

#### Die integrierte Symbolauswahl (`IconPickerDialog`)

Klicken Sie beim Konfigurieren benutzerdefinierter Schaltflächen auf die Symbolvorschau-Schaltfläche, um den integrierten **Icon Picker** zu öffnen: 

- Verfügt über einen sofortigen Suchfilter für Hunderte von gebündelten SVG- und PNG-Symbolen. 
- Zeigt Symbole in einem einheitlichen Raster mit hochauflösender Vorschau und Asset-Stammnamen an. 

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

### 7.3 Anpassung der Verzeichnis-Hotlist und der Favoriten-Registerkarten

- **Verzeichnis-Hotlist (`page_hotlist.py`)**: Verwalten Sie Ihre `Ctrl+D`-Lesezeichen. Fügen Sie aktuelle Pfade hinzu, ordnen Sie Lesezeichen per Drag-and-Drop neu an, konfigurieren Sie die Synchronisierung des Zielbereichs und weisen Sie Zugriffsschlüssel zu. 
- **Lieblingsregisterkarten (`page_favorite_tabs.py`)**: Speichern Sie vollständige Dual-Panel-Arbeitsbereichslayouts mit mehreren Registerkarten. Stellen Sie Ihre genauen Entwicklungs- oder Fotobearbeitungsverzeichnissätze mit einem Klick wieder her. 

![Directory Hotlist](images/quick_access_paths.png) 
*Abbildung 7.4: Verzeichnis-Hotlist-Lesezeichen und -Pfade verwalten.* 

---

## 8. Konfigurationsportabilität und isolierter Testmodus

Ob Sie auf einen neuen Mac migrieren, eine Flotte von Entwicklungsmaschinen bereitstellen oder benutzerdefinierte Tastenkombinationen mit Kollegen teilen, ATBCmder macht die Sicherung und Bereitstellung von Konfigurationen zum Kinderspiel.

### 8.1 Konfigurationsspeicherarchitektur

ATBCmder speichert alle Benutzereinstellungen in sauber strukturierten, für Menschen lesbaren XML-Dateien, die sich in Ihrem Standard-Betriebssystemkonfigurationsverzeichnis befinden: 

- **macOS-Standardpfad**: 
`~/Library/Einstellungen/atbcmder/` 

- **macOS App Sandbox-Pfad**: 
`~/Library/Containers/com.aitobox.atbcmder/Data/Library/Einstellungen/atbcmder/` 

- **Linux-/UNIX-Pfad**: 
`~/.config/atbcmder/` 

- **Direktzugriffsbefehl**: 
Führen Sie **`cm_OpenConfigDirectory`** aus (oder wählen Sie **Konfiguration ➔ Konfigurationsverzeichnis öffnen** aus dem Menü), um im aktiven Panel sofort direkt zu diesem Ordner zu navigieren. 

```
~/Library/Preferences/atbcmder/
├── atbcmder.xml          # Core application configuration, geometry, themes, view rules
├── atbcmder_hotkeys.xml  # User keyboard shortcut overrides and custom bindings
├── favtabs.xml           # Saved favorite folder tab layouts and paths
├── hotlist.xml           # Directory Hotlist (Ctrl+D) bookmarks hierarchy
└── history.xml           # Recent directory jumps, command line history, search history
```
 

---

### 8.2 Konfigurationspakete exportieren (`cm_ExportConfiguration`)

So erstellen Sie ein tragbares All-in-One-Backup Ihrer ATBCmder-Umgebung: 

1. Wählen Sie **Konfiguration ➔ Konfiguration exportieren...** aus der Menüleiste (oder führen Sie `cm_ExportConfiguration` aus). 
2. Wählen Sie Ihr Zielverzeichnis und einen Dateinamen (Standard: `atbcmder-config.zip`). 
3. Klicken Sie auf **Speichern**. 

ATBCmder schreibt alle ausstehenden Speicheränderungen auf die Festplatte, sammelt alle Konfigurations-XML-Dateien (`atbcmder.xml`, `atbcmder_hotkeys.xml`, `favtabs.xml`, `hotlist.xml`) und verpackt sie in ein atomares, komprimiertes ZIP-Archiv. 

---

### 8.3 Konfigurationspakete importieren (`cm_ImportConfiguration`)

So stellen Sie eine Konfigurationssicherung auf einem neuen Computer wieder her oder stellen einen bekanntermaßen guten Zustand wieder her: 

1. Wählen Sie **Konfiguration ➔ Konfiguration importieren...** aus der Menüleiste (oder führen Sie `cm_ImportConfiguration` aus). 
2. Wählen Sie Ihr zuvor exportiertes `atbcmder-config.zip`-Archiv aus. 
3. Bestätigen Sie die Warnmeldung: 
> Durch den Import werden alle aktuellen Einstellungen durch den Inhalt der ausgewählten Datei ersetzt. Weitermachen? 
4. Klicken Sie auf **Ja**. 

ATBCmder entpackt das Archiv sicher, überprüft, ob alle extrahierten Dateien gültige XML-Konfigurationen sind, ersetzt aktive Festplattendateien, lädt den internen Singleton `Config()` neu und aktualisiert sowohl Dateibereiche als auch Spaltenlayouts sofort – alles ohne einen Neustart der Anwendung erforderlich. 

> [!IMPORTANT] 
> **Unternehmenssicherheit: Anti-Traversal-Schutz** 
> ATBCmder erzwingt eine strikte Pfadüberquerungsvalidierung während des Konfigurationsimports (`zipfile` Bereinigung). Jedes Archivmitglied, das Pfadtrennzeichen (`/`, `\`), Verzeichnisdurchläufe (`..`) oder Nicht-XML-Dateierweiterungen enthält, wird sofort abgelehnt und schützt so Ihr Betriebssystem vor böswilligen Archivmanipulationen. 

---

### 8.4 Isolierter Testmodus (`ATBCmder_test.sh`)

Wenn Sie benutzerdefinierte Plugins entwickeln, mit aggressiven Hotkey-Rebindings experimentieren oder Beta-Konfigurationen testen, sollten Sie es vermeiden, Ihre tägliche Treiberkonfiguration zu ändern. 

ATBCmder unterstützt die vollständige Konfigurationsumleitung über die Umgebungsvariable `ATBCMDER_CONFIG_PATH`. Ein spezielles Testskript ist im Projekt-Repository enthalten: 

```bash
# Launch ATBCmder in completely isolated test mode:
./scripts/ATBCmder_test.sh
```

#### So funktioniert der isolierte Testmodus:

1. Stellt ein sauberes, temporäres Testverzeichnis unter `tests/.test_config/` bereit. 
2. Kopiert die werkseitigen Grundeinstellungen von `src/atbcmder/resources/test_config.xml` nach `tests/.test_config/atbcmder.xml`. 
3. Setzt `export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"`. 
4. Erzeugt ATBCmder in Python. Alle während der Sitzung geänderten oder gelöschten Einstellungen wirken sich nur auf das temporäre Testverzeichnis aus, sodass Ihre persönlichen `~/Library/Einstellungen/atbcmder/`-Dateien zu 100 % unberührt bleiben. 

---

## 9. ⚡ Profi-Tipps und ausführliche Informationen: Erweiterte Anpassung

### Profi-Tipp 1: Automatisierte Dotfile-Bereitstellung über Chezmoi / Ansible

Da ATBCmder den gesamten Status in Standard-UTF-8-XML-Dateien serialisiert, können Sie Ihre Konfiguration in ein Git-Dotfiles-Repository einchecken und über Tools wie Chezmoi, GNU Stow oder Ansible verwalten: 

```bash
# Example: Adding ATBCmder configuration to Chezmoi dotfiles manager
chezmoi add ~/Library/Preferences/atbcmder/atbcmder.xml
chezmoi add ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml
```

### Profi-Tipp 2: Leistungsstarkes Network Watcher-Tuning

Bei der Arbeit auf unternehmensweiten SMB/NFS-Dateiservern mit Millionen von Dateien kann die aktive rekursive Ereignisüberwachung zu einer Netzwerküberlastung führen. 

1. Öffnen Sie **Einstellungen ➔ Automatische Aktualisierung**. 
2. Deaktivieren Sie **Wenn sich Größe, Datum oder Attribute ändern**. 
3. Stellen Sie das **Abfrageintervall** auf `15` oder `30` Sekunden ein. 
4. Fügen Sie das Netzwerk-Mount-Root (`/Volumes/EnterpriseShare`) zur **Pfad-Ausschlussliste** hinzu. 
5. Verwenden Sie die manuelle Panel-Aktualisierung (**`Ctrl+R`** / `⌘R`), wenn eine sofortige Synchronisierung erforderlich ist.

### Profi-Tipp 3: Externe Befehlsumgebungsvariablen

Beim Konfigurieren benutzerdefinierter externer Symbolleistenschaltflächen oder Dateizuordnungen erbt ATBCmder automatisch Ihre Benutzer-Shell-Umgebung (`PATH`, `HOME`, `USER`). Sie können über Homebrew (`/opt/homebrew/bin/`) installierte Befehlszeilen-Dienstprogramme direkt aufrufen, ohne vollständige absolute Pfade für ausführbare Dateien anzugeben.

### Profi-Tipp 4: Konfiguration der schwebenden Datei-Tooltips

ATBCmder enthält umfangreiche Tooltips für schwebende Metadaten, die Dateiabmessungen, EXIF-Daten, Audio-Bitrate und die Anzahl der Archivmitglieder anzeigen, wenn Sie mit der Maus über Elemente fahren. Sie können Tooltips unter **Einstellungen ➔ Dateiansichten** ein- oder ausschalten. 

![Helpful Tooltips](images/helpful_tooltips.png) 
*Abbildung 7.5: Umfangreiche Metadaten-Tooltips, die detaillierte Dateieigenschaften anzeigen, wenn Sie mit der Maus darüber fahren.* 

---

## 10. Sicherheits- und Systemwarnungen

> [!CAUTION] 
> **Verifizierung des Überschreibens der Verknüpfung** 
> Durch das Überschreiben einer primären Verknüpfung im Kontext `Main` oder `FilePanel` wird die Bindung sofort vom ursprünglichen Befehl gelöst. Wenn Sie versehentlich wichtige Befehle wie `F5` (Kopieren) oder `Enter` (Öffnen) entbinden, verwenden Sie die Schaltfläche **Auf Standardwerte zurücksetzen** im Hotkey-Editor, um die werkseitigen Tastenbelegungen wiederherzustellen. 

> [!WARNING] 
> **Konfigurationsimport ersetzt alle Einstellungen** 
> Durch das Wiederherstellen eines Konfigurationspakets über `cm_ImportConfiguration` werden Ihre aktuellen Dateien `atbcmder.xml`, `favtabs.xml` und `hotlist.xml` vollständig überschrieben. Exportieren Sie immer eine Sicherung Ihrer vorhandenen Konfiguration, bevor Sie ein externes Archiv importieren. 

> [!IMPORTANT] 
> **macOS App Sandbox und vollständiger Festplattenzugriff** 
> Wenn ATBCmder unter der macOS App Sandbox ausgeführt wird, kann er ohne ausdrückliche Benutzererlaubnis keine Konfigurationsdateien oder Verzeichnisse außerhalb seines Containers lesen. Wenn beim Zugriff auf externe Laufwerke Berechtigungsfehler auftreten, führen Sie **`cm_GrantFilesystemAccess`** aus, um den Onboarding-Ablauf für macOS Full Disk Access abzuschließen. 

---

## 11. Master-Dual-Matrix-Anpassungs- und Voreinstellungen-Befehlsreferenz

| Kategorie | Aktionsbeschreibung | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | 
| :--- | :--- | :--- | :--- | :--- | 
| **Einstellungen** | Öffnen Sie den Haupteinstellungsdialog | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | 
| **Einstellungen** | Einstellungen jetzt in XML speichern | Menü: Konfiguration | — | `cm_ConfigSaveSettings` | 
| **Einstellungen** | Fensterposition und -größe speichern | Menü: Konfiguration | — | `cm_ConfigSavePos` | 
| **Einstellungen** | Datei-Tooltips umschalten | Einstellungen ➔ Dateiansichten | — | *(Einstellungen)* | 
| **Einstellungen** | Vollständige Festplattenberechtigungen erteilen | Menü: Konfiguration | — | `cm_GrantFilesystemAccess` | 
| **Hotkeys** | Öffnen Sie die Hotkey-Editor-Seite | `Cmd+,` ➔ Hotkeys | — | `cm_Options` | 
| **Hotkeys** | Globaler Hotkey zum Ein-/Ausblenden von Fenstern | `Ctrl+Alt+H` / `⌘⌥H` | `Ctrl+Alt+H` | *(Globaler System-Hotkey)* | 
| **Verbände** | Öffnen Sie den Dateizuordnungs-Manager | Menü: Konfiguration | — | `cm_FileAssoc` | 
| **Lesezeichen** | Verzeichnis-Hotlist-Manager | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| **Lesezeichen** | Aktuelles Verzeichnis zur Hotlist hinzufügen | Menü: Lesezeichen | — | `cm_AddDirToHotlist` | 
| **Ordnerregisterkarten** | Favoritenordner-Registerkarten-Manager | Menü: Konfiguration | — | `cm_ConfigFavoriteTabs` | 
| **Ordnerregisterkarten** | Aktuelle Tabs als Favoritensatz speichern| Menü: Registerkarten | — | `cm_SaveFavoriteTabs` | 
| **Archiver** | Archiver-Binärdateien konfigurieren | Menü: Konfiguration | — | `cm_ConfigArchivers` | 
| **Portabilität** | Konfiguration in ZIP exportieren | Menü: Konfiguration | — | `cm_ExportConfiguration` | 
| **Portabilität** | Konfiguration aus ZIP importieren | Menü: Konfiguration | — | `cm_ImportConfiguration` | 
| **Portabilität** | Öffnen Sie den Konfigurationsordner | Menü: Konfiguration | — | `cm_OpenConfigDirectory` | 
| **Ansichtsmodi** | Miniaturansicht-Rasteransicht umschalten | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| **Ansichtsmodi** | Liste der aktiven Panels aktualisieren | `Ctrl+R` / `⌃R` | `Ctrl+R` | `cm_Refresh` |

--- 

<div align="center"> 
<p>Bereit, alle Tastaturkürzel und Befehlsmatrizen in der gesamten Anwendung zu beherrschen?</p> 
<p><strong><a href="keyboard_shortcuts.md">Fahren Sie mit Kapitel 8 fort: Master-Tastaturkürzel &rarr;</a></strong></p> 
</div>