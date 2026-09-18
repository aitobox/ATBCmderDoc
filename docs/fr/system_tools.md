# Chapitre 7: Outils système et maintenance

Un gestionnaire de fichiers professionnel ne fonctionne pas en vase clos : il constitue le centre névralgique de votre stockage, de votre mémoire vive et des ressources de votre système d'exploitation. Alors que la gestion de fichiers orthodoxe à double panneau excelle dans l'organisation, le déplacement et la synchronisation des arborescences de répertoires, les utilisateurs chevronnés, développeurs et administrateurs système sont fréquemment confrontés à des défis d'ordre système : identifier avec précision le dossier caché qui consomme silencieusement 50 Go d'espace disque, repérer un processus d'arrière-plan emballé qui sature les cœurs du processeur, purger des gigaoctets de caches de développement et d'artefacts de compilation obsolètes, et désinstaller proprement les applications macOS sans laisser de fichiers de préférences orphelins, de démons de lancement ou de dossiers de support d'application éparpillés dans `~/Library/`.

ATBCmder intègre quatre outils spécialisés de maintenance et de diagnostic système directement dans le menu **Outils**. Animés par un démon de surveillance natif et asynchrone, ces outils fonctionnent de manière transparente aux côtés de vos panneaux de fichiers sans jamais bloquer l'interface utilisateur ni nécessiter d'utilitaires tiers encombrants et truffés de publicités.

---

## 1. Démarrage rapide visuel : suite d'outils système et capsule d'état HUD

ATBCmder divise la maintenance du système en quatre instruments opérationnels fondamentaux, accompagnés d'une capsule de surveillance toujours visible dans la barre d'outils :

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    SUITE D'OUTILS SYSTÈME ATBCMDER                                     │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  [1] Capsule d'état HUD et popover      [2] État du système et diagnostics (⌘⇧M)                       │
│      • CPU, RAM et réseau en temps réel     • Barres par cœur, tableau complet des processus           │
│      • Seuils visuels par code couleur      • Filtrage des processus, envoi de SIGTERM/SIGKILL          │
│      • Clic pour popover multi-métriques    • Capacité des disques et graphiques réseau                │
│                                                                                                        │
│  [3] Analyseur d'utilisation (⌘⇧D)      [4] Nettoyeur système (⌘⇧C)                                    │
│      • Analyseur de dossiers multithread    • Nettoyeur en 2 étapes : analyser, examiner, nettoyer     │
│      • Treemap rectangulaire interactif     • 6 catégories : caches, logs, Xcode, outils dev, corbeille│
│      • Navigation par fil d'Ariane          • 3 niveaux de risque (Sûr, Avertissement, Danger) + Blanc │
│                                                                                                        │
│  [5] Désinstallateur d'applications (⌘⇧U)                                                              │
│      • Suppression complète des paquets .app et résidus profonds                                       │
│      • Nettoie Application Support, Preferences, Caches, LaunchAgents et Containers                    │
│      • Mode double : Désinstallation complète vs Résidus seuls (nettoyer les apps supprimées)          │
│                                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Matrice de raccourcis des outils système à double matrice

| Outil / Action | Raccourci macOS | Touche Commander classique | ID de commande | Emplacement dans le menu |
| :--- | :--- | :--- | :--- | :--- |
| **Panneau d'état du système** | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` | **Outils ➔ État du système...** |
| **Analyseur d'utilisation du disque** | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` | **Outils ➔ Analyseur d'utilisation du disque...** |
| **Nettoyeur système** | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` | **Outils ➔ Nettoyeur système...** |
| **Désinstallateur d'applications** | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` | **Outils ➔ Désinstaller une application...** |
| **Activer/désactiver la capsule d'état** | Préférences ➔ Général | — | *(Paramètres)* | **Configuration ➔ Options ➔ Général** |

---

## 2. Capsule d'état HUD dans la barre d'outils et popover en direct

