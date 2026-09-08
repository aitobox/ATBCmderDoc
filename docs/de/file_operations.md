# Kapitel 3: Dateioperationen & Hintergrundwarteschlange

Jeden Tag werden Dateimanager anhand einer Messgröße beurteilt: wie schnell, genau und sicher Sie Daten manipulieren können. In ATBCmder müssen Sie nie mit mehreren überlappenden Fenstern jonglieren, versehentliche Drop-Fehler ertragen oder untätig warten, während große Dateiübertragungen Ihren Bildschirm einfrieren. 

Dieses Kapitel behandelt das gesamte Spektrum von Dateivorgängen: direktionale Kopier- und Verschiebungsworkflows, In-Place-Inline-Umbenennung, Power-Marking mit Platzhaltern, System-Drag-and-Drop-Interoperabilität, granulare Kollisionsbehandlung, UNIX-Berechtigungen und Symlinks sowie die Multithread-Warteschlange für Hintergrundoperationen. 

---

## 1. Visueller Schnellstart: Das direktionale Betriebsmodell

Orthodoxe Dateimanager verwenden ein Richtungsmodell **Quelle ➔ Ziel**. Wenn Sie eine Dateiübertragung oder Linkerstellung initiieren, übernimmt ATBCmder die im **Aktiven Bereich** (Quelle) ausgewählten Elemente und führt den Vorgang direkt in dem im **Inaktiven Bereich** (Ziel) geöffneten Verzeichnis aus. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  AKTIVES PANEL (Quelle Source)                      INAKTIVES PANEL (Ziel Target)      │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Größe  Datum   │   │  Name                         Größe │
│  ▸ [..]                              --:--   │ K │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 Dateien gewählt: 1.8 GB]                 │   │  [Zielordner empfangsbereit]        │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Kopieren   [F6] Bewegen   [Shift+F5] Duplizieren   [F8 / ⌘⌫] In den Papierkorb   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Spickzettel für Dual-Matrix-Kernoperationen

