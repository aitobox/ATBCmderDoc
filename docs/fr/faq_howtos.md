# Chapitre 9: Recettes pratiques et dépannage

Alors que les gestionnaires de fichiers orthodoxes à double panneau sont réputés pour leur vitesse brute et l'efficacité de leur clavier, la maîtrise des tâches du monde réel nécessite souvent de comprendre comment des sous-systèmes distincts, tels que la synchronisation d'annuaires, le renommage de modèles par lots, les systèmes de fichiers virtuels distants, le reconditionnement d'archives et la recherche récursive, fonctionnent ensemble dans les scénarios quotidiens. De plus, fonctionner dans macOS moderne introduit des limites de sécurité, des contraintes de bac à sable et des intersections de raccourcis système que chaque utilisateur finit par rencontrer. 

Ce chapitre est divisé en deux sections complètes : 

1. **Recettes pratiques & cas d'usage réels** : cinq procédures pas à pas complètes de bout en bout couvrant les flux de travail de gestion de fichiers de grande valeur avec des procédures étape par étape, des représentations visuelles de l'interface utilisateur, des raccourcis clavier et des conseils d'utilisateurs expérimentés. 
2. **Guide de dépannage et FAQ** : explications détaillées et résolutions de diagnostic pour les questions opérationnelles courantes, les erreurs d'autorisation, les comportements d'actualisation automatique, les réinitialisations de configuration, les touches de fonction du clavier Apple et les mécanismes de transfert de fichiers entre volumes. 

---

## 1. Démarrage rapide visuel : matrice de résolution de problèmes quotidiens

La matrice de décision suivante mappe les objectifs courants de gestion de fichiers et les défis techniques directement aux outils intégrés et aux identifiants de commande d'ATBCmder : 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      ROUTEUR DE TÂCHES QUOTIDIENNES ET DÉPANNAGE                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TÂCHE / OBJECTIF                          OUTIL / MÉTHODE          RACCOURCI          │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Synchroniser des projets vers NAS/DDE Synchronisation dossiers Shift+F12 (⇧F12)   │
│  [2] Renommer des photos par date / lot    Renommage par lot       Ctrl+M (⌃M)         │
│  [3] Monter un NAS, FTP ou serveur cloud   Gestionnaire VFS réseau cm_ManageConnections│
│  [4] Modifier un fichier dans .zip         VFS archive + Éditeur   Entrée ➔ F4 ➔ Sauver│
│  [5] Trouver de gros fichiers imbriqués    Vue plate (Branch View) Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLÈME / SYMPTÔME                       CAUSE RACINE            RÉSOLUTION          │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Erreur « Operation not permitted »        Bac à sable macOS / TCC cm_GrantAccess      │
│  Les disques externes ne s'actualisent pas FSEvents absent sur FAT attr_poll_interval  │
│  Tester des réglages sans aucun risque     Protection du XML de prod ATBCmder_test.sh  │
│  Touches F règlent son/luminosité          Médias standard macOS   Touche Fn / Réglages│
│  Déplacement lent entre deux volumes       Copie + Suppression     Vérifier l'espace   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Tableau de référence rapide à double matrice

