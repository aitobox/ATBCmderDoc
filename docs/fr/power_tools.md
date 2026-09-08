# Chapitre 5: Outils avancés et automatisation

Dans la gestion de fichiers volumineux, la manipulation de base des fichiers (copie, déplacement et suppression d'éléments individuels) n'est que le début. Les ingénieurs professionnels, les administrateurs système, les créateurs de contenu et les analystes de données sont fréquemment confrontés à des défis opérationnels complexes : restructuration de milliers d'actifs numériques aux noms incohérents, isolement des régressions de code subtiles entre les branches de versions parallèles, maintien de miroirs synchronisés sur les baies de stockage réseau, localisation de fichiers de configuration profondément enfouis et vérification cryptographique de l'intégrité des fichiers. 

ATBCmder transforme ces tâches à forte intensité de main d'œuvre en opérations rapides et déterministes. Au lieu de nécessiter des scripts de ligne de commande externes, des utilitaires de traitement par lots tiers ou des applications de comparaison autonomes encombrantes, ATBCmder intègre une suite d'automatisation complète directement dans son noyau orthodoxe à double panneau. Que vous ayez besoin d'exécuter des substitutions d'expressions régulières sur l'intégralité d'une archive de photos, d'effectuer une synchronisation d'annuaire bidirectionnelle avec hachage au niveau du contenu ou d'introduire des résultats de recherche multi-filtres dans un espace de travail virtuel, ATBCmder fournit les outils dont vous avez besoin avec une efficacité totale du clavier. 

---

## 1. Démarrage rapide visuel : le moteur d'automatisation et la matrice de commandes

ATBCmder divise les outils électriques et l'automatisation en six domaines fonctionnels spécialisés qui interagissent de manière transparente avec l'interface à double panneau : 

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

### Aide-mémoire pour l'automatisation à double matrice

| Actions | Raccourci macOS | Clé de commandant classique | ID de commande | Descriptif | 
| :--- | :--- | :--- | :--- | :--- | 
| **Renommage multiple par lots** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Ouvre la boîte de dialogue de l'outil Batch Multi-Rename. | 
| **Différence de fichiers côte à côte** | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | Compare deux fichiers sélectionnés côte à côte (`Shift+F3` pour `cm_CompareContents`). | 
| **Synchronisation du répertoire** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Compare et synchronise les répertoires à double panneau. | 
| **Recherche avancée de fichiers** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | Ouvre la boîte de dialogue de recherche multi-filtres. | 
| **Recherche rapide Spotlight** | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menu Commandes)* | Lance une recherche instantanée de métadonnées Spotlight. | 
| **Entrée de commande sémantique**| `/` | `/` | `cm_VisSemanticCommand` | Active la barre de commandes en langage naturel intégrée. | 
| ** Diviser un gros fichier ** | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | Divise les gros fichiers en morceaux numérotés. | 
| **Combiner des fichiers fractionnés** | Menu : Fichiers ➔ Combiner des fichiers | — | `cm_FileLinker` / `cm_Combine` | Réassemble les morceaux `.001`, `.002` en un seul fichier. | 
| **Calculer la somme de contrôle** | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | Calcule les hachages MD5, SHA-1, SHA-256 ou SHA-512. | 
| **Vérifier le fichier de somme de contrôle** | Menu Outils | — | `cm_CheckSumVerify` / `cm_VerifyChecksum` | Vérifie les fichiers par rapport à `.md5`, `.sha256` ou `.sfv`. | 
| **Essuyage sécurisé (déchiquetage)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Écrase et supprime les fichiers en toute sécurité. | 
| **Exécuter le terminal système** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Génère le terminal macOS au chemin actuel du panneau. | 

---

## 2. Outil de renommage multiple par lots (`Ctrl+M` / `⌃M` / `cm_MultiRename`)

Renommer manuellement des dizaines ou des centaines de fichiers est fastidieux et sujet aux erreurs. L'**Outil de renommage multiple par lots** (`cm_MultiRename`, mappé à `fmultirename.pas` dans l'architecture classique) vous permet de définir des modèles de dénomination flexibles, d'appliquer des compteurs de séquence dynamiques, d'effectuer des conversions de casse et d'exécuter de puissantes règles de recherche et de remplacement d'expressions régulières (RegEx) avec des garanties de sécurité visuelle en temps réel. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figure 5.1 : L'outil de renommage multiple par lots comprenant des lignes d'aperçu en direct, des masques de jetons, des paramètres de compteur numérique et une détection des doublons.*

### 2.1 Le workflow de renommage multiple

1. **Sélectionner des fichiers** : dans le panneau de fichiers actif, sélectionnez les fichiers ou répertoires que vous souhaitez renommer à l'aide de `Space`, `Insert` ou d'une sélection générique (`+`). Si rien n'est sélectionné, l'élément sous le curseur est utilisé. 
2. **Lancer l'outil** : appuyez sur **`Ctrl+M`** (`⌃M`) ou choisissez **Fichiers ➔ Outil de renommage multiple...** dans la barre de menu. 
3. **Configurer les modèles et les règles** : saisissez les masques de nom de fichier/d'extension, définissez les options du compteur ou définissez les chaînes de recherche et de remplacement. 
4. **Inspecter l'aperçu en direct** : le tableau à 3 colonnes (`Old Name`, `New Name`, `Directory`) se met à jour instantanément à chaque frappe. 
5. **Exécuter** : cliquez sur **Démarrer Renommer** (ou appuyez sur `Enter`). ATBCmder effectue les changements de nom de manière atomique et actualise les panneaux de fichiers. 

---

### 2.2 Jetons de modèle et découpage de plage

ATBCmder utilise des jetons entre crochets intuitifs pour référencer des parties des métadonnées du fichier d'origine : 

| Jeton | Descriptif | Exemple d'entrée | Valeur résultante | 
| :--- | :--- | :--- | :--- | 
| **`[N]`** | Nom de fichier original sans extension | `report_2026.pdf` | `report_2026` | 
| **`[E]`** | Extension de fichier d'origine (sans point) | `archive.tar.gz` | `gz` | 
| **`[C]`** | Compteur numérique séquentiel | *(Fichier 3 dans la liste)* | `003` (dépend du réglage des chiffres) | 
| **`[Y]`** | Année à 4 chiffres de la modification du fichier | `2026-09-06` | `2026` | 
| **`[M]`** | Mois de modification du fichier à 2 chiffres | `September` | `09` | 
| **`[D]`** | Jour de modification du fichier à 2 chiffres | `6th` | `06` | 
| **`[h]`** | Heure à 2 chiffres (horloge de 24 heures) | `14:30:15` | `14` | 
| **`[m]`** | Minutes à 2 chiffres | `14:30:15` | `30` | 
| **`[s]`** | Seconde à 2 chiffres | `14:30:15` | `15` |

