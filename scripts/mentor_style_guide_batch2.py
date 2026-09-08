#!/usr/bin/env python3
"""
scripts/mentor_style_guide_batch2.py
Localized ASCII diagrams and mentor terminology for Batch 2:
- file_operations.md
- viewers_and_editors.md
- power_tools.md
"""

from typing import Dict

# 1. file_operations.md Block 0: Core Two-Panel Transfer
ASCII_FILE_OPS_TRANSFER: Dict[str, str] = {
    "en": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE PANEL (Source)                              INACTIVE PANEL (Target)            │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Date    │   │  Name                         Size  │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ C │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ O │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ P │  ● .env.production                  │
│                                              │ Y │                                     │
│  [2 files selected: 1.8 GB]                  │ ➔ │  [Destination ready for ingestion] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Copy     [F6] Move     [Shift+F5] Duplicate In-Place     [F8 / ⌘⌫] Trash         │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  当前激活面板 (源目录 Source)                         对侧闲置面板 (目标目录 Target)   │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  名称                         大小   修改时间│   │  名称                         大小  │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ 复│  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ 制│  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │ 对│                                     │
│  [已选中 2 个文件: 1.8 GB]                   │ 侧│  [目标目录就绪，随时可接收写入]     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] 复制     [F6] 移动     [Shift+F5] 原地创建副本     [F8 / ⌘⌫] 移至废纸篓          │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  啟用面板 (源目錄 Source)                            對側面板 (目標目錄 Target)        │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  名稱                         大小   修改時間│   │  名稱                         大小  │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ 復│  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ 製│  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │ 對│                                     │
│  [已選中 2 個檔案: 1.8 GB]                   │ 側│  [目標目錄就緒，隨時可接收寫入]     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] 複製     [F6] 移動     [Shift+F5] 原地建立副本     [F8 / ⌘⌫] 移至垃圾桶          │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  アクティブパネル (操作元 Source)                   非アクティブパネル (操作先 Target) │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  名前                         サイズ 更新日時│ コ│  名前                         サイズ│
│  ▸ [..]                              --:--   │ ピ│  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ ｜│  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ ➔ │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ 対│  ● .env.production                  │
│                                              │ 側│                                     │
│  [2 項目を選択中: 1.8 GB]                    │   │  [転送先は準備完了・即座に書込可能] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] コピー     [F6] 移動     [Shift+F5] 同一複製     [F8 / ⌘⌫] ゴミ箱へ移動          │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  AKTIVES PANEL (Quelle Source)                      INAKTIVES PANEL (Ziel Target)      │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Größe  Datum   │   │  Name                         Größe │
│  ▸ [..]                              --:--   │ K │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 Dateien gewählt: 1.8 GB]                 │   │  [Zielordner empfangsbereit]        │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Kopieren   [F6] Bewegen   [Shift+F5] Duplizieren   [F8 / ⌘⌫] In den Papierkorb   │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANNEAU ACTIF (Source)                             PANNEAU INACTIF (Cible)            │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nom                          Taille Date    │   │  Nom                          Taille│
│  ▸ [..]                              --:--   │ C │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 fichiers sélectionnés : 1.8 GB]          │   │  [Dossier cible prêt à recevoir]    │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Copier   [F6] Déplacer   [Shift+F5] Dupliquer   [F8 / ⌘⌫] Mettre à la corbeille  │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANEL ACTIVO (Origen)                              PANEL INACTIVO (Destino)           │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nombre                       Tamaño Fecha   │   │  Nombre                       Tamaño│
│  ▸ [..]                              --:--   │ C │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 archivos seleccionados: 1.8 GB]          │   │  [Carpeta destino lista para recibir]│
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Copiar   [F6] Mover   [Shift+F5] Duplicar   [F8 / ⌘⌫] Mover a la papelera        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PAINEL ATIVO (Origem)                              PAINEL INATIVO (Destino)           │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nome                         Tam.   Data    │   │  Nome                           Tam.│
│  ▸ [..]                              --:--   │ C │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 arquivos selecionados: 1.8 GB]           │   │  [Diretório de destino pronto]      │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Copiar   [F6] Mover   [Shift+F5] Duplicar   [F8 / ⌘⌫] Mover para a lixeira       │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  활성 패널 (원본 Source)                            비활성 패널 (대상 Target)          │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  이름                         크기   수정일  │ 복│  이름                         크기  │
│  ▸ [..]                              --:--   │ 사│  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ ➔ │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │   │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ 대│  ● .env.production                  │
│                                              │ 상│                                     │
│  [2개 파일 선택됨: 1.8 GB]                   │   │  [대상 디렉터리 준비 완료]          │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] 복사     [F6] 이동     [Shift+F5] 동일 위치 복제     [F8 / ⌘⌫] 휴지통으로 이동   │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  АКТИВНАЯ ПАНЕЛЬ (Источник)                         НЕАКТИВНАЯ ПАНЕЛЬ (Приемник)       │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Имя                          Размер Дата    │   │  Имя                          Размер│
│  ▸ [..]                              --:--   │ К │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ О │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ П │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [Выбрано 2 файла: 1.8 GB]                   │   │  [Целевая папка готова к записи]    │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Копировать   [F6] Переместить   [Shift+F5] Дублировать   [F8 / ⌘⌫] В Корзину     │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANNELLO ATTIVO (Sorgente)                         PANNELLO INATTIVO (Destinazione)   │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nome                         Dim.   Data    │   │  Nome                           Dim.│
│  ▸ [..]                              --:--   │ C │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 file selezionati: 1.8 GB]                │   │  [Cartella di destinazione pronta]  │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Copia   [F6] Sposta   [Shift+F5] Duplica   [F8 / ⌘⌫] Sposta nel Cestino          │
└────────────────────────────────────────────────────────────────────────────────────────┘"""
}

# 2. viewers_and_editors.md Block 0: Quick View Split
ASCII_VIEWERS_QUICK_VIEW: Dict[str, str] = {
    "en": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE PANEL (File Navigation)                     INACTIVE PANEL (Quick View)        │
│  /Users/brain/Projects/atbcmder/src                 [Quick View Preview: main.py]      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Date    │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Main application entry point  │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Line 1/140]  │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Toggle Quick View    [F3] Universal Lister    [F4] Internal Editor  │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  激活面板 (文件列表浏览)                            对侧闲置面板 (快速预览 Quick View) │
│  /Users/brain/Projects/atbcmder/src                 [正在快速预览: main.py]            │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  名称                         大小   修改时间│   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: 主程序入口入口文件            │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [行 1/140]    │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] 开启/关闭快速预览   [F3] 全能查看器   [F4] 内置轻量代码/图像编辑器  │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  啟用面板 (檔案列表瀏覽)                            對側閒置面板 (快速預覽 Quick View) │
│  /Users/brain/Projects/atbcmder/src                 [正在快速預覽: main.py]            │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  名稱                         大小   修改時間│   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: 主程式進入點檔案              │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [行 1/140]    │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] 開啟/關閉快速預覽   [F3] 全能檢視器   [F4] 內建輕量程式碼/影像編輯器│
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  アクティブパネル (ファイル一覧)                    非アクティブパネル (Quick View)    │
│  /Users/brain/Projects/atbcmder/src                 [プレビュー表示中: main.py]        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  名前                         サイズ 更新日時│   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: メインエントリポイント        │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [行 1/140]    │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Quick View切替      [F3] Lister表示      [F4] 内蔵エディタ起動      │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  AKTIVES PANEL (Dateinavigation)                    INAKTIVES PANEL (Quick View)       │
│  /Users/brain/Projects/atbcmder/src                 [Schnellvorschau: main.py]         │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Größe  Datum   │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Programmeinstiegspunkt        │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Zeile 1/140] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Quick View umschalten   [F3] Lister öffnen   [F4] Editor starten    │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANNEAU ACTIF (Navigation)                         PANNEAU INACTIF (Quick View)       │
│  /Users/brain/Projects/atbcmder/src                 [Aperçu rapide : main.py]          │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nom                          Taille Date    │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Point d'entrée principal      │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Ligne 1/140] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Basculer Quick View    [F3] Visionneuse Lister    [F4] Éditeur      │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANEL ACTIVO (Navegación)                          PANEL INACTIVO (Quick View)        │
│  /Users/brain/Projects/atbcmder/src                 [Vista previa rápida: main.py]     │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nombre                       Tamaño Fecha   │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Punto de entrada principal    │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Línea 1/140] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Alternar Quick View    [F3] Visor Lister    [F4] Editor de código   │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PAINEL ATIVO (Navegação)                           PAINEL INATIVO (Quick View)        │
│  /Users/brain/Projects/atbcmder/src                 [Prévia rápida: main.py]           │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nome                         Tam.   Data    │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Ponto de entrada do programa  │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Linha 1/140] │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Alternar Quick View    [F3] Visualizador Lister    [F4] Editor      │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  활성 패널 (파일 목록 탐색)                         비활성 패널 (Quick View 빠른 미리보기)│
│  /Users/brain/Projects/atbcmder/src                 [미리보기 표시 중: main.py]        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  이름                         크기   수정일  │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: 메인 프로그램 진입점          │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [줄 1/140]    │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Quick View 토글     [F3] Lister 뷰어     [F4] 내장 코드 에디터      │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  АКТИВНАЯ ПАНЕЛЬ (Просмотр файлов)                  НЕАКТИВНАЯ ПАНЕЛЬ (Quick View)     │
│  /Users/brain/Projects/atbcmder/src                 [Быстрый просмотр: main.py]        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Имя                          Размер Дата    │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Главная точка входа           │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Строка 1/140]│
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Быстрый просмотр     [F3] Lister просмотр     [F4] Встроенный редакт│
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANNELLO ATTIVO (Navigazione file)                 PANNELLO INATTIVO (Quick View)     │
│  /Users/brain/Projects/atbcmder/src                 [Anteprima rapida: main.py]        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nome                         Dim.   Data    │   │ 0001: \"\"\"                           │
│  ▸ [..]                              --:--   │ Q │ 0002: Punto di ingresso principale  │
│  ✔ main.py                    8.4 KB 15:10   │ U │ 0003: \"\"\"                           │
│  ● config.xml                12.1 KB 14:20   │ I │ 0004: import sys                    │
│  ● hero_banner.png          248.5 KB 09:12   │ C │ 0005: from PySide6.QtWidgets import │
│  ● sample_invoice.pdf       512.0 KB 11:30   │ K │ 0006:     QApplication              │
│  ● release_theme.mp3          4.2 MB 16:45   │   │                                     │
│  ● firmware_dump.bin          1.0 MB 10:00   │ V │ [UTF-8] [Python] [LF] [Riga 1/140]  │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│   [Cmd+Q / Ctrl+Q] Attiva Quick View    [F3] Visualizzatore Lister    [F4] Editor      │
└────────────────────────────────────────────────────────────────────────────────────────┘"""
}

