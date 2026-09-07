# Kapitel 8: Tastaturkurzbefehle-Referenz

ATBCmder ist von Grund auf als Dateimanager für die Tastatur konzipiert. Alle Dateivorgänge, Verzeichnissprünge, Ansichtsumwandlungen und Batch-Dienstprogramme können ohne Mausinteraktion ausgeführt werden. 

Um orthodoxe Commander-Traditionen mit nativer Apple-Ergonomie zu verbinden, verwendet ATBCmder eine **Dual-Matrix-Tastaturarchitektur**: Jeder Befehl kann entweder mit den klassischen Commander-Funktionstasten (`F1`–`F12`, `Insert`, Ziffernblock) oder nativen macOS-Modifikatorakkorden aufgerufen werden (`⌘` Befehl, `⌥` Option, `⇧` Umschalt, `⌃` Steuerung). 

---

## 1. Die Dual-Matrix-Philosophie und Schlüsselnotation

Unabhängig davon, ob Sie über zwanzig Jahre Muskelgedächtnis von Total Commander und Norton Commander verfügen oder vollständig mit den nativen macOS Finder-Verknüpfungen leben, passt ATBCmder Ihre Reflexe sofort an, ohne dass eine manuelle Neuzuordnung erforderlich ist. 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DUAL-MATRIX KEYBOARD ENGINE                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  CLASSIC COMMANDER PARADIGM          │  NATIVE macOS PARADIGM               │
│  • Function Key Centric (F1–F12)     │  • Modifier Chords (⌘, ⌥, ⇧, ⌃)      │
│  • Dedicated Keypad Marking (+, -, *)│  • Finder Parity (⌘C, ⌘V, ⌘⌫, ⏎)     │
│  • Zero-Modal Terminal Velocity      │  • Native Menu Bar Integration       │
│  Examples:                           │  Examples:                           │
│    F5        ➔ Copy Files            │    ⌘C ➔ ⌘V   ➔ Copy Files            │
│    F6        ➔ Move Files            │    ⌘C ➔ ⌥⌘V  ➔ Move Files            │
│    Shift+F4  ➔ Create Text File      │    ⇧⌘4       ➔ Create Text File      │
│    Alt+F7    ➔ Find Files            │    ⌥⌘F       ➔ Find Files            │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Modifikatorsymbole für die Apple-Tastatur

In diesem Handbuch und in den Einstellungsdialogen von ATBCmder werden Tastenkombinationen durch typografische Standardglyphen von macOS dargestellt: 

| Glyphe | Modifikatorname | Windows/PC-Äquivalent | Beschreibung | 
| :---: | :--- | :--- | :--- | 
| **`⌘`** | **Befehl** (`Cmd`) | `Win` / `Ctrl` | Primäre macOS-Aktionsmodifikatortaste. | 
| **`⌥`** | **Option** (`Alt`) | `Alt` | Sekundärer Modifikator für alternative Aktionen und Sonderzeichen. | 
| **`⇧`** | **Umschalt** | `Shift` | Erweitert die Auswahl, kehrt Aktionen um oder aktiviert den Großbuchstabenmodus. | 
| **`⌃`** | **Steuerung** (`Ctrl`) | `Ctrl` | Terminalsteuerung und klassischer Commander-Akkordmodifikator. | 
| **`⎋`** | **Escape** (`Esc`) | `Esc` | Bricht Vorgänge ab, löscht Filter oder schließt Dialoge. | 
| **`⏎`** | **Zurück** (`Enter`) | `Enter` | Führt Aktionen aus, öffnet Elemente oder übermittelt Dialogaufforderungen. | 
| **`⌫`** | **Löschen / Rücktaste** | `Backspace` | Löschen von Zeichen rückwärts oder Navigation im übergeordneten Verzeichnis. | 
| **`⌦`** | **Löschen weiterleiten** | `Del` | Weiterleiten, Zeichen löschen oder ausgewählte Datei löschen. | 
| **`⇥`** | **Tabulatortaste** | `Tab` | Wechselt den Fokus zwischen Quell- und Zielfenstern. | 
| **`⇞`** | **Seite nach oben** | `PgUp` | Scrollt die Panel-Liste um ein Fenster-Ansichtsfenster nach oben. | 
| **`⇟`** | **Seite nach unten** | `PgDn` | Scrollt die Bedienfeldliste um ein Fenster-Ansichtsfenster nach unten. | 

---

## 2. macOS-Funktion (`Fn`) Schlüsselanleitung

