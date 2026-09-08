# Bienvenue sur ATBCmder

[![macOS](https://img.shields.io/badge/platform-macOS%2012%2B-blue.svg)](download.md) 
[![Architecture](https://img.shields.io/badge/arch-Apple%20Silicon%20(ARM64)-orange.svg)](download.md) 
[![Release](https://img.shields.io/badge/release-latest-green.svg)](download.md) 
[![Privacy](https://img.shields.io/badge/telemetry-zero%20tracking-brightgreen.svg)](privacy_policy.md) 

Bienvenue sur le portail de documentation officiel de **ATBCmder**, le gestionnaire de fichiers rapide à double panneau, doté d'un clavier d'abord, conçu spécifiquement pour macOS. ATBCmder allie l'héritage de vitesse et de commande des gestionnaires de fichiers orthodoxes (Total Commander, Double Commander, Norton Commander) avec une conception macOS moderne, une intégration système native et des outils électriques avancés. 

---

## La philosophie du double panneau

Les gestionnaires de fichiers de bureau traditionnels à fenêtre unique comme macOS Finder obligent les utilisateurs à ouvrir un cycle sans fin de fenêtres qui se chevauchent, à perdre la trace des dossiers source et de destination et à risquer des chutes accidentelles dans de mauvais sous-dossiers. 

```
Navigation traditionnelle (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Dossier A (J'étais où?)│ ──?  │ Dossier B (Lequel ?)   │  → Fenêtres superposées, perte
└────────────────────────┘      └────────────────────────┘    de focus et glissers erronés

La méthode ATBCmder (Double panneau orthodoxe):
┌───────────────────────────────┬───────────────────────────────┐
│     PANNEAU ACTIF (Source)    │    PANNEAU INACTIF (Cible)    │
│  Fichiers prêts pour l'action │  Destination prévisible       │
│  [ Copier / Déplacer / Synchro ════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘
```
 

ATBCmder résout ce problème grâce au **paradigme à double panneau source-cible** : 

- **Une vision claire et permanente** : deux vues de répertoire indépendantes sont visibles côte à côte à tout moment. 
- **Opérations directionnelles prévisibles** : lorsque vous déclenchez la copie (`F5`) ou le déplacement (`F6`), ATBCmder transfère automatiquement les éléments du **Panneau actif** (où se trouve votre curseur) vers le **Panneau inactif** (la vue opposée). Pas de glisser, pas de devinettes, pas de recherche de fenêtres de destination cachées. 
- **Vitesse du clavier** : gardez vos mains sur le clavier. Parcourez les répertoires, sélectionnez les fichiers avec des caractères génériques, inspectez les archives et exécutez des transformations par lots en quelques millisecondes. 
- **Zero Finder Window Clutter** : Une seule fenêtre gère tout : volumes locaux, serveurs réseau (FTP, SFTP, SMB, WebDAV), contenus d'archives (`.zip`, `.7z`, `.tar`) et files d'attente de transfert en arrière-plan. 

---

## Visite guidée de l'interface et zones clés

ATBCmder organise la puissance et la productivité dans une présentation claire et intuitive conçue pour vous donner une connaissance instantanée de la situation des deux répertoires. 

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Barre de menus : Fichier   Marquer   Commandes   Affichage   Options   Aide          │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Barre d'outils : [🔍 Recherche]  [⚡ File d'attente]  [⚙️ Réglages]  [📁 Disques]     │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Fil d'Ariane : 🏠 > Users > brain > work│ [3] Fil d'Ariane : 💾 > Volumes > Backup   │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Onglets : [Projet Alpha ✕] [Docs] [+]   │ [4] Onglets : [Archive 2026 ✕] [+]         │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Panneau gauche (Actif / Source)  │ [6]  │ [5] Panneau droit (Inactif / Cible)        │
│ 📁 .. [Dossier parent]               │  M   │ 📁 .. [Dossier parent]                     │
│ 📁 assets                            │  I   │ 📁 archive_2025                            │
│ 📁 src                               │  L   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  I   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  E   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  U   │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Barre d'état : 6 éléments | 2 sélectionnés   │ Disque : 142.6 Go libres / 494.3 Go    │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Référence de référence de l'interface utilisateur

1. **Barre de menus et intégration native de macOS (`[1]`)** : prise en charge complète du menu de l'application macOS, raccourcis standard (`⌘,`, `⌘Q`, `⌘W`) et accès complet au menu de chaque commande interne du Commander (`cm_*`). 
2. **Barre d'outils principale et lanceurs rapides (`[2]`)** : accès immédiat en un clic à la recherche (`Alt+F7`), à la file d'attente de transfert en arrière-plan (`cm_OperationsPanel`), aux préférences (`Cmd+,`) et aux sélecteurs de lecteur. 
3. **Barre de chemin de navigation interactive (`[3]`)** : cliquez sur n'importe quel segment de répertoire dans le chemin pour sauter directement dans la hiérarchie. Cliquez sur la flèche déroulante du segment pour parcourir les sous-répertoires. 
4. **Onglets de dossier et espaces de travail (`[4]`)** : ouvrez un nombre illimité d'onglets dans chaque panneau (`Cmd+T`), fermez les onglets (`Cmd+W`), verrouillez les emplacements favoris et enregistrez l'intégralité des espaces de travail à onglets à deux panneaux (`cm_SaveFavoriteTabs`). 
5. **Panneaux de fichiers doubles (`[5]`)** : tables de fichiers indépendantes. Le panneau actif affiche une bordure d'accent distincte et un curseur ciblé. Changez de focus instantanément avec `Tab`. 
6. **Barre d'outils centrale et séparateur déplaçable (`[6]`)** : une bande verticale à action rapide placée directement sur le séparateur de panneau. Fournit des déclencheurs en un clic pour afficher (`F3`), modifier (`F4`), copier (`F5`), déplacer (`F6`), nouveau dossier (`F7`), supprimer (`F8`), effacer et permuter les panneaux. (`cm_Exchange`). Faites glisser le séparateur vers la gauche ou la droite pour redimensionner les panneaux. 
7. **Barre d'état et compteur de stockage de lecteur (`[7]`)** : affiche le nombre de fichiers en direct, les statistiques des éléments sélectionnés, la taille globale des octets et une jauge de capacité de stockage de volume actif avec calcul de l'espace libre. 

---

## Vitrine des interfaces

Explorez les capacités d'ATBCmder à travers les principales fonctionnalités : 

| Panneaux doubles et vue arborescente | Barre d'outils d'action rapide centrale | 
| :---: | :---: | 
| ![Tree View and Thumbnail Display](images/treeview+thumbview.png) | ![Middle Toolbar](images/middle_toolbar.png) | 
| *Disposition à deux panneaux avec arborescence de répertoires et aperçu miniature.* | *Bande d'action rapide : Afficher, Modifier, Copier, Déplacer, MkDir, Supprimer, Effacer.* | 

| Commandes en langage naturel | Vue arborescente plate (Flat Branch View) récursive | 
| :---: | :---: | 
| ![Natural Language File Search](images/semantic_command.png) | ![Flat View of Nested Directories](images/branch_view.png) | 
| *Recherche instantanée optimisée par macOS Spotlight et analyse sémantique des requêtes.* | *Vue des branches (`Cmd+B`) affichant le contenu imbriqué dans une seule liste plate.* | 

| Réseau et VFS distant | Archiver VFS (aucune extraction nécessaire) | 
| :---: | :---: | 
| ![Network VFS](images/network_vfs.png) | ![Archive VFS](images/archive_vfs.png) | 
| *Connectez-vous aux partages réseau FTP, SFTP, WebDAV et SMB/Samba.* | *Parcourez et modifiez les archives ZIP, TAR, 7z comme des dossiers standard.* | 

---

## Choisissez votre chemin

Que vous n'ayez jamais touché à un outil à double panneau auparavant ou que vous ayez passé deux décennies à utiliser Total Commander, ATBCmder offre une voie à suivre optimisée :

### 🟢 Piste A : Nouveau dans les gestionnaires de fichiers à double panneau ?

*Bienvenue dans une manière plus rapide et plus propre de gérer les fichiers sur macOS.* 

Si vous utilisez le Finder ou des systèmes d'exploitation de bureau standard, les gestionnaires de fichiers orthodoxes peuvent sembler peu familiers au début. Une fois que vous aurez appris les modèles de base, vous ne voudrez plus jamais glisser des fichiers sur des fenêtres dispersées : 

1. **Commencez par les concepts de base** : lisez [Chapitre 1 : Principes de base et configuration de macOS](getting_started.md) pour comprendre les panneaux actifs et inactifs, la barre d'outils centrale et l'octroi d'autorisations de disque macOS. 
2. **Maîtrisez les opérations quotidiennes** : Apprenez à copier, déplacer, renommer et supprimer sans toucher votre souris dans [Chapitre 3 : Opérations quotidiennes sur les fichiers et file d'attente](file_operations.md). 
3. **Prévisualisez tout instantanément** : découvrez comment prévisualiser des images, écouter des fichiers audio, lire du code et inspecter des PDF d'une seule touche dans [Chapitre 4 : Listeur et éditeurs universels](viewers_and_editors.md). 
4. **Suivez les guides pratiques** : découvrez les flux de travail pratiques quotidiens et les questions courantes dans le [Chapitre 9 : Recettes et dépannage du monde réel](faq_howtos.md). 

---

### ⚡ Piste B : Migrer depuis Total Commander / Double Commander ?

*Toutes les puissances et réflexes de clavier que vous connaissez, conçus nativement pour macOS.* 

ATBCmder a été créé pour apporter l'expérience Commander authentique aux macOS modernes sans exécuter de X11 encombrant, de wrappers de vin ou de ports hérités non maintenus : 

1. **Maîtrisez les combinaisons de touches à double matrice** : consultez notre matrice complète de raccourcis côte à côte (`macOS Cmd` vs `Commander Fn`) dans [Chapitre 8 : Raccourcis clavier clavier principaux] (keyboard_shortcuts.md). 
2. **Exploitez les outils électriques avancés** : utilisez l'outil de renommage multiple par lots (`Ctrl+M`), la comparaison de fichiers côte à côte (`Meta+Shift+F12`), la synchronisation des dossiers (`Shift+F12`) et la recherche avancée dans [Chapitre 5 : Outils électriques et automatisation] (power_tools.md). 
3. **Connectez-vous aux systèmes distants et virtuels** : parcourez et modifiez directement les archives `.zip` et `.tar` avec reconditionnement en direct, ou gérez les serveurs distants via SFTP, SMB et WebDAV dans le [Chapitre 6 : Systèmes de fichiers virtuels et réseau] (network_and_vfs.md). 
4. **Personnalisez et portez votre configuration** : reliez les commandes, configurez le comportement d'actualisation automatique et exportez votre XML de configuration dans [Chapitre 7 : Préférences et personnalisation] (preferences_and_customization.md). 

---

## Table des matières principale

Explorez la suite complète de documentation ATBCmder :

### 🚀 [Chapitre 1 : Principes de base et configuration de macOS](getting_started.md)

Comprenez la philosophie du double panneau, explorez l'anatomie de l'interface, configurez les autorisations macOS App Sandbox via l'assistant d'intégration (`cm_GrantFilesystemAccess`), définissez les remplacements de langue du système dans plus de 30 paramètres régionaux et personnalisez les thèmes clairs/sombres.

### 🧭 [Chapitre 2 : Onglets de navigation et de dossiers](navigation_and_tabs.md)

Déplacez-vous sans effort dans les arborescences de répertoires à l'aide du fil d'Ariane interactif, des raccourcis clavier (`Ctrl+\`, `Backspace`), de l'organisation multi-onglets (`Cmd+T`, `Cmd+W`), des ensembles d'espaces de travail favoris à deux panneaux (`cm_SaveFavoriteTabs`), des signets de la liste de favoris de l'annuaire. (`Ctrl+D`) et des modes d'affichage flexibles (Brief, Colonnes complètes, Miniatures, Arborescence et Branche plate `Cmd+B`).

### 📁 [Chapitre 3 : Opérations quotidiennes sur les fichiers et file d'attente](file_operations.md)

Effectuez des opérations de fichiers rapides et solides : copie (`F5`), déplacement (`F6`), nouveau dossier (`F7`), suppression dans la corbeille (`F8`) et renommage rapide en ligne (`F2`). Maîtrisez les sélections de caractères génériques et d'attributs, l'interopérabilité par glisser-déposer, la résolution des conflits de collision, les autorisations octales UNIX (`Alt+Enter`) et la surveillance des transferts asynchrones via la file d'attente des opérations en arrière-plan (`cm_OperationsPanel`).

### 👁️ [Chapitre 4 : Lister universel et éditeurs intégrés](viewers_and_editors.md)

Inspectez les fichiers sans lancer de logiciels tiers lourds. Utilisez Quick View (`Ctrl+Q` / `Cmd+Q`) pour les aperçus en direct du panneau latéral et Universal Lister (`F3`) pour les documents Word, les feuilles de calcul, les bases de données SQLite, les blocs-notes Jupyter, les EPUB, le code avec mise en évidence de la syntaxe, l'inspection des octets hexadécimaux bruts (`2`), les annotations d'image et filigrane (`F4`), lecteur de documents PDF et lecteurs multimédias audio/vidéo intégrés avec lecture audio en arrière-plan. Modifiez les fichiers directement avec l'éditeur de texte intégré (`F4`).

### ⚡ [Chapitre 5 : Outils électriques et automatisation](power_tools.md)

Automatisez les défis de gestion de fichiers complexes : renommage multiple par lots (`Ctrl+M`) avec jetons et substitution RegEx, comparaison de fichiers visuels côte à côte (`Meta+Shift+F12`), synchronisation d'annuaire bidirectionnelle (`Shift+F12`), recherche multi-filtres avancée (`Alt+F7`) avec "Feed to Listbox", Spotlight et langage naturel Commandes sémantiques (`/`), séparateur et éditeur de fichiers, vérification de la somme de contrôle (MD5, SHA-256, CRC32), effacement multi-passes sécurisé (`cm_Wipe`) et terminal intégré (`Ctrl+J`).

### 🌐 [Chapitre 6 : Systèmes de fichiers virtuels et réseau](network_and_vfs.md)

Traitez les serveurs distants et les archives compressées comme des dossiers locaux ordinaires à l'aide d'URI `vfs://` unifiés. Naviguez dans les archives `.zip`, `.tar` et `.7z` sans décompression, modifiez les fichiers sur place avec le reconditionnement automatisé en direct, créez des archives cryptées (`Alt+F5`) et gérez les connexions persistantes sur les partages réseau FTP, SFTP (clés SSH), WebDAV et SMB/Samba.

### ⚙️ [Chapitre 7 : Préférences et personnalisation](preferences_and_customization.md)

Configurez ATBCmder pour qu'il corresponde exactement à votre style de travail. Recherchez et associez les raccourcis clavier primaires/secondaires avec des avertissements de conflit en temps réel, personnalisez les colonnes de la table de fichiers et les règles d'ajustement automatique, ajustez la sensibilité d'actualisation automatique de l'observateur de fichiers, définissez des associations d'extensions de fichiers personnalisées et exportez/importez des profils de configuration portables (`cm_ExportConfiguration`).

### ⌨️ [Chapitre 8 : Raccourcis clavier clavier principal](keyboard_shortcuts.md)

Guide de référence complet des raccourcis à double matrice comparant les raccourcis macOS natifs (modificateurs `Cmd`) avec les touches de fonction Commander classiques (`F1`-`F12`). Comprend des instructions dédiées au comportement du modificateur du clavier Apple `Fn` et à la configuration des « touches de fonction standard » de macOS.

### ❓ [Chapitre 9 : Recettes du monde réel et dépannage](faq_howtos.md)

Procédures pas à pas pratiques pour les tâches courantes du monde réel : synchronisation des sauvegardes de répertoires, renommage par lots des bibliothèques de photos d'appareils photo avec horodatages, montage de lecteurs NAS réseau, mise à jour des fichiers de configuration dans des archives distantes et diagnostic des erreurs d'autorisation du bac à sable macOS ou des problèmes d'actualisation automatique.

### 📥 [Chapitre 10 : Téléchargement et installation](download.md)

Options d'installation pour macOS 12.0+ Monterey via Sequoia. Téléchargez directement depuis le Mac App Store ou récupérez les packages d'installation DMG autonomes conçus nativement pour Apple Silicon (architecture M1/M2/M3/M4, ARM64). *Remarque : les Mac Intel (x86_64) ne sont actuellement pas pris en charge.* 

---

### 🔒 [Annexe : Politique de confidentialité et sécurité des données](privacy_policy.md)

Notre engagement fondamental en matière de confidentialité des utilisateurs : ATBCmder n'inclut aucun suivi, aucune journalisation télémétrique et aucune analyse en arrière-plan. Toutes les opérations sur les fichiers, les informations d'identification réseau et les index de recherche restent strictement locaux sur votre Mac. 

--- 

<div align="center"> 
<p>Prêt à commencer ?</p> 
<p><strong><a href="getting_started.md">Passer au chapitre 1 : Principes de base et configuration de macOS &rarr;</a></strong></p> 
</div>