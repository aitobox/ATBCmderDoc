# Chapitre 7: Préférences et personnalisation

Un gestionnaire de fichiers vraiment efficace doit s'adapter à votre flux de travail et ne pas vous obliger à vous adapter à ses paramètres par défaut. Chaque ingénieur, administrateur système, archiviste numérique et professionnel de la création apporte une mémoire musculaire, des exigences d'affichage et des habitudes opérationnelles distinctes : certains s'appuient strictement sur les touches de fonction orthodoxes Norton Commander / Total Commander (`F1`–`F10`), tandis que d'autres s'attendent à des raccourcis macOS natifs (`Cmd+C`, `Cmd+V`, `Cmd+O`); certains exigent un ajustement automatique des colonnes dynamiques avec des métriques typographiques sous-pixels, tandis que d'autres ont besoin de limites de colonnes rigides et fixes ; certains nécessitent une surveillance agressive des événements du système de fichiers en temps réel, tandis que d'autres fonctionnent sur des partages réseau à latence élevée où une interrogation passive est obligatoire. 

ATBCmder est conçu dès le départ pour une configurabilité totale. Grâce à son **boîte de dialogue Préférences** modulaire (`Cmd+,` / `⌘,` / `cm_Options`), son **éditeur de raccourcis clavier** intuitif avec détection de conflits en temps réel, son **moteur d'ajustement automatique de colonnes** intelligent, ses **associations de fichiers** personnalisables avec des macros de jetons externes et ses **ensembles de configuration ZIP** portables. (`cm_ExportConfiguration`), ATBCmder vous permet d'affiner chaque dimension de votre environnement à double panneau et de réaliser votre configuration personnalisée de manière transparente sur tous vos systèmes Mac. 

---

## 1. Démarrage rapide visuel : le centre de préférences et la matrice de commandes

ATBCmder centralise tous les paramètres utilisateur dans une architecture de préférences unifiée composée de 16 pages de configuration spécialisées, d'un moteur de mappage de raccourcis clavier isolé et d'une couche de stockage XML atomique. 

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

### Aide-mémoire sur les préférences et la personnalisation de la double matrice

| Actions | Raccourci macOS | Clé de commandant classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Ouvrir les préférences** | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | Ouvre la boîte de dialogue principale Préférences multipage. | 
| **Configurer les raccourcis clavier** | `Cmd+,` ➔ Raccourcis clavier clavier | — | `cm_Options` (raccourcis clavier) | Accès direct au tableau de liaison des raccourcis clavier. | 
| **Configurer les associations de fichiers**| Menu : Configuration | — | `cm_FileAssoc` | Mappe les extensions de fichiers vers des visualiseurs/éditeurs internes ou externes. | 
| **Configuration de la liste de véhicules recherchés du répertoire** | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | Modifie les signets des dossiers enregistrés et les raccourcis clavier actifs (`Ctrl+D` pour ouvrir la liste de véhicules recherchés). | 
| **Configurer les onglets favoris** | Menu : Configuration | — | `cm_ConfigFavoriteTabs`| Gère les ensembles d'onglets de dossiers à double panneau enregistrés. | 
| **Configurer les archiveurs** | Menu : Configuration | — | `cm_ConfigArchivers` | Configure les exécutables de l'archiveur externe et les règles de compression. | 
| **Exporter la configuration** | Menu : Configuration | — | `cm_ExportConfiguration`| Exporte tous les fichiers XML de configuration dans un bundle `.zip` portable. | 
| **Importer la configuration** | Menu : Configuration | — | `cm_ImportConfiguration`| Restaure les fichiers XML de configuration à partir d'un bundle `.zip`. | 
| **Ouvrir le répertoire de configuration** | Menu : Configuration | — | `cm_OpenConfigDirectory`| Navigue le panneau actif directement vers le dossier de configuration d'ATBCmder. | 
| **Enregistrer les paramètres immédiatement** | Menu : Configuration | — | `cm_ConfigSaveSettings`| Vide immédiatement toutes les modifications de configuration en mémoire sur le disque. | 
| **Enregistrer la position de la fenêtre** | Menu : Configuration | — | `cm_ConfigSavePos` | Conserve la géométrie actuelle de la fenêtre et les proportions du séparateur. | 
| **Basculer les info-bulles des fichiers** | Préférences : Vues de fichiers | — | *(Préférences)* | Active ou désactive les info-bulles détaillées des métadonnées flottantes. | 
| **Accorder des autorisations système** | Menu : Configuration | — | `cm_GrantFilesystemAccess`| Lance le guide d’intégration de macOS App Sandbox Full Disk Access. | 

---

## 2. La boîte de dialogue Préférences Anatomie et navigation (`Cmd+,` / `cm_Options`)

La salle de contrôle centrale d'ATBCmder est la **boîte de dialogue Préférences**. Vous pouvez l'invoquer à tout moment en appuyant sur **`Cmd+,`** (`⌘,`) sur macOS, en choisissant **ATBCmder ➔ Préférences...** dans le menu de l'application ou en exécutant `cm_Options` via la barre de commande sémantique (`/`).

### 2.1 Disposition des boîtes de dialogue et modèle d'interaction

La boîte de dialogue Préférences utilise une disposition divisée maître-détail conçue pour plus de clarté et d'accessibilité au clavier : 