> [!IMPORTANT] 
> ### So verwenden Sie Funktionstasten auf Mac-Tastaturen 
> 
> Standardmäßig weisen Apple-Tastaturen (einschließlich integrierter MacBook-Tastaturen, Magic Keyboards und Touch Bar-Macs) die oberste physische Reihe (`F1` bis `F12`) Hardwaresteuerungen wie Displayhelligkeit, Mission Control, Spotlight, Diktieren, Medienwiedergabe und Lautsprecherlautstärke zu. 
> 
> Da klassische Commander-Workflows stark von `F1`–`F12` abhängen, haben Sie zwei Möglichkeiten: 
> 
> #### Methode A: Halten Sie den Tastenakkord `Fn` (Standardeinstellung) 
> Halten Sie die physische **`Fn`**-Taste (oder Globus-Taste 🌐) in der unteren linken Ecke Ihrer Mac-Tastatur gedrückt, während Sie eine beliebige Funktionstaste drücken: 
> 
> * **`Fn + F3`**: Datei im Lister anzeigen 
> * **`Fn + F4`**: Datei bearbeiten 
> * **`Fn + F5`**: Dateien in das Zielpanel kopieren 
> * **`Fn + F6`**: Dateien in das Zielfenster verschieben 
> * **`Fn + F7`**: Neues Verzeichnis erstellen 
> * **`Fn + F8`**: Dateien löschen 
> * **`Fn + Shift + F4`**: Neue Textdatei erstellen und bearbeiten 
> * **`Fn + Alt + F7`**: Dateisuche öffnen 
> 
> #### Methode B: „Standardfunktionstasten“ in den macOS-Einstellungen aktivieren (empfohlen) 
> Wenn Sie ATBCmder regelmäßig verwenden, wechseln Sie Ihre Funktionszeile so, dass durch Drücken von `F1`–`F12` Funktionsbefehle direkt ausgelöst werden, während das Halten von `Fn` Helligkeits- und Lautstärkeanpassungen auslöst: 
> 
> 1. **macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia**: 
> - Öffnen Sie ** Apple-Menü ➔ Systemeinstellungen...** 
> - Wählen Sie in der linken Seitenleiste **Tastatur** aus. 
> - Klicken Sie auf die Schaltfläche **Tastaturkürzel...**. 
> - Wählen Sie in der Seitenleiste des Dialogs **Funktionstasten** aus. 
> - Schalten Sie **"F1-, F2-usw.-Tasten als Standardfunktionstasten verwenden"** auf **EIN** um. 
> - Klicken Sie auf **Fertig**. 
> 
> 2. **macOS 12 Monterey & macOS 11 Big Sur**: 
> - Öffnen Sie ** Apple-Menü ➔ Systemeinstellungen... ➔ Tastatur**. 
> - Aktivieren Sie auf der Registerkarte **Tastatur** das Kontrollkästchen mit der Bezeichnung **"F1-, F2-usw.-Tasten als Standardfunktionstasten verwenden"**. 
> 
> #### MacBook Pro-Modelle mit Touch Bar 
> 
> * Halten Sie die physische **`Fn`**-Taste unten links gedrückt, um sofort die virtuelle Zeile `F1`–`F12` auf der Touch Bar anzuzeigen. 
> * Alternativ können Sie **Systemeinstellungen ➔ Tastatur ➔ Touch Bar-Einstellungen...** konfigurieren und **"Touch Bar zeigt"** auf **"F1, F2 usw. Tasten"** setzen, wenn ATBCmder die aktive, vorderste Anwendung ist. 
> 
> #### Kompakte Tastaturen ohne eigene Funktionszeile 
> 
> * Wenn Sie eine zu 60 % oder 65 % mechanische Tastatur ohne dedizierte `F`-Tasten verwenden, müssen Sie Ihre Finger nicht verdrehen. Verwenden Sie die nativen macOS-Modifikatorakkorde von ATBCmder (`⌘C`, `⌥⌘V`, `⇧⌘N`, `⌘⌫`, `⌥⏎`), die 100 % Betriebsparität bieten.

---

## 3. Kontextbezogene Shortcut-Architektur

