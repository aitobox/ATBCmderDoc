# Kapitel 6: Virtuelle Dateisysteme & Netzwerk

Modernes Dateimanagement endet selten an der Grenze einer einzelnen physischen Festplatte. Softwareentwickler verwalten Remote-Staging-Umgebungen über SFTP; Systemadministratoren verwalten Unternehmensdateifreigaben über SMB/CIFS; Inhaltsersteller greifen über WebDAV auf Cloud-Speicher und Medienserver zu; und Power-User prüfen, bearbeiten und verpacken routinemäßig komprimierte Archive im Gigabyte-Bereich. 

Herkömmliche Desktop-Umgebungen zwingen Benutzer dazu, mit getrennten Anwendungen zu jonglieren: ein eigenständiges Archivierungsdienstprogramm zum Entpacken und erneuten Komprimieren von ZIP-Archiven, ein externer FTP/SFTP-Client zum Verwalten von Serverressourcen und Betriebssystem-Mount-Dialoge, die Remote-Volumes über getrennte Finder-Fenster verteilen. 

ATBCmder beseitigt diese Fragmentierung durch seine **Virtual File System (VFS)**-Engine. ATBCmder basiert auf einer einheitlichen URI-Abstraktionsschicht `vfs://` und behandelt Remote-Server und komprimierte Archive genau wie lokale Standardordner. Sie können in ein `.tar.gz`-Archiv navigieren, Codedateien mit `F3` in der Vorschau anzeigen, eine verschachtelte Konfigurationsdatei mit `F4` bearbeiten (mit automatischem Live-Neupacken beim Speichern) und Assets mithilfe des Standardschlüssels `F5` direkt über eine sichere SFTP-Sitzung auf ein SMB-NAS vor Ort kopieren – alles ohne Extrahieren von Zwischendateien auf die Festplatte oder das Umschalten zwischen separaten Tools. 

---

## 1. Visueller Schnellstart: Die VFS-Architektur und Befehlsmatrix