1. **Liste de navigation par catégorie (à gauche)** : un sélecteur vertical doté d'une police d'interface lisible de 14 points et d'une barre latérale fixe de 195 pixels. Naviguez entre les catégories à l’aide des touches fléchées `Up` et `Down`, ou cliquez avec votre souris. 
2. **Zone de défilement de page empilée (à droite)** : Un vaste panneau de configuration enfermé dans un `QScrollArea` sans cadre. Lorsque vous changez de catégorie, la page de paramètres correspondante apparaît en douceur sans provoquer de redimensionnement de la boîte de dialogue ni de scintillement de la fenêtre. 
3. **Matrice des boutons d'action (en bas)** : 
- **OK** : valide tous les champs de saisie sur toutes les pages, écrit les paramètres modifiés sur le disque (`atbcmder.xml`), déclenche la retraduction et les mises à jour du thème et ferme la boîte de dialogue. 
- **Appliquer** : valide immédiatement tous les paramètres modifiés sans fermer la boîte de dialogue. C'est idéal pour tester les polices de l'interface utilisateur, les variations de thème, le remplissage des colonnes et les intervalles d'actualisation automatique en temps réel. 
- **Annuler** : annule toutes les modifications non enregistrées effectuées dans la session en cours. Si vous avez prévisualisé un thème sans l'appliquer, ATBCmder restaure automatiquement l'interface vers votre thème précédent. 

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

### 2.2 Répertoire complet des pages de configuration

Chaque page de la boîte de dialogue Préférences concerne un domaine fonctionnel spécifique :

| Pages | Module de mise en œuvre | Contrôles de configuration principaux | 
| :--- | :--- | :--- | 
| **Général** | `page_general.py` | Visibilité des fichiers cachés, icônes de fichiers, boîtes de dialogue de confirmation de suppression/écrasement, intégration de la corbeille système, taille du tampon de copie/déplacement (4 Ko à 10 Mo), sélection de thème, taille de police globale, bascule de réduction dans la barre d'état système et raccourci clavier global d'affichage/masquage de la fenêtre (`Cmd+Opt+H`). | 
| **Raccourcis clavier clavier** | `page_hotkeys.py` | Recherche de commandes multi-contextes, liaison d'accords de raccourci principal et secondaire, avertissements de collision de raccourcis automatisés et réinitialisation des paramètres d'usine. | 
| **Langue** | `page_language.py` | Sélecteur de localisation dynamique prenant en charge plus de 30 langues (anglais, allemand, français, chinois simplifié, japonais, russe, espagnol, etc.) avec traduction instantanée de l'interface utilisateur en direct. | 
| **Vues de fichiers** | `page_fileview.py` | Tri numérique naturel et sensible à la casse, positionnement du tri des dossiers (dossiers en premier, fichiers en premier, mixtes), placement des fichiers nouveaux/mis à jour, modes d'ajustement automatique des colonnes (Fixe, Moyenne, Max), curseur de facteur de remplissage et formats datetime personnalisés. | 
| **Actualisation automatique** | `page_auto_refresh.py` | Surveillance de la création/suppression/renommage du système de fichiers, surveillance des modifications d'attributs de fichier, intervalle de repli d'interrogation du minuteur, bascule de désactivation en arrière-plan et liste de filtres d'exclusion de répertoire. | 
| **Opérations** | `page_operations.py` | Politiques de collision de fichiers par défaut (Demander, Écraser, Ignorer, Écraser les anciens, Cible de renommage automatique), politiques de collision de répertoires (Demander, Fusionner, Écraser, Ignorer), pré-allocation d'espace libre, gestion des liens symboliques, préservation des autorisations/horodatage et vérification. | 
| **Emballeur** | `page_packer.py` | Format d'archive de compression par défaut (`zip`, `7z`, `tar.gz`, `tar.bz2`, `tar.xz`, `tar`), chemins d'exécutables externes pour 7-Zip, GNU Tar, Gzip, Utilitaires Bzip2 et XZ. | 
| **Liste de l'annuaire**| `page_hotlist.py` | Gestionnaire de favoris interactif : ajoutez, supprimez et réorganisez (`Drag & Drop`) les répertoires favoris, spécifiez les chemins cibles à double panneau et attribuez des clés d'accès rapide. | 
| **Onglets favoris** | `page_favorite_tabs.py` | Gestionnaire d'instantanés d'espace de travail : enregistrez, renommez, réorganisez et restaurez les dispositions de répertoires multi-onglets à double panneau. | 
| **Éditeur** | `page_editor.py` | Famille de polices de l'éditeur de code interne, taille de police, largeur des taquets de tabulation, retour à la ligne et basculement des numéros de ligne ; Chemin d'accès de l'exécutable de l'éditeur externe et arguments de ligne de commande. | 
| **Visionneuse** | `page_viewer.py` | Typographie de texte Universal Lister, taquets de tabulation, marges, retour à la ligne, visibilité du curseur, options de rendu d'image (rotation automatique EXIF, modes de zoom, grille de transparence) et outil CLI de visualisation externe. | 
| **Barre d'outils** | `page_toolbar.py` | Personnalisation de la barre de boutons supérieure : curseur de taille d'icône (16 à 64 px), curseur de taille de barre, style de bouton plat, bascule de légendes, arborescence de hiérarchie de commandes et boîte de dialogue de sélection d'icônes personnalisée. | 
| **Barre d'outils du milieu** | `page_toolbar.py` | Configuration de la barre d'outils de séparation verticale centrale : tailles des icônes, boutons d'action et réorganisation de la disposition. | 
| **Journal** | `page_log.py` | Journalisation d'audit opérationnel : destination du fichier journal, substitution du chemin du jeton, taille maximale du fichier journal, comportement de rotation des journaux et filtres d'événements d'opération spécifiques (copier, déplacer, supprimer, décompresser). | 
| **Recherche rapide** | `page_quicksearch.py` | Mode de recherche rapide du clavier (correspondance exacte, début, fin, caractères génériques), respect de la casse et délai d'expiration de fermeture automatique. | 
| **Filtre sémantique** | `page_semantic_filter.py` | Comportement de la barre de commandes en langage naturel intégré (`/`), backends du fournisseur de recherche et anti-rebond des suggestions. | 
| **Onglets** | `page_tabs.py` | Apparence des onglets de dossiers : visibilité du bouton de fermeture, disposition des onglets sur plusieurs lignes par rapport aux onglets défilants, comportement de navigation dans les onglets verrouillés et confirmations de fermeture des onglets. |

---

### 2.3 Thème en temps réel et changement de langue dynamique