| Actions/Diagnostic | Raccourci macOS | Touche Commander classique | ID de commande | Objectif principal | 
| :--- | :--- | :--- | :--- | :--- | 
| **Synchronisation du répertoire** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Compare et synchronise les arborescences de répertoires à double panneau. | 
| **Renommage multiple par lots** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Renomme plusieurs fichiers à l'aide de jetons, de compteurs et de RegEx. | 
| **Connexions réseau** | Menu : Réseau | `cm_ManageConnections`| `cm_ManageConnections`| Gère les profils de serveur SMB, SFTP, WebDAV et FTP enregistrés. | 
| **Connexion réseau rapide** | Menu : Réseau | `cm_NetworkConnect` | `cm_NetworkConnect` | Boîte de dialogue de connexion ad hoc pour les serveurs distants. | 
| **Édition directe dans l'archive** | `F4` / `Fn+F4` | `F4` | `cm_Edit` | Modifie le élément de l'archive ; déclenche `RepackWorker` lors de la sauvegarde. | 
| **Vue arborescente plate (Flat Branch View)** | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | Affiche de manière récursive tous les fichiers imbriqués dans une seule liste plate. | 
| **Recherche avancée** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` | Recherche de fichiers multi-filtres avec sortie « Feed to Listbox ». | 
| **Accorder l'accès au système de fichiers**| Menu : Fichier / Aide | — | `cm_GrantFilesystemAccess`| Lance l’assistant d’autorisation macOS App Sandbox. | 
| **Actualisation manuelle du panneau** | `Ctrl+R` / `⌃R` ou `Cmd+R` / `⌘R` | `Ctrl+R` | `cm_Refresh` | Force une relecture immédiate du répertoire à partir du disque. | 
| **Lancer le terminal du système** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Génère le terminal macOS au chemin actuel du panneau. | 
| **Calculer l'espace du dossier** | `Alt+Shift+Enter` (`Space`) | `Alt+Shift+Enter` (`Space`) | `cm_CountDirContent` / `cm_CalculateSpace` | Calcule la taille d'octet récursive globale (`Space` pour un seul, `Ctrl+L` pour le total sélectionné). | 
| **Effacement sécurisé (Broyage définitif)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Écrasement multi-passes et suppression permanente des fichiers. | 

---

## 2. Recettes pratiques & cas d'usage réels

### 2.1 Recette 1 : Comparaison et synchronisation de deux dossiers de sauvegarde

**Objectif** : Assurez-vous qu'un lecteur de sauvegarde externe ou un dossier réseau contient une réplique exacte et à jour de votre répertoire de projet actif, avec une visibilité complète sur les fichiers ajoutés, modifiés ou supprimés avant d'apporter des modifications. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figure 9.1 : La boîte de dialogue Synchronisation d'annuaire affichant des comparaisons d'annuaire côte à côte, des flèches de copie directionnelles et des options de miroir asymétrique.*

#### Procédure étape par étape

1. **Alignez la source et la cible dans deux panneaux** : 
- Dans le **Panneau de gauche**, accédez à votre répertoire de travail local principal (par exemple, `~/Documents/Projects/AppAlpha`). 
- Appuyez sur **`Tab`** pour passer au **Panneau de droite** et accédez à votre destination de sauvegarde cible (par exemple, `/Volumes/BackupDrive/Backups/AppAlpha`). 
2. **Lancer la synchronisation des annuaires** : 
- Appuyez sur **`Shift+F12`** (`⇧F12`) ou sélectionnez **Commands ➔ Synchronize Dirs...** dans la barre de menu. 
- La boîte de dialogue Synchroniser les répertoires s'ouvre avec le chemin gauche et le chemin droit automatiquement renseignés. 
3. **Configurer les paramètres de comparaison** : 
- Cochez **Comparer les sous-répertoires** pour parcourir tous les dossiers imbriqués de manière récursive. 
- Cochez **Comparer par contenu** si vous avez besoin d'une certitude cryptographique (vérification des octets du fichier via `filecmp`) plutôt que de vous fier uniquement à la taille des fichiers et aux horodatages de modification. 
- Assurez-vous que la **Tolérance d'horodatage FAT/SMB (2,0 secondes)** est activée si votre destination de sauvegarde utilise FAT32, exFAT ou un partage réseau SMB, afin d'éviter les faux indicateurs de non-concordance provoqués par un arrondi d'horodatage de 2 secondes du système de fichiers. 
4. **Lancer la comparaison** : 
- Cliquez sur **Comparer** (ou appuyez sur `Alt+C` / `⌥C`). 
- ATBCmder exécute un outil de comparaison en arrière-plan (`SyncCompareWorker`) et remplit le tableau de comparaison avec des indicateurs d'action directionnelle : 
* **`->` (De gauche à droite)** : Le fichier local est plus récent ou n'existe qu'à gauche. Action : copier de gauche à droite. 
* **`<-` (Right to Left)**: The backup file is newer, or only exists on the right. Action: copy right to left.
     * **`=` (Equal)**: Both files are identical in size and timestamp/content. These are hidden from the pending action list by default.
     * **`!=` (Conflict)**: Incompatible directory-versus-file collision or timestamp mismatch requiring manual inspection.
5. **Select Your Synchronization Strategy**:
   - **Two-Way Symmetric Sync (Default)**: Copies newer files in both directions (`->` et `<-`). No files are deleted on either side. Ideal for syncing collaborative folders between machines.
   - **Asymmetric Mirroring (`Asymmetric` Checkbox Enabled)**: Makes the Right directory an exact binary replica of the Left directory. Any file on the Right that does not exist on the Left is **permanently deleted from the backup target**.
6. **Review and Execute**:
   - Inspect the summary count at the bottom: *e.g., "Left to Right: 42 files (128.4 MB) | Right to Left: 0 files | Deletes: 3 files"*.
   - Click **Synchronize** to launch the non-blocking background transfer queue. Progress bars reflect active transfer volume and remaining item counts.

> [!CAUTION] 
> **Risque de perte de données en miroir asymétrique** : 
> Lorsque le mode **Asymétrique** est coché, les fichiers présents sur le lecteur cible qui ont été supprimés ou renommés sur la source seront **définitivement supprimés** sans être déplacés vers la corbeille macOS. Consultez toujours le tableau de comparaison directionnelle avant de cliquer sur Synchroniser ! 

> [!TIP] 
> **⚡ Conseil de pro : vérification au niveau du contenu pour les médias et le code** : 
> Lors de la sauvegarde de séquences vidéo ou de référentiels Git, les tailles de fichiers peuvent correspondre alors que de subtiles corruptions d'octets internes existent. Cochez toujours **Comparer par contenu** pour les archives critiques. Bien que la comparaison octet par octet prenne plus de temps via USB ou Wi-Fi, elle garantit une intégrité des données à 100 %. 

---

### 2.2 Recette 2 : Renommer par lots des photos de l'appareil photo avec des dates et des numéros de séquence

**Objectif** : Transformez des centaines de fichiers de caméra non organisés (par exemple, `DSC_0012.JPG`, `DSC_0013.JPG`, `IMG_4901.CR3`) en noms de fichiers clairs et triables tels que `2026-09-06_Vacation_001.jpg` avec des compteurs de séquence sans zéro et des aperçus de sécurité en direct. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figure 9.2 : L'outil de renommage multiple par lots comprenant des lignes d'aperçu en temps réel, des jetons de métadonnées, des contrôles de compteurs numériques et une détection de collision.*

#### Procédure étape par étape

1. **Sélectionnez les photos** : 
- Accédez au répertoire d'importation de votre caméra dans le panneau actif. 
- Sélectionnez toutes les photos en utilisant **`Cmd+A`** (`⌘A`), ou appuyez sur **`+`** sur votre clavier pour saisir un masque générique tel que `*.jpg;*.jpeg;*.cr3;*.arw`. 
2. **Lancez l'outil de renommage multiple par lots** : 
- Appuyez sur **`Ctrl+M`** (`⌃M`) ou **`Cmd+M`** (`⌘M`), ou choisissez **Fichiers ➔ Outil de renommage multiple...** dans la barre de menu. 
3. **Définissez le masque de nom de fichier** : 
- Dans le champ **Masque de nom de fichier**, saisissez la structure souhaitée à l'aide de jetons de métadonnées : 
     ```
     [Y]-[M]-[D]_Vacation_[C]
     ```


- **Explication du jeton** : 
* `[Y]` : Année à 4 chiffres de la modification du fichier (par exemple, `2026`). 
* `[M]` : mois à 2 chiffres (par exemple, `09`). 
* `[D]` : jour à 2 chiffres (par exemple, `06`). 
* `Vacation` : Texte descriptif statique. 
* `[C]` : Compteur numérique séquentiel. 
4. **Configurez la séquence de compteur** : 
- Dans la carte **Paramètres du compteur** : 
* **Commencer à** : `1` 
* **Étape** : `1` 
* **Chiffres** : `3` (cela applique un remplissage nul : `001`, `002`, `003`... jusqu'à `999`). 
5. **Supprimez les préfixes de caméra avec Rechercher et remplacer (facultatif)** : 
- Si vous souhaitez conserver une partie du nom de fichier original sans le préfixe de la caméra (par exemple, en conservant le numéro de séquence de la caméra `DSC_8941.JPG`) : 
* Définissez le **Masque de nom de fichier** sur : `[YMD]_[N5-]`. 
* `[N5-]` extrait les caractères de l'index 5 jusqu'à la fin du nom, supprimant entièrement `DSC_`. 
- Vous pouvez également utiliser les champs **Rechercher et remplacer** : 
* **Rechercher** : `DSC_` 
* **Remplacer** : `Photo_` 
* Cochez **RegEx** si vous utilisez des modèles d'expression complexes tels que `^IMG_(\d+)`. 
6. **Inspectez le tableau d'aperçu en direct** : 
- Le tableau à 3 colonnes (`Old Name`, `New Name`, `Directory`) se met à jour instantanément à chaque frappe. 
- Vérifiez la colonne **Statut** : ATBCmder met en évidence les noms de cibles en double en rouge gras avec un indicateur de collision, évitant ainsi les écrasements accidentels. 
7. **Exécutez le changement de nom** : 
- Appuyez sur **`Enter`** ou cliquez sur **Démarrer Renommer**. ATBCmder effectue les changements de nom de manière atomique sur le disque et actualise la vue du panneau. 

> [!NOTE] 
> **Sécurité des extensions** : 
> Par défaut, le **Masque d'extension** est défini sur `[E]`, préservant ainsi l'extension du fichier d'origine non modifiée. Ne supprimez jamais `[E]` sauf si vous avez explicitement l'intention de supprimer les extensions de vos fichiers.

> [!TIP] 
> **⚡ Conseil de pro : flux de travail de l'éditeur externe (`⌘I`)** : 
> Si vous disposez d'une liste irrégulière de noms de clients ou de titres de pistes, appuyez sur **`Cmd+I`** (`⌘I` / Modifier dans un éditeur externe) dans l'outil Multi-Rename. ATBCmder exporte les noms des cibles vers votre éditeur de texte par défaut. Modifiez la liste dans Vim, VS Code ou TextEdit, enregistrez le document et ATBCmder importe immédiatement les noms révisés dans la grille d'aperçu. 

---

### 2.3 Recette 3 : Connexion à un NAS domestique/bureau via SMB, SFTP ou WebDAV

**Objectif** : Montez un pool de stockage TrueNAS ou Synology sur site, un serveur Linux AWS EC2 ou un référentiel cloud Nextcloud WebDAV dans un onglet à double panneau sans jongler avec les commandes de terminal séparées ou les feuilles de connexion du Finder. 

![Remote VFS Connection](images/smb_sftp_ftp_remote_access.png) 
*Figure 9.3 : Configuration de partages réseau distants sécurisés via les protocoles SMB, SFTP et WebDAV.*

#### Procédure étape par étape

1. **Ouvrez le gestionnaire de connexions réseau** : 
- Choisissez **Réseau ➔ Gérer les connexions réseau...** dans la barre de menu native ou exécutez la commande **`cm_ManageConnections`**. 
2. **Créez un nouveau profil de connexion** : 
- Cliquez sur le bouton **`➕ New`** en bas à gauche. 
- Dans le champ **Label**, saisissez un identifiant reconnaissable (par exemple, `Synology Office NAS` ou `AWS Production Web`). 
3. **Configurer les détails du protocole et de l'hôte** : 
- **Protocole** : sélectionnez votre protocole cible dans la liste déroulante : 
* **SMB/CIFS** : Port `445` (Standard pour Synology, QNAP, Windows Server, TrueNAS). 
* **SFTP (SSH File Transfer)** : Port `22` (Standard pour les instances cloud Linux/UNIX). 
* **WebDAV / WebDAVS** : Port `80` ou `443` (Standard pour Nextcloud, ownCloud). 
* **FTP / FTPS** : Port `21` ou `990` (hôtes de fichiers hérités). 
- **Hôte** : saisissez l'adresse IP ou le nom de domaine (par exemple, `192.168.1.100` ou `sftp.mycompany.com`). 
- **Port** : défini automatiquement lorsque le protocole est choisi ; ajustez si votre serveur utilise un port non standard. 
- **Nom d'utilisateur** : saisissez le nom d'utilisateur de votre compte système distant. 
- **Chemin distant** : définissez le répertoire d'arrivée par défaut (par exemple, `/volume1/Media` ou `/var/www/html`). 
4. **Stockage sécurisé des informations d'identification** : 
- Entrez votre mot de passe ou votre clé d'accès. 
- Cochez **Mémoriser le mot de passe dans le trousseau macOS**. 
- **Garantie de sécurité** : ATBCmder ne stocke jamais les informations d'identification en texte brut dans les fichiers de configuration XML. Tous les secrets sont scellés cryptographiquement dans le trousseau Apple natif (`com.aitobox.atbcmder.vfs`). 
5. **Testez la connexion** : 
- Cliquez sur **`🔍 Test Connection`**. 
- ATBCmder envoie un travailleur en arrière-plan (`ConnectionTestWorker`) qui valide l'accessibilité du réseau, vérifie les clés d'hôte SSH ou les certificats TLS, vérifie les informations d'identification et affiche une alerte de réussite sans fermer la boîte de dialogue. 
6. **Connectez-vous et parcourez** : 
- Cliquez sur **`🔗 Connect`** (ou appuyez sur `Enter`). 
- Un nouvel onglet de dossier s'ouvre dans le panneau actif, affichant le chemin distant formaté en tant qu'URI VFS unifié : 
     ```
     vfs://smb://admin@192.168.1.100/volume1/Media/
     vfs://sftp://ubuntu@aws.prod.internal:22/var/www/html/
     ```


- Vous pouvez désormais parcourir, rechercher, copier (`F5`), déplacer (`F6`) et supprimer (`F8`) des fichiers sur des disques locaux et des serveurs distants avec une agilité identique sur deux panneaux. 
7. **Reconnexion rapide depuis la barre de menu** : 
- Tous les profils enregistrés apparaissent automatiquement sous **Réseau ➔ Connexions enregistrées**. Cliquez simplement sur n'importe quel serveur enregistré pour le monter instantanément. 

> [!TIP] 
> **⚡ Conseil de pro : Authentification par clé SSH pour SFTP** : 
> Pour un accès automatisé au serveur cloud, configurez l'authentification par clé publique. Dans votre profil de connexion SFTP, laissez le champ du mot de passe vide et pointez sur votre clé privée locale (par exemple, `~/.ssh/id_ed25519`). Si la clé est protégée par une phrase secrète, ATBCmder vous la demande une fois et l'enregistre en toute sécurité dans votre trousseau macOS. 

---

### 2.4 Recette 4 : Modification d'un fichier directement dans une archive sans extraction

**Objectif** : modifier un fichier de configuration imbriqué (`settings.json` ou `config.yaml`) dans une archive de plusieurs gigaoctets `.zip`, `.tar.gz` ou `.7z` sur un stockage local ou un serveur distant sans décompresser l'intégralité de l'archive sur votre disque dur. 

![Archive VFS](images/archive_vfs.png) 
*Figure 9.4 : Navigation et édition dans des archives compressées via le système de fichiers virtuel unifié `vfs://`.*

