# Chapitre 8: Répertoire principal des raccourcis clavier

ATBCmder est conçu dès le départ comme un gestionnaire de fichiers axé sur le clavier. Chaque opération de fichier, saut de répertoire, transformation de vue et utilitaire de traitement par lots peut être exécuté sans aucune interaction avec la souris. 

Pour relier les traditions orthodoxes de Commander avec l'ergonomie native d'Apple, ATBCmder utilise une **architecture de clavier à double matrice** : chaque commande peut être invoquée à l'aide des touches de fonction classiques de Commander (`F1`–`F12`, `Insert`, pavé numérique) ou d'accords de modification natifs de macOS (`⌘` Command, `⌥` Option, `⇧` Shift, `⌃` Contrôle). 

---

## 1. La philosophie à double matrice et la notation clé

Que vous disposiez de vingt ans de mémoire musculaire de Total Commander et Norton Commander ou que vous viviez entièrement avec les raccourcis natifs du Finder macOS, ATBCmder s'adapte à vos réflexes dès le départ sans nécessiter de remappage manuel. 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARCHITECTURE CLAVIER DOUBLE MATRICE                      │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  PARADIGME COMMANDER CLASSIQUE       │  PARADIGME MACOS NATIF               │
│  • Touches de fonction (F1–F12)      │  • Combinaisons de touches (⌘, ⌥, ⇧, ⌃)│
│  • Marquage pavé numérique (+, -, *) │  • Parité Finder (⌘C, ⌘V, ⌘⌫, ⏎)     │
│  • Vitesse de frappe maximale        │  • Intégration à la barre de menus   │
│  Exemples :                          │  Exemples :                          │
│    F5        ➔ Copier les fichiers   │    ⌘C ➔ ⌘V   ➔ Copier les fichiers   │
│    F6        ➔ Déplacer les fichiers │    ⌘C ➔ ⌥⌘V  ➔ Déplacer les fichiers │
│    Shift+F4  ➔ Créer un fichier texte│    ⇧⌘4       ➔ Créer un fichier texte│
│    Alt+F7    ➔ Chercher des fichiers │    ⌥⌘F       ➔ Chercher des fichiers │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Symboles de modification du clavier Apple

Tout au long de ce guide et dans les boîtes de dialogue des préférences d'ATBCmder, les combinaisons de touches sont représentées à l'aide de glyphes typographiques macOS standard : 

| Glyphe | Nom du modificateur | Windows/équivalent PC | Descriptif | 
| :---: | :--- | :--- | :--- | 
| **`⌘`** | **Commande** (`Cmd`) | `Win` / `Ctrl` | Touche de modification d'action principale de macOS. | 
| **`⌥`** | **Option** (`Alt`) | `Alt` | Modificateur secondaire pour les actions alternatives et les caractères spéciaux. | 
| **`⇧`** | **Maj** | `Shift` | Étend les sélections, inverse les actions ou active les modes majuscules. | 
| **`⌃`** | **Contrôle** (`Ctrl`) | `Ctrl` | Contrôle du terminal et modificateur d'accord de commandant classique. | 
| **`⎋`** | **Évasion** (`Esc`) | `Esc` | Annule les opérations, efface les filtres ou ferme les boîtes de dialogue. | 
| **`⏎`** | **Retour** (`Enter`) | `Enter` | Exécute des actions, ouvre des éléments ou valide des invites de dialogue. | 
| **`⌫`** | **Supprimer / Retour arrière** | `Backspace` | Suppression de caractères en arrière ou navigation dans le répertoire parent. | 
| **`⌦`** | **Supprimer avant** | `Del` | Transférer le caractère de suppression ou supprimer le fichier sélectionné. | 
| **`⇥`** | **Onglet** | `Tab` | Alterne la mise au point entre les panneaux source et cible. | 
| **`⇞`** | **Page précédente** | `PgUp` | Fait défiler la liste du panneau par une fenêtre d'affichage. | 
| **`⇟`** | **Page suivante** | `PgDn` | Fait défiler la liste des panneaux vers le bas d’une fenêtre d’affichage. | 

---

## 2. Fonction macOS (`Fn`) Guide des touches

