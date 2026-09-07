# Chapitre 2: Navigation et onglets de dossiers

Un mouvement fluide et rapide dans les répertoires est la pierre angulaire de la gestion orthodoxe des fichiers. Dans ATBCmder, vous n'aurez jamais à perdre de temps à faire glisser les barres de défilement, à cliquer à plusieurs reprises sur des dossiers imbriqués ou à vous battre avec des dizaines de fenêtres du Finder fragmentées. 

Ce chapitre couvre tout ce dont vous avez besoin pour naviguer dans les systèmes de fichiers locaux et distants en toute confiance : fil d'Ariane interactif, sauts dans la hiérarchie des claviers, flux de travail multi-onglets natifs de macOS, espaces de travail persistants à deux panneaux d'onglets Favoris, signets de recherche floue instantanés et cinq modes d'affichage de panneaux spécialisés. 

---

## 1. Démarrage rapide visuel : hiérarchie et organisation spatiale sans effort

Dans ATBCmder, chaque panneau fonctionne comme un moteur de navigation autonome équipé de sa propre chaîne de fil d'Ariane, d'une bande d'onglets indépendante, d'une pile d'historique et de modes d'affichage. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [BREADCRUMB]  🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [TAB STRIP]   [★ Source (Locked)] [Assets] [Build Output] [+]                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Name                         Ext       Size      Date Modified      Attr       │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Today, 14:22       drwxr-xr-x │
│  ▸ ui                         <DIR>               Today, 15:05       drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Today, 15:10       -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Yesterday, 19:40   -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [QUICK SEARCH]  🔍 Find: mai_   (Matches: main.py)                              │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Aide-mémoire de navigation à double matrice

| Actions | Raccourci macOS | Clé de commandant classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Répertoire des parents** | `Backspace` / `⌘↑` | `Ctrl+PgUp` | `cm_ChangeDirToParent` | Remontez d’un niveau de répertoire (`..`). | 
| **Répertoire racine** | `Ctrl+\` / `⌃\` | `\` | `cm_ChangeDirToRoot` | Accédez directement à la racine du système (`/`). | 
| **Répertoire personnel** | `Ctrl+Shift+Home` / `⌃⇧Home` | `Alt+Home` | `cm_ChangeDirToHome` | Accédez au répertoire personnel de l'utilisateur (`~`). | 
| **Ouvrir l'élément/Entrer le répertoire** | `Enter` / `⌘↓` | `Enter` | — | Entrez le répertoire sélectionné ou ouvrez le fichier. | 
| **Nouvel onglet** | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | Ouvrez le dossier actif dans un nouvel onglet. | 
| **Fermer l'onglet** | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | Fermez l'onglet actuellement ciblé. | 
| **Liste chaude de l'annuaire** | `Ctrl+D` / `⌃D` | `Ctrl+D` | `cm_DirHotList` | Ouvrez une fenêtre contextuelle de signet floue instantanée. | 
| **Historique Retour** | `Cmd+[` / `⌘[` | `Alt+Left` | `cm_ViewHistoryPrev` | Revenez au dossier précédemment visité. | 
| **Histoire en avant** | `Cmd+]` / `⌘]` | `Alt+Right` | `cm_ViewHistoryNext` | Avancer dans l’historique du répertoire. | 
| **Liste déroulante de l'historique** | `Alt+F8` / `⌥F8` | `Ctrl+Down` | `cm_DirHistory` | Afficher la liste déroulante de l'historique. | 
| **Liste des lecteurs/volumes (gauche/droite)** | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | `cm_LeftOpenDrives` / `cm_RightOpenDrives` (`cm_Drives`) | Ouvrez le menu du lecteur pour le panneau gauche ou droit (`Alt+D` pour le panneau actif). | 
| **Recherche rapide** | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_QuickSearch` | Ouvrez la superposition de recherche en temps réel dans le panneau. | 

---

## 2. Navigation de base dans le répertoire : chemins, fils d'Ariane et raccourcis

ATBCmder vous offre plusieurs façons redondantes et ergonomiques de vous déplacer dans votre système de fichiers, que vous préfériez les gestes de la souris, les clics sur le trackpad ou la vitesse pure du clavier.

### Navigation avec la souris et le trackpad

- **Saisie des dossiers** : double-cliquez sur n'importe quelle ligne du répertoire ou appuyez sur `Enter` (`Return`). 
- **Hiérarchies ascendantes** : double-cliquez sur la ligne supérieure `[..]` pour accéder immédiatement au dossier parent. 
- **Onglets d'arrière-plan** : cliquez avec le bouton central sur n'importe quelle ligne de dossier pour ouvrir ce répertoire dans un nouvel onglet d'arrière-plan sans perdre votre vue actuelle (`cm_OpenDirInNewTab`).

### Barre de fil d'Ariane interactive de style Finder

Positionnée directement au-dessus de chaque panneau de fichiers, la barre de fil d'Ariane interactive représente votre chemin UNIX actuel sous la forme d'une chaîne de segments cliquables : 

```
🏠 / ▸ Users ▸ brain ▸ Projects ▸ ATBCmder ▸ docs
```
 