Contrairement aux utilitaires existants qui nécessitent la fermeture et le redémarrage de l'application après avoir modifié les paramètres d'apparence, ATBCmder propose **Thème et localisation remplaçables à chaud** : 

1. **Aperçus du thème** : ouvrez **Général**, choisissez parmi `Classic`, `Light`, `Dark` ou `macOS Native (Stylish)` et observez instantanément le changement de style de la fenêtre via l'injection de feuille de style Qt. Si vous appuyez sur **Annuler**, le thème précédent est restauré de manière transparente. 
2. **Traduction instantanée** : ouvrez **Langue**, sélectionnez votre dialecte préféré dans la liste de plus de 30 langues traduites, puis cliquez sur **Appliquer**. Le titre de la fenêtre, la barre latérale de catégorie, les menus, les boutons, les barres d'état et les invites de dialogue sont immédiatement restitués dans la langue cible via le pipeline de traduction dynamique `tr()` d'ATBCmder. 

![Language Settings](images/language_settings.png) 
*Figure 7.1 : La page Préférences de langue permettant une localisation instantanée et sans redémarrage dans plus de 30 langues prises en charge.* 

---

## 3. Personnalisation des raccourcis clavier et gestion des conflits

L'efficacité du clavier est la philosophie fondamentale de la gestion de fichiers sur deux panneaux. L'**Hotkey Editor** d'ATBCmder (`page_hotkeys.py`) offre un contrôle total sur les accords de raccourci tout en appliquant une isolation stricte du contexte et une prévention des collisions. 

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

### 3.1 Isolation et portée du contexte

Pour éviter l'épuisement des raccourcis, ATBCmder sépare les combinaisons de touches en **Étendues de contexte**. Un raccourci défini dans un contexte n'interfère pas avec des touches identiques dans des fenêtres non liées : 

- **Principal** : raccourcis d'application globaux disponibles dans toutes les fenêtres (par exemple, `Cmd+,` pour les préférences, `Cmd+Q` pour quitter). 
- **FilePanel** : actif chaque fois que la liste de fichiers de gauche ou de droite a le focus clavier (par exemple, `F5` copies, `Space` calcule la taille du répertoire, `Backspace` accède au parent). 
- **Viewer** : actif dans Universal Lister (`F3`) : contrôle les encodages de texte, les bascules d'affichage hexadécimal (`2` / Hex Mode), le zoom de l'image et la lecture multimédia. 
- **Éditeur** : actif dans l'éditeur de texte intégré (`F4`) : contrôle la coloration syntaxique, l'indentation, la recherche/le remplacement (`Cmd+F`) et l'enregistrement des fichiers (`Cmd+S`). 
- **Différent** : actif à l'intérieur du fichier Diff côte à côte : navigation par morceaux (`F7`/`F8`), synchronisation de ligne et opérations de fusion. 
- **FindFiles** : actif dans la boîte de dialogue de recherche multi-filtres : déclenchement de nouvelles recherches, navigation dans les résultats et alimentation dans la zone de liste. 
- **MultiRename** : Actif dans l'outil Batch Multi-Rename : manipulation du compteur, insertion de jetons et exécution. 

---

### 3.2 Architecture à double liaison (raccourcis primaires et secondaires)

ATBCmder vous permet d'attribuer **deux combinaisons de raccourcis distinctes** à chaque commande : 

