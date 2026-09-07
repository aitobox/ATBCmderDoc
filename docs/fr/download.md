# Chapitre 10: Téléchargement et installation

Merci de votre intérêt pour ATBCmder ! Nous proposons deux méthodes de téléchargement et d'installation différentes pour répondre à vos besoins. 

> [!IMPORTANT] 
> **Exigences système et architecture** 
> 
> - **Système d'exploitation** : macOS 12.0 (Monterey) ou version ultérieure (y compris macOS 13 Ventura, macOS 14 Sonoma et macOS 15 Sequoia). 
> - **Architecture matérielle prise en charge** : **Apple Silicon (M1 / M2 / M3 / M4, ARM64)**. 
> - **Compatibilité Intel (x86_64)** : les Mac basés sur Intel ne sont **pas pris en charge** pour le moment.

## 1. Mac App Store (recommandé)

Il s'agit de la méthode recommandée pour installer ATBCmder. **ATBCmder est désormais officiellement disponible sur le Mac App Store !** Le téléchargement via le Mac App Store officiel vous garantit des mises à jour automatiques transparentes, une protection native du bac à sable macOS et la meilleure intégration système. 

- **Mac App Store** : [Télécharger ATBCmder sur le Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. Téléchargement du programme d'installation DMG

Si vous ne pouvez pas accéder au Mac App Store ou préférez les téléchargements directs, nous proposons un package d'installation DMG autonome conçu nativement pour Apple Silicon (ARM64). 

- **Lien de téléchargement DMG** : [Cliquez ici pour télécharger ATBCmder DMG](https://storage.aitobox.com/@s/bNAshV6G/ATBCmder) *(Apple Silicon / ARM64 uniquement)* 

*Remarque : lors de l'installation via DMG, les fonctionnalités de sécurité de macOS peuvent nécessiter que vous autorisiez explicitement l'application dans « Paramètres système > Confidentialité et sécurité » la première fois que vous l'ouvrez. Les Mac Intel (x86_64) ne sont pas pris en charge.*

### ⚠️ Accorder l'accès complet au disque

ATBCmder est un outil de gestion de fichiers et nécessite des autorisations explicites de gestion de disque de la part de l'utilisateur. Veuillez suivre ces étapes : 

1. Cliquez sur l'icône Apple dans le coin supérieur gauche de votre écran et sélectionnez **Paramètres système** (ou « Préférences Système » sur les anciennes versions de macOS). 
2. Accédez à **Confidentialité et sécurité** dans le menu de gauche ou de droite. 
3. Faites défiler vers le bas et sélectionnez **Accès complet au disque**. 
4. Recherchez l'application (**ATBCmder**) dans la liste et activez le commutateur pour l'activer. Si l'application ne figure pas dans la liste, cliquez sur le bouton **++** en bas pour l'ajouter manuellement. 
5. Le système vous demandera de saisir votre mot de passe de connexion Mac ou d'utiliser Touch ID pour confirmer les modifications.

## Notes de version

### 1.7.0 (06/09/2026)

- Universal File Viewer et Office Preview Suite : ajout de moteurs de prévisualisation natifs pour les feuilles de calcul Excel (avec chargement virtuel paresseux), les documents Word (avec pagination et rendu d'image intégré) et les présentations PowerPoint (vue de carte diapositive) ; ajout d'aperçus pour les bases de données SQLite, Markdown (avec table des matières), les blocs-notes Jupyter, les polices, les archives, l'audio et EML ; mise en œuvre d'un défilement infini en streaming instantané pour les gros fichiers texte 
- Visionneuse de différences de fichiers côte à côte : outil de comparaison bidirectionnelle de style vimdiff intégré avec mise en évidence des différences au niveau des caractères, copie de morceaux, édition en direct, annulation/rétablissement et préservation de l'encodage 
- Moteur de recherche de fichiers avancé : sous-système de recherche réécrit avec correspondance de sous-chaîne floue par défaut, prise en charge des expressions régulières et mode d'onglet "Alimenter vers la liste" ; La limitation par lots de l'interface utilisateur élimine le gel de l'interface utilisateur sur les résultats de recherche massifs 
- Opérations sur les fichiers et renforcement de l'interface utilisateur : correction des invites d'écrasement en double lors des déplacements entre appareils et des blocages de la file d'attente de transfert ; ajout d'horodatages de création de fichiers dans la boîte de dialogue des propriétés ; barre d'outils centrale verticale activée par défaut et indicateurs visuels raffinés du volet actif

### 1.6.2 (2026-09-03)

- Sélection et interaction par glissement élastique : ajout de la sélection par glissement élastique de la souris dans la vue Table de fichiers et dans la vue Miniatures, ainsi que en cliquant sur un espace vide pour tout désélectionner. 
- Raccourci global de la fenêtre et entrée de raccourci : ajout d'un raccourci clavier global configurable pour afficher/masquer la fenêtre de l'application ; correction des combinaisons de modificateurs à 4 touches saisies dans les paramètres de raccourci clavier 
- Correction de la restauration du Dock et de la barre d'état macOS : résolution d'un problème où le fait de cliquer sur l'icône du Dock alors qu'elle était réduite dans la barre d'état pouvait ne pas restaurer la fenêtre principale ou afficher un cadre vide 
- Améliorations du renforcement et de la stabilité du noyau : correction des erreurs de segmentation potentielles du cycle de vie, renforcement des backends VFS et suppression des threads et suites de tests stabilisées

### 1.6.1 (2026-08-27)

- Refonte complète de l'interface utilisateur/UX de macOS : basé sur Apple HIG avec des palettes claires/foncées raffinées, un contraste de surbrillance du volet de style Finder, des info-bulles de carte natives et des animations de contrôle segmentées fluides 
- Moteur d'icônes vectorielles et widgets modernes : ajout d'un générateur d'icônes vectorielles indépendant de la résolution inspiré des symboles SF et de barres de lecteur, de fils d'Ariane et de zones de liste déroulantes modernisés. 
- Interaction et mise en page améliorée : multi-renommage repensé avec une mise en page à 2 colonnes et une détection de collision de noms en temps réel ; La vue miniature prend en charge le zoom dynamique `Cmd + Wheel` ; vues d'état vides unifiées ajoutées

### 1.6.0 (2026-08-27)

- Pipeline à double distribution : établissement de flux de travail de construction automatisés séparés, adaptés à la distribution DMG autonome et à la version Mac App Store (MAS) 
- Conformité à la politique de l'App Store : ajuste dynamiquement les menus de l'interface utilisateur dans les versions MAS en supprimant les éléments de vérification des mises à jour externes afin de respecter strictement les directives de révision d'Apple, tout en préservant les vérifications manuelles des mises à jour dans les versions DMG. 
- `itms-services` Binary Patcher : ajout d'un scanner binaire automatisé et d'un patcher sécurisé pour éliminer les chaînes de protocole privé dans les artefacts PySide6/Qt compilés, garantissant ainsi une validation automatisée sans faille de l'App Store Connect.

### 1.5.6 (2026-08-22)

- Modes d'affichage indépendants par onglet : chaque onglet conserve désormais sa propre disposition d'affichage indépendante (Vue plate / Mode Arbre), synchronisant automatiquement l'état du menu et persistant de manière transparente lors des restaurations de session. 
- Ouverture intelligente des fichiers et repli du système : ajout d'un détecteur de type de fichier multicouche (octets magiques / MIME / extension) pour ouvrir les médias et les documents pris en charge dans la visionneuse/l'éditeur intégré tout en revenant proprement aux applications par défaut du système d'exploitation pour les fichiers non pris en charge

### 1.5.5 (2026-08-21)

- Optimisation de la politique de vérification des mises à jour : désactivation des vérifications de mise à jour automatiques au démarrage de l'application par défaut ; les mises à jour peuvent désormais être vérifiées manuellement via `Help` -> `Check for Updates...`, améliorant ainsi la vitesse de lancement et la confidentialité hors ligne

### 1.5.4 (2026-08-21)

- Mise au point et sélection du panneau : correction des contours de mise au point persistants sur les panneaux divisés inactifs lors du changement de volet ; logique de réinitialisation de sélection améliorée après le déplacement de fichiers entre les panneaux pour éviter les opérations accidentelles

### 1.5.3 (2026-08-19)

- Polissage des sous-menus en cascade du fil d'Ariane : alignement précis de la position verticale des menus de sous-dossiers en cascade avec la ligne en surbrillance, éliminant ainsi les sauts de mise en page et lissant la traversée profonde des dossiers

### 1.5.2 (2026-08-19)

- Correction des notes de démarrage et de version : correction d'un problème où la boîte de dialogue Notes de version apparaissait à plusieurs reprises à chaque démarrage d'application ; gestion de secours par défaut améliorée de `Config.get` pour garantir que les notes de version ne s'affichent qu'au lancement initial ou lors des mises à niveau de version

### 1.5.1 (2026-08-19)

- Notes de version multilingues : ajout de 7 nouvelles notes de version dans les langues grand public (zh_TW, ja, ko, de, fr, ru, es) avec découverte dynamique et repli hiérarchique à 5 niveaux 
- macOS Code Signing & Build Polish : scripts d'empaquetage refactorisés avec ciblage binaire Mach-O et wrappers de nouvelle tentative d'horodatage, éliminant les échecs de signature et la limitation

### 1.5.0 (2026-08-17)

- Global Session Manager : implémentation de la persistance de session au niveau de l'application qui restaure de manière transparente tous les onglets du panneau gauche/droite, les chemins, les modes d'affichage (Plat/Arbre), les ratios de panneau et les limites des fenêtres multi-moniteurs au redémarrage 
- Importation/Exportation de paramètres : ajout de l'exportation et de l'importation ZIP en 1 clic pour toutes les configurations et données d'application, rationalisant ainsi la migration entre appareils 
- Améliorations de l'éditeur d'images : ajout d'un redimensionnement d'image personnalisé avec verrouillage des proportions et résolutions prédéfinies rapides

### 1.4.9 (2026-08-17)

- Éditeur d'images avancé : ajout d'un recadrage d'image, d'une rotation fine, d'ajustements de filtre et d'un module de suppression et d'inpainting de filigrane AI alimenté par OpenCV. 
- Visionneuse d'images améliorée : prise en charge complète des GIF animés, du zoom, du panoramique, de la rotation, de l'extraction des métadonnées EXIF et du mode diaporama 
- Intégration de la recherche Spotlight : Spotlight natif macOS profondément intégré pour une recherche instantanée de fichiers et une navigation améliorée dans les résultats de recherche

### 1.4.8 (2026-08-16)

- Localisation complète (i18n) : audit complet et traduction complète dans l'interface utilisateur, F3 Viewer et F4 Editor, améliorant considérablement la localisation des lecteurs multimédias et des composants de prévisualisation 
- Optimisations de la visionneuse F3 : amélioration de la gestion des liens externes et de la logique de recherche dans le lecteur EPUB de secours (SimpleEpubPanel) ; rationalisation de la barre d'outils de la visionneuse PDF en supprimant les boutons de rotation redondants

### 1.4.7 (2026-08-16)

- Améliorations du lecteur multimédia : interface utilisateur, UX et stabilité des lecteurs audio et vidéo intégrés considérablement améliorés 
- Refactorisation du système de construction : renommé l'indicateur d'environnement `BUILD_EPUB` en `BUILD_WEBENGINE` pour refléter avec précision le comportement de l'empaquetage 
- Correction des dépendances d'empaquetage : garantie que `ebooklib` est toujours intégré dans des versions DMG légères pour le lecteur EPUB de secours

### 1.4.6 (2026-08-16)

- Lecteur EPUB léger (SimpleEpubPanel) : ajout d'un lecteur EPUB de secours sans WebEngine avec navigation et recherche de chapitre, ainsi qu'un argument CLI `--epub-reader` pour remplacer le moteur par défaut 
- Menus de fil d'Ariane en cascade : refactorisation du fil d'Ariane en une disposition déroulante sur une seule colonne avec des sous-menus en cascade infinis, corrigeant les problèmes de chevauchement et de verrouillage de la souris.

### 1.4.5 (2026-08-15)

- Visionneuse de code avancée (F3) : ajout de la coloration syntaxique (Pygments), de la fin des fichiers en direct, de la recherche d'expressions régulières et des numéros de ligne 
- Éditeur de code avancé (F4) : ajout d'un encodage dynamique/conversion EOL, d'une sauvegarde atomique sécurisée, d'une indentation intelligente et d'une recherche/remplacement 
- Glisser-déposer externe global : faites glisser en toute transparence des fichiers, y compris des contenus d'archives profondément imbriqués, directement vers le bureau macOS ou des éditeurs tiers (par exemple VSCode)

### 1.4.4 (2026-08-15)

- Améliorations de la typographie : augmentation de la taille des polices dans les menus, les boutons, les info-bulles et la boîte de dialogue des paramètres pour une meilleure lisibilité 
- Corrections du curseur de redimensionnement : restauration des curseurs de redimensionnement de la souris manquants sur les bords des fenêtres, les séparateurs et les en-têtes de colonnes du tableau. 
- Corrections de l'interface utilisateur macOS : résolution des arrière-plans de sélection noirs dans les menus déroulants et des débordements de titres dans les zones de groupe.

### 1.4.3 (2026-08-14)

- Nouvelle interface utilisateur native macOS (thème Aqua Blue) : introduit comme nouveau thème par défaut, avec navigation interactive dans le fil d'Ariane (avec exploration des sous-dossiers en cascade), compteur de stockage de style Mac (débordement de To fixe) et sélection de capsules arrondies 
- Perfectionnement approfondi de l'interface utilisateur : disposition raffinée du bouton de fermeture des onglets, chevauchement fixe des invites de commande et arrière-plans, séparateurs et bordures de panneaux unifiés pour tous les thèmes 
- Mise à niveau i18n et application : audit complet de la couverture du projet i18n ; ajout du support de l'API de partage AList/OpenList dans le module de mise à jour automatique

### 1.4.2 (2026-08-13)

- Filtre sémantique AI amélioré : prise en charge de l'analyse des extensions plus courantes, des formes plurielles et entièrement intégré à i18n 
- Semantic Search UX : remplacement du curseur d'attente par QProgressBar et amélioration du comportement de la touche Entrée pour les achèvements 
- Analyse sémantique de base : détection améliorée du type de cible et suppression de mots clés pour une recherche en langage naturel plus précise

### 1.4.1 (2026-08-13)

- Révision et refactorisation complètes de la base de code (Batchs A-D) 
- Améliorations de la sécurité : correction des vulnérabilités potentielles de traversée de chemin et d'accès 
- Concurrence et performances : amélioration de la sécurité des threads d'arrière-plan et de l'efficacité d'exécution 
- Architecture : stabilité améliorée et gestion des ressources dans les composants principaux

### 1.4.0 (2026-08-12)

- Correctifs réseau Deep VFS : prise en charge du multi-encodage, pilotes de protocole, montage d'archives en chaîne et résolution de conflits 
- Module de mise à niveau de l'application amélioré : correctifs de vérification SSL, validation de téléchargement DMG et intégration de l'interface utilisateur 
- Interface utilisateur des notes de version : affiche l'historique complet des versions lors des mises à jour automatiques

### 1.3.9 (2026-08-12)

- Ajout d'un lecteur EPUB intégré (vue rapide F3) 
- Implémentation d'un mécanisme de détection de mise à niveau d'application 
- Correction du blocage du travailleur VFS lors de la résolution des conflits de fichiers

### 1.3.8 (2026-08-08)

- Affinement de l'interface utilisateur de l'arborescence 
- Intégration réseau fsspec refactorisée 
- Amélioration de la gestion des caractères de fichier invalides

### 1.3.7 (2026-08-06)

- Architecture réseau VFS : révision des systèmes de fichiers réseau (FTP/WebDAV/SMB) à l'aide de `fsspec`, implémentation asynchrone `VfsTableModel`, streaming `StreamCopyWorker`, opérations de fichiers à distance (mkdir/renommer/supprimer/écraser) et visualisation/édition à distance F3/F4. 
- Barre d'état système et raccourcis clavier : prise en charge de la réduction dans la barre d'état système, raccourci global (`Option+Cmd+H`), bascule d'icône du Dock macOS et intégration d'icône de modèle natif 
- Configuration LLM : introduire la ressource `default_llm.xml` et le singleton pour le filtrage sémantique de l'IA et les options de l'interface utilisateur 
- Améliorations de la navigation : prise en charge des raccourcis de navigation PageUp / PageDown / Home / End / Fn dans les panneaux de fichiers et les fenêtres contextuelles de liste de véhicules recherchés 
- Internationalisation : enveloppez tous les messages d'erreur VFS, les étiquettes du panneau Quick View et les chaînes de menu de la barre d'état avec les catalogues de traduction i18n

### 1.3.6 (2026-08-04)

- Améliorations du réseau VFS : ajout de la détection automatique UTF-8/GBK, mise à jour de l'encodage dynamique du makefile, gestion de secours et réinitialisation du socket pour FTP ; résoudre le délai d'attente et la désynchronisation des réponses 
- Corrections WebDAV et SMB : correction de la suppression du chemin racine WebDAV/SMB, de la propagation de la dernière erreur, de la fiabilité de la connexion, des icônes VFS et de l'affichage des titres des onglets 
- Navigation par vignettes : implémentez une navigation fluide par flèches de grille 2D pour la vue par vignettes 
- i18n & Code Quality : correction des traductions corrompues de Close Tab dans les catalogues zh_CN/zh_TW et audit complet d'optimisation de la base de code

### 1.3.5 (2026-08-03)

- Panneau d'affichage rapide : implémentation de la fonctionnalité d'affichage rapide (`cm_QuickView`, `Cmd+Q`/`Ctrl+Q`) prenant en charge les aperçus multiformats, les propriétés de fichier de secours, le retournement symétrique, l'intégration du menu Afficher et l'i18n complet 
- Widgets d'affichage rapide : ajoutez `QuickViewContainer` et `QuickViewPropertiesWidget` intégrés dans FilePanel 
- UI Polish : correction de l'alignement de l'en-tête des onglets et des problèmes d'écrasement de la page de dialogue d'options dans le thème clair

### 1.3.4 (2026-08-02)

- Interface utilisateur du panneau de fichiers : ajoutez la sélection par lots Shift+PageUp / Shift+PageDown dans les vues du panneau de fichiers 
- Opérations sur les fichiers : correction des défauts de copie F5 et de déplacement de fichier/répertoire F6 
- Créer des scripts : définissez les noms d'identité exacts des certificats, ajoutez un horodatage à la conception du code et gérez le statut invalide de la notarisation avec élégance

### 1.3.3 (2026-08-01)

- Transfer Engine : calculez avec précision la vitesse de transfert en temps réel et l'ETA dans ProcessTransferWorker 
- Autorisations et bac à sable : contrôles distincts du bac à sable macOS du flux de détection de l'accès complet au disque 
- Scripts de build : mise à jour de la configuration du script de build pour les builds signés 1.3.3 DMG

### 1.3.2 (2026-08-01)

- Subprocess Transfer Worker : correction d'un échec de gel/démarrage sous le mode bundle App Store autonome de Nuitka 
- Compétences d'agent : ajoutez le contrôle d'audit d'exhaustivité i18n à la compétence d'audit de révision de code et d'optimisation.

### 1.3.1 (2026-08-01)

- macOS Sandbox : correction du faux état "Accès complet au disque accordé" provoqué par la vérification `os.access` 
- Tâches simultanées : résoudre les interférences d'état pour les opérations en arrière-plan simultanées 
- i18n : ajouter la traduction chinoise pour la case à cocher par lots dans la boîte de dialogue de suppression permanente 
- Compétences d'agent : ajouter et mettre à jour la compétence d'audit d'optimisation de révision de code

### 1.3.0 (01/08/2026)

- Moteur de transfert isolé par processus : implémentez ProcessTransferWorker et ProcessIOEngine pour décharger la copie de fichiers/déplacer les E/S du thread de l'interface utilisateur 
- Performances de transfert et réactivité : limitation du débit IPC à 10 Hz, mise en mémoire tampon adaptative et optimisation macOS `F_NOCACHE` pour éviter le bégaiement de l'interface graphique 
- Audit et renforcement du code : refactorisation en 4 phases incluant les verrous mutex de concurrence, le renforcement de la sécurité et le nettoyage de l'architecture 
- Corrections de l'interface utilisateur : correction de l'erreur de suppression Shiboken C++, de la disposition du mode panneau horizontal et des signaux d'indicateur de progression des tâches en arrière-plan

### 1.2.0 (2026-07-30)

- Implémenter un pool de processus d'E/S global (IoWorkerPool) pour isoler les opérations d'E/S de fichiers bloquantes et empêcher le gel de l'interface graphique. 
- Gestion des versions de configuration : lecture/écriture de la version app_version sur le nœud racine XML et ajout d'un registre d'exécution de migration automatisé 
- Glisser-déposer / Presse-papiers : intégrez le pont natif macOS Finder, les dossiers chargés à ressort et la machine à états du presse-papiers 
- Extension du chemin : ajout de l'utilitaire partagé `expand_path` prenant en charge `~`, `$VAR`, `%VAR%` et `%COMMANDER_PATH%` 
- Hotlist : implémentez la configuration autonome du singleton HotlistConfig et de la liste de véhicules recherchés par défaut

### 1.1.0 (2026-07-29)

- Correction de l'ordre d'entrée des notes de version pour garantir un tri chronologique inversé sous l'en-tête de la note de version. 
- Correction du script du gestionnaire de versions pour prendre en charge le nœud XML System/LastVersion dans default_config.xml 
- Raccourcis clavier clavier : ajoutez les raccourcis par défaut Meta+Tab et Meta+Shift+Tab pour la navigation par onglets 
- Onglets favoris : ajoutez la migration automatique et le nettoyage des anciens onglets favoris de la configuration principale 
- Visionneuse de fichiers : optimisez les performances de chargement de fichiers volumineux et l'utilisation de la mémoire

### 1.0.1 (2026-07-22)

> Correction de l'échec de l'aperçu du texte F3 dans les environnements sandbox de l'App Store

### 1.0.0 (2026-07-18)

> Implémentation initiale du portage Python de TotalCommander.