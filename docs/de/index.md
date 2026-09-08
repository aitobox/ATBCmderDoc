# Willkommen bei ATBCmder

[![macOS](https://img.shields.io/badge/platform-macOS%2012%2B-blue.svg)](download.md) 
[![Architecture](https://img.shields.io/badge/arch-Apple%20Silicon%20(ARM64)-orange.svg)](download.md) 
[![Release](https://img.shields.io/badge/release-latest-green.svg)](download.md) 
[![Privacy](https://img.shields.io/badge/telemetry-zero%20tracking-brightgreen.svg)](privacy_policy.md) 

Willkommen im offiziellen Dokumentationsportal für **ATBCmder** – dem schnellen, tastaturgesteuerten Dual-Panel-Dateimanager, der speziell für macOS entwickelt wurde. ATBCmder vereint die Geschwindigkeits- und Befehlstradition traditioneller Dateimanager (Total Commander, Double Commander, Norton Commander) mit modernem macOS-Design, nativer Systemintegration und fortschrittlichen Power-Tools. 

---

## Die Dual-Panel-Philosophie

Herkömmliche Einzelfenster-Desktop-Dateimanager wie macOS Finder zwingen Benutzer dazu, sich in einem endlosen Kreislauf überlappender Fenster zu öffnen, den Überblick über Quell- und Zielordner zu verlieren und das Risiko einzugehen, versehentlich in falsche Unterordner zu gelangen. 

```
Herkömmliche Dateiverwaltung (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Ordner A (Wo war ich?) │ ──?  │ Ordner B (Welcher?)    │  → Fensterchaos, Fokusverlust
└────────────────────────┘      └────────────────────────┘    und falsches Ablegen

Der ATBCmder-Weg (Orthodoxes Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│     AKTIVES PANEL (Quelle)    │    INAKTIVES PANEL (Ziel)     │
│  Dateien warten auf Aktion    │  Klares, verlässliches Ziel   │
│  [ Kopieren / Bewegen / Sync  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘
```
 

ATBCmder löst dieses Problem durch das **Quelle-Ziel-Dual-Panel-Paradigma**: 

- **Klare Orientierung auf einen Blick**: Zwei unabhängige Verzeichnisansichten sind jederzeit nebeneinander sichtbar. 
- **Vorhersehbare Richtungsoperationen**: Wenn Sie Kopieren (`F5`) oder Verschieben (`F6`) auslösen, überträgt ATBCmder automatisch Elemente vom **Aktiven Bereich** (wo sich Ihr Cursor befindet) in den **Inaktiven Bereich** (die entgegengesetzte Ansicht). Kein Ziehen, kein Raten, kein Suchen nach versteckten Zielfenstern. 
- **Flüssiger Tastatur-Flow**: Lassen Sie Ihre Hände auf der Tastatur. Springen Sie durch Verzeichnisse, wählen Sie Dateien mit Platzhaltern aus, prüfen Sie Archive und führen Sie Stapeltransformationen in Millisekunden aus. 
- **Keine Unordnung im Finder-Fenster**: Ein Fenster verwaltet alles – lokale Volumes, Netzwerkserver (FTP, SFTP, SMB, WebDAV), Archivinhalte (`.zip`, `.7z`, `.tar`) und Hintergrundübertragungswarteschlangen. 

---

## Benutzeroberfläche und Funktionsbereiche im Überblick

ATBCmder vereint maximale Produktivität und Kontrolle in einem übersichtlichen, intuitiven Layout, das Ihnen einen sofortigen Überblick über die Situation beider Verzeichnisse gibt. 

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Menüleiste: Datei   Markieren   Befehle   Ansicht   Konfiguration   Hilfe            │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Hauptsymbolleiste: [🔍 Suchen]  [⚡ Warteschlange]  [⚙️ Einstellungen]  [📁 Laufwerke] │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Pfadzeile: 🏠 > Users > brain > work    │ [3] Pfadzeile: 💾 > Volumes > Backup       │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Tab-Leiste: [Projekt Alpha ✕] [Docs] [+]│ [4] Tab-Leiste: [2026 Archiv ✕] [+]        │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Linkes Panel (Aktiv / Quelle)    │ [6]  │ [5] Rechtes Panel (Inaktiv / Ziel)         │
│ 📁 .. [Übergeordneter Ordner]        │  M   │ 📁 .. [Übergeordneter Ordner]              │
│ 📁 assets                            │  I   │ 📁 archive_2025                            │
│ 📁 src                               │  T   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  T   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  E   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  L   │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Statusleiste: 6 Objekte | 2 gewählt (10.5 KB)│ Speicher: 142.6 GB frei / 494.3 GB     │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Referenz zu UI-Wahrzeichen

1. **Menüleiste und native macOS-Integration (`[1]`)**: Vollständige Unterstützung des macOS-Anwendungsmenüs, Standardverknüpfungen (`⌘,`, `⌘Q`, `⌘W`) und vollständiger Menüzugriff auf alle internen Commander-Befehle (`cm_*`). 
2. **Hauptsymbolleiste und Schnellstarter (`[2]`)**: Sofortiger Ein-Klick-Zugriff auf Suche (`Alt+F7`), Hintergrundübertragungswarteschlange (`cm_OperationsPanel`), Einstellungen (`Cmd+,`) und Laufwerksauswahl. 
3. **Interaktive Breadcrumb-Pfadleiste (`[3]`)**: Klicken Sie auf ein beliebiges Verzeichnissegment im Pfad, um direkt in der Hierarchie nach oben zu springen. Klicken Sie auf den Segment-Dropdown-Pfeil, um Unterverzeichnisse zu durchsuchen. 
4. **Ordnerregisterkarten und Arbeitsbereiche (`[4]`)**: Öffnen Sie unbegrenzt viele Registerkarten in jedem Bereich (`Cmd+T`), schließen Sie Registerkarten (`Cmd+W`), sperren Sie bevorzugte Speicherorte und speichern Sie gesamte Arbeitsbereiche mit Registerkarten mit zwei Bedienfeldern (`cm_SaveFavoriteTabs`). 
5. **Dual File Panels (`[5]`)**: Unabhängige Dateitabellen. Das aktive Bedienfeld zeigt einen deutlichen Akzentrahmen und einen fokussierten Cursor an. Wechseln Sie den Fokus sofort mit `Tab`. 
6. **Mittlere Symbolleiste und ziehbarer Splitter (`[6]`)**: Ein vertikaler Schnellaktionsstreifen, der direkt auf dem Panel-Trenner platziert wird. Bietet Ein-Klick-Auslöser für Anzeigen (`F3`), Bearbeiten (`F4`), Kopieren (`F5`), Verschieben (`F6`), Neuer Ordner (`F7`), Löschen (`F8`), Löschen und Austauschen von Bedienfeldern (`cm_Exchange`). Ziehen Sie den Splitter nach links oder rechts, um die Größe der Panels zu ändern. 
7. **Statusleiste und Laufwerksspeicheranzeige (`[7]`)**: Zeigt Live-Dateianzahlen, ausgewählte Elementstatistiken, aggregierte Bytegrößen und eine Anzeige der aktiven Volume-Speicherkapazität mit Berechnung des freien Speicherplatzes an. 

---

## Interface-Showcase

Entdecken Sie die Fähigkeiten von ATBCmder anhand der wichtigsten Funktionshighlights: 

| Dual-Panels und Baumansicht | Mittlere Schnellaktionssymbolleiste | 
| :---: | :---: | 
| ![Tree View and Thumbnail Display](images/treeview+thumbview.png) | ![Middle Toolbar](images/middle_toolbar.png) | 
| *Dual-Panel-Layout mit Verzeichnisbaum und Miniaturvorschau.* | *Schnellaktionsleiste: Anzeigen, Bearbeiten, Kopieren, Verschieben, MkDir, Löschen, Löschen.* | 

| Befehle in natürlicher Sprache | Rekursive flache Zweigansicht | 
| :---: | :---: | 
| ![Natural Language File Search](images/semantic_command.png) | ![Flat View of Nested Directories](images/branch_view.png) | 
| *Sofortige Suche mit macOS Spotlight und semantischer Abfrageanalyse.* | *Zweigansicht (`Cmd+B`) zeigt verschachtelte Inhalte in einer einzelnen flachen Liste an.* | 

| Netzwerk- und Remote-VFS | VFS archivieren (keine Extraktion erforderlich) | 
| :---: | :---: | 
| ![Network VFS](images/network_vfs.png) | ![Archive VFS](images/archive_vfs.png) | 
| *Stellen Sie eine Verbindung zu FTP-, SFTP-, WebDAV- und SMB/Samba-Netzwerkfreigaben her.* | *Durchsuchen und bearbeiten Sie ZIP-, TAR- und 7z-Archive wie Standardordner.* | 

---

## Wählen Sie Ihren Weg

Unabhängig davon, ob Sie noch nie zuvor ein Dual-Panel-Tool verwendet haben oder Total Commander zwei Jahrzehnte lang verwendet haben, bietet ATBCmder einen optimierten Weg nach vorne:

### 🟢 Track A: Neu bei Dual-Panel-Dateimanagern?

*Willkommen bei einer schnelleren und saubereren Möglichkeit, Dateien unter macOS zu verwalten.* 

Wenn Sie Finder oder Standard-Desktop-Betriebssysteme verwenden, könnten herkömmliche Dateimanager auf den ersten Blick ungewohnt aussehen. Sobald Sie die Kernmuster kennengelernt haben, werden Sie nie wieder Dateien über verstreute Fenster ziehen wollen: 

1. **Beginnen Sie mit den Kernkonzepten**: Lesen Sie [Kapitel 1: Grundlagen und macOS-Setup](getting_started.md), um aktive vs. inaktive Bedienfelder, die mittlere Symbolleiste und das Gewähren von macOS-Festplattenberechtigungen zu verstehen. 
2. **Tägliche Vorgänge meistern**: Erfahren Sie in [Kapitel 3: Tägliche Dateivorgänge und Warteschlange] (file_operations.md), wie Sie kopieren, verschieben, umbenennen und löschen, ohne die Maus zu berühren. 
3. **Alles sofort in der Vorschau anzeigen**: Erfahren Sie in [Kapitel 4: Universal Lister & Editors](viewers_and_editors.md), wie Sie mit einem einzigen Tastendruck eine Vorschau von Bildern anzeigen, Audiodateien anhören, Code lesen und PDFs überprüfen können. 
4. **Befolgen Sie praktische Anleitungen**: Sehen Sie sich praktische Alltagsabläufe und häufige Fragen in [Kapitel 9: Rezepte aus der Praxis und Fehlerbehebung](faq_howtos.md) an. 

---

### ⚡ Track B: Migration von Total Commander / Double Commander?

*Alle Leistungs- und Tastaturreflexe, die Sie kennen, nativ für macOS entwickelt.* 

ATBCmder wurde entwickelt, um das authentische Commander-Erlebnis auf modernes macOS zu bringen, ohne umständliches X11, Wine Wrapper oder nicht gewartete Legacy-Ports auszuführen: 

1. **Beherrschen Sie die Dual-Matrix-Tastenkombinationen**: Sehen Sie sich unsere vollständige Parallel-Tastenkombinationsmatrix (`macOS Cmd` vs. `Commander Fn`) in [Kapitel 8: Master-Tastenkombinationen] (keyboard_shortcuts.md) an. 
2. **Erweiterte Elektrowerkzeuge nutzen**: Verwenden Sie das Batch Multi-Rename Tool (`Ctrl+M`), den Side-by-Side-Dateivergleich (`Meta+Shift+F12`), die Ordnersynchronisierung (`Shift+F12`) und die erweiterte Suche in [Kapitel 5: Elektrowerkzeuge und Automatisierung] (power_tools.md). 
3. **Verbindung zu Remote- und virtuellen Systemen herstellen**: Durchsuchen und bearbeiten Sie direkt in den Archiven `.zip` und `.tar` mit Live-Neuverpackung oder verwalten Sie Remote-Server über SFTP, SMB und WebDAV in [Kapitel 6: Virtuelle Dateisysteme und Netzwerk] (network_and_vfs.md). 
4. **Anpassen und Portieren Ihres Setups**: Binden Sie Befehle neu, konfigurieren Sie das automatische Aktualisierungsverhalten und exportieren Sie Ihre Konfigurations-XML in [Kapitel 7: Einstellungen und Anpassung](preferences_and_customization.md). 

---

## Hauptinhaltsverzeichnis

Entdecken Sie die komplette ATBCmder-Dokumentationssuite:

### 🚀 [Kapitel 1: Grundlagen und macOS-Setup](getting_started.md)

Verstehen Sie die Dual-Panel-Philosophie, erkunden Sie die Anatomie der Benutzeroberfläche, konfigurieren Sie macOS App Sandbox-Berechtigungen über den Onboarding-Assistenten (`cm_GrantFilesystemAccess`), legen Sie Überschreibungen der Systemsprache für mehr als 30 Gebietsschemas fest und passen Sie Hell/Dunkel-Designs an.

### 🧭 [Kapitel 2: Navigation und Ordnerregisterkarten](navigation_and_tabs.md)

Navigieren Sie mühelos durch Verzeichnisbäume mit interaktiven Breadcrumbs, Tastatursprüngen (`Ctrl+\`, `Backspace`), Organisation mit mehreren Registerkarten (`Cmd+T`, `Cmd+W`), Favoriten-Arbeitsbereichssätzen mit zwei Bedienfeldern (`cm_SaveFavoriteTabs`) und Verzeichnis-Hotlist-Lesezeichen (`Ctrl+D`) und flexible Ansichtsmodi (Kurzansicht, vollständige Spalten, Miniaturansichten, Baumansicht und flache Zweigansicht `Cmd+B`).

### 📁 [Kapitel 3: Tägliche Dateivorgänge und Warteschlange](file_operations.md)

Führen Sie schnelle und zuverlässige Dateivorgänge aus: Kopieren (`F5`), Verschieben (`F6`), Neuer Ordner (`F7`), In den Papierkorb löschen (`F8`) und schnelles Inline-Umbenennen (`F2`). Master-Platzhalter- und Attributauswahl, Drag-and-Drop-Interoperabilität, Kollisionskonfliktlösung, UNIX-Oktalberechtigungen (`Alt+Enter`) und asynchrone Übertragungsüberwachung über die Hintergrundoperationswarteschlange (`cm_OperationsPanel`).

### 👁️ [Kapitel 4: Universeller Lister und integrierte Editoren](viewers_and_editors.md)

Überprüfen Sie Dateien, ohne umfangreiche Software von Drittanbietern zu starten. Verwenden Sie Quick View (`Ctrl+Q` / `Cmd+Q`) für Live-Vorschauen im Seitenbereich und Universal Lister (`F3`) für Word-Dokumente, Tabellenkalkulationen, SQLite-Datenbanken, Jupyter-Notebooks, EPUBs, syntaxhervorgehobenen Code, rohe Hex-Byte-Inspektion (`2`), Bildanmerkungen und Wasserzeichen (`F4`), PDF-Dokumentenleser und integrierte Audio-/Video-Mediaplayer mit Hintergrund-Audiowiedergabe. Bearbeiten Sie Dateien direkt mit dem integrierten Texteditor (`F4`).

### ⚡ [Kapitel 5: Elektrowerkzeuge und Automatisierung](power_tools.md)

Automatisieren Sie komplexe Herausforderungen bei der Dateiverwaltung: Batch-Mehrfachumbenennung (`Ctrl+M`) mit Token und RegEx-Ersetzung, paralleler visueller Dateivergleich (`Meta+Shift+F12`), bidirektionale Verzeichnissynchronisierung (`Shift+F12`), erweiterte Multifiltersuche (`Alt+F7`) mit „Feed to Listbox“, Spotlight und natürlicher Sprache Semantische Befehle (`/`), File Splitter & Linker, Prüfsummenüberprüfung (MD5, SHA-256, CRC32), Secure Multi-Pass Wipe (`cm_Wipe`) und eingebettetes Terminal (`Ctrl+J`).

### 🌐 [Kapitel 6: Virtuelle Dateisysteme und Netzwerk](network_and_vfs.md)

Behandeln Sie Remote-Server und komprimierte Archive wie gewöhnliche lokale Ordner mit einheitlichen `vfs://`-URIs. Navigieren Sie in den Archiven `.zip`, `.tar` und `.7z` ohne Dekomprimierung, bearbeiten Sie Dateien direkt mit automatisiertem Live-Neupacken, erstellen Sie verschlüsselte Archive (`Alt+F5`) und verwalten Sie dauerhafte Verbindungen über FTP, SFTP (SSH-Schlüssel), WebDAV und SMB/Samba-Netzwerkfreigaben.

### ⚙️ [Kapitel 7: Einstellungen und Anpassung](preferences_and_customization.md)

Konfigurieren Sie ATBCmder so, dass er genau zu Ihrem Arbeitsstil passt. Suchen und binden Sie primäre/sekundäre Hotkeys mit Echtzeit-Konfliktwarnungen, passen Sie Dateitabellenspalten und automatische Anpassungsregeln an, passen Sie die Empfindlichkeit der automatischen Aktualisierung des Datei-Watchers an, definieren Sie benutzerdefinierte Dateierweiterungszuordnungen und exportieren/importieren Sie tragbare Konfigurationsprofile (`cm_ExportConfiguration`).

### ⌨️ [Kapitel 8: Master-Tastaturkürzel](keyboard_shortcuts.md)

Umfassendes Dual-Matrix-Shortcut-Referenzhandbuch, das native macOS-Shortcuts (`Cmd`-Modifikatoren) mit klassischen Commander-Funktionstasten (`F1`-`F12`) vergleicht. Enthält spezielle Anweisungen für das Modifikatorverhalten der Apple-Tastatur `Fn` und die macOS-Konfiguration der „Standardfunktionstasten“.

### ❓ [Kapitel 9: Rezepte aus der Praxis und Fehlerbehebung](faq_howtos.md)

Praktische Schritt-für-Schritt-Anleitungen für gängige Aufgaben aus der Praxis: Synchronisieren von Verzeichnissicherungen, Batch-Umbenennen von Kamerafotobibliotheken mit Zeitstempeln, Mounten von Netzwerk-NAS-Laufwerken, Aktualisieren von Konfigurationsdateien in Remote-Archiven und Diagnostizieren von macOS-Sandbox-Berechtigungsfehlern oder Problemen mit der automatischen Aktualisierung.

### 📥 [Kapitel 10: Download und Installation](download.md)

Installationsoptionen für macOS 12.0+ Monterey über Sequoia. Laden Sie es direkt aus dem Mac App Store herunter oder holen Sie sich eigenständige DMG-Installationspakete, die nativ für Apple Silicon (M1/M2/M3/M4, ARM64-Architektur) entwickelt wurden. *Hinweis: Intel (x86_64) Macs werden derzeit nicht unterstützt.* 

---

### 🔒 [Anhang: Datenschutzrichtlinie und Datensicherheit](privacy_policy.md)

Unser grundlegendes Versprechen zum Schutz der Privatsphäre der Benutzer: ATBCmder umfasst keine Nachverfolgung, keine Telemetrieprotokollierung und keine Hintergrundanalyse. Alle Dateivorgänge, Netzwerkanmeldeinformationen und Suchindizes bleiben ausschließlich lokal auf Ihrem Mac. 

--- 

<div align="center"> 
<p>Bereit, loszulegen?</p> 
<p><strong><a href="getting_started.md">Fahren Sie mit Kapitel 1 fort: Grundlagen und macOS-Einrichtung &rarr;</a></strong></p> 
</div>