#### Procédure étape par étape

1. **Entrez l'archive en tant que répertoire virtuel** : 
- Mettez en surbrillance le fichier d'archive (par exemple, `production_backup.zip`) dans le panneau actif. 
- Appuyez sur **`Enter`** (ou double-cliquez). 
- ATBCmder intercepte la navigation et monte l'archive en tant que système de fichiers virtuel : 
     ```
     vfs:///Users/brain/Downloads/production_backup.zip/
     ```
 

2. ** Accédez au fichier cible ** : 
- Parcourez les répertoires virtuels imbriqués (`etc`, `nginx`, `conf.d`) comme vous le feriez sur un volume physique. 
- Localisez le fichier que vous devez mettre à jour (par exemple, `nginx.conf` ou `app_settings.json`). 
3. **Ouvrir dans l'éditeur de texte intégré** : 
- Appuyez sur **`F4`** (`Fn+F4` / `cm_Edit`). 
- ATBCmder diffuse le membre compressé dans un tampon isolé temporaire et l'ouvre directement dans l'éditeur de texte avec mise en évidence de la syntaxe. 
4. **Effectuer des modifications et enregistrer** : 
- Apportez les modifications de configuration requises. 
- Appuyez sur **`Cmd+S`** (`⌘S`) pour enregistrer le tampon. 
5. **Cycle de vie du reconditionnement automatique (`RepackWorker`)** : 
- Lorsque vous enregistrez ou fermez l'éditeur, le moteur de repack en arrière-plan d'ATBCmder (`RepackWorker`) active automatiquement : 
1. Il calcule le delta entre le membre compressé d'origine et votre tampon modifié. 
2. Il vérifie la taille globale de l'archive par rapport au seuil d'avertissement configuré (`ArchiveRepackWarningMB`). 
3. Il recompresse le fichier modifié et reconstruit la structure de l'archive dans un fichier temporaire. 
4. Il remplace atomiquement le fichier d'archive d'origine sur le disque, garantissant qu'aucune corruption ne se produit si le système perd de l'alimentation en cours d'écriture. 
5. La vue du panneau actif s'actualise automatiquement pour afficher les tailles d'octets et les horodatages des membres mis à jour.