# 3. power_tools.md Block 0: Automation Landmarks Map
ASCII_POWER_TOOLS_MAP: Dict[str, str] = {
    "en": """┌────────────────────────────────────────────────────────────────────────────────────────┐
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
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 双栏文件操作面板                                       │
│          左侧面板 (源路径 / 目录 A)                    右侧面板 (目标路径 / 目录 B)    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] 批量多重重命名 (Ctrl+M)             │  [2] 差异比对与双栏 Diff (Meta+Shift+F12)   │
│      智能通配符、正则、计数器、实时安全预览│      逐行高亮差异、代码段合并同步、就地保存 │
│                                          │                                             │
│  [3] 文件夹双向同步 (Shift+F12)          │  [4] 全局深度高级搜索 (Alt+F7)              │
│      内容/时间比对、非对称单向镜像复制   │      Spotlight / 递归深搜 ➔ 填入虚拟面板    │
│                                          │                                             │
│  [5] 语义化命令输入栏 (/)                │  [6] 极客安全与实用工具箱                   │
│      原生 Spotlight 检索、AI 自然语言命令│      大文件分割合并、哈希校验、安全粉碎擦除 │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [填入虚拟列表] ➔ 将全盘搜索匹配项聚合为虚拟文件夹面板，统一执行跨目录批量操作         │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 雙欄檔案操作面板                                       │
│          左側面板 (源路徑 / 目錄 A)                    右側面板 (目標路徑 / 目錄 B)    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] 批次多重重新命名 (Ctrl+M)           │  [2] 差異比對與雙欄 Diff (Meta+Shift+F12)   │
│      智慧萬用字元、正規表示式、計數器    │      逐行高亮差異、程式碼區塊合併同步       │
│                                          │                                             │
│  [3] 資料夾雙向同步 (Shift+F12)          │  [4] 全域深度進階搜尋 (Alt+F7)              │
│      內容/時間比對、非對稱單向鏡像複製   │      Spotlight / 遞迴深搜 ➔ 填入虛擬面板    │
│                                          │                                             │
│  [5] 語意化命令輸入列 (/)                │  [6] 極客安全與實用工具箱                   │
│      原生 Spotlight 檢索、AI 自然語言指令│      大檔案分割合併、雜湊校驗、安全抹除     │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [填入虛擬清單] ➔ 將全碟搜尋符合項目聚合為虛擬資料夾面板，統一執行跨目錄批次操作       │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                デュアルファイル操作パネル                              │
│          左パネル (操作元 / フォルダ A)                右パネル (操作先 / フォルダ B)  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] 一括リネーム (Ctrl+M)               │  [2] 2画面ファイル差分比較 (Meta+Shift+F12) │
│      トークン、正規表現、連番、安全プレビュー│  行ハイライト、差分同期、直接編集・保存 │
│                                          │                                             │
│  [3] ディレクトリ同期 (Shift+F12)        │  [4] 高度なファイル検索 (Alt+F7)            │
│      内容/更新日時比較、非対称ミラー同期 │      Spotlight / 詳細検索 ➔ リストへ転送    │
│                                          │                                             │
│  [5] セマンティック検索バー (/)          │  [6] セキュリティ＆ファイルユーティリティ   │
│      Spotlight 連携、自然言語 AI クエリ  │      ファイル分割・結合、ハッシュ、完全消去 │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [リストボックスへ転送] ➔ 検索結果を仮想タブに集約し、フォルダ横断で一括処理を実行     │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                DUALES DATEIPANEL                                       │
│          Linkes Panel (Quelle / Ordner A)              Rechtes Panel (Ziel / Ordner B) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Mehrfach-Umbenennung (Ctrl+M)       │  [2] Datei-Differenzvergleich (⌘⇧F12)       │
│      Platzhalter, RegEx, Zähler, Vorschau│      Zeilen-Highlight, Hunk-Sync, Speichern │
│                                          │                                             │
│  [3] Ordner-Synchronisierung (Shift+F12) │  [4] Erweiterte Suche (Alt+F7)              │
│      Inhalt/Datum, Asymmetrischer Spiegel│      Spotlight / Tiefenscan ➔ An Liste senden│
│                                          │                                             │
│  [5] Semantische Befehlszeile (/)        │  [6] Datei-Dienstprogramme & Sicherheit     │
│      Spotlight-Filter, KI-Befehle, NLP   │      Teilen/Zusammenfügen, Hash, Schreddern │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [An Liste senden] ➔ Führt Suchergebnisse in einem virtuellen Tab für Stapelaktionen zusammen│
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                DOUBLE PANNEAU DE FICHIERS                              │
│          Panneau gauche (Source / Dossier A)           Panneau droit (Cible / Dossier B)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Renommage par lot (Ctrl+M)          │  [2] Différence de fichiers côte à côte (⌘⇧F12)│
│      Balises, RegEx, Compteurs, Aperçu   │      Surlignage, Fusion de blocs, Édition   │
│                                          │                                             │
│  [3] Synchronisation de dossiers (⇧F12)  │  [4] Recherche avancée (Alt+F7)             │
│      Comparaison contenu/date, Miroir    │      Spotlight / Analyse ➔ Vers la liste    │
│                                          │                                             │
│  [5] Barre de commande sémantique (/)    │  [6] Utilitaires et sécurité                │
│      Requêtes Spotlight, Requêtes IA     │      Découpage/Fusion, Hachage, Broyage     │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Vers la liste] ➔ Charge les résultats dans un onglet virtuel pour traitement par lot │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                PANEL DUAL DE ARCHIVOS                                  │
│          Panel izquierdo (Origen / Carpeta A)          Panel derecho (Destino / Carpeta B)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Renombrado masivo (Ctrl+M)          │  [2] Comparador de diferencias Diff (⌘⇧F12) │
│      Comodines, RegEx, Contadores, Vista │      Resaltado de líneas, Fusión, Edición   │
│                                          │                                             │
│  [3] Sincronización de carpetas (⇧F12)   │  [4] Búsqueda avanzada (Alt+F7)             │
│      Contenido/Fecha, Espejo asimétrico  │      Spotlight / Escaneo ➔ Enviar a lista   │
│                                          │                                             │
│  [5] Barra de comandos semánticos (/)    │  [6] Utilidades de archivos y seguridad     │
│      Búsqueda Spotlight, Consultas IA    │      Dividir/Unir, Checksum, Borrado seguro │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Enviar a lista] ➔ Carga los resultados en una pestaña virtual para acciones en lote │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                PAINEL DUPLO DE ARQUIVOS                                │
│          Painel esquerdo (Origem / Pasta A)            Painel direito (Destino / Pasta B)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Renomeação em lote (Ctrl+M)         │  [2] Comparador Diff lado a lado (⌘⇧F12)    │
│      Máscaras, RegEx, Contadores, Prévia │      Destaque de linhas, Mesclagem, Edição  │
│                                          │                                             │
│  [3] Sincronização de pastas (Shift+F12) │  [4] Busca avançada de arquivos (Alt+F7)    │
│      Conteúdo/Data, Espelhamento         │      Spotlight / Varredura ➔ Enviar à lista │
│                                          │                                             │
│  [5] Barra de comandos semânticos (/)    │  [6] Utilitários de arquivo e segurança     │
│      Consultas Spotlight, Intenções IA   │      Dividir/Unir, Checksum, Trituração     │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Enviar à lista] ➔ Carrega resultados em uma aba virtual para ações em lote           │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 듀얼 파일 작업 패널                                    │
│          왼쪽 패널 (원본 / 폴더 A)                     오른쪽 패널 (대상 / 폴더 B)     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] 일괄 이름 바꾸기 (Ctrl+M)           │  [2] 나란히 파일 차이 비교 (Meta+Shift+F12) │
│      토큰 마스크, 정규식, 카운터, 미리보기│      줄 단위 강조, 블록 동기화, 즉시 저장   │
│                                          │                                             │
│  [3] 디렉터리 동기화 (Shift+F12)         │  [4] 고급 파일 검색 (Alt+F7)                │
│      내용/날짜 비교, 비대칭 미러 복제    │      Spotlight / 심층 스캔 ➔ 목록으로 전달  │
│                                          │                                             │
│  [5] 자연어 시맨틱 명령줄 (/)            │  [6] 파일 유틸리티 및 보안 도구             │
│      Spotlight 메타데이터, AI 자연어 질의│      파일 분할/병합, 해시 검증, 완전 파쇄   │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [목록으로 전달] ➔ 검색 결과를 가상 탭에 모아 폴더를 넘나드는 일괄 작업을 수행합니다   │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                ДВУХПАНЕЛЬНЫЙ ИНТЕРФЕЙС                                 │
│          Левая панель (Источник / Папка A)             Правая панель (Приемник / Папка B)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Групповое переименование (Ctrl+M)   │  [2] Сравнение файлов Diff (Meta+Shift+F12) │
│      Маски, RegEx, Счетчики, Предпросмотр│      Подсветка строк, Слияние, Сохранение   │
│                                          │                                             │
│  [3] Синхронизация каталогов (Shift+F12) │  [4] Расширенный поиск файлов (Alt+F7)      │
│      Сравнение по дате/байтам, Зеркало   │      Spotlight / Сканирование ➔ В список    │
│                                          │                                             │
│  [5] Семантическая командная строка (/)  │  [6] Системные утилиты и безопасность       │
│      Запросы Spotlight, ИИ-команды       │      Разбивка/Сборка, Хеширование, Шредер   │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [В список] ➔ Передает результаты во вкладку для пакетных операций по всем папкам      │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                DOPPIO PANNELLO FILE                                    │
│          Pannello sinistro (Sorgente / A)              Pannello destro (Destinazione / B)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Ridenominazione in blocco (Ctrl+M)  │  [2] Confronto file affiancato (⌘⇧F12)      │
│      Token, RegEx, Contatori, Anteprima  │      Evidenziazione righe, Sync, Salvataggio│
│                                          │                                             │
│  [3] Sincronizzazione cartelle (Shift+F12)│ [4] Ricerca avanzata (Alt+F7)              │
│      Confronto contenuto/data, Mirror    │      Spotlight / Scansione ➔ Invia a elenco │
│                                          │                                             │
│  [5] Barra comandi semantici (/)         │  [6] Utilità file e sicurezza               │
│      Query Spotlight, Comandi IA         │      Divisione/Unione, Checksum, Triturazione│
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Invia a elenco] ➔ Raccoglie i risultati in una scheda virtuale per azioni in blocco  │
└────────────────────────────────────────────────────────────────────────────────────────┘"""
}