1. **Instant Ancestor Leaping** : cliquez sur n'importe quel segment d'ancêtre (tel que `Projects` ou `Users`) pour accéder directement à ce niveau, en contournant les navigations dans plusieurs dossiers parents. 
2. **Menu déroulant des répertoires frères et sœurs** : passez la souris sur ou cliquez sur le chevron (`▸`) entre les segments pour afficher un menu déroulant répertoriant tous les dossiers frères à ce niveau hiérarchique. Cliquez sur n’importe quel frère pour y accéder directement. 
3. **Utilitaires contextuels** : cliquez avec le bouton droit sur n'importe quel segment de fil d'Ariane pour appeler un menu contextuel dédié : 
- **Ouvrir dans un nouvel onglet** : ouvre ce dossier ancêtre spécifique dans un nouvel onglet. 
- **Révéler dans le Finder** : ouvre le répertoire dans le Finder natif de macOS (`open -R`). 
- **Copier le chemin** : copie le chemin UNIX absolu du segment dans votre presse-papiers macOS. 
- **Ouvrir dans le terminal** : génère une fenêtre de terminal dans ce répertoire exact. 
4. **Édition de texte par chemin direct (`BreadcrumbLineEdit`)** : 
- Double-cliquez sur l'espace vide à droite du fil d'Ariane (ou appuyez sur `Shift+F2`). 
- Les segments du fil d'Ariane se transforment instantanément en un champ de texte modifiable (`QLineEdit`). 
- Tapez ou collez des chemins arbitraires (tels que `~/Library/Application Support`, `/var/log`, `/Volumes/ExternalDrive` ou `vfs://` emplacements d'archives). 
- Appuyez sur `Enter` pour sauter, ou sur `Esc` pour annuler et revenir aux boutons de fil d'Ariane.

### Sauts rapides du clavier

Gardez la main sur la ligne d'accueil avec ces commandes de navigation dédiées : 

- **Répertoire parent (`Backspace` / `⌘↑` / `Ctrl+PgUp` / `cm_ChangeDirToParent`)** : remonte instantanément vers le répertoire parent. Lorsque vous montez, ATBCmder positionne automatiquement le curseur sur le dossier que vous venez de quitter, vous assurant de ne jamais perdre votre place. 
- **Répertoire racine (`Ctrl+\` / `cm_ChangeDirToRoot`)** : accède directement à la racine de votre volume de démarrage macOS (`/`). 
- **Répertoire personnel (`Ctrl+Shift+Home` / `cm_ChangeDirToHome`)** : permet d'accéder directement au répertoire personnel de votre utilisateur (`/Users/username` ou `~`). 
- **Première et dernière entrée** : appuyez sur `Home` (`cm_GoToFirst`) pour placer le curseur sur l'entrée supérieure (`..`), ou `End` (`cm_GoToLast`) pour accéder au fichier final dans le panneau actuel. 

---

## 3. Onglets de dossier : multitâche dans chaque panneau

Travailler sur des projets logiciels complexes, des photothèques ou des sauvegardes de serveur nécessite souvent de jongler avec plusieurs dossiers simultanément. Plutôt que d'ouvrir des dizaines de fenêtres, ATBCmder intègre des bandes multi-onglets indépendantes pour les deux panneaux. 

![Folder Tabs and Splitters](images/quick_access_paths.png) 
*Gestion multi-onglets et navigation rapide dans ATBCmder*

### Conception native de la barre d'onglets macOS

Construite avec `MacNativeTabBar`, la barre d'onglets correspond à l'esthétique moderne de macOS : 

- **Conception visuelle** : coins des onglets arrondis, états de survol fluides et indicateurs d'accentuation des onglets actifs clairs. 
- **Boutons de fermeture en survol** : chaque onglet comporte un bouton de fermeture `✕` intégré qui apparaît lors du survol ou de la sélection. 
- **Clic du milieu pour fermer** : cliquez sur n'importe quel onglet avec le bouton central de votre souris/cliquez avec trois doigts sur le trackpad pour le fermer immédiatement. 
- **Double-cliquez pour ajouter** : double-cliquez sur un espace vide sur la bande d'onglets pour générer instantanément un nouvel onglet cloné à partir du chemin actif.

### Opérations sur les onglets et raccourcis clavier

| Actions | Raccourci macOS | Clé classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Nouvel onglet** | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | Ouvre le répertoire actuel dans un nouvel onglet. | 
| **Fermer l'onglet** | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | Ferme l'onglet actif (minimum 1 onglet conservé). | 
| **Onglet suivant** | `Ctrl+Tab` / `⌃⇥` | `Ctrl+Tab` | `cm_NextTab` | Les cycles se concentrent sur l'onglet suivant à droite. | 
| **Onglet précédent** | `Ctrl+Shift+Tab` / `⌃⇧⇥` | `Ctrl+Shift+Tab` | `cm_PrevTab` | Les cycles se concentrent sur l'onglet précédent à gauche. | 
| **Liste d'onglets rapides** | `Ctrl+Shift+L` / `⌃⇧L` | `Ctrl+Shift+L` | `cm_ShowTabsList` | Affiche un menu numéroté de tous les onglets ouverts. | 
| **Onglet Renommer** | *Clic droit sur l'onglet* | — | `cm_RenameTab` | Attribue une étiquette conviviale personnalisée à l’onglet. | 
| **Fermer les autres onglets** | *Clic droit sur l'onglet* | — | `cm_CloseOtherTabs` | Ferme tous les onglets sauf celui sélectionné. | 
| **Fermer les doublons** | *Clic droit sur l'onglet* | — | `cm_CloseDuplicateTabs` | Détecte et ferme les onglets en double avec des chemins identiques. | 
| **Fermer tous les onglets** | *Onglets de menu* | — | `cm_CloseAllTabs` | Réinitialise le panneau à un seul onglet. | 
| **Copier ci-contre** | *Onglets de menu* | — | `cm_CopyAllTabsToOpposite` | Copie tous les onglets du panneau actif vers le panneau cible. |

### Modes de verrouillage des onglets

Empêchez les modifications accidentelles de répertoire dans les dossiers critiques en configurant les options de verrouillage des onglets. Cliquez avec le bouton droit sur n'importe quel onglet pour choisir son mode de verrouillage : 

1. **Normal (déverrouillé)** : 
- Comportement des onglets par défaut. 
- La navigation dans les dossiers met directement à jour le chemin de l'onglet actuel. 
2. **Verrouillé (`cmd_SetTabOptionLock`)** : 
- Le chemin de l'onglet est strictement figé à son emplacement d'ancrage initial. 
- Une icône de verrouillage visuel (`🔒` ou `★`) apparaît sur le titre de l'onglet. 
- Si vous double-cliquez sur un sous-répertoire ou naviguez, ATBCmder laisse automatiquement l'onglet verrouillé inchangé et ouvre le dossier cible dans un **nouvel onglet adjacent**. 
3. **Verrouillé avec sous-répertoires autorisés (`cmd_SetTabOptionLockWithSubdirs`)** : 
- Vous permet de parcourir librement les dossiers et sous-répertoires enfants de cette arborescence. 
- Vous empêche de monter plus haut que le dossier de base verrouillé. 
- Si vous quittez ou rechargez, l'onglet se réinitialise en toute sécurité à sa racine d'ancrage. 

---

## 4. Onglets favoris : espaces de travail nommés à double panneau

Alors que les onglets individuels offrent une flexibilité locale, les **onglets favoris** vous permettent de capturer et de restaurer des environnements opérationnels complets à deux panneaux en une seule commande. 

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
 

Un ensemble d'onglets Favoris encapsule : 

- Tous les onglets ouverts dans le panneau de gauche (y compris les chemins et les états de verrouillage). 
- Tous les onglets ouverts dans le panneau de droite (y compris les chemins et les états de verrouillage). 
- La sélection d'onglets actifs pour les deux panneaux.

### Commandes des onglets favoris

- **Enregistrer les onglets actuels (`cm_SaveFavoriteTabs`)** : 
- Accessible via le menu **Favoris** → **Enregistrer les onglets actuels dans de nouveaux onglets favoris**, ou en cliquant avec le bouton droit sur la bande d'onglets. 
- Vous invite à nommer l'espace de travail (par exemple, `Rust Web Backend`, `Photo Editing 2026` ou `Server Deployment`). 
- Stocke la définition de l'espace de travail de manière persistante dans `fav_tab_config.xml`. 
- **Charger les onglets favoris (`cm_LoadFavoriteTabs`)** : 
- Accessible via Menu **Favoris** → **Charger les onglets à partir des onglets Favoris**. 
- Ouvre une boîte de dialogue modale répertoriant vos jeux d'onglets enregistrés. Sélectionnez un ensemble et les deux panneaux reconstruisent immédiatement la disposition complète à plusieurs onglets. 
- **Réenregistrer les onglets favoris (`cm_ResaveFavoriteTabs`)** : 
- Met à jour l'espace de travail actuellement actif avec tous les onglets nouvellement ouverts, fermés ou parcourus sans demander un nouveau nom. 
- **Recharger les onglets favoris (`cm_ReloadFavoriteTabs`)** : 
- Ramène les deux panneaux à l'état propre et enregistré de l'espace de travail actif, en supprimant tous les onglets exploratoires ouverts pendant la session. 
- **Espaces de travail de cycle (onglets favoris suivant/précédent)** : 
- Basculez rapidement entre les différents espaces de travail de projet enregistrés de manière séquentielle à partir du menu Favoris. 
- **Configuration (`cm_ConfigFavoriteTabs`)** : 
- Ouvrez **Préférences** → **Onglets favoris** pour réorganiser les ensembles, renommer les espaces de travail, modifier manuellement les chemins d'onglets individuels ou supprimer les ensembles obsolètes. 

---

## 5. Listes de favoris de l'annuaire (signets)

La **Directory Hotlist** offre un accès global et instantané à vos dossiers les plus fréquemment utilisés sur les lecteurs locaux, les disques externes et les montages réseau distants. 

![Directory Hotlist](images/quick_access_paths.png) 

* Fenêtre contextuelle de la liste de favoris de l'annuaire avec recherche floue en temps réel *

### Fenêtre contextuelle de liste de véhicules recherchés instantanée (`Ctrl+D` / `⌃D` / `cm_DirHotList`)

Appuyer sur `Ctrl+D` fait apparaître une boîte de dialogue de recherche légère et flottante centrée juste sous vos yeux : 

1. **Recherche floue en temps réel** : 
- Commencez à taper immédiatement. La barre de recherche filtre tous vos noms de signets et chemins cibles en temps réel. 
- Par exemple, taper `down` correspond instantanément à `Downloads — /Users/username/Downloads`. 
2. **Parcours du clavier** : 
- Utilisez les touches fléchées `Up` et `Down` pour mettre en surbrillance le signet souhaité. 
- Appuyez sur `Enter` pour naviguer dans le panneau actif directement vers ce chemin. 
- Appuyez sur `Esc` pour fermer la fenêtre contextuelle sans modifier votre répertoire. 
3. **Création rapide de signets** : 
- Cliquez sur le bouton **Ajouter le répertoire actuel** (ou appuyez sur `Alt+A`) dans la fenêtre contextuelle. 
- ATBCmder remplit automatiquement le chemin du dossier actuel et suggère un nom d'affichage propre.

### Configuration de la liste de véhicules recherchés (`Ctrl+Shift+D` / `⌃⇧D` / `cm_ConfigDirHotList`)

Ouvrez **Préférences** → **Répertoire Hotlist** (ou déclenchez `cm_ConfigDirHotList`) pour organiser vos favoris : 

- **Hierarchical Sub-Menus**: Group related bookmarks into categories (e.g. `Work`, `Personal`, `Cloud Storage`, `Network Shares`).
 - **Étiquettes d'affichage personnalisées** : attribuez des noms conviviaux tels que `Work Documents` au lieu de longs chemins comme `/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Work`. 
- **Réorganisation par glisser-déposer** : réorganisez l'ordre des signets pour conserver les répertoires prioritaires tout en haut de votre liste. 

---

## 6. Historique et lecteurs : navigation dans le temps et les volumes de stockage

ATBCmder maintient une piste d'audit complète de vos sessions de navigation, vous permettant de retracer vos étapes sur le stockage local et les volumes montés.

### Historique de navigation

Chaque panneau enregistre sa propre pile d'historique de cheminement chronologique : 

- **Retour (`Cmd+[` / `⌘[` ou `Alt+Left` / `cm_ViewHistoryPrev`)** : recule d'un pas dans l'historique du chemin du panneau actif. 
- **Avant (`Cmd+]` / `⌘]` ou `Alt+Right` / `cm_ViewHistoryNext`)** : avance d'un pas après un retour en arrière. 
- **Popup historique de l'annuaire (`Alt+F8` / `⌥F8` ou `Ctrl+Down` / `⌃↓` / `cm_DirHistory`)** : 
- Affiche un menu contextuel déroulant affichant les 20+ derniers répertoires visités dans le panneau actif. 
- Cliquez ou faites glisser la flèche vers le bas sur n'importe quel répertoire précédent pour y accéder directement, en sautant les pressions répétitives sur Retour.

### Sélecteur de lecteur et de volume

Sur macOS, toutes les partitions internes, les lecteurs externes USB-C/Thunderbolt, les DMG montés et les partages réseau résident sous `/Volumes`. ATBCmder fournit des commandes dédiées pour basculer entre ces cibles : 

![Drive and Volume Switcher Menu](images/driver_select.png) 
*Lecteur monté instantanément et sélecteur de volume déclenché via Alt+F1 (panneau gauche), Alt+F2 (panneau droit) ou Alt+D* 

- **Sélecteur de lecteur du panneau gauche (`Alt+F1` / `⌥F1` / `cm_LeftOpenDrives`)** : raccourci principal du Commander classique qui ouvre le menu de sélection du lecteur et du volume ciblant le panneau de gauche. 
- **Sélecteur de lecteur du panneau droit (`Alt+F2` / `⌥F2` / `cm_RightOpenDrives`)** : raccourci principal de Classic Commander qui ouvre le menu de sélection de lecteur et de volume ciblant le panneau droit. 
- **Menu Active Panel Drive (`Alt+D` / `⌥D` / `cm_Drives`)** : ouvre un menu contextuel répertoriant tous les volumes montés, le système de fichiers racine `/`, l'accueil de l'utilisateur `~` et les points de terminaison du réseau connectés pour le panneau actuellement ciblé. 

> [!NOTE] 
> **Autorisations des lecteurs externes macOS** : lors de la première navigation vers des disques externes sous `/Volumes`, macOS App Sandbox peut vous demander l'autorisation. ATBCmder affichera une boîte de dialogue d'autorisation pour créer un signet persistant à portée de sécurité pour ce lecteur. 

---

## 7. Modes d'affichage du panneau : personnalisation de l'affichage

ATBCmder propose 5 modes d'affichage spécialisés conçus pour optimiser l'espace d'écran et la densité des informations pour différents flux de travail de gestion de fichiers.

### 1. Vue complète des colonnes (`Ctrl+F2` / `⌃F2` / `cm_ColumnsView`)

Le mode d'affichage standard et le plus complet. Il affiche les fichiers dans un format tabulaire riche avec des en-têtes configurables : 

| Colonne | Descriptif | Alignement | 
| :--- | :--- | :--- | 
| **Nom** | Nom du fichier ou du répertoire avec icône de type macOS natif. | Gauche | 
| **Poste** | Extension de fichier (par exemple, `py`, `png`, `zip`). | Gauche | 
| **Taille** | Taille formatée (B, Ko, Mo, Go). Les dossiers affichent `<DIR>`. | Droite | 
| **Date de modification** | Horodatage formaté selon les paramètres régionaux de macOS. | Gauche | 
| **Attributs** | Autorisations UNIX (octales `0755` et symboliques `rwxr-xr-x`). | Centre | 
| **Propriétaire / Groupe** | Noms de propriété des utilisateurs et des groupes UNIX. | Gauche | 

- **Tri des en-têtes** : cliquez sur n'importe quel en-tête de colonne pour basculer entre l'ordre de tri croissant ou décroissant. Cliquez avec `Cmd` enfoncé pour effectuer un tri secondaire.

### 2. Brève vue (`Ctrl+F1` / `⌃F1` / `cm_BriefView`)

Brief View supprime les colonnes de métadonnées, organisant les fichiers en plusieurs colonnes verticales compactes qui remplissent toute la largeur du panneau. 

- **Navigation haute densité** : affiche simultanément 3 à 5 fois plus d'éléments à l'écran. 
- **Meilleur pour** : analyse rapide de grandes listes de répertoires (telles que les polices, les photos ou les archives de journaux) où il vous suffit d'identifier les noms de fichiers.

### 3. Affichage des vignettes (`Ctrl+Shift+F1` / `⌃⇧F1` / `cm_ThumbnailsView`)

La vue Miniatures convertit la liste de fichiers en une grille d'images et d'icônes multimédias. 

![Thumbnails View](images/thumbnails_grid_view.png) 
*Vue miniature affichant des aperçus multimédias dans le panneau actif* 

- **Médias pris en charge** : aperçus instantanés des photos (JPEG, PNG, HEIC, TIFF, WebP, GIF), des formats vectoriels (SVG), des documents PDF et des vignettes vidéo (MP4, MOV, MKV). 
- **Génération d'arrière-plan asynchrone** : le rendu des vignettes se produit dans les threads d'arrière-plan sans bloquer l'interaction de l'utilisateur. 
- **Taille réglable** : configurez la taille des icônes miniatures (de 64 px à 256 px) dans **Préférences** → **Vues de fichiers**.

### 4. Vue arborescente (`cm_TreeView`, `cm_TreeViewSplit`, `cm_TreeViewBoth`)

L'arborescence affiche une arborescence de répertoires hiérarchique extensible, ce qui facilite la compréhension des structures de dossiers approfondies en un coup d'œil. 

![Tree View and Thumbnails View](images/treeview+thumbview.png) 
*Tree View intégré aux listes de fichiers et aux miniatures* 

ATBCmder prend en charge trois présentations d'arborescence distinctes via le menu **Afficher** : 

- **Arborescence (Remplacer) (`cm_TreeView`)** : La table de fichiers du panneau actif est entièrement remplacée par une arborescence de répertoires extensible. 
- **Tree View (Split) (`cm_TreeViewSplit`)** : Le panneau actif est divisé verticalement en deux sous-volets : une arborescence de répertoires à gauche et la liste de fichiers standard pour le dossier d'arborescence sélectionné à droite. 
- **Arborescence (les deux panneaux) (`cm_TreeViewBoth`)** : Active l'arborescence de répertoires divisée dans les panneaux gauche et droit simultanément. 
- **Afficher les fichiers** : cliquez avec le bouton droit dans l'arborescence et activez **Afficher les fichiers** pour choisir si les fichiers doivent être affichés dans l'arborescence à côté des répertoires ou masqués pour afficher uniquement les répertoires.

### 5. Branche/Vue plate (`Cmd+B` / `⌘B` ou `Ctrl+B` / `⌃B` / `cm_FlatView`)

Flat View (également connu sous le nom de Branch View) est l'une des fonctionnalités les plus puissantes d'ATBCmder. Il parcourt de manière récursive tous les sous-répertoires et sous-dossiers du dossier actuel, aplatissant tous les fichiers imbriqués dans une **seule liste unifiée**. 

![Branch View](images/branch_view.png) 
*Vue de branche plate (`Cmd+B`) affichant le contenu imbriqué dans tous les sous-répertoires* 

- **La colonne Chemin** : en vue plate, ATBCmder ajoute automatiquement une colonne **Chemin** indiquant le chemin relatif du dossier imbriqué de chaque fichier (par exemple, `assets/icons/` ou `src/core/`). 
- **Tri global** : Triez simultanément tous les fichiers imbriqués dans l'ensemble de l'arborescence du projet par taille, date de modification ou extension de fichier. 
- **Traitement par lots** : sélectionnez des fichiers provenant d'une douzaine de sous-répertoires différents et copiez, déplacez, comparez ou renommez-les tous en même temps. 
- **Streaming Traversal** : ATBCmder diffuse progressivement les résultats de recherche dans la vue à l'aide de travailleurs en arrière-plan, garantissant ainsi que les grands projets (avec des dizaines de milliers de fichiers imbriqués) se chargent en douceur sans geler l'interface utilisateur. 
- **Quick Exit** : Appuyez à nouveau sur `Cmd+B` (`Ctrl+B`) pour quitter la vue plate et revenir à la vue normale du répertoire hiérarchique. 

---

## 8. ⚡ Conseils de pro et plongée approfondie : contrôle de précision

Pour les utilisateurs avancés et les claviéristes expérimentés, ATBCmder propose un réglage précis et des mécanismes de recherche rapide.

### Superposition de recherche rapide dans le panneau (`Ctrl+S` / `⌃S` / `cm_QuickSearch`)

La recherche rapide vous permet d'accéder directement à n'importe quel fichier en tapant son nom sans ouvrir une boîte de dialogue de recherche complète. 

```
┌─────────────────────────────────────────────────────────────────┐
│  main.py            py      8.4 KB    Today, 15:10   -rw-r--r-- │
│  main_window.py     py     72.1 KB    Today, 15:18   -rw-r--r-- │
├─────────────────────────────────────────────────────────────────┤
│ 🔍 Quick Search: main_                 [ Next: ↓ ] [ Prev: ↑ ]  │
└─────────────────────────────────────────────────────────────────┘
```
 

1. **Recherche incrémentielle** : 
- Appuyez sur `Ctrl+S` (ou commencez simplement à taper si configuré dans les Préférences). 
- Une barre de superposition apparaît ancrée en bas du panneau actif. 
- Au fur et à mesure que vous tapez des caractères, le curseur du panneau passe en temps réel à la première entrée correspondante. 
2. **Matchs cyclistes** : 
- Appuyez sur `Down Arrow` (`↓`) pour passer au fichier correspondant suivant. 
- Appuyez sur `Up Arrow` (`↑`) pour passer au match précédent. 
- Appuyez sur `Enter` pour ouvrir ou exécuter l'élément correspondant. 
- Appuyez sur `Esc` pour fermer la barre de recherche tout en gardant le curseur sur le fichier trouvé. 
3. **L'astuce du point final** : 
- Tapez un point final (par exemple, `config.`) pour correspondre spécifiquement à la fin d'une base de nom de fichier, en distinguant `config.xml` de `configuration_guide.md`. 
4. **Recherche rapide, filtre ou filtre sémantique** : 
- **Recherche rapide (`Ctrl+S` / `cm_QuickSearch`)** : Navigue le curseur entre les correspondances tout en gardant tous les fichiers visibles. 
- **Filtre rapide (`cm_QuickFilter`)** : masque temporairement tous les fichiers qui ne correspondent pas, affichant uniquement les lignes correspondantes dans le tableau. 
- **Filtre sémantique (`Ctrl+F` / `cm_SemanticFilter`)** : utilise des requêtes en langage naturel (par exemple, `/larger than 10MB`, `//today modified pdf`) via macOS Spotlight.

### Modes de colonne d'ajustement automatique

Vous en avez assez du redimensionnement manuel des colonnes ou des noms de fichiers tronqués ? ATBCmder dispose d'un moteur de dimensionnement de colonnes intelligent configuré sous **Préférences** → **Vues de fichiers** : 

1. **Largeur maximale du texte (`mode="max"`)** : 
- Analyse tous les noms de fichiers visibles et étire la colonne Nom afin que le nom de fichier visible le plus long soit entièrement lisible sans points de suspension (`...`). 
2. **Largeur moyenne du texte (`mode="average"`, par défaut)** : 
- Évalue la largeur statistique moyenne des caractères dans les fichiers multipliée par un facteur de remplissage configurable (`auto_fit_padding`, par défaut `1.0`) plus les marges des icônes. 
- **Avantage** : empêche un seul nom de fichier anormal de 150 caractères de pousser toutes les colonnes secondaires (taille, date, autorisations) hors du bord de l'écran. 
3. **Largeurs fixes (`mode="fixed"`)** : 
- Conserve les dimensions exactes des pixels de la colonne. 
- Activé automatiquement chaque fois que vous faites glisser manuellement un séparateur de colonne dans l'en-tête du tableau, en respectant vos ajustements manuels de mise en page.

### Mode horizontal à deux panneaux (`Ctrl+Shift+H` / `⌃⇧H` / `cm_HorizontalFilePanels`)

Par défaut, ATBCmder place les deux panneaux de fichiers côte à côte (séparation verticale). Sur les moniteurs ultra-larges ou les écrans portrait verticaux, vous pouvez passer à des panneaux horizontaux empilés : 

![Horizontal Dual Panels Mode](images/horizontal_panels_view.png) 
*Orientation horizontale des panneaux empilés avec panneaux supérieur et inférieur* 

- Basculez via le menu **Afficher** → **Mode panneaux horizontaux** ou appuyez sur `Ctrl+Shift+H` (`cm_HorizontalFilePanels`). 
- Le paradigme Actif/Inactif reste identique : les opérations se déroulent sans problème entre les panneaux Haut (Source) et Bas (Cible).

### Persistance des paramètres d'affichage par onglet

Dans la plupart des gestionnaires de fichiers, la modification de la colonne de tri ou le passage des colonnes détaillées aux vignettes force la fenêtre entière à changer globalement. 

ATBCmder isole et mémorise les préférences d'affichage au niveau des **onglets** individuels (`TabState`), automatiquement conservées lors des redémarrages via `SessionManager` (`atbcmder_session.xml`) : 

- **Modes d'affichage indépendants** : vous pouvez conserver l'onglet 1 dans la **Vue complète des colonnes** pour les révisions de code, l'onglet 2 dans la **Vue en grille des miniatures** pour les ressources graphiques et l'onglet 3 dans la **Vue brève** pour un survol rapide. 
- **Tri indépendant** : chaque onglet mémorise sa propre colonne de tri (nom, extension, taille, date ou autorisations) et son sens de tri (ascendant ou décroissant). Passer d’un onglet à l’autre ne réinitialise jamais vos priorités de tri. 
- **États plats et arborescents indépendants** : un onglet défini sur **Vue de branche plate** (`Cmd+B` / `cm_FlatView`) ou **Mode d'affichage d'arborescence** maintient son aplatissement de répertoire récursif sans modifier l'état d'affichage de tout autre onglet dans l'un ou l'autre panneau. 

---

## 9. Recettes pratiques étape par étape

Voici trois recettes concrètes montrant comment la navigation, les onglets et les listes de véhicules recherchés se combinent pour rationaliser les tâches quotidiennes.

### Recette 1 : Créer un espace de travail de développement persistant

**Objectif** : Configurer un espace de travail à double panneau pour le développement full-stack qui peut être restauré en un seul clic à tout moment. 

1. **Configurer le panneau de gauche (code source)** : 
- Accédez à `~/Projects/MyApp/src`. 
- Ouvrez un deuxième onglet (`Cmd+T`) et accédez à `~/Projects/MyApp/tests`. 
- Cliquez avec le bouton droit sur l'onglet `src` et choisissez **Verrouiller l'onglet** (`cmd_SetTabOptionLock`). 
2. **Configurer le panneau de droite (Build et journaux)** : 
- Cliquez sur le panneau de droite pour le mettre au point (`Tab`). 
- Accédez à `~/Projects/MyApp/dist`. 
- Ouvrez un deuxième onglet (`Cmd+T`) et accédez à `/var/log`. 
3. **Enregistrer l'espace de travail favori** : 
- Choisissez Menu **Favoris** → **Enregistrer les onglets actuels dans de nouveaux onglets favoris** (`cm_SaveFavoriteTabs`). 
- Entrez `MyApp FullStack` et appuyez sur `Enter`. 
4. **Restauration instantanée** : 
- Chaque fois que vous travaillez sur ce projet, sélectionnez simplement **Favoris** → **Charger les onglets à partir des onglets favoris** (`cm_LoadFavoriteTabs`) et choisissez `MyApp FullStack`. Les deux panneaux configureront instantanément les quatre onglets avec vos chemins exacts et vos paramètres de verrouillage. 

---

### Recette 2 : Aplatir les arborescences de répertoires profondes pour rechercher des actifs volumineux

**Objectif** : Trouver et nettoyer les montages de test surdimensionnés et les vidages de journaux dispersés dans des dizaines de sous-dossiers imbriqués. 

1. Accédez au haut de votre projet ou répertoire multimédia dans le panneau actif. 
2. Appuyez sur `Cmd+B` (`⌘B`) ou `Ctrl+B` (`cm_FlatView`) pour activer **Flat Branch View**. 
3. Regardez comme tous les sous-répertoires sont aplatis de manière récursive en une seule liste dans le panneau. 
4. Cliquez une ou deux fois sur l'en-tête de colonne **Taille** pour trier tous les fichiers du plus grand au plus petit. 
5. Les fichiers les plus volumineux de toute l'arborescence de répertoires apparaissent immédiatement en haut du panneau, avec la colonne **Chemin** indiquant leurs emplacements imbriqués exacts. 
6. Inspectez ou supprimez directement les fichiers volumineux. 
7. Appuyez à nouveau sur `Cmd+B` pour désactiver la vue plate et revenir à la navigation standard dans les dossiers. 

---

### Recette 3 : Création de favoris ultra-rapide sur les volumes internes et réseau

**Objectif** : Ajoutez un dossier de sauvegarde NAS distant à vos favoris et accédez-y en moins de deux secondes. 

1. Accédez à votre lecteur réseau monté (par exemple, `/Volumes/BackupShare/Archives`). 
2. Appuyez sur `Ctrl+D` (`⌃D`) pour appeler la fenêtre contextuelle **Directory Hotlist**. 
3. Cliquez sur le bouton **Ajouter le répertoire actuel** (`btn_add` / `cm_AddDirToHotlist`). 
4. Entrez un nom convivial tel que `NAS Archives`. 
5. Demain, lorsque vous serez n'importe où dans votre système de fichiers local, appuyez simplement sur `Ctrl+D`, tapez `nas` et appuyez sur `Enter`. ATBCmder vous transporte instantanément sur le réseau vers ce dossier précis. 

---

## 10. Alertes de sécurité et de système

> [!NOTE] 
> **Stockage externe et partages réseau** : 
> Lorsque vous accédez à des lecteurs USB externes ou à des partages réseau (`/Volumes/...`) dans des onglets ou des signets, assurez-vous que le volume est actuellement monté. Si un lecteur est démonté au lancement d'ATBCmder, les onglets pointant vers lui afficheront en toute sécurité un avis « Emplacement indisponible » plutôt que de planter ou de supprimer l'onglet. 

> [!ASTUCE] 
> **Mise en miroir des onglets sur les panneaux** : 
> Vous souhaitez que votre panneau de droite reflète immédiatement tous les onglets ouverts de votre panneau de gauche ? Utilisez Menu **Onglets** → **Copier tous les onglets dans le panneau opposé** (`cm_CopyAllTabsToOpposite`) pour reproduire la disposition de vos onglets des deux côtés. 

> [!AVERTISSEMENT] 
> **Attention concernant les opérations en vue plate (`Cmd+B`)** : 
> Dans Flat Branch View, les fichiers de plusieurs branches de répertoires distinctes apparaissent côte à côte dans une seule liste. Soyez prudent lorsque vous utilisez `Cmd+A` (Sélectionner tout) suivi de `F8` (Supprimer) ou `F6` (Déplacer), car votre action s'appliquera de manière récursive dans tous les sous-répertoires imbriqués. 

---

## 11. Tableau de référence du clavier à double matrice

| Catégorie | Actions | Raccourci macOS | Clé classique | ID de commande interne | 
| :--- | :--- | :--- | :--- | :--- | 
| **Navigation dans le répertoire** | Répertoire des parents | `Backspace` / `⌘↑` | `Ctrl+PgUp` | `cm_ChangeDirToParent` | 
| | Répertoire racine | `Ctrl+\` / `⌃\` | `\` | `cm_ChangeDirToRoot` | 
| | Répertoire Accueil | `Ctrl+Shift+Home` / `⌃⇧Home` | `Alt+Home` | `cm_ChangeDirToHome` | 
| | Première entrée | `Home` | `Home` | `cm_GoToFirst` | 
| | Dernière entrée | `End` | `End` | `cm_GoToLast` | 
| **Onglets de dossier** | Nouvel onglet | `Cmd+T` / `⌘T` | `Ctrl+T` | `cm_NewTab` | 
| | Fermer l'onglet | `Cmd+W` / `⌘W` | `Ctrl+W` | `cm_CloseTab` | 
| | Fermer les onglets en double | *Menu contextuel de l'onglet* | — | `cm_CloseDuplicateTabs` | 
| | Fermer tous les onglets | *Menu Onglets* | — | `cm_CloseAllTabs` | 
| | Renommer l'onglet | *Menu contextuel de l'onglet* | — | `cm_RenameTab` | 
| | Copier les onglets en face | *Menu Onglets* | — | `cm_CopyAllTabsToOpposite` | 
| | Onglet suivant | `Ctrl+Tab` / `⌃⇥` | `Ctrl+Tab` | `cm_NextTab` | 
| | Onglet précédent | `Ctrl+Shift+Tab` / `⌃⇧⇥` | `Ctrl+Shift+Tab` | `cm_PrevTab` | 
| | Afficher la liste des onglets | `Ctrl+Shift+L` / `⌃⇧L` | `Ctrl+Shift+L` | `cm_ShowTabsList` | 
| **Onglets favoris** | Enregistrer les onglets favoris | *Menu Favoris* | — | `cm_SaveFavoriteTabs` | 
| | Charger les onglets favoris | *Menu Favoris* | — | `cm_LoadFavoriteTabs` | 
| | Réenregistrer le favori actif | *Menu Favoris* | — | `cm_ResaveFavoriteTabs` | 
| | Recharger le favori actif | *Menu Favoris* | — | `cm_ReloadFavoriteTabs` | 
| | Configurer les onglets favoris | *Préférences* | — | `cm_ConfigFavoriteTabs` | 
| **Listes recherchées et historique** | Liste de favoris de l'annuaire | `Ctrl+D` / `⌃D` | `Ctrl+D` | `cm_DirHotList` | 
| | Configurer la liste de véhicules recherchés | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| | Ajouter le répertoire à la liste de véhicules recherchés | *Pop-up liste de favoris* | — | `cm_AddDirToHotlist` | 
| | Histoire en arrière | `Cmd+[` / `⌘[` | `Alt+Left` | `cm_ViewHistoryPrev` | 
| | Histoire en avant | `Cmd+]` / `⌘]` | `Alt+Right` | `cm_ViewHistoryNext` | 
| | Liste déroulante de l'historique | `Alt+F8` / `⌥F8` | `Ctrl+Down` | `cm_DirHistory` | 
| **Lecteurs et volumes** | Lecteurs du panneau gauche | `Alt+F1` / `⌥F1` | `Alt+F1` | `cm_LeftOpenDrives` | 
| | Lecteurs du panneau droit | `Alt+F2` / `⌥F2` | `Alt+F2` | `cm_RightOpenDrives` | 
| | Menu du lecteur de panneau actif | `Alt+D` / `⌥D` | `Alt+D` | `cm_Drives` | 
| **Modes d'affichage** | Affichage des colonnes complètes | `Ctrl+F2` / `⌃F2` | `Ctrl+F2` | `cm_ColumnsView` | 
| | Bref aperçu | `Ctrl+F1` / `⌃F1` | `Ctrl+F1` | `cm_BriefView` | 
| | Affichage des vignettes | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| | Vue arborescente (Remplacer) | *Afficher le menu* | `Ctrl+Shift+F8` | `cm_TreeView` | 
| | Vue arborescente (divisée) | *Afficher le menu* | — | `cm_TreeViewSplit` | 
| | Vue arborescente (les deux panneaux) | *Afficher le menu* | — | `cm_TreeViewBoth` | 
| | Vue de branche plate | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | 
| | Mode panneaux horizontaux | `Ctrl+Shift+H` / `⌃⇧H` | `Ctrl+Shift+H` | `cm_HorizontalFilePanels` | 
| **Recherche et filtres** | Superposition de recherche rapide | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_QuickSearch` | 
| | Filtre sémantique | `Ctrl+F` / `⌃F` | `Ctrl+F` | `cm_SemanticFilter` |

--- 

<div align="center"> 
<p>Maintenant que vous maîtrisez la navigation dans les répertoires, les onglets et les vues de panneau :</p> 
<p><strong><a href="file_operations.md">Passez au chapitre 3 : Opérations quotidiennes sur les fichiers et file d'attente &rarr;</a></strong></p> 
</div>