> [!IMPORTANT] 
> **Large Archive Repack Guard (`ArchiveRepackWarningMB`)** : 
> La mise à jour d'un seul fichier texte de 2 Ko dans une archive de 15 Go nécessite de réécrire l'intégralité du fichier d'archive sur le disque. Pour éviter les pics inattendus du processeur et l'usure du SSD, ATBCmder vérifie la taille de l'archive. Si l'archive dépasse `ArchiveRepackWarningMB` (par défaut : 500 Mo), une boîte de dialogue d'avertissement vous invite : *"Cette archive fait 1,4 Go. Le reconditionnement réécrira l'intégralité du fichier. Souhaitez-vous continuer ?"* Vous pouvez personnaliser ce seuil sous **Configuration ➔ Options ➔ Archives**. 

---

### 2.5 Recette 5 : Recherche et suppression de fichiers volumineux dans des répertoires imbriqués

**Objectif** : Récupérez une précieuse capacité SSD en localisant rapidement et en supprimant en toute sécurité les rendus vidéo 4K abandonnés, les dossiers `node_modules` surchargés, les images de disque virtuel Docker ou les programmes d'installation DMG obsolètes dispersés au cœur de structures de répertoires à plusieurs niveaux. 

![Flat Branch View](images/branch_view.png) 
*Figure 9.5 : Vue arborescente plate (Flat Branch View) (`Cmd+B`) affichant des contenus profondément imbriqués dans un seul tableau aplati pour un tri instantané par taille.*

#### Méthode A : aplatissement instantané via une vue de branche plate (`Cmd+B`)

1. ** Accédez au dossier racine parent ** : 
- Mettez en surbrillance le dossier parent de niveau supérieur que vous souhaitez auditer (par exemple, `~/Projects` ou `~/Downloads`). 
2. **Activer la vue de branche plate** : 
- Appuyez sur **`Cmd+B`** (`⌘B`) ou **`Ctrl+B`** (`cm_FlatView`), ou sélectionnez **Afficher ➔ Vue des branches (vue plate)**. 
- ATBCmder analyse de manière récursive tous les sous-répertoires et affiche chaque fichier imbriqué dans une **liste unique et plate**, supprimant les limites des dossiers de répertoires. 
3. **Trier par taille décroissante** : 
- Cliquez sur l'en-tête de colonne **Taille** ou appuyez sur **`Ctrl+F6`** (`cm_SortBySize`) pour trier les fichiers les plus gros vers le haut. 
- Les fichiers ISO géants, les sauvegardes de bases de données et les images de machines virtuelles flottent immédiatement en haut de votre panneau. 
4. **Calculer l'espace du répertoire** : 
- Pour les sous-dossiers visibles dans les vues standard, placez votre curseur sur n'importe quel dossier et appuyez sur **`Space`** (`␣` / `cm_CalculateSpace`). ATBCmder calcule l'empreinte totale d'octets récursifs et l'affiche à la place de l'étiquette `<DIR>` par défaut. 
5. **Quitter la vue Branche** : 
- Appuyez à nouveau sur **`Cmd+B`**, ou appuyez sur `Esc` / `Backspace` sur `..` pour revenir à la navigation normale dans le répertoire hiérarchique. 

---

#### Méthode B : Filtrage ciblé via la recherche avancée (`Alt+F7`) et "Alimenter vers la liste"

![Advanced Search](images/advanced_search_dialog.png) 
*Figure 9.6 : Boîte de dialogue de recherche avancée avec critères de filtre de taille et bouton « Alimenter à la liste ».* 

