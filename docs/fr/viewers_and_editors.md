# Chapitre 4: Visionneuse universelle et éditeurs intégrés

Dans la gestion orthodoxe des fichiers à deux panneaux, la vitesse dépend fortement de la rapidité de l’inspection. Le lancement d'environnements de développement intégrés (IDE) lourds ou d'applications de bureau volumineuses simplement pour vérifier une somme de contrôle, vérifier une ligne de configuration, recadrer une capture d'écran ou inspecter un PDF crée des frictions cognitives et un encombrement des fenêtres. 

ATBCmder résout ce problème en fournissant un sous-système de visualisation et d'édition unifié et multimoteur directement intégré au cœur de l'application. Que vous ayez besoin d'un aperçu en ligne en temps réel lorsque vous vous déplacez dans des dossiers, d'une analyse médico-légale approfondie au niveau des octets en mode Hex, d'un lecteur audio qui continue de jouer en arrière-plan pendant que vous organisez des fichiers ou d'un éditeur de code atomique prenant en compte la syntaxe, ATBCmder vous offre un contrôle instantané du clavier. 

---

## 1. Démarrage rapide visuel : inspection et modification immédiate des fichiers

ATBCmder divise l'inspection et la modification des fichiers en deux paradigmes distincts : 

1. **Vue rapide du panneau opposé (`Cmd+Q` / `Ctrl+Q`)** : intègre un aperçu en direct et anti-rebond directement à l'intérieur du panneau inactif sans générer de fenêtres séparées. 
2. **Liste universelle dédiée (`F3`) et éditeur interne (`F4`)** : ouvre des fenêtres indépendantes et non modales prenant en charge les moteurs de format spécialisés, la recherche de texte intégral, la lecture multimédia et la coloration syntaxique. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANNEAU ACTIF (Navigation)                         PANNEAU INACTIF (Quick View)       │
│  /Users/brain/Projects/atbcmder/src                 [Aperçu rapide : main.py]          │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nom                          Taille Date    │   │ 0001: """                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Point d'entrée principal      │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: """                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Ligne 1/140] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Basculer Quick View    [F3] Visionneuse Lister    [F4] Éditeur      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Aide-mémoire pour l'inspection et l'édition à double matrice

| Actions | Raccourci macOS | Clé de commandant classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Basculer l'affichage rapide** | `Cmd+Q` / `⌘Q` | `Ctrl+Q` | `cm_QuickView` | Ouvre l'aperçu en direct dans le panneau opposé. | 
| **Liste universelle** | `F3` / `Fn+F3` | `F3` | `cm_View` | Ouvre l’élément sélectionné dans Universal Lister. | 
| **Éditeur interne** | `F4` / `Fn+F4` | `F4` | `cm_Edit` | Ouvre l'éditeur de code pour le texte ou l'éditeur d'images pour les graphiques. | 
| **Créer et modifier un nouveau fichier** | `Shift+F4` / `⇧F4` | `Shift+F4` | `cm_EditNew` | Demande le nom et ouvre l'éditeur. | 
| **Mise au point du panneau de commutation** | `Tab` / `⇥` | `Tab` | `cm_SwitchPanel` | Change la mise au point ; retourne Quick View symétriquement. | 
| **Mode d'affichage hexadécimal** | `2` | `2` | — *(Liste)* | Active/désactive l'inspection hexadécimale au niveau de l'octet dans Lister. | 
| **Mode d'affichage du texte** | `1` | `1` | — *(Liste)* | Renvoie Lister en mode texte brut formaté. | 
| **Bascule de retour à la ligne** | `Alt+W` / `⌥W` | `Alt+W` | — *(Liste/Éditeur)* | Active/désactive le retour à la ligne progressif dans Lister et Editor. | 
| **Basculer les numéros de ligne**| `Alt+L` / `⌥L` | `Alt+L` | — | Bascule les numéros de ligne de gouttière gauche. | 
| **Mode queue de journal en direct** | `F5` / `Fn+F5` | `F5` | — | Diffuse les entrées de journal nouvellement ajoutées en temps réel. | 
| **Audio de fond** | `Background` Bouton | — | — | Ancre la lecture audio dans la bande d’état du panneau. | 
| **Configurer les associations**| Menu de configuration | — | `cm_FileAssoc` | Configure les extensions de fichiers et les outils d'aide. | 

---

## 2. Panneau d'affichage rapide (`Cmd+Q` / `Ctrl+Q` / `cm_QuickView`)

Le **Panneau d'affichage rapide** est l'un des flux de travail les plus puissants des gestionnaires de fichiers orthodoxes. Plutôt que d'ouvrir et de fermer des fenêtres flottantes lorsque vous inspectez un dossier contenant des centaines d'éléments, Quick View transforme le panneau inactif en une fenêtre contextuelle intégrée. 

![Quick View Panel](images/quick_view_panel.png) 
*Figure 4.1 : Coup d'œil intégré dans le panneau opposé affichant le code en direct avec la syntaxe mise en évidence ainsi que la navigation dans le répertoire.*

### 2.1 L'avantage de l'aperçu sur deux panneaux

Pour activer l'aperçu rapide : 

1. Accédez à n’importe quel fichier ou répertoire dans le panneau actif. 
2. Appuyez sur **`Cmd+Q`** (`⌘Q`) sur macOS ou **`Ctrl+Q`** (`cm_QuickView`). 
3. Le panneau opposé passe instantanément de sa liste de répertoire normale au **Conteneur d'affichage rapide** (`QuickViewContainer`), affichant le contenu de l'élément sous votre curseur. 
4. Appuyer à nouveau sur `Cmd+Q` ou `Ctrl+Q` ferme l'aperçu et restaure la liste précédente des onglets et des dossiers du panneau opposé sans perdre votre place.

### 2.2 Mise à jour en temps réel anti-rebond de 100 ms

Lorsque vous maintenez enfoncées les touches fléchées `Up` ou `Down` pour faire défiler rapidement un dossier contenant des milliers de fichiers, les prévisualiseurs de fichiers standard gèlent souvent l'interface utilisateur ou déclenchent une destruction intense du disque. 

ATBCmder résout ce problème grâce à un **minuteur anti-rebond unique de 100 millisecondes** interne (`_quick_view_timer`) : 

- Au fur et à mesure que vous naviguez rapidement dans les lignes, le chemin du fichier actif est mis en mémoire. 
- Le chargement lourd des fichiers, l'analyse syntaxique et le rendu des vignettes ne se déclenchent qu'une fois que votre curseur s'arrête sur un élément pendant au moins 100 ms. 
- Le défilement reste parfaitement fluide à plus de 60 images par seconde, même lors de la navigation dans des répertoires multimédias de plusieurs gigaoctets ou lors de sauvegardes de disque brut.