ATBCmder intègre une **capsule d'état du système** logée directement sur le côté droit de la barre d'outils principale. Elle offre une visibilité périphérique immédiate sur l'état de santé de votre Mac sans avoir à basculer vers le Moniteur d'activité ni à ouvrir une fenêtre de Terminal distincte.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Onglets panneau gauche]           [Onglets panneau droit]      [ CPU 18% | RAM 44% | ↓1.2M ↑340K ]│
└───────────────────────────────────────────────────────────────────────────┬────────────┘
                                                                            │ Cliquer la capsule
                                                                            ▼
                                                ┌───────────────────────────────────────┐
                                                │ RÉSUMÉ DES MÉTRIQUES SYSTÈME          │
                                                ├───────────────────────────────────────┤
                                                │ Utilisation CPU :  [████░░░░░░░░░░] 18%│
                                                │ Mémoire :          [████████░░░░░░] 44%│
                                                │ Charge GPU :       [██░░░░░░░░░░░░] 12%│
                                                │ Batterie :         [████████████░░] 88%│
                                                ├───────────────────────────────────────┤
                                                │ Stockage :                            │
                                                │  Macintosh HD:  312.4 Go / 994.6 Go   │
                                                │  SSD externe:   842.1 Go / 2.0 To     │
                                                ├───────────────────────────────────────┤
                                                │ Principaux processus :                │
                                                │  • ATBCmder         PID: 54102  CPU: 2%│
                                                │  • WindowServer     PID: 284    CPU: 8%│
                                                │  • Xcode            PID: 88120  CPU: 4%│
                                                ├───────────────────────────────────────┤
                                                │ [ Ouvrir le moniteur système (⌘⇧M) ➔ ]│
                                                └───────────────────────────────────────┘