1. **Lancer la recherche avancée** : 
- Appuyez sur **`Alt+F7`** (`⌥F7`) ou sélectionnez **Commandes ➔ Rechercher...**. 
2. **Définir les filtres de taille et de type** : 
- Dans le champ **Rechercher dans**, confirmez votre répertoire racine. 
- Vérifiez le filtre **Taille** : sélectionnez **`>`** et saisissez `100` avec l'unité **`MB`** (ou `1` **`GB`**). 
- Dans le champ **Masque de fichier**, spécifiez les extensions cibles (par exemple, `*.dmg;*.iso;*.mp4;*.mov;*.zip`) ou laissez `*` pour rechercher tout élément volumineux. 
- Dans l'onglet **Date**, limitez éventuellement les résultats aux fichiers non modifiés au cours des 180 derniers jours. 
3. **Exécutez la recherche** : 
- Cliquez sur **Lancer la recherche**. 
4. **Introduire les résultats dans un onglet de panneau virtuel ("Alimenter vers la zone de liste")** : 
- Une fois les résultats remplis, cliquez sur le bouton **Alimenter à la liste**. 
- L'ensemble des résultats de recherche est transféré dans un **onglet virtuel dédié** dans votre panneau actif. 
- Contrairement à une boîte de dialogue modale statique, les fichiers de cet onglet se comportent comme des éléments normaux du panneau de fichiers : vous pouvez les prévisualiser avec Quick View (`Ctrl+Q` / `⌘Q`), les inspecter dans Universal Lister (`F3`) ou marquer plusieurs fichiers avec `Insert` / `Space`. 
5. **Vérifier et supprimer** : 
- Sélectionnez les fichiers indésirables et appuyez sur **`F8`** (`Fn+F8` / `cm_Delete`) pour les déplacer en toute sécurité vers la corbeille macOS. 
- Si vous avez besoin d'un effacement permanent et irrécupérable des données (par exemple, effacer les données confidentielles du client), appuyez sur **`Alt+Delete`** (`⌥⌫` / `cm_Wipe`) pour déclencher le déchiquetage sécurisé des fichiers en plusieurs passes. 

> [!TIP] 
> **⚡ Astuce de pro : Identification des fichiers en double identiques via des sommes de contrôle** : 
> Si vous pensez que plusieurs fichiers volumineux sont des doublons exacts, sélectionnez-les et appuyez sur **`Ctrl+X`** (`⌃X` / `cm_CheckSumCalc`). Choisissez **SHA-256** et cliquez sur Calculer. Les résumés de hachage correspondants confirment 100 % des doublons binaires, vous permettant de supprimer les copies superflues en toute confiance. 

---

## 3. Guide de dépannage et questions fréquemment posées (FAQ)

### 3.1 Erreurs « Opération non autorisée » / Autorisation macOS refusée

#### Cause première

Sous macOS moderne (macOS 12 Monterey à macOS 15 Sequoia), Apple applique des limites strictes de confidentialité **App Sandbox** et **TCC (Transparence, Consentement et Contrôle)**. Les applications en bac à sable ne peuvent pas accéder aux disques externes, aux dossiers système ou même aux répertoires d'utilisateurs standard (`~/Documents`, `~/Downloads`, `~/Desktop`) sans un jeton d'autorisation cryptographique explicite accordé par l'utilisateur, connu sous le nom de **Signet de sécurité**. 

Si ATBCmder n'a pas obtenu l'accès au système de fichiers, vous pouvez rencontrer : 

- Boîtes de dialogue d'opération de fichier affichant : `"Error: Operation not permitted"`. 
- Les répertoires apparaissent vides même si des fichiers existent dans le Finder. 
- Lecteurs externes USB ou Thunderbolt sous `/Volumes` affichant des erreurs d'accès refusé.

#### Solution 1 : utilisez l'assistant d'intégration de l'App Sandbox (`cm_GrantFilesystemAccess`)

ATBCmder comprend un assistant d'intégration intégré conçu pour enregistrer des signets de sécurité persistants avec macOS : 

```
┌─────────────────────────────────────────────────────────────┐
│  Accès au système de fichiers (Filesystem Access)       [x] │
├─────────────────────────────────────────────────────────────┤
│  ATBCmder s'exécute dans un bac à sable macOS sécurisé et   │
│  requiert votre autorisation pour accéder aux dossiers      │
│  critiques et disques de stockage externes.                 │
│                                                             │
│  [  Autoriser l'accès au répertoire racine (/)  ]           │
│                                                             │
│  [  Autoriser l'accès aux disques externes (/Volumes)  ]    │
│                                                             │
│  [  Ouvrir les réglages d'accès complet au disque…  ]       │
│                                                             │
│  L'accès racine est requis pour le bac à sable de l'app.    │
│  L'accès complet protège les données utilisateur sensibles. │
│                                                [ Terminé ]  │
└─────────────────────────────────────────────────────────────┘
```
 

1. Dans la barre de menu, choisissez **Fichier** (ou **Aide**) ➔ **Accorder l'accès au système de fichiers…**, ou déclenchez la commande **`cm_GrantFilesystemAccess`**. 
2. Cliquez sur **"Accorder l'accès au répertoire racine (/)"**. 
* Lorsque la feuille Apple `NSOpenPanel` native apparaît et pointe vers `Macintosh HD` (`/`), cliquez sur **Accorder l'accès** (ou **Ouvrir**). 
* **Pourquoi cela fonctionne** : L'autorisation de `/` génère un signet racine à portée de sécurité stocké dans `sandbox_bookmarks.plist`. Étant donné que les chemins enfants héritent des jetons de sécurité vers le bas, l'octroi de l'accès à `/` déverrouille définitivement tous les dossiers utilisateur standard (`~/Documents`, `~/Downloads`, `/Applications`, `~/Projects`). 
3. Cliquez sur **"Accorder l'accès aux disques externes (/Volumes)"**. 
* Dans la feuille ouverte, cliquez sur **Accorder l'accès** pour `/Volumes`. 
* Cela autorise toutes les clés USB connectées, les SSD externes, les cartes SD, les images disque (DMG) et les supports réseau SMB. 
4. Cliquez sur **Terminé**. Vos autorisations sont enregistrées de manière permanente lors des redémarrages de l'application.

#### Solution 2 : accorder l'accès complet au disque (FDA) dans les paramètres système macOS

Si vous devez gérer des emplacements système protégés, tels que `~/Library/Mail`, `~/Library/Messages`, les caches de navigation Safari ou les arborescences de sauvegarde Time Machine, macOS TCC nécessite un droit supplémentaire au niveau du système : 

1. Ouvrez **Paramètres système** (menu Pomme  ➔ Paramètres système). 
2. Accédez à **Confidentialité et sécurité ➔ Accès complet au disque**. 
3. Localisez **ATBCmder** dans la liste des applications et basculez le commutateur sur **On**. 
4. Si ATBCmder n'est pas répertorié : 
* Cliquez sur le bouton **`+`** en bas. 
* Authentifiez-vous avec votre mot de passe Mac ou Touch ID. 
* Sélectionnez `/Applications/ATBCmder.app` et cliquez sur **Ouvrir**. 
5. Lorsque vous êtes invité à redémarrer l'application, cliquez sur **Quitter et rouvrir**.

