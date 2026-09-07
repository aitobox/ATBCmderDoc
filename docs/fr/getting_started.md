# Chapitre 1: Notions de base et configuration macOS

Bienvenue sur **ATBCmder** ! Conçu nativement pour macOS 12+ sur Apple Silicon (architecture M1/M2/M3/M4, ARM64 ; Intel x86_64 n'est actuellement pas pris en charge), ATBCmder apporte au Mac la vitesse, l'agilité du clavier et la précision inégalées de la gestion de fichiers orthodoxe à double panneau. 

Ce chapitre vous présente la philosophie de base du double panneau, détaille chaque point majeur de l'interface, vous guide dans l'intégration des autorisations macOS App Sandbox et fournit les configurations système essentielles requises pour une expérience transparente. 

---

## 1. Démarrage rapide visuel : la philosophie du double panneau

Si vous avez utilisé macOS Finder, vous avez l'habitude d'ouvrir plusieurs fenêtres qui se chevauchent, de faire glisser des fichiers sur des bureaux encombrés et d'espérer que les fichiers atterrissent dans le dossier de destination prévu plutôt que dans un sous-dossier adjacent accidentel. 

ATBCmder remplace cette friction par le paradigme éprouvé du **Orthodox File Manager (OFM)** : deux panneaux de répertoires indépendants et complémentaires placés côte à côte. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE (SOURCE) PANEL                     INACTIVE (TARGET) PANEL              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Name               Size    Date    │   │  Name                Size     Date    │
│  ▸ [..]                     --:--   │ C │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Yesterday O │  ▸ 2025_Archive      <DIR>    May 12  │
│  ● release_notes.md 14.2 KB Today   │ P │  ▸ Website_V2        <DIR>    Aug 28  │
│  ● update_v1.7.pkg  84.5 MB Today   │ Y │  ● config.yaml       3.2 KB   Jun 04  │
│                                     │ ➔ │                                       │
│  [ Focused / Blue Accent Outline ]  │   │  [ Unfocused / Subdued Outline ]      │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘
```

### Le modèle actif (source) ou inactif (cible)

Dans ATBCmder, vous n’aurez jamais à vous demander où une opération prendra effet : 

1. **Le panneau actif (source)** : 
- Il s'agit du panneau où résident actuellement le focus de votre clavier et votre curseur. 
- Toute sélection, navigation ou action que vous effectuez cible directement ce panneau. 
- **Repère visuel** : le panneau actif comporte une bague de mise au point proéminente (couleur d'accent du système macOS), un texte d'onglet en surbrillance et une surbrillance de curseur actif distincte sur l'élément actuellement ciblé. 

2. **Le panneau inactif (cible)** : 
- C'est le panneau opposé. Il reste entièrement visible, affichant une hiérarchie de dossiers indépendante. 
- Le panneau inactif fait office de **destination automatique** pour les opérations sur les fichiers initiées dans le panneau actif. 
- **Repère visuel** : le panneau inactif affiche une bordure atténuée, un texte légèrement grisé et des titres d'onglets assourdis.

### Opérations directionnelles : toujours source ➔ cible

Lorsque vous lancez une opération dans ATBCmder, l'application comprend automatiquement la direction : 

- **Copier (`F5` / `Cmd+C` ➔ `Cmd+V`)** : Copie les fichiers sélectionnés du panneau Actif (Source) directement dans le répertoire actuellement affiché dans le panneau Inactif (Cible). 
- **Déplacer (`F6` / `Cmd+C` ➔ `Opt+Cmd+V`)** : Déplace les fichiers sélectionnés du panneau actif vers le panneau inactif sans avoir besoin de saisir ou de rechercher le répertoire de destination. 
- **Synchronisation du répertoire (`Shift+F12` / `cm_SyncDirs`)** : Compare le répertoire du panneau actif avec le répertoire du panneau inactif. 

> [!ASTUCE] 
> **Aucune hypothèse de glisser-déposer requise** : vous n'avez pas besoin de faire glisser des éléments au-delà des limites de l'écran. Sélectionnez simplement ce que vous voulez dans le panneau actif, appuyez sur `F5` (Copier) ou `F6` (Déplacer), appuyez sur `Enter` pour confirmer l'invite et ATBCmder transfère les fichiers immédiatement.

### Navigation dans le panneau et changement de mise au point

| Actions | Raccourci macOS | Clé de commandant classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Changer de mise au point** | `Tab` | `Tab` | `cm_FocusSwap` | Alterne le focus clavier entre les panneaux gauche et droit (`cm_SwitchPanel`). | 
| **Mise au point inversée** | `Shift+Tab` | `Shift+Tab` | `cm_FocusSwap` | Inverse l’ordre de mise au point sur les panneaux et les commandes. | 
| **Échanger gauche et droite** | `Ctrl+U` | `Ctrl+U` | `cm_Exchange` | Échange les chemins de répertoire entre les panneaux gauche et droit sans perdre les onglets ou la sélection. | 
| **Rapport d'égalisation** | `Double-click splitter` | `Double-click splitter` | — | Réinitialise automatiquement le répartiteur central à une balance propre 50/50. | 

---

## 2. Anatomie de l'interface et visite historique

ATBCmder fournit une interface macOS propre et native construite avec Qt6 et PySide6, conçue selon les directives d'Apple Human Interface tout en respectant les flux de travail classiques des commandants centrés sur le clavier. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] NATIVE MACOS MENU BAR                                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] TOP MAIN TOOLBAR  [ ↺ Refresh ] [ 📋 Copy ] [ ✂ Move ] [ 🗑 Delete ] ...   │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] BREADCRUMB BAR (Left Panel)     │   │ [3] BREADCRUMB BAR (Right Panel)      │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] FOLDER TABS: [Dev] [Docs] [+]   │[6]│ [4] FOLDER TABS: [Photos] [Backup] [+]│
├─────────────────────────────────────┤MID│───────────────────────────────────────┤
│                                     │DLE│                                       │
│ [5] DUAL FILE PANEL (Left)          │   │ [5] DUAL FILE PANEL (Right)           │
│     - Virtualized table listing     │BAR│     - Virtualized table listing       │
│     - Name, Ext, Size, Date, Attr   │ & │     - Name, Ext, Size, Date, Attr     │
│     - Real-time sort & filter       │SPL│     - Real-time sort & filter         │
│                                     │IT-│                                       │
│                                     │TER│                                       │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] STATUS BAR & DRIVE STORAGE METER                                            │
│  3 of 28 files selected (42.8 MB / 1.2 GB)  |  Macintosh HD: 218.4 GB free      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### [1] Barre de menus native de macOS

Entièrement intégré à la barre de menu supérieure de macOS. Toutes les opérations, bascules d'affichage, outils électriques et préférences sont classés logiquement : 

- **Fichier** : Nouvel onglet, Fermer l'onglet, Propriétés du fichier, Autorisations Sandbox, Quitter. 
- **Marquer** : Sélectionner un groupe (`Num+`), Désélectionner un groupe (`Num-`), Inverser la sélection (`Num*`), Sélectionner tout (`Cmd+A`). 
- **Commandes** : liste de répertoires recherchés (`Ctrl+D`), lecteurs gauche/droite (`Alt+F1/F2`), recherche (`Alt+F7`), répertoires de synchronisation (`Shift+F12`), panneaux d'échange (`Ctrl+U`), terminal (`Ctrl+J`). 
- **Afficher** : bascule le mode d'affichage (Brief, Colonnes complètes, Miniatures, Arbre, Vue à branches plates), visibilité de la barre d'outils, disposition des panneaux horizontaux. 
- **Configuration** : Options / Préférences (`Cmd+,`), Enregistrer la position (`cm_ConfigSavePos`), Enregistrer les onglets.

### [2] Barre d'outils principale supérieure

Situé directement sous la barre de titre de la fenêtre. Fournit un accès instantané en un clic aux commandes globales : 

- **Actions par défaut** : Actualiser (`Ctrl+R`), Affichage rapide (`Ctrl+Q`), Copier (`F5`), Déplacer (`F6`), Nouveau dossier (`F7`), Supprimer (`F8`), Rechercher (`Alt+F7`) et Options (`Cmd+,`). 
- **Personnalisable** : personnalisez la taille des icônes (16 px à 48 px), activez les étiquettes de texte des boutons ou masquez entièrement la barre d'outils via le menu **Afficher** → **Afficher la barre d'outils** pour maximiser l'espace à l'écran.

### [3] Barre de fil d'Ariane interactive de style Finder

Positionnée au-dessus de chaque panneau de fichiers, la barre de chemin de navigation permet des sauts hiérarchiques ultra-rapides : 

- **Navigation par segment** : cliquez sur n'importe quel dossier ancêtre dans la chaîne de fil d'Ariane (par exemple, en cliquant sur `username` dans `/Users/username/Projects/ATBCmder`) pour accéder directement à ce répertoire. 
- **Déroulants frères et sœurs** : passez la souris ou cliquez sur la flèche en chevron entre les segments pour afficher un menu déroulant répertoriant tous les dossiers frères à ce niveau. 
- **Menu contextuel du segment** : cliquez avec le bouton droit sur n'importe quel segment de fil d'Ariane pour accéder à des utilitaires contextuels rapides : 
- **Ouvrir dans un nouvel onglet** : conserve votre vue actuelle lors de l'ouverture du répertoire parent dans un nouvel onglet. 
- **Révéler dans le Finder** : ouvre le répertoire dans le Finder macOS (`open -R`). 
- **Copier le chemin** : copie le chemin UNIX absolu du segment dans le presse-papiers de votre système. 
- **Ouvrir dans le terminal** : génère le terminal macOS directement dans ce dossier (`open -a Terminal`). 
- **Édition directe du chemin (`BreadcrumbLineEdit`)** : double-cliquez sur l'espace vide à droite du fil d'Ariane. La barre se convertit instantanément en un champ de texte modifiable dans lequel vous pouvez coller ou saisir n'importe quel chemin (par exemple, archives `/var/log`, `~/Library` ou `vfs://`). Appuyez sur `Enter` pour naviguer ou sur `Esc` pour annuler.

### [4] Barre d'onglets des dossiers

Chaque panneau conserve un ensemble indépendant d'onglets : 

- Ouvrez de nouveaux onglets avec `Cmd+T` (`cm_NewTab`), fermez les onglets avec `Cmd+W` (`cm_CloseTab`). 
- Glisser-déposer pour réorganiser les onglets dans un panneau. 
- Cliquez avec le bouton droit sur les onglets pour verrouiller les chemins, renommer les titres, fermer les doublons ou dupliquer les onglets sur le panneau opposé.

### [5] Panneaux à double fichier

Listes de fichiers virtualisées hautes performances capables de restituer des dossiers contenant des centaines de milliers d'entrées en douceur sans bégaiement de l'interface utilisateur : 

- Tri des colonnes : cliquez sur n'importe quel en-tête (Nom, Ext, Taille, Date, Attributs) pour trier par ordre croissant ou décroissant. 
- Plusieurs modes d'affichage : vue complète des détails, vue en grille brève, vue en galerie de vignettes, vue en arborescence et vue en branches plates récursive (`Cmd+B`).

### [6] Barre d'outils centrale et séparateur déplaçable

Positionnée directement entre les panneaux de fichiers gauche et droit, la barre d'outils centrale est une fonctionnalité unique d'ATBCmder combinant la gestion de fichiers en un clic avec un séparateur de panneau réglable : 

![Middle Toolbar](images/middle_toolbar.png) 

- **Quick Action Strip** : contient des boutons verticaux pour les opérations courantes : 
- `cm_Copy` (Copie) 
- `cm_Move` (Déplacer / Couper) 
- `cm_Delete` (Supprimer dans la corbeille) 
- `cm_MkDir` (Nouveau répertoire) 
- `cm_Rename` (Renommage rapide en ligne) 
- `cm_View` (Liste universelle) 
- `cm_Edit` (éditeur de texte/code interne) 
- `cm_Exchange` (échanger les panneaux gauche et droit) 
- `cm_SyncDirs` (synchroniseur de dossiers) 
- `cm_FileSearch` (Recherche avancée) 
- ** Glissement continu du séparateur ** : en déplaçant le curseur de votre souris sur la barre du milieu, le pointeur se transforme en curseur divisé horizontal (`SplitHCursor`). Cliquez et faites glisser horizontalement pour ajuster en douceur la proportion de largeur entre les deux panneaux. 
- **Préréglages de rapport de thème élégant** : lors de l'utilisation du thème moderne "Élégant", la barre du milieu affiche des commandes segmentées permettant un accrochage instantané à **50/50**, **70/30** ou **30/70** la distribution de la largeur du panneau. 
- **Préférences de la barre d'outils centrale** : activez ou désactivez la barre d'outils centrale, ajustez la taille des icônes ou basculez entre les boutons plats modernes et les séparateurs encastrés classiques dans **Préférences** (`Cmd+,`) → **Barres d'outils** → **Barre d'outils centrale**.

### [7] Barre d'état et compteur de stockage du lecteur

Ancré tout en bas de la fenêtre : 

- **Statistiques de sélection** : affiche les métriques en temps réel pour le panneau actif : 
- Nombre total d'éléments et taille totale du dossier. 
- Nombre d'éléments sélectionnés et taille d'octet sélectionnée combinée. 
- **Drive Storage Meter** : indicateur visuel d'utilisation du disque affichant le nom du volume actuellement monté (par exemple, `Macintosh HD`), la capacité totale, le stockage utilisé et le pourcentage d'espace libre restant. 

---

## 3. Recette étape par étape : autorisations du bac à sable et du système de fichiers de l'application macOS

macOS moderne utilise un sandboxing strict de sécurité des applications pour protéger les données des utilisateurs contre tout accès non autorisé. Lors de l'exécution d'ATBCmder (en particulier lorsqu'elle est installée via le Mac App Store ou distribuée avec le sandboxing activé), l'application est isolée dans son propre répertoire de conteneur sécurisé : 
`~/Library/Containers/com.aitobox.atbcmder/Data` 

Par défaut, les applications en bac à sable ne peuvent pas inspecter ou modifier arbitrairement les fichiers en dehors de leur conteneur, à moins que l'utilisateur n'accorde explicitement l'autorisation via les panneaux ouverts natifs d'Apple. 

ATBCmder rationalise ce processus d'intégration avec des **signets à portée de sécurité**, vous permettant d'accorder l'autorisation une seule fois et de bénéficier d'un accès persistant et sans restriction pour toutes les sessions futures.

### Comprendre les signets de sécurité

Lorsque vous autorisez un chemin de dossier à l'aide de macOS `NSOpenPanel` : 

1. macOS émet un **signet de sécurité** cryptographique (`NSURLBookmarkCreationWithSecurityScope`). 
2. ATBCmder sérialise et enregistre ce signet dans son répertoire de configuration : 
`~/Library/Application Support/ATBCmder/sandbox_bookmarks.plist` 

3. À chaque lancement d'application, ATBCmder résout et active automatiquement ces signets via `startAccessingSecurityScopedResource()`. 
4. Une fois accordé, vous n’aurez plus jamais besoin de réautoriser ces répertoires.

### Procédure pas à pas de configuration guidée : utilisation de `cm_GrantFilesystemAccess`

Pour configurer vos autorisations lors du premier lancement ou à tout moment ultérieurement, procédez comme suit :

#### Étape 1 : ouvrez l'assistant d'intégration des autorisations

Dans la barre de menu native, sélectionnez **Fichier** (ou **Aide**) → **Grant Filesystem Access…**, ou déclenchez la commande interne `cm_GrantFilesystemAccess`. La boîte de dialogue d'intégration apparaît : 

```
┌─────────────────────────────────────────────────────────────┐
│  Grant Filesystem Access                                [x] │
├─────────────────────────────────────────────────────────────┤
│  Because this version of ATBCmder runs inside a secure      │
│  macOS Sandbox, it needs your permission to access          │
│  critical folders.                                          │
│                                                             │
│  [  Grant Access to Root Directory (/)  ]                   │
│                                                             │
│  [  Grant Access to External Disks (/Volumes)  ]            │
│                                                             │
│  [  Open Full Disk Access Settings…  ]                      │
│                                                             │
│  Root directory access is required by the App Sandbox.      │
│  Full Disk Access is a separate macOS permission for        │
│  protected user data.                                       │
│                                                   [ Done ]  │
└─────────────────────────────────────────────────────────────┘
```

#### Étape 2 : Accorder l'accès au répertoire racine (`/`)

1. Cliquez sur **"Accorder l'accès au répertoire racine (/)"**. 
2. ATBCmder appelle la feuille `NSOpenPanel` native de macOS, pointant vers le disque racine `Macintosh HD` (`/`). 
3. Cliquez sur **"Accorder l'accès"** (ou **Ouvrir**). 
4. Le bouton se met immédiatement à jour en **"Accès au répertoire racine accordé ✓"** et devient désactivé. 
5. **Ce que cela permet** : L'autorisation du chemin racine `/` couvre automatiquement tous les répertoires d'utilisateurs (`~/Documents`, `~/Downloads`, `~/Desktop`, `~/Projects`, `/Applications`, etc.) car Les signets à portée de sécurité héritent automatiquement des autorisations descendantes sur tous les sous-chemins enfants.

#### Étape 3 : Accorder l'accès aux disques externes (`/Volumes`)

1. Cliquez sur **"Accorder l'accès aux disques externes (/Volumes)"**. 
2. Lorsque le panneau natif affiche `/Volumes`, cliquez sur **"Accorder l'accès"**. 
3. Le bouton se met à jour et devient **"Accès aux disques externes accordé ✓"**. 
4. **Ce que cela permet** : Accès illimité en lecture/écriture aux lecteurs USB externes, aux lecteurs Thunderbolt, aux cartes SD, aux montages d'images disque DMG et aux volumes SMB/NFS/AFP montés en réseau.

#### Étape 4 : Accès sélectif dossier par dossier (alternative)

Si vous préférez ne pas accorder un accès root étendu à ATBCmder, vous n'êtes pas obligé de cliquer sur accès root : 

- Lorsque vous naviguez dans un dossier non autorisé (tel qu'un dossier externe ou un référentiel de projet), ATBCmder détecte la limite d'autorisation et affiche une invite à la demande : 
`ATBCmder requires your permission to access: /Users/username/SecretProject` 

- Cliquez sur **"Accorder l'accès au dossier"**, approuvez la boîte de dialogue native et ce répertoire spécifique sera définitivement ajouté à vos favoris.

#### Étape 5 : Accès complet au disque (FDA) pour les données système protégées

> [!IMPORTANT] 
> **Sandbox Signets vs accès complet au disque (FDA)** : 
> 
> - **Les signets Sandbox** accordent un accès général au système de fichiers aux dossiers utilisateur standard, aux fichiers et aux lecteurs externes. 
> - **Full Disk Access (FDA)** est une autorisation de confidentialité supplémentaire de transparence, de consentement et de contrôle (TCC) de macOS requise pour inspecter les données personnelles sensibles de macOS (telles que l'historique Safari, les pièces jointes aux messages, les messages, les sauvegardes Time Machine et les caches système). 
> 
> Si vous devez gérer ces dossiers protégés : 
> 
> 1. Cliquez sur **"Ouvrir les paramètres d'accès complet au disque…"** dans la boîte de dialogue d'intégration. 
> 2. macOS ouvre **Paramètres système** → **Confidentialité et sécurité** → **Accès complet au disque**. 
> 3. Cliquez sur le verrou ou authentifiez-vous avec Touch ID/mot de passe. 
> 4. Assurez-vous que l'interrupteur à bascule à côté de **ATBCmder** est activé **ON**.

### Révocation et réinitialisation des autorisations

Si jamais vous devez réinitialiser ou révoquer vos favoris sandbox : 

1. Ouvrez le répertoire de configuration d'ATBCmder via le menu **Configuration** → **Open Config Directory** (`cm_OpenConfigDirectory`). 
2. Supprimez le fichier `sandbox_bookmarks.plist`. 
3. Redémarrez ATBCmder. 
4. Pour réinitialiser les autorisations TCC au niveau du système macOS, exécutez la commande suivante dans le terminal macOS : 
   ```bash
   tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder
   ```
 

---

## 4. Paramètres de langue et personnalisation de l'apparence

ATBCmder est localisé pour les flux de travail globaux et s'intègre parfaitement aux préférences d'apparence de macOS.

### Internationalisation et remplacements de langues

ATBCmder prend en charge **plus de 30 langues**, dont l'anglais, le chinois simplifié (简体中文), le chinois traditionnel (繁體中文), l'allemand (Deutsch), le français (Français), l'espagnol (Español), le russe (Русский), le japonais (日本語), l'italien, le polonais, le coréen, etc. 

![Language Settings](images/language_settings.png) 

- **Suivi automatique de la langue du système** : par défaut, ATBCmder détecte les paramètres régionaux de votre système macOS (`AppleLanguages`) au démarrage et applique automatiquement la traduction correspondante. 
- **Sélection manuelle de la langue** : 
1. Ouvrez les Préférences en appuyant sur `Cmd+,` ou en exécutant `cm_Options`. 
2. Dans le volet de navigation de gauche, sélectionnez **Langue**. 
3. Choisissez votre langue préférée dans la liste déroulante. 
- **Live Reload (Aucun redémarrage requis)** : contrairement à la plupart des utilitaires Mac traditionnels qui nécessitent de quitter et de redémarrer l'application, ATBCmder retraduit dynamiquement l'intégralité de l'interface (menus, barres d'outils, boîtes de dialogue, info-bulles des boutons et messages d'état) en temps réel au moment où vous sélectionnez une nouvelle langue.

### Apparence et thèmes

ATBCmder prend entièrement en charge les modes d'apparence macOS Light et Dark : 

- **Synchronisation de l'apparence du système** : passe automatiquement du mode clair au mode sombre chaque fois que l'apparence de votre système macOS change (par exemple au coucher du soleil ou via le centre de contrôle). 
- **Options de thème** : 
- **Fusion / Native macOS** : esthétique de bureau classique et épurée qui respecte les couleurs d'accentuation de macOS et le dynamisme des fenêtres. 
- **Thème élégant** : esthétique moderne avec commandes segmentées arrondies, séparateurs de dégradé subtils et barres d'onglets en forme de pilule. 
- **Palette du mode sombre** : utilise des surfaces anthracite foncées (`#2C2C2E` / `#242426`) avec du texte à contraste élevé et des icônes de dossiers personnalisées, réduisant ainsi la fatigue oculaire dans les environnements faiblement éclairés. 
- **Palette de modes d'éclairage** : fond blanc éclatant avec des séparateurs gris doux (`#FAFBFD` / `#EEF2F7`) et des bordures contrastées claires. 

---

## 5. ⚡ Conseils de pro et configurations de mise en page avancées

Profitez pleinement du moteur de mise en page flexible d'ATBCmder pour adapter votre espace de travail à des configurations de gestion de données multi-moniteurs, ultra-larges ou spécialisées.

### Astuce 1 : Enregistrement de la position de la fenêtre et des ratios de disposition (`cm_ConfigSavePos`)

Lorsque vous organisez votre espace de travail (en personnalisant les dimensions de la fenêtre, en l'agrandissant sur un écran externe ou en définissant une proportion spécifique de séparateur central), vous pouvez verrouiller cette configuration afin qu'elle soit restaurée de manière identique à chaque fois : 

1. Organisez la fenêtre principale d'ATBCmder et ajustez le séparateur central selon votre rapport préféré. 
2. Sélectionnez le menu **Configuration** → **Enregistrer la position et la mise en page**, ou exécutez la commande interne : 
   ```
   cm_ConfigSavePos
   ```
 

3. La taille de votre fenêtre, les coordonnées de l'écran, l'état maximisé et les rapports de panneaux sont écrits directement dans `atbcmder.xml`. 
4. Dans **Préférences** → **Mise en page**, assurez-vous que **"Enregistrer la position de la fenêtre à la sortie"** est coché pour les mises à jour automatiques continues.

### Astuce 2 : basculer la disposition horizontale à deux panneaux (`cm_HorizontalFilePanels`)

Alors que les panneaux verticaux côte à côte sont standard pour les opérations sur les fichiers, les panneaux horizontaux empilés (panneau supérieur et panneau inférieur) sont exceptionnellement utiles lorsque : 

- Travailler avec des noms de fichiers ultra-longs nécessitant une largeur plein écran. 
- Comparaison de colonnes de métadonnées de fichiers étendues (autorisations, propriétaires, sommes de contrôle, dimensions). 
- Travailler sur des moniteurs ou des tablettes verticaux pivotés. 

Pour changer de disposition : 

1. Sélectionnez le menu **Afficher** → **Panneaux horizontaux** ou déclenchez la commande interne : 
   ```
   cm_HorizontalFilePanels
   ```
 

2. Lorsque le mode horizontal est actif : 
- Les panneaux s'empilent verticalement (Panneau supérieur et Panneau inférieur). 
- La barre d'outils centrale pivote automatiquement en une bande horizontale entre les panneaux supérieur et inférieur. 
- Le curseur glissant s'adapte à un pointeur de division verticale (`SplitVCursor`), vous permettant de redimensionner le rapport de hauteur entre les panneaux supérieur et inférieur sans effort.

### Astuce 3 : Snapping du séparateur central en un clic

- **Équilibre instantané 50/50** : double-cliquez n'importe où sur la barre de séparation centrale ou sur la ligne de séparation. Les panneaux reviennent immédiatement à une répartition exacte de 50 %/50 %. 
- **Ratio Presets** : dans le thème « Élégant », en cliquant sur les boutons segmentés du milieu, la mise en page s'aligne sur `50:50`, `70:30` (en mettant l'accent sur le panneau source) ou `30:70` (en mettant l'accent sur le panneau de destination).

### Astuce 4 : Restauration automatique de session et persistance de l'espace de travail

ATBCmder dispose d'un sous-système de gestion de session intelligent (`SessionManager`) qui garantit que votre environnement de travail est toujours préservé : 

- **Session XML Storage** : l'état de session est automatiquement conservé dans `atbcmder_session.xml` dans votre répertoire de configuration (`~/Library/Application Support/ATBCmder/`). 
- **Mémoire de géométrie de fenêtre** : restaure les coordonnées exactes de la fenêtre (`x`, `y`), les dimensions (`width`, `height`), l'état maximisé et la proportion du diviseur central (`splitter_ratio`). 
- **Restauration des onglets à double panneau** : 
- Restaure tous les onglets ouverts dans les panneaux gauche et droit au lancement. 
- Mémorise l'index des onglets actifs dans chaque panneau. 
- Charge automatiquement le répertoire de travail exact pour chaque onglet, éliminant ainsi la friction liée à la re-navigation manuelle vers des dossiers de projet approfondis. 
- **Verrouillage de la position par défaut** : vous pouvez également verrouiller de manière permanente la géométrie de votre fenêtre et le rapport de répartition actuels comme configuration de démarrage par défaut à l'aide de **Configuration ➔ Enregistrer la position** (`cm_ConfigSavePos`). 

---

## 6. Alertes de sécurité et système : configuration de la touche de fonction macOS (Fn)

Si vous avez utilisé Total Commander, Double Commander ou Norton Commander sur un clavier de PC, vos doigts sont entraînés à utiliser les touches de fonction de la rangée supérieure (`F3` View, `F4` Edit, `F5` Copy, `F6` Move, `F7` MkDir, `F8` Supprimer). 

Cependant, les claviers Apple gèrent différemment la ligne de fonctions dès la sortie de la boîte. 

> [!AVERTISSEMENT] 
> ### 🍎 Conflit matériel entre les touches de fonction macOS 
> Sur les claviers Apple (claviers intégrés MacBook, Apple Magic Keyboard), les touches de la rangée supérieure sont par défaut **Fonctionnalités matérielles spéciales macOS** (luminosité de l'écran, contrôle de mission, projecteur, dictée, ne pas déranger, commandes multimédias et volume audio). 
> 
> Si vous appuyez sur `F5` sur un MacBook sans configuration, macOS tentera de régler l'éclairage du clavier ou de déclencher la dictée plutôt que de copier vos fichiers !

### Option A : maintenez la touche `Fn` (Globe 🌐) (configuration macOS par défaut)

Si vous préférez conserver intactes les clés multimédias par défaut d’Apple : 

- Maintenez enfoncée la touche **`Fn`** (ou Globe 🌐) tout en appuyant sur n'importe quelle touche de fonction : 
- `Fn+F3` : Lister universel 
- `Fn+F4` : Editeur interne 
- `Fn+F5` : Copier des fichiers 
- `Fn+F6` : déplacer des fichiers 
- `Fn+F7` : Créer un dossier 
- `Fn+F8` : supprimer dans la corbeille

### Option B : activer les touches de fonction standard à l'échelle du système (recommandé)

Si vous souhaitez des réflexes Commander authentiques et rapides à une seule touche sans maintenir le modificateur `Fn` : 

1. Ouvrez **Paramètres système** dans le menu Pomme (). 
2. Cliquez sur **Clavier** dans la barre latérale. 
3. Cliquez sur le bouton **Raccourcis clavier clavier…**. 
4. Dans la liste de navigation de gauche, sélectionnez **Touches de fonction**. 
5. Activez la bascule : **"Utiliser les touches F1, F2, etc. comme touches de fonction standard"**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Keyboard Shortcuts                                         │
├──────────────────┬──────────────────────────────────────────┤
│  Launchpad & Dock│  Use F1, F2, etc. keys as standard       │
│  Display         │  function keys                           │
│  Mission Control │                                          │
│  Keyboard        │  [ ON ───● ]                             │
│  Input Sources   │                                          │
│  Screenshots     │  When this option is selected, press the │
│ ▸ Function Keys  │  Fn key to use the special features      │
│  App Shortcuts   │  printed on each key.                    │
└──────────────────┴──────────────────────────────────────────┘
```
 

Une fois activé : 

- Appuyer sur `F1`–`F12` déclenche directement et immédiatement les commandes ATBCmder. 
- Pour utiliser les commandes de luminosité ou de volume, maintenez simplement `Fn` tout en appuyant sur la touche. 

---

## 7. Référence rapide des raccourcis essentiels à double matrice

ATBCmder offre une prise en charge complète du clavier à double matrice : utilisez les raccourcis macOS natifs (`Cmd ⌘`), les touches Commander classiques (`Fn`) ou les deux de manière interchangeable.

| Action de base | ID de commande | macOS Natif (`Cmd ⌘`) | Commandant classique (`Fn`) | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Liste chaude de l'annuaire** | `cm_DirHotList` | `Cmd+D` / `⌘D` | `Ctrl+D` / `⌃D` | Ouvre la fenêtre contextuelle des signets du répertoire avec une recherche floue instantanée. | 
| **Liste des lecteurs (gauche/droite)** | `cm_LeftOpenDrives` / `cm_RightOpenDrives` | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | Ouvre le menu Lecteur et volume pour le panneau gauche ou droit (`Alt+D` pour le panneau actif). | 
| **Copier des fichiers** | `cm_Copy` | `Cmd+C` ➔ `Cmd+V` | `F5` (ou `Fn+F5`) | Copie les éléments sélectionnés du panneau actif vers le panneau inactif. | 
| **Déplacer des fichiers** | `cm_Move` | `Cmd+C` ➔ `Opt+Cmd+V` | `F6` (ou `Fn+F6`) | Déplace les éléments sélectionnés du panneau actif vers le panneau inactif. | 
| **Afficher dans Lister** | `cm_View` | `Space` / `Cmd+Y` | `F3` (ou `Fn+F3`) | Ouvre le fichier dans Universal Lister (code, hexadécimal, image, pdf, audio). | 
| **Coup d'œil** | `cm_QuickView` | `Cmd+Q` / `Ctrl+Q` | `Ctrl+Q` | Affiche un aperçu instantané en direct dans le panneau opposé. | 
| **Modifier le fichier** | `cm_Edit` | `Cmd+E` | `F4` (ou `Fn+F4`) | Ouvre le fichier dans l'éditeur de code/texte intégré. | 
| **Nouveau répertoire** | `cm_MkDir` | `Shift+Cmd+N` | `F7` (ou `Fn+F7`) | Crée un nouveau dossier dans le panneau actif. | 
| **Supprimer dans la corbeille** | `cm_Delete` | `Cmd+Backspace` | `F8` (ou `Fn+F8`) | Déplace en toute sécurité les fichiers sélectionnés vers la corbeille macOS. | 
| **Renommer en ligne** | `cm_Rename` | `Return` | `F2` / `Shift+F6` | Renomme le fichier en surbrillance sur place. | 
| **Panneau de commutation** | `cm_FocusSwap` | `Tab` | `Tab` | Déplace le focus du clavier vers le panneau opposé (`cm_SwitchPanel`). | 
| **Échanger gauche/droite** | `cm_Exchange` | `Ctrl+U` | `Ctrl+U` | Échange les chemins de répertoire entre les panneaux gauche et droit. | 
| **Nouvel onglet** | `cm_NewTab` | `Cmd+T` | `Ctrl+T` | Ouvre un nouvel onglet de dossier dans le panneau actuel. | 
| **Fermer l'onglet** | `cm_CloseTab` | `Cmd+W` | `Ctrl+W` | Ferme l'onglet actif. | 
| **Mode horizontal** | `cm_HorizontalFilePanels` | Menu : Afficher ➔ Horizontal | Menu : Afficher ➔ Horizontal | Bascule entre la disposition empilée côte à côte et la disposition empilée haut et bas. | 
| **Enregistrer la mise en page** | `cm_ConfigSavePos` | Menu : Config ➔ Enregistrer Pos | Menu : Config ➔ Enregistrer Pos | Enregistre les dimensions actuelles de la fenêtre et les proportions des panneaux. | 
| **Accès au bac à sable** | `cm_GrantFilesystemAccess` | Menu : Fichier ➔ Autorisations | Menu : Fichier ➔ Autorisations | Lance l’assistant d’intégration macOS App Sandbox. | 
| **Préférences** | `cm_Options` | `Cmd+,` | `Alt+O` | Ouvre la boîte de dialogue de configuration d'ATBCmder. |

---

## Prochaines étapes

Maintenant que vous maîtrisez la base du double panneau et configurez votre environnement macOS, passez au **[Chapitre 2 : Onglets de navigation et de dossier](navigation_and_tabs.md)** pour apprendre à naviguer rapidement dans les arborescences de répertoires, à maîtriser les espaces de travail multi-onglets, à enregistrer les ensembles de répertoires favoris, à utiliser des listes de véhicules recherchés instantanées et à exploiter les vues de branches plates récursives.