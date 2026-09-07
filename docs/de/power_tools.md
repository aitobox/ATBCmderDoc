# Kapitel 5: Power-Tools & Automatisierung

Bei der Dateiverwaltung großer Mengen ist die grundlegende Dateibearbeitung – das Kopieren, Verschieben und Löschen einzelner Elemente – nur der Anfang. Professionelle Ingenieure, Systemadministratoren, Inhaltsersteller und Datenanalysten stehen häufig vor komplexen betrieblichen Herausforderungen: Restrukturierung Tausender inkonsistent benannter digitaler Assets, Isolierung subtiler Code-Regressionen zwischen parallelen Release-Zweigen, Aufrechterhaltung synchronisierter Spiegelungen über Netzwerkspeicher-Arrays, Lokalisierung tief vergrabener Konfigurationsdateien und kryptografische Überprüfung der Dateiintegrität. 

ATBCmder wandelt diese arbeitsintensiven Aufgaben in schnelle, deterministische Vorgänge um. Anstatt externe Befehlszeilenskripte, Batch-Dienstprogramme von Drittanbietern oder umständliche eigenständige Diff-Anwendungen zu benötigen, integriert ATBCmder eine umfassende Automatisierungssuite direkt in seinen herkömmlichen Dual-Panel-Kern. Ganz gleich, ob Sie Ersetzungen regulärer Ausdrücke in einem gesamten Fotoarchiv durchführen, eine bidirektionale Verzeichnissynchronisierung mit Hashing auf Inhaltsebene durchführen oder Suchergebnisse mit mehreren Filtern in einen virtuellen Arbeitsbereich einspeisen müssen, ATBCmder bietet die Tools, die Sie benötigen, mit vollständiger Tastatureffizienz. 

---

## 1. Visueller Schnellstart: Die Automatisierungs-Engine und Befehlsmatrix

ATBCmder unterteilt Elektrowerkzeuge und Automatisierung in sechs spezialisierte Funktionsbereiche, die nahtlos mit der Dual-Panel-Schnittstelle interagieren: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                DUAL FILE PANELS                                        │
│     Left Panel (Source / Directory A)        Right Panel (Target / Directory B)        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Batch Multi-Rename (Ctrl+M)         │  [2] Side-by-Side File Diff (Meta+Shift+F12)│
│      Tokens, RegEx, Counters, Preview    │      Line highlights, Hunk sync, In-place   │
│                                          │                                             │
│  [3] Directory Sync (Shift+F12)          │  [4] Advanced Search (Alt+F7)               │
│      Content/Date compare, Asym mirror   │      Spotlight / Deep scan ➔ Feed to Listbox│
│                                          │                                             │
│  [5] Semantic Command Bar (/)            │  [6] File Utilities & Security              │
│      Spotlight queries, AI intent, NLP   │      Split/Link, Checksum, Wipe (Alt+Del)   │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Feed to Listbox] ➔ Populates virtual panel tab for bulk operations across directories│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Spickzettel zur Dual-Matrix-Automatisierung

| Aktion | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Batch-Mehrfachumbenennung** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Öffnet das Dialogfeld „Batch-Mehrfachumbenennung“. | 
| **Side-by-Side-Dateiunterschied** | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | Vergleicht zwei ausgewählte Dateien nebeneinander (`Shift+F3` für `cm_CompareContents`). | 
| **Verzeichnissynchronisierung** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Vergleicht und synchronisiert Dual-Panel-Verzeichnisse. | 
| **Erweiterte Dateisuche** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | Öffnet den Suchdialog mit mehreren Filtern. | 
| **Spotlight-Schnellsuche** | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Befehlsmenü)* | Leitet eine sofortige Spotlight-Metadatensuche ein. | 
| **Semantische Befehlseingabe**| `/` | `/` | `cm_VisSemanticCommand` | Aktiviert die eingebettete Befehlsleiste in natürlicher Sprache. | 
| **Große Datei teilen** | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | Teilt große Dateien in nummerierte Blöcke auf. | 
| **Geteilte Dateien kombinieren** | Menü: Dateien ➔ Dateien kombinieren | — | `cm_FileLinker` / `cm_Combine` | Setzt die Blöcke `.001`, `.002` in einer einzigen Datei zusammen. | 
| **Prüfsumme berechnen** | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | Berechnet MD5-, SHA-1-, SHA-256- oder SHA-512-Hashes. | 
| **Prüfsummendatei überprüfen** | Extras-Menü | — | `cm_CheckSumVerify` / `cm_VerifyChecksum` | Überprüft Dateien anhand von `.md5`, `.sha256` oder `.sfv`. | 
| **Sicheres Löschen (Shred)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Überschreibt und löscht Dateien sicher. | 
| **Systemterminal ausführen** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Erzeugt das macOS-Terminal im aktuellen Panel-Pfad. | 

---

## 2. Batch-Multi-Rename-Tool (`Ctrl+M` / `⌃M` / `cm_MultiRename`)

Das manuelle Umbenennen Dutzender oder Hunderter Dateien ist mühsam und fehleranfällig. Mit dem **Batch Multi-Rename Tool** (`cm_MultiRename`, in der klassischen Architektur `fmultirename.pas` zugeordnet) können Sie flexible Benennungsmuster definieren, dynamische Sequenzzähler anwenden, Fallkonvertierungen durchführen und leistungsstarke Such- und Ersetzungsregeln für reguläre Ausdrücke (RegEx) mit visuellen Sicherheitsgarantien in Echtzeit ausführen. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Abbildung 5.1: Das Batch Multi-Rename Tool mit Live-Vorschauzeilen, Token-Masken, numerischen Zählerparametern und Duplikaterkennung.*

### 2.1 Der Multi-Rename-Workflow

1. **Dateien auswählen**: Wählen Sie im aktiven Dateibereich die Dateien oder Verzeichnisse aus, die Sie umbenennen möchten, indem Sie `Space`, `Insert` oder eine Platzhalterauswahl (`+`) verwenden. Wenn nichts ausgewählt ist, wird das Element unter dem Cursor verwendet. 
2. **Tool starten**: Drücken Sie **`Ctrl+M`** (`⌃M`) oder wählen Sie **Dateien ➔ Multi-Rename Tool...** aus der Menüleiste. 
3. **Vorlagen und Regeln konfigurieren**: Geben Sie Dateinamen-/Erweiterungsmasken ein, legen Sie Zähleroptionen fest oder definieren Sie Such- und Ersetzungszeichenfolgen. 
4. **Live-Vorschau prüfen**: Die dreispaltige Tabelle (`Old Name`, `New Name`, `Directory`) wird bei jedem Tastendruck sofort aktualisiert. 
5. **Ausführen**: Klicken Sie auf **Umbenennen starten** (oder drücken Sie `Enter`). ATBCmder führt die Umbenennungen atomar durch und aktualisiert die Dateibereiche. 

---

### 2.2 Template-Tokens und Range-Slicing

ATBCmder verwendet intuitive in Klammern gesetzte Token, um auf Teile der ursprünglichen Dateimetadaten zu verweisen: 

| Token | Beschreibung | Beispieleingabe | Resultierender Wert | 
| :--- | :--- | :--- | :--- | 
| **`[N]`** | Ursprünglicher Dateiname ohne Erweiterung | `report_2026.pdf` | `report_2026` | 
| **`[E]`** | Ursprüngliche Dateierweiterung (ohne Punkt) | `archive.tar.gz` | `gz` | 
| **`[C]`** | Sequentielle numerische Zähler | *(Datei 3 in der Liste)* | `003` (abhängig von der Zifferneinstellung) | 
| **`[Y]`** | 4-stellig Jahr der Dateiänderung | `2026-09-06` | `2026` | 
| **`[M]`** | 2-stellig Monat der Dateiänderung | `September` | `09` | 
| **`[D]`** | 2-stelliger Tag der Dateiänderung | `6th` | `06` | 
| **`[h]`** | 2-stellige Stunde (24-Stunden-Uhr) | `14:30:15` | `14` | 
| **`[m]`** | 2-stellige Minute | `14:30:15` | `30` | 
| **`[s]`** | 2-stellige Sekunde | `14:30:15` | `15` |