#### Solution 3 : Réinitialisation des autorisations de confidentialité TCC corrompues via le terminal

Si les autorisations sont corrompues après une mise à niveau du système d'exploitation macOS ou un événement de re-signature d'application, réinitialisez la base de données TCC à l'aide de l'outil de ligne de commande macOS `tccutil` : 

```bash
# Reset all Full Disk Access permissions for ATBCmder
tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder

# Reset Desktop, Documents, and Downloads folder permissions
tccutil reset SystemPolicyDocumentsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDownloadsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDesktopFolder com.aitobox.atbcmder
```
 

Après avoir exécuté ces commandes, redémarrez ATBCmder et réexécutez **`cm_GrantFilesystemAccess`**. 

---

### 3.2 Actualisation automatique ne détectant pas les modifications de fichiers sur le disque

#### Cause première

ATBCmder utilise un moteur de surveillance de fichiers à plusieurs niveaux : 

1. **Kernel `FSEvents`** : sur les volumes natifs Apple APFS et HFS+, le noyau macOS émet des événements de mutation de répertoire instantanés lorsque des fichiers sont ajoutés, modifiés ou supprimés par des outils externes. 
2. **Limitations du système de fichiers** : les systèmes de fichiers non Apple (par exemple, les clés USB externes formatées en **FAT32** ou **exFAT**) et les montages réseau à distance (**SMB**, **NFS**, **SFTP**, **WebDAV**) **ne prennent pas en charge les notifications `FSEvents` du noyau**. Lorsqu'une application tierce crée ou supprime un fichier sur un partage SMB, le noyau macOS ne reçoit aucun événement de notification.

#### Étapes de résolution

1. **Ajustez l'intervalle de repli d'interrogation (`attr_poll_interval`)** : 
- Ouvrez les Préférences via **`Cmd+,`** (`⌘,`) ou **Configuration ➔ Options...**. 
- Accédez à la page **Actualisation automatique**. 
- Vérifiez que **Surveiller le changement de nom de fichier** et **Surveiller le changement d'attributs** sont activés. 
- Ajustez l'**intervalle d'interrogation (`attr_poll_interval`)** : 
* Par défaut : `5 seconds`. 
* Pour des tests locaux rapides ou un développement de réseau actif : diminuez à `1` ou `2 seconds`. 
* Pour les partages Wi-Fi à latence élevée : augmentez à `10` ou `15 seconds` pour minimiser la surcharge du réseau. 
2. **Vérifiez la liste des répertoires exclus** : 
- Sur la même page de préférences **Actualisation automatique**, consultez le tableau **Répertoires exclus**. 
- Si votre chemin actif (ou un dossier parent) a été ajouté à la liste d'exclusion, ATBCmder supprimera délibérément la surveillance des fichiers pour conserver les cycles CPU. Supprimez le chemin si vous souhaitez réactiver la surveillance. 
3. **Vérifiez les paramètres d'actualisation en arrière-plan** : 
- Si les panneaux de fichiers ne parviennent pas à se mettre à jour uniquement lorsque ATBCmder est réduit ou derrière d'autres fenêtres, cochez l'option : 
`[ ] Disable auto-refresh when ATBCmder is in the background` 

- Décochez cette option si vous souhaitez qu'ATBCmder reflète en permanence les sorties de build en arrière-plan et les téléchargements externes. 
4. **Forcer une actualisation manuelle immédiate** : 
- À tout moment, appuyez sur **`Ctrl+R`** (`⌃R`) ou **`Cmd+R`** (`⌘R`) (`cm_Refresh`). 
- Cela contourne toutes les couches de mise en cache, vide les modèles de répertoire internes et relit immédiatement le contenu du répertoire à partir du contrôleur de stockage. 

---

### 3.3 Réinitialisation en toute sécurité de la configuration ou des tests en mode test isolé

#### Tester de nouvelles configurations en toute sécurité avec `scripts/ATBCmder_test.sh`

Lorsque vous testez des dispositions expérimentales de raccourcis clavier, de nouveaux thèmes de couleurs ou des commandes de script automatisées, vous devez éviter de modifier le XML de votre configuration de production. 

ATBCmder fournit un script de lancement de test en bac à sable : 
```bash
# Run ATBCmder in an isolated test environment
./scripts/ATBCmder_test.sh
```
 

**Comment ça marche** : 

1. Le script crée un répertoire temporaire dédié : `tests/.test_config/`. 
2. Il copie la configuration de test de base propre (`src/atbcmder/resources/test_config.xml`) dans `tests/.test_config/atbcmder.xml`. 
3. Il exporte la variable d'environnement : 
   ```bash
   export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"
   ```
 

4. Une fois lancé, ATBCmder lit tous les paramètres exclusivement à partir de ce dossier de test. Tous les changements, modifications d'onglets ou expériences de raccourcis clavier sont entièrement contenus dans `tests/.test_config/`, laissant vos préférences personnelles complètement intactes.

#### Restauration de la configuration d'usine par défaut

Si votre configuration de production est corrompue ou si vous souhaitez repartir à zéro : 

1. **Quittez complètement ATBCmder** (**`Cmd+Q`** / `⌘Q`). 
2. Ouvrez le terminal macOS et localisez votre répertoire de configuration : 
*Installation standard : `~/Library/Préférences/atbcmder/` 

* Repli Linux/XDG : `~/.config/atbcmder/` 
3. Sauvegardez ou supprimez les fichiers de configuration actifs : 
   ```bash
   # Move configuration files to a backup location
   mv ~/Library/Preferences/atbcmder/atbcmder.xml ~/Library/Preferences/atbcmder/atbcmder.xml.bak
   mv ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml.bak
   ```
 

4. Redémarrez ATBCmder. 
5. Au démarrage, ATBCmder détecte les fichiers de configuration manquants et régénère automatiquement les configurations XML propres et validées, remplies avec les paramètres d'usine officiels.

#### Exportation et importation de configurations portables

Pour migrer votre configuration sur plusieurs Mac ou créer une sauvegarde externe : 

- **Exporter** : choisissez **Configuration ➔ Exporter la configuration...** (commande **`cm_ExportConfiguration`**) pour enregistrer un instantané consolidé `.zip` ou `.xml` contenant vos raccourcis clavier, colonnes, onglets favoris et palettes de couleurs. 
- **Importer** : Choisissez **Configuration ➔ Importer la configuration...** (commande **`cm_ImportConfiguration`**) sur votre machine cible pour restaurer les paramètres instantanément. 

---

### 3.4 Touches de fonction déclenchant la luminosité/le volume de macOS au lieu de commandes