> [!IMPORTANT] 
> ### Comment utiliser les touches de fonction sur les claviers Mac 
> 
> Par défaut, les claviers Apple (y compris les claviers MacBook intégrés, les Magic Keyboards et les Mac Touch Bar) attribuent la rangée physique supérieure (`F1` à `F12`) aux commandes matérielles telles que la luminosité de l'écran, Mission Control, Spotlight, Dictée, la lecture multimédia et le volume du haut-parleur. 
> 
> Étant donné que les flux de travail Commander classiques reposent fortement sur `F1`–`F12`, vous disposez de deux options : 
> 
> #### Méthode A : maintenez l'accord clé `Fn` (prêt à l'emploi par défaut) 
> Maintenez la touche physique **`Fn`** (ou la touche Globe 🌐) située dans le coin inférieur gauche du clavier de votre Mac tout en appuyant sur n'importe quelle touche de fonction : 
> 
> * **`Fn + F3`** : Afficher le fichier dans Lister 
> * **`Fn + F4`** : Modifier le fichier 
> * **`Fn + F5`** : Copier les fichiers vers le panneau cible 
> * **`Fn + F6`** : déplacer les fichiers vers le panneau cible 
> * **`Fn + F7`** : Créer un nouveau répertoire 
> * **`Fn + F8`** : Supprimer des fichiers 
> * **`Fn + Shift + F4`** : Créer et modifier un nouveau fichier texte 
> * **`Fn + Alt + F7`** : Ouvrir la recherche de fichiers 
> 
> #### Méthode B : Activer les « Touches de fonction standard » dans les paramètres macOS (recommandé) 
> Si vous utilisez régulièrement ATBCmder, changez de ligne de fonctions pour qu'appuyer sur `F1`–`F12` déclenche directement les commandes de fonction, tandis que maintenir `Fn` déclenche les réglages de luminosité et de volume : 
> 
> 1. **macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia** : 
> - Ouvrir ** Menu Apple ➔ Paramètres système...** 
> - Dans la barre latérale gauche, sélectionnez **Clavier**. 
> - Cliquez sur le bouton **Raccourcis clavier clavier...**. 
> - Dans la barre latérale de la boîte de dialogue, sélectionnez **Touches de fonction**. 
> - Basculez **"Utiliser les touches F1, F2, etc. comme touches de fonction standard"** sur **ON**. 
> - Cliquez sur **Terminé**. 
> 
> 2. **macOS 12 Monterey et macOS 11 Big Sur** : 
> - Ouvrez ** Menu Apple ➔ Préférences Système... ➔ Clavier**. 
> - Dans l'onglet **Clavier**, cochez la case **"Utiliser les touches F1, F2, etc. comme touches de fonction standard"**. 
> 
> #### Modèles de MacBook Pro avec Touch Bar 
> 
> * Maintenez la touche physique **`Fn`** en bas à gauche pour afficher instantanément la ligne virtuelle `F1`–`F12` sur la Touch Bar. 
> * Vous pouvez également configurer **Paramètres système ➔ Clavier ➔ Paramètres de la barre tactile...** et définir **"La barre tactile affiche"** sur **"Touches F1, F2, etc."** lorsque ATBCmder est l'application active au premier plan. 
> 
> #### Claviers compacts sans ligne de fonctions dédiée 
> 
> * Si vous utilisez un clavier 60% ou 65% mécanique sans touches dédiées `F`, vous n'avez pas besoin de vous tordre les doigts. Utilisez les accords de modificateur macOS natifs d'ATBCmder (`⌘C`, `⌥⌘V`, `⇧⌘N`, `⌘⌫`, `⌥⏎`) qui offrent une parité opérationnelle de 100 %.

---

## 3. Architecture de raccourcis contextuels