#### Zeichenbereichsaufteilung (`[Na-b]` / `[Ea-b]`)

Mit 1-basiertem Index-Slicing können Sie bestimmte Zeichenbereiche aus dem Originalnamen oder der Originalerweiterung extrahieren: 

- **`[N1-4]`**: Extrahiert die ersten 4 Zeichen des Namens. Für `Document_Final.txt` ergibt dies `Docu`. 
- **`[N5-]`**: Auszüge vom 5. Zeichen bis zum Ende des Namens. Für `DSC_0982.jpg` ergibt dies `0982`. 
- **`[N-5]`**: Extrahiert bis zum 5. Zeichen. 
- **`[E1-2]`**: Extrahiert die ersten 2 Zeichen der Erweiterung. Für `archive.html` ergibt dies `ht`. 

---

### 2.3 Zählersteuerung und numerische Sequenzen

Die Gruppe **Zählereinstellungen** ermöglicht eine detaillierte Steuerung der numerischen Indizierung: 

- **Start bei**: Die Start-Ganzzahl für die Zählersequenz (Standard: `1`). 
- **Schritt**: Der für jede nachfolgende Datei hinzugefügte Inkrementwert (Standard: `1`). Wenn Sie Schritt auf `2` setzen, wird `1, 3, 5, 7...` generiert. 
- **Ziffern**: Die Nullauffüllbreite (Bereich: `1` bis `10`). Durch das Festlegen von Ziffern auf `3` werden Zahlen als `001`, `002`, `003` formatiert. Durch das Setzen von Ziffern auf `1` werden führende Nullen deaktiviert (`1`, `2`, `3`). 

---

### 2.4 Suchen & Ersetzen und reguläre Ausdrücke

Die Gruppe **Suchen & Ersetzen** ermöglicht Textersetzungen für alle ausgewählten Elemente: 

- **Suchen**: Ziel-Teilzeichenfolge oder reguläres Ausdrucksmuster. 
- **Ersetzen durch**: Ersatzzeichenfolge. Wenn RegEx aktiviert ist, verweisen Rückverweise (`$1`, `$2` oder `\1`, `\2`) auf Erfassungsgruppen. 
- **Reguläre Ausdrücke verwenden (Regex)**: Schaltet die Analyse regulärer Ausdrücke der Python-Standardbibliothek um. 
- **Groß-/Kleinschreibung beachten**: Wenn diese Option deaktiviert ist, ignoriert der Abgleich die Groß-/Kleinschreibung von Zeichen (z. B. Übereinstimmung mit `.JPG` und `.jpg`).

#### Leistungsstarke RegEx-Ersetzungsbeispiele

```
Example 1: Strip unwanted tracking or release tags from filenames
Input File:      Album_Artist_-_Track_01_[Lossless_24bit_96kHz].flac
Find Pattern:    \s*\[.*?\]
Replace with:    (leave empty)
Output File:     Album_Artist_-_Track_01.flac

Example 2: Reorder dates from YYYY-MM-DD to DD-MM-YYYY
Input File:      Invoice_2026-09-06_Acme.pdf
Find Pattern:    (\d{4})-(\d{2})-(\d{2})
Replace with:    $3-$2-$1
Output File:     Invoice_06-09-2026_Acme.pdf

Example 3: Convert spaces and underscores to standardized hyphens
Input File:      my new blog post_draft.md
Find Pattern:    [ _]+
Replace with:    -
Output File:     my-new-blog-post-draft.md
```
 

---

### 2.5 Fallkonvertierungsmodi

ATBCmder bietet eine sofortige Normalisierung der Groß-/Kleinschreibung, ohne dass komplexe Muster erforderlich sind: 

- **Keine Änderung**: Behält die ursprüngliche Groß- und Kleinschreibung bei. 
- **Kleinbuchstaben**: Konvertiert den gesamten Dateinamen und die Erweiterung in Kleinbuchstaben (`PHOTO_001.JPG` ➔ `photo_001.jpg`). 
- **GROSSBUCHSTABEN**: Wandelt alle Zeichen in Großbuchstaben um (`readme.txt` ➔ `README.TXT`). 
- **Großbuchstabe des ersten Buchstabens**: Schreibt den Anfangsbuchstaben jedes Wortes groß (`war and peace.epub` ➔ `War And Peace.epub`). 

---

### 2.6 Live-Vorschau-Raster und Kollisionsschutz

Das Umbenennen von Hunderten von Dateien ohne Vorschau kann zu katastrophalen Datenüberschreibungen führen. ATBCmder implementiert eine **Null-Unfall-Sicherheitsarchitektur**: 

1. **Sofortige entprellte Vorschau**: Während Sie Eingaben in die Vorlage eingeben oder Drehfelder anpassen, berechnet die Tabelle sofort die resultierenden Dateinamen. 
2. **Erkennung doppelter Ziele**: ATBCmder scannt alle berechneten Ausgabedateinamen im Zielordner. Wenn zwei oder mehr Dateien genau den gleichen Namen erhalten würden oder wenn ein Dateiname in eine leere Zeichenfolge aufgelöst würde: 
- Die kollidierenden Zeilen werden sofort in auffälligem Rot hervorgehoben (`#FFEBEB` / `#D70000` im hellen Modus, `#4A1515` / `#FF8080` im dunklen Modus). 
- Die Schaltfläche **Umbenennen starten** ist automatisch **deaktiviert**. 
- Ein Tooltip warnt: * „Namenskollisionen erkannt. Bitte lösen Sie Duplikate vor dem Umbenennen auf.“* 
3. **Kollisionsbeseitigung**: Sobald Sie Ihren Zähler, Ihre Vorlage oder Ihren regulären Ausdruck anpassen, um alle Zieldateinamen eindeutig zu machen, wird die Warnung gelöscht und die Schaltfläche **Umbenennen starten** wird wieder aktiviert. 

---

### 2.7 Praktische Schritt-für-Schritt-Rezepte

#### Rezept A: Digitalkamerafotos mit Zeitstempeln umbenennen

Verwandeln Sie kryptische Kameranamen (`IMG_4092.JPG`, `IMG_4093.JPG`) in chronologisch organisierte Assets: 

1. Wählen Sie die Fotodateien aus und drücken Sie **`Ctrl+M`**. 
2. Setzen Sie **Dateinamenvorlage** auf: `Photo_[Y][M][D]_[C]`. 
3. Setzen Sie **Erweiterungsvorlage** auf: `[E]`. 
4. Stellen Sie **Ziffern** auf `3` und **Beginn bei** auf `1` ein. 
5. Setzen Sie **Fallkonvertierung** auf `lowercase`. 
6. Vorschau des Ergebnisses: `photo_20260906_001.jpg`, `photo_20260906_002.jpg`. 
7. Drücken Sie `Enter`, um sich zu bewerben.

#### Rezept B: Hinzufügen eines Präfixes unter Beibehaltung von Name und Erweiterung

Stellen Sie einem Dokumentenstapel einen Projektcode voran: 

1. Wählen Sie Dokumente aus und drücken Sie **`Ctrl+M`**. 
2. Geben Sie unter **Dateinamenvorlage** Folgendes ein: `PRJ-ALPHA_[N]`. 
3. Belassen Sie **Erweiterungsvorlage** als `[E]`. 
4. Klicken Sie auf **Umbenennen starten**. 

---

## 3. Paralleler visueller Dateiunterschied (`Meta+Shift+F12` / `⌘⇧F12` / `cm_FileDiff`)