#### Cause première

Par défaut, les claviers Apple (claviers intégrés MacBook, Magic Keyboards) attribuent des fonctions matérielles spéciales à la rangée supérieure de touches : 

- `F1` / `F2` : Luminosité de l'écran vers le bas/vers le haut 
- `F3` : Contrôle de mission 
- `F4` : Pleins feux / Launchpad 
- `F7` / `F8` / `F9` : commandes de lecture multimédia (rembobinage, lecture/pause, avance rapide) 
- `F10` / `F11` / `F12` : sourdine audio, baisse du volume, augmentation du volume 

Lorsque vous appuyez sur `F5` dans l'espoir de copier un fichier, macOS intercepte la frappe et ne fait rien (ou ajuste l'éclairage du clavier).

#### Solution 1 : utilisez l'accord modificateur `Fn`

Maintenez enfoncée la touche **`Fn`** (Fonction) ou **Globe (`🌐`)** dans le coin inférieur gauche de votre clavier tout en appuyant sur la touche de fonction : 

- **`Fn+F3`** : Lister universel (`cm_View`) 
- **`Fn+F4`** : Éditeur de texte (`cm_Edit`) 
- **`Fn+F5`** : Copier des fichiers (`cm_Copy`) 
- **`Fn+F6`** : Déplacer/Renommer des fichiers (`cm_Rename`) 
- **`Fn+F7`** : Créer un nouveau dossier (`cm_MakeDir`) 
- **`Fn+F8`** : Supprimer dans la corbeille (`cm_Delete`) 
- **`Fn+Shift+F12`** : Synchroniser les répertoires (`cm_SyncDirs`)

#### Solution 2 : activer les touches de fonction standard à l'échelle du système dans les paramètres macOS

Si vous utilisez régulièrement ATBCmder, configurer macOS pour traiter les touches de fonction comme des touches `F1`-`F12` standard est la configuration recommandée : 

1. Ouvrez **Paramètres système** (menu Pomme  ➔ Paramètres système). 
2. Sélectionnez **Clavier** dans la barre latérale gauche. 
3. Cliquez sur le bouton **Raccourcis clavier clavier...**. 
4. Sélectionnez **Touches de fonction** dans la liste de gauche de la feuille modale. 
5. Allumez l'interrupteur à bascule : 
**"Utilisez les touches F1, F2, etc. comme touches de fonction standard"** 