ATBCmder leitet den gesamten Dateisystemzugriff über eine einheitliche Abstraktionsschicht. Unabhängig davon, ob ein Pfad auf eine Apple APFS SSD-Partition, ein Mitglied in einem verschachtelten `.zip`-Archiv oder ein Remote-Verzeichnis verweist, das auf einem Linux-SFTP-Server am anderen Ende der Welt gehostet wird, bietet die Dual-Panel-Schnittstelle ein identisches Betriebsmodell. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              ATBCMDER DUAL-PANEL GUI                                   │
│            Left Panel (Active)                  Right Panel (Inactive / Target)        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Local File System                   │  [2] Archive Virtual File System (VFS)      │
│      file:///Users/brain/projects/       │      vfs:///Users/brain/backup.tar.gz/src/  │
│      Direct POSIX / APFS access          │      In-place browse, F3 view, F4 live edit │
│                                          │                                             │
│  [3] Remote Network VFS (SFTP/SSH)       │  [4] Remote Storage VFS (SMB / WebDAV)      │
│      vfs://sftp://deploy@aws.prod/app/   │      vfs://smb://admin@truenas/Pool/Media/  │
│      Paramiko / SSH Keys / Keychain      │      Kernel mount_smbfs / WebDAVClient3     │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                          UNIFIED VFS DISPATCH ENGINE (vfs://)                          │
│     FileSystemModel ➔ VFSManager ➔ SessionCache ➔ StreamCopyWorker / RepackWorker      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Dual-Matrix-VFS- und Netzwerk-Spickzettel

| Aktion | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | Beschreibung | 
| :--- | :--- | :--- | :--- | :--- | 
| **Dateien ins Archiv packen** | `Alt+F5` / `⌥F5` | `Alt+F5` | `cm_PackFiles` | Öffnet das Dialogfeld „Archive Pack“ mit Format-, Komprimierungs- und Kennwortoptionen. | 
| **Dateien aus dem Archiv extrahieren** | `Alt+F9` / `⌥F9` | `Alt+F9` | `cm_ExtractFiles` | Entpackt ausgewählte Archive mit Kollisionsauflösung. | 
| **Schnelle Netzwerkverbindung** | Menü: Netzwerk | `cm_NetworkConnect` | `cm_NetworkConnect` | Öffnet den Dialog für die schnelle Ad-hoc-Verbindung. | 
| **Verbindungsmanager** | Menü: Netzwerk | `cm_ManageConnections`| `cm_ManageConnections`| Öffnet den vollständigen CRUD-Netzwerkmanager mit gespeicherten Verbindungsprofilen. | 
| **FTP-Verbindung** | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_FTPConnect` | Schnelle Verknüpfung zum Auslösen einer FTP-Verbindungssitzung. | 
| **Archiv/Ordner eingeben** | `Enter` / `⏎` | `Enter` | `cm_Open` | Navigiert direkt innerhalb eines `.zip`, `.tar`, `.7z` oder Remote-Verzeichnisses. | 
| **Aufsteigen zum übergeordneten Ordner** | `Backspace` / `⌫` | `Backspace` | `cm_GoToParent` | Steigt aus dem Archiv oder Remote-Verzeichnis zurück auf die übergeordnete Ebene. | 
| **Virtuelle/Remote-Datei anzeigen**| `F3` / `Fn+F3` | `F3` | `cm_View` | Streamt Remote- oder Archivdateien in Universal Lister. | 
| **Virtuelle/Remote-Datei bearbeiten**| `F4` / `Fn+F4` | `F4` | `cm_Edit` | Öffnet die Datei im Editor; Wird beim Speichern automatisch neu gepackt oder hochgeladen. | 
| **Panelübergreifend kopieren / VFS** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Kopiert ausgewählte Elemente über lokale, Archiv- oder Netzwerkendpunkte. | 
| **Hintergrund-Bedienfeld**| Menü: Anzeigen | `cm_OperationsPanel` | `cm_OperationsPanel` | Überwacht Hintergrundübertragungswarteschlangen, Geschwindigkeiten und aktive Threads. | 

---

## 2. Die einheitliche `vfs://` URI-Abstraktion

Herkömmliche Dateimanager behandeln Remote-Server und -Archive als Bürger zweiter Klasse und erfordern externe Bereitstellungsprogramme, temporäre Extraktionsordner oder Übertragungsclients von Drittanbietern. ATBCmder vereint jede Dateiquelle unter einer einzigen, klar definierten URI-Spezifikation: 

```
vfs://[protocol]://[user]@[host]:[port]/[remote_path]
```

### 2.1 Anatomie virtueller Pfade

Abhängig von der Betriebsdomäne nehmen `vfs://`-URIs eine von zwei Standardformen an: 

1. **Virtuelle Pfade archivieren**: 
   ```
   vfs:///Users/brain/Documents/release_v1.7.zip/src/main.py
   ```
 

- **Äußeres Präfix**: `vfs://` weist `FileSystemModel` an, die Pfaddurchquerung abzufangen. 
- **Containerpfad**: `/Users/brain/Documents/release_v1.7.zip` identifiziert das physische Containerarchiv im lokalen Speicher. 
- **Internes Mitglied**: `src/main.py` lokalisiert die im Archiv verschachtelte virtuelle Ressource. 

2. **Netzwerkserverpfade**: 
   ```
   vfs://sftp://developer@staging.internal.net:2222/var/www/html/index.php
   vfs://smb://admin@192.168.1.50/StoragePool/Backups/2026/
   vfs://webdavs://user@cloud.mycompany.com:443/remote.php/dav/files/user/
   ```
 

- **Schema Specifier**: Identifiziert den Transporttreiber (`sftp`, `ftp`, `ftps`, `smb`, `webdav`, `webdavs`, `gdrive`). 
- **Authentifizierung**: Kodiert Benutzeranmeldeinformationen und Zielport. 
- **Remote-Ziel**: Löst absolute Verzeichnis- und Dateipfade auf dem Remote-Host auf. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              VFS URI ROUTING IN ACTION                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Input URI: vfs://sftp://deploy@aws.infra:22/var/log/nginx/access.log                 │
│                 │      │        │        │   └────────────────────► Remote Path        │
│                 │      │        │        └────────────────────────► Port (Default 22)  │
│                 │      │        └─────────────────────────────────► Host / Server      │
│                 │      └──────────────────────────────────────────► Username           │
│                 └─────────────────────────────────────────────────► Protocol Scheme    │
│                                                                                        │
│   Input URI: vfs:///Volumes/Data/Archive.zip/docs/manual.pdf                           │
│                 │                      │        └─────────────────► Archive Member     │
│                 │                      └──────────────────────────► Physical Archive   │
│                 └─────────────────────────────────────────────────► Virtual Scheme     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Nahtlose Dual-Panel-Integration

Da virtuelle Pfade den Standardverzeichnisstrukturen in ATBCmder entsprechen, genießen Sie volle Dual-Panel-Parität: 

- **Virtuelle Arbeitsbereiche mit Registerkarten**: Öffnen Sie einen Remote-SFTP-Ordner in Tab 1, ein verschlüsseltes lokales ZIP-Archiv in Tab 2 und Ihren lokalen Ordner `~/Downloads` in Tab 3. 
- **Directional Copying (`F5`)**: Wählen Sie Dateien in Ihrem lokalen aktiven Bereich aus und drücken Sie `F5`, um sie direkt auf den Remote-Server oder das komprimierte Archiv hochzuladen, das im inaktiven Bereich angezeigt wird. 
- **Drag-and-Drop-Interoperabilität**: Ziehen Sie Elemente ohne Zwischenspeicherung über Panels zwischen lokalen Festplatten, Netzwerkfreigaben und Archivhierarchien. 
- **Interaktive Breadcrumb-Leiste**: Die Breadcrumb-Pfadleiste analysiert virtuelle URIs in anklickbare Segmente. Klicken Sie auf einen beliebigen übergeordneten Ordner oder das Root-Server-Badge, um sofort in der Baumstruktur nach oben zu springen. 

---

## 3. Archiv-VFS: In-Place-Navigation und -Inspektion

Das Öffnen eines Archivs in ATBCmder erfordert keine manuelle Extraktion oder ein Dekomprimierungstool eines Drittanbieters. Markieren Sie einfach ein unterstütztes Archiv und drücken Sie **`Enter`** (oder doppelklicken Sie). ATBCmder mountet das Archiv direkt und verwandelt das Panel in einen Hochgeschwindigkeits-Browser für virtuelle Verzeichnisse. 

![Archive VFS In-Place Navigation](images/archive_vfs.png) 
*Abbildung 6.1: Navigieren in einem mehrfach verschachtelten komprimierten Archiv als virtueller Ordner mit unkomprimierten Größen, Zeitstempeln und Unterverzeichnissen.*

### 3.1 Unterstützte Archivformate

ATBCmder verfügt über integrierte Treiber für alle branchenüblichen Archiv- und Komprimierungsformate: 

| Formatieren | Dateierweiterungen | Lesen Sie Support | Schreiben / Packen | Verschlüsselungsunterstützung | 
| :--- | :--- | :---: | :---: | :--- | 
| **PLZ** | `.zip` | Ja | Ja | Standard & AES-256 (`pyzipper`) | 
| **GZip-Tarball** | `.tar.gz`, `.tgz` | Ja | Ja | POSIX-Standard-Tar-Streaming | 
| **BZip2-Tarball**| `.tar.bz2`, `.tbz2` | Ja | Ja | Bzip2-Blockkomprimierung mit hohem Verhältnis | 
| **XZ-Tarball** | `.tar.xz`, `.txz` | Ja | Ja | Hocheffiziente LZMA2-Komprimierung | 
| **Einfacher TAR** | `.tar` | Ja | Ja | Unkomprimiertes UNIX-Bandarchiv | 
| **7-Zip** | `.7z` | Ja | Ja (über `py7zr`)| LZMA / LZMA2 solide Komprimierung |

### 3.2 Workflows für die In-Place-Navigation

Beim Durchsuchen eines Archivs: 

1. **Unterverzeichnisse eingeben**: Drücken Sie `Enter` in einem beliebigen Ordner im Archiv, um verschachtelte Bäume zu erkunden. 
2. **Aufsteigen zum übergeordneten Element (`..`)**: Drücken Sie `Backspace` (`⌫`) oder doppelklicken Sie auf den Eintrag `.. [Parent Directory]`, um aufzusteigen. Sobald Sie das Stammverzeichnis des Archivs erreicht haben, gelangen Sie durch Drücken von `Backspace` direkt zum physischen Verzeichnis zurück, das die Archivdatei enthält. 
3. **Sofortige Vorschau (`F3` / `Fn+F3`)**: Markieren Sie ein beliebiges Dokument, Bild oder eine Quelldatei im Archiv und drücken Sie `F3`. ATBCmder extrahiert die Zieldatei automatisch in eine sichere temporäre Sandbox und rendert sie im Universal Lister. 
4. **Selektives Kopieren (`F5` / `Fn+F5`)**: Anstatt ein ganzes Multi-Gigabyte-Archiv zu entpacken, nur um eine oder zwei Dateien abzurufen, wählen Sie die spezifischen Mitglieder aus, die Sie benötigen, und drücken Sie `F5`. ATBCmder entpackt nur die ausgewählten Elemente direkt in das inaktive Panel. 

> [!NOTE] 
> Bei der Vorschau oder dem Kopieren einzelner Dateien aus einem Archiv streamt ATBCmder nur die angeforderten Dateibytes direkt aus dem Container-Stream. Das Entpacken nicht ausgewählter Geschwisterdateien verschwendet weder Speicherplatz noch Zeit. 

---

## 4. Live-Umpacken: Direktbearbeitung in Archiven

Einer der leistungsstärksten Workflows in ATBCmder ist **Live Repacking**. In der Vergangenheit erforderte das Ändern einer einzelnen Datei, die in einem komprimierten Archiv verschachtelt war, eine langwierige Abfolge von sechs Schritten: Extrahieren des gesamten Archivs, Suchen der Zieldatei, Bearbeiten und Speichern, erneutes Komprimieren des Verzeichnisses in ein neues Archiv, Löschen des Originalarchivs und Bereinigen temporärer Ordner. 

ATBCmder macht das Bearbeiten von Dateien in Archiven genauso mühelos wie das Bearbeiten lokaler Standarddateien. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              LIVE REPACKING LIFECYCLE                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  1. User presses F4 on "config.json" inside "package.zip"                              │
│     │                                                                                  │
│     ├──► ATBCmder extracts "config.json" to sandbox: /tmp/dc_repack_xyz/config.json    │
│     └──► Opens internal EditorDialog with window title: "config.json — Editor"         │
│                                                                                        │
│  2. User modifies file and presses Cmd+S (Save)                                        │
│     │                                                                                  │
│     ├──► Editor emits file_saved signal                                                │
│     └──► RepackWorker checks original archive size vs ArchiveRepackWarningMB threshold │
│                                                                                        │
│  3. Atomic Repack Execution                                                            │
│     │                                                                                  │
│     ├──► Writes modified stream to staging archive: /tmp/package.zip.tmp               │
│     ├──► Validates container integrity via archive driver                              │
│     ├──► Atomic swap: os.replace("/tmp/package.zip.tmp", "/original/package.zip")      │
│     └──► Refreshes active file panel and cleans up sandbox /tmp/dc_repack_xyz/         │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Schritt-für-Schritt: Bearbeiten einer archivierten Konfigurationsdatei

1. Navigieren Sie in das Archiv (z. B. `application_bundle.zip`), indem Sie `Enter` drücken. 
2. Suchen Sie die Datei, die Sie ändern möchten (z. B. `settings.yaml`). 
3. Drücken Sie **`F4`** (`Fn+F4`). ATBCmder extrahiert die Datei in einen temporären Cache und startet den integrierten Editor. 
4. Nehmen Sie Ihre Änderungen im Editor vor. 
5. Drücken Sie zum Speichern **`Cmd+S`** (`⌘S`). 
6. Schließen Sie den Editor mit `Cmd+W` (`⌘W`) oder `Esc`. 
7. `RepackWorker` von ATBCmder aktualisiert automatisch das interne Mitglied, komprimiert die aktualisierte Struktur in eine temporäre Datei, ersetzt atomar das Originalarchiv und aktualisiert die Panelansicht. 

> [!ACHTUNG] 
> **Großer Archivschutz (`ArchiveRepackWarningMB`)** 
> Das Neupacken eines komprimierten Archivs erfordert das Dekomprimieren und Neukodieren von Container-Streams. Das Ändern einer 10-KB-Datei in einem 20-GB-Videoarchiv `.tar.gz` würde den Computer dazu zwingen, alle 20 GB an Daten neu zu schreiben. 
> 
> Um ein versehentliches Einfrieren der Festplatte zu verhindern, enthält ATBCmder einen schützenden Sicherheitsschwellenwert (`ArchiveRepackWarningMB`, Standard: **100 MB** in `atbcmder.xml`). Wenn Sie versuchen, eine Datei in einem Archiv zu bearbeiten oder zu löschen, das diesen Grenzwert überschreitet, zeigt ATBCmder eine Bestätigungsaufforderung an: 
> *„Um dieses Archiv zu ändern, muss die gesamte Datei neu gepackt werden, was lange dauern kann. Möchten Sie fortfahren?“* 

---

## 5. Archive erstellen und extrahieren (`Alt+F5` / `Alt+F9`)

ATBCmder stellt dedizierte Hintergrundarbeiter zum Erstellen und Extrahieren von Archiven bereit und stellt sicher, dass Ihre Dateibereiche auch bei lang andauernden Komprimierungsaufträgen reaktionsfähig bleiben. 

![Pack and Extract Archives](images/archive_pack_extract.png) 
*Abbildung 6.2: Das Dialogfeld „Archivparameter“ (Alt+F5 / cm_PackFiles) zeigt Zielpfad, Formatauswahl, Komprimierungsstufen und Passwortverschlüsselung.*

### 5.1 Dateien komprimieren (`Alt+F5` / `⌥F5` / `cm_PackFiles`)

So erstellen Sie ein neues Archiv: 

1. Wählen Sie im aktiven Bereich die Dateien oder Verzeichnisse aus, die Sie bündeln möchten. 
2. Drücken Sie **`Alt+F5`** (`⌥F5`) oder wählen Sie **Dateien ➔ Packen...** aus der Menüleiste. 
3. Das Dialogfeld **Dateien packen** erscheint: 
- **Archivdatei erstellen**: Zieldateipfad. Standardmäßig schlägt ATBCmder vor, das Archiv im Verzeichnis des inaktiven Panels abzulegen, das nach dem fokussierten Element benannt ist. 
- **Archivformat**: Wählen Sie zwischen `ZIP`, `TAR`, `TAR.GZ`, `TAR.BZ2`, `TAR.XZ` oder `7Z`. 
- **Komprimierungsstufe**: 
- `Store`: Keine Komprimierung; Sofortverpackung für vorkomprimierte Medien (MP4, JPEG). 
- `Fast`: Geringer CPU-Overhead; Ideal für schnelle Transfers. 
- `Normal (Deflated)`: Ausgewogenes Geschwindigkeits- und Komprimierungsverhältnis (empfohlen für den allgemeinen Gebrauch). 
- `Maximum`: Komprimierung mit höchster Dichte (verwendet ggf. LZMA/Bzip2). 
- **Passwort (nur ZIP)**: Geben Sie eine geheime Passphrase ein, um das Archiv zu verschlüsseln. 
4. Klicken Sie auf **Start** (oder drücken Sie `Enter`). Der Vorgang wird in einem nicht blockierenden Hintergrundthread mit einem Fortschrittsbalken und einer Datei-für-Datei-Statusanzeige ausgeführt.

#### AES-256-Passwortverschlüsselung nach Militärstandard

Die Standard-ZIP-Verschlüsselung (älteres ZipCrypto) ist kryptografisch fehlerhaft und anfällig für Klartext-Wörterbuchangriffe. Wenn Sie ein Passwort für ein ZIP-Archiv angeben, verwendet ATBCmder die **AES-256-Verschlüsselung** mit `pyzipper` (`pyzipper.AESZipFile` mit `WZ_AES`-Standard). Dies stellt die Kompatibilität mit macOS, WinZip und 7-Zip sicher und schützt gleichzeitig sensible Daten vor Brute-Force-Entschlüsselung.

#### Aufteilen riesiger Archive auf Sets mit mehreren Bänden

Wenn Sie ein Archiv über E-Mail-Anhänge, FAT32-Laufwerke oder Cloud-Upload-Grenzen mit Dateigrößenbeschränkungen verteilen müssen: 

1. Bündeln Sie Ihre Dateien mit `Alt+F5` (`cm_PackFiles`). 
2. Markieren Sie das resultierende Archiv `.zip` oder `.tar` und lösen Sie den Dateisplitter über **`Alt+F6`** (`cm_FileSpliter`) aus. 
3. Wählen Sie eine voreingestellte Teilungsgröße (z. B. `100 MB`, `4.7 GB DVD`, `CD 700 MB` oder eine benutzerdefinierte Bytegröße). 
4. ATBCmder generiert nummerierte Teilstücke (`archive.zip.001`, `archive.zip.002` usw.) zusammen mit einem CRC32-Verifizierungsmanifest. Empfänger können den ursprünglichen Container jederzeit mit **`cm_FileLinker`** (`cm_Combine`) wieder zusammensetzen. 

---

### 5.2 Archive extrahieren (`Alt+F9` / `⌥F9` / `cm_ExtractFiles`)

So extrahieren Sie Archive auf die Festplatte: 

1. Markieren Sie ein oder mehrere Archive im aktiven Bereich. 
2. Drücken Sie **`Alt+F9`** (`⌥F9`) oder wählen Sie **Dateien ➔ Extrahieren...** aus der Menüleiste. 
3. Das Dialogfeld **Dateien extrahieren** wird angezeigt: 
- **Zu extrahierendes Archiv**: Ausgewählter Container-Quellpfad. 
- **In Verzeichnis extrahieren**: Zielverzeichnis (standardmäßig das inaktive Panel). 
- **Vorschau des Inhalts**: Ein interaktives Listenfeld, das Archivmitglieder in Echtzeit lädt. 
- **Passwort**: Eingabefeld für passwortgeschützte Archive. 
4. Klicken Sie auf **Start**. Wenn im Zielordner bereits eine Zieldatei vorhanden ist, hält ATBCmder den Worker an und zeigt einen interaktiven Kollisionsdialog an: 
- **Überschreiben**: Ersetzt die in Konflikt stehende Zieldatei. 
- **Überspringen**: Lässt die vorhandene Datei unberührt und fährt mit dem nächsten Element fort. 
- **Alle überschreiben**: Überschreibt stillschweigend alle nachfolgenden Konflikte. 
- **Alle überspringen**: Alle vorhandenen Zieldateien werden automatisch umgangen. 
- **Abbrechen**: Stoppt den Extraktionsprozess sicher. 

---

## 6. Remote-Netzwerk-VFS: Protokolle und Remote-Speicher

ATBCmder umfasst eine Multiprotokoll-Netzwerk-Client-Engine, mit der Remote-Server direkt im Dual-Panel-Arbeitsbereich bereitgestellt, durchsucht und manipuliert werden können. 

![Network VFS Client](images/network_vfs.png) 
*Abbildung 6.3: Durchsuchen von Remote-Linux-Serververzeichnissen über sicheres SFTP mit Live-Dateiattributen, Besitzberechtigungen und Dual-Panel-Übertragung.* 

![Remote Connection Overview](images/smb_sftp_ftp_remote_access.png) 
*Abbildung 6.4: Unterstützte Netzwerkverbindungstypen: FTP/FTPS, sicheres SFTP, WebDAV-Cloud-Speicher und SMB-Netzwerkfreigaben.*

### 6.1 Unterstützte Netzwerkprotokolle

| Protokollschema | Standardport | Transportschicht | Authentifizierungsmodi | Am besten geeignet für | 
| :--- | :---: | :--- | :--- | :--- | 
| **`sftp://`** | `22` | SSH-2 (Paramiko) | Passwort, SSH-Schlüssel (`id_rsa`, `id_ed25519`) | Linux-Server, Cloud-Instanzen, Staging-Hosts | 
| **`ftp://`** | `21` | Einfach RFC 959 | Anonym, Klartext-Benutzername und Passwort | Legacy-Webhosting, lokale Laborgeräte | 
| **`ftps://`** | `990` | TLS-verschlüsseltes FTP | Benutzername und Passwort mit SSL/TLS | Sichere kommerzielle FTP-Server | 
| **`smb://`** | `445` | CIFS / SMB3 | Windows NT / Kerberos / Lokales Konto | Windows-Freigaben, NAS-Appliances, Samba-Server | 
| **`webdav://`** | `80` | HTTP-WebDAV | Basic, Digest-Authentifizierung | Webserver, lokaler Netzwerkspeicher | 
| **`webdavs://`** | `443` | HTTPS-WebDAV | SSL-verschlüsselte Basic/Digest-Authentifizierung | Nextcloud, ownCloud, kommerzieller Cloud-Speicher | 
| **`gdrive://`** | `443` | Google Drive-API | OAuth2-Token-Autorisierung | Cloud-Laufwerke und freigegebene Ordner von Google Drive | 

---

### 6.2 Protokollfunktionen und tiefer Einblick

#### SFTP (SSH File Transfer Protocol)

Unterstützt durch die branchenübliche SSH-Engine `paramiko` baut der SFTP-Treiber von ATBCmder verschlüsselte Tunnel über Port 22 auf: 

- **Host-Schlüsselsicherheit (`WarningPolicy`)**: In Übereinstimmung mit strengen Sicherheitsanforderungen konsultiert ATBCmder automatisch Ihre lokale Datei `~/.ssh/known_hosts`. Beim Herstellen einer Verbindung zu einem bekannten Host werden die Hostschlüssel kryptografisch überprüft. Wenn ein unbekannter Server gefunden wird, gibt ATBCmder eine Sicherheitswarnung aus, anstatt unerwarteten öffentlichen Schlüsseln stillschweigend zu vertrauen. 
- **SSH-Schlüsselauthentifizierung**: Zusätzlich zur Standard-Passwortauthentifizierung unterstützt ATBCmder private SSH-Schlüsseldateien (`~/.ssh/id_rsa`, `~/.ssh/id_ed25519`). 
- **UNIX-Attributzuordnung**: Behält Remote-Oktaldateimodi (`chmod`), Benutzer-/Gruppenbesitzzeichenfolgen und genaue POSIX-Änderungszeitstempel bei.

#### FTP & FTPS (Explizites / Implizites SSL)

Angetrieben durch Pythons `ftplib` unterstützt der FTP-Treiber:

 - **Passiver Modus (PASV)**: Standardmäßig aktiviert, um zuverlässige Verbindungen über restriktive NAT-Router und Consumer-Firewalls sicherzustellen. 
- **Konfigurierbare Kodierungen**: Behebt Anzeigeprobleme bei Nicht-ASCII-Dateinamen, indem Sie zwischen den Zeichensätzen `UTF-8`, `ISO-8859-1`, `GB18030` und `Windows-1252` wechseln können.

#### SMB / Samba (Windows-Freigaben und NAS-Geräte)

Im Gegensatz zu naiven Userspace-Python-SMB-Bibliotheken, die unter langsamen Übertragungsgeschwindigkeiten leiden, verwendet ATBCmder eine Hybridarchitektur: 

- **macOS Native Kernel Acceleration (`mount_smbfs`)**: Unter macOS nutzt ATBCmders `SambaMounter` das native `/sbin/mount_smbfs`-Subsystem von Apple. Es mountet die Remote-Freigabe direkt in den macOS VFS-Baum (`/Volumes/` oder ein isoliertes Mount-Verzeichnis) und ermöglicht so den vollen hardwarebeschleunigten SMB3-Lese-/Schreibdurchsatz. 
- **Vorhandene Mount-Erkennung**: Wenn macOS Finder oder ein Systemskript die Ziel-SMB-Freigabe bereits gemountet hat, erkennt ATBCmder automatisch den aktiven Mountpunkt aus der OS-Tabelle `mount` und navigiert sofort zu ihm, wodurch redundante Netzwerkverbindungen vermieden werden. 

> [!IMPORTANT] 
> **SMB-Freigabenamenanforderung** 
> Ein SMB-Server kann nicht auf der Ebene des reinen Hostnamens durchsucht werden. Ein SMB-URI **muss** den Zielfreigabe- oder Exportnamen im Pfad enthalten: 
> 
> - ❌ Ungültig: `vfs://smb://nas.local/` 
> - ✅ Gültig: `vfs://smb://nas.local/StoragePool` oder `vfs://smb://192.168.1.100/Media`

#### WebDAV & WebDAVS (Nextcloud / Cloud Storage)

Dieser Treiber basiert auf `webdavclient3` und bietet bidirektionale Dateisynchronisierung mit modernen Cloud-Speicherlösungen: 

- **SSL-Zertifikatsüberprüfung**: Unterstützt die strikte SSL-Zertifikatsvalidierung für öffentliche WebDAVS-Hosts, mit einem Override-Schalter für selbstsignierte Zertifikate in privaten Homelab-Setups. 
- **Rekursive Verzeichniserstellung (`makedirs`)**: Erstellt bei Massen-Upload-Vorgängen automatisch fehlende verschachtelte Remote-Verzeichnispfade. 

---

## 7. Quick Connect vs. Verbindungsmanager

ATBCmder bietet zwei flexible Mechanismen für die Verbindung zu Remote-Hosts: **Quick Connect** für schnelle, temporäre Sitzungen und **Connection Manager** für dauerhafte, kategorisierte Server-Lesezeichen.

### 7.1 Schnellverbindung (`cm_NetworkConnect`)

Wenn Sie schnell auf einen Server zugreifen müssen, ohne Ihre permanente Konfiguration zu überladen: 

1. Wählen Sie **Netzwerk ➔ Schnellverbindung...** (oder führen Sie den Befehl `cm_NetworkConnect` aus). 
2. Die Lightweight-Verbindungsaufforderung erscheint: 
- **Protokoll**: Wählen Sie `sftp`, `ftp`, `ftps`, `smb`, `webdav`, `webdavs` oder `gdrive`. 
- **Host & Port**: Geben Sie die Serveradresse ein (der Port füllt automatisch die Standardwerte aus). 
- **Benutzername und Passwort**: Verbindungsanmeldeinformationen eingeben. 
- **Remote-Pfad**: Remote-Startverzeichnis (Standard: `/`). 
- **Passwort merken**: Für eine flüchtige Einzelsitzungsverbindung deaktiviert lassen. 
3. Klicken Sie auf **Verbindung testen**, um den Netzwerk-Handshake und die Anmeldeinformationen zu überprüfen, bevor Sie eine Verbindung herstellen. 
4. Klicken Sie auf **Verbinden**. ATBCmder öffnet sofort eine neue Registerkarte im aktiven Bereich, die auf den Remote-Server verweist. 

---

### 7.2 Verbindungsmanager (`cm_ManageConnections`)

Für Server, auf die Sie regelmäßig zugreifen, bietet der **Connection Manager** ein vollständiges Konfigurations-Dashboard: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              CONNECTION MANAGER DIALOG                                 │
├──────────────────────────────┬─────────────────────────────────────────────────────────┤
│  Saved Connections           │  Connection Details                                     │
│  ┌────────────────────────┐  │  Label:        [ Staging Web Server (AWS)             ] │
│  │ 🔐 AWS Staging Server  │  │  Protocol:     [ SFTP (port 22)                     ▼ ] │
│  │ 🖧 Synology Office NAS │  │  Host:         [ ec2-54-210-10-2.compute.amazonaws.com] │
│  │ 🌐 Nextcloud Personal  │  │  Port:         [ 22                                   ] │
│  │ 📂 Legacy Archive FTP  │  │  Username:     [ ubuntu                               ] │
│  │                        │  │  Password:     [ ••••••••••••••••••                   ] │
│  │                        │  │  Remote Path:  [ /var/www/production                  ] │
│  │                        │  │  [✓] Remember password in macOS Keychain                │
│  └────────────────────────┘  │                                                         │
│  [➕ New] [⧉ Dup] [🗑 Del]    │  [🔍 Test Connection]          [💾 Save]  [🔗 Connect] │
└──────────────────────────────┴─────────────────────────────────────────────────────────┘
```

#### Verwalten von Serverprofilen

- **Neu erstellen (`➕ New`)**: Löscht das rechte Formular, um eine neue Serverkonfiguration zu definieren. 
- **Duplikat (`⧉ Duplicate`)**: Klont das ausgewählte Verbindungsprofil. Ideal für die Verwaltung mehrerer Umgebungen (Entwicklung, Staging, Produktion) auf identischen Hostkonfigurationen. 
- **Löschen (`🗑 Delete`)**: Entfernt das Verbindungsprofil und löscht zugehörige Anmeldeinformationen aus dem Systemschlüsselbund. 
- **Verbindung testen (`🔍 Test Connection`)**: Entsendet einen Hintergrund-Worker (`ConnectionTestWorker`), um eine Verbindung herzustellen, sich zu authentifizieren und ordnungsgemäß zu trennen und so die Reaktionsfähigkeit des Servers zu überprüfen, ohne wegnavigieren zu müssen. 
- **Verbinden (`🔗 Connect`)**: Speichert alle ausstehenden Feldbearbeitungen, richtet die Remote-Sitzung ein und lädt das Remote-Verzeichnis in eine neue aktive Panel-Registerkarte.

#### Menü „Dynamische gespeicherte Verbindungen“.

Gespeicherte Verbindungen werden automatisch in die obere Menüleiste unter **Netzwerk ➔ Gespeicherte Verbindungen** integriert. Sie können jeden mit einem Lesezeichen versehenen Server mit einem einzigen Klick mounten: 

- `Network ➔ Saved Connections ➔ 🔐 AWS Staging Server` 
- `Network ➔ Saved Connections ➔ 🖧 Synology Office NAS` 

---

## 8. Sicherheit von Ausweisen und Schlüsselbundintegration

Konfigurationsdateien des Dateimanagers sind ein Hauptziel für Malware zum Sammeln von Anmeldeinformationen. Viele ältere Dateimanager speichern FTP/SFTP-Passwörter in Klartext-XML- oder INI-Konfigurationsdateien im Home-Verzeichnis des Benutzers. 

**ATBCmder garantiert keine Speicherung von Anmeldeinformationen im Klartext.**

### 8.1 Die Sicherheitsarchitektur

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           CREDENTIAL STORAGE ARCHITECTURE                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Connection Configuration XML                    Apple System Keychain                │
│   (~/.config/atbcmder/atbcmder.xml)               (service: "ATBCmder_VFS")            │
│   ┌─────────────────────────────────────┐         ┌──────────────────────────────────┐ │
│   │ <connection>                        │         │ Label: "AWS Staging Server"      │ │
│   │   <label>AWS Staging</label>        │         │ Key:   Encrypted Secret          │ │
│   │   <scheme>sftp</scheme>             │         │ Access: Controlled by macOS      │ │
│   │   <host>aws.infra.net</host>        │         │         Hardware Security Enclave│ │
│   │   <user>deploy</user>               │         └──────────────────────────────────┘ │
│   │   <password></password>             │                           ▲                  │
│   │ </connection>                       │                           │                  │
│   └─────────────────────────────────────┘                           │                  │
│         ▲                                                           │                  │
│         │ Password stripped on save                                 │ Stored via       │
│         └─────────────────── ConnectionManager ─────────────────────┘ Python keyring   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

1. **Klartext-XML-Scrubbing**: Immer wenn Verbindungsprofile auf die Festplatte serialisiert werden (`atbcmder.xml`), erzwingt die Routine `ConnectionManager.save()` explizit `d["password"] = ""` vor dem Schreiben. Selbst wenn eine unbefugte Partei Ihre Konfigurations-XML überprüft, werden niemals Serverkennwörter preisgegeben. 
2. **MacOS-System-Schlüsselbundverschlüsselung**: Wenn das Kontrollkästchen **Passwort speichern** aktiviert ist, werden Passwörter über die System-API `keyring` unter der sicheren Dienstkennung `ATBCmder_VFS` direkt im macOS-Schlüsselbund gespeichert. Schlüsselableitung und -speicherung werden durch Apples Hardware Secure Enclave geschützt. 
3. **Ephemere In-Memory-Sitzungen**: Wenn „Passwort speichern“ deaktiviert ist, werden Anmeldeinformationen während des aktuellen Anwendungslebenszyklus ausschließlich im dynamischen Speicher (`VFSSessionCache`) gespeichert und gelöscht, sobald ATBCmder beendet wird. 

---

## 9. ⚡ Profi-Tipps: Hochleistungs-Fernbedienung

### Tipp 1: Nicht blockierende Hintergrundübertragungswarteschlange (`cm_OperationsPanel`)

Beim Kopieren großer Verzeichnisse über Remote-Server oder beim Herunterladen von Multi-Gigabyte-ISOs über SFTP darf Ihr Arbeitsbereich niemals einfrieren. Alle Netzwerkdateivorgänge in ATBCmder werden automatisch in die **Hintergrundoperationswarteschlange** integriert: 

- Drücken Sie **`F5`**, um eine Übertragung zu starten, und klicken Sie dann auf **Hintergrund** (oder lassen Sie sie automatisch in die Warteschlange stellen). 
- Öffnen Sie das Bedienfeld über **Anzeigen ➔ Bedienfeld** (`cm_OperationsPanel`), um Live-Bandbreitendiagramme, Bytezahlen pro Datei und verbleibende Übertragungsschätzungen zu überwachen. 
- Sie können in der Warteschlange befindliche Netzwerkübertragungen anhalten, fortsetzen oder neu anordnen, während Sie in beiden Bereichen weiterhin lokale Dateien durchsuchen.

### Tipp 2: Streamen Sie das Kopieren über heterogene Protokolle hinweg

Die `stream_copy_file`-Engine von ATBCmder ermöglicht direktes **Server-zu-Server-Streaming**. Wenn Sie einen Ordner von einem SFTP-Server im linken Bereich auf eine SMB-Netzwerkfreigabe im rechten Bereich ziehen: 

- ATBCmder lädt **nicht** das gesamte Verzeichnis auf Ihre lokale Mac-Festplatte herunter, bevor es erneut hochgeladen wird. 
- Die Daten werden über einen speicherinternen Pufferring aufgeteilt, wobei Bytes vom Quell-Socket direkt in den Ziel-Socket gestreamt werden. Dies eliminiert den lokalen Festplattenverschleiß und ermöglicht Übertragungen, die größer sind als Ihre verfügbare lokale SSD-Kapazität.

### Tipp 3: Halten Sie das Netzwerk am Leben und verhindern Sie Verbindungsabbrüche

Zustandsbehaftete Netzwerk-Firewalls und NAT-Gateways trennen inaktive TCP-Verbindungen häufig nach 60 bis 300 Sekunden Inaktivität. So verhindern Sie getrennte Sitzungen beim Durchsuchen großer Remote-Bäume: 

– Die `BaseNetworkVFS`-Schicht von ATBCmder verwaltet automatisch Sitzungs-Heartbeats über inaktive Verbindungen. 

- Wenn es zu einem vorübergehenden Netzwerkausfall kommt, führt der interne `_retry()`-Mechanismus bis zu **3 Wiederholungsversuche** mit exponentiellem Backoff (`2^attempt` Sekundenintervalle) durch, bevor ein Verbindungsfehler gemeldet wird.

### Tipp 4: Remote-Dateien mit Auto-Upload-Lebenszyklus bearbeiten

Müssen Sie ein `nginx.conf` oder ein Python-Skript direkt auf einem Remote-Server bearbeiten? 

1. Markieren Sie die Remote-Datei in Ihrer SFTP- oder WebDAV-Panel-Ansicht. 
2. Drücken Sie **`F4`** (`Fn+F4`). 
3. ATBCmder lädt die Datei in eine isolierte temporäre Sandbox (`/tmp/`) herunter und öffnet sie im integrierten Editor. 
4. Jedes Mal, wenn Sie **`Cmd+S`** (`⌘S`) drücken, löst ATBCmder `_upload_vfs_temp()` aus, streamt die aktualisierte Datei asynchron zurück zum Remote-Server und zeigt eine Bestätigung in der Statusleiste an. 
5. Wenn Sie den Editor schließen, wird die Verknüpfung der temporären Datei mit `/tmp/` sicher aufgehoben. 

---

## 10. System- und Sicherheitswarnungen

> [!WARNUNG] 
> **Nichtübereinstimmung des SSH-Hostschlüssels** 
> Wenn ein SFTP-Server seine Hostschlüssel neu generiert (z. B. nach einer Neuinstallation des Betriebssystems) oder wenn versucht wird, ein Man-in-the-Middle-Netzwerk abzufangen, erkennt ATBCmder, dass der Serverschlüssel nicht mit dem in `~/.ssh/known_hosts` registrierten Fingerabdruck übereinstimmt. 
> Umgehen Sie niemals Hostschlüsselwarnungen in nicht vertrauenswürdigen öffentlichen Wi-Fi-Netzwerken, ohne den Fingerabdruck des öffentlichen Schlüssels des Servers unabhängig von Ihrem Systemadministrator zu überprüfen. 

> [!IMPORTANT] 
> **Temporärer Cache-Speicherplatz für große Remote-Dateien** 
> Beim Anzeigen (`F3`) oder Bearbeiten (`F4`) von Multi-Gigabyte-Dateien, die auf Remote-VFS-Servern gespeichert sind, streamt ATBCmder das Zielelement auf Ihr lokales `/tmp`-Volume. Stellen Sie sicher, dass der primäre APFS-Container Ihres Mac über ausreichend freien Speicherplatz verfügt, bevor Sie umfangreiche Remote-Video- oder Datenbankdateien öffnen. 

> [!ACHTUNG] 
> **Entfernte Netzwerkfreigaben aushängen** 
> Bei SMB-Freigaben, die über macOS `mount_smbfs` gemountet wurden, kann das Beenden der Netzwerkverbindung ohne Trennen der Verbindung dazu führen, dass veraltete Mount-Handles in `/Volumes/` zurückbleiben. Verwenden Sie immer das Bedienfeld-Laufwerksmenü oder die Trennaktion, bevor Sie Ihren Laptop schließen oder das Wi-Fi-Netzwerk wechseln. 

---

## 11. Referenztabelle für Master-Dual-Matrix-Tastaturen

| Kategorie | Aktionsbeschreibung | macOS-Verknüpfung | Klassischer Commander-Schlüssel | Befehls-ID | 
| :--- | :--- | :--- | :--- | :--- | 
| **Archivierungsvorgänge** | Ausgewählte Dateien/Ordner packen | `Alt+F5` / `⌥F5` | `Alt+F5` | `cm_PackFiles` | 
| **Archivierungsvorgänge** | Ausgewählte Archive extrahieren | `Alt+F9` / `⌥F9` | `Alt+F9` | `cm_ExtractFiles` | 
| **Archivierungsvorgänge** | Durchsuchen Sie den Archivcontainer| `Enter` / `⏎` | `Enter` | `cm_Open` | 
| **Archivierungsvorgänge** | Archiv zum übergeordneten Verzeichnis verlassen| `Backspace` / `⌫` | `Backspace` | `cm_ChangeDirToParent` | 
| **Archivierungsvorgänge** | Vorschau der Datei im Archiv | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Archivierungsvorgänge** | Datei im Archiv bearbeiten (Live)| `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Archivierungsvorgänge** | Nur ausgewählte Elemente extrahieren | `F5` / `Fn+F5` | `F5` | `cm_Copy` | 
| **Archivierungsvorgänge** | Großes Archiv in Volumes aufteilen| `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Archivierungsvorgänge** | Geteilte Volumenteile wieder zusammensetzen | Menü: Dateien ➔ Dateien kombinieren | — | `cm_FileLinker` / `cm_Combine` | 
| **Netzwerkverbindungen**| Dialogfeld „Schnelle Netzwerkverbindung“ | Menü: Netzwerk | — | `cm_NetworkConnect` | 
| **Netzwerkverbindungen**| Netzwerkverbindungen verwalten | Menü: Netzwerk | — | `cm_ManageConnections` | 
| **Netzwerkverbindungen**| Schnellverbindung zum FTP-Server | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_FTPConnect` | 
| **Netzwerkverbindungen**| Remote-Netzwerkfreigabe trennen| Menü: Netzwerk | — | `cm_NetworkDisconnect` | 
| **Transferverwaltung**| Offene Operationsübertragungswarteschlange | Menü: Anzeigen | — | `cm_OperationsPanel` | 
| **Transferverwaltung**| Aktive Warteschlange anhalten/fortsetzen | `Space` (in der Warteschlange)| `Space` | — |

--- 

<div align="center"> 
<p>Bereit, Hotkeys, Bedienfeldansichten und Anwendungsverhalten anzupassen?</p> 
<p><strong><a href="preferences_and_customization.md">Fahren Sie mit Kapitel 7 fort: Einstellungen und Anpassung &rarr;</a></strong></p> 
</div>