Das Erkennen von Unterschieden zwischen Konfigurationsrevisionen, Quellcodedateien oder Datendumps ist eine tägliche Aufgabe für Power-User. ATBCmder enthält einen integrierten, parallelen **Visual File Diff Viewer** (`DiffViewerDialog`), der den Start schwerer externer Tools überflüssig macht. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Side-by-side Diff: config.py (Left)  vs.  config.py.new (Right)                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [💾 Save Left] [💾 Save Right] | [Copy to Right →] [← Copy to Left] | [Prev] [Next]    │
│ [🔄 Re-compare] | [✔] Ignore whitespace  [ ] Ignore case  [ ] Ignore blank lines       │
├─────────────────────────────────────────────┬──────────────────────────────────────────┤
│ config.py (Left)                            │ config.py.new (Right)                    │
├─────────────────────────────────────────────┼──────────────────────────────────────────┤
│ 12: DEBUG = False                           │ 12: DEBUG = False                        │
│ 13: LOG_LEVEL = "INFO"                      │ 13: LOG_LEVEL = "DEBUG"      [CHANGED]   │
│ 14: PORT = 8080                             │ 14: PORT = 8080                          │
│ 15: # Deprecated database setting           │ 15:                                      │
│ 16: DB_TIMEOUT = 30              [REMOVED]  │ 16: DB_TIMEOUT = 10          [CHANGED]   │
│ 17:                                         │ 17: SSL_ENABLED = True       [ADDED]     │
├─────────────────────────────────────────────┴──────────────────────────────────────────┤
│  Difference 2 of 4  │  Ln 16, Col 1 (Left)  │  Ln 16, Col 1 (Right)                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Starten von File Diff

- **Zwei ausgewählte Dateien vergleichen**: Wählen Sie in einem einzigen Panel genau zwei Dateien aus und drücken Sie **`Meta+Shift+F12`** (`⌘⇧F12`) oder wählen Sie **Befehle ➔ Nach Inhalt vergleichen...**. 
- **Gegnerische Dateien vergleichen**: Markieren Sie eine Datei im linken Bereich, markieren Sie die entsprechende Datei im rechten Bereich und lösen Sie `cm_CompareContents` aus. 
- **Unterstützte Befehle**: `cm_CompareContents`, `cm_FileDiff` und `cm_CompareByContent` leiten alle an die Side-by-Side-Vergleichs-Engine weiter. 

---

### 3.2 Visuelle Differenzhervorhebung und Farbcodes

Die Diff-Engine analysiert Text Zeile für Zeile mithilfe eines optimierten Hunt-Szymanski-LCS-Algorithmus (`TextDiffer`) und unterteilt Unterschiede in farbcodierte Abschnitte: 

| Diff-Typ | Licht-Themen-Highlight | Dunkles Theme-Highlight | Beschreibung | 
| :--- | :--- | :--- | :--- | 
| **Zeilen hinzugefügt** | Weicher Smaragd (`#e6ffed`) | Dunkles Waldgrün (`#234b2d`) | Zeilen sind nur in der rechten Datei vorhanden. | 
| **Entfernte Zeilen** | Weiches Purpur (`#ffeef0`) | Dunkles Purpurrot (`#552328`) | Zeilen sind in der linken Datei vorhanden, fehlen aber in der rechten Datei. | 
| **Geänderte Zeilen** | Sanfter Bernstein (`#fff5b1`) | Dunkles Bernsteingold (`#50461e`) | Linien zwischen linker und rechter Version geändert. | 
| **Aktiver Adonis** | Lebendiger Kontrastfarbton | Lebendiger Kontrastfarbton | Der Differenzblock, auf den sich der Cursor derzeit konzentriert. | 

Jeder Bereich verfügt über einen eigenen linken Randstreifen (`LineNumberArea`), in dem 1-basierte Zeilennummern synchronisiert mit Diff-Positionen angezeigt werden. 

---

### 3.3 Synchronisiertes Scrollen und Wiedereintrittssicherheit

Beim Vergleich langer Quelldateien mit Tausenden von Zeilen erfordert die Navigation durch den Code eine Lockstep-Koordination: 

- Durch Scrollen der vertikalen oder horizontalen Bildlaufleiste eines der beiden Editoren wird der gegnerische Editor sofort um den gleichen Pixelversatz angepasst. 
– ATBCmder implementiert eine interne **Wiedereintrittssperre** (`_syncing_vscroll`, `_syncing_hscroll`), die Ereignisrückkopplungsschleifen, Stottern oder Cursordrift verhindert. 

---

### 3.4 Hunk-Navigation und bidirektionale Zusammenführung

Sie können durch Unterschiede navigieren, ohne die Maus zu verwenden: 

- **Nächster Unterschied**: Drücken Sie **`Alt+Down`** / `⌥↓` (oder `Ctrl+Down`). 
- **Vorheriger Unterschied**: Drücken Sie **`Alt+Up`** / `⌥↑` (oder `Ctrl+Up`). 
- **Zu Hunk springen**: Wenn Sie direkt auf eine hervorgehobene Zeile in einem der Bereiche klicken, wird dieser Hunk automatisch als aktiv gesetzt.

#### Bidirektionale Zusammenführung (Vimdiff `dp` / `do` Kompatibilität)

Unterschiede zwischen Dateien mit nur einem Tastendruck zusammenführen: 

- **Von links nach rechts kopieren (`→`)**: Drücken Sie **`Alt+Right`** / `⌥→` (oder `Ctrl+Alt+Right` oder Vimdiff `dp` über **`Alt+P`**). Der aktive Abschnitt im linken Editor ersetzt den entsprechenden Abschnitt im rechten Editor. 
- **Von rechts nach links kopieren (`←`)**: Drücken Sie **`Alt+Left`** / `⌥←` (oder `Ctrl+Alt+Left` oder Vimdiff `do` über **`Alt+O`**). Der aktive Abschnitt im rechten Editor ersetzt den entsprechenden Abschnitt im linken Editor. 

---

### 3.5 Direktbearbeitung und atomares Speichern

Im Gegensatz zu Diff-Viewern, die Text als schreibgeschützt behandeln, sind beide Bereiche in ATBCmder voll funktionsfähige Code-Editoren: 

- Geben Sie Text direkt in einem der Editoren ein, fügen Sie ihn ein oder löschen Sie ihn. 
- Wenn manuelle Änderungen Zeilen ändern, drücken Sie **`F5`** (oder `Ctrl+R`), um die Differenzberechnung für die aktualisierten Puffer erneut auszuführen. 
- Linke Datei speichern: Klicken Sie auf **💾 Linke Datei speichern** (oder drücken Sie `Cmd+S` / `Ctrl+S`, während der linke Editor den Fokus hat). 
- Rechte Datei speichern: Klicken Sie auf **💾 Rechte Datei speichern** (oder drücken Sie `Cmd+S` / `Ctrl+S`, während der rechte Editor den Fokus hat). 

---

### 3.6 Vergleichsfilteroptionen

Mit der Diff-Viewer-Symbolleiste können Sie echte Logikänderungen vom Formatierungsrauschen isolieren: 

- **Leerzeichen ignorieren (`_cb_ws`)**: Ignoriert Änderungen an Tabulatoren, nachgestellten Leerzeichen und Leerzeichen-gegen-Tabulator-Einrückungen. 
- **Groß-/Kleinschreibung ignorieren (`_cb_case`)**: Führt Zeichenvergleiche ohne Berücksichtigung der Groß-/Kleinschreibung durch. 
- **Leerzeilen ignorieren (`_cb_blank`)**: Reduziert das Hinzufügen und Löschen von Leerzeilen und konzentriert sich ausschließlich auf wesentliche Codeänderungen. 

---

### 3.7 Erkennung von Binärdateiunterschieden

Wenn eine der zum Vergleich ausgewählten Dateien Nullbytes oder binäre MIME-Signaturen enthält (z. B. Bilder, ausführbare Dateien, kompilierte Archive), ruft ATBCmder automatisch `BinaryDiffer` auf: 

- Zeigt Dateigrößen und kryptografische SHA-256-Hashes nebeneinander an. 
- Gibt eindeutig an, ob die Binärdateien byteidentisch oder divergent sind. 

---

## 4. Verzeichnissynchronisierung (`Shift+F12` / `⇧F12` / `cm_SyncDirs`)

Die Synchronisierung von Verzeichnisbäumen auf lokalen Festplatten, Sicherungslaufwerken und Netzwerkspeichern ist ein Grundpfeiler zuverlässiger Systeme. Der **Directory Synchronizer** von ATBCmder (`SyncDirsDialog`, zugeordnet zu `fsyncdirsdlg.pas`) vergleicht gesamte Ordnerhierarchien, ermittelt genaue Richtungsvorgänge und zeigt eine Vorschau aller Dateikopien und -löschungen an, bevor sie Ihren Speicher berührt. 