### 2.3 Inversion de mise au point symétrique sur `Tab`

Un problème courant dans les gestionnaires à double panneau est la perte de votre aperçu lors du changement de panneau. Dans ATBCmder, Quick View propose **Symmetric Focus Flipping** : 

- Si l'affichage rapide est actif sur le panneau de droite et que vous appuyez sur **`Tab`** pour basculer le focus actif sur le panneau de droite : 
1. Le panneau de droite restaure immédiatement sa table de fichiers normale afin que vous puissiez interagir avec les fichiers. 
2. L'affichage rapide bascule automatiquement et de manière transparente vers le panneau de gauche, affichant un aperçu en direct de tout fichier mis en surbrillance dans le panneau de droite. 
- Cela maintient une boucle de navigation et d'inspection ininterrompue, quel que soit le panneau dans lequel vous travaillez.

### 2.4 Routage de contenu intelligent

Le conteneur Quick View détecte dynamiquement les extensions de fichiers, les signatures MIME et les en-têtes d'octets bruts pour sélectionner le moteur de prévisualisation optimal : 

| Type de contenu | Extensions/Signatures | Moteur de prévisualisation intégré | 
| :--- | :--- | :--- | 
| **Code source et texte** | `.py`, `.rs`, `.cpp`, `.c`, `.h`, `.js`, `.ts`, `.html`, `.css`, `.json`, `.xml`, `.yaml`, `.md`, heuristiques en texte brut | `TextPanel` avec coloration syntaxique et numéros de ligne Pygments. | 
| **Images raster et vectorielles**| `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`, `.bmp`, `.gif`, `.ico`, `.tiff` | `ImagePanel` avec sous-échantillonnage fluide et préservation des proportions. | 
| **Documents PDF** | `.pdf` | `PdfPanel` avec rendu de page natif `PySide6.QtPdf` (Ajuster à la largeur). | 
| **Médias audio et vidéo** | `.mp3`, `.wav`, `.flac`, `.aac`, `.m4a`, `.ogg`, `.mp4`, `.mkv`, `.mov`, `.avi`, `.webm` | `MediaPanel` avec aperçu audio en sourdine et commandes de lecture. | 
| **Données tabulaires** | `.csv`, `.tsv`, `.xlsx`, `.xls`, `.ods` | `SpreadsheetPanel` avec grille de tableau en lecture seule et dimensionnement automatique des colonnes. | 
| **Documents et livres électroniques** | `.docx`, `.odt`, `.rtf`, `.epub` | `DocumentPanel` / `EpubPanel` moteur de rendu de documents en texte enrichi. | 
| **Fichiers de base de données** | `.sqlite`, `.sqlite3`, `.db` | `SqlitePanel` avec navigateur de schéma et visionneuse de données de table. | 
| **Archives** | `.zip`, `.tar`, `.gz`, `.bz2`, `.xz`, `.7z` | `ArchiveInspectorPanel` affichant les hiérarchies de membres non compressées. |

### 2.5 Remplacement des propriétés de métadonnées (`QuickViewPropertiesWidget`)

Lorsque vous mettez en surbrillance un répertoire ou un format de fichier qui ne peut pas être restitué sous forme de texte ou de média, ATBCmder passe automatiquement à la **Vue de secours des propriétés** (`QuickViewPropertiesWidget`) : 

```
┌────────────────────────────────────────────────────────┐
│  📁 release_builds                                     │
│  /Volumes/ExternalSSD/Projects/release_builds          │
├────────────────────────────────────────────────────────┤
│  Metadata                                              │
│    Full Path:      /Volumes/ExternalSSD/...            │
│    Size:           Directory (or 148,290,112 bytes)    │
│    Last Modified:  2026-09-06 14:10:22                 │
│    Last Accessed:  2026-09-06 15:02:18                 │
├────────────────────────────────────────────────────────┤
│  Permissions (UNIX)                                    │
│    Octal Mode: 0755                                    │
│    Owner:  [✔] Read  [✔] Write  [✔] Execute            │
│    Group:  [✔] Read  [ ] Write  [✔] Execute            │
│    Others: [✔] Read  [ ] Write  [✔] Execute            │
├────────────────────────────────────────────────────────┤
│  Checksums / Stats                                     │
│    Contents: 42 files, 8 folders                       │
│    MD5:      Calculating... ➔ 8f14e45fceea167a...      │
│    SHA256:   Calculating... ➔ 3a491d90bc1f4201...      │
└────────────────────────────────────────────────────────┘
```
 

- **Carte d'en-tête** : affiche l'icône du système haute résolution, le nom du fichier et le chemin parent. 
- **Métadonnées du fichier** : affiche la taille exacte en octets, la taille lisible par l'homme (`KB`, `MB`, `GB`, `TB`), l'horodatage de modification (`mtime`) et l'horodatage d'accès. (`atime`). 
- **Matrice d'autorisation UNIX** : affiche le mode d'autorisation octale à 4 chiffres (par exemple `0755`, `0644`) ainsi qu'une matrice de cases à cocher 3x3 en lecture seule pour le propriétaire, le groupe et autres (`rwx`). 
- **Hachages d'arrière-plan asynchrones** : pour les fichiers, un thread d'arrière-plan asynchrone (`HashWorker`) calcule les hachages cryptographiques MD5 et SHA-256 sans bloquer l'interface. Pour les répertoires, il analyse et rapporte le nombre total de fichiers et sous-dossiers imbriqués. 

---

## 3. Liste universelle (`F3` / `Fn+F3` / `cm_View`)

Alors que Quick View est optimisé pour des aperçus rapides dans la fenêtre à deux panneaux, le **Universal Lister** (`F3` / `Fn+F3` / `cm_View`) ouvre une fenêtre non modale dédiée de niveau supérieur (`UniversalViewerDialog`). Plusieurs fenêtres Universal Lister peuvent être ouvertes simultanément, vous permettant de comparer des documents côte à côte ou de conserver les journaux en streaming sur des écrans secondaires.

### Barre d'outils d'action rapide supérieure

Le Lister dispose d'une barre d'outils d'action rapide intégrée offrant un accès rapide aux modes d'affichage, à la navigation et aux paramètres d'affichage : 

```
[Text (1)] [Hex (2)] [Wrap (Alt+W)] [Line Numbers (Alt+L)] [Tail (F5)] | [◀ Prev (P)] [Next ▶ (N)] | [🔍 Search (Ctrl+F)] [Go to Line (Ctrl+G)] | [Open in System (Ctrl+O)] [Fullscreen (F11)]
```
 