```

### 2.1 Composants de la capsule et style visuel

La capsule d'état (d'une largeur de `320px`) affiche trois métriques de télémétrie en temps réel actualisées une fois par seconde :

1. **Utilisation du processeur (CPU)** : pourcentage d'utilisation globale du processeur en direct avec un code couleur dynamique :
   - **Normale (< 75 %)** : bleu d'accentuation / couleur principale du thème.
   - **Élevée (75 % – 90 %)** : orange d'avertissement.
   - **Critique (> 90 %)** : rouge d'alerte.
2. **Utilisation de la mémoire (RAM)** : pression actuelle de la mémoire active et liée (wired) exprimée en pourcentage de la RAM physique.
3. **Débit réseau** : vitesses globales d'envoi et de réception en temps réel sur toutes les interfaces réseau actives, présentées sous forme compacte (par ex. `↓2.4 Mo/s ↑512 Ko/s`).

### 2.2 Popover interactif (`StatusPopup`)

Cliquer n'importe où sur la capsule d'état ouvre un **popover d'état** flottant et non modal :

- **Télémétrie matérielle** : affiche les pourcentages combinés du processeur, de la mémoire, du processeur graphique (GPU) et de la batterie (y compris le pourcentage de charge et l'état d'alimentation).
- **Volumes et points de montage** : répertorie tous les conteneurs APFS locaux et disques externes montés avec des jauges d'espace libre et de capacité totale.
- **Top 5 des processus** : met en évidence les cinq processus les plus gourmands en ressources selon leur utilisation processeur et leur empreinte mémoire.
- **Bouton d'accès approfondi** : cliquez sur **« Ouvrir le moniteur système »** (ou appuyez sur `⌘⇧M`) pour lancer la fenêtre de diagnostic détaillée.

### 2.3 Configuration de la visibilité de la capsule

Si vous préférez une barre d'outils épurée, dédiée exclusivement aux commandes de navigation :

1. Ouvrez les **Préférences** (`⌘,` / **Configuration ➔ Options...**).
2. Sélectionnez **Général** dans la barre latérale gauche.
3. Sous **Affichage et disposition**, cochez ou décochez la case :
   `[X] Afficher la capsule d'état du système dans la barre d'outils`
4. Cliquez sur **Appliquer** ou **OK**. La capsule apparaîtra ou disparaîtra immédiatement de la barre d'outils principale.

---

## 3. État du système et diagnostics (`cm_SystemStatus` / `⌘⇧M`)

Une pression sur **`⌘⇧M`** (ou **`Ctrl+Shift+M`**) ouvre le panneau complet **État du système**. Cet utilitaire fait office de console de diagnostic intégrée, spécialement conçue pour les administrateurs système, les développeurs et l'analyse des performances.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                ÉTAT DU SYSTÈME ET DIAGNOSTICS                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ UTILISATION CPU : Apple M3 Max (14 cœurs)                                              │
│ Cœur 01: [██████░░░░] 60%    Cœur 05: [██░░░░░░░░] 20%    Cœur 09: [███░░░░░░░] 30%    │
│ Cœur 02: [████░░░░░░] 40%    Cœur 06: [████░░░░░░] 42%    Cœur 10: [█░░░░░░░░░] 10%    │
│ Cœur 03: [████████░░] 80%    Cœur 07: [█░░░░░░░░░] 12%    Cœur 11: [░░░░░░░░░░]  5%    │
│ Cœur 04: [███░░░░░░░] 30%    Cœur 08: [██░░░░░░░░] 18%    Cœur 12: [░░░░░░░░░░]  4%    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ MÉMOIRE : Totale 36.0 Go | Utilisée : 16.2 Go (45%) | App : 9.4 Go | Fichée : 4.1 Go   │
│ FICHIER D'ÉCHANGE (SWAP) : Total 2.0 Go | Utilisé : 0 Mo (0%)                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ LISTE DES PROCESSUS                           Filtre : [ node                   ] [x]  │
│ PID      Nom              Utilisateur    % CPU       Mémoire     Fils       Action     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ 72841    node (dev-srv)   brain          48.2%       612.4 Mo    28         [ Tuer ✕ ] │
│ 72910    node (esbuild)   brain          12.1%       184.2 Mo    14         [ Tuer ✕ ] │
│ 73104    node (lsp)       brain           1.4%        98.5 Mo     8         [ Tuer ✕ ] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Intervalle : [ 1.0s ▼ ]       [ Suspendre la surveillance ]         [ Fermer (Échap) ] │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Fonctions de diagnostic et sections de métriques

1. **Moniteur de processeur multicœur** :
   - Visualise la charge système globale ainsi que la répartition entre les cœurs individuels de performance et d'efficacité énergétique.
   - Les jauges de progression par cœur mettent en évidence la saturation lors des compilations multithreads ou des rendus complexes.
2. **Répartition de la mémoire et pression du fichier d'échange (swap)** :
   - Classe l'allocation de la mémoire physique en mémoire d'application, mémoire résidente/fichée (wired), mémoire compressée et fichiers en cache.
   - Surveille l'utilisation du swap virtuel pour aider à déterminer si des fuites de mémoire provoquent des accès intempestifs au disque (paging).
3. **Aperçu du stockage et des points de montage** :
   - Métriques de débit de lecture/écriture sur disque en temps réel, accompagnées des données de capacité des volumes montés.
4. **Gestionnaire interactif de processus** :
   - Tableau triable en temps réel regroupant l'ensemble des tâches système et utilisateur en cours d'exécution.
   - **Recherche et filtrage** : saisissez le nom d'un processus ou un PID dans le champ de recherche pour filtrer instantanément les résultats.
   - **Arrêt de processus** :
     - Cliquez sur **Tuer** ou sélectionnez un processus et appuyez sur la touche `Supprimer` (`⌫`).
     - Une boîte de dialogue de confirmation vous invite à choisir entre **Terminer (`SIGTERM`)** pour une fermeture ordonnée et **Forcer l'arrêt (`SIGKILL`)** pour les tâches qui ne répondent plus.

---

## 4. Analyseur d'utilisation du disque (`cm_DiskUsageAnalyzer` / `⌘⇧D`)

Lorsqu'un disque SSD commence à manquer d'espace libre, découvrir où se cachent des dizaines de gigaoctets de données peut s'avérer fastidieux. Les listes de fichiers du Finder ne calculent pas automatiquement la taille des dossiers, et une inspection manuelle oblige à parcourir patiemment d'innombrables arborescences imbriquées.

L'**analyseur d'utilisation du disque** (`cm_DiskUsageAnalyzer`, raccourci clavier **`⌘⇧D`** / **`Ctrl+Shift+D`**) analyse des arborescences entières de manière asynchrone grâce à un moteur multithread, et représente votre espace de stockage à la fois sous la forme d'une arborescence hiérarchique classique et d'un **treemap rectangulaire interactif**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ ANALYSEUR D'UTILISATION DU DISQUE : /Users/brainzhang                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Chemin : /Users/brainzhang ➔ Developer ➔ Projects                                      │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ HIÉRARCHIE DES DOSSIERS              │ TREEMAP RECTANGULAIRE INTERACTIF                │
│ Nom du dossier   Taille     Pourcent │ ┌───────────────────────────┬─────────────────┐ │
│ ──────────────────────────────────── │ │                           │ node_modules    │ │
│ ▼ Developer      142.6 Go   58.2%    │ │ target/debug              │ 28.4 Go         │ │
│   ► Projects     118.2 Go   48.2%    │ │ 64.2 Go                   │ (build Rust)    │ │
│   ► Caches        24.4 Go   10.0%    │ │                           ├─────────────────┤ │
│ ▼ Library         64.2 Go   26.2%    │ │                           │ DerivedData     │ │
│   ► Caches        38.1 Go   15.5%    │ │                           │ 18.2 Go         │ │
│   ► App Support   22.4 Go    9.1%    │ ├───────────────────────────┴─────────────────┤ │
│ ► Downloads       24.1 Go    9.8%    │ │ Vidéos (4K ProRes)                          │ │
│ ► Pictures        14.2 Go    5.8%    │ │ 31.8 Go                                     │ │
├──────────────────────────────────────┴─┴───────────────────────────────────────────────┤
│ [ Zoom arrière (..) ] [ Afficher dans le double panneau ] [ Corbeille (⌘⌫) ] [ CSV... ]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Architecture clé et fonctionnalités

- **Analyse multithread asynchrone** : parcourt des centaines de milliers de fichiers à travers les conteneurs APFS sans bloquer l'interface principale d'ATBCmder. Une barre de progression affiche en direct le nombre de répertoires analysés par seconde.
- **Visualisation par treemap rectangulaire** :
  - Les dossiers et fichiers sont matérialisés par des blocs rectangulaires imbriqués dont la surface 2D est strictement proportionnelle à leur encombrement sur le disque.
  - Les couleurs reflètent automatiquement la profondeur hiérarchique, ce qui permet d'identifier d'un simple coup d'œil les éléments les plus volumineux.
- **Synchronisation bidirectionnelle** :
  - La sélection d'un élément dans l'arborescence met en surbrillance son bloc correspondant dans le treemap.
  - Un clic sur n'importe quel rectangle du treemap sélectionne la ligne équivalente dans la vue arborescente et affiche le chemin complet ainsi que la taille exacte en octets.

### 4.2 Navigation interactive et flux de travail

1. **Explorer en profondeur (Drill Down)** : double-cliquez sur une ligne de dossier ou sur un bloc du treemap pour vous concentrer sur ce sous-répertoire et recalculer l'affichage en fonction de cette nouvelle racine.
2. **Revenir en arrière (Zoom Out)** : cliquez sur le bouton **Zoom arrière** dans la barre d'outils ou cliquez sur un segment dans la barre de fil d'Ariane supérieure pour remonter vers les répertoires parents.
3. **Inspecter dans le double panneau** : cliquez sur **Afficher dans le double panneau** pour naviguer instantanément dans le dossier sélectionné depuis le panneau de fichiers actif d'ATBCmder.
4. **Nettoyage immédiat** : sélectionnez un dossier ou un fichier volumineux et obsolète, puis appuyez sur **`⌘⌫`** (ou cliquez sur **Placer dans la corbeille**). L'élément est envoyé en toute sécurité dans la Corbeille de macOS, et l'arborescence d'analyse est actualisée automatiquement.
5. **Exporter des rapports de stockage** : cliquez sur **Exporter** pour générer un bilan complet de l'espace disque, au format CSV structuré ou sous forme de résumé en texte brut, idéal pour planifier votre stockage.

---

## 5. Nettoyeur système (`cm_CleanSystem` / `⌘⇧C`)

Au fil des mois d'utilisation quotidienne, macOS accumule des gigaoctets de données temporaires : caches d'applications périmés, artefacts de compilation Xcode, téléchargements de gestionnaires de paquets, journaux de diagnostic orphelins et caches de navigateurs web. Si certains caches accélèrent les flux de travail, les éléments obsolètes gaspillent un espace précieux sur votre SSD haute vitesse.

Le **nettoyeur système** (`cm_CleanSystem`, raccourci clavier **`⌘⇧C`** / **`Ctrl+Shift+C`**) propose un mécanisme déterministe en deux étapes conçu avec des garanties de sécurité de niveau entreprise.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          NETTOYEUR SYSTÈME : AUDIT À BLANC (DRY RUN)                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Analyser ]    Éléments analysés : 48 192 en 2.1s        Espace récupérable : 34.8 Go │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CATÉGORIE                         ÉLÉMENTS    TAILLE      NIVEAU DE RISQUE SÉLECTION   │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ [X] Caches d'applications         12 410      14.2 Go     Sûr (Vert)     [Tout sélect.]│
│ [X] Journaux système & util.       4 218       1.8 Go     Sûr (Vert)     [Tout sélect.]│
│ [X] Données dérivées Xcode         8 940      12.4 Go     Avertis. (Org) [Tout sélect.]│
│ [ ] Caches Homebrew & CocoaPods    1 420       3.6 Go     Avertis. (Org) [Tout sélect.]│
│ [ ] Caches des navigateurs web    21 200       2.8 Go     Sûr (Vert)     [Tout sélect.]│
│ [ ] Conteneur de la Corbeille          4       8.2 Go     Danger (Rouge) [Non sélect. ]│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Sélectionné pour nettoyage : 28.4 Go répartis sur 25 568 fichiers                     │
│ Liste blanche : ~/.config/atbsys/whitelist (4 règles actives)                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Éditeur liste blanche... ]   [ Exporter le journal ]   [ Nettoyer la sélection ]     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 L'architecture de sécurité en deux étapes

Contrairement aux outils de nettoyage « en un clic » imprudents qui suppriment des fichiers silencieusement en arrière-plan, ATBCmder applique un **protocole de sécurité strict en deux étapes** :

1. **Étape 1 : Analyse préliminaire et évaluation (Dry-Run)** :
   - Le nettoyeur procède à un inventaire en lecture seule dans des emplacements système standardisés.
   - Il calcule le nombre exact de fichiers et leur taille en octets sans modifier ni supprimer le moindre élément.
   - Il regroupe les résultats par catégories transparentes associées à des niveaux de risque explicites.
2. **Étape 2 : Suppression sélective validée par l'utilisateur** :
   - Vous examinez la liste catégorisée et cochez ou décochez des éléments spécifiques ou des catégories entières.
   - Cliquer sur **« Nettoyer les éléments sélectionnés »** déclenche la suppression uniquement pour les cibles explicitement cochées.
   - Chaque opération de suppression est consignée dans un journal d'audit atomique situé dans `~/Library/Preferences/atbcmder/operations.log`.

### 5.2 Six domaines de nettoyage fondamentaux

| Catégorie | Emplacement habituel | Niveau de risque | Description |
| :--- | :--- | :---: | :--- |
| **Caches d'applications** | `~/Library/Caches/` | **Sûr** | Caches obsolètes créés par les applications de bureau, recréés automatiquement au besoin. |
| **Journaux système et utilisateur** | `~/Library/Logs/`, `/var/log/` | **Sûr** | Anciens rapports de crash, instantanés de diagnostic et journaux de mise à jour devenus inutiles. |
| **Caches des navigateurs** | Safari, Chrome, Edge, Firefox | **Sûr** | Pages web en cache, mémoires tampons multimédias et scripts des navigateurs installés. |
| **Données dérivées Xcode (DerivedData)** | `~/Library/Developer/Xcode/DerivedData` | **Avertissement** | Fichiers objets intermédiaires, caches de modules et index des compilations antérieures. |
| **Caches des gestionnaires de paquets** | Homebrew, CocoaPods, NPM, Yarn | **Avertissement** | Archives tarball téléchargées, archives de formules et dossiers de cache des paquets. |
| **Corbeille** | `~/.Trash`, `.Trashes` | **Danger** | Éléments précédemment placés dans la Corbeille de macOS qui n'ont pas encore été purgés définitivement. |

### 5.3 Niveaux de risque et liste blanche de sécurité

- 🟢 **Sûr (Vert)** : caches temporaires et métadonnées superflues qui peuvent être supprimés sans perte de configuration ni interruption de votre travail.
- 🟡 **Avertissement (Orange)** : artefacts de développement ou caches de paquets. Leur suppression est sans danger, mais les compilations ultérieures de projets ou le téléchargement des dépendances prendront plus de temps lors de leur récupération.
- 🔴 **Danger (Rouge)** : éléments nécessitant une confirmation explicite (comme le vidage définitif de la Corbeille).
- **Règles de liste blanche personnalisées** :
  - Définissez des chemins d'accès spécifiques, des extensions ou des noms de dossiers qu'ATBCmder ne doit **jamais** modifier dans `~/.config/atbsys/whitelist`.
  - Des règles de protection intégrées empêchent automatiquement l'analyse des fichiers critiques du système d'exploitation macOS, des trousseaux d'accès utilisateur et des dossiers de synchronisation hors ligne du stockage cloud.

---

## 6. Désinstallateur d'applications (`cm_UninstallApp` / `⌘⇧U`)

Sur macOS, faire glisser une application de `/Applications` vers la Corbeille ne supprime que le paquet `.app` lui-même. Les applications modernes disséminent fréquemment des centaines de fichiers annexes sur votre disque : fichiers de préférences plist, bases de données Application Support, agents de lancement en arrière-plan, conteneurs de bac à sable (sandbox) et fichiers multimédias mis en cache. Au fil du temps, ces résidus orphelins monopolisent des gigaoctets de stockage et peuvent laisser s'exécuter des processus inutiles dès l'ouverture de votre session.

Le **désinstallateur d'applications** (`cm_UninstallApp`, raccourci clavier **`⌘⇧U`** / **`Ctrl+Shift+U`**) assure une analyse approfondie des dépendances afin d'éradiquer complètement les applications et l'ensemble de leurs résidus associés.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DÉSINSTALLATEUR PROFOND D'APPLICATIONS                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Filtre : Docker                    ]  Trouvées : 142 applications (Total : 48.2 Go)   │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ APPLICATIONS INSTALLÉES              │ RÉSIDUS ASSOCIÉS ET FICHIERS DE SUPPORT         │
│ Nom d'app         Version    Taille  │ Chemin d'accès / Composant          Taille      │
│ ──────────────────────────────────── │ ─────────────────────────────────────────────── │
│ [X] Docker.app    4.28.0     1.8 Go  │ [X] /Applications/Docker.app        1.8 Go (.app│
│ [ ] Figma.app     116.15     240 Mo  │ [X] ~/Library/Application Support/Docker 14.2 Go│
│ [ ] Slack.app     4.36.0     310 Mo  │ [X] ~/Library/Caches/com.docker.docker   2.1 Go │
│ [ ] Visual Studio 1.87.0     450 Mo  │ [X] ~/Library/Preferences/com.docker...  12 Ko  │
│ [ ] Xcode.app     15.3      12.4 Go  │ [X] ~/Library/LaunchAgents/com.docker...  4 Ko  │
│                                      │ [X] ~/Library/Containers/com.docker...  380 Mo  │
├──────────────────────────────────────┴─────────────────────────────────────────────────┤
│ Mode : (•) Désinstallation complète (app + résidus)   ( ) Résidus seuls (orphelins)    │
│ Total sélectionné pour suppression : 18.48 Go répartis sur 6 éléments                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Actualiser les apps ]        [ Annuler ]             [ Désinstaller l'app (18.5 Go) ]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Emplacements de détection des résidus

Lors de l'analyse des composants d'une application, ATBCmder inspecte les sous-systèmes standard de macOS suivants en se basant sur une correspondance exacte de l'identifiant de bundle (Bundle Identifier) :

1. **Paquet d'application (Bundle)** : `/Applications/<Nom>.app` et `~/Applications/<Nom>.app`.
2. **Support d'application** : `~/Library/Application Support/<Nom>` et `<BundleID>`.
3. **Caches de l'application** : `~/Library/Caches/<BundleID>`.
4. **Préférences et réglages par défaut** : `~/Library/Preferences/<BundleID>.plist`.
5. **État de sauvegarde de l'application** : `~/Library/Saved Application State/<BundleID>.savedState`.
6. **Démons et agents de lancement** : `~/Library/LaunchAgents/<BundleID>.plist`.
7. **Conteneurs sandbox** : `~/Library/Containers/<BundleID>/` et `~/Library/Group Containers/`.
8. **Journaux de l'application** : `~/Library/Logs/<Nom>/`.

### 6.2 Deux modes de fonctionnement

- **Désinstallation complète (par défaut)** :
  - Conçu pour supprimer une application actuellement installée sur votre Mac.
  - Supprime à la fois le paquet exécutable `.app` de `/Applications` et tous les fichiers de support associés en une seule opération atomique.
- **Résidus seuls** :
  - Destiné à nettoyer les traces laissées par des applications précédemment supprimées manuellement via le Finder ou des utilitaires tiers.
  - Analyse `~/Library/` à la recherche de dossiers de support orphelins dont le paquet `.app` d'origine n'est plus présent sur le système.

### 6.3 Intégrité du système Apple et garde-fous de sécurité

Pour prévenir toute déstabilisation accidentelle du système :

- **Protection des applications système** : les applications natives intégrées à macOS (Safari, Finder, Aperçu, Musique, Réglages Système, etc.) sont signalées par une icône de cadenas en lecture seule et ne peuvent pas être désinstallées.
- **Détection des processus en cours d'exécution** : si une application ou son démon d'assistance est actuellement actif, ATBCmder vous invite à fermer l'application proprement avant de procéder à la désinstallation.
- **Priorité à la Corbeille** : tous les éléments désinstallés sont déplacés par défaut vers la Corbeille de macOS plutôt que supprimés définitivement du disque, ce qui permet une récupération intégrale en cas de besoin.

---

## 7. Alertes système et de maintenance

> [!NOTE]
> **Impact minimal sur les ressources système**  
> Le démon de surveillance d'état en arrière-plan est développé en code natif compilé et fonctionne selon un intervalle d'interrogation de 1,0 seconde. Il consomme moins de 0,1 % du processeur pendant la navigation active et suspend automatiquement son activité lorsque ATBCmder est réduit ou masqué.

> [!TIP]
> **Associer l'analyseur d'utilisation du disque à la vue arborescente plate du double panneau**  
> Si l'analyseur d'utilisation du disque repère un dossier contenant des milliers de fichiers temporaires disséminés, sélectionnez ce dossier et cliquez sur **Afficher dans le double panneau**. Appuyez ensuite sur **`Cmd+B`** (`cm_DirBranch`) pour aplatir l'arborescence complète en une liste unique dans laquelle vous pourrez trier, sélectionner et supprimer des éléments par lot avec une précision totale au clavier.

> [!IMPORTANT]
> **Toujours vérifier les sélections du nettoyeur avant de confirmer**  
> Bien que le nettoyeur système classe les caches comme **Sûr (Vert)**, certains outils de développement (comme les DerivedData de Xcode ou les volumes Docker locaux) peuvent nécessiter du temps pour recompiler ou retélécharger des ressources lors du prochain lancement de projet. Vérifiez les catégories cochées pour éviter d'effacer les caches d'un projet en cours.

> [!CAUTION]
> **Forcer l'arrêt des processus système (`SIGKILL`)**  
> Dans le gestionnaire de processus de l'état du système, l'envoi du signal `SIGKILL` (Forcer l'arrêt) interrompt immédiatement le processus cible sans lui permettre de vider ses tampons de fichiers ou d'enregistrer l'état de ses documents. Privilégiez toujours un arrêt ordonné avec `SIGTERM` en premier lieu.

> [!WARNING]
> **Suppression des conteneurs sandbox d'applications**  
> Lors de la désinstallation d'applications issues du Mac App Store, les fichiers secondaires stockés sous `~/Library/Containers/<BundleID>` contiennent souvent des bases de données de documents isolés. Assurez-vous d'avoir exporté tous les fichiers de projet essentiels avant de confirmer la suppression des conteneurs.

---

## 8. Tableau de référence général des outils système à double matrice

| Catégorie | Description de l'action | Raccourci macOS | Touche Commander classique | ID de commande |
| :--- | :--- | :--- | :--- | :--- |
| **Moniteur système** | Ouvrir le panneau de diagnostics système complet | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` |
| **Moniteur système** | Ouvrir le popover d'état léger | Cliquer sur la capsule de la barre d'outils | — | *(Action UI)* |
| **Moniteur système** | Filtrer la liste du gestionnaire de processus | `Cmd+F` (dans le panneau) | `F7` | — |
| **Moniteur système** | Terminer le processus (`SIGTERM`) | `Supprimer` / `⌫` | `Supprimer` | — |
| **Moniteur système** | Forcer l'arrêt du processus (`SIGKILL`) | `Shift+Delete` / `⇧⌫` | `Shift+Delete` | — |
| **Analyseur de disque** | Ouvrir la boîte de dialogue de l'analyseur de disque | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` |
| **Analyseur de disque** | Descendre dans le dossier sélectionné | `Entrée` / `Retour` | `Entrée` | — |
| **Analyseur de disque** | Remonter au répertoire parent | `Retour arrière` / `⌫` | `Retour arrière` | — |
| **Analyseur de disque** | Déplacer l'élément sélectionné vers la Corbeille | `Cmd+Delete` / `⌘⌫` | `F8` / `Supprimer` | — |
| **Analyseur de disque** | Afficher l'élément sélectionné dans le double panneau | `Cmd+Return` / `⌘⏎` | `Ctrl+Enter` | — |
| **Nettoyeur système** | Ouvrir la boîte de dialogue du nettoyeur sécurisé | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` |
| **Nettoyeur système** | Exécuter une analyse à blanc en lecture seule (Dry Run) | `Cmd+R` / `⌘R` | `Ctrl+R` | — |
| **Nettoyeur système** | Basculer la sélection de la catégorie | `Espace` | `Espace` | — |
| **Désinstallateur d'applications** | Ouvrir le désinstallateur d'applications | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` |
| **Désinstallateur d'applications** | Basculer en mode Résidus seuls | `Cmd+2` / `⌘2` | `Alt+2` | — |
| **Préférences** | Activer/désactiver la capsule d'état dans la barre d'outils | Préférences ➔ Général | — | *(Configuration)* |

---

<div align="center">
  <p>Prêt à personnaliser les raccourcis clavier, les vues des panneaux et le comportement de l'application ?</p>
  <p><strong><a href="preferences_and_customization.md">Passer au Chapitre 8: Préférences et personnalisation &rarr;</a></strong></p>
</div>
