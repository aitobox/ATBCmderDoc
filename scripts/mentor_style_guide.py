#!/usr/bin/env python3
"""
scripts/mentor_style_guide.py
Defines the Mentor-Style guidelines, macOS official localization dictionaries,
and beautifully aligned ASCII diagrams across all 10 supported non-English languages.
"""

from typing import Dict

# Alert token canonical map to ensure Material callouts always render properly
ALERT_CANONICAL_MAP = {
    # TIP
    'ヒント': 'TIP', '팁': 'TIP', 'ASTUCE': 'TIP', 'CONSEJO': 'TIP', 'DICA': 'TIP', 'TIPP': 'TIP', 'СОВЕТ': 'TIP', 'CONSIGLIO': 'TIP',
    # NOTE
    'ノート': 'NOTE', '참고': 'NOTE', 'NOTA': 'NOTE', 'HINWEIS': 'NOTE', 'ПРИМЕЧАНИЕ': 'NOTE',
    # IMPORTANT
    '重要': 'IMPORTANT', '중요': 'IMPORTANT', 'IMPORTANTE': 'IMPORTANT', 'WICHTIG': 'IMPORTANT', 'ВАЖНО': 'IMPORTANT',
    # WARNING
    '警告': 'WARNING', '경고': 'WARNING', 'AVERTISSEMENT': 'WARNING', 'ADVERTENCIA': 'WARNING', 'AVISO': 'WARNING', 'WARNUNG': 'WARNING', 'ПРЕДУПРЕЖДЕНИЕ': 'WARNING', 'ATTENZIONE': 'WARNING',
    # CAUTION
    '注意': 'CAUTION', '주의': 'CAUTION', 'ATTENTION': 'CAUTION', 'PRECAUCIÓN': 'CAUTION', 'PRECAUCION': 'CAUTION', 'CUIDADO': 'CAUTION', 'ACHTUNG': 'CAUTION', 'ОСТОРОЖНО': 'CAUTION'
}

## Machine translation blacklist & native mentor terminology mappings per language
TERMINOLOGY_REPLACEMENTS: Dict[str, Dict[str, str]] = {
    "ja": {
        "一定の向き": "常に迷わない操作視界",
        "キーボードのベロシティ": "指先が跳ねるようなキーボード操作",
        "トータル コマンダー": "Total Commander",
        "ダブル コマンダー": "Double Commander",
        "ノートン コマンダー": "Norton Commander",
        "ビジュアル インターフェイス ツアーとランドマーク": "インターフェースツアーと各部名称",
        "ドラッグ アンド ドロップの推測は必要ありません": "マウスで恐る恐るドラッグ＆ドロップする必要はありません",
        "アクティブ (ソース) モデルと非アクティブ (ターゲット) モデル": "アクティブ（操作元）と非アクティブ（操作先）パネルの役割",
        "方向性のある操作: 常にソース ➔ ターゲット": "操作の黄金ルール：常に「操作元」から「操作先」へ",
    },
    "de": {
        "Ständige Orientierung": "Klare Orientierung auf einen Blick",
        "Konstante Ausrichtung": "Klare Orientierung auf einen Blick",
        "Tastaturgeschwindigkeit": "Flüssiger Tastatur-Flow",
        "Visuelle Benutzeroberflächentour und Orientierungspunkte": "Benutzeroberfläche und Funktionsbereiche im Überblick",
        "Visuelle Interface-Tour und Sehenswürdigkeiten": "Benutzeroberfläche und Funktionsbereiche im Überblick",
        "Sehenswürdigkeiten": "Funktionsbereiche",
        "organisiert die Stromversorgung": "vereint maximale Produktivität und Kontrolle",
        "Kein Rätselraten beim Drag-and-Drop": "Schluss mit zittrigem Drag & Drop",
        "Direktionale Operationen: Immer Quelle ➔ Ziel": "Die goldene Regel: Immer von der Quelle zum Ziel",
    },
    "zh-hant": {
        "Finder 訪達": "Finder",
        "訪達": "Finder",
        "拖拽": "拖曳",
        "標籤頁": "分頁",
        "默認": "預設",
        "快捷鍵": "快速鍵",
        "偏好設置": "偏好設定",
        "終端": "終端機",
        "回收站": "垃圾桶",
    },
    "fr": {
        "Orientation constante": "Une vision claire et permanente",
        "Vélocité du clavier": "Fluidité et rapidité absolue au clavier",
        "Visite guidée de l'interface visuelle et points de repère": "Visite guidée de l'interface et zones clés",
        "Visite de l'interface visuelle et monuments": "Visite guidée de l'interface et zones clés",
        "organise l'alimentation": "organise la puissance et la productivité",
        "Fini les incertitudes du glisser-déposer": "Oubliez la corvée du glisser-déposer",
        "Opérations directionnelles : toujours Source ➔ Cible": "La règle d'or : toujours de la Source vers la Cible",
    },
    "es": {
        "Orientación constante": "Orientación clara y constante",
        "Velocidad del teclado": "Fluidez total con el teclado",
        "Recorrido visual por la interfaz y puntos de referencia": "Recorrido por la interfaz y zonas clave",
        "Visita a la interfaz visual y lugares emblemáticos": "Recorrido por la interfaz y zonas clave",
        "organiza la energía": "organiza toda su potencia y productividad",
        "Sin adivinanzas al arrastrar y soltar": "Adiós a la pesadilla de arrastrar y soltar",
        "Operaciones direccionales: siempre Origen ➔ Destino": "La regla de oro: siempre de Origen a Destino",
    },
    "pt": {
        "Orientação constante": "Orientação clara e constante",
        "Velocidade do teclado": "Agilidade total com o teclado",
        "Tour visual pela interface e pontos de referência": "Tour visual pela interface e áreas principais",
        "Tour visual pela interface e pontos turísticos": "Tour visual pela interface e áreas principais",
        "organiza a energia": "organiza toda a sua potência e produtividade",
        "Sem adivinhações ao arrastar e soltar": "Chega de sofrer com arrastar e soltar",
        "Operações direcionais: sempre Origem ➔ Destino": "A regra de ouro: sempre da Origem para o Destino",
    },
    "ko": {
        "일정한 방향성": "항상 명확한 작업 시야",
        "키보드 속도": "손끝에서 이어지는 키보드 플로우",
        "토탈 커맨더": "Total Commander",
        "더블 커맨더": "Double Commander",
        "노턴 커맨더": "Norton Commander",
        "시각적 인터페이스 둘러보기 및 주요 요소": "인터페이스 둘러보기 및 핵심 구역 안내",
        "드래그 앤 드롭으로 헤맬 필요が 없습니다": "조마조마한 마우스 드래그 앤 드롭은 이제 그만",
        "드래그 앤 드롭으로 헤맬 필요가 없습니다": "조마조마한 마우스 드래그 앤 드롭은 이제 그만",
        "방향性 있는 작업: 항상 원본 ➔ 대상": "작업의 황금률: 항상 '원본'에서 '대상'으로",
        "방향성 있는 작업: 항상 원본 ➔ 대상": "작업의 황금률: 항상 '원본'에서 '대상'으로",
    },
    "ru": {
        "Постоянная ориентация": "Всегда ясный и контролируемый обзор",
        "Скорость клавиатуры": "Высочайшая скорость работы с клавиатуры",
        "Визуальный обзор интерфейса и ориентиры": "Обзор интерфейса и ключевых зон",
        "Никаких догадок при перетаскивании": "Забудьте о нервном перетаскивании мышью",
        "Направленные операции: всегда Источник ➔ Приемник": "Золотое правило: всегда от Источника к Приемнику",
    },
    "it": {
        "Orientamento costante": "Orientamento visivo immediato e costante",
        "Velocità della tastiera": "Massima velocità e controllo da tastiera",
        "Tour visivo dell'interfaccia e punti di riferimento": "Panoramica dell'interfaccia e aree principali",
        "Tour visivo dell'interfaccia e monumenti": "Panoramica dell'interfaccia e aree principali",
        "organizza l'alimentazione": "organizza la massima potenza e produttività",
        "Nessun dubbio con il drag-and-drop": "Basta trascinare i file con l'ansia di sbagliare",
        "Operazioni direzionali: sempre Sorgente ➔ Destinazione": "La regola d'oro: sempre dalla Sorgente alla Destinazione",
    }
}