6. Cliquez sur **Terminé**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Raccourcis clavier                                         │
├──────────────────────────────┬──────────────────────────────┤
│  Navigation au clavier       │  Utiliser les touches F1, F2 │
│  Touches de modification     │  touches standard       [OUI]│
│  Touches de fonction    ◄─── │                              │
│  Spotlight                   │  Lorsque cette option est    │
│  Mission Control             │  activée, appuyez sur la     │
│  Raccourcis de l'app         │  touche Fn pour utiliser les │
│                              │  fonctions spéciales.        │
│                              │                  [ Terminé ] │
└──────────────────────────────┴──────────────────────────────┘
```
 

*Résultat* : appuyer sur `F5` déclenche désormais directement la copie dans ATBCmder. Pour régler la luminosité ou le volume, maintenez `Fn` tout en appuyant sur la touche .

#### Solution 3 : utiliser les équivalents de clé natifs macOS `Cmd`

Si vous préférez ne pas modifier les paramètres du clavier système, ATBCmder fournit des raccourcis clavier natifs macOS pour chaque opération principale : 

- **Copie** : `Cmd+C` / `Cmd+V` (ou standard `F5`) 
- **Déplacer** : `Cmd+C` ➔ `Cmd+Option+V` (`⌥⌘V` déplacer et coller) 
- **Supprimer** : `Cmd+Delete` (`⌘⌫`) 
- **Nouveau dossier** : `Shift+Cmd+N` (`⇧⌘N`) 
- **Renommer** : `F2` ou `Return` 
- **Renommage multiple par lots** : `Ctrl+M` (`⌃M`) ou `Cmd+M` (`⌘M`) 
- **Préférences** : `Cmd+,` (`⌘,`) 
- **Fermer l'onglet** : `Cmd+W` (`⌘W`) 

---

### 3.5 Déplacement de fichiers sur différents lecteurs ou sur le même lecteur

Une question fréquente des utilisateurs est de savoir pourquoi déplacer un fichier de 20 Go dans le même dossier prend une fraction de seconde, alors que déplacer le même fichier vers un lecteur externe ou un partage réseau prend plusieurs minutes.

#### Déplacement intra-volume (même lecteur/partition APFS)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   DÉPLACEMENT SUR LE MÊME VOLUME (EN MILLISECONDES)                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso ➔ Cible: /Users/brain/Movies/             │
│                                                                                        │
│   1. L'appel système POSIX rename() met simplement à jour l'entrée d'inode du système. │
│   2. Les blocs de données physiques sur le SSD ne sont JAMAIS lus ni copiés.           │
│   3. Temps d'exécution : < 5 ms. Espace disque supplémentaire requis : 0 octet.        │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Lorsque les chemins source et de destination résident sur le **même volume physique du système de fichiers**, ATBCmder émet un appel système atomique POSIX `rename()`. Le système d'exploitation met simplement à jour les entrées de pointeur dans le catalogue de répertoires du système de fichiers. Les clusters de données physiques sur votre SSD ne bougent pas.

#### Déplacement entre volumes (différents lecteurs/partitions/montages réseau)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     DÉPLACEMENT ENTRE DEUX VOLUMES (FLUX PHYSIQUE)                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso ➔ Cible: /Volumes/ExternalSSD/Movie/      │
│                                                                                        │
│   Étape 1 : Copie du flux binaire (Lecture SSD interne ➔ Écriture SSD externe)         │
│   Étape 2 : Vérification et vidage (fsync garantit l'écriture physique complète)       │
│   Étape 3 : Suppression sécurisée de la source (le fichier source n'est délié qu'après)│
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Lors d'un transfert à travers différentes limites du système de fichiers (par exemple, depuis votre SSD Mac interne vers un lecteur USB externe, un partage réseau SMB ou une image disque), une mise à jour du pointeur atomique est physiquement impossible. ATBCmder exécute un **pipeline Copier-Vérifier-Supprimer** en plusieurs étapes : 

1. **Lecture/écriture de flux binaire** : les données sont diffusées en morceaux depuis le contrôleur de stockage source via la mémoire système et écrites sur le contrôleur de stockage cible. La durée du transfert dépend entièrement de la vitesse du bus physique (par exemple, USB 3.0 à ~100 Mo/s contre Thunderbolt 4 à ~2 800 Mo/s). 
2. **Buffer Flush & Verification** : ATBCmder appelle `fsync()` sur le descripteur de fichier de destination pour s'assurer que toutes les données mises en cache ont été écrites sur un support physique et vérifie l'équivalence du nombre d'octets. 
3. **Suppression sécurisée de la source** : Ce n'est qu'une fois que le fichier de destination a été complètement écrit et vérifié qu'ATBCmder supprime le fichier source du disque d'origine.

#### Implications critiques et garanties de sécurité

* **Espace libre requis** : le lecteur cible **doit disposer d'une capacité libre suffisante** pour stocker la charge utile complète du fichier *avant* le début de l'opération. Si vous essayez de déplacer un fichier de 30 Go vers un disque externe avec seulement 10 Go d'espace libre, le transfert échouera. 
* **Garantie zéro perte de données** : si un disque externe est accidentellement débranché ou si le stockage cible manque d'espace en cours de transfert, ATBCmder abandonne immédiatement l'opération, laisse le fichier source **complètement intact et indemne**, supprime tout fichier cible partiel et signale une boîte de dialogue d'erreur claire. 
* **Surveillance des files d'attente en arrière-plan (`cm_OperationsPanel`)** : les déplacements inter-volumes de longue durée sont exécutés sur des threads de travail en arrière-plan asynchrones (`FileOpWorker`). Vous pouvez surveiller les vitesses de transfert en temps réel, les temps restants, suspendre/reprendre les transferts ou mettre en file d'attente les opérations ultérieures sans verrouiller l'interface utilisateur. 

---

### 3.6 Questions fréquemment posées supplémentaires

#### Q1 : Comment puis-je basculer entre les panneaux gauche et droit ?

Appuyez sur la touche **`Tab`** (`⇥`). Le focus bascule instantanément entre les tables de fichiers actives et inactives. Le panneau actif affiche une bordure accentuée et un texte de barre d'état ciblé.

#### Q2 : Comment puis-je échanger le contenu des panneaux gauche et droit ?

Appuyez sur **`Ctrl+U`** (`⌃U`) ou exécutez la commande **`cm_Exchange`**. Les répertoires, les onglets de dossiers et les positions du curseur des panneaux gauche et droit s'échangent instantanément. Pour égaliser les largeurs des panneaux jusqu'à une répartition exacte de 50/50, double-cliquez n'importe où sur la barre de séparation verticale centrale.

#### Q3 : Comment sélectionner des fichiers à l'aide de modèles génériques ?

Appuyez sur la touche **`+`** de votre clavier (ou choisissez **Marquer ➔ Sélectionner un groupe...** / `cm_MarkPlus`). Entrez un modèle de caractère générique tel que `*.pdf` ou `photo_2026_*.jpg`. Pour désélectionner les fichiers correspondant à un modèle, appuyez sur la touche **`-`** (`cm_MarkMinus`). Pour inverser votre sélection actuelle, appuyez sur **`*`** (`cm_MarkInvert`).

#### Q4 : Comment puis-je activer/désactiver la visibilité des fichiers de points masqués ?

Appuyez sur **`Cmd+H`** (`⌘H`) ou **`Cmd+Shift+Period`** (`⇧⌘.`) ou exécutez la commande **`cm_ShowSysFiles`**. Les fichiers Unix masqués (fichiers commençant par un point, tels que `.zshrc`, `.gitignore`, `.env`) basculent immédiatement entre les états visible et masqué.

#### Q5 : Comment ouvrir une fenêtre de terminal macOS dans le répertoire actuel ?

Appuyez sur **`Ctrl+J`** (`⌃J`) ou exécutez la commande **`cm_RunTerm`**. ATBCmder génère une nouvelle session de terminal macOS (ou iTerm2) avec son répertoire de travail actuel défini sur le chemin exact de votre panneau de fichiers actif.

#### Q6 : ATBCmder prend-il en charge les Mac Intel (x86_64) ?

Actuellement, ATBCmder est compilé de manière native et exclusive pour les Mac **Apple Silicon (M1/M2/M3/M4, architecture ARM64)** afin de tirer pleinement parti de la mémoire unifiée d'Apple, de l'accélération matérielle Metal et des sous-systèmes Neural Engine. **Les Mac Intel (x86_64) ne sont pas pris en charge pour le moment.** 

---

## 4. Conseils de pro et liste de contrôle de maintenance du système

Pour que ATBCmder continue de fonctionner à une vitesse maximale dans les flux de travail de l'entreprise : 

- **Maintenance hebdomadaire du cache** : Si vous parcourez fréquemment les cartes d'appareil photo haute résolution, effacez périodiquement les caches de vignettes temporaires via **Configuration ➔ Options ➔ Vignettes ➔ Effacer le cache des vignettes** pour récupérer de l'espace disque. 
- **Keychain Audit** : si vous alternez les mots de passe sur des serveurs SFTP ou SMB distants, mettez à jour vos informations d'identification dans ATBCmder via **Réseau ➔ Gérer les connexions réseau...**. La modification et l’enregistrement mettent à jour de manière transparente l’élément d’identification correspondant dans votre trousseau macOS. 
- **Optimisation de la file d'attente en arrière-plan** : pour les transferts de plusieurs gigaoctets sur des réseaux de 1 Gbit/s ou 10 Gbit/s, ajustez la taille des tampons de fragments dans **Configuration ➔ Options ➔ Opérations sur les fichiers** pour maximiser la saturation du bus. 
- **Préserver les autorisations UNIX** : lors de la copie de scripts ou de binaires compilés entre des lecteurs macOS APFS, assurez-vous que **Préserver les attributs et les autorisations des fichiers** est coché dans la boîte de dialogue Copier (`F5`), en conservant automatiquement les indicateurs d'exécution (`chmod +x`). 

--- 

<div align="center"> 
<p><strong>ATBCmder Guide de l'utilisateur et portail de documentation</strong></p> 
<p> 
<a href="index.md">&larr; Revenir au portail de documentation</a> &nbsp;&bull;&nbsp; 
<a href="getting_started.md">Chapitre 1 : Principes de base</a> &nbsp;&bull;&nbsp; 
<a href="keyboard_shortcuts.md">Chapitre 8 : Raccourcis clavier</a> &nbsp;&bull;&nbsp; 
<a href="download.md">Chapitre 10 : Téléchargement et installation &rarr;</a> 
</p> 
</div>