Um Hotkey-Kollisionen zwischen verschiedenen Anwendungsbereichen zu verhindern (z. B. Suche in der Hauptdateiliste im Vergleich zur Suche in einem Textdatei-Viewer), segmentiert ATBCmder alle Tastenkombinationen in verschiedene hierarchische Kontexte: 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION SCOPE: Main                            │
│  Global commands, panel navigation, window management, toolbar, power tools │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PANEL SCOPE: FilePanel       │  MODAL TOOLS SCOPES                         │
│  Active during directory      │  • Viewer      (Lister preview window)      │
│  table and thumbnail browsing │  • Editor      (Built-in code editor)       │
│  (marking, range selection,   │  • Differ      (Side-by-side diff viewer)   │
│  inline editing, space count) │  • FindFiles   (Multi-threaded file search) │
│                               │  • MultiRename (Batch rename engine)        │
└───────────────────────────────┴─────────────────────────────────────────────┘
```
 

Wenn Sie einen Tastenakkord drücken, führt die **`HotkeyManager`**-Engine Folgendes aus: 

1. Bewertet den aktiven fokussierten Kontext (z. B. `Viewer` oder `FilePanel`). 
2. Wenn eine genaue Bindung übereinstimmt, wird der zugehörige Befehl `cm_*` sofort ausgeführt. 
3. Wenn im lokalen Kontext keine Bindung vorhanden ist, wird der Tastendruck ordnungsgemäß auf den Kontext `Main` zurückgesetzt. 
4. Wenn die Bindung noch ungebunden ist, übernimmt die Standardtextbearbeitung oder die Handhabung von Systemtastenanschlägen. 

---

## 4. Meistern Sie kategorisierte Dual-Matrix-Tabellen

Die folgenden Referenztabellen dokumentieren alle von ATBCmder unterstützten Befehle, kategorisiert nach funktionalem Workflow.

### 4.1 Dateioperationen

Dateioperationen bilden das Rückgrat der täglichen Arbeit. Bei jedem Vorgang gilt standardmäßig das Paradigma **Quelle ➔ Ziel**: Im aktiven Bereich ausgewählte Elemente werden in das Verzeichnis verarbeitet, das im inaktiven gegenüberliegenden Bereich geöffnet ist.

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_View` | Datei mit Universal Lister anzeigen (schreibgeschützte Vorschau) | `⌘3` / `Space` *(Schnellansicht)* | `F3` / `Shift+F3` | Haupt | 
| `cm_Edit` | Datei im integrierten Texteditor öffnen | `⌘4` | `F4` | Haupt | 
| `cm_EditNew` | Erstellen und bearbeiten Sie sofort eine neue Textdatei | `⇧⌘4` / `⇧F4` | `Shift+F4` | Haupt | 
| `cm_Copy` | Ausgewählte Dateien vom aktiven zum Zielpanel kopieren | `⌘C` *(in die Zwischenablage)* / `F5` | `F5` | Haupt | 
| `cm_CopySamePanel` | Ausgewählte Datei im selben Verzeichnis duplizieren/klonen | `⇧F5` | `Shift+F5` | Haupt | 
| `cm_Move` | Ausgewählte Dateien vom aktiven in das Zielfenster verschieben | `⌥⌘V` *(Verschiebung einfügen)* / `F6` | `F6` | Haupt | 
| `cm_RenameOnly` | Schnelle Inline-Umbenennung der Datei unter dem Cursor | `⏎` *(Rückgabe)* / `F2` | `F2` / `Shift+F6` | Haupt | 
| `cm_Rename` | Ausgewählte Datei über Dialog | umbenennen `⇧F6` | `Shift+F6` | Haupt | 
| `cm_MkDir` | Erstellen Sie ein neues Verzeichnis/Ordner | `⇧⌘N` / `F7` | `F7` | Haupt | 
| `cm_Delete` | Ausgewählte Elemente in den macOS-Papierkorb löschen | `⌘⌫` *(Befehl+Löschen)* / `⌦` | `F8` / `Delete` | Haupt | 
| `cm_Wipe` | Dateien sicher löschen (Papierkorb dauerhaft umgehen) | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | FilePanel | 
| `cm_Open` | Öffnen Sie die Datei mit der Standard-App oder geben Sie das Verzeichnis | ein `⌘↓` / `⏎` *(Rückgabe)* | `Enter` | Haupt | 
| `cm_SetFileProperties` | Dateimetadaten, Daten und UNIX-Berechtigungen prüfen und bearbeiten | `⌥⏎` *(Option+Return)* / `⌘I` | `Alt+Enter` | Haupt | 
| `cm_CountDirContent` | Berechnen Sie die Bytegröße des Verzeichnisses unter dem Cursor | `⌥⇧⏎` *(Wahl+Umschalt+Eingabetaste)* | `Alt+Shift+Enter` | FilePanel | 
| `cm_CalculateSpace` | Gesamtgröße aller ausgewählten Verzeichnisse berechnen | `⌃L` / `⌘L` | `Ctrl+L` | Haupt | 
| `cm_SymLink` | Symbolischen Link im Zielpanel erstellen | `⌥⌘S` | *(Menü: Dateien ➔ Symlink)* | Haupt | 
| `cm_HardLink` | Dateisystem-Hardlink im Zielfenster erstellen | `⌥⌘H` | *(Menü: Dateien ➔ Hardlink)* | Haupt | 
| `cm_PackFiles` | Ausgewählte Dateien in Archiv packen/komprimieren (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Haupt | 
| `cm_ExtractFiles` | Archivinhalte direkt in das Zielpanel extrahieren | `⌥F9` / `⌥⌘E` | `Alt+F9` | Haupt | 
| `cm_ArchiveView` | Geben Sie das Archiv als virtuelles Dateisystemverzeichnis ein (`vfs://`) | `⌃⇟` *(Strg+BildAb)* / `⌘↓` | `Ctrl+PgDn` | Haupt | 
| `cm_CompareContents` | Inhalte zweier ausgewählter Dateien vergleichen | `⇧F3` | `Shift+F3` | Haupt |

---

### 4.2 Auswahl und Kennzeichnung

Orthodoxe Dateimanager zeichnen sich durch die schnelle Auswahl mehrerer Dateien aus. ATBCmder ermöglicht die Auswahl einzelner Elemente, Platzhaltermuster, Erweiterungsgruppen oder fortlaufender Blöcke ohne Verwendung einer Maus.

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_MarkMarkAll` | Wählen Sie alle Dateien und Ordner im aktiven Bereich | aus `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Haupt | 
| `cm_MarkUnmarkAll` | Alle Dateien und Ordner im aktiven Bereich abwählen | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Haupt | 
| `cm_MarkInvert` | Aktuellen Auswahlstatus im aktiven Bereich umkehren | `⌘I` / `⌃I` | `Num*` *(Tastatur `*`)* | FilePanel | 
| `cm_MarkPlus` | Wählen Sie ein passendes Platzhaltermuster für die Gruppe aus (z. B. `*.ts`) | `⌘+` / `⌃+` | `Num+` *(Tastatur `+`)* | FilePanel | 
| `cm_MarkMinus` | Gruppenübereinstimmungs-Platzhaltermuster abwählen (z. B. `*.log`) | `⌘-` / `⌃-` | `Num-` *(Tastatur `-`)* | FilePanel | 
| `cm_MarkCurrentExtension` | Wählen Sie alle Dateien mit der Dateierweiterung | des Cursors aus `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Haupt | 
| `cm_UnmarkCurrentExt` | Deaktivieren Sie alle Dateien mit der Dateierweiterung | des Cursors `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Haupt | 
| `cm_MarkCurrentName` | Alle Dateien auswählen, die den Basisdateinamen des Cursors teilen | `⌥⌘N` | *(Menü: Markieren ➔ Gleicher Name)* | Haupt | 
| `cm_SelectOrDeselectFile` | Elementauswahl umschalten und Cursor nach unten bewegen | `Space` | `Insert` / `Space` | FilePanel | 
| `Shift+Up / Shift+Down` | Kontinuierliches Auswahlspektrum erweitern oder verkleinern | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | FilePanel | 
| `Shift+PageUp / Shift+PageDown` | Kontinuierliche Auswahl um vollständige Ansichtsfensterseite erweitern | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | FilePanel | 
| `cm_ClearAll` | Alle Auswahlmarkierungen und Suchhervorhebungen löschen | `⌃L` | `Ctrl+L` | Haupt | 
| `cm_CopyToClipboard` | Ausgewählte Dateien in die Zwischenablage des macOS-Systems kopieren | `⌘C` | `Ctrl+C` | Haupt | 
| `cm_CutToClipboard` | Ausgewählte Dateien in die macOS-Systemzwischenablage ausschneiden | `⌘X` | `Ctrl+X` | Haupt | 
| `cm_PasteFromClipboard` | Dateien aus der Zwischenablage in das aktive Verzeichnis einfügen | `⌘V` | `Ctrl+V` | Haupt | 
| `cm_PasteAsMove` | Dateien aus der Zwischenablage als Verschiebevorgang einfügen | `⌥⌘V` | `Ctrl+Alt+V` | Haupt | 
| `cm_CopyNamesToClip` | Dateinamen nur in die Zwischenablage kopieren | `⇧⌘X` | `Ctrl+Shift+X` | Haupt | 
| `cm_CopyFullNamesToClip` | Vollständige(n) absolute(n) Pfad(e) in die Zwischenablage kopieren | `⇧⌘C` | `Ctrl+Shift+C` | Haupt | 
| `cm_CompareDirectories` | Markieren Sie Dateien, die in einem Bereich vorhanden sind, im anderen jedoch nicht | `⌥⇧C` | *(Menü: Markieren ➔ Verzeichnisse vergleichen)* | Haupt |

---

### 4.3 Panel-Navigation und Lesezeichen

Bewegen Sie sich mühelos zwischen Ordnern, lokalen Volumes, Netzwerkbereitstellungen und dem Browserverlauf.

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FocusSwap` / `cm_SwitchPanel` | Wechselnder Tastaturfokus zwischen linkem und rechtem Bedienfeld | `⇥` *(Tab)* | `Tab` | Haupt | 
| `cm_Refresh` | Active Directory-Inhalte aktualisieren/erneut lesen | `⌘R` / `⌃R` | `Ctrl+R` | Haupt | 
| `cm_ChangeDirToParent` | Navigieren Sie zum übergeordneten Verzeichnis (`..`) | `⌘↑` / `⌫` *(Rücktaste)* | `Backspace` / `Ctrl+PgUp` | Haupt | 
| `cm_ChangeDirToRoot` | Direkt zum Dateisystem-Root (`/`) | springen `⌘\` | `Ctrl+\` | Haupt | 
| `cm_ChangeDirToHome` | Direkt zum Home-Ordner des Benutzers springen (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | FilePanel | 
| `cm_ViewHistoryPrev` | Navigieren Sie zurück in den Browserverlauf des Verzeichnisses | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Haupt | 
| `cm_ViewHistoryNext` | Navigieren Sie vorwärts im Verzeichnis Browserverlauf | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Haupt | 
| `cm_DirHistory` | Öffnen Sie das Dropdown-Menü „Interaktiver Verzeichnisverlauf“ | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Haupt | 
| `cm_Drives` | Öffnen Sie das Popup-Fenster zur Auswahl des Laufwerks und des gemounteten Volumes | `⌥D` | `Alt+D` | Haupt | 
| `cm_LeftOpenDrives` | Öffnen Sie das Laufwerksauswahlmenü für den linken Bereich | `⌥F1` | `Alt+F1` | Haupt | 
| `cm_RightOpenDrives` | Öffnen Sie das Laufwerksauswahlmenü für den rechten Bereich | `⌥F2` | `Alt+F2` | Haupt | 
| `cm_Exchange` | Vertauschen Sie den linken und rechten Bereich (Verzeichnisse, Registerkarten, Status) | `⌘U` | `Ctrl+U` | Haupt | 
| `cm_TargetEqualSource` | Stellen Sie das inaktive Panel-Verzeichnis so ein, dass es mit dem aktiven Verzeichnis übereinstimmt | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Haupt | 
| `cm_SyncSlaveDir` | Zielpanel-Navigation sperren, um Quellpanel zu spiegeln | `⌥S` | *(Menü: Befehle ➔ Navigation synchronisieren)* | Haupt | 
| `cm_DirHotList` | Öffnen Sie das Verzeichnis-Hotlist-/Lesezeichen-Menü | `⌘D` | `Ctrl+D` | Haupt | 
| `cm_ConfigDirHotList` | Konfigurationsdialog für die Open Directory-Hotlist | `⇧⌘D` | `Ctrl+Shift+D` | Haupt | 
| `cm_GoToFirst` | Cursor zum ersten Element im aktiven Bereich springen | `⌘↑` / `Fn+←` *(Home)* | `Home` | Haupt | 
| `cm_GoToLast` | Cursor zum letzten Element im aktiven Bereich springen | `⌘↓` / `Fn+→` *(Ende)* | `End` | Haupt | 
| `PageUp / PageDown` | Aktives Panel um ein ganzes Ansichtsfenster nach oben oder unten scrollen | `⇞` *(Fn+↓)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | FilePanel |

---

### 4.4 Ansichtsmodi und Sortierung

Wechseln Sie nahtlos zwischen kompakten Listen, detaillierten Metadatenspalten, visuellen Miniaturansichtsrastern, rekursiver Verzeichnisreduzierung und synchronisierten Baumansichten.

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_BriefView` | Zur Kurzansicht wechseln (mehrspaltige kompakte Namen) | `⌃F1` | `Ctrl+F1` | Haupt | 
| `cm_ColumnsView` | Wechseln Sie zur Spalten-/Detailansicht (Name, Größe, Datum, Dauer) | `⌃F2` | `Ctrl+F2` | Haupt | 
| `cm_ThumbnailsView` | Wechseln Sie zur Rasteransicht der Miniaturansichten (Bilder, Medien, PDFs) | `⌃⇧F1` | `Ctrl+Shift+F1` | Haupt | 
| `cm_FlatView` | Flache/Zweigansicht umschalten (rekursive Verzeichnisliste) | `⌘B` | `Ctrl+B` | Haupt | 
| `cm_FlatViewSel` | Flache/Zweigansicht nur ausgewählter Verzeichnisse | `⇧⌘B` | `Ctrl+Shift+B` | Haupt | 
| `cm_TreeView` | Baumansicht (Aktives Panel durch Verzeichnisbaum ersetzen) | `⌃⇧F8` | `Ctrl+Shift+F8` | Haupt | 
| `cm_TreeViewSplit` | Baumansicht (geteiltes Bedienfeld: Baum oben/links, Dateien unten/rechts) | `cm_TreeViewSplit` | *(Menü: Anzeigen ➔ Baumansicht teilen)* | Haupt | 
| `cm_TreeViewBoth` | Baumansicht (Beide Panels zeigen Verzeichnisbäume) | `cm_TreeViewBoth` | *(Menü: Anzeigen ➔ Baumansicht Beide)* | Haupt | 
| `cm_QuickView` | Schnellansicht-Panel umschalten (Live-Vorschau im gegenüberliegenden Panel) | `⌘Q` / `⌃Q` | `Ctrl+Q` | Haupt | 
| `cm_SortByName` | Elemente nach Namen sortieren (aufsteigend/absteigend umschalten) | `⌃F3` | `Ctrl+F3` | Haupt | 
| `cm_SortByExt` | Elemente nach Erweiterung sortieren | `⌃F4` | `Ctrl+F4` | Haupt | 
| `cm_SortByDate` | Elemente nach Änderungsdatum/-uhrzeit sortieren | `⌃F5` | `Ctrl+F5` | Haupt | 
| `cm_SortBySize` | Elemente nach Dateigröße sortieren | `⌃F6` | `Ctrl+F6` | Haupt | 
| `cm_SortByAttr` | Elemente nach UNIX-Attributen/Berechtigungen sortieren | `cm_SortByAttr` | *(Menü: Sortieren ➔ Attribute)* | Haupt | 
| `cm_ShowHiddenFiles` | Sichtbarkeit versteckter Dateien umschalten (`.` dotfiles) | `⌘H` / `⇧⌘.` | `Ctrl+H` | Haupt | 
| `cm_ShowSysFiles` | Sichtbarkeit des macOS-Systems und geschützter Dateien umschalten | `⇧⌘.` | `Ctrl+.` | Haupt | 
| `cm_QuickSearch` | Öffnen Sie die Schnellsuchleiste im Bedienfeld (geben Sie die zu filternden Buchstaben ein) | `⌥S` / `⌃S` *(oder Eingabe)* | `Ctrl+S` / *(Buchstabeneingabe)* | Haupt | 
| `cm_SemanticFilter` | Öffnen Sie die semantische Smart-Filterleiste für natürliche Sprache | `⌘F` | `Ctrl+F` | Haupt | 
| `cm_HorizontalFilePanels` | Horizontales Dual-Panel-Layout umschalten (vertikal gestapelt) | `⇧⌘H` | `Ctrl+Shift+H` | Haupt |

---

### 4.5 Registerkarten und Fensterverwaltung

ATBCmder ermöglicht das Öffnen unbegrenzter Tabs in beiden Panels, das Sperren bevorzugter Arbeitsorte und die Verwaltung von Dual-Panel-Multi-Tab-Sitzungen.

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_NewTab` | Öffnen Sie die Registerkarte „Neuer Ordner“ im aktiven Bereich | `⌘T` | `Ctrl+T` | Haupt | 
| `cm_CloseTab` | Schließen Sie die Registerkarte „Aktuell aktiver Ordner“ | `⌘W` | `Ctrl+W` | Haupt | 
| `cm_NextTab` / `cm_NextTabCtrl` | Zur nächsten Registerkarte rechts wechseln | `⌃⇥` *(Strg+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Haupt | 
| `cm_PrevTab` / `cm_PrevTabCtrl` | Zur vorherigen Registerkarte auf der linken Seite wechseln | `⌃⇧⇥` *(Strg+Umschalt+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Haupt | 
| `cm_ShowTabsList` | Popup-Menü aller geöffneten Tabs im aktiven Panel anzeigen | `⇧⌘L` | `Ctrl+Shift+L` | Haupt | 
| `cm_CloseAllTabs` | Alle Registerkarten im aktiven Bereich schließen, außer der letzten | `⌥⌘W` | *(Tab-Kontextmenü: Alle schließen)* | Haupt | 
| `cm_CloseOtherTabs` | Schließen Sie alle Registerkarten außer der aktuell aktiven Registerkarte | `⇧⌘W` | *(Tab-Kontextmenü: Andere schließen)* | Haupt | 
| `cm_Duplicatetab` | Registerkarte „Aktiven Ordner duplizieren“ | `⌘D` / `cm_Duplicatetab` | *(Tab-Kontextmenü: Duplizieren)* | Haupt | 
| `cm_MoveTabLeft` | Aktive Registerkarte um eine Position nach links verschieben | `⌃⇧←` | *(Tab-Kontextmenü: Nach links verschieben)* | Haupt | 
| `cm_MoveTabRight` | Aktive Registerkarte um eine Position nach rechts verschieben | `⌃⇧→` | *(Tab-Kontextmenü: Nach rechts verschieben)* | Haupt | 
| `cm_CopyTabToOtherPanel` | Aktive Registerkarte direkt in gegenüberliegendes Bedienfeld klonen | `⌥⌘T` | *(Tab-Kontextmenü: In andere kopieren)* | Haupt | 
| `cm_SaveTab` / `cm_SaveTabs` | Aktuelles Tab-Layout in der Konfiguration speichern | `cm_SaveTab` | *(Menü: Tabs ➔ Tabs speichern)* | Haupt | 
| `cm_LoadTab` / `cm_LoadTabs` | Gespeichertes Tab-Layout aus Konfiguration wiederherstellen | `cm_LoadTab` | *(Menü: Tabs ➔ Tabs laden)* | Haupt | 
| `cm_OptionsFavorites` | Konfigurieren Sie Favoriten-Tab-Sets und persistente Arbeitsbereiche | `cm_OptionsFavorites` | *(Menü: Tabs ➔ Favoriten-Tabs)* | Haupt | 
| `cm_FullScreen` | Vollbild-Anwendungsfenster umschalten | `⌃⌘F` / `F11` | `F11` | Haupt |

---

### 4.6 Elektrowerkzeuge und Dienstprogramme

Starten Sie erweiterte Automatisierungstools, Batch-Dienstprogramme und eingebettete Systemtools direkt über Tastaturakkorde.

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FileSearch` / `cm_Search` | Öffnen Sie das Dialogfeld „Erweiterte Multifilter-Suche“ | `⌥F7` / `⌥⌘F` | `Alt+F7` | Haupt | 
| `cm_FileDiff` / `cm_CompareFiles` | Öffnen Sie den Side-by-Side Visual File Difference Viewer | `⌘⇧F12` | `Meta+Shift+F12` | Haupt | 
| `cm_SyncDirs` | Öffnen Sie das Tool zur bidirektionalen Verzeichnissynchronisierung | `⇧F12` | `Shift+F12` | Haupt | 
| `cm_MultiRename` | Öffnen Sie das Batch-Multi-Rename-Tool (RegEx und Token) | `⌘M` | `Ctrl+M` | Haupt | 
| `cm_Split` | Große Datei in einheitliche Blocksegmente aufteilen | `⌥F6` | `Alt+F6` | Haupt | 
| `cm_Combine` | Geteilte nummerierte Segmente wieder zur Originaldatei zusammenfügen | `⌥F7` | `Alt+F7` | Haupt | 
| `cm_CalculateChecksum` | Berechnen Sie den kryptografischen Hash (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Haupt | 
| `cm_VerifyChecksum` | Dateien anhand der Prüfsummendatei überprüfen (`.md5`, `.sha256`) | `cm_VerifyChecksum` | *(Menü: Dateien ➔ Prüfsumme überprüfen)* | Haupt | 
| `cm_RunTerm` | Starten Sie das Systemterminal im aktiven Panel-Verzeichnis | `⌃J` / `F9` | `Ctrl+J` / `F9` | Haupt | 
| `cm_FocusCmdLine` | Verschieben Sie den Tastaturfokus direkt zur unteren Befehlszeile | `⇧F2` | `Shift+F2` | Haupt | 
| `cm_ShowCmdLineHistory` | Dropdown-Liste „Verlauf“ früherer Shell-Befehle öffnen | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Haupt | 
| `cm_AddPathToCmdLine` | Active Directory-Pfad an Befehlszeile anhängen | `⌘P` | `Ctrl+P` | Haupt | 
| `cm_ShowCommandLine` | Untere Befehlszeile/Konsoleneingabeleiste umschalten | `⌘O` | `Ctrl+O` | Haupt | 
| `cm_DiskBenchmark` | Führen Sie den Benchmark für die Lese-/Schreibleistung des Speicherlaufwerks aus | `cm_DiskBenchmark` | *(Menü: Befehle ➔ Benchmark)* | Haupt | 
| `cm_VisSemanticCommand` | Öffnen Sie die Befehlsleiste für semantische Suche und natürliche Sprache | `/` / `⇧⌘P` | `/` | Haupt |

---

### 4.7 System, Konfiguration und Hilfe

Greifen Sie auf Anwendungseinstellungen, Konfigurationsverwaltung, Software-Updates und Benutzerdokumentation zu. 

| Befehls-ID | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_Options` | Öffnen Sie das Dialogfeld „Anwendungseinstellungen/Einstellungen“ | `⌘,` | `Ctrl+,` | Haupt | 
| `cm_HelpContents` / `cm_HelpIndex` | Öffnen Sie die interaktive Benutzerdokumentation und den Leitfaden | `⌘?` / `F1` | `F1` | Haupt | 
| `cm_HelpKeyboard` | Öffnen Sie die Referenzkarte für schnelle Tastaturkürzel | `cm_HelpKeyboard` | *(Menü: Hilfe ➔ Tastatur)* | Haupt | 
| `cm_Exit` | Beenden / Beenden Sie ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Haupt | 
| `cm_About` | ATBCmder-Version, Lizenz und Credits anzeigen | `cm_About` | *(Menü: ATBCmder ➔ Über)* | Haupt | 
| `cm_OpenConfigDirectory` | Konfigurationsordner (`atbcmder.xml`) im Panel anzeigen | `cm_OpenConfigDirectory` | *(Menü: Konfiguration ➔ Konfiguration öffnen)* | Haupt | 
| `cm_ExportConfiguration` | Alle Einstellungen in ein tragbares ZIP-Paket exportieren | `cm_ExportConfiguration` | *(Menü: Konfiguration ➔ Exportieren)* | Haupt | 
| `cm_ImportConfiguration` | Einstellungen aus portablem ZIP-Bundle importieren | `cm_ImportConfiguration` | *(Menü: Konfiguration ➔ Importieren)* | Haupt | 
| `cm_CheckForUpdate` | Nach Aktualisierungen der Anwendungssoftware suchen | `cm_CheckForUpdate` | *(Menü: Hilfe ➔ Nach Updates suchen)* | Haupt | 

---

## 5. Modale Tool-Kontextverknüpfungen

Beim Öffnen spezieller Tools wie Universal Lister, dem integrierten Texteditor, der Side-by-Side-Dialoge oder Stapeldialogen aktiviert ATBCmder kontextspezifische Keymaps. Diese Verknüpfungen funktionieren direkt in jedem Toolfenster und nicht über globale anwendungsweite Registrierungsbefehle `cm_*`.

### 5.1 Universeller Lister (`Viewer` Kontext)

Aktiv bei der Vorschau von Dokumenten, Text, Code, Bildern, Audio, Video oder rohen Hex-Bytes.

| Aktion / Feature | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| Alle auswählen | Den gesamten Text/Inhalt im Viewer auswählen | `⌘A` | `Ctrl+A` | Betrachter | 
| Nur-Text-Modus | Wechseln Sie in den Nur-Text-Modus | `1` | `1` | Betrachter | 
| Binärmodus | Wechseln Sie in den Binärmodus | `2` | `2` | Betrachter | 
| Roher Hex-Modus | Wechseln Sie in den Roh-Hex-Byte-Inspektionsmodus | `3` | `3` | Betrachter | 
| Dezimalmodus | Wechseln Sie in den Dezimalmodus | `4` | `4` | Betrachter | 
| Buchansicht | Wechseln Sie in den Modus „Paginiertes Buch“ | `5` | `5` | Betrachter | 
| Bildansicht | Wechseln Sie in den Bildbetrachtermodus | `6` | `6` | Betrachter | 
| Benutzerdefinierte Plugins | Wechseln Sie zum benutzerdefinierten Plugin-Viewer | `7` | `7` | Betrachter | 
| PDF-/Office-Ansicht | Wechseln Sie in den PDF-/Office-Dokumentenlesemodus | `8` | `8` | Betrachter | 
| Codemodus | Wechseln Sie in den Syntax-hervorgehobenen Codemodus | `9` | `9` | Betrachter | 
| Bild zentrieren | Bild im Viewer-Fenster zentrieren | `C` | `C` | Betrachter | 
| An Fenster anpassen | Bild an Fensterabmessungen anpassen | `F` | `F` | Betrachter | 
| Nur für große Größen geeignet | Nur verkleinern, wenn das Bild die Fensterabmessungen überschreitet | `L` | `L` | Betrachter | 
| Wrap umschalten | Zeilenumbruch ein-/ausschalten | `W` | `W` | Betrachter | 
| Caret umschalten | Sichtbares Textcursor-Caret | umschalten `F6` | `F6` | Betrachter | 
| Text suchen | Text im Dokument suchen | `⌘F` / `F7` | `F7` | Betrachter | 
| Weiter finden | Zum nächsten Suchtreffer springen | `⌘G` / `F3` | `F3` | Betrachter | 
| Vorheriges suchen | Zum vorherigen Suchtreffer springen | `⇧⌘G` / `⇧F3` | `Shift+F3` | Betrachter | 
| Vergrößern | Bild oder PDF vergrößern | `⌘+` / `Num+` | `Num+` | Betrachter | 
| Verkleinern | Bild oder PDF verkleinern | `⌘-` / `Num-` | `Num-` | Betrachter | 
| Vollbild | Vollbildanzeigemodus umschalten | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Betrachter | 
| Viewer schließen | Lister-Viewer-Fenster schließen | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Betrachter |

---

### 5.2 Integrierter Texteditor (`Editor` Kontext)

Aktiv beim Erstellen oder Ändern von Text- und Quellcodedateien. 

| Aktion / Feature | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| Datei speichern | Geänderte Datei auf Datenträger speichern | `⌘S` / `F2` | `F2` | Herausgeber | 
| Text suchen | Text im Editordokument suchen | `⌘F` / `F7` | `F7` | Herausgeber | 
| Weiter finden | Zum nächsten Suchtreffer springen | `⌘G` / `F3` | `F3` | Herausgeber | 
| Vorheriges suchen | Zum vorherigen Suchtreffer springen | `⇧⌘G` / `⇧F3` | `Shift+F3` | Herausgeber | 
| Schneiden | Ausgewählten Text in die Zwischenablage ausschneiden | `⌘X` | `Ctrl+X` | Herausgeber | 
| Kopieren | Ausgewählten Text in die Zwischenablage kopieren | `⌘C` | `Ctrl+C` | Herausgeber | 
| Einfügen | Text aus der Zwischenablage einfügen | `⌘V` | `Ctrl+V` | Herausgeber | 
| Rückgängig machen | Letzte Eingabeaktion rückgängig machen | `⌘Z` | `Ctrl+Z` | Herausgeber | 
| Wiederholen | Letzte rückgängig gemachte Aktion wiederherstellen | `⇧⌘Z` | `Ctrl+Shift+Z` | Herausgeber | 
| Alle auswählen | Gesamten Dokumenttext auswählen | `⌘A` | `Ctrl+A` | Herausgeber | 
| Editor schließen | Texteditor-Fenster schließen | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Herausgeber | 

---

### 5.3 Visuelle Unterschiede nebeneinander (`Differ` Kontext)

Aktiv im Vergleichstool für visuelle Unterschiede. 

| Aktion / Feature | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| Text suchen | Text innerhalb der Differenzbereiche durchsuchen | `⌘F` / `F7` | `F7` | Unterscheiden | 
| Weiter finden | Zum nächsten Suchvorkommen springen | `⌘G` / `F3` | `F3` | Unterscheiden | 
| Vorheriges suchen | Zum vorherigen Suchvorkommen springen | `⇧⌘G` / `⇧F3` | `Shift+F3` | Unterscheiden | 
| Nächster Unterschied | Cursor zum nächsten Differenzblock springen | `⌥↓` *(Wahl+Runter)* | `Alt+Down` | Unterscheiden | 
| Vorheriger Unterschied | Cursor zum vorherigen Differenzblock springen | `⌥↑` *(Option+Up)* | `Alt+Up` | Unterscheiden | 
| Erster Unterschied | Direkt zum ersten Dateiunterschied springen | `⌥Fn+←` *(Opt+Home)* | `Alt+Home` | Unterscheiden | 
| Letzter Unterschied | Direkt zum letzten Dateiunterschied springen | `⌥Fn+→` *(Opt+End)* | `Alt+End` | Unterscheiden | 
| Von rechts nach links kopieren | Differenzblock vom rechten Bereich in den linken Bereich kopieren | `⌥←` *(Wahl+Links)* | `Alt+Left` | Unterscheiden | 
| Von links nach rechts kopieren | Differenzblock vom linken Bereich in den rechten Bereich kopieren | `⌥→` *(Wahl+Rechts)* | `Alt+Right` | Unterscheiden | 
| Aktualisieren / erneut scannen | Dateien erneut von der Festplatte lesen und Differenzvergleich erneut ausführen | `⌘R` | `Ctrl+R` | Unterscheiden | 
| Close Differ | Differenzvergleichsfenster schließen | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | Unterscheiden | 

---

### 5.4 Dialogfeld „Erweiterte Dateisuche“ (`FindFiles` Kontext)

Aktiv im Hintergrund-Multithread-Suchdialog. 

| Aktion / Feature | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| Suche starten | Suchausführung starten | `⏎` *(Rückgabe)* / `F9` | `F9` | FindFiles | 
| Abbrechen / Schließen | Laufende Suche abbrechen oder Dialog schließen | `⎋` *(Esc)* | `Esc` | FindFiles | 
| Ausgewählte anzeigen | Ausgewähltes Suchergebnis in Lister | anzeigen `⌘3` / `F3` | `F3` | FindFiles | 
| Ausgewählte bearbeiten | Ausgewähltes Suchergebnis im Editor | öffnen `⌘4` / `F4` | `F4` | FindFiles | 
| Neue Suche | Suchanfrage zurücksetzen und neue Suche vorbereiten | `⌘N` | `Ctrl+N` | FindFiles | 
| Filter löschen | Neue Suche mit allen Datums-/Größen-/Attributfiltern gelöscht | `⇧⌘N` | `Ctrl+Shift+N` | FindFiles | 
| Vorheriges zurückrufen | Parameter aus vorheriger Suche abrufen | `⌘L` | `Ctrl+L` | FindFiles | 

---

### 5.5 Batch-Multi-Rename-Tool (`MultiRename` Kontext)

Aktiv im Arbeitsbereich für die Stapelumbenennung. 

| Aktion / Feature | Beschreibung | Primäre macOS-Verknüpfung (mit ⌘/⌥/⇧/⌃-Glyphen) | Klassische Commander-Verknüpfung (mit Fn-Tasten) | Kontext | 
| :--- | :--- | :---: | :---: | :---: | 
| Regeln zurücksetzen | Umbenennungsmasken- und Musterregeln auf Standard zurücksetzen | `⌘R` | `Ctrl+R` | MultiRename | 
| Namen im Editor bearbeiten | Zieldateinamenliste im externen Editor zur manuellen Bearbeitung öffnen | `⌘I` | `Ctrl+I` | MultiRename | 
| Namensdatei laden | Ersatznamen aus einer externen Textdatei laden | `F3` | `F3` | MultiRename | 

---

## 6. Profi-Tipps und System-Hotkey-Optimierung

### 6.1 Beheben globaler macOS-Verknüpfungskollisionen

Bestimmte Standard-Hotkeys des macOS-Systems fangen Tastendrücke ab, bevor sie Desktop-Anwendungen erreichen. Um die volle Commander-Agilität freizuschalten, können Sie widersprüchliche macOS-Verknüpfungen anpassen oder deaktivieren: 

1. **Spotlight-Suche (`⌘Space` vs. Schnellsuche)**: 
- Standardmäßig aktiviert `⌘Space` Spotlight. Wenn Sie lieber `⌘Space` für die Dateimarkierung oder In-Panel-Suche verwenden möchten, ordnen Sie Spotlight unter **Systemeinstellungen ➔ Tastatur ➔ Tastaturkürzel... ➔ Spotlight** neu `⌥Space` zu. 
2. **Mission Control (`⌃↑`) & App Exposé (`⌃↓`)**: 
- macOS verwendet `⌃↑` und `⌃↓` für Mission Control. In ATBCmder öffnet `⌃↓` das Dropdown-Menü „Verzeichnisverlauf“. Sie können Mission Control unter **Systemeinstellungen ➔ Tastatur ➔ Tastaturkürzel... ➔ Mission Control** neu zuweisen. 
3. **Anwendung ausblenden (`⌘H`)**: 
– In macOS verbirgt `⌘H` die vorderste Anwendung. ATBCmder verwendet `⌘H` oder `⇧⌘.`, um ausgeblendete Punktdateien umzuschalten. Wenn Sie möchten, dass `⌘H` versteckte Dateien strikt umschaltet, deaktivieren Sie „Anwendung ausblenden“ in macOS oder verwenden Sie den Finder-Standard `⇧⌘.` (`Cmd+Shift+Period`). 

4. **Fensterminimierung (`⌘M`)**: 
– macOS weist `⌘M` zu, um das Fenster zum Dock zu minimieren. ATBCmder weist `⌘M` dem Batch Multi-Rename Tool (`cm_MultiRename`) zu. ATBCmder erfasst `⌘M` in seinem Hauptfenster, aber Sie können Multi-Rename auch über `Ctrl+M` oder die Symbolleiste auslösen. 

---

### 6.2 Ergonomie von Trackpad und Maus

Für Laptop-Benutzer ohne externe Tastatur kombiniert ATBCmder Tastaturkürzel mit intuitiven Trackpad-Gesten: 

* **Zum Zoomen von Miniaturansichten zusammenziehen**: Ziehen Sie in der Miniaturansicht (`cm_ThumbnailsView`) die Finger auf Ihrem MacBook-Trackpad hinein oder heraus (oder halten Sie `⌃` gedrückt und scrollen Sie), um die Größe der Miniaturansichten kontinuierlich von `48 px` bis `512 px` zu ändern. 
* **Mit zwei Fingern nach hinten/vorwärts wischen**: Wischen Sie mit zwei Fingern nach links oder rechts über die Dateitabelle, um rückwärts (`cm_ViewHistoryPrev`) und vorwärts (`cm_ViewHistoryNext`) durch den Ordnerverlauf zu navigieren. 
* **Doppelklick-Splitter**: Doppelklicken Sie irgendwo auf der vertikalen mittleren Trennleiste, um die Panels auf eine exakte 50/50-Horizontalteilung zurückzusetzen. 
* **Mit der mittleren Maustaste auf Tabs klicken**: Klicken Sie mit der mittleren Maustaste (oder tippen Sie mit drei Fingern) auf eine beliebige Ordnerregisterkarte, um sie sofort zu schließen, ohne `⌘W` zu drücken. 

---

### 6.3 Anpassen der Tastenkombinationen in den Einstellungen

Jede oben dokumentierte Verknüpfung kann angepasst oder neu gestaltet werden: 

1. Drücken Sie **`⌘,`** (oder wählen Sie **Konfiguration ➔ Optionen...**), um das Dialogfeld „Einstellungen“ zu öffnen. 
2. Wählen Sie in der Seitenleiste **Hotkeys** aus. 
3. Verwenden Sie das Dropdown-Menü **Kontext**, um auszuwählen, welchen Bereich Sie konfigurieren möchten (`Main`, `FilePanel`, `Viewer` usw.). 
4. Verwenden Sie das Suchfilterfeld, um einen beliebigen Befehl anhand des Namens oder der `cm_*`-ID zu finden. 
5. Klicken Sie auf das Verknüpfungsfeld und drücken Sie die gewünschte Tastenkombination. Der eingebaute Kollisionsdetektor warnt Sie sofort, wenn dieser Akkord bereits an anderer Stelle zugewiesen ist. 
6. Klicken Sie auf **Übernehmen**, um die Änderungen sofort zu aktivieren, ohne die Anwendung neu starten zu müssen. 

Benutzertastenkombinationen werden unter `~/.config/atbcmder/atbcmder_hotkeys.xml` (oder `~/Library/Einstellungen/atbcmder/` unter macOS) gespeichert. Sie können diese Datei mithilfe von **`cm_ExportConfiguration`** exportieren und zwischen Computern übertragen. 

--- 

<div align="center"> 
<p>Suchen Sie nach praktischen Alltagsrezepten, NAS-Montage-Workflows oder Tipps zur Fehlerbehebung?</p> 
<p><strong><a href="faq_howtos.md">Fahren Sie mit Kapitel 9 fort: Rezepte aus der Praxis und Fehlerbehebung &rarr;</a></strong></p> 
</div>