#### Découpage de la plage de caractères (`[Na-b]` / `[Ea-b]`)

Vous pouvez extraire des plages de caractères spécifiques du nom ou de l'extension d'origine à l'aide d'un découpage d'index basé sur 1 : 

- **`[N1-4]`** : Extrait les 4 premiers caractères du nom. Pour `Document_Final.txt`, cela donne `Docu`. 
- **`[N5-]`** : Extraits du 5ème caractère jusqu'à la fin du nom. Pour `DSC_0982.jpg`, cela donne `0982`. 
- **`[N-5]`** : Extrait jusqu'au 5ème caractère. 
- **`[E1-2]`** : Extrait les 2 premiers caractères de l'extension. Pour `archive.html`, cela donne `ht`. 

---

### 2.3 Commandes de compteur et séquences numériques

Le groupe **Paramètres du compteur** permet un contrôle granulaire sur l'indexation numérique : 

- **Start At** : L'entier de départ de la séquence de compteurs (par défaut : `1`). 
- **Étape** : La valeur d'incrément ajoutée pour chaque fichier suivant (par défaut : `1`). La définition de l'étape sur `2` génère `1, 3, 5, 7...`. 
- **Chiffres** : la largeur de remplissage de zéros (plage : `1` à `10`). La définition des chiffres sur `3` formate les nombres comme `001`, `002`, `003`. La définition des chiffres sur `1` désactive les zéros non significatifs (`1`, `2`, `3`). 

---

### 2.4 Rechercher et remplacer et expressions régulières

Le groupe **Rechercher et remplacer** permet de remplacer le texte de tous les éléments sélectionnés : 

- **Rechercher** : sous-chaîne cible ou modèle d'expression régulière. 
- **Remplacer par** : Chaîne de remplacement. Lorsque RegEx est activé, les références arrière (`$1`, `$2` ou `\1`, `\2`) font référence aux groupes de capture. 
- **Utiliser des expressions régulières (Regex)** : active l'analyse des expressions régulières de la bibliothèque standard Python. 
- **Case Sensitive** : lorsque cette case n'est pas cochée, la correspondance ignore la casse des caractères (par exemple, la correspondance à la fois `.JPG` et `.jpg`).

#### Exemples de substitution RegEx puissants

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

### 2.5 Modes de conversion de cas

ATBCmder fournit une normalisation instantanée du boîtier sans nécessiter de modèles complexes : 

- **Aucun changement** : préserve la majuscule d'origine. 
- **minuscule** : convertit l'intégralité du nom de fichier et de l'extension en minuscules (`PHOTO_001.JPG` ➔ `photo_001.jpg`). 
- **UPPERCASE** : Convertit tous les caractères en majuscules (`readme.txt` ➔ `README.TXT`). 
- **Première lettre majuscule** : Met en majuscule le caractère initial de chaque mot (`war and peace.epub` ➔ `War And Peace.epub`). 

---

### 2.6 Grille de prévisualisation en direct et protection contre les collisions

Renommer des centaines de fichiers sans prévisualisation peut entraîner des écrasements de données désastreux. ATBCmder met en œuvre une **Architecture de sécurité zéro accident** : 

1. **Aperçu instantané anti-rebond** : lorsque vous tapez dans les entrées du modèle ou ajustez les zones de sélection numérique, le tableau calcule immédiatement les noms de fichiers résultants. 
2. **Détection de cible en double** : ATBCmder analyse tous les noms de fichiers de sortie calculés dans le dossier de destination. Si deux fichiers ou plus aboutissent exactement au même nom, ou si un nom de fichier se résout en une chaîne vide : 
- Les lignes en collision sont immédiatement mises en évidence en rouge proéminent (`#FFEBEB` / `#D70000` en mode clair, `#4A1515` / `#FF8080` en mode sombre). 
- Le bouton **Démarrer Renommer** est automatiquement **désactivé**. 
- Une info-bulle avertit : *"Collision de noms détectée. Veuillez résoudre les doublons avant de renommer."* 
3. **Collision Clearance** : Une fois que vous avez ajusté votre compteur, votre modèle ou votre expression régulière pour rendre tous les noms de fichiers cibles uniques, l'avertissement disparaît et le bouton **Démarrer le renommage** est réactivé. 

---

### 2.7 Recettes pratiques étape par étape

#### Recette A : Renommer les photos d'un appareil photo numérique avec des horodatages

Transformez les noms de caméras énigmatiques (`IMG_4092.JPG`, `IMG_4093.JPG`) en actifs organisés chronologiquement : 

1. Sélectionnez les fichiers photo et appuyez sur **`Ctrl+M`**. 
2. Définissez **Modèle de nom de fichier** sur : `Photo_[Y][M][D]_[C]`. 
3. Définissez **Modèle d'extension** sur : `[E]`. 
4. Définissez **Chiffres** sur `3`, **Début à** sur `1`. 
5. Définissez **Conversion de cas** sur `lowercase`. 
6. Prévisualisez le résultat : `photo_20260906_001.jpg`, `photo_20260906_002.jpg`. 
7. Appuyez sur `Enter` pour postuler.

#### Recette B : ajouter un préfixe tout en préservant le nom et l'extension

Préfixez un lot de documents avec un code projet : 

1. Sélectionnez les documents et appuyez sur **`Ctrl+M`**. 
2. Dans **Modèle de nom de fichier**, saisissez : `PRJ-ALPHA_[N]`. 
3. Laissez **Modèle d'extension** sous la forme `[E]`. 
4. Cliquez sur **Démarrer Renommer**. 

---

## 3. Différence de fichiers visuels côte à côte (`Meta+Shift+F12` / `⌘⇧F12` / `cm_FileDiff`)

Détecter les différences entre les révisions de configuration, les fichiers de code source ou les vidages de données est une tâche quotidienne pour les utilisateurs expérimentés. ATBCmder comprend un **Visual File Diff Viewer** intégré côte à côte (`DiffViewerDialog`) qui élimine le besoin de lancer des outils externes lourds. 

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

### 3.1 Lancement du fichier Diff

- **Comparez deux fichiers sélectionnés** : dans un seul panneau, sélectionnez exactement deux fichiers et appuyez sur **`Meta+Shift+F12`** (`⌘⇧F12`) ou choisissez **Commandes ➔ Comparer par contenu...**. 
- **Comparer les fichiers opposés** : mettez en surbrillance un fichier dans le panneau de gauche, mettez en surbrillance le fichier correspondant dans le panneau de droite et déclenchez `cm_CompareContents`. 
- **Commandes prises en charge** : `cm_CompareContents`, `cm_FileDiff` et `cm_CompareByContent` sont toutes acheminées vers le moteur de comparaison côte à côte. 