Pour éviter les collisions de raccourcis clavier entre différents domaines d'application (par exemple, recherche dans la liste de fichiers principale ou recherche dans un visualiseur de fichiers texte), ATBCmder segmente tous les raccourcis dans des contextes hiérarchiques distincts : 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PORTÉE APPLICATION : Main                            │
│  Commandes globales, navigation panneaux, onglets, barre d'outils           │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PORTÉE PANNEAU : FilePanel   │  PORTÉES OUTILS MODAUX                      │
│  Actif dans les listes et     │  • Viewer      (Fenêtre Universal Lister)   │
│  miniatures (sélection,       │  • Editor      (Éditeur de code intégré)    │
│  marquage, renommage direct,  │  • Differ      (Comparateur de fichiers)    │
│  calcul de taille)            │  • FindFiles   (Recherche avancée)          │
│                               │  • MultiRename (Renommage par lot)          │
└───────────────────────────────┴─────────────────────────────────────────────┘
```
 

Lorsque vous appuyez sur un accord clé, le moteur **`HotkeyManager`** : 

1. Évalue le contexte ciblé actif (par exemple, `Viewer` ou `FilePanel`). 
2. Si une liaison exacte correspond, la commande `cm_*` associée s'exécute immédiatement. 
3. Si aucune liaison n'existe dans le contexte local, la frappe revient progressivement au contexte `Main`. 
4. S'il n'est toujours pas lié, l'édition de texte standard ou la gestion des frappes système prend le relais. 

---

## 4. Tableaux maîtres catégorisés à double matrice

Les tableaux de référence suivants documentent toutes les commandes prises en charge par ATBCmder, classées par flux de travail fonctionnel.

### 4.1 Opérations sur les fichiers

Les opérations sur les fichiers constituent l’épine dorsale du travail quotidien. Chaque opération utilise par défaut le paradigme **Source ➔ Cible** : les éléments sélectionnés dans le panneau actif sont traités dans le répertoire ouvert dans le panneau opposé inactif.

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_View` | Afficher le fichier à l'aide de Universal Lister (aperçu en lecture seule) | `⌘3` / `Space` *(Coup d'œil)* | `F3` / `Shift+F3` | Principal | 
| `cm_Edit` | Ouvrir le fichier dans l'éditeur de texte intégré | `⌘4` | `F4` | Principal | 
| `cm_EditNew` | Créez et modifiez immédiatement un nouveau fichier texte | `⇧⌘4` / `⇧F4` | `Shift+F4` | Principal | 
| `cm_Copy` | Copier les fichiers sélectionnés du panneau actif vers le panneau cible | `⌘C` *(dans le presse-papiers)* / `F5` | `F5` | Principal | 
| `cm_CopySamePanel` | Dupliquer/cloner le fichier sélectionné dans le même répertoire | `⇧F5` | `Shift+F5` | Principal | 
| `cm_Move` | Déplacer les fichiers sélectionnés du panneau actif vers le panneau cible | `⌥⌘V` *(coller le déplacement)* / `F6` | `F6` | Principal | 
| `cm_RenameOnly` | Renommage rapide en ligne du fichier sous le curseur | `⏎` *(Retour)* / `F2` | `F2` / `Shift+F6` | Principal | 
| `cm_Rename` | Renommer le fichier sélectionné via la boîte de dialogue | `⇧F6` | `Shift+F6` | Principal | 
| `cm_MkDir` | Créer un nouveau répertoire/dossier | `⇧⌘N` / `F7` | `F7` | Principal | 
| `cm_Delete` | Supprimer les éléments sélectionnés dans la corbeille macOS | `⌘⌫` *(Cmd+Suppr)* / `⌦` | `F8` / `Delete` | Principal | 
| `cm_Wipe` | Supprimez les fichiers en toute sécurité (contournez la corbeille de manière permanente) | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | Panneau de fichiers | 
| `cm_Open` | Ouvrez le fichier avec l'application par défaut ou entrez dans le répertoire | `⌘↓` / `⏎` *(Retour)* | `Enter` | Principal | 
| `cm_SetFileProperties` | Inspecter et modifier les métadonnées des fichiers, les dates et les autorisations UNIX | `⌥⏎` *(Option+Retour)* / `⌘I` | `Alt+Enter` | Principal | 
| `cm_CountDirContent` | Calculer la taille en octets du répertoire sous le curseur | `⌥⇧⏎` *(Option+Maj+Retour)* | `Alt+Shift+Enter` | Panneau de fichiers | 
| `cm_CalculateSpace` | Calculer la taille totale de tous les répertoires sélectionnés | `⌃L` / `⌘L` | `Ctrl+L` | Principal | 
| `cm_SymLink` | Créer un lien symbolique dans le panneau cible | `⌥⌘S` | *(Menu : Fichiers ➔ Lien symbolique)* | Principal | 
| `cm_HardLink` | Créer un lien physique du système de fichiers dans le panneau cible | `⌥⌘H` | *(Menu : Fichiers ➔ Lien physique)* | Principal | 
| `cm_PackFiles` | Regrouper/compresser les fichiers sélectionnés dans une archive (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Principal | 
| `cm_ExtractFiles` | Extraire le contenu de l'archive directement dans le panneau cible | `⌥F9` / `⌥⌘E` | `Alt+F9` | Principal | 
| `cm_ArchiveView` | Entrez l'archive en tant que répertoire de système de fichiers virtuel (`vfs://`) | `⌃⇟` *(Ctrl+PgDn)* / `⌘↓` | `Ctrl+PgDn` | Principal | 
| `cm_CompareContents` | Comparer le contenu de deux fichiers sélectionnés | `⇧F3` | `Shift+F3` | Principal |

---

### 4.2 Sélection et marquage

Les gestionnaires de fichiers orthodoxes excellent dans la sélection rapide de plusieurs fichiers. ATBCmder permet de sélectionner des éléments individuels, des modèles de caractères génériques, des groupes d'extension ou des blocs continus sans utiliser de souris.

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_MarkMarkAll` | Sélectionnez tous les fichiers et dossiers dans le panneau actif | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Principal | 
| `cm_MarkUnmarkAll` | Désélectionnez tous les fichiers et dossiers dans le panneau actif | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Principal | 
| `cm_MarkInvert` | Inverser l'état de sélection actuel dans le panneau actif | `⌘I` / `⌃I` | `Num*` *(Clavier `*`)* | Panneau de fichiers | 
| `cm_MarkPlus` | Sélectionnez le modèle de caractère générique correspondant au groupe (par exemple `*.ts`) | `⌘+` / `⌃+` | `Num+` *(Clavier `+`)* | Panneau de fichiers | 
| `cm_MarkMinus` | Désélectionnez le modèle de caractère générique correspondant au groupe (par exemple `*.log`) | `⌘-` / `⌃-` | `Num-` *(Clavier `-`)* | Panneau de fichiers | 
| `cm_MarkCurrentExtension` | Sélectionnez tous les fichiers partageant l'extension de fichier du curseur | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Principal | 
| `cm_UnmarkCurrentExt` | Désélectionnez tous les fichiers partageant l'extension de fichier du curseur | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Principal | 
| `cm_MarkCurrentName` | Sélectionnez tous les fichiers partageant le nom de fichier de base du curseur | `⌥⌘N` | *(Menu : Marquer ➔ Même nom)* | Principal | 
| `cm_SelectOrDeselectFile` | Basculer la sélection des éléments et faire avancer le curseur vers le bas | `Space` | `Insert` / `Space` | Panneau de fichiers | 
| `Shift+Up / Shift+Down` | Élargir ou réduire la gamme de sélection continue | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | Panneau de fichiers | 
| `Shift+PageUp / Shift+PageDown` | Développer la sélection continue par la page d'affichage complète | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | Panneau de fichiers | 
| `cm_ClearAll` | Effacer toutes les marques de sélection et les surlignages de recherche | `⌃L` | `Ctrl+L` | Principal | 
| `cm_CopyToClipboard` | Copier les fichiers sélectionnés dans le presse-papiers du système macOS | `⌘C` | `Ctrl+C` | Principal | 
| `cm_CutToClipboard` | Couper les fichiers sélectionnés dans le presse-papiers du système macOS | `⌘X` | `Ctrl+X` | Principal | 
| `cm_PasteFromClipboard` | Coller les fichiers du presse-papiers dans Active Directory | `⌘V` | `Ctrl+V` | Principal | 
| `cm_PasteAsMove` | Coller des fichiers du presse-papiers en tant qu'opération de déplacement | `⌥⌘V` | `Ctrl+Alt+V` | Principal | 
| `cm_CopyNamesToClip` | Copier le(s) nom(s) de fichier uniquement dans le presse-papiers | `⇧⌘X` | `Ctrl+Shift+X` | Principal | 
| `cm_CopyFullNamesToClip` | Copier le(s) chemin(s) absolu(s) complet(s) dans le presse-papiers | `⇧⌘C` | `Ctrl+Shift+C` | Principal | 
| `cm_CompareDirectories` | Marquer les fichiers qui existent dans un panneau mais pas dans l'autre | `⌥⇧C` | *(Menu : Marquer ➔ Comparer les répertoires)* | Principal |

---

### 4.3 Navigation dans le panneau et signets

Déplacez-vous sans effort entre les dossiers, les volumes locaux, les montages réseau et l'historique de navigation.

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FocusSwap` / `cm_SwitchPanel` | Alterner la mise au point du clavier entre les panneaux gauche et droit | `⇥` *(Tabulation)* | `Tab` | Principal | 
| `cm_Refresh` | Actualiser / relire le contenu d'Active Directory | `⌘R` / `⌃R` | `Ctrl+R` | Principal | 
| `cm_ChangeDirToParent` | Accédez au répertoire parent (`..`) | `⌘↑` / `⌫` *(Retour arrière)* | `Backspace` / `Ctrl+PgUp` | Principal | 
| `cm_ChangeDirToRoot` | Accédez directement à la racine du système de fichiers (`/`) | `⌘\` | `Ctrl+\` | Principal | 
| `cm_ChangeDirToHome` | Accédez directement au dossier de départ de l'utilisateur (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | Panneau de fichiers | 
| `cm_ViewHistoryPrev` | Revenir dans l'historique de navigation dans le répertoire | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Principal | 
| `cm_ViewHistoryNext` | Naviguer vers l'avant dans l'historique de navigation dans les répertoires | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Principal | 
| `cm_DirHistory` | Ouvrir le menu déroulant de l'historique du répertoire interactif | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Principal | 
| `cm_Drives` | Ouvrir le lecteur et le sélecteur de volume monté | `⌥D` | `Alt+D` | Principal | 
| `cm_LeftOpenDrives` | Ouvrir le menu de sélection du lecteur pour le panneau de gauche | `⌥F1` | `Alt+F1` | Principal | 
| `cm_RightOpenDrives` | Ouvrir le menu de sélection du lecteur pour le panneau de droite | `⌥F2` | `Alt+F2` | Principal | 
| `cm_Exchange` | Échanger les panneaux gauche et droit (répertoires, onglets, états) | `⌘U` | `Ctrl+U` | Principal | 
| `cm_TargetEqualSource` | Définir le répertoire du panneau inactif pour qu'il corresponde au répertoire actif | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Principal | 
| `cm_SyncSlaveDir` | Verrouiller la navigation du panneau cible pour refléter le panneau source | `⌥S` | *(Menu : Commandes ➔ Synchroniser la navigation)* | Principal | 
| `cm_DirHotList` | Menu Liste de favoris / Favoris Open Directory | `⌘D` | `Ctrl+D` | Principal | 
| `cm_ConfigDirHotList` | Boîte de dialogue de configuration de la liste de véhicules recherchés Open Directory | `⇧⌘D` | `Ctrl+Shift+D` | Principal | 
| `cm_GoToFirst` | Passer le curseur au premier élément du panneau actif | `⌘↑` / `Fn+←` *(Accueil)* | `Home` | Principal | 
| `cm_GoToLast` | Passer le curseur au dernier élément du panneau actif | `⌘↓` / `Fn+→` *(Fin)* | `End` | Principal | 
| `PageUp / PageDown` | Faites défiler le panneau actif vers le haut ou vers le bas d'une fenêtre complète | `⇞` *(Fn+↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | Panneau de fichiers |

---

### 4.4 Modes d'affichage et tri

Basculez en toute transparence entre les listes compactes, les colonnes de métadonnées détaillées, les grilles de vignettes visuelles, l'aplatissement récursif des répertoires et les arborescences synchronisées.

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_BriefView` | Passer à la vue brève (noms compacts multicolonnes) | `⌃F1` | `Ctrl+F1` | Principal | 
| `cm_ColumnsView` | Passer à la vue Colonnes/Détails (nom, taille, date, autorisations) | `⌃F2` | `Ctrl+F2` | Principal | 
| `cm_ThumbnailsView` | Passer à l'affichage en grille de vignettes (images, médias, PDF) | `⌃⇧F1` | `Ctrl+Shift+F1` | Principal | 
| `cm_FlatView` | Basculer la vue plate/branche (liste de répertoires récursifs) | `⌘B` | `Ctrl+B` | Principal | 
| `cm_FlatViewSel` | Vue plate/branche des répertoires sélectionnés uniquement | `⇧⌘B` | `Ctrl+Shift+B` | Principal | 
| `cm_TreeView` | Vue arborescente (Remplacer le panneau actif par une arborescence de répertoires) | `⌃⇧F8` | `Ctrl+Shift+F8` | Principal | 
| `cm_TreeViewSplit` | Vue arborescente (panneau divisé : arbre en haut/à gauche, fichiers en bas/à droite) | `cm_TreeViewSplit` | *(Menu : Afficher ➔ Division de l'arborescence)* | Principal | 
| `cm_TreeViewBoth` | Vue arborescente (les deux panneaux affichent des arborescences de répertoires) | `cm_TreeViewBoth` | *(Menu : Afficher ➔ Vue arborescente les deux)* | Principal | 
| `cm_QuickView` | Basculer le panneau Coup d'œil (aperçu en direct dans le panneau opposé) | `⌘Q` / `⌃Q` | `Ctrl+Q` | Principal | 
| `cm_SortByName` | Trier les éléments par nom (basculer par ordre croissant/décroissant) | `⌃F3` | `Ctrl+F3` | Principal | 
| `cm_SortByExt` | Trier les éléments par extension | `⌃F4` | `Ctrl+F4` | Principal | 
| `cm_SortByDate` | Trier les éléments par date/heure de modification | `⌃F5` | `Ctrl+F5` | Principal | 
| `cm_SortBySize` | Trier les éléments par taille de fichier | `⌃F6` | `Ctrl+F6` | Principal | 
| `cm_SortByAttr` | Trier les éléments par attributs UNIX/autorisations | `cm_SortByAttr` | *(Menu : Trier ➔ Attributs)* | Principal | 
| `cm_ShowHiddenFiles` | Basculer la visibilité des fichiers cachés (`.` dotfiles) | `⌘H` / `⇧⌘.` | `Ctrl+H` | Principal | 
| `cm_ShowSysFiles` | Basculer la visibilité du système macOS et des fichiers protégés | `⇧⌘.` | `Ctrl+.` | Principal | 
| `cm_QuickSearch` | Ouvrir la barre de recherche rapide dans le panneau (saisissez des lettres pour filtrer) | `⌥S` / `⌃S` *(ou en tapant)* | `Ctrl+S` / *(Saisie de lettres)* | Principal | 
| `cm_SemanticFilter` | Barre de filtre intelligent sémantique ouvert en langage naturel | `⌘F` | `Ctrl+F` | Principal | 
| `cm_HorizontalFilePanels` | Basculer la disposition horizontale à deux panneaux (empilés verticalement) | `⇧⌘H` | `Ctrl+Shift+H` | Principal |

---

### 4.5 Gestion des onglets et des fenêtres

ATBCmder permet d'ouvrir un nombre illimité d'onglets dans l'un ou l'autre panneau, de verrouiller les emplacements de travail favoris et de gérer des sessions multi-onglets sur deux panneaux.

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_NewTab` | Ouvrir un nouvel onglet de dossier dans le panneau actif | `⌘T` | `Ctrl+T` | Principal | 
| `cm_CloseTab` | Fermer l'onglet du dossier actuellement actif | `⌘W` | `Ctrl+W` | Principal | 
| `cm_NextTab` / `cm_NextTabCtrl` | Passer à l'onglet suivant à droite | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Principal | 
| `cm_PrevTab` / `cm_PrevTabCtrl` | Passer à l'onglet précédent à gauche | `⌃⇧⇥` *(Ctrl+Maj+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Principal | 
| `cm_ShowTabsList` | Afficher le menu contextuel de tous les onglets ouverts dans le panneau actif | `⇧⌘L` | `Ctrl+Shift+L` | Principal | 
| `cm_CloseAllTabs` | Fermez tous les onglets du panneau actif sauf le dernier | `⌥⌘W` | *(Menu contextuel de l'onglet : Fermer tout)* | Principal | 
| `cm_CloseOtherTabs` | Fermez tous les onglets autres que l'onglet actuellement actif | `⇧⌘W` | *(Menu contextuel de l'onglet : Fermer les autres)* | Principal | 
| `cm_Duplicatetab` | Onglet du dossier actif en double | `⌘D` / `cm_Duplicatetab` | *(Menu contextuel de l'onglet : Dupliquer)* | Principal | 
| `cm_MoveTabLeft` | Déplacer l'onglet actif d'une position vers la gauche | `⌃⇧←` | *(Menu contextuel de l'onglet : Déplacer vers la gauche)* | Principal | 
| `cm_MoveTabRight` | Déplacer l'onglet actif d'une position vers la droite | `⌃⇧→` | *(Menu contextuel de l'onglet : Déplacer vers la droite)* | Principal | 
| `cm_CopyTabToOtherPanel` | Cloner l'onglet actif directement dans le panneau opposé | `⌥⌘T` | *(Menu contextuel de l'onglet : Copier vers un autre)* | Principal | 
| `cm_SaveTab` / `cm_SaveTabs` | Enregistrer la disposition actuelle des onglets dans la configuration | `cm_SaveTab` | *(Menu : Onglets ➔ Enregistrer les onglets)* | Principal | 
| `cm_LoadTab` / `cm_LoadTabs` | Restaurer la disposition des onglets enregistrée à partir de la configuration | `cm_LoadTab` | *(Menu : Onglets ➔ Charger les onglets)* | Principal | 
| `cm_OptionsFavorites` | Configurer les ensembles d'onglets favoris et les espaces de travail persistants | `cm_OptionsFavorites` | *(Menu : Onglets ➔ Onglets Favoris)* | Principal | 
| `cm_FullScreen` | Basculer la fenêtre de l'application en plein écran | `⌃⌘F` / `F11` | `F11` | Principal |

---

### 4.6 Outils électriques et utilitaires

Lancez des outils d'automatisation avancés, des utilitaires par lots et des outils système intégrés directement à partir des accords du clavier.

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FileSearch` / `cm_Search` | Ouvrir la boîte de dialogue de recherche avancée multi-filtres | `⌥F7` / `⌥⌘F` | `Alt+F7` | Principal | 
| `cm_FileDiff` / `cm_CompareFiles` | Ouvrir la visionneuse de différences de fichiers visuels côte à côte | `⌘⇧F12` | `Meta+Shift+F12` | Principal | 
| `cm_SyncDirs` | Outil de synchronisation d'annuaire bidirectionnel ouvert | `⇧F12` | `Shift+F12` | Principal | 
| `cm_MultiRename` | Outil de renommage multiple par lots ouverts (RegEx et jetons) | `⌘M` | `Ctrl+M` | Principal | 
| `cm_Split` | Diviser un gros fichier en segments uniformes | `⌥F6` | `Alt+F6` | Principal | 
| `cm_Combine` | Combinez les segments numérotés divisés dans le fichier d'origine | `⌥F7` | `Alt+F7` | Principal | 
| `cm_CalculateChecksum` | Calculer le hachage cryptographique (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Principal | 
| `cm_VerifyChecksum` | Vérifier les fichiers par rapport au fichier de somme de contrôle (`.md5`, `.sha256`) | `cm_VerifyChecksum` | *(Menu : Fichiers ➔ Vérifier la somme de contrôle)* | Principal | 
| `cm_RunTerm` | Lancer le terminal du système dans le répertoire du panneau actif | `⌃J` / `F9` | `Ctrl+J` / `F9` | Principal | 
| `cm_FocusCmdLine` | Déplacer le focus du clavier directement vers la ligne de commande inférieure | `⇧F2` | `Shift+F2` | Principal | 
| `cm_ShowCmdLineHistory` | Ouvrir la liste déroulante de l'historique des commandes shell passées | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Principal | 
| `cm_AddPathToCmdLine` | Ajouter le chemin du répertoire actif à la ligne de commande | `⌘P` | `Ctrl+P` | Principal | 
| `cm_ShowCommandLine` | Basculer la ligne de commande inférieure/la barre de saisie de la console | `⌘O` | `Ctrl+O` | Principal | 
| `cm_DiskBenchmark` | Exécuter un test de performances en lecture/écriture du lecteur de stockage | `cm_DiskBenchmark` | *(Menu : Commandes ➔ Benchmark)* | Principal | 
| `cm_VisSemanticCommand` | Ouvrir la recherche sémantique et la barre de commande en langage naturel | `/` / `⇧⌘P` | `/` | Principal |

---

### 4.7 Système, configuration et aide

Accédez aux préférences des applications, à la gestion de la configuration, aux mises à jour logicielles et à la documentation utilisateur. 

| ID de commande | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_Options` | Ouvrir la boîte de dialogue Préférences/Paramètres de l'application | `⌘,` | `Ctrl+,` | Principal | 
| `cm_HelpContents` / `cm_HelpIndex` | Documentation et guide utilisateur interactifs ouverts | `⌘?` / `F1` | `F1` | Principal | 
| `cm_HelpKeyboard` | Ouvrir la carte de référence des raccourcis clavier rapides | `cm_HelpKeyboard` | *(Menu : Aide ➔ Clavier)* | Principal | 
| `cm_Exit` | Quitter / Quitter ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Principal | 
| `cm_About` | Afficher la version, la licence et les crédits d'ATBCmder | `cm_About` | *(Menu : ATBCmder ➔ À propos)* | Principal | 
| `cm_OpenConfigDirectory` | Révéler le dossier de configuration (`atbcmder.xml`) dans le panneau | `cm_OpenConfigDirectory` | *(Menu : Configuration ➔ Ouvrir la configuration)* | Principal | 
| `cm_ExportConfiguration` | Exporter toutes les préférences vers un bundle ZIP portable | `cm_ExportConfiguration` | *(Menu : Configuration ➔ Exporter)* | Principal | 
| `cm_ImportConfiguration` | Importer les préférences à partir du bundle ZIP portable | `cm_ImportConfiguration` | *(Menu : Configuration ➔ Importer)* | Principal | 
| `cm_CheckForUpdate` | Rechercher les mises à jour du logiciel d'application | `cm_CheckForUpdate` | *(Menu : Aide ➔ Rechercher les mises à jour)* | Principal | 

---

## 5. Raccourcis clavier contextuels de l'outil modal

Lors de l'ouverture d'outils spécialisés tels que Universal Lister, l'éditeur de texte intégré, les boîtes de dialogue côte à côte ou par lots, ATBCmder active des mappages de touches spécifiques au contexte. Ces raccourcis fonctionnent directement dans chaque fenêtre d'outil plutôt que via les commandes de registre `cm_*` globales de l'application.

### 5.1 Lister universel (Contexte `Viewer`)

Actif lors de la prévisualisation de documents, de texte, de code, d'images, d'audio, de vidéo ou d'octets hexadécimaux bruts.

| Actions/Fonctionnalité | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| Sélectionner tout | Sélectionnez tout le texte/contenu dans la visionneuse | `⌘A` | `Ctrl+A` | Visionneuse | 
| Mode texte brut | Passer en mode texte brut | `1` | `1` | Visionneuse | 
| Mode binaire | Passer en mode binaire | `2` | `2` | Visionneuse | 
| Mode hexadécimal brut | Passer en mode d'inspection des octets Raw Hex | `3` | `3` | Visionneuse | 
| Mode décimal | Passer en mode décimal | `4` | `4` | Visionneuse | 
| Voir le livre | Passer en mode Livre paginé | `5` | `5` | Visionneuse | 
| Affichage des images | Passer en mode visionneuse d'images | `6` | `6` | Visionneuse | 
| Plugins personnalisés | Passer à la visionneuse de plugins personnalisée | `7` | `7` | Visionneuse | 
| PDF / Vue Bureau | Passer en mode lecteur de documents PDF/Office | `8` | `8` | Visionneuse | 
| Mode Code | Passer en mode code avec mise en évidence de la syntaxe | `9` | `9` | Visionneuse | 
| Image centrale | Centrer l'image dans la fenêtre du visualiseur | `C` | `C` | Visionneuse | 
| Ajuster à la fenêtre | Ajuster l'image aux dimensions de la fenêtre | `F` | `F` | Visionneuse | 
| Convient uniquement aux tailles grandes | Réduire l'échelle uniquement si l'image dépasse les dimensions de la fenêtre | `L` | `L` | Visionneuse | 
| Basculer l'enveloppement | Activer/désactiver le retour à la ligne | `W` | `W` | Visionneuse | 
| Basculer le curseur | Basculer le curseur de texte visible | `F6` | `F6` | Visionneuse | 
| Rechercher du texte | Rechercher du texte dans le document | `⌘F` / `F7` | `F7` | Visionneuse | 
| Rechercher suivant | Passer à la recherche suivante | `⌘G` / `F3` | `F3` | Visionneuse | 
| Rechercher le précédent | Aller à la recherche précédente | `⇧⌘G` / `⇧F3` | `Shift+F3` | Visionneuse | 
| Zoom avant | Zoomer sur l'image ou PDF | `⌘+` / `Num+` | `Num+` | Visionneuse | 
| Zoom arrière | Zoom arrière sur l'image ou PDF | `⌘-` / `Num-` | `Num-` | Visionneuse | 
| Plein écran | Basculer le mode d'affichage plein écran | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Visionneuse | 
| Fermer la visionneuse | Fermer la fenêtre du visualiseur Lister | `⎋` *(Échap)* / `Q` | `Escape` / `Q` | Visionneuse |

---

### 5.2 Éditeur de texte intégré (contexte `Editor`)

Actif lors de la création ou de la modification de fichiers texte et de code source. 

| Actions/Fonctionnalité | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| Enregistrer le fichier | Enregistrer le fichier modifié sur le disque | `⌘S` / `F2` | `F2` | Editeur | 
| Rechercher du texte | Rechercher du texte dans le document de l'éditeur | `⌘F` / `F7` | `F7` | Editeur | 
| Rechercher suivant | Passer à la recherche suivante | `⌘G` / `F3` | `F3` | Editeur | 
| Rechercher le précédent | Aller à la recherche précédente | `⇧⌘G` / `⇧F3` | `Shift+F3` | Editeur | 
| Couper | Couper le texte sélectionné dans le presse-papiers | `⌘X` | `Ctrl+X` | Editeur | 
| Copier | Copier le texte sélectionné dans le presse-papiers | `⌘C` | `Ctrl+C` | Editeur | 
| Coller | Coller le texte du presse-papiers | `⌘V` | `Ctrl+V` | Editeur | 
| Annuler | Annuler la dernière action de saisie | `⌘Z` | `Ctrl+Z` | Editeur | 
| Refaire | Rétablir la dernière action annulée | `⇧⌘Z` | `Ctrl+Shift+Z` | Editeur | 
| Sélectionner tout | Sélectionner le texte entier du document | `⌘A` | `Ctrl+A` | Editeur | 
| Fermer l'éditeur | Fermer la fenêtre de l'éditeur de texte | `⎋` *(Échap)* / `⌘W` | `Esc` / `Alt+X` | Editeur | 

---

### 5.3 Différence visuelle côte à côte (contexte `Differ`)

Actif dans l'outil de comparaison des différences visuelles. 

| Actions/Fonctionnalité | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| Rechercher du texte | Rechercher du texte dans les volets de différence | `⌘F` / `F7` | `F7` | Différent | 
| Rechercher suivant | Passer à l'occurrence de recherche suivante | `⌘G` / `F3` | `F3` | Différent | 
| Rechercher le précédent | Aller à l'occurrence de recherche précédente | `⇧⌘G` / `⇧F3` | `Shift+F3` | Différent | 
| Différence suivante | Passer le curseur au bloc de différence suivant | `⌥↓` *(Option+Bas)* | `Alt+Down` | Différent | 
| Différence précédente | Passer le curseur au bloc de différence précédent | `⌥↑` *(Option+Haut)* | `Alt+Up` | Différent | 
| Première différence | Aller directement à la première différence dans les fichiers | `⌥Fn+←` *(Opt+Accueil)* | `Alt+Home` | Différent | 
| Dernière différence | Aller directement à la dernière différence dans les fichiers | `⌥Fn+→` *(Opt+Fin)* | `Alt+End` | Différent | 
| Copier de droite à gauche | Copier le bloc de différence du volet droit vers le volet gauche | `⌥←` *(Option+Gauche)* | `Alt+Left` | Différent | 
| Copier de gauche à droite | Copier le bloc de différence du volet gauche vers le volet droit | `⌥→` *(Option+Droite)* | `Alt+Right` | Différent | 
| Actualiser / Nouvelle analyse | Relisez les fichiers du disque et relancez la comparaison des différences | `⌘R` | `Ctrl+R` | Différent | 
| Fermer Différent | Fermer la fenêtre de comparaison des différences | `⎋` *(Échap)* / `⌘W` | `Alt+X` / `Esc` | Différent | 

---

### 5.4 Boîte de dialogue de recherche avancée de fichiers (contexte `FindFiles`)

Actif dans la boîte de dialogue de recherche multithread en arrière-plan. 

| Actions/Fonctionnalité | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| Lancer la recherche | Démarrer l'exécution de la recherche | `⏎` *(Retour)* / `F9` | `F9` | Rechercher des fichiers | 
| Annuler / Fermer | Annuler la recherche en cours ou fermer la boîte de dialogue | `⎋` *(Échap)* | `Esc` | Rechercher des fichiers | 
| Afficher la sélection | Afficher les résultats de recherche sélectionnés dans Lister | `⌘3` / `F3` | `F3` | Rechercher des fichiers | 
| Modifier la sélection | Ouvrir le résultat de recherche sélectionné dans l'Éditeur | `⌘4` / `F4` | `F4` | Rechercher des fichiers | 
| Nouvelle recherche | Réinitialiser la requête de recherche et préparer une nouvelle recherche | `⌘N` | `Ctrl+N` | Rechercher des fichiers | 
| Effacer les filtres | Nouvelle recherche avec tous les filtres de date/taille/attribut effacés | `⇧⌘N` | `Ctrl+Shift+N` | Rechercher des fichiers | 
| Rappel précédent | Rappeler les paramètres de la recherche précédente | `⌘L` | `Ctrl+L` | Rechercher des fichiers | 

---

### 5.5 Outil de renommage multiple par lots (contexte `MultiRename`)

Actif dans l’espace de travail de renommage par lots. 

| Actions/Fonctionnalité | Descriptif | Raccourci macOS principal (avec glyphes ⌘/⌥/⇧/⌃) | Raccourci Commander classique (avec touches Fn) | Contexte | 
| :--- | :--- | :---: | :---: | :---: | 
| Réinitialiser les règles | Réinitialiser les règles de renommage du masque et du motif par défaut | `⌘R` | `Ctrl+R` | MultiRenommer | 
| Modifier les noms dans l'éditeur | Ouvrir la liste des noms de fichiers cibles dans un éditeur externe pour une édition manuelle | `⌘I` | `Ctrl+I` | MultiRenommer | 
| Charger le fichier de noms | Charger les noms de remplacement à partir d'un fichier texte externe | `F3` | `F3` | MultiRenommer | 

---

## 6. Conseils de pro et optimisation des raccourcis clavier du système

### 6.1 Résolution des collisions de raccourcis globaux macOS

Certains raccourcis clavier par défaut du système macOS interceptent les pressions sur les touches avant qu'elles n'atteignent les applications de bureau. Pour débloquer toute l’agilité de Commander, vous pouvez personnaliser ou désactiver les raccourcis macOS en conflit : 

1. **Recherche Spotlight (`⌘Space` vs recherche rapide)** : 
- Par défaut, `⌘Space` active Spotlight. Si vous préférez utiliser `⌘Space` pour le marquage de fichiers ou la recherche dans le panneau, remapper Spotlight sur `⌥Space` dans **Paramètres système ➔ Clavier ➔ Raccourcis clavier clavier... ➔ Spotlight**. 
2. **Contrôle de mission (`⌃↑`) et App Exposé (`⌃↓`)** : 
- macOS utilise `⌃↑` et `⌃↓` pour Mission Control. Dans ATBCmder, `⌃↓` ouvre la liste déroulante Historique du répertoire. Vous pouvez réaffecter Mission Control dans **Paramètres système ➔ Clavier ➔ Raccourcis clavier clavier... ➔ Mission Control**. 
3. **Masquage d'application (`⌘H`)** : 
- Sous macOS, `⌘H` masque l'application au premier plan. ATBCmder utilise `⌘H` ou `⇧⌘.` pour basculer les fichiers de points cachés. Si vous souhaitez que `⌘H` bascule strictement les fichiers cachés, désactivez « Masquer l'application » dans macOS ou utilisez la norme du Finder `⇧⌘.` (`Cmd+Shift+Period`). 
4. **Réduction de la fenêtre (`⌘M`)** : 
- macOS attribue `⌘M` pour minimiser la fenêtre du Dock. ATBCmder attribue `⌘M` à l'outil de renommage multiple par lots (`cm_MultiRename`). ATBCmder capture `⌘M` dans sa fenêtre principale, mais vous pouvez également déclencher Multi-Rename via `Ctrl+M` ou la barre d'outils. 

---

### 6.2 Ergonomie du trackpad et de la souris

Pour les utilisateurs d'ordinateurs portables sans clavier externe, ATBCmder associe des raccourcis clavier à des gestes intuitifs du trackpad : 

* **Pincer pour zoomer sur les miniatures** : dans la vue Miniatures (`cm_ThumbnailsView`), pincez vers l'intérieur ou vers l'extérieur sur le trackpad de votre MacBook (ou maintenez `⌃` et faites défiler) pour redimensionner les aperçus miniatures en continu de `48 px` jusqu'à `512 px`. 
* **Balayage arrière/avant à deux doigts** : balayez vers la gauche ou la droite avec deux doigts sur la table des fichiers pour naviguer en arrière (`cm_ViewHistoryPrev`) et en avant (`cm_ViewHistoryNext`) dans l'historique des dossiers. 
* **Répartiteur double-clic** : double-cliquez n'importe où sur la barre de séparation centrale verticale pour réinitialiser les panneaux à une division horizontale exacte de 50/50. 
* **Clic du milieu sur les onglets** : cliquez avec le bouton du milieu (ou appuyez avec trois doigts) sur n'importe quel onglet de dossier pour le fermer immédiatement sans appuyer sur `⌘W`. 

---

### 6.3 Personnalisation des raccourcis clavier dans les préférences

Chaque raccourci documenté ci-dessus peut être personnalisé ou rebondi : 

1. Appuyez sur **`⌘,`** (ou sélectionnez **Configuration ➔ Options...**) pour ouvrir la boîte de dialogue Préférences. 
2. Sélectionnez **Raccourcis clavier clavier** dans la barre latérale. 
3. Utilisez la liste déroulante **Contexte** pour choisir la zone que vous souhaitez configurer (`Main`, `FilePanel`, `Viewer`, etc.). 
4. Utilisez la zone de filtre de recherche pour localiser n'importe quelle commande par son nom ou son ID `cm_*`. 
5. Cliquez sur la zone de raccourci et appuyez sur la combinaison de touches souhaitée. Le détecteur de collision intégré vous avertira immédiatement si cet accord est déjà attribué ailleurs. 
6. Cliquez sur **Appliquer** pour activer les modifications instantanément sans redémarrer l'application. 

Les raccourcis clavier utilisateur sont enregistrés dans `~/.config/atbcmder/atbcmder_hotkeys.xml` (ou `~/Library/Préférences/atbcmder/` sur macOS). Vous pouvez exporter et transférer ce fichier entre machines en utilisant **`cm_ExportConfiguration`**. 

--- 

<div align="center"> 
<p>Vous recherchez des recettes pratiques au quotidien, des flux de travail de montage de NAS ou des conseils de dépannage ?</p> 
<p><strong><a href="faq_howtos.md">Passez au chapitre 9 : Recettes réelles et dépannage &rarr;</a></strong></p> 
</div>