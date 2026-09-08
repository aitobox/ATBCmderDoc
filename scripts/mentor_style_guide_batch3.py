#!/usr/bin/env python3
"""
scripts/mentor_style_guide_batch3.py
Localized ASCII diagrams and mentor terminology for Batch 3:
- keyboard_shortcuts.md
- network_and_vfs.md
- preferences_and_customization.md
"""

from typing import Dict

# 1. keyboard_shortcuts.md Block 0: Dual-Matrix Engine
ASCII_KEYBOARD_ENGINE: Dict[str, str] = {
    "en": """┌─────────────────────────────────────────────────────────────────────────────┐
│                      DUAL-MATRIX KEYBOARD ENGINE                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  CLASSIC COMMANDER PARADIGM          │  NATIVE macOS PARADIGM               │
│  • Function Key Centric (F1–F12)     │  • Modifier Chords (⌘, ⌥, ⇧, ⌃)      │
│  • Dedicated Keypad Marking (+, -, *)│  • Finder Parity (⌘C, ⌘V, ⌘⌫, ⏎)     │
│  • Zero-Modal Terminal Velocity      │  • Native Menu Bar Integration       │
│  Examples:                           │  Examples:                           │
│    F5        ➔ Copy Files            │    ⌘C ➔ ⌘V   ➔ Copy Files            │
│    F6        ➔ Move Files            │    ⌘C ➔ ⌥⌘V  ➔ Move Files            │
│    Shift+F4  ➔ Create Text File      │    ⇧⌘4       ➔ Create Text File      │
│    Alt+F7    ➔ Find Files            │    ⌥⌘F       ➔ Find Files            │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────────────────────┐
│                          双矩阵快捷键引擎架构                               │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  经典 COMMANDER 体系 (PC/经典习惯)     │  macOS 原生体系 (Mac 标准人机工学) │
│  • 以功能键为核心 (F1–F12)            │  • 以修饰组合键为核心 (⌘, ⌥, ⇧, ⌃)  │
│  • 专用小键盘标记快捷键 (+, -, *)    │  • 与 Finder 深度一致 (⌘C, ⌘V, ⌘⌫, ⏎)│
│  • 盲操盲打、极速响应                │  • 深度集成原生菜单栏加速键          │
│  典型示例：                          │  典型示例：                          │
│    F5        ➔ 复制文件到对侧        │    ⌘C ➔ ⌘V   ➔ 复制文件              │
│    F6        ➔ 移动文件到对侧        │    ⌘C ➔ ⌥⌘V  ➔ 剪切移动文件          │
│    Shift+F4  ➔ 快速新建文本文件      │    ⇧⌘4       ➔ 快速新建文本文件      │
│    Alt+F7    ➔ 高级文件搜索          │    ⌥⌘F       ➔ 高级文件搜索          │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────────────────────┐
│                          雙矩陣快捷鍵引擎架構                               │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  經典 COMMANDER 體系 (PC/經典習慣)   │  macOS 原生體系 (Mac 標準人體工學)   │
│  • 以功能鍵為核心 (F1–F12)            │  • 以組合鍵為核心 (⌘, ⌥, ⇧, ⌃)      │
│  • 專用鍵盤標記鍵 (+, -, *)          │  • 與 Finder 深度一致 (⌘C, ⌘V, ⌘⌫, ⏎)│
│  • 盲打盲操、極速響應                │  • 深度整合原生選單列加速鍵          │
│  典型範例：                          │  典型範例：                          │
│    F5        ➔ 複製檔案到對側        │    ⌘C ➔ ⌘V   ➔ 複製檔案              │
│    F6        ➔ 移動檔案到對側        │    ⌘C ➔ ⌥⌘V  ➔ 剪下移動檔案          │
│    Shift+F4  ➔ 快速新增文字檔        │    ⇧⌘4       ➔ 快速新增文字檔        │
│    Alt+F7    ➔ 進階檔案搜尋          │    ⌥⌘F       ➔ 進階檔案搜尋          │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────────────────────┐
│                       デュアルマトリックス キーボード構造                   │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  クラシック Commander 体系           │  macOS ネイティブ体系                │
│  • ファンクションキー中心 (F1–F12)   │  • 修飾キーコンビネーション(⌘, ⌥, ⇧, ⌃)│
│  • テンキー記号による範囲選択(+, -, *)│ • Finder互換操作 (⌘C, ⌘V, ⌘⌫, ⏎)    │
│  • 指先が跳ねるブラインド操作        │  • ネイティブメニューバー連携        │
│  操作例:                             │  操作例:                             │
│    F5        ➔ 対側へコピー          │    ⌘C ➔ ⌘V   ➔ ファイルをコピー      │
│    F6        ➔ 対側へ移動            │    ⌘C ➔ ⌥⌘V  ➔ ファイルを移動        │
│    Shift+F4  ➔ 新規テキスト作成      │    ⇧⌘4       ➔ 新規テキスト作成      │
│    Alt+F7    ➔ ファイル高度検索      │    ⌥⌘F       ➔ ファイル高度検索      │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────────────────────┐
│                    DUAL-MATRIX-TASTATUR-ARCHITEKTUR                         │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  KLASSISCHES COMMANDER-PARADIGMA     │  NATIVES macOS-PARADIGMA             │
│  • Fokus auf Funktionstasten (F1–F12)│  • Modifier-Kombinationen (⌘, ⌥, ⇧, ⌃)│
│  • Tastenfeld-Markierung (+, -, *)   │  • Finder-Parität (⌘C, ⌘V, ⌘⌫, ⏎)    │
│  • Höchste Tastatur-Geschwindigkeit  │  • Native Menüleisten-Integration    │
│  Beispiele:                          │  Beispiele:                          │
│    F5        ➔ Dateien kopieren      │    ⌘C ➔ ⌘V   ➔ Dateien kopieren      │
│    F6        ➔ Dateien bewegen       │    ⌘C ➔ ⌥⌘V  ➔ Dateien bewegen       │
│    Shift+F4  ➔ Textdatei anlegen     │    ⇧⌘4       ➔ Textdatei anlegen     │
│    Alt+F7    ➔ Dateien suchen        │    ⌥⌘F       ➔ Dateien suchen        │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────────────────────┐
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
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE TECLADO DE DOBLE MATRIZ                  │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  PARADIGMA CLÁSICO COMMANDER         │  PARADIGMA NATIVO DE MACOS           │
│  • Teclas de función (F1–F12)        │  • Teclas modificadoras (⌘, ⌥, ⇧, ⌃) │
│  • Marcado numérico (+, -, *)        │  • Paridad con Finder (⌘C, ⌘V, ⌘⌫, ⏎)│
│  • Máxima velocidad táctil           │  • Integración con la barra de menús │
│  Ejemplos:                           │  Ejemplos:                           │
│    F5        ➔ Copiar archivos       │    ⌘C ➔ ⌘V   ➔ Copiar archivos       │
│    F6        ➔ Mover archivos        │    ⌘C ➔ ⌥⌘V  ➔ Mover archivos        │
│    Shift+F4  ➔ Crear archivo de texto│    ⇧⌘4       ➔ Crear archivo de texto│
│    Alt+F7    ➔ Buscar archivos       │    ⌥⌘F       ➔ Buscar archivos       │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITETURA DE TECLADO EM MATRIZ DUPLA                   │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  PARADIGMA CLÁSSICO COMMANDER        │  PARADIGMA NATIVO DO MACOS           │
│  • Teclas de função (F1–F12)         │  • Teclas modificadoras (⌘, ⌥, ⇧, ⌃) │
│  • Marcação numérica (+, -, *)       │  • Paridade com o Finder (⌘C, ⌘V, ⌘⌫)│
│  • Máxima agilidade de digitação     │  • Integração com a barra de menus   │
│  Exemplos:                           │  Exemplos:                           │
│    F5        ➔ Copiar arquivos       │    ⌘C ➔ ⌘V   ➔ Copiar arquivos       │
│    F6        ➔ Mover arquivos        │    ⌘C ➔ ⌥⌘V  ➔ Mover arquivos        │
│    Shift+F4  ➔ Criar arquivo de texto│    ⇧⌘4       ➔ Criar arquivo de texto│
│    Alt+F7    ➔ Buscar arquivos       │    ⌥⌘F       ➔ Buscar arquivos       │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────────────────────┐
│                         듀얼 매트릭스 단축키 구조                           │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  클래식 COMMANDER 패러다임           │  macOS 네이티브 패러다임             │
│  • 기능 키 중심 워크플로우 (F1–F12)  │  • 조합 수식 키 중심 (⌘, ⌥, ⇧, ⌃)    │
│  • 전용 키패드 파일 마킹 (+, -, *)   │  • Finder 단축키 완전 호환 (⌘C, ⌘V)  │
│  • 손끝에서 끝나는 초고속 조작       │  • 네이티브 시스템 메뉴 바 통합      │
│  주요 예시:                          │  주요 예시:                          │
│    F5        ➔ 대상 패널로 복사      │    ⌘C ➔ ⌘V   ➔ 파일 복사             │
│    F6        ➔ 대상 패널로 이동      │    ⌘C ➔ ⌥⌘V  ➔ 파일 이동             │
│    Shift+F4  ➔ 새 텍스트 파일 생성   │    ⇧⌘4       ➔ 새 텍스트 파일 생성   │
│    Alt+F7    ➔ 고급 파일 검색        │    ⌥⌘F       ➔ 고급 파일 검색        │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────────────────────┐
│                  ДВУХМАТРИЧНАЯ СИСТЕМА ГОРЯЧИХ КЛАВИШ                       │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  КЛАССИЧЕСКИЙ COMMANDER              │  СТАНДАРТ MACOS                      │
│  • Функциональные клавиши (F1–F12)   │  • Клавиши модификаторы (⌘, ⌥, ⇧, ⌃) │
│  • Выделение на цифровом блоке (+, -)│  • Совместимость с Finder (⌘C, ⌘V, ⏎)│
│  • Мгновенная слепая работа          │  • Интеграция с системным меню macOS │
│  Примеры:                            │  Примеры:                            │
│    F5        ➔ Копировать файлы      │    ⌘C ➔ ⌘V   ➔ Копировать файлы      │
│    F6        ➔ Переместить файлы     │    ⌘C ➔ ⌥⌘V  ➔ Переместить файлы     │
│    Shift+F4  ➔ Создать текстовый файл│    ⇧⌘4       ➔ Создать текстовый файл│
│    Alt+F7    ➔ Поиск файлов          │    ⌥⌘F       ➔ Поиск файлов          │
└──────────────────────────────────────┴──────────────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────────────────────┐
│                  ARCHITETTURA TASTIERA A DOPPIA MATRICE                     │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  PARADIGMA CLASSICO COMMANDER        │  PARADIGMA NATIVO MACOS              │
│  • Tasti funzione al centro (F1–F12) │  • Modificatori di sistema (⌘, ⌥, ⇧) │
│  • Selezione tastierino (+, -, *)    │  • Piena parità con Finder (⌘C, ⌘V)  │
│  • Controllo rapido da tastiera      │  • Integrazione barra dei menu       │
│  Esempi:                             │  Esempi:                             │
│    F5        ➔ Copia file            │    ⌘C ➔ ⌘V   ➔ Copia file            │
│    F6        ➔ Sposta file           │    ⌘C ➔ ⌥⌘V  ➔ Sposta file           │
│    Shift+F4  ➔ Crea file di testo    │    ⇧⌘4       ➔ Crea file di testo    │
│    Alt+F7    ➔ Cerca file            │    ⌥⌘F       ➔ Cerca file            │
└──────────────────────────────────────┴──────────────────────────────────────┘"""
}