![Directory Synchronization](images/folder_synchronization.png) 
*Abbildung 5.2: Dialogfeld „Verzeichnissynchronisierung“ mit Anzeige des rekursiven Vergleichsstatus, gerichteter Synchronisierungspfeile und Steuerelementen für asymmetrische Spiegelung.*

### 4.1 Starten der Verzeichnissynchronisierung

1. Öffnen Sie das **Quellverzeichnis** im linken Bereich und das **Zielverzeichnis** im rechten Bereich. 
2. Drücken Sie **`Shift+F12`** (`⇧F12`) oder wählen Sie **Befehle ➔ Verzeichnisse synchronisieren...**. 
3. Das Dialogfeld „Verzeichnisse synchronisieren“ wird angezeigt, wobei beide Pfade in den Kopfzeilenkarten vorab ausgefüllt sind. 

---

### 4.2 Vergleichsmethoden und Präzision

Konfigurieren Sie vor der Synchronisierung Ihre Vergleichskriterien auf der Karte **Synchronisierungseinstellungen**: 

| Einstellung | Standard | Beschreibung | 
| :--- | :--- | :--- | 
| **Unterverzeichnisse vergleichen** | `Enabled` | Durchläuft rekursiv alle verschachtelten Verzeichnisse. | 
| **Nach Inhalt vergleichen** | `Disabled` | Liest und überprüft Dateibytes direkt mit `filecmp.cmp`. Garantiert 100 % Genauigkeit für Dateien mit identischen Zeitstempeln, aber geänderten Daten. | 
| **Datum ignorieren** | `Disabled` | Vergleicht Dateien ausschließlich nach Bytegröße und ignoriert dabei die Zeitstempel der Dateisystemänderungen. | 
| **FAT/SMB-Zeitstempeltoleranz** | `2.0 sec` | Berücksichtigt automatisch FAT/FAT32/exFAT 2-Sekunden-Zeitstempelauflösungen und verhindert so falsche Nichtübereinstimmungsflags bei der Synchronisierung zwischen macOS und externen Laufwerken. | 

---

### 4.3 Richtungsanalyse und Statusindikatoren

Klicken Sie auf **Vergleichen**, um einen nicht blockierenden Hintergrundvergleichs-Worker (`SyncCompareWorker`) zu starten. Die Vergleichstabelle wird mit farbcodierten Richtungszeilen gefüllt: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Relative Path             │ Operation │ Reason            │ Details                    │
├───────────────────────────┼───────────┼───────────────────┼────────────────────────────┤
│ assets/banner.png         │    ->     │ Left is newer     │ 2026-09-06 > 2026-08-15    │
│ docs/manual.pdf           │    ->     │ Right missing     │ File exists only on left   │
│ config/settings.json      │    <-     │ Right is newer    │ 2026-09-06 > 2026-09-01    │
│ vendor/legacy_lib.so      │    <-     │ Left missing      │ File exists only on right  │
│ build/cache.db            │    !=     │ Conflict          │ Timestamp / type mismatch  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

- **`->` (von links nach rechts)**: Die Datei links ist neuer oder existiert nur links. Standardaktion: Nach rechts kopieren. 
- **`<-` (von rechts nach links)**: Die Datei auf der rechten Seite ist neuer oder existiert nur auf der rechten Seite. Standardaktion: Nach links kopieren (im Zwei-Wege-Modus). 
- **`=` (Gleich)**: Dateien stimmen in Größe und Zeitstempel/Inhalt überein. Aus der aktiven Synchronisierungsliste herausgefiltert, um Zeit zu sparen. 
- **`!=` (Konflikt)**: Inkompatible Verzeichnis-gegen-Datei-Kollision oder unlösbarer Zeitstempelkonflikt. Wird aus Gründen der Datensicherheit während der automatischen Massensynchronisierung übersprungen. 

---

### 4.4 Asymmetrische Spiegelung vs. bidirektionale symmetrische Synchronisierung

ATBCmder unterstützt zwei grundsätzlich unterschiedliche Synchronisationsphilosophien:

#### 1. Zwei-Wege-symmetrische Synchronisierung (Standard)

- **Ziel**: Bringen Sie beide Verzeichnisse in Einklang, sodass beide über die neuesten Versionen jeder Datei verfügen. 
- **Aktion**: Mit `->` gekennzeichnete Dateien werden von links nach rechts kopiert. Mit `<-` gekennzeichnete Dateien werden von rechts nach links kopiert. 
- **Sicherheit**: Auf beiden Seiten werden keine Dateien gelöscht.

#### 2. Asymmetrische Spiegelung (Kontrollkästchen `Asymmetric` aktiviert)

- **Ziel**: Machen Sie das rechte Verzeichnis zu einer exakten, identischen Kopie des linken Verzeichnisses. 
- **Aktion**: Mit `->` gekennzeichnete Dateien werden von links nach rechts kopiert. Dateien auf der rechten Seite, die auf der linken Seite *nicht* vorhanden sind (`<- Right missing on Left`), werden **dauerhaft aus dem rechten Verzeichnis entfernt**. 
- **Anwendungsfall**: Erstellen makelloser Backup-Spiegel auf externen Backup-Festplatten oder NAS-Freigaben. 

---

### 4.5 Sicherheits- und Auditprotokollierung vor der Ausführung

- **Vor der Synchronisierung prüfen**: Überprüfen Sie die ausgefüllte Tabelle sorgfältig. Sie können für jede Übertragung die genauen relativen Pfade und die betrieblichen Gründe einsehen. 
- **Steuerung stoppen**: Wenn ein großer Vergleichs- oder Synchronisierungsauftrag abgebrochen werden muss, klicken Sie auf **Stop**. Der Hintergrundthread wird sicher beendet, ohne dass beschädigte Teildateien zurückbleiben. 
- **Automatisiertes Prüfprotokoll**: Jedes während der Synchronisierung ausgeführte Kopieren, Überschreiben und Löschen wird im internen **Vorgangsprotokoll** von ATBCmder aufgezeichnet (`LogCategory.COPY_MOVE_LINK`, `LogCategory.DELETE`). 

---

## 5. Erweiterte Dateisuche und Zuführung zur Listbox (`Alt+F7` / `⌥F7` / `cm_Search`)

Das Auffinden bestimmter Dateien in verschachtelten Ordnerstrukturen ist ein häufiger administrativer Engpass. ATBCmder bietet einen leistungsstarken **Dialog zur erweiterten Dateisuche** (`SearchDialog`, zugeordnet zu `fFindDlg.pas`), der die native macOS Spotlight-Indizierung mit einer umfassenden Dateisystem-Scan-Engine und der unverzichtbaren Funktion **Feed to Listbox** kombiniert. 

![Advanced File Search](images/advanced_search_dialog.png) 
*Abbildung 5.3: Dialogfeld „Erweiterte Dateisuche“ mit Multifilter-Parametern, Deep-Scan-Steuerelementen und der Schaltfläche „Zu Listbox hinzufügen“.*

### 5.1 Suche starten

- Drücken Sie in einem beliebigen Bereich **`Alt+F7`** (`⌥F7`) oder wählen Sie **Befehle ➔ Dateien durchsuchen...**. 
- Das Suchdialogfeld wird geöffnet und das Feld **Im Verzeichnis suchen** ist bereits mit dem aktuellen Pfad des aktiven Panels ausgefüllt. 

---

### 5.2 Dual-Search-Backends: Spotlight vs. Deep Scan

ATBCmder verfügt über zwei spezialisierte Suchmaschinen: 

```
                  ┌───────────────────────────────────────────────┐
                  │          Search Query Triggered               │
                  └───────────────────────┬───────────────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
    ┌───────────────────────────┐                   ┌───────────────────────────┐
    │  Spotlight Engine         │                   │  Deep Scan Engine         │
    │  (SpotlightSearchWorker)  │                   │  (DeepScanWorker)         │
    ├───────────────────────────┤                   ├───────────────────────────┤
    │ • Uses macOS mdfind       │                   │ • Recursive os.scandir    │
    │ • Millisecond results     │                   │ • Scans unindexed drives  │
    │ • APFS metadata indexed   │                   │ • Network shares (SMB/NFS)│
    │ • Standard local storage  │                   │ • Raw text/regex parsing  │
    └───────────────────────────┘                   └───────────────────────────┘
```
 