| Aktion | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Auf Ziel kopieren** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Kopiert ausgewählte Elemente in das gegenüberliegende Bedienfeld. | 
| **In dasselbe Panel kopieren** | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Dupliziert Elemente im aktiven Bereich mit Aufforderung zum Umbenennen. | 
| **Zum Ziel verschieben** | `F6` / `Fn+F6` | `F6` | `cm_Move` | Verschiebt ausgewählte Elemente in den gegenüberliegenden Bereich. | 
| **Neuer Ordner (MkDir)** | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Erstellt ein neues Verzeichnis im aktiven Panel. | 
| **In den Papierkorb löschen** | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Verschiebt ausgewählte Elemente in den macOS-Papierkorb. | 
| **Endgültiges Löschen** | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Umgeht den Papierkorb und hebt die Verknüpfung von Dateien dauerhaft auf. | 
| **Inline-Schnellumbenennung**| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Benennt das aktive Element direkt in der Tabellenzeile um. | 
| **Dateieigenschaften** | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Öffnet das Dialogfeld „UNIX-Berechtigungen, Zeitstempel und Metadaten“. | 
| **Ordnerplatz berechnen**| `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Berechnet rekursive Bytes für Verzeichnisse (`Ctrl+L` / `cm_CalculateSpace` für die ausgewählte Gesamtzahl). | 
| **Hintergrundwarteschlange** | `Toolbar ⚡` | — | `cm_OperationsPanel` | Öffnet den 3-Warteschlangen-Hintergrundübertragungsmonitor. |

### Visuelles Wahrzeichen: Die mittlere Symbolleiste

ATBCmder verfügt über eine spezielle vertikale Schnellaktions-Symbolleiste, die direkt in die zentrale Trennwand eingebettet ist, die die beiden Bereiche trennt: 

![Middle Toolbar](images/middle_toolbar.png) 
*Die zentrale mittlere Symbolleiste bietet sofortigen Mauszugriff auf „Ansicht“ (F3), „Bearbeiten“ (F4), „Kopieren“ (F5), „Verschieben“ (F6), „Neuer Ordner“ (F7), „Löschen“ (F8) und „Panel tauschen“.* 

---

## 2. Kernoperationen: Kopieren, Verschieben, MkDir und Löschen

Die tägliche Dateiverwaltung besteht aus vier Hauptaktionen: Kopieren, Verschieben, Erstellen von Verzeichnissen und Löschen unerwünschter Dateien.

### 2.1 Dateien kopieren (`F5` / `cm_Copy`)

So kopieren Sie Dateien oder Verzeichnisse: 

1. **Wählen** Sie mit der Tastatur oder der Maus ein oder mehrere Elemente im aktiven Bereich aus. 
2. **Drücken Sie `F5`** (oder `Fn+F5` auf Apple-Tastaturen oder klicken Sie auf **Kopieren** in der mittleren Symbolleiste). 
3. Der **Kopieren-Dialog** erscheint: 
- **Zielzeile**: Wird automatisch mit dem aktuellen Verzeichnispfad des gegenüberliegenden Panels gefüllt. Sie können diesen Pfad manuell bearbeiten, einen neuen Unterordnernamen anhängen, um ihn gleichzeitig zu kopieren und zu erstellen, oder zum Durchsuchen auf `...` klicken. 
- **Start (`Enter`)**: Beginnt sofort mit dem Kopieren im Vordergrund mit einem Fortschrittsdialog in Echtzeit. 
- **Zur Warteschlange hinzufügen (`F2`)**: Stellt die Übertragung in eine Warteschlange, damit sie im Hintergrund ausgeführt wird (siehe [Abschnitt 7.4](#74-warteschlange-fur-hintergrundoperationen-cm_operationspanel)). 
- **Optionen**: Erweitert erweiterte Konfliktregeln, Attributerhaltung und Prüfsummenüberprüfungen. 

```
┌────────────────────────────────────────────────────────┐
│ Copy file(s)                                           │
│ Copy selected 3 files?                                 │
│ To: [/Volumes/Backup/Assets                          ] │
│ [Options ▼]   [Add To Queue #1 ▾]   [Cancel]   [Start] │
└────────────────────────────────────────────────────────┘
```

#### In-Panel-Duplizierung (`Shift+F5` / `cm_CopySamePanel`)

So klonen Sie schnell eine Datei im aktuellen Verzeichnis (z. B. Erstellen einer Sicherung vor der Bearbeitung von `nginx.conf`): 

- Markieren Sie das Element und drücken Sie `Shift+F5` (oder `⇧F5`). 
– ATBCmder fordert Sie mit einem Zielpfad im *gleichen* Verzeichnis auf, sodass Sie einen neuen Namen eingeben können (z. B. `nginx.conf.bak`).

#### Standard-MacOS-Zwischenablage (`Cmd+C` ➔ `Cmd+V`)

ATBCmder lässt sich vollständig in die Zwischenablage-Verknüpfungen des macOS-Systems integrieren: 

- **`Cmd+C` (`⌘C`)**: Kopiert ausgewählte Dateipfade in die Zwischenablage (`cm_CopyToClipboard`). 
- **`Cmd+V` (`⌘V`)**: Fügt Dateien aus der Zwischenablage in das aktive Bedienfeld ein (`cm_PasteFromClipboard`). 
- **`Cmd+Option+V` (`⌥⌘V`)**: Verschiebt Zwischenablagedateien in das aktive Bedienfeld (`cm_PasteAsMove`). 

---

### 2.2 Dateien verschieben (`F6` / `cm_Move`)

Beim Verschieben werden Dateien aus dem Quellverzeichnis in das Zielverzeichnis übertragen: 

1. Wählen Sie Elemente aus und drücken Sie **`F6`** (oder `Fn+F6` / klicken Sie in der mittleren Symbolleiste auf **Verschieben**). 
2. Das **Verschieben-Dialogfeld** wird geöffnet und zeigt den Ziel-Panel-Pfad an. 
3. Drücken Sie **`Enter`**, um Folgendes auszuführen: 
- **Same-Filesystem Move**: Sofort und atomar auf APFS/HFS+-Volumes durch Aktualisieren der Dateisystemkatalogreferenzen ohne Verschieben von Raw-Festplattenblöcken. 
- **Dateisystemübergreifende Verschiebung**: Streamt Daten über Volumes zum Ziel, überprüft die Byte-Vervollständigung und entfernt die Quelle bei verifizierter Ankunft sicher. 
4. Wenn sich am Ziel eine vorhandene Datei mit demselben Namen befindet, hält ATBCmder an und ruft den **Überschreibdialog** auf (siehe [Abschnitt 6](#6-kollisionsbehandlung-und-konfliktlosung)). 

---

### 2.3 Neue Verzeichnisse erstellen (`F7` / `cm_MkDir`)

Müssen Sie spontan eine Ordnerstruktur erstellen? 

1. Drücken Sie **`F7`** (oder `Fn+F7` / `Shift+Cmd+N` / `cm_MkDir`). 
2. Eine einfache Eingabeaufforderung wird angezeigt: `Enter folder name:`. 
3. Geben Sie den Ordnernamen ein und drücken Sie `Enter`. 

```
┌──────────────────────────────────────────────┐
│ Create Directory                             │
│ Enter folder name:                           │
│ [2026-09-Q3_Reports                        ] │
│                      [Cancel]      [OK (⏎)]  │
└──────────────────────────────────────────────┘
```

#### Verkettung von Unterverzeichnissen

Sie können in einem einzigen Schritt verschachtelte Ordnerhierarchien erstellen. Durch die Eingabe von `deep/nested/project/assets` werden sofort alle vier Hierarchieebenen erstellt (entspricht `mkdir -p`).

#### Autofokus-Platzierung

Bei der Erstellung platziert ATBCmder den Panel-Cursor automatisch direkt auf dem neuen Ordner, bereit für die sofortige Eingabe (`Enter`) oder Dateiübertragung. 

---

### 2.4 Dateien löschen: macOS-Papierkorb vs. permanente Bereinigung

Sicherheit und Wiederherstellbarkeit stehen im Vordergrund. ATBCmder unterstützt doppelte Löschworkflows: 

```
                  ┌────────────────────────────────────────┐
                  │          File Deletion Trigger         │
                  └───────────────────┬────────────────────┘
                                      │
                 ┌────────────────────┴───────────────────┐
                 ▼                                        ▼
    [ F8 / Delete / Cmd+Backspace ]             [ Shift+Delete / Shift+F8 ]
                 │                                        │
                 ▼                                        ▼
    macOS System Trash (.Trash)                  Permanent Unlink
      • Fully recoverable                         • Bypasses Trash
      • Put Back support in Finder                • Zero disk footprint
      • Volume .Trashes directory                 • Unrecoverable without deep carve
```

#### Löschen in den macOS-Papierkorb (`F8` / `Delete` / `Cmd+Backspace`)

– Ausgewählte Dateien werden über die macOS-APIs `send2trash` in den Papierkorb Ihres Systems geleitet. 

- Dateien können jederzeit über den macOS Finder („Put Back“) eingesehen oder wiederhergestellt werden. 
- Bestätigungsdialoge können in **Einstellungen** (`operations.confirm_delete`) aktiviert oder unterdrückt werden.

#### Endgültige sofortige Löschung (`Shift+Delete` / `Shift+F8`)

- Umgeht den Papierkorb vollständig, hebt die Verknüpfung von Dateien sofort auf und gibt Speicherplatz frei. 
- Ideal zum Löschen virtueller Multi-Gigabyte-Maschinen oder Festplatten-Images, bei denen Einschränkungen des Papierkorbpuffers oder die Erschöpfung der Festplatte ein Staging verhindern würden.

#### Volumes ohne Papierkorbunterstützung (`trash_unavailable`-Erkennung)

Beim Löschen von bestimmten Netzwerkfreigaben (SMB, NFS), virtuellen Dateisystemen (`vfs://`) oder externen Laufwerken, die mit älteren FAT/exFAT-Dateisystemen formatiert sind und kein `.Papierkorbes`-Verzeichnis haben, kann macOS keine Elemente in den Papierkorb senden. 

In solchen Fällen löst ATBCmder einen intelligenten Sicherheitsalarm aus: 
```
┌────────────────────────────────────────────────────────┐
│ Trash Unavailable                                      │
│ The volume containing '/Volumes/NAS/backup.iso' does   │
│ not support Trash.                                     │
│ Would you like to permanently delete this file?        │
│                                                        │
│ [✔] Apply to all remaining items                       │
│              [Skip]               [Delete Permanently] │
└────────────────────────────────────────────────────────┘
```
 
Sie können zwischen **Endgültig löschen**, **Überspringen** wählen oder **Auf alle verbleibenden Elemente anwenden** aktivieren, um große Batch-Löschungen unbeaufsichtigt durchzuführen.

#### Sicheres Multi-Pass-Shreddern (`Alt+Delete` / `cm_Wipe`)

Für vertrauliche Dokumente, Anmeldeinformationen oder private Schlüssel, die nicht über Raw-Flash-Recovery-Tools wiederhergestellt werden dürfen: 

- Markieren Sie das Element und wählen Sie **Menü Datei** → **Löschen** (`Alt+Delete` / `cm_Wipe`). 
– ATBCmder führt ein Multi-Pass-Überschreiben mit zufälligen Bitmustern und Nullen durch, bevor die Verknüpfung des Inodes aufgehoben wird. 

---

## 3. Inline-Schnellumbenennung und Namensbearbeitung

Das Umbenennen einer einzelnen Datei sollte keine komplexen Menüs oder Dialog-Popups erfordern. ATBCmder ermöglicht eine schnelle direkte Bearbeitung von Tabellenzeilen. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Name                                  Ext      Size      Date Modified         │
│  ▸ [..]                                         --:--     drwxr-xr-x            │
│  ● Annual_Financial_Report_2025        .pdf     4.2 MB    Today, 11:20          │
│    ▲                                                                            │
│    └── [Editable Text Box: Stem highlighted, .pdf extension preserved]          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Auslösen einer Inline-Umbenennung

1. Markieren Sie eine beliebige Datei oder ein beliebiges Verzeichnis im Bedienfeld. 
2. Drücken Sie **`F2`** oder **`Shift+F6`** (`cm_RenameOnly`) oder klicken Sie einmal auf den bereits markierten Dateinamen. 
3. Die Tabellenzelle verwandelt sich in einen Inline-Editor (`QLineEdit`).

### Intelligente Erweiterungserhaltung

Beim Umbenennen einer Datei wie `invoice_september.pdf`: 

– ATBCmder wählt automatisch nur den Basisdateinamen (`invoice_september`) vor. 
– Die Dateierweiterung (`.pdf`) bleibt nicht ausgewählt und intakt, wodurch ein versehentliches Entfernen der Erweiterung verhindert wird, das die macOS-Dateizuordnungen zerstören würde. 

- Wenn Sie die Erweiterung ändern möchten, verwenden Sie einfach die Pfeiltasten oder drücken Sie `Cmd+A` im Bearbeitungsfeld.

### Tastaturkürzel innerhalb der Inline-Umbenennung

- **`Enter` (`Return`)**: Übernimmt den neuen Namen und indiziert das Panel neu. 
- **`Esc`**: Bricht die Bearbeitung ab und stellt den ursprünglichen Namen ohne Änderungen wieder her. 
- **`Tab`**: Übernimmt den aktuellen Namen und beginnt sofort mit der Umbenennung der *nächsten* Datei unten in der Liste, was eine schnelle sequentielle Dateiumbenennung ermöglicht, ohne die Tastatur zu verlassen. 

---

## 4. Auswahltechniken: Power-Marking-Dateien

In herkömmlichen Dateimanagern sind Ihre Cursorposition und Ihre Auswahl eng miteinander verknüpft: Durch Bewegen des Cursors wird die Auswahl vorheriger Dateien aufgehoben, es sei denn, Sie halten `Cmd` gedrückt. In ATBCmder sind **Cursorfokus** und **markierte Auswahl** entkoppelt, was eine präzise Stapelbereitstellung ermöglicht. 

```
  Status Column:
  [ ]  Unselected (cursor may or may not be on row)
  [✔]  Marked / Selected (accumulated into operation payload)
```

### 4.1 Globale Auswahlaktionen

| Aktion | macOS-Verknüpfung | Klassischer Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Alle auswählen** | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Markiert jede Datei und jeden Ordner im aktiven Bereich. | 
| **Alle abwählen** | `Cmd+Shift+A` / `⇧⌘A`| `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Löscht alle Markierungen im aktiven Bereich. | 
| **Auswahl umkehren**| `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Ändert den Auswahlstatus: „Markiert“ wird zu „Unmarkiert“ und umgekehrt. | 

---

### 4.2 Muster- und Platzhalterauswahl

Durch die Auswahl von Platzhaltern können Sie mit wenigen Tastendrücken Hunderte spezifischer Dateien in einem Verzeichnis mit Tausenden gezielt ansprechen. 

```
┌────────────────────────────────────────────────────────┐
│ Mark Files by Pattern                                  │
│ Pattern: [*.jpg;*.png;*.webp                        ]  │
│                                                        │
│ [✔] Case sensitive       [ ] Regular expression        │
│                      [Cancel]                 [OK (⏎)] │
└────────────────────────────────────────────────────────┘
```

#### Gruppe markieren (`Num+` / `cm_MarkPlus`)

- Drücken Sie **`Num+`** (Keypad Plus oder Auslöser über Menü **Markieren** → **Gruppe auswählen**). 
- Geben Sie Standard-Shell-Platzhalter ein: 
- `*.log`: Markiert alle Dateien, die auf `.log` enden. 
- `*.jpg;*.png;*.webp`: Durch Semikolons getrennte Liste, um mehrere Erweiterungen gleichzeitig abzugleichen. 
- `data_2026_??.csv`: Entspricht zweistelligen Monatsdateien (`01` bis `12`). 
- `*draft*`: Entspricht jeder Datei, die das Wort „Entwurf“ enthält. 
- Drücken Sie `Enter`, um alle passenden Einträge sofort auszuwählen.

#### Markierung der Gruppe aufheben (`Num-` / `cm_MarkMinus`)

- Drücken Sie **`Num-`** (Tastatur Minus). 
– Geben Sie ein Muster ein, um passende Elemente aus einer vorhandenen Auswahl zu entfernen (z. B. `*test*`).

#### Alle mit derselben Erweiterung markieren (`Shift+Num+` / `cm_MarkCurrentExtension`)

- Positionieren Sie den Cursor auf einer beliebigen Datei (z. B. `app.tsx`). 
- Drücken Sie **`Shift+Num+`**. 
- Jede einzelne `.tsx`-Datei im aktuellen Verzeichnis wird sofort ausgewählt. 

---

### 4.3 Reichweite und Punktauswahl

- **Kontinuierliche Blockauswahl (`Shift+Up` / `Shift+Down`)**: Wenn Sie beim Navigieren mit den Pfeiltasten `Shift` gedrückt halten, wird ein zusammenhängender Auswahlblock nach oben oder unten erweitert. 
- **Einzelelement umschalten (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: 
- Durch Drücken von `Space` wird das Element unter dem Cursor markiert oder die Markierung aufgehoben und sofort die Verzeichnisgröße berechnet, wenn es sich um einen Ordner handelt. 
- Durch Drücken von `Insert` (oder `Fn+Return` auf bestimmten Mac-Tastaturen) wird das Element markiert und der Cursor springt automatisch nach unten zur nächsten Zeile, was schnelle Auswahlvorgänge mit einem Finger ermöglicht. 
- **Maus & Trackpad**: 
- `Cmd+Click`: Schaltet die Auswahl in einzelnen Zeilen um, ohne andere Auswahlen zu ändern. 
- `Shift+Click`: Erweitert die Auswahl von der aktuellen Ankerzeile auf die angeklickte Zeile.

### Live-Auswahl-Telemetrie in der Statusleiste

Immer wenn Dateien markiert werden, wird die untere Statusleiste sofort aktualisiert: 
```
[ 48 items | 12 selected (284.6 MB) ]   [ Volume Free: 184.2 GB / 494.3 GB ]
```
 
Sie erhalten in Echtzeit einen Überblick über die Situation der genauen Byte-Nutzdaten, bevor Sie große Kopien oder Löschungen vornehmen. 

---

## 5. Drag-and-Drop-Interoperabilität

ATBCmder behandelt Drag-and-Drop als erstklassigen Bürger und behält gleichzeitig die vollständige Kompatibilität mit herkömmlichen Arbeitsabläufen und dem macOS-Desktop-Ökosystem bei. 

```
       Dual-Panel Transfer                       External macOS Desktop
 ┌──────────────┐   ┌──────────────┐       ┌──────────────┐   ┌──────────────┐
 │ Left Panel   │══►│ Right Panel  │       │ ATBCmder     │══►│ Finder / App │
 │ (Source)     │   │ (Target)     │       │ Panel        │   │ (Desktop)    │
 └──────────────┘   └──────────────┘       └──────────────┘   └──────────────┘
```

### Zwischen Panels ziehen

- Klicken Sie auf markierte Elemente und ziehen Sie sie aus dem aktiven Bereich über den zentralen Splitter in den inaktiven Bereich. 
- Legen Sie die Datei an einer beliebigen Stelle in der Dateitabelle ab, um die Übertragung in den Zielordner zu starten. 
- **Ablegen auf einen Unterordner**: Wenn Sie direkt auf eine bestimmte Unterverzeichniszeile ablegen, leitet ATBCmder die Nutzlast in diesen Unterordner und nicht in das Panel-Stammverzeichnis.

### Interaktion mit macOS Finder, Desktop und externen Apps

- **Ziehen in ATBCmder**: Ziehen Sie Dateien aus dem Finder, Ihrem Desktop oder AirDrop-Downloads direkt in eines der ATBCmder-Bedienfelder, um sie zu kopieren oder zu verschieben. 
- **Herausziehen aus ATBCmder**: Ziehen Sie Dateien aus ATBCmder direkt in VS Code, Terminal (das den Dateipfad einfügt), Slack, Apple Mail oder Webbrowser-Upload-Boxen.

### Zusatztasten beim Ziehen

| Modifikatorschlüssel | Aktion ziehen | Mauszeiger-Symbol | Beschreibung | 
| :--- | :--- | :--- | :--- | 
| **Kein Modifikator** | Standardaktion | Standardpfeil | Kopiert über Volumes hinweg; bewegt sich innerhalb des gleichen Volumens. | 
| **Option (`⌥`)** | **Kopie erzwingen** | Grünes `+`-Abzeichen | Kopiert Elemente immer und lässt die Quelldateien intakt. | 
| **Befehl (`⌘`)** | **Bewegung erzwingen** | Gebogenes Pfeilabzeichen | Verschiebt Elemente immer und hebt die Verknüpfung der Quelldateien bei der Ankunft auf. |

### Gefederte Ordner

Beim Ziehen von Dateien über ein verschachteltes Verzeichnis in ATBCmder: 

- Bewegen Sie Ihren Mauszeiger **750 Millisekunden** lang über den Zielordner. 
- Der Ordner blinkt automatisch, springt auf und navigiert darin. 
- Sie können mehrere Ebenen tief in verschachtelte Unterverzeichnisse navigieren, ohne die Maustaste loszulassen, und Ihre Nutzlast dann genau an der gewünschten Stelle ablegen. 

---

## 6. Kollisionsbehandlung und Konfliktlösung

Namenskollisionen sind der gefährlichste Moment bei der Dateiverwaltung. Das Überschreiben der falschen Datei kann stundenlange Arbeit zunichte machen. ATBCmder implementiert eine Konfliktlösungs-Engine der Enterprise-Klasse, die Dateien vor dem Überschreiben überprüft und detaillierte Sicherheitskontrollen bereitstellt. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Confirm File Overwrite                                                                 │
│                                                                                        │
│ File already exists at the destination.                                                │
│                                                                                        │
│ Source:      /Users/brain/Downloads/build_artifacts.zip                                │
│ Source info: 124,518,400 bytes, 2026-09-06 14:15                                       │
│                                                                                        │
│ Destination: /Volumes/Backup/build_artifacts.zip                                       │
│ Dest info:   118,204,112 bytes, 2026-09-01 09:30                                       │
│                                                                                        │
│ Would you like to overwrite it?                                                        │
│                                                                                        │
│ [Skip All]   [Overwrite All]   [Rename]   [Auto-rename]                                │
│                                                                                        │
│ [Cancel]                                        [Skip]               [Overwrite (⏎)]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Die Aufschlüsselung des Dialogfelds „Überschreiben“.

Wenn eine Zielkollision auftritt, zeigt ATBCmder das Dialogfeld **Überschreiben der Datei bestätigen** an: 

1. **Side-by-Side-Metadatenprüfung**: 
- Vergleicht genaue Dateigrößen bis auf das einzelne Byte. 
- Vergleicht Änderungsdaten und Zeitstempel. Zeigt deutlich an, ob die Quelldatei neuer, älter oder identisch groß ist. 
2. **Entscheidungsschaltflächen für aktuelle Elemente**: 
- **Überschreiben (`Enter`)**: Ersetzt die in Konflikt stehende Zieldatei durch die Quelldatei. 
- **Überspringen**: Lässt die vorhandene Zieldatei intakt und fährt mit dem nächsten Element im Übertragungsstapel fort. 
- **Abbrechen (`Esc`)**: Bricht den verbleibenden Vorgang sofort ab und behält alle bereits übertragenen Dateien bei. 
3. **Chargen- und Sicherheitsmaßnahmen**: 
- **Alle überschreiben**: Überschreibt stillschweigend alle nachfolgenden in Konflikt stehenden Dateien in diesem Übertragungsauftrag. 
- **Alle überspringen**: Überspringt stillschweigend alle verbleibenden in Konflikt stehenden Dateien, ohne erneut nachzufragen. 
- **Umbenennen**: Fordert Sie auf, vor dem Schreiben einen benutzerdefinierten neuen Namen für die kopierte Datei einzugeben. 
- **Automatische Umbenennung**: Fügt automatisch einen inkrementellen Zähler hinzu (z. B. `build_artifacts_1.zip`, `build_artifacts_2.zip`), um sicherzustellen, dass beide Versionen ohne manuelles Eingreifen nebeneinander erhalten bleiben. 

---

### Vorkonfigurierte Kollisionsrichtlinien im Kopierdialog

Für große automatisierte Batch-Jobs oder unbeaufsichtigte Backups können Sie das Konfliktverhalten im Voraus im erweiterbaren **Optionen**-Bereich des Dialogfelds „Kopieren/Verschieben“ vorkonfigurieren: 

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Copy Options Panel                                                           │
│ ┌─ Conflict Resolution ─────────────────┐ ┌─ Attributes & Behaviors ──────┐  │
│ │ When file exists:      [Ask          ▾]│ │ [✔] Check free space          │ │
│ │ When directory exists: [Merge        ▾]│ │ [✔] Copy date/time            │ │
│ │ When cannot set attr:  [Skip         ▾]│ │ [✔] Copy attributes           │ │
│ └───────────────────────────────────────┘ │ [ ] Drop readonly flag        │  │
│ ┌─ Filters ─────────────────────────────┐ │ [✔] Copy ownership (POSIX)     │ │
│ │ [ ] Exclude empty directories         │ │ [✔] Verify after copy: [SHA256]│ │
│ └───────────────────────────────────────┘ └───────────────────────────────┘  │
│ [Save these options as default]                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```
 

- **Wenn die Datei vorhanden ist**: 
- `Ask`: Fordert den Überschreibdialog bei jeder Kollision auf (Standard). 
- `Overwrite`: Überschreibt vorhandene Dateien automatisch. 
- `Skip`: Überspringt in Konflikt stehende Dateien automatisch. 
- `Overwrite older`: Überschreibt das Ziel nur, wenn die Änderungszeit der Quelle neuer ist. 
- `Rename copied`: Fügt das Zählersuffix (`_1`, `_2`) an kopierte Dateien an. 
- `Auto-rename target`: Benennt die bestehende Zieldatei um und schreibt die neue Datei unter dem ursprünglichen Namen. 
- **Wenn ein Verzeichnis vorhanden ist**: 
- `Merge`: Vereint Ordnerinhalte rekursiv. Nicht in Konflikt stehende Unterdateien werden in vorhandene Ordner kopiert. 
- `Ask` / `Overwrite` / `Skip`. 
- **Erweiterte Verifizierung und Attribute**: 
- **Freien Speicherplatz prüfen / Speicherplatz reservieren**: Berechnet vorab die Quellbytes und stellt sicher, dass das Zielvolume vor dem Start über ausreichende Kapazität verfügt. 
- **Nach dem Kopieren überprüfen**: Berechnet kryptografische Prüfsummen (`SHA-256`, `MD5`, `SHA-1`, `CRC32`) sowohl für Quell- als auch für geschriebene Zieldateien, um 100 % Datenintegrität gegen unbemerkte Speicherbeschädigung zu gewährleisten. 
- **Links folgen**: Steuert, ob Symlinks als Zeigerreferenzen kopiert oder in vollständige physische Kopien dereferenziert werden. 
- **Datum/Uhrzeit und Besitz des Kopiervorgangs**: Behält POSIX-Erstellungsdaten, Änderungszeitstempel und Benutzer-/Gruppen-Besitz-IDs bei. 

---

## 7. ⚡ Profi-Tipps und tiefer Einblick: Erweiterte Dateisystemleistung

Um die Dual-Panel-Verwaltung zu beherrschen, müssen Sie das zugrunde liegende UNIX-Substrat von macOS verstehen. Hier finden Sie leistungsstarke Funktionen für Entwickler, Systemadministratoren und Speicherprofis.

### 7.1 Symbolische Links und Hardlinks (`cm_SymLink`, `cm_HardLink`)

macOS basiert auf Darwin UNIX und bietet zwei verschiedene Linktypen: 

```
  Symbolic Link (Symlink):
  [ Symlink File ] ──(Path Pointer)──► [ Target File / Directory ]
  • Can cross volume boundaries
  • Can point to directories
  • Breaks if target is moved

  Hard Link:
  [ Hard Link Entry ] ──┐
                        ├──(Direct Inode Reference)──► [ Raw Disk Blocks ]
  [ Original Entry  ] ──┘
  • Cannot cross filesystem boundaries (same APFS container)
  • Files only (no directory hard links on macOS)
  • Data persists until all hard links are deleted
```

#### Symbolische Links erstellen (`cm_SymLink`)

1. Markieren Sie eine oder mehrere Dateien/Ordner im aktiven Bereich. 
2. Wählen Sie **Menü Datei** → **Symbolischen Link erstellen...** (`cm_SymLink`). 
3. ATBCmder generiert automatisch einen Symlink im gegenüberliegenden Bereich, der auf den absoluten Pfad des Quellelements verweist. 
4. Symlinks zeigen im Panel ein eindeutiges Attributflag `l` an (z. B. `lrwxr-xr-x`).

#### Hardlinks erstellen (`cm_HardLink`)

1. Markieren Sie Dateien auf einem lokalen APFS/HFS+-Volume. 
2. Wählen Sie **Menü Datei** → **Hardlink erstellen...** (`cm_HardLink`). 
3. ATBCmder erstellt einen zusätzlichen Verzeichniseintrag im Zielfenster, der genau denselben Inode verwendet. 
4. Änderungen, die in eine der beiden Dateien geschrieben werden, werden sofort in beiden Dateien wirksam. Durch das Löschen einer Datei werden die Daten erst gelöscht, wenn die Linkanzahl Null erreicht. 

> [!NOTE] 
> **Einschränkungen der Linkgrenzen**: Hardlinks können keine Volume-Grenzen überschreiten oder auf Netzwerkfreigaben erstellt werden (`vfs://`). Symlinks sollten immer dann verwendet werden, wenn eine Verknüpfung über verschiedene Laufwerke oder Remote-Mount-Punkte hinweg hergestellt wird. 

---

### 7.2 Dateiberechtigungen und -attribute (`Alt+Enter` / `cm_SetFileProperties`)

Überprüfen und ändern Sie POSIX-Dateiattribute mithilfe des umfassenden **Eigenschaftendialogs**: 

```
┌────────────────────────────────────────────────────────┐
│ Properties - production_api.py                         │
│ ┌─ Metadata ─────────────────────────────────────────┐ │
│ │ Full Path:     /Users/brain/work/production_api.py │ │
│ │ Size:          84,210 bytes                        │ │
│ │ Created:       2026-03-12 10:14:22                 │ │
│ │ Last Modified: 2026-09-06 13:45:01                 │ │
│ │ Last Accessed: 2026-09-06 15:30:10                 │ │
│ └────────────────────────────────────────────────────┘ │
│ ┌─ Permissions (UNIX) ───────────────────────────────┐ │
│ │ Octal Mode: [ 755 ]                                │ │
│ │ ┌─ Owner ──┐   ┌─ Group ──┐   ┌─ Others ─┐         │ │
│ │ │ [✔] Read │   │ [✔] Read │   │ [✔] Read │         │ │
│ │ │ [✔] Write│   │ [ ] Write│   │ [ ] Write│         │ │
│ │ │ [✔] Exec │   │ [✔] Exec │   │ [✔] Exec │         │ │
│ │ └──────────┘   └──────────┘   └──────────┘         │ │
│ └────────────────────────────────────────────────────┘ │
│                             [Cancel]         [OK (⏎)]  │
└────────────────────────────────────────────────────────┘
```
 

1. **Auslöser**: Markieren Sie eine beliebige Datei oder ein beliebiges Verzeichnis und drücken Sie **`Alt+Enter`** (`⌥⏎` / `cm_SetFileProperties`). 
2. **Metadatenüberprüfung**: Zeigen Sie den vollständigen Dateipfad, die genauen Bytes, die Erstellungszeit (`btime`), die Änderungszeit (`mtime`) und die letzte Zugriffszeit (`atime`) an. 
3. **UNIX-Berechtigungsmatrix**: 
- **Interaktive Kontrollkästchen**: Schalten Sie die Berechtigungen Lesen (`r`), Schreiben (`w`) und Ausführen (`x`) unabhängig voneinander für **Eigentümer**, **Gruppe** und **Andere** um. 
- **Zwei-Wege-Oktaleingabe**: Geben Sie Oktalzahlen direkt in das Feld **Oktalmodus** ein (z. B. `755` für ausführbare Dateien, `644` für Standarddokumente, `600` für private SSH-Schlüssel). Die Kontrollkästchen werden in Echtzeit aktualisiert und umgekehrt. 
4. Drücken Sie `OK` (`Enter`), um Änderungen über POSIX `chmod` zu übernehmen. 

---

### 7.3 Berechnung der belegten Fläche (`cm_CountDirContent` / `cm_CalculateSpace` / `Space`)

Standardmäßig zeigen Dateimanager Verzeichnisgrößen als `<DIR>` oder `--` an, da die Berechnung rekursiver Ordnergrößen über Millionen von Dateien hinweg die Leistung des Dateisystems beeinträchtigen würde. ATBCmder bietet Ihnen sofortige Berechnungen auf Abruf: 

- **Größe eines einzelnen Ordners (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: Drücken Sie `Space`, während Sie sich auf einem beliebigen Ordner befinden. ATBCmder berechnet im Hintergrund die gesamten rekursiven Bytes des Ordners und ersetzt `<DIR>` durch die genaue Größe (z. B. `14.2 GB`). 
- **Alle Ordner im aktiven Panel (`Alt+Shift+Enter` / `⌥⇧⏎` / `cm_CountDirContent`)**: 
- Scannt jedes im aktuellen Panel sichtbare Verzeichnis. 
- Aktualisiert Tabellenzeilen mit präzisen Byte-Gesamtzahlen. 
- **Kumulative ausgewählte Verzeichnisgröße (`Ctrl+L` / `⌃L` / `cm_CalculateSpace`)**: 
– Sammelt die gesamten rekursiven Bytes für ausgewählte Ordner und fasst die Dateianzahl, Ordneranzahl und Speichergröße in der Statusleiste zusammen. 

---

### 7.4 Warteschlange für Hintergrundoperationen (`cm_OperationsPanel`)

Das Kopieren großer 50-GB-Videoaufnahmen oder das Übertragen Hunderttausender kleiner Quellcodedateien sollte Ihren Dateimanager niemals zum Einfrieren bringen. ATBCmder enthält eine **3-Warteschlangen-Asynchronous-Transfer-Engine**. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Background Operations                                                                  │
│ ┌─ [Queue #1 (Active)] ───────────┬─ [Queue #2 (Idle)] ───┬─ [Queue #3 (Idle)] ──────┐ │
│ │                                                                                    │ │
│ │ [RUNNING] Copy: 14 items -> /Volumes/BackupDrive/Media                             │ │
│ │   Current: RED_4K_Clip_0042.r3d (2.4 GB / 8.6 GB)                                  │ │
│ │   Speed: 428.5 MB/s | ETA: 00:01:14                                                │ │
│ │   [████████████████████████████████░░░░░░░░░░░░░░░░░░] 64%                         │ │
│ │                                                                                    │ │
│ │ [QUEUED] Move: 4 items -> /Volumes/BackupDrive/RAW_Audio                           │ │
│ │ [COMPLETED] Copy: 28 items -> /Users/brain/Projects/Website                        │ │
│ │                                                                                    │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
│                                         [Cancel Task]   [Clear Completed]   [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Warum drei unabhängige Warteschlangen?

- **Serialisiert innerhalb jeder Warteschlange**: Aufgaben in **Warteschlange Nr. 1** werden nacheinander in strenger FIFO-Reihenfolge ausgeführt. Dies verhindert ein Überlasten des Plattenkopfes auf mechanischen Festplatten und vermeidet Konfliktengpässe. 
- **Parallel über Warteschlangen hinweg**: **Warteschlange Nr. 1**, **Warteschlange Nr. 2** und **Warteschlange Nr. 3** arbeiten gleichzeitig in separaten Hintergrundthreads (`QThread`). Sie können Übertragungen mit dem Ziel **NVMe SSD A** der Warteschlange Nr. 1, Übertragungen mit dem Ziel **Externes USB-Laufwerk B** der Warteschlange Nr. 2 und Netzwerk-NAS-Uploads der Warteschlange Nr. 3 zuweisen – wodurch ein maximaler aggregierter Busdurchsatz erreicht wird.

#### Jobs an die Warteschlange senden

1. Wählen Sie im aktiven Bereich Ihre Dateien aus und drücken Sie `F5` (Kopieren) oder `F6` (Verschieben). 
2. Anstatt auf Start zu klicken, klicken Sie auf **Zu Warteschlange Nr. 1 hinzufügen** (oder klicken Sie auf das Dropdown-Chevron, um **Warteschlange Nr. 2** oder **Warteschlange Nr. 3** auszuwählen). 
3. Das Dialogfeld wird sofort geschlossen und das Hauptfenster zum weiteren Durchsuchen und Navigieren freigegeben.

#### Verwalten des Warteschlangenfensters (`cm_OperationsPanel`)

- Klicken Sie in der Hauptsymbolleiste auf die Schaltfläche **⚡ Warteschlange** oder wählen Sie **Menübefehle** → **Hintergrundoperationen** (`cm_OperationsPanel`). 
- **Echtzeit-Telemetrie**: Überprüfen Sie aktive Aufgaben, aktuell übertragene Dateien, Streaming-Übertragungsgeschwindigkeiten (z. B. `428.5 MB/s`) und berechnete ETA-Countdowns. 
- **Farbcodierte Status**: 
- `[QUEUED]`: Warten in der Schlange. 
- `[RUNNING]`: Aktive Datenübertragung. 
- `[COMPLETED]`: Mit überprüfter Byteanzahl erfolgreich abgeschlossen. 
- `[FAILED]`: Es ist ein E/A-Fehler aufgetreten (Fehlermeldung wird inline angezeigt). 
- `[CANCELLED]`: Vom Benutzer abgebrochen. 
- **Kontrollaktionen**: 
- **Aufgabe abbrechen**: Beendet die ausgewählte in der Warteschlange befindliche oder laufende Übertragung sicher. 
- **Abgeschlossen löschen**: Löscht abgeschlossene, fehlgeschlagene und abgebrochene Jobs aus der Liste. 
- **Auflösung von Hintergrundkonflikten**: Wenn eine Hintergrundaufgabe auf einen Überschreibkonflikt stößt, löst ATBCmder eine Benachrichtigung aus, die es Ihnen ermöglicht, den Konflikt zu lösen, ohne andere gleichzeitige Aufgaben abzubrechen. 

---

## 8. Praktische Schritt-für-Schritt-Rezepte

### Rezept 1: Sicheres Multi-Volume-Backup mit Prüfsummenüberprüfung

**Ziel**: Sichern Sie ein hochwertiges Fotoarchiv von Ihrem Mac auf einem externen APFS-Laufwerk, um sicherzustellen, dass keine stille Beschädigung auftritt und potenzielle Duplikate sicher aufgelöst werden. 

```
Step 1: Open source in Left Panel (~/Pictures/2026_Photos).
Step 2: Open backup destination in Right Panel (/Volumes/SanDiskPro/Photo_Backup).
Step 3: Press Cmd+A (Select All) in Left Panel.
Step 4: Press F5 (Copy).
Step 5: Click [Options ▼] to expand advanced parameters:
        • Set 'When file exists' to: [Auto-rename target]
        • Check [✔] Verify after copy: [SHA-256]
        • Check [✔] Copy date/time
        • Check [✔] Check free space
Step 6: Click [Start].
```
 
*Ergebnis: ATBCmder berechnet SHA-256-Hashes während des Kopierstreams, bestätigt die genaue Blockintegrität auf der externen Festplatte und nummeriert automatisch alle widersprüchlichen Snapshots ohne menschliches Eingreifen.* 

---

### Rezept 2: Präzisions-Staging: Wildcard-Auswahl, Inversion und Symlink-Bereitstellung

**Ziel**: Wählen Sie in einem gemischten Repository mit Code und kompilierten Artefakten alle JavaScript-, TypeScript- und JSON-Dateien aus, ignorieren Sie dabei die kompilierten Ausgaben `.map` und `.log` und verknüpfen Sie sie dann per Symlink mit einem Testbed-Ordner. 

```
Step 1: Navigate Left Panel to /Users/brain/dev/app/src.
Step 2: Navigate Right Panel to /Users/brain/dev/testbed/lib.
Step 3: Press Num+ (Select Group).
Step 4: Enter pattern: *.ts;*.tsx;*.js;*.json and press Enter.
Step 5: Notice you also matched *.test.ts files. Press Num- (Unmark Group).
Step 6: Enter pattern: *.test.ts and press Enter.
Step 7: Check your status bar: 84 files selected.
Step 8: Select Menu File → Create Symbolic Link... (cm_SymLink).
```
 
*Ergebnis: Im Testbed-Ordner werden sofort 84 symbolische Links erstellt, die eindeutig auf Ihre aktiven Quelldateien verweisen.* 

---

### Rezept 3: Parallele Aufnahme mit hohem Durchsatz mithilfe von Hintergrundwarteschlangen

**Ziel**: Laden Sie zwei große Medienkamerakarten gleichzeitig auf das RAID Ihrer Workstation, ohne die Benutzeroberfläche zu blockieren oder einen der Kartenleser zu verlangsamen. 

```
Step 1: Mount Card A (/Volumes/CFexpress_A) in Left Panel.
Step 2: Select all raw footage (Cmd+A), press F5 (Copy).
Step 3: Click [Add To Queue #1]. Transfer begins streaming in background.
Step 4: Open Card B (/Volumes/SD_Card_B) in Left Panel (Cmd+T for a new tab).
Step 5: Select all audio tracks (Cmd+A), press F5 (Copy).
Step 6: Click the queue dropdown chevron and choose [Queue #2].
Step 7: Press Toolbar ⚡ (cm_OperationsPanel) to watch both queues stream concurrently.
```
 
*Ergebnis: Beide Karten nehmen gleichzeitig Daten bei voller Hardware-Bus-Sättigung auf, während Sie weiterhin Dateien durchsuchen, Notizen bearbeiten oder Assets umbenennen.* 

---

## 9. Sicherheits- und Systemwarnungen

> [!WARNING] 
> **Permanente Löschung auf externen Laufwerken und Netzwerklaufwerken**: 
> Externen Laufwerken, die mit FAT32, exFAT oder NTFS (über Treiber von Drittanbietern) und Remote-Netzwerkfreigaben (SMB/SFTP) formatiert sind, fehlt oft ein macOS-Systemverzeichnis `.Papierkorbes`. Wenn Sie Elemente aus diesen Volumes löschen, werden Sie von ATBCmder darauf hingewiesen, dass der Papierkorb nicht verfügbar ist. Durch Bestätigen dieser Aktion werden die Dateien **dauerhaft gelöscht**. Überprüfen Sie die Pfadüberschriften immer noch einmal, bevor Sie sie bestätigen. 

> [!CAUTION] 
> **Überschreiben von Dateien bei Stapelvorgängen**: 
> Wenn Sie im Kollisionsdialog **Alle überschreiben** verwenden, unterdrückt ATBCmder weitere Kollisionswarnungen für den gesamten Job. Wenn Ihr Quellverzeichnis versehentlich doppelte Dateinamen enthält, werden vorhandene Zieldateien unwiderruflich ersetzt. Erwägen Sie die Verwendung von **Automatisches Umbenennen** oder **Älteres überschreiben** für unbeaufsichtigte Stapelkopien. 

> [!IMPORTANT] 
> **APFS-Hardlink-Einschränkungen**: 
> Hardlinks können sich nicht über verschiedene APFS-Volumes, Festplattenpartitionen oder Festplattenimages erstrecken. Wenn Sie versuchen, eine feste Verbindung zwischen zwei verschiedenen Bereitstellungspunkten (z. B. `/Users/...` zu `/Volumes/ExternalDrive/...`) zu erstellen, schlägt der Vorgang fehl. Verwenden Sie **Symbolische Links** (`cm_SymLink`), wenn Sie über verschiedene Speichervolumes hinweg verknüpfen. 

> [!TIP] 
> **Optimierung der NVMe-Übertragungsgeschwindigkeit**: 
> ATBCmder ist für modernen Apple Silicon Unified Memory und PCIe 4.0/5.0 NVMe SSDs optimiert. Standardmäßig nutzen Dateivorgänge einen leistungsstarken **1 MB-Kopierpuffer** (`operations.copy_buffer_size`). Sie können diesen Puffer unter **Einstellungen** → **Dateivorgänge** feinabstimmen, um ihn an High-End-10GbE-Netzwerkschnittstellen oder spezielle Speicherarrays anzupassen. 

---

## 10. Referenztabelle für Dual-Matrix-Tastaturen

| Kategorie | Aktion | macOS-Verknüpfung | Klassischer Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | :--- | 
| **Kerndateioperationen** | Auf Ziel kopieren | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Kopiert ausgewählte Elemente in das inaktive Panel. | 
| | In dasselbe Panel kopieren | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Klont die Datei im aktiven Bereich mit der Aufforderung zum Umbenennen. | 
| | Zum Ziel verschieben | `F6` / `Fn+F6` | `F6` | `cm_Move` | Verschiebt ausgewählte Elemente in den inaktiven Bereich. | 
| | Neues Verzeichnis | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Erstellt ein neues Verzeichnis oder einen verschachtelten Baum. | 
| | In den Papierkorb löschen | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Sendet ausgewählte Elemente in den macOS-Papierkorb. | 
| | Endgültiges Löschen | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Entbindet Dateien sofort ohne Papierkorb. | 
| | Sicheres Löschen | `Alt+Delete` / `⌥⌦` | `Alt+Delete` | `cm_Wipe` | Überschreibt Dateien mit zufälligen Daten, bevor die Verknüpfung aufgehoben wird. | 
| **Umbenennung** | Inline-Schnellumbenennung| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Benennt das aktive Element direkt in der Tabellenzeile um. | 
| | Dialog „Umbenennen“ | *Menüdatei* | — | `cm_Rename` | Öffnet einen modalen Textdialog zum Umbenennen. | 
| **Auswahl** | Alle auswählen | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Wählt alle Dateien und Ordner aus. | 
| | Alle abwählen | `Cmd+Shift+A` / `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Löscht alle Auswahlen. | 
| | Auswahl umkehren | `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Kehrt den Auswahlstatus aller Elemente um. | 
| | Gruppe markieren | `Num+` | `Num+` | `cm_MarkPlus` | Wählt Elemente nach Platzhalter- oder RegEx-Muster aus. | 
| | Markierung der Gruppe aufheben | `Num-` | `Num-` | `cm_MarkMinus` | Hebt die Auswahl von Elementen nach Platzhaltermuster auf. | 
| | Gleiche Erweiterung | `Shift+Num+` | `Shift+Num+` | `cm_MarkCurrentExtension`| Wählt alle Elemente mit derselben Dateierweiterung aus. | 
| | Auswahl umschalten | `Space` / `Insert` | `Insert` / `Space` | `cm_SelectOrDeselectFile` | Schaltet die Elementauswahl um und geht nach unten. | 
| **Zwischenablage** | In die Zwischenablage kopieren | `Cmd+C` / `⌘C` | `Ctrl+C` | `cm_CopyToClipboard` | Kopiert Dateipfade in die Systemzwischenablage. | 
| | In die Zwischenablage schneiden | `Cmd+X` / `⌘X` | `Ctrl+X` | `cm_CutToClipboard` | Schneidet Dateipfade in die Systemzwischenablage aus. | 
| | Zwischenablage einfügen | `Cmd+V` / `⌘V` | `Ctrl+V` | `cm_PasteFromClipboard` | Fügt Zwischenablagedateien in das aktive Bedienfeld ein. | 
| | Als Verschieben einfügen | `Cmd+Option+V` / `⌥⌘V`| `Ctrl+Alt+V` | `cm_PasteAsMove` | Verschiebt Zwischenablagedateien in das aktive Bedienfeld. | 
| | Vollständigen Pfad kopieren | *Menü Bearbeiten* | — | `cm_CopyFullPath` | Kopiert den absoluten UNIX-Pfad in die Zwischenablage. | 
| | Dateinamen kopieren | *Menü Bearbeiten* | — | `cm_CopyFileNameToClip` | Kopiert den Dateinamen in die Zwischenablage. | 
| **Links & Leerzeichen** | Symlink erstellen | *Menüdatei* | — | `cm_SymLink` | Erstellt einen symbolischen Link im Zielbereich. | 
| | Hardlink erstellen | *Menüdatei* | — | `cm_HardLink` | Erstellt einen Hardlink im Zielbereich. | 
| | Eigenschaften / Chmod | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Öffnet Berechtigungen, oktales CHMOD und Zeitstempel. | 
| | Raum berechnen | `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Berechnet rekursive Verzeichnisgrößen (`Ctrl+L` / `cm_CalculateSpace` für die ausgewählte Gesamtzahl). | 
| **Übertragungswarteschlange**| Hintergrundwarteschlange | `Toolbar ⚡` | — | `cm_OperationsPanel` | Öffnet den 3-Warteschlangen-Übertragungsmonitor im Hintergrund. |

--- 

<div align="center"> 
<p>Jetzt beherrschen Sie die täglichen Dateivorgänge, Auswahltechniken und Hintergrundübertragungen:</p> 
<p><strong><a href="viewers_and_editors.md">Fahren Sie mit Kapitel 4 fort: Universal Lister und integrierte Editoren &rarr;</a></strong></p> 
</div>