- **Mode texte (`1`) / Mode hexadécimal (`2`)** : basculez instantanément entre l'affichage des caractères décodés et l'inspection des octets bruts. 
- **Word Wrap (`Alt+W` / `⌥W`)** : active le retour à la ligne souple pour les longues lignes. 
- **Numéros de ligne (`Alt+L` / `⌥L`)** : bascule la gouttière de numérotation des lignes. 
- **Mode Tail (`F5`)** : fait défiler et capture automatiquement les données de journal nouvellement écrites en temps réel. 
- **Fichier précédent (`P`) / Fichier suivant (`N`)** : Navigue vers le fichier adjacent dans la table de fichiers du dossier parent sans fermer la fenêtre de la visionneuse. 
- **Rechercher (`Ctrl+F` / `Cmd+F`)** : ouvre la barre de recherche inférieure ancrée. 
- **Aller à la ligne (`Ctrl+G` / `Cmd+G`)** : demande un numéro de ligne pour accéder directement au code cible. 
- **Ouvrir dans le système (`Ctrl+O` / `Cmd+O`)** : transmet le fichier à l'application par défaut du système macOS (par exemple, Aperçu, Safari ou Xcode). 
- **Plein écran (`F11` / `Alt+Enter`)** : Maximise la fenêtre du Lister pour remplir l'affichage. 

---

### 3.1 Domaine 1 : Documents et livres structurés

ATBCmder intègre des moteurs de mise en page spécialisés pour les documents structurés, les diapositives, les livres électroniques et le texte formaté, éliminant ainsi le besoin d'attendre le lancement des suites bureautiques externes.

#### 3.1.1 Documents Word et texte enrichi (`DocumentPanel`)

Lorsque vous appuyez sur `F3` sur des fichiers Microsoft Word (`.docx`, `.doc`), Rich Text (`.rtf`) ou OpenDocument (`.odt`), ATBCmder engage `DocumentPanel` : 

- **Cartes de pages de documents** : rend les pages structurées sur des cartes papier centrées (`.doc-page`) avec une typographie nette et des marges correspondant aux mises en page de traitement de texte modernes. 
- **Préservation du formatage** : préserve les hiérarchies de paragraphes, les styles gras/italique/souligné, les variations de couleur de police, les listes non ordonnées et numérotées et les hyperliens en ligne. 
- **Tableaux complexes et rendu d'images intégré** : analyse les grilles de tableaux complexes à plusieurs colonnes avec un espacement des cellules bordé et restitue les illustrations raster en ligne intégrées. 
- **Zoom et recherche de page** : commandes de zoom de page granulaires (`Ctrl++` / `Ctrl+-` ou boîte de sélection de zoom) et barre de recherche intégrée dans le document (`ViewerSearchBar`).

#### 3.1.2 Diapositives de présentation (`PresentationPanel`)

Pour les présentations Microsoft PowerPoint (`.pptx`, `.ppt`), ATBCmder lance `PresentationPanel` : 

- **Lecteur de cartes de diapositives** : chaque diapositive est extraite et formatée comme une carte de présentation distincte et ombrée (`.slide-card`), vous permettant de consulter le contenu de manière séquentielle. 
- **Bande de sélection de diapositives** : un tiroir de navigation visuelle répertorie toutes les diapositives avec des index miniatures, vous permettant de passer instantanément à n'importe quelle diapositive dans un jeu de 100 diapositives. 
- **Recherche de diapositives** : appuyez sur `Cmd+F` pour rechercher des titres de diapositives, des puces, des notes de l'intervenant et des blocs de texte de légende sur l'ensemble de la présentation.

#### 3.1.3 Visionneuse de documents PDF (`PdfPanel`)

Propulsé nativement par `PySide6.QtPdf` et `QPdfView`, ATBCmder intègre un lecteur PDF de niveau entreprise : 

![PDF Viewer](images/pdf_viewer.png) 
*Figure 4.2 : Visionneuse PDF intégrée comprenant un aperçu des signets, une bande de vignettes de page, une recherche dans le document et des thèmes de lecture.* 

- **Défilement continu de plusieurs pages** : faites défiler de manière transparente des centaines de pages en mode multipage (`QPdfView.PageMode.MultiPage`), ou passez aux vues de livre sur une seule page ou sur deux pages. 
- **Barre latérale du document** : 
- *Plan / Arborescence des signets* : cliquez sur n'importe quel titre de chapitre ou de section dans la table des matières PDF (`QPdfBookmarkModel`) pour accéder directement à cette section. 
- *Bande de vignettes de page* : numérisez visuellement la mise en page et les éléments graphiques via la liste de vignettes verticales (`PdfThumbnailList`). 
- **Recherche et mise en surbrillance dans le document** : appuyez sur `Cmd+F` pour rechercher du texte dans le document. Les correspondances sont mises en évidence à l'écran avec une indexation des occurrences en temps réel (`Match 3 of 28`). Passez d’une occurrence à l’autre avec `Enter` ou `Shift+Enter`. 
- **Thèmes de lecture** : 
- *Normal* : Rendu papier standard des documents. 
- *Mode nuit inversé* : Inverse la luminance des pixels RVB (`InvertColorEffect`) pour une lecture confortable dans des environnements sombres sans fatigue oculaire. 
- *Chaleur sépia* : ton doux et chaud réduisant l'émission de lumière bleue lors de l'examen prolongé de documents. 
- **Sécurité et cryptage** : demande de manière transparente des mots de passe sur les fichiers PDF cryptés via `PdfPasswordDialog` et inspecte les métadonnées du créateur/producteur via `PdfPropertiesDialog`.

#### 3.1.4 Livres électroniques EPUB (`EpubPanel`)

La gestion de la documentation technique, des manuels ou des livres numériques au format EPUB (`.epub`) est native d'ATBCmder : 

- **Architecture double moteur** : utilise un moteur de rendu WebEngine haute fidélité (`QWebEngineView` avec `EpubUrlSchemeHandler` pour un style CSS riche et des illustrations vectorielles SVG) avec un repli automatique vers `QTextBrowser` sur les environnements minimaux. 
- **Barre latérale de la table des matières** : affiche les arborescences de chapitres imbriquées (`QTreeView`), permettant de passer en un clic entre les chapitres et les annexes du livre. 
- **Typographie et mise à l'échelle des polices** : redimensionnez dynamiquement la taille du texte de lecture via le curseur de police de la barre d'outils inférieure. 
- **Thèmes de confort de lecture** : basculement instantané entre les palettes de couleurs claires, foncées et sépia.

#### 3.1.5 Documents de démarque (`MarkdownPanel`)

Pour les fichiers README, les notes techniques et la documentation du développeur (`.md`, `.markdown`) : 