# 2. keyboard_shortcuts.md Block 1: Context Scopes
ASCII_KEYBOARD_SCOPES: Dict[str, str] = {
    "en": """┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION SCOPE: Main                            │
│  Global commands, panel navigation, window management, toolbar, power tools │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PANEL SCOPE: FilePanel       │  MODAL TOOLS SCOPES                         │
│  Active during directory      │  • Viewer      (Lister preview window)      │
│  table and thumbnail browsing │  • Editor      (Built-in code editor)       │
│  (marking, range selection,   │  • Differ      (Side-by-side diff viewer)   │
│  inline editing, space count) │  • FindFiles   (Multi-threaded file search) │
│                               │  • MultiRename (Batch rename engine)        │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────────────────────┐
│                          全局主作用域 (Main Scope)                          │
│  通用命令、双面板跳转、标签页切换、工具栏、系统级自动化工具                 │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  文件面板作用域 (FilePanel)   │  专用模态工具作用域 (Modal Tools)           │
│  在目录列表与缩略图浏览时生效 │  • Viewer      (全能查看器 Lister 窗口)     │
│  (文件多选、通配符标记、行内  │  • Editor      (内置代码/文本编辑器)         │
│  快速重命名、目录容量统计)    │  • Differ      (双栏文件差异对比窗口)        │
│                               │  • FindFiles   (多线程高级文件搜索对话框)    │
│                               │  • MultiRename (多重批量重命名工具)          │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────────────────────┐
│                          全域主作用域 (Main Scope)                          │
│  通用命令、雙面板跳轉、分頁切換、工具列、系統級自動化工具                   │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  檔案面板作用域 (FilePanel)   │  專用強制回應工具作用域 (Modal Tools)       │
│  在目錄清單與縮圖瀏覽時生效   │  • Viewer      (全能檢視器 Lister 視窗)     │
│  (檔案多選、萬用字元標記、行內│  • Editor      (內建程式碼/文字編輯器)       │
│  快速重新命名、目錄容量統計)  │  • Differ      (雙欄檔案差異比對視窗)        │
│                               │  • FindFiles   (多執行緒進階檔案搜尋對話方塊)│
│                               │  • MultiRename (多重批次重新命名工具)        │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────────────────────┐
│                          アプリケーション全体スコープ (Main)                │
│  グローバルコマンド、パネル移動、タブ切替、ツールバー、パワー機能           │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  ファイルパネルスコープ       │  専用ツールスコープ (Modal Tools)           │
│  リスト・サムネイル一覧操作時 │  • Viewer      (Universal Lister プレビュー)│
│  (ファイル選択、ワイルドカード│  • Editor      (内蔵コードエディタ)         │
│  インラインリネーム、容量計算)│  • Differ      (2画面差分比較ツール)        │
│                               │  • FindFiles   (高度なファイル検索)         │
│                               │  • MultiRename (一括リネームツール)         │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────────────────────┐
│                      ANWENDUNGS-GÜLTIGKEITSBEREICH: Main                    │
│  Globale Befehle, Panel-Navigation, Tabs, Symbolleiste, Power-Tools         │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PANEL-BEREICH: FilePanel     │  MODALE WERKZEUGBEREICHE                    │
│  Aktiv bei Verzeichnis- und   │  • Viewer      (Lister-Vorschaufenster)     │
│  Miniaturansichten (Auswahl,  │  • Editor      (Integrierter Code-Editor)   │
│  Platzhalter, Direktumbenenn.,│  • Differ      (Differenz-Vergleich)        │
│  Größenberechnung)            │  • FindFiles   (Erweiterte Dateisuche)      │
│                               │  • MultiRename (Mehrfach-Umbenennung)       │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────────────────────┐
│                        PORTÉE APPLICATION : Main                            │
│  Commandes globales, navigation panneaux, onglets, barre d'outils           │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PORTÉE PANNEAU : FilePanel   │  PORTÉES OUTILS MODAUX                      │
│  Actif dans les listes et     │  • Viewer      (Fenêtre Universal Lister)   │
│  miniatures (sélection,       │  • Editor      (Éditeur de code intégré)    │
│  marquage, renommage direct,  │  • Differ      (Comparateur de fichiers)    │
│  calcul de taille)            │  • FindFiles   (Recherche avancée)          │
│                               │  • MultiRename (Renommage par lot)          │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────────────────────┐
│                        ÁMBITO DE APLICACIÓN: Main                           │
│  Comandos globales, navegación entre paneles, pestañas, barra de herramientas│
├───────────────────────────────┬─────────────────────────────────────────────┤
│  ÁMBITO PANEL: FilePanel      │  ÁMBITOS DE HERRAMIENTAS MODALES            │
│  Activo en la tabla de        │  • Viewer      (Ventana del visor Lister)   │
│  archivos y miniaturas        │  • Editor      (Editor de código integrado) │
│  (selección, comodines,       │  • Differ      (Comparador de diferencias)  │
│  renombrado directo, tamaño)  │  • FindFiles   (Búsqueda avanzada)          │
│                               │  • MultiRename (Renombrado masivo)          │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────────────────────┐
│                        ESCOPO DA APLICAÇÃO: Main                            │
│  Comandos globais, navegação entre painéis, abas, barra de ferramentas      │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  ESCOPO PAINEL: FilePanel     │  ESCOPOS DE FERRAMENTAS MODAIS              │
│  Ativo na navegação de        │  • Viewer      (Janela Universal Lister)    │
│  diretórios e miniaturas      │  • Editor      (Editor de código integrado) │
│  (seleção, máscaras,          │  • Differ      (Comparador de arquivos Diff)│
│  renomeação direta, tamanho)  │  • FindFiles   (Busca avançada de arquivos) │
│                               │  • MultiRename (Renomeação em lote)         │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────────────────────┐
│                         애플리케이션 전역 범위: Main                        │
│  전역 명령, 패널 전환, 탭 탐색, 도구 모음, 파워 툴                          │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  패널 유효 범위: FilePanel    │  모달 도구 유효 범위                        │
│  디렉터리 목록 및 썸네일 탐색 │  • Viewer      (Universal Lister 뷰어 창)   │
│  (다중 선택, 와일드카드 마킹, │  • Editor      (내장 코드/텍스트 에디터)    │
│  인라인 이름 변경, 용량 계산) │  • Differ      (나란히 파일 차이 비교 창)   │
│                               │  • FindFiles   (다중 스레드 파일 검색 창)   │
│                               │  • MultiRename (일괄 이름 변경 도구)        │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────────────────────┐
│                     ГЛОБАЛЬНАЯ ОБЛАСТЬ ПРИЛОЖЕНИЯ: Main                     │
│  Общие команды, навигация по панелям, вкладки, панель инструментов, утилиты │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  ОБЛАСТЬ ПАНЕЛИ: FilePanel    │  ОБЛАСТИ МОДАЛЬНЫХ ИНСТРУМЕНТОВ             │
│  Действует в списке файлов и  │  • Viewer      (Просмотр Universal Lister)  │
│  эскизах (выделение, маски,   │  • Editor      (Встроенный редактор кода)   │
│  быстрое переименование,      │  • Differ      (Сравнение файлов Diff)      │
│  подсчет размера)             │  • FindFiles   (Многопоточный поиск файлов) │
│                               │  • MultiRename (Пакетное переименование)    │
└───────────────────────────────┴─────────────────────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────────────────────┐
│                       AMBITO APPLICAZIONE: Main                             │
│  Comandi globali, navigazione pannelli, schede, barra strumenti, strumenti  │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  AMBITO PANNELLO: FilePanel   │  AMBITI STRUMENTI MODALI                    │
│  Attivo durante l'esplorazione│  • Viewer      (Finestra Universal Lister)  │
│  di tabelle file e miniature  │  • Editor      (Editor di codice integrato) │
│  (selezione, filtri,          │  • Differ      (Confronto file affiancato)  │
│  rinomina diretta, calcolo)   │  • FindFiles   (Ricerca avanzata file)      │
│                               │  • MultiRename (Ridenominazione in blocco)  │
└───────────────────────────────┴─────────────────────────────────────────────┘"""
}