1. **Spotlight-Suchmaschine (`SpotlightSearchWorker`)**: Wenn Sie unter macOS auf **Suche starten** klicken (oder `Enter` drücken), wird der Spotlight-Metadatenindex des Systems (`mdfind`) verwendet. Es ruft im Bruchteil einer Sekunde Tausende übereinstimmender Pfade über Gigabyte an Speicher ab. 
2. **Deep Scan Engine (`DeepScanWorker`)**: Durch Klicken auf **Deep Scan** wird die Systemindizierung umgangen und eine direkte, rekursive Dateisystemdurchquerung durchgeführt. Dies ist bei der Suche unbedingt erforderlich: 
- Externe USB-Laufwerke oder SD-Karten, bei denen die Spotlight-Indizierung deaktiviert ist. 
- Remote-Netzwerkdateifreigaben (SMB, SFTP, FTP, WebDAV). 
– Entwickler-Build-Verzeichnisse über `.metadata_never_index` ausgeschlossen. 

---

### 5.3 Suchkriterien für mehrere Filter

Optimieren Sie Suchanfragen mithilfe detaillierter Parameter in den Gruppen **Allgemein** und **Erweiterte Filter**: 

- **Muster für Dateinamen**: 
- *Platzhalter*: Standard-Shell-Platzhalter wie `*.py`, `invoice_2026_*.pdf` oder `test_??.go`. 
- *Teilzeichenfolgen*: Durch Eingabe von `draft` werden alle Dateien oder Ordner gefunden, die „Entwurf“ enthalten. 
- *Reguläre Ausdrücke*: Aktivieren Sie **Regulärer Ausdruck**, um die vollständige Regex-Syntax zu aktivieren (z. B. `^v\d+\.\d+\.(json|xml)$`). 
- **Nach Text suchen (In-File-Suche)**: 
- Sucht nach UTF-8- und ASCII-String-Inhalten in Text-, Quellcode- und Dokumentdateien. 
- Überprüfen Sie **Inhaltssuche mit Berücksichtigung der Groß-/Kleinschreibung** auf genaue Übereinstimmungen mit der Groß-/Kleinschreibung. 
- **Dateigrößenbereich**: 
- Legen Sie **Mindestgröße** und **Maximale Größe** in Kilobyte fest (`KB`). Wenn Sie die maximale Größe auf `0` festlegen, bleiben die Obergrenzen unbegrenzt. 
- **Datumsbereich**: 
- Geben Sie **Geändert innerhalb der letzten N Tage** an (z. B. `7` Tage, um Arbeit aus der letzten Woche zu finden). 

---

### 5.4 Schnelle Überprüfung in Suchergebnissen

Beim Durchsuchen der Suchergebnisse in der Ergebnisliste: 

- **Datei anzeigen (`F3`)**: Öffnet sofort das hervorgehobene Suchergebnis im Universal Lister. 
- **Datei bearbeiten (`F4`)**: Öffnet die Datei direkt im integrierten Texteditor. 
- **Gehe zu Datei (`Enter` / `Go to File`)**: Schließt den Suchdialog, navigiert im Hauptfenster zum übergeordneten Verzeichnis der Datei und platziert den Cursor direkt auf der Datei. 

---

### 5.5 Die Macht von „Feed to Listbox“

Die transformativste Funktion herkömmlicher Dateimanager ist **Feed to Listbox**: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ SEARCH RESULTS (Flat Virtual Panel Tab)             OPPOSING PANEL (Destination)       │
│ [Search: *.log modified < 30 days]                 /Volumes/ArchiveStorage/Logs        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Folder  │   │  Name                        Size   │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ app_server.log            14 MB   /var/log│ C │  ▸ archive_2025             <DIR>   │
│  ✔ auth_audit.log             2 MB   /etc/sec│ O │                                     │
│  ✔ worker_3.log              88 KB   /opt/app│ P │                                     │
│  ● access.log               512 KB   /var/log│ Y │                                     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [3 items selected] ➔ Press F5 to copy all matching files into destination folder!     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

1. Sobald im Suchdialog passende Dateien gefunden wurden, klicken Sie auf die Schaltfläche **Feed to listbox**. 
2. ATBCmder schließt den Dialog und öffnet eine neue **virtuelle Suchergebnisse-Registerkarte** im aktiven Bereich. 
3. Anstatt zu jedem Ordner einzeln zu navigieren, werden alle übereinstimmenden Dateien aus unterschiedlichen Verzeichnistiefen in einer einzigen, flachen Tabelle angezeigt. 
4. **Eine beliebige Commander-Aktion ausführen**: 
- Wählen Sie alle oder bestimmte Elemente aus (`Space`, `+`, `Cmd+A`). 
- **Kopieren (`F5`)** oder **Verschieben (`F6`)** übereinstimmende Dateien über verschiedene Ordner hinweg in einen einzigen Zielordner im gegenüberliegenden Bereich. 
- **Batch Multi-Rename (`Ctrl+M`)** alle passenden Suchergebnisse gleichzeitig. 
- **Löschen Sie (`F8` oder `Alt+Delete`)** unerwünschte temporäre Dateien in der gesamten Projekthierarchie auf einmal sicher. 

---

## 6. Spotlight-Integration und semantisches Befehlssystem (`/` & `Ctrl+Shift+F`)

Moderne Arbeitsabläufe erfordern agile Abfragen über starre Filterdialoge hinaus. ATBCmder integriert die macOS Spotlight-Indizierung direkt mit einem **Semantischen Befehlssystem in natürlicher Sprache**, auf das über die eingebettete Befehlsleiste am unteren Rand des Hauptfensters zugegriffen werden kann. 

![Semantic Command Bar](images/semantic_command.png) 
*Abbildung 5.4: Die semantische Befehlsleiste analysiert eine Abfrage in natürlicher Sprache mit Live-Autovervollständigungsvorlagen.* 

![Semantic Search](images/semantic_search_bar.png) 
*Abbildung 5.5: Ergebnisse der semantischen Suche werden direkt im aktiven Bereich angezeigt.*

### 6.1 Semantische Befehle aktivieren

- **Drücken Sie `/`**: Drücken Sie im aktiven Dateifenster einfach die Schrägstrichtaste (`/`). ATBCmder fokussiert sofort die untere Befehlsbearbeitungsleiste und füllt sie vorab mit `/` aus. 
- **Spotlight-Suchverknüpfung**: Drücken Sie **`Ctrl+Shift+F`** (`⌃⇧F`) oder `Cmd+Shift+F`, um die semantische Filterschnittstelle zu öffnen. 
- **Verwerfen**: Drücken Sie `Escape`, um den Filter zu löschen und die Standardverzeichnisliste wiederherzustellen. 

---

### 6.2 Bereiche: Lokal (`/`) vs. Global (`//`)

ATBCmder unterscheidet zwischen Filterung auf Ordnerebene und systemweiter Erkennung mithilfe von Präfixkonventionen:

#### 1. Lokaler Verzeichnisbereich (`/<query>`)

Abfragen, die mit einem einzelnen Schrägstrich beginnen, beziehen sich ausschließlich auf das im aktiven Bereich geöffnete Verzeichnis (und seine Unterordner, wenn rekursive Optionen angegeben sind): 

- `/larger than 10MB`: Zeigt nur Dateien im aktuellen Ordner an, die größer als 10 Megabyte sind. 
- `/> 50MB`: Numerische Abkürzung für Größenfilterung. 
- `/today modified pdf`: Filter für PDF-Dokumente, die innerhalb der letzten 24 Stunden geändert wurden. 
- `/images`: Zeigt nur Raster- und Vektorbildformate an. 
- `/source code`: Zeigt Python, C++, Rust, Go, JavaScript und andere Quelldateien an. 
- `/contains "API_KEY"`: Filter für Textdateien, die die Zeichenfolge „API_KEY“ enthalten. 
- `/hide *.log`: Versteckt Protokolldateien vor der aktiven Anzeige.

#### 2. Globaler Systemumfang (`//<query>`)

Abfragen, die mit einem doppelten Schrägstrich beginnen, fragen über Spotlight das gesamte macOS-Systemvolume ab: 