- **GitHub-Flavored Markdown (GFM)** : affiche les en-têtes, les citations, les règles horizontales, les listes de tâches (`- [x]`) et les tableaux à plusieurs colonnes. 
- **Style de syntaxe des blocs de code** : formate automatiquement les blocs de code clôturés (```python, ```bash, ```json) avec un ombrage d'arrière-plan distinct, une typographie à espacement fixe et une coloration syntaxique. 

---

### 3.2 Domaine 2 : données, tables et environnements d'exécution pour les développeurs

Pour les utilisateurs techniques, les analystes de données et les ingénieurs logiciels, ATBCmder fournit des outils d'inspection de données instantanés et hors ligne qui éliminent la surcharge des clients de bases de données externes ou des applications de feuilles de calcul.

#### 3.2.1 Feuilles de calcul hautes performances (`SpreadsheetPanel`)

L'ouverture de gros fichiers CSV ou de classeurs Excel à plusieurs feuilles dans des suites bureautiques lourdes peut prendre 10 à 20 secondes. `SpreadsheetPanel` d'ATBCmder les restitue instantanément : 

![Excel Spreadsheet and Data Preview](images/xls_viewer.png) 
*Aperçu d'une feuille de calcul Excel hautes performances dans Universal Lister avec onglets multi-feuilles et coordonnées figées* 

- **Prise en charge des formats** : Microsoft Excel (`.xlsx`, `.xls`), valeurs séparées par des virgules (`.csv`) et valeurs séparées par des tabulations (`.tsv`). 
- **Onglets multi-feuilles** : les classeurs comportant plusieurs feuilles comportent une barre d'onglets inférieure (`QTabBar`), permettant une commutation rapide entre les feuilles de données. 
- **Modèle de table virtuelle (`VirtualSpreadsheetModel`)** : utilise le chargement de lignes incrémentiel paresseux via `canFetchMore` et `fetchMore`. Vous pouvez faire défiler des fichiers CSV ou des feuilles de calcul contenant des centaines de milliers de lignes en douceur avec une empreinte mémoire minimale. 
- **En-têtes de colonnes et de lignes figés** : les coordonnées standard de la feuille de calcul (`A, B, C...` et `1, 2, 3...`) restent épinglées pendant le défilement pour une orientation claire. 
- **Exportation TSV du Presse-papiers** : sélectionnez n'importe quelle plage de cellules et appuyez sur **`Cmd+C`** (`⌘C`) pour copier les données formatées sous forme de valeurs propres séparées par des tabulations, prêtes à être collées dans le code, Slack ou les tuyaux de terminal. 
- **Recherche rapide** : appuyez sur `Cmd+F` pour rechercher le contenu des cellules dans toutes les colonnes avec le focus cellulaire en temps réel.

#### 3.2.2 Navigateur de base de données SQLite (`SqlitePanel`)

Inspectez les bases de données SQLite (`.sqlite`, `.sqlite3`, `.db`) directement sans clients GUI externes : 

- **Répertoire des tables et des vues** : la barre latérale gauche répertorie toutes les tables et vues de la base de données ainsi que leur nombre de lignes actives. Cliquer sur n’importe quelle table charge immédiatement son contenu. 
- **Vue des données virtualisées** : utilise le `VirtualSpreadsheetModel` hautes performances pour un défilement transparent à travers des tableaux volumineux. 
- **Console de requêtes SQL interactive** : saisissez des requêtes SQL personnalisées dans l'éditeur de requêtes supérieur et appuyez sur **`Ctrl+Return`** (ou `Cmd+Return`) pour les exécuter. Les résultats s’affichent instantanément dans la vue tableau. 
- **Formatage du type de données** : gère les données en toute sécurité : formate les blobs binaires en `<BLOB: N B>` et affiche les champs vides en italique `NULL`. 
- **Exporter les données** : cliquez avec le bouton droit pour copier les enregistrements sélectionnés ou exporter les résultats de la requête au format CSV ou TSV.

#### 3.2.3 Carnets Jupyter (`NotebookPanel`)

Examinez les expériences de science des données, les exécutions de machine learning et les blocs-notes d'analyse Python (`.ipynb`) : 

- **Rendu natif sans serveur** : analyse les structures de notebook JSON complètement hors ligne sans nécessiter un démon de serveur Jupyter ou JupyterLab actif. 
- **Disposition des cellules basée sur une carte** : 
- *Cellules Markdown* : rendu dans une typographie épurée avec des titres, du texte en gras et des listes. 
- *Cellules de code* : formaté avec du code Python, des numéros de ligne et des badges d'exécution de cellule avec une syntaxe mise en évidence (par exemple `[1]`, `[14]`). 
- *Blocs de sortie* : affiche les flux de sortie de la console, les traces d'erreurs et les tableaux et graphiques encodés en base64 en ligne (PNG/SVG).

#### 3.2.4 Affichage du code et du texte brut (`TextPanel`)

Le moteur principal d'inspection de texte est optimisé pour une navigation rapide et d'énormes vidages de données : 

- **Chargeur fragmenté de 64 Ko (`FileLoaderWorker`)** : lit les fichiers volumineux en blocs de 64 Ko avec capture automatique des limites de nouvelle ligne, empêchant le gel des threads et la corruption des caractères multioctets UTF-8. 
- **Mise en évidence de la syntaxe Pygments** : plus de 150 langages de programmation et de configuration pris en charge avec une adaptation dynamique du mode Clair/Sombre. 
- **Sélecteur d'encodage dynamique** : détection statistique du jeu de caractères (`chardet`) avec commutation manuelle de la barre d'état entre UTF-8, GB18030, Big5, Shift-JIS, Windows-1252 et ISO-8859-1. 
- **Mode Live Tail (`F5`)** : engagez `FileTailWatcher` pour diffuser les lignes de journal ajoutées en temps réel, correspondant à UNIX `tail -f`. Appuyez à nouveau sur `F5` pour faire une pause.

#### 3.2.5 Inspection des octets hexadécimaux bruts (`2` / Mode hexadécimal)

Lors de l'inspection de fichiers binaires, de dumps de micrologiciels, de bibliothèques compilées ou de fichiers corrompus : 

- **Grille hexadécimale de 16 octets** : affiche les adresses de décalage hexadécimal à 8 chiffres, 16 octets hexadécimaux répartis en deux colonnes visuelles de 8 octets et le texte ASCII imprimable sur la droite (`.` pour les octets de contrôle). 
- **Détection automatique Hex** : si des octets nuls (`\x00`) sont détectés dans le premier Ko d'un fichier, ATBCmder passe automatiquement en mode Hex pour éviter toute confusion du terminal. 

---

### 3.3 Domaine 3 : Actifs multimédias et système

ATBCmder comprend des lecteurs multimédias accélérés par le matériel, des visionneuses graphiques et des inspecteurs de typographie intégrés directement au noyau.

#### 3.3.1 Visionneuse d'images (`ImagePanel`)

Appuyez sur `F3` sur n'importe quel format d'image pris en charge (`.png`, `.jpg`, `.webp`, `.svg`, `.gif`, `.bmp`, `.ico`, `.tiff`) : 

![Image Viewer](images/image_viewer_window.png) 
*Figure 4.3 : Visionneuse d'images intégrée avec zoom interactif sur le canevas, rotation et extraction de métadonnées EXIF.* 

- **Toile interactive** : zoom fluide avec la molette de la souris ancré à la position du curseur (`SmoothPixmapTransform`), inspection 1:1 des pixels, ajustement à la fenêtre et panoramique par glissement manuel. 
- **EXIF Telemetry Inspector** : cliquez sur **EXIF Info** pour extraire les métadonnées de l'appareil photo : marque, modèle, distance focale de l'objectif, temps d'exposition, ouverture, ISO et coordonnées GPS. 
- **Scène de transparence en damier (`CheckerboardScene`)** : les canaux alpha transparents dans les images PNG, WebP et SVG sont rendus sur une grille en damier gris et blanc standard de l'industrie.

#### 3.3.2 Lecteur audio et mode de lecture en arrière-plan (`AudioPlayerDialog`)

Écoutez des podcasts, des effets sonores ou des collections de musique pendant que vous travaillez : 

![Audio Player](images/audio_player.png) 
*Figure 4.4 : Lecteur audio intégré avec analyse des balises ID3, pochettes d'album et gestion des listes de lecture par glisser-déposer.* 

- **Formats pris en charge** : MP3, FLAC, WAV, AAC, M4A, OGG et AIFF avec balise mutagène ID3 et extraction des illustrations de couverture. 
- **Mode de lecture en arrière-plan** : cliquez sur le bouton **Arrière-plan** dans le lecteur. La fenêtre du lecteur s'ancre dans un **mini-contrôleur de lecteur** compact dans la barre d'opérations en arrière-plan du panneau de droite (`bg_ops_container`) : 
- Affiche le titre et l'artiste de la piste en cours de lecture. 
- Boutons de lecture interactifs : Précédent (`⏮`), Lecture/Pause (`▶` / `⏸`) et Suivant (`⏭`). 
- La musique est diffusée sans interruption pendant que vous parcourez les fichiers, exécutez des renommages par lots ou synchronisez des dossiers. 
- Appuyer sur `F3` sur des fichiers audio supplémentaires dans le panneau de fichiers les ajoute automatiquement à la liste de lecture en cours ! 

![Music Player in Panel](images/music_player_window.png) 
*Figure 4.5 : Mini-lecteur d'arrière-plan intégré directement dans la barre d'opérations du panneau.*

#### 3.3.3 Lecteur vidéo à accélération matérielle (`MediaPanel`)

Pour les fichiers vidéo (`.mp4`, `.mkv`, `.mov`, `.avi`, `.webm`) : 

![Video Player](images/video_player_window.png) 
*Figure 4.6 : Lecteur vidéo à accélération matérielle avec commandes d'affichage à l'écran flottant (OSD).* 

- **Décodage sans surcharge** : optimisé par `QtMultimedia` utilisant macOS VideoToolbox et l'accélération GPU Apple Silicon. 
- **Contrôles OSD à fondu automatique** : le curseur de chronologie flottant, le curseur de volume et les commandes de lecture disparaissent pendant la lecture. 
- **Commutation de sous-titres et de pistes** : basculez entre les flux audio intégrés et les fichiers de sous-titres externes (`.srt`, `.vtt`). 
- **Mode plein écran** : appuyez sur **`F11`** ou double-cliquez pour passer en mode plein écran ; appuyez sur `Esc` pour revenir.

#### 3.3.4 Inspecteur de typographie de police (`FontPanel`)

Aperçu du système et des polices de conception (`.ttf`, `.otf`, `.woff`, `.woff2`, `.ttc`) : 

- **Aperçus de la taille de la cascade** : affiche le texte d'aperçu dans des tailles de points de conception standard : 12, 16, 20, 24, 32, 48 et 64 pt. 
- **Chaîne de test personnalisée** : saisissez des chaînes personnalisées pour tester le crénage et la ponctuation de caractères spécifiques. 
- **Pangrammes bilingues** : l'aperçu par défaut affiche des pangrammes bilingues complets : *"Le renard brun rapide saute par-dessus le chien paresseux 1234567890 敏捷的棕狐跃过懒狗"*. 

---

### 3.4 Domaine 4 : Archives système et communications

#### 3.4.1 Inspecteur d'archives dans la liste (`ArchivePanel`)

Tout en appuyant sur `Enter` ouvre les archives directement dans le panneau des fichiers via Archive VFS, en appuyant sur **`F3`** sur une archive (`.zip`, `.tar`, `.7z`, `.tar.gz`, `.tar.bz2`, `.tar.xz`) ouvre l'**Archive Inspector** : 

- Inspectez les hiérarchies de répertoires internes, le nombre de membres, la taille des octets non compressés, la taille des octets compressés et les taux de compression dans une arborescence rapide en lecture seule.

#### 3.4.2 Visionneuse d'archives de courrier électronique (`EmailPanel`)

Pour les communications par courrier électronique enregistrées et les archives de messages (`.eml`, `.msg`) : 

- **Décodage d'en-tête MIME RFC 2047** : décode avec précision les noms des expéditeurs internationaux, les dates, les destinataires CC et les objets des e-mails. 
- **Carte d'en-tête visuelle** : formate les en-têtes d'e-mails dans une carte de métadonnées propre. 
- **Rich Body Toggle** : basculez entre le corps des e-mails HTML formatés et le texte brut. 
- **Extraction de pièces jointes** : répertorie toutes les pièces jointes intégrées avec la taille des fichiers et fournit un bouton **"Enregistrer la pièce jointe sous..."** pour extraire les fichiers directement sur le disque. 

---

## 4. Éditeurs internes : architecture double mode (`F4` / `Fn+F4` / `cm_Edit`)

ATBCmder dispose d'un **moteur de répartition d'éditeur double mode** intelligent : 

- **Lorsque le curseur se trouve sur du texte, du code ou des fichiers de configuration** : appuyer sur `F4` ouvre l'**Éditeur de code interne** (`EditorWindow`). 
- **Lorsque le curseur est sur les fichiers image (`.png`, `.jpg`, `.webp`, `.bmp`, `.svg`)** : appuyer sur `F4` lance automatiquement **l'éditeur d'images dédié** (`ImageEditorDialog`) ! 

Pour créer et modifier un tout nouveau fichier à partir de zéro dans le dossier actif, appuyez sur **`Shift+F4`** (`cm_EditNew`). ATBCmder vous demande un nom de fichier (par exemple `deploy.sh` ou `docker-compose.yml`), initialise le fichier et l'ouvre immédiatement dans l'éditeur. 

---

### 4.1 Éditeur de code interne (`EditorWindow`)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Edit: /Users/brain/Projects/atbcmder/scripts/deploy.sh [*]                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [💾 Save] [Save As] | [↶ Undo] [↷ Redo] | [🔍 Find] [Replace] | [Wrap] [Lines] [Zoom]   │
├──────┬─────────────────────────────────────────────────────────────────────────────────┤
│ 0001 │ #!/usr/bin/env bash                                                             │
│ 0002 │ set -euo pipefail                                                               │
│ 0003 │                                                                                 │
│ 0004 │ echo "Deploying ATBCmder release bundle..."                                     │
│ 0005 │ TARGET_DIR="/opt/atbcmder"                                                      │
│ 0006 │ if [ ! -d "$TARGET_DIR" ]; then                                                 │
│ 0007 │     mkdir -p "$TARGET_DIR"                                                      │
│ 0008 │ fi                                                                              │
├──────┴─────────────────────────────────────────────────────────────────────────────────┤
│  Find: [deploy                  ]  Replace: [release                  ] [Match 1 of 3] │
│  [Aa] Match Case   [\b] Whole Word   [.*] RegEx   [Find Next] [Replace] [Replace All]  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Line 5, Col 12 | 8 lines | UTF-8 | LF (UNIX) | Bash Shell | [Modified *]              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Capacités principales de l'éditeur de code

- **Mise en évidence de la syntaxe Pygments** : reconnaît plus de 150 formats de programmation, de script et de configuration avec détection automatique de la langue à partir des extensions de fichiers et des lignes shebang. 
- **Gouttière de numéro de ligne dynamique** : la marge gauche s'agrandit dynamiquement pour accueillir les numéros de ligne avec alignement visuel. 
- **Indentation automatique intelligente et retrait de bloc** : appuyer sur `Enter` fait avancer les espaces d'indentation ; sélectionnez les blocs et appuyez sur `Tab` pour mettre en retrait ou `Shift+Tab` pour annuler le retrait. 
- **Soft Word Wrap (`Alt+W` / `⌥W`)** : enveloppe les longues lignes aux limites de la fenêtre sans insérer de sauts de ligne définitifs. 
- **Contrôles de zoom** : mettez à l'échelle la typographie sans effort à l'aide de `Cmd++` (`⌘+`), `Cmd+-` (`⌘-`) ou réinitialisez-la avec `Cmd+0` (`⌘0`).

#### Barre interactive de recherche et de remplacement (`EditorReplaceBar`)

Appuyer sur **`Cmd+F`** (`⌘F`) ou **`Cmd+Option+F`** (`⌥⌘F`) ancre la barre Rechercher et remplacer en bas : 

- Recherche incrémentielle en temps réel avec indexation des occurrences (`Match 4 of 19`). 
- Indicateurs de recherche : sensible à la casse (`[Aa]`), mot entier (`[\b]`) et expressions régulières Python (`[.*]`). 
- Actions par lots : **Remplacer** (occurrence actuelle) et **Remplacer tout** (document entier).

#### Barre d'état et protection de sauvegarde atomique

- **Télémétrie** : affiche la ligne, la colonne, le nombre total de lignes, l'encodage et la convention de nouvelle ligne (`LF` vs `CRLF`). 
- **Dirty State Badge** : un indicateur `*` bien visible apparaît dans la barre de titre et la barre d'état chaque fois que des modifications non enregistrées existent. 
- **Atomic Save Protection** : lorsque vous appuyez sur `Cmd+S`, ATBCmder écrit les données dans un fichier temporaire sur le même volume, synchronise les tampons de disque et exécute un remplacement atomique, garantissant que votre fichier d'origine ne sera jamais corrompu en cas de crash ou de coupure de courant en cours de sauvegarde. 

---

### 4.2 Éditeur d'images dédié (`ImageEditorDialog`)

Lorsque vous appuyez sur **`F4`** sur un graphique ou une capture d'écran, ATBCmder ouvre l'**Image Editor** complet :

#### Canevas interactif et transformations

- **Arrière-plan en damier (`CheckerboardScene`)** : les graphiques transparents sont rendus sur une grille grise et blanche épurée, garantissant que les bordures alpha sont clairement visibles. 
- **Rotation et retournement** : faites pivoter de 90° dans le sens des aiguilles d'une montre/dans le sens inverse des aiguilles d'une montre, affinez les angles de nivellement arbitraires ou effectuez un miroir horizontalement et verticalement. 
- **Zoom et panoramique** : zoom fluide avec suivi du curseur et navigation par glisser-déplacer.

#### Recadrage avec des préréglages de rapport hauteur/largeur

- Faites glisser les poignées du canevas pour définir les limites du recadrage. 
- Basculez entre les formats **Freeform**, **1:1 Square** (avatars/icônes d'application), **4:3 Classic** et **16:9 Cinema**. Appuyez sur `Enter` pour postuler.

#### Annotations vectorielles

- **Rectangles et cercles** : mettez en surbrillance les éléments de l'interface avec des largeurs de bordure et des couleurs de palette personnalisées. 
- **Flèches directionnelles** : dessinez des flèches de légende vectorielles pointues. 
- **Stylo à main levée** : dessinez des corrections ou des signatures à main levée directement sur la toile. 
- **Tampons de texte** : ajoutez une typographie avec des polices, des tailles, des couleurs et des ombres portées subtiles.

#### Rédaction de confidentialité (mosaïque / flou)

Besoin de partager une capture d'écran contenant des jetons confidentiels, des noms de clients ou des numéros de téléphone ? 

- Sélectionnez l'outil **Mosaïque / Flou**. 
- Faites glisser une zone de sélection sur les informations sensibles. 
- ATBCmder applique une pixellisation à rayon variable ou un flou gaussien, expurgeant en toute sécurité les données sensibles avant l'exportation.

#### Module de filigrane

Appliquez une image de marque de propriété professionnelle à l'aide de 4 emplacements prédéfinis : 

- **Carrelage (`tiled`)** : motif de filigrane incliné et répétitif couvrant toute la toile (idéal pour les brouillons confidentiels). 
- **Tampon (`stamp`)** : Tampon d'authentification distinct placé dans le coin inférieur droit. 
- **Bannière (`banner`)** : bannière de marque horizontale semi-transparente s'étendant sur la toile. 
- **Logo unique (`single`)** : logo unique ou filigrane de texte librement positionnable avec curseur d'opacité. 

---

### 4.3 Édition VFS aller-retour transparente (à distance et archives)

L'aspect le plus puissant du sous-système éditeur d'ATBCmder est son **intégration VFS universelle** : 

- Que vous appuyiez sur `F4` sur un script shell stocké sur un serveur SFTP distant, un fichier de configuration dans un montage AWS Nextcloud WebDAV ou une capture d'écran dans une archive `.zip` imbriquée (`vfs://`) : 
1. ATBCmder télécharge le fichier de manière asynchrone dans un bac à sable temporaire sécurisé. 
2. Le fichier s'ouvre dans `EditorWindow` ou `ImageEditorDialog`. 
3. Lorsque vous appuyez sur `Cmd+S`, ATBCmder intercepte l'événement de sauvegarde, synchronise le fichier modifié et diffuse automatiquement les données mises à jour via SFTP/SMB ou engage `RepackWorker` pour reconditionner l'archive ! 
4. À la fermeture de l'éditeur, les fichiers de cache temporaires sont nettoyés proprement. Vous n’aurez jamais besoin de décompresser, modifier et télécharger à nouveau manuellement des fichiers. 

---

## 5. ⚡ Conseils de pro et plongée approfondie

Maîtrisez ces fonctionnalités avancées pour maximiser votre efficacité d’inspection et d’édition.

### Conseil de pro 1 : Ingestion de file d'attente audio dynamique avec `F3`

Lorsque le lecteur audio s'exécute en **mode de lecture en arrière-plan** lorsque vous parcourez votre collection musicale, vous n'avez pas besoin de rouvrir la boîte de dialogue pour mettre davantage de musique en file d'attente : 

1. Mettez en surbrillance un ou plusieurs fichiers audio dans l'un ou l'autre panneau de fichiers. 
2. Appuyez sur **`F3`** (ou `Fn+F3`). 
3. ATBCmder détecte qu'une instance de lecteur audio est déjà active et **ajoute automatiquement les pistes sélectionnées** à la liste de lecture en cours (`append_tracks`) sans interrompre la piste en cours de lecture.

### Conseil de pro 2 : associations de fichiers personnalisées (`cm_FileAssoc`)

Par défaut, appuyer sur `F3` ouvre le listeur universel et `F4` ouvre l'éditeur de code interne. Cependant, vous pouvez mapper des extensions de fichiers spécifiques à des applications de bureau externes ou à des commandes shell personnalisées à l'aide du **File Associations Manager** (`cm_FileAssoc`) : 

Accédez à **Configuration ➔ Configuration des associations de fichiers** : 

- Vous pouvez mapper des extensions (par exemple `*.rs`, `*.py`, `*.psd`) à des actions personnalisées. 
- **Commandes internes** : liées aux actions du commandant interne (par exemple `cm_View`, `cm_Edit`). 
- **Commandes Shell externes avec substitution de jetons** : 
- `%f` ➔ Remplacé par le chemin absolu du fichier (par exemple `/Users/brain/main.rs`). 
- `%d` ➔ Remplacé par le chemin du répertoire parent (par exemple `/Users/brain`). 
- `%n` ➔ Remplacé par le nom du fichier sans extension (ex. `main`). 
- `%e` ➔ Remplacé par l'extension du fichier sans point (ex. `rs`). 

*Exemple d'association externe pour les fichiers Rust :* 
```bash
code --goto %f
```

### Conseil de pro 3 : mode Live Tail (`F5`) pour les journaux DevOps

Lors du débogage de démons de serveur local, de conteneurs Docker ou de scripts de build, ouvrez le fichier journal dans Universal Lister (`F3`) et appuyez sur **`F5`** : 

- Engage le démon `FileTailWatcher`. 
- Lister défile automatiquement vers le bas et diffuse les lignes nouvellement ajoutées à l'écran en temps réel, correspondant au comportement d'UNIX `tail -f`. 
- Vous pouvez garder les filtres de recherche actifs pendant la recherche pour mettre en évidence les erreurs au fur et à mesure qu'elles se produisent.

### Conseil de pro 4 : Streaming décalé arbitraire pour les fichiers de plusieurs gigaoctets

Si vous devez inspecter un vidage de base de données ou une image disque de 20 Go, n'essayez pas de l'ouvrir dans un éditeur standard. Dans le Lister universel d’ATBCmder : 

- Utilisez **Aller à la ligne (`Ctrl+G`)** ou sautez les commandes du curseur. 
- Le `FileLoaderWorker` sous-jacent utilise la recherche directe de pointeur de fichier binaire (`fh.seek(offset)`), en lisant uniquement le bloc exact de 64 Ko requis pour restituer la vue. 
- Vous pouvez inspecter instantanément des secteurs arbitraires d'un volume de plusieurs téraoctets sans aucune surcharge de mémoire. 

---

## 6. Recettes pratiques étape par étape

### Recette 1 : Inspecter et rédiger une capture d'écran sensible

**Objectif** : vous avez capturé une capture d'écran contenant des jetons d'API confidentiels ou des informations client et devez la rédiger avant de la télécharger sur un outil de suivi des problèmes public. 

```
Step 1: Highlight screenshot.png in the active panel and press F3 (Universal Lister).
Step 2: On the top toolbar, click "Edit Image" to launch the Image Editor.
Step 3: Select the "Mosaic / Blur" tool from the tool palette.
Step 4: Click and drag a selection rectangle over the API token to pixelate the text.
Step 5: Select the "Crop" tool, frame the relevant portion of the window, and press Enter.
Step 6: Click "Save" (Cmd+S) to overwrite, or "Save As" to create screenshot_redacted.png.
Step 7: Press Esc to close the editor; your clean image is ready in the file panel.
```
 

---

### Recette 2 : Surveillance des journaux en direct et inspection médico-légale hexadécimale

**Objectif** : un processus en arrière-plan échoue avec une erreur d'encodage. Vous devez regarder le journal en direct et inspecter les octets bruts autour d'une séquence mal formée. 

```
Step 1: Highlight server.log in the active panel and press F3.
Step 2: Press F5 to activate Tail Mode. Watch incoming live log entries stream past.
Step 3: When the error appears, press F5 again to pause tailing.
Step 4: Press Ctrl+F and search for the error code (e.g. "0xEF").
Step 5: Press 2 on your keyboard to switch into Hex Mode.
Step 6: Inspect the exact 16-byte hexadecimal dump to examine unprintable control characters.
Step 7: Press 1 to return to formatted text mode, or Esc to close.
```
 

---

### Recette 3 : Création rapide de code source et mise en scène Git

**Objectif** : créez un nouveau script shell dans le référentiel de votre projet actuel, configurez les en-têtes bash standard et préparez-le pour son exécution sans quitter ATBCmder. 

```
Step 1: In the active directory, press Shift+F4 (cm_EditNew).
Step 2: In the dialog prompt, type "build_release.sh" and press Enter.
Step 3: The Internal Code Editor opens immediately with an empty buffer.
Step 4: Type your script. Notice that auto-indent automatically indents loops and if-blocks:
        #!/usr/bin/env bash
        set -euo pipefail
        echo "Building binaries..."
Step 5: Press Cmd+S (⌘S) to save the file atomically to disk.
Step 6: Press Cmd+W (⌘W) to close the editor.
Step 7: With build_release.sh highlighted in the panel, press Alt+Enter (cm_SetFileProperties).
Step 8: Check the "Execute" permission for Owner (chmod +x) and press Enter.
```
 

---

## 7. Alertes de sécurité et de système

> [!WARNING] 
> **Observateurs de modifications externes** 
> Si un fichier ouvert est modifié ou tronqué par une application externe pendant que vous travaillez dans l'éditeur interne (`F4`), ATBCmder affiche un avertissement de conflit de modification externe avant de l'enregistrer. Choisissez toujours **Recharger** pour inspecter la dernière version du disque ou **Enregistrer sous** pour conserver vos modifications locales dans un fichier séparé. 

> [!IMPORTANT] 
> **Sécurité des fichiers binaires : mode texte ou mode hexadécimal** 
> L'ouverture d'un fichier binaire inconnu en mode texte et sa sauvegarde sur le disque peuvent corrompre définitivement le fichier en raison des remplacements du décodage UTF-8 (`\ufffd`). Le Lister universel d'ATBCmder est en lecture seule par défaut, garantissant que vos fichiers binaires ne sont jamais écrasés accidentellement lors de l'inspection. 

> [!CAUTION] 
> **Performances d'affichage rapide sur les partages réseau distants** 
> Lorsque vous parcourez des serveurs distants à haute latence (FTP, SFTP ou WebDAV) avec Quick View (`Cmd+Q`) actif, la prévisualisation de fichiers vidéo ou d'archives distants volumineux déclenchera la diffusion à distance. Si la bande passante du réseau est limitée, désactivez Quick View (`Cmd+Q`) pour parcourir les arborescences de répertoires à pleine vitesse. 

> [!TIP] 
> **Accessibilité des touches de fonction macOS** 
> Sur les Apple MacBook et Magic Keyboards modernes, les touches de fonction (`F1`-`F12`) sont mappées par défaut aux commandes matérielles (luminosité, lecture multimédia). Pour déclencher `F3` ou `F4`, maintenez la touche **`Fn`** (par exemple `Fn+F3`, `Fn+F4`). Vous pouvez également activer **"Utiliser les touches F1, F2, etc. comme touches de fonction standard"** dans macOS *Paramètres système ➔ Clavier ➔ Raccourcis clavier clavier ➔ Touches de fonction*. 

---

## 8. Tableau de référence du clavier à double matrice

| Domaine fonctionnel | Description de l'action | Raccourci macOS | Clé de commandant classique | ID de commande | 
| :--- | :--- | :--- | :--- | :--- | 
| **Coup d'œil** | Basculer l'aperçu du panneau opposé | `Cmd+Q` / `⌘Q` | `Ctrl+Q` | `cm_QuickView` | 
| **Coup d'œil** | Panneau de commutation et aperçu inversé | `Tab` / `⇥` | `Tab` | `cm_SwitchPanel` | 
| **Liste** | Ouvrir le fichier dans Universal Lister | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Liste** | Mode d'affichage en texte brut | `1` | `1` | — *(Liste)* | 
| **Liste** | Mode d'affichage hexadécimal brut | `2` | `2` | — *(Liste)* | 
| **Liste** | Basculer le retour à la ligne | `Alt+W` / `⌥W` | `Alt+W` | — *(Liste/Éditeur)* | 
| **Liste** | Basculer les numéros de ligne | `Alt+L` / `⌥L` | `Alt+L` | — *(Liste/Éditeur)* | 
| **Liste** | Basculer le mode de queue de journal en direct | `F5` / `Fn+F5` | `F5` | — *(Liste)* | 
| **Liste** | Fichier précédent dans le répertoire | `P` | `P` | — *(Liste)* | 
| **Liste** | Fichier suivant dans le répertoire | `N` | `N` | — *(Liste)* | 
| **Liste** | Rechercher du texte | `Cmd+F` / `⌘F` | `Ctrl+F` | — *(Liste/Éditeur)* | 
| **Liste** | Accédez au numéro de ligne | `Cmd+G` / `⌘G` | `Ctrl+G` | — *(Liste/Éditeur)* | 
| **Liste** | Ouvrir dans l'application par défaut du système | `Cmd+O` / `⌘O` | `Ctrl+O` | — *(Liste)* | 
| **Liste** | Basculement plein écran | `F11` / `Fn+F11` | `F11` | `cm_FullScreen` | 
| **Éditeur** | Modifier le fichier sélectionné (code / image) | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Éditeur** | Créer et modifier un nouveau fichier | `Shift+F4` / `⇧F4` | `Shift+F4` | `cm_EditNew` | 
| **Éditeur** | Enregistrer le fichier (atomique) | `Cmd+S` / `⌘S` | `Ctrl+S` | — | 
| **Éditeur** | Enregistrer le fichier sous | `Shift+Cmd+S` / `⇧⌘S` | `F12` | — | 
| **Éditeur** | Recharger/Rétablir le fichier | `Cmd+R` / `⌘R` | `Ctrl+R` | — | 
| **Éditeur** | Fermer la fenêtre de l'éditeur | `Cmd+W` / `⌘W` | `Esc` | — | 
| **Éditeur** | Rechercher dans le document | `Cmd+F` / `⌘F` | `Ctrl+F` | — | 
| **Éditeur** | Rechercher et remplacer | `Cmd+Option+F` / `⌥⌘F` | `Ctrl+H` | — | 
| **Éditeur** | Indenter le bloc sélectionné | `Tab` / `⇥` | `Tab` | — | 
| **Éditeur** | Annuler l'indentation du bloc sélectionné | `Shift+Tab` / `⇧⇥` | `Shift+Tab` | — | 
| **Éditeur** | Zoom avant / arrière / Réinitialiser | `⌘+` / `⌘-` / `⌘0` | `Ctrl++` / `Ctrl+-` / `Ctrl+0` | — | 
| **Médias** | Lecture audio en arrière-plan | Cliquez sur `Background` | — | — | 
| **Médias** | Ajouter de l'audio à la liste de lecture | `F3` (lors de la lecture) | `F3` | `cm_View` | 
| **Configuration** | Gestionnaire d'associations de fichiers | Menu de configuration | — | `cm_FileAssoc` |

--- 

<div align="center"> 
<p>Prêt à automatiser des flux de travail complexes et le traitement par lots ?</p> 
<p><strong><a href="power_tools.md">Passer au chapitre 5 : Outils électriques et automatisation &rarr;</a></strong></p> 
</div>