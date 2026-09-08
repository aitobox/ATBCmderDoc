# Chapitre 3: Opérations de fichiers et file d'attente en arrière-plan

Chaque jour, les gestionnaires de fichiers sont jugés selon une seule mesure : la rapidité, la précision et la sécurité avec lesquelles vous pouvez manipuler les données. Dans ATBCmder, vous n'aurez jamais à jongler avec plusieurs fenêtres qui se chevauchent, à subir des erreurs de chute accidentelle ou à attendre sans rien faire pendant que les transferts de fichiers volumineux gèlent votre écran. 

Ce chapitre couvre le spectre complet des opérations sur les fichiers : flux de travail de copie et de déplacement directionnels, renommage en ligne sur place, marquage puissant avec des caractères génériques, interopérabilité du système par glisser-déposer, gestion granulaire des collisions, autorisations et liens symboliques UNIX et file d'attente des opérations en arrière-plan multithread. 

---

## 1. Démarrage rapide visuel : le modèle d'opération directionnelle

Les gestionnaires de fichiers orthodoxes utilisent un modèle directionnel **Source ➔ Target**. Lorsque vous lancez un transfert de fichier ou une création de lien, ATBCmder prend les éléments sélectionnés dans le **Panneau actif** (Source) et exécute l'opération directement dans le répertoire ouvert dans le **Panneau inactif** (Cible). 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE PANEL (Source)                              INACTIVE PANEL (Target)            │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Date    │   │  Name                        Size   │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ C │  ▸ client_portal            <DIR>   │
│  ✔ schema_migration.sql      42 KB   14:12   │ O │  ▸ microservices            <DIR>   │
│  ● notes.txt                  4 KB   09:30   │ P │  ● .env.production          2.1 KB  │
│                                              │ Y │                                     │
│  [2 files selected: 1.8 GB]                  │ ➔ │  [Destination ready for ingest]     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│                         ▼ Press F5 (Copy) or F6 (Move) ▼                               │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Copy file(s)                                                                     │  │
│  │ Copy selected 2 files?                                                           │  │
│  │ To: [/Volumes/ExternalSSD/Projects                                          ] […]│  │
│  │ [Options ▼]        [Add To Queue #1 ▾]       [Cancel]               [Start (⏎)]  │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Aide-mémoire pour les opérations de base à double matrice

| Actions | Raccourci macOS | Clé de commandant classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Copier vers la cible** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copie les éléments sélectionnés dans le panneau opposé. | 
| **Copier dans le même panneau** | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Duplique les éléments dans le panneau actif avec une invite de changement de nom. | 
| **Déplacer vers la cible** | `F6` / `Fn+F6` | `F6` | `cm_Move` | Déplace les éléments sélectionnés vers le panneau opposé. | 
| **Nouveau dossier (MkDir)** | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Crée un nouveau répertoire dans le panneau actif. | 
| **Supprimer dans la corbeille** | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Déplace les éléments sélectionnés vers la corbeille macOS. | 
| **Suppression permanente** | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Contourne la corbeille et dissocie définitivement les fichiers. | 
| **Renommer rapidement en ligne**| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Renomme l'élément actif directement à l'intérieur de la ligne du tableau. | 
| **Propriétés du fichier** | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Ouvre la boîte de dialogue des autorisations UNIX, des horodatages et des métadonnées. | 
| **Calculer l'espace du dossier**| `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcule les octets récursifs pour les répertoires (`Ctrl+L` / `cm_CalculateSpace` pour le total sélectionné). | 
| **File d'attente en arrière-plan** | `Toolbar ⚡` | — | `cm_OperationsPanel` | Ouvre le moniteur de transfert en arrière-plan à 3 files d'attente. |

### Repère visuel : la barre d'outils du milieu

ATBCmder dispose d'une barre d'outils verticale dédiée à action rapide intégrée directement sur le séparateur central séparant les deux panneaux : 

![Middle Toolbar](images/middle_toolbar.png) 
*La barre d'outils centrale centrale offre un accès instantané de la souris à Afficher (F3), Modifier (F4), Copier (F5), Déplacer (F6), Nouveau dossier (F7), Supprimer (F8) et Permuter le panneau.* 

---

## 2. Opérations de base : copier, déplacer, MkDir et supprimer

La gestion quotidienne des fichiers s'articule autour de quatre actions principales : copier, déplacer, créer des répertoires et supprimer les fichiers indésirables.

### 2.1 Copie de fichiers (`F5` / `cm_Copy`)

Pour copier des fichiers ou des répertoires : 

1. **Sélectionnez** un ou plusieurs éléments dans le panneau actif à l'aide du clavier ou de la souris. 
2. **Appuyez sur `F5`** (ou `Fn+F5` sur les claviers Apple, ou cliquez sur **Copier** dans la barre d'outils centrale). 
3. La **boîte de dialogue Copier** apparaît : 
- **Ligne de destination** : automatiquement renseignée avec le chemin du répertoire actuel du panneau opposé. Vous pouvez modifier ce chemin manuellement, ajouter un nouveau nom de sous-dossier à copier et créer simultanément, ou cliquer sur `...` pour parcourir. 
- **Démarrer (`Enter`)** : commence la copie immédiate au premier plan avec une boîte de dialogue de progression en temps réel. 
- **Ajouter à la file d'attente (`F2`)** : Met en file d'attente le transfert à exécuter en arrière-plan (voir [Section 7.4](#74-file-dattente-des-operations-en-arriere-plan-cm_operationspanel)). 
- **Options** : étend les règles avancées de conflit, la préservation des attributs et les vérifications de la somme de contrôle. 

```
┌────────────────────────────────────────────────────────┐
│ Copy file(s)                                           │
│ Copy selected 3 files?                                 │
│ To: [/Volumes/Backup/Assets                          ] │
│ [Options ▼]   [Add To Queue #1 ▾]   [Cancel]   [Start] │
└────────────────────────────────────────────────────────┘
```

#### Duplication dans le panneau (`Shift+F5` / `cm_CopySamePanel`)

Pour cloner rapidement un fichier dans le répertoire actuel (par exemple, créer une sauvegarde avant de modifier `nginx.conf`) : 

- Mettez l'élément en surbrillance et appuyez sur `Shift+F5` (ou `⇧F5`). 
- ATBCmder vous demande un chemin de destination dans le *même* répertoire, vous permettant de saisir un nouveau nom (par exemple, `nginx.conf.bak`).

#### Presse-papiers macOS standard (`Cmd+C` ➔ `Cmd+V`)

ATBCmder s'intègre entièrement aux raccourcis du presse-papiers du système macOS : 

- **`Cmd+C` (`⌘C`)** : Copie les chemins de fichiers sélectionnés dans le presse-papiers (`cm_CopyToClipboard`). 
- **`Cmd+V` (`⌘V`)** : Colle les fichiers du presse-papiers dans le panneau actif (`cm_PasteFromClipboard`). 
- **`Cmd+Option+V` (`⌥⌘V`)** : Déplace les fichiers du presse-papiers dans le panneau actif (`cm_PasteAsMove`). 

---

### 2.2 Déplacement de fichiers (`F6` / `cm_Move`)

Déplacer les fichiers de transfert hors du répertoire source vers le répertoire cible : 

1. Sélectionnez les éléments et appuyez sur **`F6`** (ou `Fn+F6` / cliquez sur **Déplacer** dans la barre d'outils centrale). 
2. La **boîte de dialogue Déplacer** s'ouvre et affiche le chemin du panneau cible. 
3. Appuyez sur **`Enter`** pour exécuter : 
- **Déplacement du même système de fichiers** : instantané et atomique sur les volumes APFS/HFS+ en mettant à jour les références du catalogue du système de fichiers sans déplacer les blocs de disque bruts. 
- **Déplacement entre systèmes de fichiers** : diffuse les données sur plusieurs volumes vers la destination, vérifie l'achèvement des octets et supprime en toute sécurité la source dès son arrivée vérifiée. 
4. Si un fichier existant portant le même nom réside à la destination, ATBCmder fait une pause et appelle la **boîte de dialogue d'écrasement** (voir [Section 6](#6-gestion-des-collisions-et-resolution-des-conflits)). 

---

### 2.3 Création de nouveaux répertoires (`F7` / `cm_MkDir`)

Besoin de créer une structure de dossiers à la volée ? 

1. Appuyez sur **`F7`** (ou `Fn+F7` / `Shift+Cmd+N` / `cm_MkDir`). 
2. Une invite légère apparaît : `Enter folder name:`. 
3. Tapez le nom du dossier et appuyez sur `Enter`. 

```
┌──────────────────────────────────────────────┐
│ Create Directory                             │
│ Enter folder name:                           │
│ [2026-09-Q3_Reports                        ] │
│                      [Cancel]      [OK (⏎)]  │
└──────────────────────────────────────────────┘
```

#### Chaînage de sous-répertoires

Vous pouvez créer des hiérarchies de dossiers imbriquées en une seule étape. Taper `deep/nested/project/assets` crée instantanément les quatre niveaux hiérarchiques (équivalent à `mkdir -p`).

#### Placement de mise au point automatique

Lors de la création, ATBCmder place automatiquement le curseur du panneau directement sur le nouveau dossier, prêt pour une saisie immédiate (`Enter`) ou un transfert de fichier. 

---

### 2.4 Suppression de fichiers : corbeille macOS ou purge permanente

La sécurité et la récupérabilité sont primordiales. ATBCmder prend en charge les workflows de double suppression : 

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

#### Suppression dans la corbeille macOS (`F8` / `Delete` / `Cmd+Backspace`)

- Les fichiers sélectionnés sont acheminés via les API macOS `send2trash` vers la corbeille de votre système. 
- Les fichiers peuvent être inspectés ou restaurés à tout moment via macOS Finder ("Put Back"). 
- Les boîtes de dialogue de confirmation peuvent être activées ou supprimées dans **Préférences** (`operations.confirm_delete`).

#### Suppression immédiate permanente (`Shift+Delete` / `Shift+F8`)

- Contourne entièrement la corbeille, dissociant immédiatement les fichiers et libérant de l'espace de stockage. 
- Idéal pour effacer des machines virtuelles de plusieurs gigaoctets ou des images de disque où les limites de la mémoire tampon de la corbeille ou l'épuisement du disque empêcheraient le transfert.

#### Volumes sans prise en charge de la corbeille (détection `trash_unavailable`)

Lors de la suppression de certains partages réseau (SMB, NFS), systèmes de fichiers virtuels (`vfs://`) ou disques externes formatés avec des systèmes de fichiers FAT/exFAT existants dépourvus de répertoire `.Corbeillees`, macOS ne peut pas envoyer d'éléments dans la corbeille. 

Dans de tels cas, ATBCmder déclenche une alerte de sécurité intelligente : 
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
 
Vous pouvez choisir de **Supprimer définitivement**, **Ignorer** ou de cocher **Appliquer à tous les éléments restants** pour gérer les suppressions par lots importantes sans surveillance.

#### Déchiquetage sécurisé multi-passes (`Alt+Delete` / `cm_Wipe`)

Pour les documents sensibles, les informations d'identification ou les clés privées qui ne doivent pas rester récupérables via les outils de récupération flash brute : 

- Mettez l'élément en surbrillance et sélectionnez **Menu Fichier** → **Wipe** (`Alt+Delete` / `cm_Wipe`). 
- ATBCmder effectue un écrasement multi-passes avec des modèles de bits aléatoires et des zéros avant de dissocier l'inode. 

---

## 3. Modification rapide du nom et du nom en ligne

Renommer un seul fichier ne devrait pas nécessiter de menus complexes ou de fenêtres contextuelles de dialogue. ATBCmder permet une édition rapide et sur place des lignes de tableau. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Name                                  Ext      Size      Date Modified         │
│  ▸ [..]                                         --:--     drwxr-xr-x            │
│  ● Annual_Financial_Report_2025        .pdf     4.2 MB    Today, 11:20          │
│    ▲                                                                            │
│    └── [Editable Text Box: Stem highlighted, .pdf extension preserved]          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Déclenchement du changement de nom en ligne

1. Mettez en surbrillance n’importe quel fichier ou répertoire dans le panneau. 
2. Appuyez sur **`F2`** ou **`Shift+F6`** (`cm_RenameOnly`), ou cliquez une fois sur le nom de fichier déjà en surbrillance. 
3. La cellule du tableau se transforme en éditeur en ligne (`QLineEdit`).

### Préservation intelligente des extensions

Lorsque vous renommez un fichier tel que `invoice_september.pdf` : 

- ATBCmder présélectionne automatiquement uniquement le nom de fichier de base (`invoice_september`). 
- L'extension de fichier (`.pdf`) reste non sélectionnée et intacte, empêchant ainsi la suppression accidentelle d'extension qui romprait les associations de fichiers macOS. 
- Si vous souhaitez modifier l'extension, utilisez simplement les touches fléchées ou appuyez sur `Cmd+A` à l'intérieur de la zone d'édition.

### Raccourcis clavier clavier dans le renommage en ligne

- **`Enter` (`Return`)** : valide le nouveau nom et réindexe le panneau. 
- **`Esc`** : annule la modification et restaure le nom d'origine sans modification. 
- **`Tab`** : valide le nom actuel et commence immédiatement à renommer le fichier *suivant* dans la liste, permettant un renommage séquentiel rapide des fichiers sans quitter le clavier. 

---

## 4. Techniques de sélection : fichiers de marquage puissant

Dans les gestionnaires de fichiers traditionnels, la position de votre curseur et votre sélection sont étroitement liées : déplacer le curseur désélectionne les fichiers précédents, sauf si vous maintenez enfoncé `Cmd`. Dans ATBCmder, le **focus du curseur** et les **sélections marquées** sont découplés, permettant une préparation par lots de précision. 

```
  Status Column:
  [ ]  Unselected (cursor may or may not be on row)
  [✔]  Marked / Selected (accumulated into operation payload)
```

### 4.1 Actions de sélection globale

| Actions | Raccourci macOS | Clé classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Sélectionner tout** | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Marque chaque fichier et dossier dans le panneau actif. | 
| **Désélectionner tout** | `Cmd+Shift+A` / `⇧⌘A`| `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Efface toutes les marques du panneau actif. | 
| **Inverser la sélection**| `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | État de sélection des flips : marqués deviennent non marqués et vice versa. | 

---

### 4.2 Sélection de modèles et de caractères génériques

La sélection générique vous permet de cibler des centaines de fichiers spécifiques dans un répertoire de milliers de personnes en quelques frappes. 

```
┌────────────────────────────────────────────────────────┐
│ Mark Files by Pattern                                  │
│ Pattern: [*.jpg;*.png;*.webp                        ]  │
│                                                        │
│ [✔] Case sensitive       [ ] Regular expression        │
│                      [Cancel]                 [OK (⏎)] │
└────────────────────────────────────────────────────────┘
```

#### Groupe de marques (`Num+` / `cm_MarkPlus`)

- Appuyez sur **`Num+`** (Clavier Plus ou déclencheur depuis le menu **Marque** → **Sélectionner un groupe**). 
- Entrez les caractères génériques du shell standard : 
- `*.log` : marque tous les fichiers se terminant par `.log`. 
- `*.jpg;*.png;*.webp` : liste séparée par des points-virgules pour faire correspondre plusieurs extensions à la fois. 
- `data_2026_??.csv` : correspond aux fichiers mensuels à deux chiffres (`01` à `12`). 
- `*draft*` : correspond à tout fichier contenant le mot « draft ». 
- Appuyez sur `Enter` pour sélectionner instantanément toutes les entrées correspondantes.

#### Désélectionner le groupe (`Num-` / `cm_MarkMinus`)

- Appuyez sur **`Num-`** (Clavier Moins). 
- Entrez un modèle pour supprimer les éléments correspondants d'une sélection existante (par exemple, `*test*`).

#### Marquer tout avec la même extension (`Shift+Num+` / `cm_MarkCurrentExtension`)

- Positionnez le curseur sur n'importe quel fichier (par exemple, `app.tsx`). 
- Appuyez sur **`Shift+Num+`**. 
- Chaque fichier `.tsx` du répertoire actuel est instantanément sélectionné. 

---

### 4.3 Sélection de portée et de point

- **Sélection de bloc continu (`Shift+Up` / `Shift+Down`)** : maintenir `Shift` tout en naviguant avec les touches fléchées développe un bloc de sélection contigu vers le haut ou vers le bas. 
- **Bascule d'élément unique (`Space` / `Insert` / `cm_SelectOrDeselectFile`)** : 
- Appuyer sur `Space` marque ou décoche l'élément sous le curseur et calcule immédiatement la taille du répertoire s'il se trouve dans un dossier. 
- Appuyer sur `Insert` (ou `Fn+Return` sur certains claviers Mac) marque l'élément et fait automatiquement descendre le curseur jusqu'à la ligne suivante, permettant des passes de sélection rapides à un doigt. 
- **Souris et trackpad** : 
- `Cmd+Click` : bascule la sélection sur des lignes individuelles sans modifier les autres sélections. 
- `Shift+Click` : étend la sélection de la ligne d'ancrage actuelle à la ligne cliquée.

### Télémétrie de sélection en direct dans la barre d'état

Chaque fois que des fichiers sont marqués, la barre d'état inférieure est immédiatement mise à jour : 
```
[ 48 items | 12 selected (284.6 MB) ]   [ Volume Free: 184.2 GB / 494.3 GB ]
```
 
Vous obtenez une connaissance de la situation en temps réel des charges utiles exactes en octets avant de vous engager dans des copies ou des suppressions volumineuses. 

---

## 5. Interopérabilité par glisser-déposer

ATBCmder traite le glisser-déposer comme un citoyen de premier ordre tout en conservant une compatibilité totale avec les flux de travail orthodoxes et l'écosystème de bureau macOS. 

```
       Dual-Panel Transfer                       External macOS Desktop
 ┌──────────────┐   ┌──────────────┐       ┌──────────────┐   ┌──────────────┐
 │ Left Panel   │══►│ Right Panel  │       │ ATBCmder     │══►│ Finder / App │
 │ (Source)     │   │ (Target)     │       │ Panel        │   │ (Desktop)    │
 └──────────────┘   └──────────────┘       └──────────────┘   └──────────────┘
```

### Faire glisser entre les panneaux

- Cliquez et faites glisser les éléments marqués du panneau actif à travers le séparateur central vers le panneau inactif. 
- Déposez-le n'importe où dans la table des fichiers pour lancer le transfert vers le dossier de destination. 
- **Déposer sur un sous-dossier** : si vous déposez directement sur une ligne de sous-répertoire spécifique, ATBCmder achemine la charge utile vers ce sous-dossier plutôt que vers la racine du panneau.

### Interagir avec macOS Finder, Desktop et les applications externes

- **Glisser dans ATBCmder** : faites glisser les fichiers depuis le Finder, votre bureau ou les téléchargements AirDrop directement dans l'un des panneaux ATBCmder pour les copier ou les déplacer. 
- **Glisser hors d'ATBCmder** : faites glisser les fichiers depuis ATBCmder directement vers VS Code, Terminal (qui colle le chemin du fichier), Slack, Apple Mail ou les boîtes de téléchargement du navigateur Web.

### Touches de modification pendant le glisser

| Touche de modification | Action de glisser | Icône du curseur de la souris | Descriptif | 
| :--- | :--- | :--- | :--- | 
| **Aucun modificateur** | Action par défaut | Flèche standard | Copies sur plusieurs volumes ; se déplace dans le même volume. | 
| **Option (`⌥`)** | **Forcer la copie** | Insigne vert `+` | Copie toujours les éléments, en laissant les fichiers sources intacts. | 
| **Commande (`⌘`)** | **Déplacement forcé** | Insigne de flèche incurvée | Déplace toujours les éléments, dissociant les fichiers sources à leur arrivée. |

### Dossiers à ressort

Lorsque vous faites glisser des fichiers sur un répertoire imbriqué dans ATBCmder : 

- Passez le curseur de votre souris sur le dossier cible pendant **750 millisecondes**. 
- Le dossier clignote automatiquement et s'ouvre, naviguant à l'intérieur. 
- Vous pouvez naviguer sur plusieurs niveaux dans des sous-répertoires imbriqués sans relâcher le bouton de la souris, puis déposer votre charge utile exactement là où vous le souhaitez. 

---

## 6. Gestion des collisions et résolution des conflits

Les collisions de noms sont le moment le plus dangereux de la gestion de fichiers. L'écrasement d'un mauvais fichier peut détruire des heures de travail. ATBCmder implémente un moteur de résolution de conflits de niveau entreprise qui inspecte les fichiers avant de les écraser et fournit des contrôles de sécurité granulaires. 

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

### La répartition de la boîte de dialogue Écraser

Lorsqu'une collision cible se produit, ATBCmder affiche la boîte de dialogue **Confirmer l'écrasement du fichier** : 

1. **Inspection côte à côte des métadonnées** : 
- Compare la taille exacte des fichiers jusqu'à l'octet unique. 
- Compare les dates de modification et les horodatages. Met en évidence si le fichier source est plus récent, plus ancien ou de taille identique. 
2. **Boutons de décision sur l'élément actuel** : 
- **Écraser (`Enter`)** : remplace le fichier de destination en conflit par le fichier source. 
- **Sauter** : laisse le fichier de destination existant intact et passe à l'élément suivant du lot de transfert. 
- **Annuler (`Esc`)** : abandonne immédiatement l'opération restante, en préservant les fichiers déjà transférés. 
3. **Actions par lots et de sécurité** : 
- **Ecraser tout** : écrase silencieusement tous les fichiers en conflit ultérieurs dans cette tâche de transfert. 
- **Skip All** : ignore silencieusement tous les fichiers en conflit restants sans vous demander à nouveau. 
- **Renommer** : vous invite à saisir un nouveau nom personnalisé pour le fichier copié avant de l'écrire. 
- **Renommer automatiquement** : ajoute automatiquement un compteur incrémentiel (par exemple, `build_artifacts_1.zip`, `build_artifacts_2.zip`), garantissant que les deux versions sont conservées côte à côte sans intervention manuelle. 

---

### Politiques de collision préconfigurées dans la boîte de dialogue Copier

Pour les tâches par lots automatisées volumineuses ou les sauvegardes sans surveillance, vous pouvez préconfigurer le comportement de conflit à l'avance dans le panneau **Options** extensible de la boîte de dialogue Copier/Déplacer : 

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
 

- **Lorsque le fichier existe** : 
- `Ask` : affiche la boîte de dialogue d'écrasement à chaque collision (par défaut). 
- `Overwrite` : écrase automatiquement les fichiers existants. 
- `Skip` : ignore automatiquement les fichiers en conflit. 
- `Overwrite older` : écrase la destination uniquement si l'heure de modification de la source est plus récente. 
- `Rename copied` : ajoute le suffixe du compteur (`_1`, `_2`) aux fichiers copiés. 
- `Auto-rename target` : renomme le fichier cible existant et écrit le nouveau fichier sous le nom d'origine. 
- **Lorsque le répertoire existe** : 
- `Merge` : unit le contenu du dossier de manière récursive. Les sous-fichiers non conflictuels sont copiés dans les dossiers existants. 
- `Ask` / `Overwrite` / `Skip`. 
- **Vérification et attributs avancés** : 
- **Vérifier l'espace libre / Réserver de l'espace** : précalcule les octets sources et garantit que le volume de destination dispose d'une capacité adéquate avant de démarrer. 
- **Vérifier après copie** : calcule les sommes de contrôle cryptographiques (`SHA-256`, `MD5`, `SHA-1`, `CRC32`) sur les fichiers source et de destination écrits pour garantir l'intégrité des données à 100 % contre la corruption silencieuse du stockage. 
- **Suivre les liens** : contrôle si les liens symboliques sont copiés en tant que références de pointeur ou déréférencés en copies physiques complètes. 
- **Copier la date/l'heure et la propriété** : préserve les dates de création POSIX, les horodatages de modification et les identifiants de propriété des utilisateurs/groupes. 

---

## 7. ⚡ Conseils de pro et analyse approfondie : puissance avancée du système de fichiers

Maîtriser la gestion à double panneau signifie comprendre le substrat UNIX sous-jacent de macOS. Voici des fonctionnalités puissantes conçues pour les développeurs, les administrateurs système et les professionnels du stockage.

### 7.1 Liens symboliques et liens physiques (`cm_SymLink`, `cm_HardLink`)

macOS est construit sur Darwin UNIX, fournissant deux types de liens distincts : 

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

#### Création de liens symboliques (`cm_SymLink`)

1. Mettez en surbrillance un ou plusieurs fichiers/dossiers dans le panneau actif. 
2. Sélectionnez **Menu Fichier** → **Créer un lien symbolique...** (`cm_SymLink`). 
3. ATBCmder génère automatiquement un lien symbolique dans le panneau opposé pointant vers le chemin absolu de l'élément source. 
4. Les liens symboliques affichent un indicateur d'attribut `l` distinct (par exemple, `lrwxr-xr-x`) dans le panneau.

#### Création de liens physiques (`cm_HardLink`)

1. Mettez en surbrillance les fichiers sur un volume APFS/HFS+ local. 
2. Sélectionnez **Menu Fichier** → **Créer un lien physique...** (`cm_HardLink`). 
3. ATBCmder crée une entrée de répertoire supplémentaire dans le panneau cible partageant exactement le même inode. 
4. Les modifications écrites dans l'un ou l'autre fichier se reflètent instantanément dans les deux. La suppression d'un fichier ne supprime pas les données tant que le nombre de liens n'atteint pas zéro. 

> [!NOTE] 
> **Restrictions des limites des liens** : les liens physiques ne peuvent pas franchir les limites des volumes ni être créés sur des partages réseau (`vfs://`). Les liens symboliques doivent être utilisés lors de la liaison entre différents lecteurs ou points de montage distants. 

---

### 7.2 Autorisations et attributs des fichiers (`Alt+Enter` / `cm_SetFileProperties`)

Inspectez et modifiez les attributs du fichier POSIX à l'aide de la **boîte de dialogue Propriétés** complète : 

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
 

1. **Déclencheur** : mettez en surbrillance n'importe quel fichier ou répertoire et appuyez sur **`Alt+Enter`** (`⌥⏎` / `cm_SetFileProperties`). 
2. **Révision des métadonnées** : affichez le chemin complet du fichier, les octets exacts, l'heure de création (`btime`), l'heure de modification (`mtime`) et l'heure du dernier accès (`atime`). 
3. **Matrice des autorisations UNIX** : 
- **Boxes à cocher interactives** : activez indépendamment les autorisations de lecture (`r`), d'écriture (`w`) et d'exécution (`x`) pour **Propriétaire**, **Groupe** et **Autres**. 
- **Entrée octale bidirectionnelle** : saisissez des nombres octaux directement dans le champ **Mode octal** (par exemple, `755` pour les exécutables, `644` pour les documents standard, `600` pour les clés SSH privées). Les cases à cocher se mettent à jour en temps réel, et vice versa. 
4. Appuyez sur `OK` (`Enter`) pour appliquer les modifications via POSIX `chmod`. 

---

### 7.3 Calcul de l'espace occupé (`cm_CountDirContent` / `cm_CalculateSpace` / `Space`)

Par défaut, les gestionnaires de fichiers affichent la taille des répertoires sous la forme `<DIR>` ou `--`, car le calcul récursif de la taille des dossiers sur des millions de fichiers dégraderait les performances du système de fichiers. ATBCmder vous offre un calcul instantané et à la demande : 

- **Taille de dossier unique (`Space` / `Insert` / `cm_SelectOrDeselectFile`)** : Appuyez sur `Space` tout en vous reposant sur n'importe quel dossier. ATBCmder calcule le nombre total d'octets récursifs du dossier en arrière-plan et remplace `<DIR>` par la taille exacte (par exemple, `14.2 GB`). 
- **Tous les dossiers du panneau actif (`Alt+Shift+Enter` / `⌥⇧⏎` / `cm_CountDirContent`)** : 
- Analyse tous les répertoires visibles dans le panneau actuel. 
- Met à jour les lignes du tableau avec des totaux d'octets précis. 
- **Taille cumulée du répertoire sélectionné (`Ctrl+L` / `⌃L` / `cm_CalculateSpace`)** : 
- Accumule le nombre total d'octets récursifs pour les dossiers sélectionnés et résume le nombre de fichiers, le nombre de dossiers et la taille de stockage dans la barre d'état. 

---

### 7.4 File d'attente des opérations en arrière-plan (`cm_OperationsPanel`)

La copie de gros tournages vidéo de 50 Go ou le transfert de centaines de milliers de petits fichiers de code source ne devraient jamais geler votre gestionnaire de fichiers. ATBCmder intègre un **moteur de transfert asynchrone à 3 files d'attente**. 

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

#### Pourquoi trois files d'attente indépendantes ?

- **Sérialisé dans chaque file d'attente** : les tâches dans la **file d'attente n°1** s'exécutent les unes après les autres dans un ordre FIFO strict. Cela évite les problèmes de tête de disque sur les disques durs mécaniques et évite les goulots d'étranglement de contention. 
- **Parallèle entre files d'attente** : **Queue #1**, **Queue #2** et **Queue #3** fonctionnent simultanément sur des threads d'arrière-plan distincts (`QThread`). Vous pouvez attribuer des transferts ciblant **NVMe SSD A** à la file d'attente n°1, des transferts ciblant le **lecteur USB externe B** à la file d'attente n°2 et des téléchargements de NAS réseau vers la file d'attente n°3, pour obtenir un débit de bus global maximal.

#### Envoi de tâches vers la file d'attente

1. Dans le panneau actif, sélectionnez vos fichiers et appuyez sur `F5` (Copier) ou `F6` (Déplacer). 
2. Au lieu de cliquer sur Démarrer, cliquez sur **Ajouter à la file d'attente n°1** (ou cliquez sur le chevron déroulant pour sélectionner **Queue n°2** ou **Queue n°3**). 
3. La boîte de dialogue se ferme immédiatement, libérant la fenêtre principale pour une navigation et une navigation continues.

#### Gestion de la fenêtre de file d'attente (`cm_OperationsPanel`)

- Cliquez sur le bouton **⚡ File d'attente** dans la barre d'outils principale ou sélectionnez **Commandes de menu** → **Opérations en arrière-plan** (`cm_OperationsPanel`). 
- **Télémétrie en temps réel** : inspectez les tâches actives, les fichiers en cours de transfert, les vitesses de transfert en streaming (par exemple, `428.5 MB/s`) et les comptes à rebours ETA calculés. 
- **Statuts codés par couleur** : 
- `[QUEUED]` : Faire la queue. 
- `[RUNNING]` : transfert actif de données. 
- `[COMPLETED]` : terminé avec succès avec un nombre d'octets vérifié. 
- `[FAILED]` : rencontré une erreur d'E/S (message d'erreur affiché en ligne). 
- `[CANCELLED]` : abandonné par l'utilisateur. 
- **Actions de contrôle** : 
- **Annuler la tâche** : termine en toute sécurité le transfert sélectionné en file d'attente ou en cours d'exécution. 
- **Effacer terminé** : supprime les tâches terminées, échouées et annulées de la liste. 
- **Résolution des conflits en arrière-plan** : si une tâche en arrière-plan rencontre un conflit d'écrasement, ATBCmder génère une notification vous permettant de le résoudre sans abandonner les autres tâches simultanées. 

---

## 8. Recettes pratiques étape par étape

### Recette 1 : Sauvegarde multi-volumes sécurisée avec vérification de la somme de contrôle

**Objectif** : Sauvegardez une archive de photos de grande valeur depuis votre Mac sur un lecteur APFS externe, garantissant ainsi l'absence de corruption silencieuse et résolvant les doublons potentiels en toute sécurité. 

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
 
*Résultat : ATBCmder calcule les hachages SHA-256 pendant le flux de copie, confirme l'intégrité exacte des blocs sur le disque externe et numérote automatiquement tout instantané en conflit sans intervention humaine.* 

---

### Recette 2 : Staging de précision : sélection de caractères génériques, inversion et déploiement de liens symboliques

**Objectif** : dans un référentiel mixte contenant du code et des artefacts compilés, sélectionnez tous les fichiers JavaScript, TypeScript et JSON tout en ignorant les sorties `.map` et `.log` compilées, puis créez un lien symbolique vers un dossier de banc d'essai. 

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
 
*Résultat : Quatre-vingt-quatre liens symboliques sont instantanément créés dans le dossier du banc de test, pointant proprement vers vos fichiers sources actifs.* 

---

### Recette 3 : Ingestion parallèle à haut débit à l'aide de files d'attente en arrière-plan

**Objectif** : déchargez simultanément deux grandes cartes de caméra multimédia sur le RAID de votre station de travail sans verrouiller l'interface utilisateur ni ralentir l'un ou l'autre des lecteurs de cartes. 

```
Step 1: Mount Card A (/Volumes/CFexpress_A) in Left Panel.
Step 2: Select all raw footage (Cmd+A), press F5 (Copy).
Step 3: Click [Add To Queue #1]. Transfer begins streaming in background.
Step 4: Open Card B (/Volumes/SD_Card_B) in Left Panel (Cmd+T for a new tab).
Step 5: Select all audio tracks (Cmd+A), press F5 (Copy).
Step 6: Click the queue dropdown chevron and choose [Queue #2].
Step 7: Press Toolbar ⚡ (cm_OperationsPanel) to watch both queues stream concurrently.
```
 
*Résultat : les deux cartes ingèrent simultanément à pleine saturation du bus matériel pendant que vous continuez à parcourir les fichiers, à modifier des notes ou à renommer des ressources.* 

---

## 9. Alertes de sécurité et de système

> [!WARNING] 
> **Suppression définitive sur les disques externes et réseau** : 
> Les disques externes formatés avec FAT32, exFAT ou NTFS (via des pilotes tiers) et les partages réseau distants (SMB/SFTP) manquent souvent d'un répertoire système macOS `.Corbeillees`. Lors de la suppression d'éléments de ces volumes, ATBCmder vous avertira que la corbeille n'est pas disponible. La confirmation de cette action **supprime définitivement** les fichiers. Vérifiez toujours les en-têtes de chemin avant de confirmer. 

> [!CAUTION] 
> **Écrasement de fichiers dans les opérations par lots** : 
> Lorsque vous utilisez **Overwrite All** dans la boîte de dialogue de collision, ATBCmder supprime les autres alertes de collision pour l'ensemble de cette tâche. Si votre répertoire source contient des noms de fichiers en double accidentels, les fichiers cibles existants seront remplacés de manière irréversible. Pensez à utiliser **Renommer automatiquement** ou **Écraser l'ancienne** pour les copies par lots sans surveillance. 

> [!IMPORTANT] 
> **Limites du lien physique APFS** : 
> Les liens physiques ne peuvent pas s'étendre sur différents volumes APFS, partitions de disque ou images disque. Si vous tentez de créer un lien physique entre deux points de montage différents (tels que `/Users/...` à `/Volumes/ExternalDrive/...`), l'opération échouera. Utilisez des **Liens symboliques** (`cm_SymLink`) lors de la création de liens entre différents volumes de stockage. 

> [!TIP] 
> **Optimisation des vitesses de transfert NVMe** : 
> ATBCmder est optimisé pour la mémoire unifiée Apple Silicon moderne et les SSD PCIe 4.0/5.0 NVMe. Par défaut, les opérations sur les fichiers utilisent un **tampon de copie de 1 Mo** hautes performances (`operations.copy_buffer_size`). Vous pouvez affiner ce tampon sous **Préférences** → **Opérations sur les fichiers** pour correspondre aux interfaces réseau 10GbE haut de gamme ou aux baies de stockage spécialisées. 

---

## 10. Tableau de référence du clavier à double matrice

| Catégorie | Actions | Raccourci macOS | Clé classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | :--- | 
| **Opérations de fichiers de base** | Copier vers la cible | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copie les éléments sélectionnés dans le panneau inactif. | 
| | Copier dans le même panneau | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Clone le fichier dans le panneau actif avec une invite de changement de nom. | 
| | Déplacer vers la cible | `F6` / `Fn+F6` | `F6` | `cm_Move` | Déplace les éléments sélectionnés vers le panneau inactif. | 
| | Nouveau répertoire | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Crée un nouveau répertoire ou une arborescence imbriquée. | 
| | Supprimer dans la corbeille | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Envoie les éléments sélectionnés vers la corbeille macOS. | 
| | Suppression permanente | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Dissocie les fichiers immédiatement sans corbeille. | 
| | Effacement sécurisé | `Alt+Delete` / `⌥⌦` | `Alt+Delete` | `cm_Wipe` | Écrase les fichiers avec des données aléatoires avant de les dissocier. | 
| **Renommer** | Renommer rapidement en ligne| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Renomme l'élément actif directement dans la ligne du tableau. | 
| | Boîte de dialogue Renommer | *Menu Fichier* | — | `cm_Rename` | Ouvre la boîte de dialogue de texte modale pour renommer. | 
| **Sélection** | Sélectionner tout | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Sélectionne tous les fichiers et dossiers. | 
| | Désélectionner tout | `Cmd+Shift+A` / `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Efface toutes les sélections. | 
| | Inverser la sélection | `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Inverse l'état de sélection de tous les éléments. | 
| | Marquer le groupe | `Num+` | `Num+` | `cm_MarkPlus` | Sélectionne les éléments par caractère générique ou modèle RegEx. | 
| | Décocher le groupe | `Num-` | `Num-` | `cm_MarkMinus` | Désélectionne les éléments par motif générique. | 
| | Même extension | `Shift+Num+` | `Shift+Num+` | `cm_MarkCurrentExtension`| Sélectionne tous les éléments avec la même extension de fichier. | 
| | Basculer la sélection | `Space` / `Insert` | `Insert` / `Space` | `cm_SelectOrDeselectFile` | Bascule la sélection des éléments et descend. | 
| **Presse-papiers** | Copier dans le Presse-papiers | `Cmd+C` / `⌘C` | `Ctrl+C` | `cm_CopyToClipboard` | Copie les chemins de fichiers dans le presse-papiers du système. | 
| | Couper dans le Presse-papiers | `Cmd+X` / `⌘X` | `Ctrl+X` | `cm_CutToClipboard` | Coupe les chemins de fichiers dans le presse-papiers du système. | 
| | Coller le Presse-papiers | `Cmd+V` / `⌘V` | `Ctrl+V` | `cm_PasteFromClipboard` | Colle les fichiers du presse-papiers dans le panneau actif. | 
| | Coller en tant que déplacement | `Cmd+Option+V` / `⌥⌘V`| `Ctrl+Alt+V` | `cm_PasteAsMove` | Déplace les fichiers du presse-papiers dans le panneau actif. | 
| | Copier le chemin complet | *Menu Modifier* | — | `cm_CopyFullPath` | Copie le chemin UNIX absolu dans le presse-papiers. | 
| | Copier le nom du fichier | *Menu Modifier* | — | `cm_CopyFileNameToClip` | Copie le nom du fichier dans le presse-papiers. | 
| **Liens et espace** | Créer un lien symbolique | *Menu Fichier* | — | `cm_SymLink` | Crée un lien symbolique dans le panneau cible. | 
| | Créer un lien physique | *Menu Fichier* | — | `cm_HardLink` | Crée un lien physique dans le panneau cible. | 
| | Propriétés / Chmod | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Ouvre les autorisations, le chmod octal et les horodatages. | 
| | Calculer l'espace | `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcule les tailles de répertoires récursifs (`Ctrl+L` / `cm_CalculateSpace` pour le total sélectionné). | 
| **File d'attente de transfert**| File d'attente en arrière-plan | `Toolbar ⚡` | — | `cm_OperationsPanel` | Ouvre le moniteur de transfert en arrière-plan à 3 files d'attente. |

--- 

<div align="center"> 
<p>Maintenant que vous maîtrisez les opérations quotidiennes sur les fichiers, les techniques de sélection et les transferts en arrière-plan :</p> 
<p><strong><a href="viewers_and_editors.md">Passer au chapitre 4 : Liste universelle et éditeurs intégrés &rarr;</a></strong></p> 
</div>