---

### 3.2 Mise en évidence des différences visuelles et codes de couleur

Le moteur de comparaison analyse le texte ligne par ligne à l'aide d'un algorithme Hunt-Szymanski LCS optimisé (`TextDiffer`), divisant les différences en morceaux codés par couleur : 

| Type de différence | Thème clair | Thème sombre | Descriptif | 
| :--- | :--- | :--- | :--- | 
| **Lignes ajoutées** | Émeraude douce (`#e6ffed`) | Vert forêt foncé (`#234b2d`) | Lignes présentes uniquement dans le fichier Droit. | 
| **Lignes supprimées** | Pourpre doux (`#ffeef0`) | Rouge cramoisi foncé (`#552328`) | Lignes présentes dans le fichier Gauche mais manquantes dans le fichier Droite. | 
| **Lignes modifiées** | Ambre doux (`#fff5b1`) | Or ambre foncé (`#50461e`) | Lignes modifiées entre les versions Gauche et Droite. | 
| **Beau morceau actif** | Nuance contrastée vive | Nuance contrastée vive | Le bloc de différence actuellement focalisé par le curseur. | 

Chaque volet comporte une gouttière gauche dédiée (`LineNumberArea`) affichant les numéros de ligne de base 1 synchronisés avec les positions des différences. 

---

### 3.3 Défilement synchronisé et sécurité de réentrée

Lorsque l'on compare de longs fichiers source contenant des milliers de lignes, la navigation dans le code nécessite une coordination étroite : 

- Le défilement de la barre de défilement verticale ou horizontale de l'un ou l'autre éditeur ajuste instantanément l'éditeur opposé selon le décalage de pixels identique. 
- ATBCmder implémente un **verrouillage de réentrée** interne (`_syncing_vscroll`, `_syncing_hscroll`) empêchant les boucles de retour d'événements, le bégaiement ou la dérive du curseur. 

---

### 3.4 Navigation de morceaux et fusion bidirectionnelle

Vous pouvez parcourir les différences sans utiliser la souris : 

- **Différence suivante** : Appuyez sur **`Alt+Down`** / `⌥↓` (ou `Ctrl+Down`). 
- **Différence précédente** : Appuyez sur **`Alt+Up`** / `⌥↑` (ou `Ctrl+Up`). 
- **Aller au morceau** : cliquer directement sur n'importe quelle ligne en surbrillance dans l'un ou l'autre volet définit automatiquement ce morceau comme actif.

#### Fusion bidirectionnelle (compatibilité Vimdiff `dp` / `do`)

Fusionnez les différences entre les fichiers avec une seule frappe : 

- **Copier de gauche à droite (`→`)** : Appuyez sur **`Alt+Right`** / `⌥→` (ou `Ctrl+Alt+Right` ou Vimdiff `dp` via **`Alt+P`**). Le morceau actif dans l'éditeur de gauche remplace la section correspondante dans l'éditeur de droite. 
- **Copier de droite à gauche (`←`)** : Appuyez sur **`Alt+Left`** / `⌥←` (ou `Ctrl+Alt+Left` ou Vimdiff `do` via **`Alt+O`**). Le morceau actif dans l'éditeur de droite remplace la section correspondante dans l'éditeur de gauche. 

---

### 3.5 Édition sur place et sauvegarde atomique

Contrairement aux visionneuses de différences qui traitent le texte en lecture seule, les deux volets d'ATBCmder sont des éditeurs de code entièrement fonctionnels : 