- **Raccourci principal** : votre accord de mémoire musculaire principal (par exemple, `F5` pour les utilisateurs de Commander classique). 
- **Raccourci secondaire** : Un accord alternatif (par exemple, `Cmd+C` pour l'ergonomie native de macOS). 

Les deux raccourcis restent actifs simultanément dans le contexte spécifié. Lors de la navigation dans les menus, ATBCmder affiche automatiquement le raccourci principal à côté du texte de l'élément de menu pour une référence visuelle claire. 

---

### 3.3 Recette étape par étape : personnalisation d'un raccourci clavier

Suivez cette procédure pas à pas pratique pour relier une commande existante ou attribuer un raccourci secondaire : 

1. Appuyez sur **`Cmd+,`** (`⌘,`) pour ouvrir les Préférences et sélectionnez **Raccourcis clavier clavier** dans la barre latérale gauche. 
2. Sélectionnez le **Contexte de raccourci clavier** approprié dans la liste déroulante (par exemple, `FilePanel`). 
3. Tapez le nom de la commande ou un mot-clé dans la zone **Commandes de filtre** (par exemple, `Wipe` ou `Terminal`). Le tableau filtre les entrées correspondantes en temps réel. 
4. Double-cliquez sur la ligne de commande ou sélectionnez la ligne et cliquez sur **Modifier...**. 
5. Dans la boîte de dialogue **Modifier le raccourci clavier** : 
- Cliquez à l'intérieur de la zone **Raccourci principal** et appuyez sur la combinaison de touches souhaitée (par exemple, `Ctrl+Alt+T`). ATBCmder capture l'accord proprement, limitant les séquences à un seul accord simultané. 
- (Facultatif) Cliquez à l'intérieur de la zone **Raccourci secondaire** et appuyez sur une combinaison alternative (par exemple, `Cmd+Shift+T`). 
6. Cliquez sur **Enregistrer**. 

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

### 3.4 Détection automatisée des collisions et avertissements de conflit

Si vous tentez d'attribuer un accord clé déjà réclamé par une autre commande dans le même contexte, le moteur de détection de collision d'ATBCmder intervient immédiatement. Une boîte de dialogue d'alerte affiche l'affectation en conflit : 

> [!WARNING] 
> **Conflit de raccourci détecté** 
> Le raccourci `Ctrl+M` est déjà affecté à `cm_MultiRename` dans le contexte `FilePanel`. 
> Voulez-vous l'écraser et réaffecter `Ctrl+M` à `cm_MarkCurrentExtension` ? 

- Cliquer sur **Oui** dissocie automatiquement `Ctrl+M` de l'ancienne commande et l'applique à votre commande nouvellement sélectionnée. 
- Cliquer sur **Non** annule la modification, préservant les liaisons existantes sans modification. 

---

### 3.5 Raccourci global Afficher/Masquer la fenêtre (`Cmd+Opt+H` / `Ctrl+Alt+H`)

Pour les utilisateurs expérimentés qui préfèrent laisser ATBCmder fonctionner discrètement en arrière-plan : 

1. Ouvrez **Préférences ➔ Général**. 
2. Cochez **Réduire dans la barre d'état système**. 
3. Localisez **Afficher/Masquer la touche de raccourci de la fenêtre** (par défaut : `Ctrl+Alt+H` / `⌘⌥H`). 
4. Cliquez sur la zone de séquence pour enregistrer un accord de raccourci clavier global personnalisé. 
5. Cliquez sur **Appliquer**. 

Vous pouvez désormais appeler instantanément ATBCmder au premier plan ou le faire passer en arrière-plan depuis n'importe où dans macOS, même lorsque vous travaillez dans d'autres applications plein écran. 

---

## 4. Vues de fichiers, modes de colonnes et gestion des vignettes

La page **Vues de fichiers** (`page_fileview.py`) régit la façon dont les répertoires sont rendus, mesurés, triés et présentés dans les deux panneaux. 

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

### Moteur d'ajustement automatique de colonne 4.1 : les trois modes

Les gestionnaires de fichiers à double panneau ont souvent du mal à gérer la longueur variable des noms de fichiers : des colonnes trop larges provoquent un défilement horizontal, tandis que des colonnes trop étroites tronquent les extensions de fichiers critiques. ATBCmder résout ce problème avec trois comportements d'ajustement automatique distincts : 

1. **Mode fixe (`fixed`)** : 
- Désactive le recalcul automatique. 
- Les largeurs de colonnes restent exactement là où vous les positionnez. 
- **Glisser manuel** : lorsque vous faites glisser la bordure verticale entre les en-têtes de colonnes (par exemple, entre `Name` et `Ext`), ATBCmder capture la largeur exacte des pixels et la conserve séparément pour chaque côté du panneau (`column_widths_left` et `column_widths_right` dans `atbcmder.xml`). 
2. **Mode moyen (`average` — Valeur par défaut recommandée)** : 
- Évalue la largeur typographique moyenne (`QFontMetrics`) de tous les noms de fichiers visibles dans le répertoire. 
- Multiplie la largeur moyenne par votre **Facteur de rembourrage** configuré (curseur réglable de `1.0x` à `5.0x`, par défaut `1.0x`–`1.25x`), en ajoutant 40 pixels pour les icônes de type de fichier et la marge de manœuvre visuelle. 
- Empêche les noms de fichiers extrêmes (tels qu'un seul nom de fichier journal de 120 caractères) de déplacer toutes les autres colonnes hors de l'écran. 
3. **Mode largeur maximale (`max`)** : 
- Analyse les entrées du répertoire et agrandit la colonne pour qu'elle corresponde au nom de fichier unique le plus large plus un remplissage de sécurité (+50 px). 
- Garantit qu'aucun nom de fichier n'est tronqué avec des points de suspension (`...`), idéal pour les archives multimédias et les ensembles de données scientifiques. 

> [!TIP] 
> **Optimisation de grands annuaires** : 
> Dans des répertoires contenant des dizaines de milliers d'éléments, mesurer chaque chaîne individuelle figerait l'interface. ATBCmder applique automatiquement un échantillonnage par étapes intelligent (`_MAX_SAMPLE = 200`), évaluant un sous-ensemble de lignes uniformément réparti pour calculer les métriques typographiques en moins de 2 millisecondes tout en ignorant les marqueurs du répertoire parent (`..`). 

---

### 4.2 Options de tri des fichiers

Affinez la façon dont les éléments s’ordonnent dans les vues de tableau : 

- **Tri naturel (numérique)** : lorsqu'il est activé, les nombres dans les chaînes sont comparés mathématiquement : `file1.txt`, `file2.txt`, `file10.txt` (au lieu de l'ordre alphabétique `file1.txt`, `file10.txt`, `file2.txt`). 
- **Tri sensible à la casse** : lorsque cette case est cochée, les caractères majuscules précèdent les caractères minuscules selon les valeurs ordinales ASCII/Unicode (`File.txt` trie avant `apple.txt`). Lorsque cette case n'est pas cochée, le tri n'est pas sensible à la casse. 
- **Mode de tri des dossiers** : 
- `Folders first` : Les répertoires sont regroupés en haut du panneau au dessus de tous les fichiers. 
- `Files first` : les fichiers sont répertoriés en premier, avec les répertoires placés en bas. 
- `Mixed` : les fichiers et dossiers sont triés par ordre alphabétique dans une séquence unifiée. 
- **Position des fichiers nouveaux et mis à jour** : contrôlez l'endroit où les fichiers nouvellement créés ou récemment modifiés apparaissent lors des mises à jour en direct du système de fichiers (`Sorted`, `Top` ou `Bottom`). 

---

### 4.3 Affichage de la grille de miniatures et mécanismes de cache

Pour les photographes, les concepteurs et les monteurs vidéo, ATBCmder fournit une **Vue en grille de vignettes** intégrée (`cm_ThumbnailsView`), remplaçant les lignes tabulaires par des aperçus visuels d'images. 

![Thumbnail Grid View](images/thumbnails_grid_view.png) 
*Figure 7.2 : Vue miniature hautes performances affichant des aperçus d'images avec un espacement de grille personnalisé.*

#### Dimensionnement et zoom dynamique

- **Taille de vignette par défaut** : configurable de 48 px à 512 px (par défaut : 128 px). 
- **Pinch-to-Zoom interactif** : sur les trackpads Apple, utilisez les gestes de pincement standard à deux doigts ou maintenez **`Ctrl`** tout en faisant défiler la molette de la souris pour redimensionner les vignettes de manière dynamique en temps réel.

#### Architecture de mise en cache à plusieurs niveaux

La génération de vignettes pour des photos RAW haute résolution de 48 mégapixels ou des SVG vectoriels complexes est gourmande en CPU. ATBCmder utilise une architecture de mise en cache robuste à deux niveaux : 

1. **Cache LRU en mémoire** : conserve 500 objets `QPixmap` décompressés dans la RAM pour un défilement instantané et fluide à 60 ips. 
2. **Cache disque persistant** : stocké localement dans votre répertoire de cache utilisateur : 
- Chemin macOS/Linux : `~/.cache/atbcmder/thumbnails/` 
- Les clés de cache sont générées via des hachages cryptographiques SHA-256 combinant le chemin du fichier, l'horodatage de modification du fichier (`mtime`), la taille de pixel demandée et la version du schéma de cache : 
$$\text{Clé de cache} = \text{SHA256}(\text{filepath} + \text{mtime} + \text{size} + \text{version})$$ 

- Si un fichier image est modifié ou mis à jour sur le disque, son horodatage change, invalidant immédiatement les entrées de cache obsolètes et déclenchant un nouveau rendu automatisé en arrière-plan. 
3. **Thèmes de travail en arrière-plan** : le traitement des images est déchargé vers un pool de travailleurs `QThread` dédié utilisant Pillow (PIL) ou des pipelines `QImage` accélérés par le matériel, garantissant que l'interface à double panneau ne bégaie jamais lors d'importations par lots importantes. 

---

### 4.4 Formatage personnalisé de la date et de l'heure

ATBCmder vous permet de définir des chaînes de formatage d'horodatage personnalisées à l'aide de la syntaxe Python `strftime` standard : 

- **Format date/heure long** (par défaut : `%Y-%m-%d %H:%M:%S`) : contrôle l'affichage de la date dans la vue en colonnes complètes (`2026-09-06 14:30:00`). 
- **Format des répertoires de synchronisation** (par défaut : `%Y.%m.%d %H:%M:%S`) : contrôle la présentation de l'horodatage dans la boîte de dialogue Synchroniseur d'annuaire. 

| Jeton | Descriptif | Exemple de sortie | 
| :--- | :--- | :--- | 
| `%Y` | Année à 4 chiffres | `2026` | 
| `%m` | Mois à 2 chiffres (`01`–`12`) | `09` | 
| `%d` | Jour du mois à 2 chiffres (`01`–`31`) | `06` | 
| `%H` | Heure à 2 chiffres au format 24 heures (`00`–`23`) | `14` | 
| `%I` | Heure à 2 chiffres au format 12 heures (`01`–`12`) | `02` | 
| `%p` | Désignation AM/PM | `PM` | 
| `%M` | Minutes à 2 chiffres (`00`–`59`) | `30` | 
| `%S` | Seconde à 2 chiffres (`00`–`59`) | `15` | 

---

## 5. Actualisation automatique du système de fichiers et sensibilité de surveillance

Lorsque vous collaborez sur des bases de code partagées, téléchargez des ressources de navigateur ou exécutez des tâches de compilation en arrière-plan, le contenu du répertoire change constamment. La page **Auto Refresh** (`page_auto_refresh.py`) équilibre la précision de l'interface utilisateur en temps réel par rapport à la consommation du processeur et de la batterie. 

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

### 5.1 Déclencheurs d'événements et retour d'interrogation

ATBCmder combine la surveillance native des événements du système d'exploitation avec une solution de secours d'interrogation intelligente : 

- **Surveillance des événements (`watch_file_name_change`)** : exploite les notifications natives du noyau du système d'exploitation (macOS `FSEvents` / `kqueue`) pour détecter les créations, suppressions et renommages de fichiers sans aucune surcharge du processeur. 
- **Surveillance des attributs (`watch_attributes_change`)** : suit les extensions de taille de fichier, les mises à jour d'horodatage et les ajustements du mode d'autorisation. 
- **Intervalle de repli d'interrogation (`attr_poll_interval`)** : configurable de 1 à 60 secondes (par défaut : 5 secondes). 
*Pourquoi l'interrogation est-elle nécessaire ?* Les montages de stockage réseau distant (SMB, CIFS, NFS, SFTP VFS) ne parviennent souvent pas à émettre des événements de système de fichiers natifs du système d'exploitation lorsque les clients distants apportent des modifications. La minuterie d'interrogation en arrière-plan garantit que vos listes de panneaux distants ne seront jamais obsolètes. 

---

### 5.2 Conservation de la batterie et du processeur : désactiver en arrière-plan

Sur les ordinateurs portables macOS fonctionnant sur batterie, les observateurs actifs du système de fichiers peuvent consommer inutilement de l’énergie. 

- La vérification de **Lorsque l'application est en arrière-plan** (`watch_only_foreground`) suspend automatiquement tous les minuteurs d'interrogation actifs et les observateurs d'événements au moment où ATBCmder perd le focus de la fenêtre. 
- Lorsque vous revenez à ATBCmder, les panneaux exécutent immédiatement une seule actualisation coordonnée, mettant instantanément à jour toutes les listes de répertoires. 

---

### 5.3 Filtres d'exclusion de chemin

Les répertoires à fort taux de désabonnement, tels que `node_modules`, les référentiels de métadonnées Git (`.git`), les caches d'artefacts de compilation (`target/`, `build/`) et les fichiers de bases de données locales, génèrent des milliers d'événements de disque par minute. 

1. Vérifiez **Les chemins suivants et leurs sous-répertoires** (`watch_exclude_dirs`). 
2. Entrez un chemin de répertoire absolu par ligne dans la zone de texte d'exclusion : 
   ```text
   /Users/username/Developer/project/node_modules
   /Users/username/Developer/linux/.git
   /Volumes/ProductionNAS/RenderingQueue
   ```
 

3. Cliquez sur **Appliquer**. ATBCmder ignore les événements du système de fichiers se produisant dans ces arborescences de chemins, éliminant ainsi les actualisations indésirables de l'interface utilisateur et les pics de processeur. 

---

## 6. Associations de fichiers personnalisées et intégration d'outils externes

Double-cliquer sur un fichier ou appuyer sur **`Enter`** l'ouvre normalement à l'aide de l'application système par défaut. Le **Système d'associations de fichiers** d'ATBCmder (`cm_FileAssoc` / `file_associations.py`) vous permet de définir des actions personnalisées pour des modèles de fichiers spécifiques, en les mappant à des commandes internes ou à des applications de terminal/interface graphique externes.

### 6.1 Architecture et spécificité des modèles

Les associations de fichiers sont évaluées par ordre de spécificité du modèle : le modèle global le plus long et le plus spécifique correspond en premier : 

$$\text{Ordre de spécificité : } \texttt{*.min.js} \longrightarrow \texttt{*.js} \longrightarrow \texttt{text/*} \longrightarrow \texttt{*}$$ 

Chaque association peut contenir plusieurs actions (par exemple, « Ouvrir dans VS Code », « Afficher Hex », « Exécuter en Python »), dont une est désignée comme action principale par défaut déclenchée sur `Enter`. 

---

### 6.2 Substitutions de macros de jetons pour les commandes externes

Lors du lancement d'outils externes ou de scripts de ligne de commande, ATBCmder remplace automatiquement les macros de jetons par les métadonnées du fichier actif : 

| Jeton macro | Signification | Exemple de valeur | 
| :--- | :--- | :--- | 
| **`%f`** | Chemin absolu complet du fichier sélectionné | `/Users/username/Documents/report.pdf` | 
| **`%d`** | Chemin du répertoire contenant le fichier | `/Users/username/Documents` | 
| **`%n`** | Nom de fichier de base sans extension | `report` | 
| **`%e`** | Extension de fichier sans point initial | `pdf` | 

---

### 6.3 Recettes pratiques d'association

#### Recette 1 : ouvrir des scripts Python dans Visual Studio Code

- **Modèle** : `*.py` 
- **Étiquette** : `Edit in VS Code` 
- **Commande** : `code %f` 
- **Type d'action** : commande Shell externe

#### Recette 2 : Exécuter le script Python dans le terminal

- **Modèle** : `*.py` 
- **Étiquette** : `Execute Script` 
- **Commande** : `python3 %f` 
- **Type d'action** : commande Shell externe

#### Recette 3 : Afficher Markdown dans un aperçu dédié

- **Modèle** : `*.md` 
- **Étiquette** : `Preview in Typora` 
- **Commande** : `open -a Typora %f` 
- **Type d'action** : commande Shell externe

#### Recette 4 : Comparer le fichier avec le panneau opposé dans Beyond Compare

- **Modèle** : `*` 
- **Étiquette** : `Compare with Target` 
- **Commande** : `bcomp %f %d` 
- **Type d'action** : commande Shell externe 

---

## 7. Personnalisation de la barre d’outils et de la barre d’outils centrale

ATBCmder fournit deux barres d'outils personnalisables : la **Barre d'outils principale** située sous la barre de menus et la **Barre d'outils intermédiaire** intégrée verticalement dans le séparateur séparant les deux panneaux de fichiers. 

![Middle Toolbar](images/middle_toolbar.png) 
*Figure 7.3 : La page d'options de la barre d'outils centrale configurant les boutons de séparation et les déclencheurs d'action rapide.*

### 7.1 Personnalisation de l'apparence de la barre d'outils

Ouvrez **Préférences ➔ Barre d'outils** ou **Préférences ➔ Barre d'outils centrale** : 

- **Curseur de taille de barre** : Ajuste la hauteur/largeur de la barre d'outils de 16 px à 64 px. 
- **Curseur de taille d'icône** : met à l'échelle les icônes des boutons de 16 px à 64 px (par défaut : 24 px). 
- **Boutons plats** : bascule entre les boutons plats modernes sans bordure et les boutons classiques en relief. 
- **Afficher les légendes** : affiche les étiquettes de texte sous ou à côté des icônes de la barre d'outils. 

---

### 7.2 Ajout d'éléments et du sélecteur d'icônes intégré

Les éléments de la barre d'outils sont organisés dans une arborescence hiérarchique prenant en charge trois types d'éléments : 

1. **Séparateur** : insère une ligne de séparation visuelle ou un espaceur entre les groupes de boutons. 
2. **Commande interne** : sélectionnez l'une des plus de 230 commandes `cm_*` d'ATBCmder à l'aide du champ de commande à saisie semi-automatique. 
3. **Commande externe** : spécifiez une commande shell externe, un répertoire de travail et des jetons de paramètres (`%f`, `%d`).

#### Le sélecteur d'icônes intégré (`IconPickerDialog`)

Lors de la configuration des boutons personnalisés, cliquez sur le bouton d'aperçu de l'icône pour ouvrir le **Sélecteur d'icônes** intégré : 

- Comprend un filtre de recherche instantané sur des centaines d'icônes SVG et PNG regroupées. 
- Affiche les icônes dans une grille uniforme avec un aperçu haute résolution et des noms de tiges d'actifs. 

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

### 7.3 Personnalisation de la liste de véhicules recherchés et des onglets favoris du répertoire

- **Liste d'annuaire (`page_hotlist.py`)** : gérez vos favoris `Ctrl+D`. Ajoutez les chemins actuels, réorganisez les signets par glisser-déposer, configurez la synchronisation du panneau cible et attribuez des clés d'accès. 
- **Onglets favoris (`page_favorite_tabs.py`)** : enregistrez les dispositions complètes de l'espace de travail multi-onglets à deux panneaux. Restaurez vos ensembles exacts de répertoires de développement ou de retouche photo en un clic. 

![Directory Hotlist](images/quick_access_paths.png) 
*Figure 7.4 : Gestion des signets et des chemins d'accès aux listes de véhicules recherchés du répertoire.* 

---

## 8. Portabilité de la configuration et mode de test isolé

Qu'il s'agisse de migrer vers un nouveau Mac, de provisionner une flotte de machines de développement ou de partager des raccourcis clavier personnalisés avec des collègues, ATBCmder simplifie la sauvegarde et le déploiement de la configuration.

### 8.1 Architecture de stockage de configuration

ATBCmder stocke tous les paramètres utilisateur dans des fichiers XML clairement structurés et lisibles par l'homme situés dans le répertoire de configuration standard de votre système d'exploitation : 

- **Chemin standard macOS** : 
`~/Library/Préférences/atbcmder/` 

- **Chemin du bac à sable de l'application macOS** : 
`~/Library/Containers/com.aitobox.atbcmder/Data/Library/Préférences/atbcmder/` 

- **Chemin Linux / UNIX** : 
`~/.config/atbcmder/` 

- **Commande d'accès direct** : 
Exécutez **`cm_OpenConfigDirectory`** (ou choisissez **Configuration ➔ Ouvrir le répertoire de configuration** dans le menu) pour naviguer instantanément dans le panneau actif directement vers ce dossier. 

```
~/Library/Preferences/atbcmder/
├── atbcmder.xml          # Core application configuration, geometry, themes, view rules
├── atbcmder_hotkeys.xml  # User keyboard shortcut overrides and custom bindings
├── favtabs.xml           # Saved favorite folder tab layouts and paths
├── hotlist.xml           # Directory Hotlist (Ctrl+D) bookmarks hierarchy
└── history.xml           # Recent directory jumps, command line history, search history
```
 

---

### 8.2 Exportation des ensembles de configuration (`cm_ExportConfiguration`)

Pour créer une sauvegarde portable tout-en-un de votre environnement ATBCmder : 

1. Choisissez **Configuration ➔ Exporter la configuration...** dans la barre de menu (ou exécutez `cm_ExportConfiguration`). 
2. Sélectionnez votre répertoire de destination et choisissez un nom de fichier (par défaut : `atbcmder-config.zip`). 
3. Cliquez sur **Enregistrer**. 

ATBCmder vide toutes les modifications de mémoire en attente sur le disque, rassemble tous les fichiers XML de configuration (`atbcmder.xml`, `atbcmder_hotkeys.xml`, `favtabs.xml`, `hotlist.xml`) et les regroupe dans une archive ZIP atomique et compressée. 

---

### 8.3 Importation de groupes de configuration (`cm_ImportConfiguration`)

Pour restaurer une sauvegarde de configuration sur une nouvelle machine ou revenir à un bon état connu : 

1. Choisissez **Configuration ➔ Importer la configuration...** dans la barre de menu (ou exécutez `cm_ImportConfiguration`). 
2. Sélectionnez votre archive `atbcmder-config.zip` précédemment exportée. 
3. Confirmez l'invite d'avertissement : 
> L'importation remplacera tous les paramètres actuels par le contenu du fichier sélectionné. Continuer? 
4. Cliquez sur **Oui**. 

ATBCmder décompresse l'archive en toute sécurité, vérifie que tous les fichiers extraits sont des configurations XML valides, remplace les fichiers de disque actifs, recharge le singleton interne `Config()` et actualise immédiatement les panneaux de fichiers et la disposition des colonnes, le tout sans nécessiter un redémarrage de l'application. 

> [!IMPORTANT] 
> **Sécurité d'entreprise : protection anti-traversée** 
> ATBCmder applique une validation stricte de la traversée du chemin lors de l'importation de la configuration (assainissement `zipfile`). Tout membre d'archive contenant des séparateurs de chemin (`/`, `\`), des traversées de répertoires (`..`) ou des extensions de fichiers non XML est immédiatement rejeté, protégeant ainsi votre système d'exploitation contre la falsification malveillante des archives. 

---

### 8.4 Mode de test isolé (`ATBCmder_test.sh`)

Lorsque vous développez des plugins personnalisés, expérimentez des raccourcis clavier agressifs ou testez des configurations bêta, vous devez éviter de modifier la configuration quotidienne de votre pilote. 

ATBCmder prend en charge la redirection complète de la configuration via la variable d'environnement `ATBCMDER_CONFIG_PATH`. Un script de test dédié est inclus dans le référentiel du projet : 

```bash
# Launch ATBCmder in completely isolated test mode:
./scripts/ATBCmder_test.sh
```

#### Comment fonctionne le mode test isolé :

1. Provisionne un répertoire de test propre et temporaire à `tests/.test_config/`. 
2. Copie les paramètres de base d'usine de `src/atbcmder/resources/test_config.xml` vers `tests/.test_config/atbcmder.xml`. 
3. Définit `export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"`. 
4. Génère ATBCmder en Python. Tout paramètre modifié ou supprimé au cours de la session affecte uniquement le répertoire de test temporaire, laissant vos fichiers personnels `~/Library/Préférences/atbcmder/` 100 % intacts. 

---

## 9. ⚡ Conseils de pro et plongée approfondie : personnalisation avancée

### Conseil de pro 1 : Approvisionnement automatisé de Dotfile via Chezmoi / Ansible

Étant donné qu'ATBCmder sérialise tous les états dans des fichiers XML UTF-8 standard, vous pouvez vérifier votre configuration dans un référentiel Git dotfiles et la gérer via des outils comme Chezmoi, GNU Stow ou Ansible : 

```bash
# Example: Adding ATBCmder configuration to Chezmoi dotfiles manager
chezmoi add ~/Library/Preferences/atbcmder/atbcmder.xml
chezmoi add ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml
```

### Conseil de pro 2 : Optimisation de l'observateur de réseau hautes performances

Lorsque vous travaillez sur des serveurs de fichiers SMB/NFS d'entreprise contenant des millions de fichiers, la surveillance active et récursive des événements peut provoquer une congestion du réseau. 

1. Ouvrez **Préférences ➔ Actualisation automatique**. 
2. Décochez **Lorsque la taille, la date ou les attributs changent**. 
3. Définissez **Intervalle d'interrogation** sur `15` ou `30` secondes. 
4. Ajoutez la racine de montage réseau (`/Volumes/EnterpriseShare`) à la **Liste d'exclusion de chemin**. 
5. Utilisez l'actualisation manuelle du panneau (**`Ctrl+R`** / `⌘R`) lorsqu'une synchronisation immédiate est requise.

### Conseil de pro 3 : Variables d'environnement de commande externe

Lors de la configuration de boutons de barre d'outils externes personnalisés ou d'associations de fichiers, ATBCmder hérite automatiquement de votre environnement shell utilisateur (`PATH`, `HOME`, `USER`). Vous pouvez appeler directement les utilitaires de ligne de commande installés via Homebrew (`/opt/homebrew/bin/`) sans fournir de chemins exécutables absolus complets.

### Conseil de pro 4 : Configuration des info-bulles de fichiers flottants

ATBCmder comprend de riches info-bulles de métadonnées flottantes qui affichent les dimensions des fichiers, les données EXIF, le débit audio et le nombre de membres d'archive lorsque vous survolez les éléments. Vous pouvez activer ou désactiver les info-bulles dans **Préférences ➔ Vues de fichiers**. 

![Helpful Tooltips](images/helpful_tooltips.png) 
*Figure 7.5 : Info-bulles de métadonnées riches affichant les propriétés détaillées du fichier au survol de la souris.* 

---

## 10. Alertes de sécurité et de système

> [!CAUTION] 
> **Vérification d'écrasement des raccourcis** 
> L'écrasement d'un raccourci principal dans le contexte `Main` ou `FilePanel` le dissocie immédiatement de la commande d'origine. Si vous dissociez accidentellement des commandes essentielles telles que `F5` (Copier) ou `Enter` (Ouvrir), utilisez le bouton **Réinitialiser les paramètres par défaut** dans l'éditeur de raccourcis clavier pour restaurer les raccourcis clavier d'usine. 

> [!WARNING] 
> **L'importation de configuration remplace tous les paramètres** 
> La restauration d'un ensemble de configuration via `cm_ImportConfiguration` écrase complètement vos fichiers `atbcmder.xml`, `favtabs.xml` et `hotlist.xml` actuels. Exportez toujours une sauvegarde de votre configuration existante avant d'importer une archive externe. 

> [!IMPORTANT] 
> **MacOS App Sandbox et accès complet au disque** 
> Si ATBCmder s'exécute sous macOS App Sandbox, il ne peut pas lire les fichiers de configuration ou les répertoires en dehors de son conteneur sans l'autorisation explicite de l'utilisateur. Si vous rencontrez des erreurs d'autorisation lors de l'accès aux disques externes, exécutez **`cm_GrantFilesystemAccess`** pour terminer le flux d'intégration de l'accès complet au disque macOS. 

---

## 11. Référence des commandes de personnalisation et de préférences de Master Dual-Matrix

| Catégorie | Description de l'action | Raccourci macOS | Clé de commandant classique | ID de commande | 
| :--- | :--- | :--- | :--- | :--- | 
| **Préférences** | Ouvrir la boîte de dialogue Préférences principales | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | 
| **Préférences** | Enregistrer les paramètres au format XML maintenant | Menu : Configuration | — | `cm_ConfigSaveSettings` | 
| **Préférences** | Enregistrer la position et la taille de la fenêtre | Menu : Configuration | — | `cm_ConfigSavePos` | 
| **Préférences** | Basculer les info-bulles des fichiers | Préférences ➔ Vues de fichiers | — | *(Préférences)* | 
| **Préférences** | Accorder des autorisations complètes sur le disque | Menu : Configuration | — | `cm_GrantFilesystemAccess` | 
| **Raccourcis clavier clavier** | Ouvrir la page de l'éditeur de raccourcis clavier | `Cmd+,` ➔ Raccourcis clavier clavier | — | `cm_Options` | 
| **Raccourcis clavier clavier** | Raccourci global Afficher/Masquer la fenêtre | `Ctrl+Alt+H` / `⌘⌥H` | `Ctrl+Alt+H` | *(Touche de raccourci système global)* | 
| **Associations** | Gestionnaire d'associations de fichiers ouverts | Menu : Configuration | — | `cm_FileAssoc` | 
| **Signets** | Gestionnaire de liste de véhicules recherchés de l'annuaire | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| **Signets** | Ajouter le répertoire actuel à la liste de véhicules recherchés | Menu : Favoris | — | `cm_AddDirToHotlist` | 
| **Onglets de dossier** | Gestionnaire d'onglets de dossiers favoris | Menu : Configuration | — | `cm_ConfigFavoriteTabs` | 
| **Onglets de dossier** | Enregistrer les onglets actuels en tant qu'ensemble de favoris | Menu : Onglets | — | `cm_SaveFavoriteTabs` | 
| **Archiveurs** | Configurer les binaires de l'archiveur | Menu : Configuration | — | `cm_ConfigArchivers` | 
| **Portabilité** | Exporter la configuration vers ZIP | Menu : Configuration | — | `cm_ExportConfiguration` | 
| **Portabilité** | Importer la configuration depuis ZIP | Menu : Configuration | — | `cm_ImportConfiguration` | 
| **Portabilité** | Ouvrir le dossier de configuration | Menu : Configuration | — | `cm_OpenConfigDirectory` | 
| **Modes d'affichage** | Basculer l'affichage de la grille de vignettes | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| **Modes d'affichage** | Actualiser la liste des panneaux actifs | `Ctrl+R` / `⌃R` | `Ctrl+R` | `cm_Refresh` |

--- 

<div align="center"> 
<p>Prêt à maîtriser tous les raccourcis clavier et matrices de commandes dans l'ensemble de l'application ?</p> 
<p><strong><a href="keyboard_shortcuts.md">Passez au chapitre 8 : Raccourcis clavier clavier principal &rarr;</a></strong></p> 
</div>