- `//today modified pdf`: Findet alle heute geänderten PDF-Dokumente auf Ihrem gesamten Mac. 
- `//larger than 1GB dmg`: Findet alle Disk-Image-Installationsprogramme, die größer als 1 GB sind. 
- `//code contains "OAuth2Handler"`: Findet systemweit alle Quelldateien, die „OAuth2Handler“ enthalten. 

---

### 6.3 KI-unterstützte semantische Abfragen (`?` oder `/?`)

Bei Konfiguration mit einem KI-Anbieter (Google Gemini, OpenAI, Anthropic Claude oder lokales Ollama) in *Einstellungen ➔ Semantischer Filter*: 

– Wenn einer Abfrage `?` oder `/?` vorangestellt wird, wird die Anweisung in natürlicher Sprache durch einen LLM-Parser geleitet. 

- Beispiel: `/? find all final invoices sent to client Acme last quarter over $5000` 
- Die KI übersetzt komplexe menschliche Formulierungen in präzise Spotlight-Metadatenattribute (`kMDItemFSSize`, `kMDItemContentModificationDate`, `kMDItemTextContent`) und zeigt passende Dateien sofort im Panel an. 

---

### 6.4 Autovervollständigung, Katalog (`/help`) und Verlauf (`/history`)

Während Sie in das Bearbeitungsfeld für semantische Befehle Folgendes eingeben: 

- **Interaktives Abschluss-Popup**: Ein Dropdown-Menü (`SemanticCompletionPopup`) zeigt kontextbezogene Vorlagenvorschläge basierend auf dem integrierten Katalog (`semantic-command-templates.xml`) an. Verwenden Sie die Pfeile `Down` und `Up`, um Vorschläge hervorzuheben, und drücken Sie zum Akzeptieren `Tab` oder `Enter`. 
- **Hilfekatalog (`/help`)**: Durch die Eingabe von `/help` wird das **Dialogfeld „Semantische Befehlshilfe“** geöffnet, in dem Dutzende durchsuchbarer Beispiele in verschiedenen Kategorien (Größe, Datum, Dateityp, Inhalt, Tagging) aufgelistet sind. Durch Doppelklicken auf einen beliebigen Eintrag wird dieser in die Befehlszeile eingefügt. 
- **Befehlsverlauf (`/history`)**: Durch die Eingabe von `/history` wird ein chronologisches Protokoll aller zuvor ausgeführten semantischen Befehle mit Ausführungszeitstempeln angezeigt, sodass ein sofortiger Abruf möglich ist. 

---

### 6.5 Sofortige Panel-Aktionsmodifikatoren

Mit der semantischen Befehlsleiste können Sie auch Panelauswahlen und Sortierungen bearbeiten, ohne die Maus zu berühren: 

| Semantischer Befehl | Aktion ausgeführt | 
| :--- | :--- | 
| `/select all visible` | Wählt alle derzeit nach dem Filtern angezeigten Elemente aus. | 
| `/clear selection` | Hebt die Auswahl aller Elemente im Bedienfeld auf. | 
| `/invert selection` | Kehrt den aktuellen Dateiauswahlstatus um. | 
| `/select images` | Fügt alle Bilddateien im Panel zur aktuellen Auswahl hinzu. | 
| `/sort by size descending` | Sortiert die Dateitabelle nach Größe vom größten zum kleinsten. | 
| `/reset sort` | Stellt die standardmäßige alphabetische Namenssortierung wieder her. | 
| `/group by date` | Gruppiert Dateien dynamisch nach Änderungsdatumsklammern. | 
| `/clear filter` | Entfernt alle aktiven semantischen Filter und stellt die vollständige Verzeichnisliste wieder her. | 

---

## 7. Grundlegende Dateidienstprogramme und Datenintegrität

Über die Suche und Batch-Umbenennung hinaus integriert ATBCmder eine Reihe wichtiger Systemdienstprogramme zur Verwaltung großer Dateien, zur Prüfung der Sicherheit und zur Überprüfung der kryptografischen Integrität.

### 7.1 Splitter für große Dateien (`cm_FileSpliter` / `cm_Split` / `Alt+F6`)

Beim Übertragen großer Disk-Images, Videoarchive oder Container virtueller Maschinen über Speichergeräte mit Dateisystemgrößenbeschränkungen (z. B. der 4-GB-Grenze von FAT32) oder E-Mail-Anhangsbeschränkungen unterteilt der **File Splitter** (`SplitWorker`) Dateien in nummerierte aufeinanderfolgende Segmente: 

1. Wählen Sie die große Datei im aktiven Bereich aus. 
2. Wählen Sie **Dateien ➔ Datei teilen...** (oder lösen Sie `cm_Split` aus). 
3. Wählen Sie das Zielverzeichnis (standardmäßig das gegenüberliegende Feld). 
4. Wählen Sie eine voreingestellte Standard-Chunk-Größe aus oder geben Sie eine benutzerdefinierte Byte-Größe ein: 
- **1,44 MB**: Ältere 3,5-Zoll-Diskette. 
- **700 MB**: Standard-CD-R-Kapazität. 
- **4,7 GB**: Single-Layer-DVD-R-Kapazität. 
- **100 MB**: Standard-Upload-Block. 
- **Benutzerdefinierte Größe**: Benutzerdefinierter Byte-, KB-, MB- oder GB-Schwellenwert. 
5. Klicken Sie auf **OK**. ATBCmder teilt die Quelldatei in einen Hintergrund-Worker-Thread auf und erstellt `.001`, `.002`, `.003`... Sequenzdateien. 

---

### 7.2 File Linker & Combiner (`cm_FileLinker` / `cm_Combine` / `Alt+F7`)

Das Zusammenfügen geteilter Dateiblöcke zur ursprünglichen intakten Datei erfolgt nahtlos: 

1. Markieren Sie im Dateifenster den **ersten geteilten Teil** (muss mit der Erweiterung `.001` enden). 
2. Wählen Sie **Dateien ➔ Dateien kombinieren...** (oder lösen Sie `cm_Combine` aus). 
3. ATBCmder erkennt automatisch alle aufeinanderfolgenden Teile (`.001`, `.002`, `.003`... bis zu `.999`). 
4. Wählen Sie den Namen der Ausgabedatei und das Zielverzeichnis aus. 
5. Klicken Sie auf **OK**. Der Hintergrund-Worker (`CombineWorker`) verkettet die Teile nacheinander wieder zu einer exakten Byte-für-Byte-Binärreplik. 

---

### 7.3 Kryptografische Prüfsummen und Verifizierung (`cm_CheckSumCalc`, `cm_CheckSumVerify`)