# ASCII Diagrams for index.md: Dual Panel Comparison
ASCII_DUAL_PANEL_INDEX = {
    "en": """Traditional File Browsing (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Folder A (Where was I?)│ ──?  │ Folder B (Which one?)  │  → Clutter, lost focus,
└────────────────────────┘      └────────────────────────┘    and accidental drops

The ATBCmder Way (Orthodox Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│     ACTIVE PANEL (Source)     │    INACTIVE PANEL (Target)    │
│  Files waiting for action     │  Predictable destination      │
│  [ Copy / Move / Diff / Sync  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "zh": """传统单窗口浏览 (Finder 访达):
┌────────────────────────┐      ┌────────────────────────┐
│ 文件夹 A (刚才是哪来着?)│ ──?  │ 文件夹 B (要移去哪?)   │  → 窗口层叠杂乱，容易丢失焦点，
└────────────────────────┘      └────────────────────────┘    频繁发生鼠标误拖放

ATBCmder 正统双面板交互 (Orthodox Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│       当前激活面板 (源目录)    │       对侧闲置面板 (目标目录)│
│  当前待操作的文件列表         │  清晰明确的目标存放位置       │
│  [ 复制 / 移动 / 比对 / 同步  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "zh-hant": """傳統單視窗瀏覽 (Finder 訪達):
┌────────────────────────┐      ┌────────────────────────┐
│ 資料夾 A (剛才是哪來著?)│ ──?  │ 資料夾 B (要移去哪?)   │  → 視窗層疊雜亂，容易丟失焦點，
└────────────────────────┘      └────────────────────────┘    頻繁發生滑鼠誤拖曳

ATBCmder 正統雙面板互動 (Orthodox Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│       當前作用面板 (來源目錄) │       對側閒置面板 (目標目錄) │
│  當前待操作的檔案清單         │  清晰明確的目標存放位置       │
│  [ 複製 / 移動 / 比對 / 同步  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "ja": """従来の単一ウィンドウ操作 (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ フォルダ A (どこだっけ?)│ ──?  │ フォルダ B (どれだ?)   │  → ウィンドウが重なり乱雑、
└────────────────────────┘      └────────────────────────┘    誤ドロップの危険

ATBCmder の流儀 (正統派デュアルパネル):
┌───────────────────────────────┬───────────────────────────────┐
│   アクティブパネル (操作元)   │ 非アクティブパネル (操作先)   │
│  操作を待つファイル一覧       │  迷いのない確実な転送先       │
│  [ コピー / 移動 / 比較 / 同期 ════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "de": """Herkömmliche Dateiverwaltung (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Ordner A (Wo war ich?) │ ──?  │ Ordner B (Welcher?)    │  → Fensterchaos, Fokusverlust
└────────────────────────┘      └────────────────────────┘    und falsches Ablegen

Der ATBCmder-Weg (Orthodoxes Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│     AKTIVES PANEL (Quelle)    │    INAKTIVES PANEL (Ziel)     │
│  Dateien warten auf Aktion    │  Klares, verlässliches Ziel   │
│  [ Kopieren / Bewegen / Sync  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "fr": """Navigation traditionnelle (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Dossier A (J'étais où?)│ ──?  │ Dossier B (Lequel ?)   │  → Fenêtres superposées, perte
└────────────────────────┘      └────────────────────────┘    de focus et glissers erronés

La méthode ATBCmder (Double panneau orthodoxe):
┌───────────────────────────────┬───────────────────────────────┐
│     PANNEAU ACTIF (Source)    │    PANNEAU INACTIF (Cible)    │
│  Fichiers prêts pour l'action │  Destination prévisible       │
│  [ Copier / Déplacer / Synchro ════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "es": """Navegación tradicional (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Carpeta A (¿Dónde era?)│ ──?  │ Carpeta B (¿Cuál era?) │  → Ventanas superpuestas, foco
└────────────────────────┘      └────────────────────────┘    perdido y arrastres erróneos

El modo ATBCmder (Doble panel ortodoxo):
┌───────────────────────────────┬───────────────────────────────┐
│      PANEL ACTIVO (Origen)    │     PANEL INACTIVO (Destino)  │
│  Archivos listos para operar  │  Destino claro y predecible   │
│  [ Copiar / Mover / Comparar  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "pt": """Navegação tradicional (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Pasta A (Onde eu tava?)│ ──?  │ Pasta B (Qual delas?)  │  → Janelas sobrepostas, foco
└────────────────────────┘      └────────────────────────┘    perdido e solturas erradas

O jeito ATBCmder (Painel duplo ortodoxo):
┌───────────────────────────────┬───────────────────────────────┐
│      PAINEL ATIVO (Origem)    │     PAINEL INATIVO (Destino)  │
│  Arquivos prontos para ação   │  Destino claro e previsível   │
│  [ Copiar / Mover / Sincroniz ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "ko": """기존 단일 창 파일 탐색 (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ 폴더 A (내가 어디였지?)│ ──?  │ 폴더 B (어느 폴더지?)  │  → 창 겹침, 포커스 분산,
└────────────────────────┘      └────────────────────────┘    엉뚱한 곳에 잘못 드롭

ATBCmder 정통 듀얼 패널 방식 (Orthodox Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│     활성 패널 (작업 원본)     │     비활성 패널 (작업 대상)   │
│  작업을 기다리는 파일 목록    │  명확하고 예측 가능한 대상 폴더│
│  [ 복사 / 이동 / 비교 / 동기화 ════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "ru": """Обычный просмотр файлов (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Папка А (Где я был?)   │ ──?  │ Папка Б (Какая именно?)│  → Нагромождение окон, потеря
└────────────────────────┘      └────────────────────────┘    фокуса и случайные сбросы

Метод ATBCmder (Классический двухпанельный режим):
┌───────────────────────────────┬───────────────────────────────┐
│    АКТИВНАЯ ПАНЕЛЬ (Источник) │  НЕАКТИВНАЯ ПАНЕЛЬ (Приемник) │
│  Файлы, готовые к действию    │  Точное и надежное назначение │
│  [ Копировать/Переместить/Sync ════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘""",

    "it": """Esplorazione tradizionale (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Cartella A (Dov'ero?)  │ ──?  │ Cartella B (Quale?)    │  → Finestre sovrapposte, perdita
└────────────────────────┘      └────────────────────────┘    di fuoco e rilasci errati

Il metodo ATBCmder (Doppio pannello ortodosso):
┌───────────────────────────────┬───────────────────────────────┐
│    PANNELLO ATTIVO (Sorgente) │   PANNELLO INATTIVO (Destin.) │
│  File in attesa di azione     │  Destinazione chiara e certa  │
│  [ Copia / Sposta / Diff/Sync ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘"""
}

# ASCII Diagram for index.md: Interface Landmarks Map
ASCII_LANDMARKS_INDEX = {
    "en": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Menu Bar: File   Mark   Commands   Show   Configuration   Help                       │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Main Toolbar:  [🔍 Search]  [⚡ Queue]  [⚙️ Preferences]  [📁 Drive Bar]             │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Breadcrumbs: 🏠 > Users > brain > work  │ [3] Breadcrumbs: 💾 > Volumes > Backup     │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Tab Bar: [Project Alpha ✕] [Docs] [+]   │ [4] Tab Bar: [2026 Archive ✕] [+]          │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Left Panel (Active / Source)     │ [6]  │ [5] Right Panel (Inactive / Target)        │
│ 📁 .. [Parent Directory]             │  M   │ 📁 .. [Parent Directory]                   │
│ 📁 assets                            │  I   │ 📁 archive_2025                            │
│ 📁 src                               │  D   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  D   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  L   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  E   │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Status Bar: 6 items | 2 selected (10.5 KB)   │ Drive: 142.6 GB free / 494.3 GB total │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] 顶部菜单栏: 文件(F)   选择(M)   命令(C)   显示(S)   配置(O)   帮助(H)                │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] 主工具栏:  [🔍 搜索]  [⚡ 任务队列]  [⚙️ 偏好设置]  [📁 驱动器切换栏]                │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] 路径面包屑: 🏠 > Users > brain > work   │ [3] 路径面包屑: 💾 > Volumes > Backup      │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] 标签页栏: [项目 A ✕] [开发文档] [+]     │ [4] 标签页栏: [2026 归档 ✕] [+]            │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] 左侧面板 (当前活动 / 源目录)     │ [6]  │ [5] 右侧面板 (对侧闲置 / 目标目录)         │
│ 📁 .. [返回上一层]                   │  中  │ 📁 .. [返回上一层]                         │
│ 📁 assets                            │  间  │ 📁 archive_2025                            │
│ 📁 src                               │  工  │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  具  │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  栏  │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] 状态栏: 6 项 | 已选 2 项 (10.5 KB)           │ 磁盘: 剩余 142.6 GB / 总计 494.3 GB   │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] 頂部選單列: 檔案(F)   選取(M)   命令(C)   檢視(S)   設定(O)   說明(H)                │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] 主工具列:  [🔍 搜尋]  [⚡ 工作佇列]  [⚙️ 偏好設定]  [📁 磁碟切換列]                  │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] 路徑導覽: 🏠 > Users > brain > work     │ [3] 路徑導覽: 💾 > Volumes > Backup        │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] 分頁標籤列: [專案 A ✕] [開發文件] [+]   │ [4] 分頁標籤列: [2026 封存 ✕] [+]          │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] 左側面板 (作用中 / 來源目錄)     │ [6]  │ [5] 右側面板 (對側閒置 / 目標目錄)         │
│ 📁 .. [返回上一層]                   │  中  │ 📁 .. [返回上一层]                         │
│ 📁 assets                            │  間  │ 📁 archive_2025                            │
│ 📁 src                               │  工  │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  具  │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  列  │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] 狀態列: 6 個項目 | 已選取 2 項 (10.5 KB)     │ 磁碟: 剩餘 142.6 GB / 總計 494.3 GB   │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] メニューバー: ファイル(F)   マーク(M)   コマンド(C)   表示(S)   設定(O)   ヘルプ(H)  │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] メインツールバー: [🔍 検索]  [⚡ キュー]  [⚙️ 環境設定]  [📁 ドライブバー]           │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] パス階層: 🏠 > Users > brain > work     │ [3] パス階層: 💾 > Volumes > Backup        │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] タブバー: [プロジェクト A ✕] [資料] [+] │ [4] タブバー: [2026 アーカイブ ✕] [+]      │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] 左パネル (アクティブ / 操作元)   │ [6]  │ [5] 右パネル (非アクティブ / 操作先)       │
│ 📁 .. [親ディレクトリへ]             │  中  │ 📁 .. [親ディレクトリへ]                   │
│ 📁 assets                            │  間  │ 📁 archive_2025                            │
│ 📁 src                               │  ツ  │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  ー  │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  ル  │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  バ  │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │  ー  │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] ステータスバー: 6 項目 | 選択 2 (10.5 KB)    │ 空き容量: 142.6 GB / 全体 494.3 GB    │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Menüleiste: Datei   Markieren   Befehle   Ansicht   Konfiguration   Hilfe            │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Hauptsymbolleiste: [🔍 Suchen]  [⚡ Warteschlange]  [⚙️ Einstellungen]  [📁 Laufwerke] │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Pfadzeile: 🏠 > Users > brain > work    │ [3] Pfadzeile: 💾 > Volumes > Backup       │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Tab-Leiste: [Projekt Alpha ✕] [Docs] [+]│ [4] Tab-Leiste: [2026 Archiv ✕] [+]        │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Linkes Panel (Aktiv / Quelle)    │ [6]  │ [5] Rechtes Panel (Inaktiv / Ziel)         │
│ 📁 .. [Übergeordneter Ordner]        │  M   │ 📁 .. [Übergeordneter Ordner]              │
│ 📁 assets                            │  I   │ 📁 archive_2025                            │
│ 📁 src                               │  T   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  T   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  E   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  L   │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Statusleiste: 6 Objekte | 2 gewählt (10.5 KB)│ Speicher: 142.6 GB frei / 494.3 GB     │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
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
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Barra de menú: Archivo   Marcar   Comandos   Ver   Configuración   Ayuda             │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Barra principal: [🔍 Buscar]  [⚡ Cola]  [⚙️ Preferencias]  [📁 Discos]               │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Ruta de navegación: 🏠 > Users > brain  │ [3] Ruta de navegación: 💾 > Volumes       │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Pestañas: [Proyecto Alfa ✕] [Docs] [+]  │ [4] Pestañas: [Archivo 2026 ✕] [+]         │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Panel izquierdo (Activo / Origen)│ [6]  │ [5] Panel derecho (Inactivo / Destino)     │
│ 📁 .. [Carpeta superior]             │  M   │ 📁 .. [Carpeta superior]                   │
│ 📁 assets                            │  E   │ 📁 archive_2025                            │
│ 📁 src                               │  D   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  I   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  A   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Barra de estado: 6 elementos | 2 selecc.     │ Disco: 142.6 GB libres / 494.3 GB      │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Barra de menus: Arquivo   Marcar   Comandos   Exibir   Ajustes   Ajuda               │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Barra principal: [🔍 Buscar]  [⚡ Fila]  [⚙️ Ajustes]  [📁 Discos]                    │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Navegação: 🏠 > Users > brain > work    │ [3] Navegação: 💾 > Volumes > Backup       │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Abas: [Projeto Alfa ✕] [Docs] [+]       │ [4] Abas: [Arquivo 2026 ✕] [+]             │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Painel esquerdo (Ativo / Origem) │ [6]  │ [5] Painel direito (Inativo / Destino)     │
│ 📁 .. [Pasta superior]               │  M   │ 📁 .. [Pasta superior]                     │
│ 📁 assets                            │  E   │ 📁 archive_2025                            │
│ 📁 src                               │  I   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  O   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │      │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Barra de status: 6 itens | 2 selecionados    │ Disco: 142.6 GB livres / 494.3 GB      │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] 메뉴 바: 파일(F)   선택(M)   명령(C)   보기(S)   설정(O)   도움말(H)                 │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] 주 도구 모음: [🔍 검색]  [⚡ 작업 큐]  [⚙️ 환경설정]  [📁 드라이브 바]               │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] 경로 탐색: 🏠 > Users > brain > work    │ [3] 경로 탐색: 💾 > Volumes > Backup       │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] 탭 바: [프로젝트 A ✕] [문서] [+]        │ [4] 탭 바: [2026 보관 ✕] [+]               │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] 왼쪽 패널 (활성 / 작업 원본)     │ [6]  │ [5] 오른쪽 패널 (비활성 / 작업 대상)       │
│ 📁 .. [상위 폴더로]                  │  중  │ 📁 .. [상위 폴더로]                        │
│ 📁 assets                            │  앙  │ 📁 archive_2025                            │
│ 📁 src                               │  도  │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  구  │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │      │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] 상태 표시줄: 6개 항목 | 2개 선택됨 (10.5 KB) │ 디스크: 142.6 GB 사용 가능 / 494.3 GB  │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Меню: Файл   Выделение   Команды   Вид   Настройки   Справка                         │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Панель инструментов: [🔍 Поиск]  [⚡ Очередь]  [⚙️ Настройки]  [📁 Диски]            │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Путь: 🏠 > Users > brain > work         │ [3] Путь: 💾 > Volumes > Backup            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Вкладки: [Проект Альфа ✕] [Доки] [+]    │ [4] Вкладки: [Архив 2026 ✕] [+]            │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Левая панель (Активная / Исток)  │ [6]  │ [5] Правая панель (Неактивная / Приемник)  │
│ 📁 .. [Родительская папка]           │  Ц   │ 📁 .. [Родительская папка]                 │
│ 📁 assets                            │  Е   │ 📁 archive_2025                            │
│ 📁 src                               │  Н   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  Т   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  Р   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Строка состояния: 6 элементов | 2 выбрано    │ Диск: 142.6 ГБ свободно / 494.3 ГБ    │
└──────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Barra dei menu: File   Seleziona   Comandi   Mostra   Configurazione   Aiuto         │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Barra strumenti: [🔍 Cerca]  [⚡ Coda]  [⚙️ Impostazioni]  [📁 Barra unità]          │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Percorso: 🏠 > Users > brain > work     │ [3] Percorso: 💾 > Volumes > Backup        │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Schede: [Progetto Alfa ✕] [Docs] [+]    │ [4] Schede: [Archivio 2026 ✕] [+]          │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Pannello sinistro (Attivo / Orig)│ [6]  │ [5] Pannello destro (Inattivo / Destin.)   │
│ 📁 .. [Cartella superiore]           │  M   │ 📁 .. [Cartella superiore]                 │
│ 📁 assets                            │  E   │ 📁 archive_2025                            │
│ 📁 src                               │  D   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  I   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  A   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │      │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Barra di stato: 6 elementi | 2 selezionati   │ Disco: 142.6 GB liberi / 494.3 GB      │
└──────────────────────────────────────────────────────────────────────────────────────────┘"""
}

# ASCII Diagram 1 for getting_started.md: Two-Panel Source-Target Flow
ASCII_FLOW_GETTING_STARTED = {
    "en": """┌─────────────────────────────────────────────────────────────────────────────────┐
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
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  当前激活面板 (源目录)                     对侧闲置面板 (目标目录)              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  名称               大小    修改时间│   │  名称                大小     修改时间│
│  ▸ [..]                     --:--   │ 复│  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <目录>  昨天    │   │  ▸ 2025_Archive      <目录>   5月12日 │
│  ● release_notes.md 14.2 KB 今天    │ 制│  ▸ Website_V2        <目录>   8月28日 │
│  ● update_v1.7.pkg  84.5 MB 今天    │ ➔ │  ● config.yaml       3.2 KB   6月04日 │
│                                     │   │                                       │
│  [ 聚焦状态 / 醒目蓝色高亮边框 ]    │   │  [ 未聚焦 / 柔和暗淡轮廓边框 ]        │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  當前作用面板 (來源目錄)                   對側閒置面板 (目標目錄)              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  名稱               大小    修改時間│   │  名稱                大小     修改時間│
│  ▸ [..]                     --:--   │ 複│  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <目錄>  昨天    │   │  ▸ 2025_Archive      <目錄>   5月12日 │
│  ● release_notes.md 14.2 KB 今天    │ 製│  ▸ Website_V2        <目錄>   8月28日 │
│  ● update_v1.7.pkg  84.5 MB 今天    │ ➔ │  ● config.yaml       3.2 KB   6月04日 │
│                                     │   │                                       │
│  [ 聚焦狀態 / 醒目強調色邊框 ]      │   │  [ 未聚焦 / 柔和暗淡輪廓邊框 ]        │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  アクティブパネル (操作元)                 非アクティブパネル (操作先)          │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  名前               サイズ  更新日時│ コ│  名前                サイズ   更新日時│
│  ▸ [..]                     --:--   │ ピ│  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   昨日    │ ｜│  ▸ 2025_Archive      <DIR>    5月12日 │
│  ● release_notes.md 14.2 KB 今日    │   │  ▸ Website_V2        <DIR>    8月28日 │
│  ● update_v1.7.pkg  84.5 MB 今日    │ ➔ │  ● config.yaml       3.2 KB   6月04日 │
│                                     │   │                                       │
│  [ フォーカス中 / 強調アクセント枠] │   │  [ 非フォーカス / 落ち着いた外枠 ]    │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  AKTIVES PANEL (Quelle)                    INAKTIVES PANEL (Ziel)               │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Name               Größe   Datum   │ K │  Name                Größe    Datum   │
│  ▸ [..]                     --:--   │ O │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Gestern │ P │  ▸ 2025_Archive      <DIR>    12. Mai │
│  ● release_notes.md 14.2 KB Heute   │ I │  ▸ Website_V2        <DIR>    28. Aug │
│  ● update_v1.7.pkg  84.5 MB Heute   │ E │  ● config.yaml       3.2 KB   04. Jun │
│                                     │ ➔ │                                       │
│  [ Fokussiert / Blauer Rahmen ]     │   │  [ Nicht fokussiert / Dezenter Rahmen]│
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  PANNEAU ACTIF (Source)                    PANNEAU INACTIF (Cible)              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Nom                Taille  Date    │ C │  Nom                Taille   Date     │
│  ▸ [..]                     --:--   │ O │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Hier    │ P │  ▸ 2025_Archive      <DIR>    12 mai  │
│  ● release_notes.md 14.2 KB Auj.    │ I │  ▸ Website_V2        <DIR>    28 août │
│  ● update_v1.7.pkg  84.5 MB Auj.    │ E │  ● config.yaml       3.2 KB   04 juin │
│                                     │ ➔ │                                       │
│  [ Avec focus / Contour accentué ]  │   │  [ Sans focus / Contour estompé ]     │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  PANEL ACTIVO (Origen)                     PANEL INACTIVO (Destino)             │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Nombre             Tamaño  Fecha   │ C │  Nombre             Tamaño   Fecha    │
│  ▸ [..]                     --:--   │ O │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Ayer    │ P │  ▸ 2025_Archive      <DIR>    12 mayo │
│  ● release_notes.md 14.2 KB Hoy     │ I │  ▸ Website_V2        <DIR>    28 ago  │
│  ● update_v1.7.pkg  84.5 MB Hoy     │ A │  ● config.yaml       3.2 KB   04 jun  │
│                                     │ ➔ │                                       │
│  [ Con foco / Borde resaltado ]     │   │  [ Sin foco / Borde atenuado ]        │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  PAINEL ATIVO (Origem)                     PAINEL INATIVO (Destino)             │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Nome               Tamanho Data    │ C │  Nome               Tamanho  Data     │
│  ▸ [..]                     --:--   │ O │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Ontem   │ P │  ▸ 2025_Archive      <DIR>    12 maio │
│  ● release_notes.md 14.2 KB Hoje    │ I │  ▸ Website_V2        <DIR>    28 ago  │
│  ● update_v1.7.pkg  84.5 MB Hoje    │ A │  ● config.yaml       3.2 KB   04 jun  │
│                                     │ ➔ │                                       │
│  [ Em foco / Borda destacada ]      │   │  [ Fora de foco / Borda suave ]       │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  활성 패널 (작업 원본)                     비활성 패널 (작업 대상)              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  이름               크기    수정일  │ 복│  이름               크기     수정일   │
│  ▸ [..]                     --:--   │ 사│  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   어제    │   │  ▸ 2025_Archive      <DIR>    5월 12일│
│  ● release_notes.md 14.2 KB 오늘    │ ➔ │  ▸ Website_V2        <DIR>    8월 28일│
│  ● update_v1.7.pkg  84.5 MB 오늘    │   │  ● config.yaml       3.2 KB   6월 04일│
│                                     │   │                                       │
│  [ 포커스 획득 / 파란색 테두리 ]    │   │  [ 포커스 없음 / 부드러운 테두리 ]    │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  АКТИВНАЯ ПАНЕЛЬ (Источник)                НЕАКТИВНАЯ ПАНЕЛЬ (Приемник)         │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Имя                Размер  Дата    │ К │  Имя                Размер   Дата     │
│  ▸ [..]                     --:--   │ О │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Вчера   │ П │  ▸ 2025_Archive      <DIR>    12 мая  │
│  ● release_notes.md 14.2 KB Сегодня │ И │  ▸ Website_V2        <DIR>    28 авг  │
│  ● update_v1.7.pkg  84.5 MB Сегодня │ Р │  ● config.yaml       3.2 KB   04 июн  │
│                                     │ ➔ │                                       │
│  [ В фокусе / Синяя рамка акцента ] │   │  [ Не в фокусе / Неяркая рамка ]      │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────────────────────────┐
│  PANNELLO ATTIVO (Sorgente)                PANNELLO INATTIVO (Destinazione)     │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Nome               Dimens. Data    │ C │  Nome               Dimens.  Data     │
│  ▸ [..]                     --:--   │ O │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Ieri    │ P │  ▸ 2025_Archive      <DIR>    12 mag  │
│  ● release_notes.md 14.2 KB Oggi    │ I │  ▸ Website_V2        <DIR>    28 ago  │
│  ● update_v1.7.pkg  84.5 MB Oggi    │ A │  ● config.yaml       3.2 KB   04 giu  │
│                                     │ ➔ │                                       │
│  [ Con focus / Bordo evidenziato ]  │   │  [ Senza focus / Bordo attenuato ]    │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘"""
}

# ASCII Diagram 2 for getting_started.md: Interface Anatomy Landmark
ASCII_ANATOMY_GETTING_STARTED = {
    "en": """┌─────────────────────────────────────────────────────────────────────────────────┐
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
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] macOS 原生顶部菜单栏                                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] 顶部主工具栏  [ ↺ 刷新 ] [ 📋 复制 ] [ ✂ 剪切 ] [ 🗑 删除 ] ...            │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] 路径面包屑导航 (左侧面板)       │   │ [3] 路径面包屑导航 (右侧面板)         │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] 文件夹标签栏: [开发] [文档] [+] │[6]│ [4] 文件夹标签栏: [照片] [备份] [+]   │
├─────────────────────────────────────┤中 ├───────────────────────────────────────┤
│                                     │间 │                                       │
│ [5] 双文件列表面板 (左)             │工 │ [5] 双文件列表面板 (右)               │
│     - 虚拟化海量列表                │具 │     - 虚拟化海量列表                  │
│     - 名称、扩展名、大小、时间、权限│栏 │     - 名称、扩展名、大小、时间、权限  │
│     - 实时排序与通配符过滤          │&  │     - 实时排序与通配符过滤            │
│                                     │分 │                                       │
│                                     │割 │                                       │
│                                     │线 │                                       │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] 底部状态栏与磁盘容量指示器                                                  │
│  选中 3 / 28 项 (已选 42.8 MB / 共 1.2 GB)  |  Macintosh HD: 218.4 GB 剩余可用  │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] macOS 原生頂部選單列                                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] 頂部主工具列  [ ↺ 重新整理 ] [ 📋 複製 ] [ ✂ 剪下 ] [ 🗑 刪除 ] ...         │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] 路徑導覽列 (左側面板)           │   │ [3] 路徑導覽列 (右側面板)             │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] 資料夾分頁: [開發] [文件] [+]   │[6]│ [4] 資料夾分頁: [相片] [備份] [+]     │
├─────────────────────────────────────┤中 ├───────────────────────────────────────┤
│                                     │間 │                                       │
│ [5] 雙檔案清單面板 (左)             │工 │ [5] 雙檔案清單面板 (右)               │
│     - 虛擬化海量清單                │具 │     - 虛擬化海量清單                  │
│     - 名稱、副檔名、大小、修改時間  │列 │     - 名稱、副檔名、大小、修改時間    │
│     - 即時排序與萬用字元篩選        │&  │     - 即時排序與萬用字元篩選          │
│                                     │分 │                                       │
│                                     │割 │                                       │
│                                     │線 │                                       │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] 底部狀態列與磁碟容量指示器                                                  │
│  已選 3 / 28 項 (已選 42.8 MB / 共 1.2 GB)   |  Macintosh HD: 218.4 GB 剩餘可用 │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] macOS ネイティブメニューバー                                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] メインツールバー  [ ↺ 更新 ] [ 📋 コピー ] [ ✂ 移動 ] [ 🗑 削除 ] ...       │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] パス階層バー (左パネル)         │   │ [3] パス階層バー (右パネル)           │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] フォルダタブ: [開発] [文書] [+] │[6]│ [4] フォルダタブ: [写真] [保存] [+]   │
├─────────────────────────────────────┤中 ├───────────────────────────────────────┤
│                                     │間 │                                       │
│ [5] デュアルファイル一覧 (左)       │ツ │ [5] デュアルファイル一覧 (右)         │
│     - 高速仮想化テーブル表示        │｜ │     - 高速仮想化テーブル表示          │
│     - ファイル名、サイズ、更新日時  │ル │     - ファイル名、サイズ、更新日時    │
│     - リアルタイムソートと絞り込み  │バ │     - リアルタイムソートと絞り込み    │
│                                     │｜ │                                       │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] ステータスバーと空き容量表示                                                │
│  選択中: 3 / 28 項目 (42.8 MB / 1.2 GB)      |  空き容量: 218.4 GB              │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] NATIVE MACOS-MENÜLEISTE                                                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] HAUPTSYMBOLLEISTE  [ ↺ Neu laden ] [ 📋 Kopieren ] [ ✂ Bewegen ] ...        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] PFADZEILE (Linkes Panel)        │   │ [3] PFADZEILE (Rechtes Panel)         │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] ORDNER-TABS: [Dev] [Docs] [+]   │[6]│ [4] ORDNER-TABS: [Fotos] [Backup] [+] │
├─────────────────────────────────────┤MIT│───────────────────────────────────────┤
│                                     │TEL│                                       │
│ [5] DUAL-DATEIPANEL (Links)         │   │ [5] DUAL-DATEIPANEL (Rechts)          │
│     - Virtualisierte Tabellenansicht│LEI│     - Virtualisierte Tabellenansicht  │
│     - Name, Ext, Größe, Datum, Rechte│STE│     - Name, Ext, Größe, Datum, Rechte │
│     - Echtzeit-Sortierung & Filter  │   │     - Echtzeit-Sortierung & Filter    │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] STATUSLEISTE & SPEICHERANZEIGE                                              │
│  3 von 28 gewählt (42.8 MB / 1.2 GB)         |  Macintosh HD: 218.4 GB frei     │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] BARRE DE MENUS MACOS NATIVE                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] BARRE D'OUTILS  [ ↺ Actualiser ] [ 📋 Copier ] [ ✂ Déplacer ] ...           │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] FIL D'ARIANE (Panneau gauche)   │   │ [3] FIL D'ARIANE (Panneau droit)      │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] ONGLETS : [Dev] [Docs] [+]      │[6]│ [4] ONGLETS : [Photos] [Backup] [+]   │
├─────────────────────────────────────┤BAR│───────────────────────────────────────┤
│                                     │RE │                                       │
│ [5] DOUBLE PANNEAU (Gauche)         │   │ [5] DOUBLE PANNEAU (Droit)            │
│     - Table virtualisée ultra-rapide│MI-│     - Table virtualisée ultra-rapide  │
│     - Nom, Ext, Taille, Date, Droits│LIE│     - Nom, Ext, Taille, Date, Droits  │
│     - Tri et filtre en temps réel   │U  │     - Tri et filtre en temps réel     │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] BARRE D'ÉTAT ET JAUGE DE STOCKAGE                                           │
│  3 sur 28 sélectionnés (42.8 Mo / 1.2 Go)    |  Macintosh HD : 218.4 Go libres  │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] BARRA DE MENÚ NATIVA DE MACOS                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] BARRA PRINCIPAL  [ ↺ Actualizar ] [ 📋 Copiar ] [ ✂ Mover ] ...             │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] RUTA DE NAVEGACIÓN (Izquierda)  │   │ [3] RUTA DE NAVEGACIÓN (Derecha)      │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] PESTAÑAS: [Dev] [Docs] [+]      │[6]│ [4] PESTAÑAS: [Fotos] [Backup] [+]    │
├─────────────────────────────────────┤BAR│───────────────────────────────────────┤
│                                     │RA │                                       │
│ [5] DOBLE PANEL (Izquierdo)         │   │ [5] DOBLE PANEL (Derecho)             │
│     - Listado virtualizado rápido   │ME-│     - Listado virtualizado rápido     │
│     - Nombre, Ext, Tamaño, Fecha    │DIA│     - Nombre, Ext, Tamaño, Fecha      │
│     - Ordenación y filtros en vivo  │   │     - Ordenación y filtros en vivo    │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] BARRA DE ESTADO Y ALMACENAMIENTO                                            │
│  3 de 28 seleccionados (42.8 MB / 1.2 GB)    |  Macintosh HD: 218.4 GB libres   │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] BARRA DE MENUS NATIVA DO MACOS                                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] BARRA PRINCIPAL  [ ↺ Atualizar ] [ 📋 Copiar ] [ ✂ Mover ] ...              │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] RUTA DE NAVEGAÇÃO (Esquerda)    │   │ [3] RUTA DE NAVEGAÇÃO (Direita)       │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] ABAS: [Dev] [Docs] [+]          │[6]│ [4] ABAS: [Fotos] [Backup] [+]        │
├─────────────────────────────────────┤BAR│───────────────────────────────────────┤
│                                     │RA │                                       │
│ [5] PAINEL DUPLO (Esquerdo)         │   │ [5] PAINEL DUPLO (Direito)            │
│     - Listagem virtualizada rápida  │ME-│     - Listagem virtualizada rápida    │
│     - Nome, Ext, Tamanho, Data      │DIA│     - Nome, Ext, Tamanho, Data        │
│     - Ordenação e filtros em tempo real│ │     - Ordenação e filtros em tempo real│
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] BARRA DE STATUS E ESPAÇO EM DISCO                                           │
│  3 de 28 selecionados (42.8 MB / 1.2 GB)     |  Macintosh HD: 218.4 GB livres   │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] macOS 네이티브 메뉴 바                                                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] 상단 주 도구 모음  [ ↺ 새로고침 ] [ 📋 복사 ] [ ✂ 이동 ] [ 🗑 삭제 ] ...     │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] 경로 탐색 바 (왼쪽 패널)        │   │ [3] 경로 탐색 바 (오른쪽 패널)        │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] 폴더 탭: [Dev] [Docs] [+]       │[6]│ [4] 폴더 탭: [사진] [백업] [+]        │
├─────────────────────────────────────┤중 ├───────────────────────────────────────┤
│                                     │앙 │                                       │
│ [5] 듀얼 파일 목록 패널 (왼쪽)      │도 │ [5] 듀얼 파일 목록 패널 (오른쪽)      │
│     - 대용량 가상화 테이블 목록     │구 │     - 대용량 가상화 테이블 목록       │
│     - 파일명, 확장자, 크기, 수정일  │   │     - 파일명, 확장자, 크기, 수정일    │
│     - 실시간 정렬 및 와일드카드 필터│바 │     - 실시간 정렬 및 와일드카드 필터  │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] 상태 표시줄 및 드라이브 저장 공간 게이지                                    │
│  선택 항목: 3 / 28개 (42.8 MB / 1.2 GB)      |  사용 가능 공간: 218.4 GB        │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] СИСТЕМНОЕ МЕНЮ MACOS                                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] ПАНЕЛЬ ИНСТРУМЕНТОВ  [ ↺ Обновить ] [ 📋 Копировать ] [ ✂ Переместить ] ... │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] СТРОКА ПУТИ (Левая панель)      │   │ [3] СТРОКА ПУТИ (Правая панель)       │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] ВКЛАДКИ: [Dev] [Docs] [+]       │[6]│ [4] ВКЛАДКИ: [Фото] [Backup] [+]      │
├─────────────────────────────────────┤ПАН│───────────────────────────────────────┤
│                                     │ЕЛЬ│                                       │
│ [5] ДВУХПАНЕЛЬНЫЙ СПИСОК (Слева)    │   │ [5] ДВУХПАНЕЛЬНЫЙ СПИСОК (Справа)     │
│     - Виртуализированная таблица    │РАЗ│     - Виртуализированная таблица      │
│     - Имя, Расш, Размер, Дата, Права│ДЕЛ│     - Имя, Расш, Размер, Дата, Права  │
│     - Мгновенная сортировка и фильтр│   │     - Мгновенная сортировка и фильтр  │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] СТРОКА СОСТОЯНИЯ И ОБЪЕМ ДИСКА                                              │
│  Выбрано 3 из 28 (42.8 МБ / 1.2 ГБ)          |  Macintosh HD: 218.4 ГБ свободно │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] BARRA DEI MENU NATIVA DI MACOS                                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] BARRA STRUMENTI  [ ↺ Ricarica ] [ 📋 Copia ] [ ✂ Sposta ] [ 🗑 Elimina ] ...│
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] BARRA DEL PERCORSO (Sinistra)   │   │ [3] BARRA DEL PERCORSO (Destra)       │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] SCHEDE: [Dev] [Docs] [+]        │[6]│ [4] SCHEDE: [Foto] [Backup] [+]       │
├─────────────────────────────────────┤BAR│───────────────────────────────────────┤
│                                     │RA │                                       │
│ [5] DOPPIO PANNELLO (Sinistra)      │   │ [5] DOPPIO PANNELLO (Destra)          │
│     - Tabella virtualizzata rapida  │ME-│     - Tabella virtualizzata rapida    │
│     - Nome, Est, Dimens, Data, Dir. │DIA│     - Nome, Est, Dimens, Data, Dir.   │
│     - Ordinamento e filtri in tempo reale│ │     - Ordinamento e filtri in tempo reale│
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] BARRA DI STATO E SPAZIO SU DISCO                                            │
│  3 di 28 selezionati (42.8 MB / 1.2 GB)      |  Macintosh HD: 218.4 GB liberi   │
└─────────────────────────────────────────────────────────────────────────────────┘"""
}

# ASCII Diagram for navigation_and_tabs.md: Breadcrumbs, Tabs and Quick Search
ASCII_NAV_TABS = {
    "en": """┌─────────────────────────────────────────────────────────────────────────────────┐
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
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [路径面包屑]  🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [标签页栏]    [★ 源码核心 (锁定)] [设计资源] [编译输出] [+]                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  名称                         类型      大小      修改时间           权限       │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <目录>              今天 14:22         drwxr-xr-x │
│  ▸ ui                         <目录>              今天 15:05         drwxr-xr-x │
│  ● main.py                    py        8.4 KB    今天 15:10         -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   昨天 19:40         -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [实时快速搜索]  🔍 查找: mai_   (匹配项: main.py)                               │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [路徑導覽列]  🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [分頁標籤列]  [★ 原始碼核心 (鎖定)] [設計資源] [組建輸出] [+]                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│  名稱                         類型      大小      修改時間           權限       │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <目錄>              今天 14:22         drwxr-xr-x │
│  ▸ ui                         <目錄>              今天 15:05         drwxr-xr-x │
│  ● main.py                    py        8.4 KB    今天 15:10         -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   昨天 19:40         -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [即時快速搜尋]  🔍 尋找: mai_   (符合項: main.py)                               │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [パス階層]    🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [タブバー]    [★ ソース (固定)] [アセット] [ビルド出力] [+]                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  名前                         拡張子    サイズ    更新日時           属性       │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               今日 14:22         drwxr-xr-x │
│  ▸ ui                         <DIR>               今日 15:05         drwxr-xr-x │
│  ● main.py                    py        8.4 KB    今日 15:10         -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   昨日 19:40         -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [クイック検索]  🔍 検索: mai_   (一致: main.py)                                 │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [PFADZEILE]   🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [TAB-LEISTE]  [★ Quellcode (Gesperrt)] [Assets] [Build-Ausgabe] [+]             │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Name                         Typ       Größe     Geändert           Rechte     │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Heute, 14:22       drwxr-xr-x │
│  ▸ ui                         <DIR>               Heute, 15:05       drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Heute, 15:10       -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Gestern, 19:40     -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [SCHNELLSUCHE]  🔍 Suchen: mai_   (Treffer: main.py)                            │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [FIL D'ARIANE] 🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src              │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [ONGLETS]     [★ Source (Verrouillé)] [Assets] [Sortie Build] [+]               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Nom                          Type      Taille    Modifié le         Droits     │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Aujourd'hui, 14:22 drwxr-xr-x │
│  ▸ ui                         <DIR>               Aujourd'hui, 15:05 drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Aujourd'hui, 15:10 -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Hier, 19:40        -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [RECHERCHE RAPIDE]  🔍 Chercher: mai_   (Correspondance : main.py)              │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [RUTA MIGA]   🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [PESTAÑAS]    [★ Código (Bloqueado)] [Recursos] [Compilación] [+]               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Nombre                       Tipo      Tamaño    Modificado         Permisos   │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Hoy, 14:22         drwxr-xr-x │
│  ▸ ui                         <DIR>               Hoy, 15:05         drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Hoy, 15:10         -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Ayer, 19:40        -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [BÚSQUEDA RÁPIDA]  🔍 Buscar: mai_   (Coincidencia: main.py)                     │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [NAVEGAÇÃO]   🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [ABAS]        [★ Código (Bloqueado)] [Recursos] [Saída Build] [+]               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Nome                         Tipo      Tamanho   Modificado         Permissões │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Hoje, 14:22        drwxr-xr-x │
│  ▸ ui                         <DIR>               Hoje, 15:05        drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Hoje, 15:10        -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Ontem, 19:40       -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [BUSCA RÁPIDA]  🔍 Buscar: mai_   (Correspondência: main.py)                    │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [경로 표시줄] 🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [탭 바]       [★ 소스 코드 (고정)] [에셋] [빌드 결과물] [+]                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  이름                         유형      크기      수정일             권한       │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               오늘 14:22         drwxr-xr-x │
│  ▸ ui                         <DIR>               오늘 15:05         drwxr-xr-x │
│  ● main.py                    py        8.4 KB    오늘 15:10         -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   어제 19:40         -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [빠른 검색]    🔍 찾기: mai_   (일치 항목: main.py)                              │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [ПУТЬ]        🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [ВКЛАДКИ]     [★ Исходники (Закрепл)] [Ресурсы] [Сборка] [+]                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Имя                          Тип       Размер    Изменен            Права      │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Сегодня, 14:22     drwxr-xr-x │
│  ▸ ui                         <DIR>               Сегодня, 15:05     drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Сегодня, 15:10     -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Вчера, 19:40       -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [БЫСТРЫЙ ПОИСК]  🔍 Найти: mai_   (Найдено: main.py)                            │
└─────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────────────────────────┐
│ [PERCORSO]    🏠 / ▸ Users ▸ username ▸ Projects ▸ ATBCmder ▸ src               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [SCHEDE]      [★ Sorgente (Bloccato)] [Risorse] [Output Build] [+]              │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Nome                         Tipo      Dimens.   Modificato il      Permessi   │
│  ▸ [..]                                           --:--              drwxr-xr-x │
│  ▸ core                       <DIR>               Oggi, 14:22        drwxr-xr-x │
│  ▸ ui                         <DIR>               Oggi, 15:05        drwxr-xr-x │
│  ● main.py                    py        8.4 KB    Oggi, 15:10        -rw-r--r-- │
│  ● config.xml                 xml       12.1 KB   Ieri, 19:40        -rw-r--r-- │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [RICERCA RAPIDA]  🔍 Cerca: mai_   (Corrispondenza: main.py)                    │
└─────────────────────────────────────────────────────────────────────────────────┘"""
}