- Tapez, collez ou supprimez du texte directement dans l'un ou l'autre éditeur. 
- Chaque fois que des modifications manuelles modifient des lignes, appuyez sur **`F5`** (ou `Ctrl+R`) pour réexécuter le calcul de différence sur les tampons mis à jour. 
- Enregistrer le fichier de gauche : cliquez sur **💾 Enregistrer à gauche** (ou appuyez sur `Cmd+S` / `Ctrl+S` pendant que l'éditeur de gauche a le focus). 
- Enregistrer le fichier de droite : cliquez sur **💾 Enregistrer à droite** (ou appuyez sur `Cmd+S` / `Ctrl+S` pendant que l'éditeur de droite a le focus). 

---

### 3.6 Options de filtrage de comparaison

La barre d'outils du visualiseur de différences vous permet d'isoler les véritables changements logiques du bruit de formatage : 

- **Ignorer les espaces (`_cb_ws`)** : ignore les modifications apportées aux tabulations, aux espaces de fin et à l'indentation espaces/tabulations. 
- **Ignorer la casse (`_cb_case`)** : effectue des comparaisons de caractères insensibles à la casse. 
- **Ignorer les lignes vides (`_cb_blank`)** : Réduit les ajouts et suppressions de lignes vides, en se concentrant strictement sur les modifications substantielles du code. 

---

### 3.7 Détection des différences de fichiers binaires

Si l'un des fichiers sélectionnés pour la comparaison contient des octets nuls ou des signatures MIME binaires (par exemple des images, des exécutables, des archives compilées), ATBCmder appelle automatiquement `BinaryDiffer` : 

- Affiche côte à côte la taille des fichiers et les hachages cryptographiques SHA-256. 
- Indique clairement si les fichiers binaires sont identiques en octets ou divergents. 

---

## 4. Synchronisation d'annuaire (`Shift+F12` / `⇧F12` / `cm_SyncDirs`)

La synchronisation des arborescences de répertoires sur les disques locaux, les lecteurs de sauvegarde et le stockage réseau est la pierre angulaire des systèmes fiables. Le **Directory Synchronizer** d'ATBCmder (`SyncDirsDialog`, mappé à `fsyncdirsdlg.pas`) compare des hiérarchies de dossiers entières, détermine les opérations directionnelles exactes et prévisualise chaque copie et suppression de fichiers avant de toucher votre stockage. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figure 5.2 : Boîte de dialogue de synchronisation d'annuaire affichant l'état de comparaison récursive, les flèches de synchronisation directionnelles et les commandes de miroir asymétriques.*

### 4.1 Lancement de la synchronisation d'annuaire

1. Ouvrez le **Répertoire source** dans le panneau de gauche et le **Répertoire de destination** dans le panneau de droite. 
2. Appuyez sur **`Shift+F12`** (`⇧F12`) ou choisissez **Commands ➔ Synchronize Dirs...**. 
3. La boîte de dialogue Synchroniser les répertoires apparaît avec les deux chemins pré-remplis dans les cartes d'en-tête. 

---

### 4.2 Méthodes de comparaison et précision

Avant de synchroniser, configurez vos critères de comparaison dans la carte **Paramètres de synchronisation** : 

| Paramètre | Par défaut | Descriptif | 
| :--- | :--- | :--- | 
| **Comparez les sous-répertoires** | `Enabled` | Parcourt de manière récursive tous les répertoires imbriqués. | 
| **Comparer par contenu** | `Disabled` | Lit et vérifie les octets du fichier directement à l'aide de `filecmp.cmp`. Garantit une précision à 100 % pour les fichiers avec des horodatages identiques mais des données modifiées. | 
| **Ignorer la date** | `Disabled` | Compare les fichiers exclusivement par taille d'octet, en ignorant les horodatages de modification du système de fichiers. | 
| **Tolérance d'horodatage FAT/SMB** | `2.0 sec` | Prend automatiquement en compte les résolutions d'horodatage FAT/FAT32/exFAT de 2 secondes, évitant ainsi les faux indicateurs de non-concordance lors de la synchronisation sur macOS et les disques externes. | 

---

### 4.3 Analyse directionnelle et indicateurs d'état

Cliquez sur **Comparer** pour lancer un outil de comparaison en arrière-plan non bloquant (`SyncCompareWorker`). Le tableau de comparaison est rempli de lignes directionnelles codées par couleur : 

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
 

- **`->` (De gauche à droite)** : Le fichier de gauche est plus récent ou n'existe qu'à gauche. Action par défaut : copier vers la droite. 
- **`<-` (De droite à gauche)** : Le fichier à droite est plus récent ou n'existe qu'à droite. Action par défaut : copier vers la gauche (en mode bidirectionnel). 
- **`=` (Égal)** : Les fichiers correspondent en termes de taille et d'horodatage/contenu. Filtré hors de la liste de synchronisation active pour gagner du temps. 
- **`!=` (Conflit)** : collision répertoire/fichier incompatible ou conflit d'horodatage insoluble. Ignoré lors de la synchronisation groupée automatisée pour la sécurité des données. 

---

### 4.4 Mise en miroir asymétrique et synchronisation symétrique bidirectionnelle

ATBCmder prend en charge deux philosophies de synchronisation fondamentalement différentes :

#### 1. Synchronisation symétrique bidirectionnelle (par défaut)

- **Objectif** : aligner les deux répertoires afin qu'ils disposent tous deux des dernières versions de chaque fichier. 
- **Action** : Les fichiers marqués `->` sont copiés Gauche ➔ Droite. Les fichiers marqués `<-` sont copiés Droite ➔ Gauche. 
- **Sécurité** : aucun fichier n'est supprimé d'un côté ou de l'autre.

#### 2. Mise en miroir asymétrique (case à cocher `Asymmetric` activée)

- **Objectif** : Faire du répertoire de droite une réplique exacte et identique du répertoire de gauche. 
- **Action** : Les fichiers marqués `->` sont copiés Gauche ➔ Droite. Les fichiers à droite qui n'existent *pas* à gauche (`<- Right missing on Left`) sont **définitivement supprimés du répertoire de droite**. 
- **Cas d'utilisation** : création de miroirs de sauvegarde impeccables sur des disques de sauvegarde externes ou des partages NAS. 

---

### 4.5 Journalisation de sécurité et d'audit avant l'exécution

- **Inspecter avant la synchronisation** : examinez attentivement le tableau rempli. Vous pouvez voir les chemins relatifs exacts et les raisons opérationnelles de chaque transfert. 
- **Arrêter le contrôle** : si une tâche de comparaison ou de synchronisation importante doit être interrompue, cliquez sur **Arrêter**. Le thread d'arrière-plan se termine en toute sécurité sans laisser de fichiers partiels corrompus. 
- **Journal d'audit automatisé** : chaque copie, écrasement et suppression exécutés pendant la synchronisation est enregistré dans le **Journal des opérations** interne d'ATBCmder (`LogCategory.COPY_MOVE_LINK`, `LogCategory.DELETE`). 

---

## 5. Recherche avancée de fichiers et alimentation vers la liste (`Alt+F7` / `⌥F7` / `cm_Search`)

La localisation de fichiers spécifiques dans des structures de dossiers imbriquées constitue un goulot d'étranglement administratif courant. ATBCmder fournit une **boîte de dialogue de recherche de fichiers avancée** hautes performances (`SearchDialog`, mappée à `fFindDlg.pas`), combinant l'indexation native macOS Spotlight avec un moteur d'analyse approfondie du système de fichiers et l'indispensable fonctionnalité **Feed to Listbox**. 

![Advanced File Search](images/advanced_search_dialog.png) 
*Figure 5.3 : Boîte de dialogue de recherche avancée de fichiers avec paramètres multi-filtres, commandes d'analyse approfondie et bouton Alimenter vers la liste.*

### 5.1 Lancement de la recherche

- Appuyez sur **`Alt+F7`** (`⌥F7`) dans n'importe quel panneau ou choisissez **Commandes ➔ Rechercher des fichiers...**. 
- La boîte de dialogue de recherche s'ouvre avec le champ **Rechercher dans le répertoire** pré-rempli avec le chemin actuel du panneau actif. 

---

### 5.2 Backends à double recherche : Spotlight ou analyse approfondie

ATBCmder propose deux moteurs de recherche spécialisés : 

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
 

1. **Moteur de recherche Spotlight (`SpotlightSearchWorker`)** : sur macOS, en cliquant sur **Démarrer la recherche** (ou en appuyant sur `Enter`), vous utilisez l'index de métadonnées Spotlight du système (`mdfind`). Il récupère des milliers de chemins correspondants sur des gigaoctets de stockage en une fraction de seconde. 
2. **Moteur d'analyse approfondie (`DeepScanWorker`)** : cliquer sur **Analyse approfondie** contourne l'indexation du système et effectue une traversée directe et récursive du système de fichiers. Ceci est essentiel lors de la recherche : 
- Clés USB externes ou cartes SD sur lesquelles l'indexation Spotlight est désactivée. 
- Partages de fichiers réseau distants (SMB, SFTP, FTP, WebDAV). 
- Répertoires de build des développeurs exclus via `.metadata_never_index`. 

---

### 5.3 Critères de recherche multi-filtres

Affinez les requêtes de recherche à l'aide de paramètres granulaires dans les groupes **Général** et **Filtres avancés** : 

- **Modèle de noms de fichiers** : 
- *Caractères génériques* : caractères génériques de shell standard tels que `*.py`, `invoice_2026_*.pdf` ou `test_??.go`. 
- *Sous-chaînes* : la saisie de `draft` permet de trouver tout fichier ou dossier contenant « brouillon ». 
- *Expressions régulières* : cochez **Expression régulière** pour activer la syntaxe regex complète (par exemple `^v\d+\.\d+\.(json|xml)$`). 
- **Recherche de texte (recherche dans un fichier)** : 
- Recherche le contenu des chaînes UTF-8 et ASCII dans les fichiers texte, code source et documents. 
- Cochez **Recherche de contenu sensible à la casse** pour les correspondances exactes de casse. 
- **Plage de tailles de fichiers** : 
- Définissez la **Taille minimale** et la **Taille maximale** en kilo-octets (`KB`). La définition de la taille maximale sur `0` laisse les limites supérieures illimitées. 
- **Plage de dates** : 
- Spécifiez **Modifié au cours des N derniers jours** (par exemple, `7` jours pour trouver du travail de la semaine dernière). 

---

### 5.4 Inspection rapide dans les résultats de recherche

En parcourant les résultats de recherche dans la liste des résultats : 

- **Afficher le fichier (`F3`)** : ouvre instantanément le résultat de la recherche en surbrillance dans le listeur universel. 
- **Modifier le fichier (`F4`)** : Ouvre le fichier directement dans l'éditeur de texte intégré. 
- **Aller au fichier (`Enter` / `Go to File`)** : ferme la boîte de dialogue de recherche, navigue dans le panneau principal jusqu'au répertoire parent du fichier et place le curseur directement sur le fichier. 

---

### 5.5 La puissance de « Alimenter vers la liste »

La fonctionnalité la plus révolutionnaire des gestionnaires de fichiers orthodoxes est **Feed to Listbox** : 

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
 

1. Dans la boîte de dialogue de recherche, une fois les fichiers correspondants trouvés, cliquez sur le bouton **Alimenter à la liste**. 
2. ATBCmder ferme la boîte de dialogue et ouvre un nouvel **onglet de résultats de recherche virtuel** dans le panneau actif. 
3. Plutôt que de naviguer vers chaque dossier individuellement, tous les fichiers correspondants provenant de différentes profondeurs de répertoire apparaissent dans un seul tableau plat. 
4. **Exécuter n'importe quelle action du commandant** : 
- Sélectionnez tous les éléments ou des éléments spécifiques (`Space`, `+`, `Cmd+A`). 
- **Copier (`F5`)** ou **Déplacer (`F6`)** les fichiers correspondants dans divers dossiers vers un seul dossier de destination dans le panneau opposé. 
- **Batch Multi-Rename (`Ctrl+M`)** tous les résultats de recherche correspondants simultanément. 
- **Supprimez en toute sécurité (`F8` ou `Alt+Delete`)** les fichiers temporaires indésirables dans toute la hiérarchie d'un projet, d'un seul coup. 

---

## 6. Intégration Spotlight et système de commande sémantique (`/` & `Ctrl+Shift+F`)

Les flux de travail modernes nécessitent des requêtes agiles au-delà des boîtes de dialogue de filtrage rigides. ATBCmder intègre l'indexation macOS Spotlight directement avec un **Système de commande sémantique en langage naturel** accessible depuis la barre de commande intégrée en bas de la fenêtre principale. 

![Semantic Command Bar](images/semantic_command.png) 
*Figure 5.4 : La barre de commandes sémantiques analysant une requête en langage naturel avec des modèles de saisie semi-automatique en direct.* 

![Semantic Search](images/semantic_search_bar.png) 
*Figure 5.5 : Résultats de la recherche sémantique affichés directement dans le panneau actif.*

### 6.1 Activation des commandes sémantiques

- **Appuyez sur `/`** : Dans le panneau de fichiers actif, appuyez simplement sur la touche barre oblique (`/`). ATBCmder concentre immédiatement la barre d'édition de commande inférieure, en la pré-remplissant avec `/`. 
- **Raccourci de recherche Spotlight** : appuyez sur **`Ctrl+Shift+F`** (`⌃⇧F`) ou `Cmd+Shift+F` pour ouvrir l'interface du filtre sémantique. 
- **Rejeter** : appuyez sur `Escape` pour effacer le filtre et restaurer la liste du répertoire standard. 

---

### 6.2 Portées : locale (`/`) et mondiale (`//`)

ATBCmder fait la différence entre le filtrage au niveau des dossiers et la découverte à l'échelle du système à l'aide de conventions de préfixe :

#### 1. Portée du répertoire local (`/<query>`)

Les requêtes commençant par une simple barre oblique fonctionnent exclusivement sur le répertoire ouvert dans le panneau actif (et ses sous-dossiers si des options récursives sont spécifiées) : 

- `/larger than 10MB` : affiche uniquement les fichiers de plus de 10 mégaoctets dans le dossier actuel. 
- `/> 50MB` : Raccourci numérique pour le filtrage par taille. 
- `/today modified pdf` : Filtres pour les documents PDF modifiés au cours des dernières 24 heures. 
- `/images` : affiche uniquement les formats d'image raster et vectoriels. 
- `/source code` : affiche Python, C++, Rust, Go, JavaScript et d'autres fichiers sources. 
- `/contains "API_KEY"` : Filtres pour les fichiers texte contenant la chaîne "API_KEY". 
- `/hide *.log` : masque les fichiers journaux de l'écran actif.

#### 2. Portée globale du système (`//<query>`)

Les requêtes commençant par une double barre oblique interrogent l'intégralité du volume du système macOS via Spotlight : 

- `//today modified pdf` : recherche tous les documents PDF modifiés aujourd'hui sur l'ensemble de votre Mac. 
- `//larger than 1GB dmg` : localise tous les programmes d'installation d'images disque dépassant 1 Go. 
- `//code contains "OAuth2Handler"` : recherche tous les fichiers sources du système contenant "OAuth2Handler". 

---

### 6.3 Requêtes sémantiques assistées par l'IA (`?` ou `/?`)

Lorsqu'il est configuré avec un fournisseur d'IA (Google Gemini, OpenAI, Anthropic Claude ou Ollama local) dans *Préférences ➔ Filtre sémantique* : 

- Le préfixe d'une requête avec `?` ou `/?` achemine l'instruction en langage naturel via un analyseur LLM. 
- Exemple : `/? find all final invoices sent to client Acme last quarter over $5000` 
- L'IA traduit des formulations humaines complexes en attributs de métadonnées Spotlight précis (`kMDItemFSSize`, `kMDItemContentModificationDate`, `kMDItemTextContent`), affichant instantanément les fichiers correspondants dans le panneau. 

---

### 6.4 Remplissage automatique, catalogue (`/help`) et historique (`/history`)

Lorsque vous tapez dans la zone d'édition de la commande sémantique : 

- **Popup de complétion interactif** : un menu déroulant (`SemanticCompletionPopup`) affiche des suggestions de modèles contextuels basées sur le catalogue intégré (`semantic-command-templates.xml`). Utilisez les flèches `Down` et `Up` pour mettre en surbrillance les suggestions et appuyez sur `Tab` ou `Enter` pour accepter. 
- **Catalogue d'aide (`/help`)** : la saisie de `/help` ouvre la **boîte de dialogue d'aide des commandes sémantiques**, répertoriant des dizaines d'exemples consultables dans toutes les catégories (taille, date, type de fichier, contenu, balisage). Double-cliquez sur n'importe quelle entrée pour l'insérer dans la ligne de commande. 
- **Historique des commandes (`/history`)** : La saisie de `/history` affiche un journal chronologique de toutes les commandes sémantiques précédemment exécutées avec des horodatages d'exécution, permettant un rappel instantané. 

---

### 6.5 Modificateurs d'action instantanée du panneau

La barre de commandes sémantique peut également manipuler les sélections et le tri des panneaux sans toucher la souris : 

| Commande sémantique | Action exécutée | 
| :--- | :--- | 
| `/select all visible` | Sélectionne tous les éléments actuellement affichés après le filtrage. | 
| `/clear selection` | Désélectionne tous les éléments du panneau. | 
| `/invert selection` | Inverse l'état actuel de la sélection de fichier. | 
| `/select images` | Ajoute tous les fichiers image du panneau à la sélection actuelle. | 
| `/sort by size descending` | Trie la table de fichiers par taille, du plus grand au plus petit. | 
| `/reset sort` | Restaure le tri alphabétique des noms par défaut. | 
| `/group by date` | Regroupe les fichiers dynamiquement par tranches de date de modification. | 
| `/clear filter` | Supprime tous les filtres sémantiques actifs et restaure la liste complète des répertoires. | 

---

## 7. Utilitaires de fichiers essentiels et intégrité des données

Au-delà de la recherche et du renommage par lots, ATBCmder intègre une suite d'utilitaires système essentiels conçus pour gérer des fichiers volumineux, auditer la sécurité et vérifier l'intégrité cryptographique.

### 7.1 Séparateur de fichiers volumineux (`cm_FileSpliter` / `cm_Split` / `Alt+F6`)

Lors du transfert d'images disque volumineuses, d'archives vidéo ou de conteneurs de machines virtuelles sur des périphériques de stockage avec des limites de taille de système de fichiers (telles que la limite de 4 Go du FAT32) ou des limites de pièces jointes aux e-mails, le **File Splitter** (`SplitWorker`) divise les fichiers en segments séquentiels numérotés : 

1. Sélectionnez le fichier volumineux dans le panneau actif. 
2. Choisissez **Fichiers ➔ Fractionner le fichier...** (ou déclenchez `cm_Split`). 
3. Choisissez le répertoire de destination (par défaut, le panneau opposé). 
4. Sélectionnez un préréglage de taille de bloc standard ou entrez une taille d'octet personnalisée : 
- **1,44 Mo** : disquette héritée de 3,5 pouces. 
- **700 Mo** : capacité CD-R standard. 
- **4,7 Go** : capacité DVD-R monocouche. 
- **100 Mo** : morceau de téléchargement standard. 
- **Taille personnalisée** : seuil d'octets, de Ko, de Mo ou de Go défini par l'utilisateur. 
5. Cliquez sur **OK**. ATBCmder divise le fichier source dans un thread de travail en arrière-plan, créant des fichiers de séquence `.001`, `.002`, `.003`.... 

---

### 7.2 Éditeur de fichiers et combinateur (`cm_FileLinker` / `cm_Combine` / `Alt+F7`)

Le réassemblage de morceaux de fichiers divisés dans le fichier intact d'origine est transparent : 

1. Dans le panneau de fichiers, mettez en surbrillance la **première partie divisée** (doit se terminer par l'extension `.001`). 
2. Choisissez **Fichiers ➔ Combiner des fichiers...** (ou déclenchez `cm_Combine`). 
3. ATBCmder détecte automatiquement toutes les parties séquentielles (`.001`, `.002`, `.003`... jusqu'à `.999`). 
4. Sélectionnez le nom du fichier de sortie et le répertoire cible. 
5. Cliquez sur **OK**. Le travailleur en arrière-plan (`CombineWorker`) concatène séquentiellement les parties dans une réplique binaire exacte octet par octet. 

---

### 7.3 Sommes de contrôle et vérification cryptographiques (`cm_CheckSumCalc`, `cm_CheckSumVerify`)

Vérifier que les fichiers téléchargés, les images disque ou les sauvegardes d'archives n'ont pas été corrompus ou falsifiés est essentiel pour l'intégrité des données. ATBCmder comprend un **calculateur et vérificateur de somme de contrôle** intégré (`ChecksumDialog`). 

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

#### Calcul des hachages (`cm_CheckSumCalc` / `Ctrl+X`)

1. Sélectionnez un ou plusieurs fichiers dans le panneau. 
2. Choisissez **Fichiers ➔ Calculer la somme de contrôle...** (ou appuyez sur `Ctrl+X`). 
3. Sélectionnez l'algorithme souhaité : **MD5**, **SHA1**, **SHA256** ou **SHA512**. 
4. Cliquez sur **Calculer**. Le travailleur diffuse les fichiers via des blocs de 64 Ko en arrière-plan sans verrouiller l'interface. 
5. Cliquez sur **Enregistrer dans un fichier** pour exporter les hachages dans un fichier manifeste standard `.sha256` ou `.md5`.

#### Vérification des manifestes de somme de contrôle (`cm_CheckSumVerify`)

1. Choisissez **Fichiers ➔ Vérifier les sommes de contrôle...**. 
2. Sélectionnez un fichier de somme de contrôle existant (`.sha256`, `.md5`, `.sha1`, `.sha512` ou `.sfv`). 
3. ATBCmder analyse automatiquement le manifeste, localise les fichiers correspondants dans le même répertoire, recalcule les hachages sur le disque et présente un rapport d'état codé par couleur : 
- **`OK`** : Le fichier correspond parfaitement à la somme de contrôle. 
- **`FAILED`** : Corruption ou modification de données détectée ! 
- **`MISSING`** : Fichier référencé introuvable dans le répertoire. 

---

### 7.4 Déchiquetage/effacement sécurisé des fichiers (`cm_Wipe` / `Alt+Delete` / `⌥⌫`)

La suppression de fichiers standard dissocie simplement les entrées du répertoire, laissant les blocs de données brutes intacts sur le disque où les utilitaires de récupération peuvent les extraire. Lors de la gestion de clés confidentielles, d'informations d'identification ou de code source propriétaire, utilisez **Secure Delete/Wipe** (`cm_Wipe`) : 

1. Sélectionnez les fichiers ou répertoires confidentiels. 
2. Appuyez sur **`Alt+Delete`** (`⌥⌫`) ou choisissez **Fichier ➔ Suppression sécurisée (Wipe)...**. 
3. Confirmez l'invite d'alerte de sécurité. 
4. **La séquence de déchiquetage cryptographique multi-passes (`wipe_path`)** : 
- **Pass 1** : écrase toute la longueur des octets du fichier par des octets pseudo-aléatoires cryptographiquement sécurisés (`os.urandom`). 
- **Pass 2** : écrase l'intégralité du fichier avec des octets nuls (`\x00`). 
- **Pass 3** : écrase avec de nouveaux octets aléatoires. 
- **Hardware Sync** : appelle `os.fsync()` sur le descripteur de fichier sous-jacent pour forcer le cache du système d'exploitation et du contrôleur de stockage à écrire des données sur un support physique. 
- **Troncation & Unlink** : tronque le fichier à 0 octet avant d'appeler `os.unlink()`. 
- **Directory Scrubbing** : efface de manière récursive tous les fichiers contenus avant de dissocier les répertoires parents. 

---

### 7.5 Terminal du système embarqué (`Ctrl+J` / `⌃J` / `cm_RunTerm`)

Bien qu'ATBCmder excelle dans les workflows graphiques à double panneau, l'accès au shell est souvent requis pour la compilation, les branches git ou la gestion du serveur : 

- Appuyez sur **`Ctrl+J`** (`⌃J`) ou choisissez **Commands ➔ Run Terminal**. 
- ATBCmder ouvre immédiatement macOS **Terminal.app** (ou votre émulateur de terminal par défaut configuré) avec son répertoire de travail initialisé avec le chemin exact ouvert dans le panneau actif. 
- Pas besoin de taper `cd /Users/...` ou de faire glisser des dossiers dans les fenêtres du terminal. 

---

## 8. ⚡ Conseils de pro et flux de travail d'automatisation approfondis

### 8.1 Recette : Recherche récursive ➔ Alimentation vers la liste ➔ Multi-Rename

**Objectif** : Supprimez les numéros de version de centaines de fichiers d'actifs dispersés dans 50 sous-dossiers imbriqués. 

1. Ouvrez la racine du projet dans le panneau de gauche. 
2. Appuyez sur **`Alt+F7`** pour ouvrir la recherche. 
3. Dans Modèle de noms de fichiers, entrez : `*_v[0-9]*.png`. 
4. Cliquez sur **Lancer la recherche**. Une fois que les éléments correspondants apparaissent, cliquez sur **Alimenter vers la zone de liste**. 
5. Dans l'onglet du panneau virtuel résultant, sélectionnez tous les fichiers avec **`Cmd+A`**. 
6. Appuyez sur **`Ctrl+M`** pour lancer l'outil Multi-Rename. 
7. Dans **Rechercher**, saisissez : `_v\d+`. Activez **Utiliser des expressions régulières (Regex)**. 
8. Laissez **Remplacer par** vide. 
9. Vérifiez que le tableau d'aperçu en direct affiche des noms de fichiers propres sans suffixes de version. 
10. Cliquez sur **Démarrer Renommer**. ATBCmder renomme instantanément chaque fichier des 50 sous-dossiers ! 

---

### 8.2 Recette : mise en miroir sécurisée des sauvegardes Cloud et NAS avec synchronisation asymétrique

**Objectif** : Conservez un miroir hors site identique de vos documents sur un disque SSD externe ou un disque NAS SMB sans accumulation de fichiers en double. 

1. Ouvrez le `~/Documents` local dans le panneau de gauche. 
2. Ouvrez `/Volumes/BackupSSD/Documents` dans le panneau de droite. 
3. Appuyez sur **`Shift+F12`** (`cm_SyncDirs`). 
4. Dans Paramètres, assurez-vous que **Comparer les sous-répertoires** est coché. 
5. Cochez **Asymétrique (Supprimer la cible si elle est manquante dans la source)**. 
6. Cliquez sur **Comparer**. 
7. Passez en revue la liste : 
- Les flèches bleues/vertes (`->`) indiquent les fichiers qui seront copiés dans la sauvegarde. 
- Les suppressions rouges (`<-`) indiquent des fichiers obsolètes sur le disque de sauvegarde que vous avez depuis supprimés localement. 
8. Cliquez sur **Synchroniser**. Votre lecteur de sauvegarde est désormais un miroir de votre dossier local. 

---

### 8.3 Recette : le hachage médico-légal se manifeste avant le stockage des archives à long terme

**Objectif** : Calculer et stocker les sommes de contrôle cryptographiques pour un projet de plusieurs téraoctets avant de le déplacer vers un stockage sur bande froide ou sur un glacier cloud. 

1. Accédez au répertoire contenant les livrables de votre projet. 
2. Sélectionnez tous les éléments (`Cmd+A`) et appuyez sur **`Ctrl+X`** (`cm_CheckSumCalc`). 
3. Définissez l'algorithme sur **SHA256**. 
4. Cliquez sur **Calculer**. Le gestionnaire de hachage de streaming traite les fichiers en arrière-plan. 
5. Cliquez sur **Enregistrer dans un fichier** et nommez-le `MANIFEST-SHA256.txt`. 
6. Chaque fois que vous récupérez les fichiers des années plus tard, sélectionnez simplement `MANIFEST-SHA256.txt` et exécutez **Verify Checksums** pour garantir une pourriture zéro des bits ou une corruption silencieuse. 

---

### 8.4 Recette : combinaison du filtrage sémantique du langage naturel avec une vue de branche plate (`Cmd+B`)

**Objectif** : Recherchez et organisez tous les fichiers multimédias dans une structure de répertoires profonde et complexe sans ouvrir de boîtes de dialogue de recherche. 

1. Mettez en surbrillance votre dossier de projet de niveau supérieur et appuyez sur **`Cmd+B`** (`cm_FlatView`) pour aplatir tout le contenu du sous-dossier en une seule liste. 
2. Appuyez sur **`/`** pour focaliser la barre de commandes sémantiques. 
3. Tapez : `/images larger than 5MB`. 
4. La liste aplatie isole instantanément les images haute résolution dans chaque répertoire imbriqué. 
5. Appuyez sur `/select all visible`, puis sur **`F5`** pour les copier tous dans un répertoire cible organisé dans le panneau opposé. 
6. Appuyez à nouveau sur `Cmd+B` pour restaurer la navigation normale dans l'arborescence hiérarchique. 

---

## 9. Alertes de sécurité, de performances et de système

> [!CAUTION] 
> **Irréversibilité de la synchronisation asymétrique des annuaires** 
> L'activation de l'option **Asymétrique** dans la synchronisation d'annuaire (`Shift+F12`) entraîne la **suppression définitive** des fichiers du répertoire cible qui n'existent pas dans la source. Effectuez toujours une inspection visuelle du tableau d'aperçu de comparaison avant de cliquer sur **Synchroniser**. 

> [!WARNING] 
> **Substitutions RegEx multi-renommages** 
> Lorsque vous effectuez des substitutions d'expressions régulières avec des références arrière (`$1`, `$2`), assurez-vous que les numéros de votre groupe de capture correspondent aux parenthèses de votre modèle. Testez votre modèle par rapport aux lignes du tableau d'aperçu en direct avant de cliquer sur **Démarrer Renommer**. Si des noms de cibles en double apparaissent, ATBCmder bloque l'exécution pour vous protéger contre la perte de données. 

> [!IMPORTANT] 
> **Limites de déchiquetage des disques SSD (Solid State Drive)** 
> L'utilitaire Secure Wipe (`cm_Wipe` / `Alt+Delete`) écrase les données du fichier avec plusieurs passages d'octets aléatoires et nuls, suivis d'un appel `fsync`. Cependant, les disques SSD (Solid State Drives) modernes utilisent des algorithmes de nivellement de l'usure et un surprovisionnement au niveau du contrôleur qui peuvent rediriger les écritures vers des blocs Flash alternatifs. Pour une élimination des SSD de haute sécurité, combinez le déchiquetage de fichiers avec le chiffrement complet du disque macOS FileVault. 

> [!NOTE] 
> **Disponibilité Spotlight sur les volumes réseau et FAT** 
> La recherche rapide Spotlight (`Ctrl+Shift+F`) s'appuie sur les index de métadonnées macOS, qui sont actifs par défaut sur les lecteurs APFS internes. Les supports réseau distants (SMB, SFTP) et les lecteurs exFAT externes ne peuvent pas être indexés par Spotlight. Si une requête Spotlight ne renvoie aucun résultat sur un lecteur externe, utilisez **Analyse approfondie** (`Alt+F7`) ou activez l'analyse récursive des répertoires. 

> [!TIP] 
> **Compatibilité des touches de fonction Apple (`Fn`)** 
> Sur les Apple Magic Keyboards et MacBooks, les touches de fonction (`F1`-`F12`) sont par défaut sur les actions matérielles (luminosité, volume). Pour appuyer sur `Shift+F12` ou `Alt+F7`, maintenez la touche **`Fn`** : `Fn+Shift+F12`, `Fn+Alt+F7`. Vous pouvez également activer **"Utiliser les touches F1, F2, etc. comme touches de fonction standard"** dans macOS *Paramètres système ➔ Clavier ➔ Raccourcis clavier clavier ➔ Touches de fonction*. 

---

## 10. Tableau de référence du clavier principal à double matrice

| Domaine fonctionnel | Description de l'action | Raccourci macOS | Clé de commandant classique | ID de commande | 
| :--- | :--- | :--- | :--- | :--- | 
| **Multi-Renommer** | Lancer l'outil de renommage multiple par lots | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | 
| **Multi-Renommer** | Exécuter/Démarrer Renommer | `Enter` / `⏎` | `Enter` | — | 
| **Multi-Renommer** | Outil Annuler/Fermer | `Esc` | `Esc` | — | 
| **Différence de fichier** | Comparer les fichiers/volets sélectionnés | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | 
| **Différence de fichier** | Passer à la différence suivante | `Alt+Down` / `⌥↓` | `Ctrl+Down` | — | 
| **Différence de fichier** | Aller à la différence précédente | `Alt+Up` / `⌥↑` | `Ctrl+Up` | — | 
| **Différence de fichier** | Copier Hunk de gauche à droite | `Alt+Right` / `⌥→` / `Alt+P` | `Ctrl+Alt+Right` | — | 
| **Différence de fichier** | Copier Hunk de droite à gauche | `Alt+Left` / `⌥←` / `Alt+O` | `Ctrl+Alt+Left` | — | 
| **Différence de fichier** | Enregistrer les modifications dans l'éditeur ciblé | `Cmd+S` / `⌘S` | `Ctrl+S` | — | 
| **Différence de fichier** | Recalculer les différences | `F5` / `Fn+F5` | `Ctrl+R` | — | 
| **Synchronisation d'annuaire**| Ouvrir les répertoires de synchronisation | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | 
| **Synchronisation d'annuaire**| Démarrer la comparaison des annuaires | `Alt+C` / `⌥C` | `Enter` | — | 
| **Synchronisation d'annuaire**| Annuler la comparaison/synchronisation | Cliquez sur `Stop` | `Esc` | — | 
| **Recherche de fichiers** | Ouvrir la boîte de dialogue de recherche avancée | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | 
| **Recherche de fichiers** | Afficher le résultat dans Universal Lister | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Recherche de fichiers** | Modifier le résultat dans l'éditeur de texte | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Recherche de fichiers** | Accédez au fichier dans le panneau actif | `Enter` / `⏎` | `Enter` | — | 
| **Recherche de fichiers** | Envoyer les résultats au panneau virtuel | Cliquez sur `Feed to listbox` | Cliquez sur `Feed to listbox` | — *(Action de boîte de dialogue)* | 
| **Pleins feux et PNL**| Recherche rapide Spotlight | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menu Commandes)* | 
| **Pleins feux et PNL**| Activer la barre de commandes sémantique | `/` | `/` | `cm_VisSemanticCommand` | 
| **Pleins feux et PNL**| Ignorer le filtre sémantique | `Esc` | `Esc` | — | 
| **Utilitaires de fichiers**| Diviser le fichier en morceaux | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Utilitaires de fichiers**| Combiner des morceaux divisés numérotés | Menu : Fichiers ➔ Combiner des fichiers | — | `cm_FileLinker` / `cm_Combine` | 
| **Utilitaires de fichiers**| Calculer la somme de contrôle (hachage) | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | 
| **Utilitaires de fichiers**| Vérifier le fichier manifeste de somme de contrôle | Menu Outils | Menu Outils | `cm_CheckSumVerify` / `cm_VerifyChecksum` | 
| **Utilitaires de fichiers**| Effacement multi-passes sécurisé (Shred)| `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | 
| **Utilitaires de fichiers**| Ouvrir le terminal macOS natif | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` |

--- 

<div align="center"> 
<p>Prêt à vous connecter à des serveurs distants et à explorer les archives virtuelles ?</p> 
<p><strong><a href="network_and_vfs.md">Passer au chapitre 6 : Systèmes de fichiers virtuels et réseau &rarr;</a></strong></p> 
</div>