Für die Datenintegrität ist es von entscheidender Bedeutung, sicherzustellen, dass heruntergeladene Dateien, Disk-Images oder Archivsicherungen nicht beschädigt oder manipuliert wurden. ATBCmder enthält einen integrierten **Prüfsummenrechner und Prüfer** (`ChecksumDialog`). 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Checksum Calculator                                                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Hash Algorithm: [ SHA256           ▾]                                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3a491d90bc1f42013149db82a890471b67823f40d12e8424e6a00a120894fe83  arch_linux.iso       │
│ 8f14e45fceea167a5a36dedd4bea25431846b9a898492efd727402c3ef30b65a  rootfs.tar.gz        │
│ e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  empty_manifest.txt   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Progress: 100%] Hashing completed.                                                   │
│  [Calculate]    [Stop]    [💾 Save to File]                                 [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Berechnen von Hashes (`cm_CheckSumCalc` / `Ctrl+X`)

1. Wählen Sie im Panel eine oder mehrere Dateien aus. 
2. Wählen Sie **Dateien ➔ Prüfsumme berechnen...** (oder drücken Sie `Ctrl+X`). 
3. Wählen Sie Ihren gewünschten Algorithmus aus: **MD5**, **SHA1**, **SHA256** oder **SHA512**. 
4. Klicken Sie auf **Berechnen**. Der Worker streamt Dateien im Hintergrund durch 64-KB-Blöcke, ohne die Schnittstelle zu sperren. 
5. Klicken Sie auf **In Datei speichern**, um die Hashes in eine Standard-Manifestdatei `.sha256` oder `.md5` zu exportieren.

#### Überprüfen von Prüfsummenmanifesten (`cm_CheckSumVerify`)

1. Wählen Sie **Dateien ➔ Prüfsummen überprüfen...**. 
2. Wählen Sie eine vorhandene Prüfsummendatei aus (`.sha256`, `.md5`, `.sha1`, `.sha512` oder `.sfv`). 
3. ATBCmder analysiert das Manifest automatisch, findet entsprechende Dateien im selben Verzeichnis, berechnet Hashes auf der Festplatte neu und präsentiert einen farbcodierten Statusbericht: 
- **`OK`**: Die Datei stimmt perfekt mit der Prüfsumme überein. 
- **`FAILED`**: Datenbeschädigung oder -änderung erkannt! 
- **`MISSING`**: Referenzierte Datei nicht im Verzeichnis gefunden. 

---

### 7.4 Sichere Dateivernichtung/-löschung (`cm_Wipe` / `Alt+Delete` / `⌥⌫`)

Beim standardmäßigen Löschen von Dateien werden lediglich die Verknüpfungen von Verzeichniseinträgen aufgehoben, sodass die Rohdatenblöcke auf der Festplatte intakt bleiben, wo sie von Wiederherstellungsdienstprogrammen extrahiert werden können. Verwenden Sie beim Umgang mit vertraulichen Schlüsseln, Anmeldeinformationen oder proprietärem Quellcode **Sicheres Löschen/Wischen** (`cm_Wipe`): 

1. Wählen Sie die vertraulichen Dateien oder Verzeichnisse aus. 
2. Drücken Sie **`Alt+Delete`** (`⌥⌫`) oder wählen Sie **Datei ➔ Sicheres Löschen (Löschen)...**. 
3. Bestätigen Sie die Sicherheitswarnung. 
4. **Die kryptografische Multi-Pass-Shredding-Sequenz (`wipe_path`)**: 
- **Pass 1**: Überschreibt die gesamte Bytelänge der Datei mit kryptografisch sicheren pseudozufälligen Bytes (`os.urandom`). 
- **Durchlauf 2**: Überschreibt die gesamte Datei mit Null-Null-Bytes (`\x00`). 
- **Durchlauf 3**: Überschreibt mit neuen Zufallsbytes. 
- **Hardware-Synchronisierung**: Ruft `os.fsync()` für den zugrunde liegenden Dateideskriptor auf, um das Betriebssystem und den Speichercontroller-Cache zu zwingen, Daten auf physische Medien zu schreiben. 
- **Truncation & Unlink**: Schneidet die Datei auf 0 Bytes ab, bevor `os.unlink()` aufgerufen wird. 
- **Verzeichnisbereinigung**: Löscht rekursiv alle enthaltenen Dateien, bevor die Verknüpfung mit übergeordneten Verzeichnissen aufgehoben wird. 

---

### 7.5 Eingebettetes Systemterminal (`Ctrl+J` / `⌃J` / `cm_RunTerm`)

Während sich ATBCmder durch grafische Dual-Panel-Workflows auszeichnet, ist für die Kompilierung, Git-Branches oder die Serververwaltung häufig Shell-Zugriff erforderlich: 

- Drücken Sie **`Ctrl+J`** (`⌃J`) oder wählen Sie **Befehle ➔ Terminal ausführen**. 
- ATBCmder öffnet sofort macOS **Terminal.app** (oder Ihren konfigurierten Standard-Terminal-Emulator), wobei sein Arbeitsverzeichnis auf den genauen Pfad initialisiert wird, der im aktiven Bereich geöffnet ist. 
- Kein Eingeben von `cd /Users/...` oder Ziehen von Ordnern in Terminalfenster erforderlich. 

---

## 8. ⚡ Profi-Tipps und detaillierte Automatisierungsworkflows

### 8.1 Rezept: Rekursive Suche ➔ Zu Listbox hinzufügen ➔ Mehrfachumbenennung

**Ziel**: Versionsnummern aus Hunderten von Asset-Dateien entfernen, die über 50 verschachtelte Unterordner verteilt sind. 

1. Öffnen Sie das Projektstammverzeichnis im linken Bereich. 
2. Drücken Sie **`Alt+F7`**, um die Suche zu öffnen. 
3. Geben Sie im Dateinamenmuster Folgendes ein: `*_v[0-9]*.png`. 
4. Klicken Sie auf **Suche starten**. Sobald passende Assets angezeigt werden, klicken Sie auf **Feed to listbox**. 
5. Wählen Sie auf der daraufhin angezeigten Registerkarte „Virtual Panel“ alle Dateien mit **`Cmd+A`** aus. 
6. Drücken Sie **`Ctrl+M`**, um das Multi-Rename-Tool zu starten. 
7. Geben Sie unter **Suchen** Folgendes ein: `_v\d+`. Aktivieren Sie **Reguläre Ausdrücke verwenden (Regex)**. 
8. Lassen Sie **Ersetzen durch** leer. 
9. Überprüfen Sie, ob in der Live-Vorschautabelle saubere Dateinamen ohne Versionssuffixe angezeigt werden. 
10. Klicken Sie auf **Umbenennen starten**. ATBCmder benennt jede Datei in allen 50 Unterordnern sofort um! 

---

### 8.2 Rezept: Sichere Cloud- und NAS-Backup-Spiegelung mit asymmetrischer Synchronisierung

**Ziel**: Behalten Sie eine identische Offsite-Spiegelung Ihrer Dokumente auf einem externen SSD- oder SMB-NAS-Laufwerk bei, ohne dass sich doppelte Dateien ansammeln. 

1. Öffnen Sie lokal `~/Documents` im linken Bereich. 
2. Öffnen Sie `/Volumes/BackupSSD/Documents` im rechten Bereich. 
3. Drücken Sie **`Shift+F12`** (`cm_SyncDirs`). 
4. Stellen Sie sicher, dass in den Einstellungen **Unterverzeichnisse vergleichen** aktiviert ist. 
5. Aktivieren Sie **Asymmetrisch (Ziel löschen, wenn es in der Quelle fehlt)**. 
6. Klicken Sie auf **Vergleichen**. 
7. Überprüfen Sie die Liste: 
- Blaue/grüne Pfeile (`->`) zeigen Dateien an, die in die Sicherung kopiert werden. 
- Rote Löschungen (`<-`) weisen auf veraltete Dateien auf der Sicherungsfestplatte hin, die Sie inzwischen lokal gelöscht haben. 
8. Klicken Sie auf **Synchronisieren**. Ihr Sicherungslaufwerk ist jetzt eine Spiegelung Ihres lokalen Ordners. 

---

### 8.3 Rezept: Forensischer Hash manifestiert sich vor der Langzeitarchivspeicherung

**Ziel**: Berechnen und speichern Sie kryptografische Prüfsummen für ein Multi-Terabyte-Projekt, bevor Sie es auf Cold-Tape- oder Cloud-Glacier-Speicher verschieben. 

1. Navigieren Sie zu dem Verzeichnis, das Ihre Projektergebnisse enthält. 
2. Wählen Sie alle Elemente aus (`Cmd+A`) und drücken Sie **`Ctrl+X`** (`cm_CheckSumCalc`). 
3. Stellen Sie den Algorithmus auf **SHA256** ein. 
4. Klicken Sie auf **Berechnen**. Der Streaming-Hash-Worker verarbeitet die Dateien im Hintergrund. 
5. Klicken Sie auf **In Datei speichern** und nennen Sie sie `MANIFEST-SHA256.txt`. 
6. Wenn Sie die Dateien Jahre später abrufen, wählen Sie einfach `MANIFEST-SHA256.txt` aus und führen Sie **Prüfsummen überprüfen** aus, um sicherzustellen, dass keine Bitfäule oder stille Beschädigung vorliegt. 

---

### 8.4 Rezept: Kombinieren der semantischen Filterung in natürlicher Sprache mit der flachen Zweigansicht (`Cmd+B`)

**Ziel**: Alle Mediendateien in einer komplexen, tiefen Verzeichnisstruktur finden und organisieren, ohne Suchdialoge öffnen zu müssen. 

1. Markieren Sie Ihren Projektordner der obersten Ebene und drücken Sie **`Cmd+B`** (`cm_FlatView`), um alle Unterordnerinhalte in einer einzigen Liste zusammenzufassen. 
2. Drücken Sie **`/`**, um die semantische Befehlsleiste zu fokussieren. 
3. Geben Sie ein: `/images larger than 5MB`. 
4. Die reduzierte Liste isoliert hochauflösende Bilder sofort in jedem verschachtelten Verzeichnis. 
5. Drücken Sie `/select all visible` und dann **`F5`**, um sie alle in ein organisiertes Zielverzeichnis im gegenüberliegenden Bereich zu kopieren. 
6. Drücken Sie erneut `Cmd+B`, um das normale Durchsuchen der hierarchischen Baumstruktur wiederherzustellen. 

---

## 9. Sicherheits-, Leistungs- und Systemwarnungen

> [!ACHTUNG] 
> **Unumkehrbarkeit der asymmetrischen Verzeichnissynchronisierung** 
> Das Aktivieren der Option **Asymmetrisch** in der Verzeichnissynchronisierung (`Shift+F12`) führt dazu, dass Dateien im Zielverzeichnis, die in der Quelle nicht vorhanden sind, **dauerhaft gelöscht** werden. Führen Sie immer eine visuelle Prüfung der Vergleichsvorschautabelle durch, bevor Sie auf **Synchronisieren** klicken. 

> [!WARNUNG] 
> **RegEx-Ersetzungen mit mehreren Umbenennungen** 
> Stellen Sie beim Ersetzen regulärer Ausdrücke mit Rückverweisen (`$1`, `$2`) sicher, dass Ihre Erfassungsgruppennummern mit den Klammern in Ihrem Muster übereinstimmen. Testen Sie Ihr Muster anhand der Tabellenzeilen der Live-Vorschau, bevor Sie auf **Umbenennen starten** klicken. Wenn doppelte Zielnamen auftreten, blockiert ATBCmder die Ausführung, um Sie vor Datenverlust zu schützen. 

> [!IMPORTANT] 
> **Einschränkungen bei der Vernichtung von Solid-State-Laufwerken (SSD)** 
> Das Secure Wipe-Dienstprogramm (`cm_Wipe` / `Alt+Delete`) überschreibt Dateidaten mit mehreren Durchgängen von Zufalls- und Nullbytes, gefolgt von einem `fsync`-Aufruf. Moderne Solid-State-Laufwerke (SSDs) nutzen jedoch Wear-Leveling-Algorithmen und Over-Provisioning auf Controller-Ebene, die Schreibvorgänge möglicherweise auf alternative Flash-Blöcke umleiten. Für eine hochsichere SSD-Entsorgung kombinieren Sie die Dateivernichtung mit der macOS FileVault-Festplattenverschlüsselung. 

> [!NOTE] 
> **Spotlight-Verfügbarkeit auf Netzwerk- und FAT-Volumes** 
> Die schnelle Spotlight-Suche (`Ctrl+Shift+F`) basiert auf macOS-Metadatenindizes, die standardmäßig auf internen APFS-Laufwerken aktiv sind. Remote-Netzwerk-Mounts (SMB, SFTP) und externe exFAT-Laufwerke werden möglicherweise nicht von Spotlight indiziert. Wenn eine Spotlight-Abfrage auf einem externen Laufwerk keine Ergebnisse zurückgibt, verwenden Sie **Deep Scan** (`Alt+F7`) oder aktivieren Sie die rekursive Verzeichnissuche. 

> [!TIP] 
> **Kompatibilität mit Apple-Funktionstasten (`Fn`)** 
> Auf Apple Magic Keyboards und MacBooks sind die Funktionstasten (`F1`-`F12`) standardmäßig auf Hardware-Aktionen (Helligkeit, Lautstärke) eingestellt. Um `Shift+F12` oder `Alt+F7` zu drücken, halten Sie die Taste **`Fn`** gedrückt: `Fn+Shift+F12`, `Fn+Alt+F7`. Alternativ aktivieren Sie **„F1-, F2-usw.-Tasten als Standardfunktionstasten verwenden“** in macOS *Systemeinstellungen ➔ Tastatur ➔ Tastaturkürzel ➔ Funktionstasten*. 

---

## 10. Referenztabelle für Master-Dual-Matrix-Tastaturen

| Funktionsbereich | Aktionsbeschreibung | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | 
| :--- | :--- | :--- | :--- | :--- | 
| **Mehrfachumbenennung** | Batch-Multi-Rename-Tool starten | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | 
| **Mehrfachumbenennung** | Ausführen / Umbenennen starten | `Enter` / `⏎` | `Enter` | — | 
| **Mehrfachumbenennung** | Tool abbrechen/schließen | `Esc` | `Esc` | — | 
| **Dateiunterschied** | Ausgewählte Dateien/Fenster vergleichen | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | 
| **Dateiunterschied** | Zum nächsten Unterschied springen | `Alt+Down` / `⌥↓` | `Ctrl+Down` | — | 
| **Dateiunterschied** | Zum vorherigen Unterschied springen | `Alt+Up` / `⌥↑` | `Ctrl+Up` | — | 
| **Dateiunterschied** | Hunk von links nach rechts kopieren | `Alt+Right` / `⌥→` / `Alt+P` | `Ctrl+Alt+Right` | — | 
| **Dateiunterschied** | Hunk von rechts nach links kopieren | `Alt+Left` / `⌥←` / `Alt+O` | `Ctrl+Alt+Left` | — | 
| **Dateiunterschied** | Änderungen im fokussierten Editor speichern | `Cmd+S` / `⌘S` | `Ctrl+S` | — | 
| **Dateiunterschied** | Differenzen neu berechnen | `F5` / `Fn+F5` | `Ctrl+R` | — | 
| **Verzeichnissynchronisierung**| Öffnen Sie Verzeichnisse synchronisieren | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | 
| **Verzeichnissynchronisierung**| Verzeichnisvergleich starten | `Alt+C` / `⌥C` | `Enter` | — | 
| **Verzeichnissynchronisierung**| Vergleich/Synchronisierung abbrechen | Klicken Sie auf `Stop` | `Esc` | — | 
| **Dateisuche** | Erweitertes Suchdialogfeld öffnen | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | 
| **Dateisuche** | Ergebnis im Universal Lister anzeigen | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Dateisuche** | Ergebnis im Texteditor bearbeiten | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Dateisuche** | Gehen Sie im aktiven Bereich zu Datei | `Enter` / `⏎` | `Enter` | — | 
| **Dateisuche** | Ergebnisse an virtuelles Panel weiterleiten | Klicken Sie auf `Feed to listbox` | Klicken Sie auf `Feed to listbox` | — *(Dialogaktion)* | 
| **Spotlight & NLP**| Spotlight-Schnellsuche | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Befehlsmenü)* | 
| **Spotlight & NLP**| Semantische Befehlsleiste aktivieren | `/` | `/` | `cm_VisSemanticCommand` | 
| **Spotlight & NLP**| Semantischen Filter verwerfen | `Esc` | `Esc` | — | 
| **Datei-Dienstprogramme**| Datei in Stücke aufteilen | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Datei-Dienstprogramme**| Kombinieren Sie nummerierte geteilte Teile | Menü: Dateien ➔ Dateien kombinieren | — | `cm_FileLinker` / `cm_Combine` | 
| **Datei-Dienstprogramme**| Prüfsumme (Hash) berechnen | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | 
| **Datei-Dienstprogramme**| Prüfsummen-Manifestdatei überprüfen | Extras-Menü | Extras-Menü | `cm_CheckSumVerify` / `cm_VerifyChecksum` | 
| **Datei-Dienstprogramme**| Sicheres Multi-Pass Wipe (Shred)| `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | 
| **Datei-Dienstprogramme**| Öffnen Sie das native macOS-Terminal | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` |

--- 

<div align="center"> 
<p>Bereit, eine Verbindung zu Remote-Servern herzustellen und virtuelle Archive zu erkunden?</p> 
<p><strong><a href="network_and_vfs.md">Fahren Sie mit Kapitel 6 fort: Virtuelle Dateisysteme und Netzwerk &rarr;</a></strong></p> 
</div>