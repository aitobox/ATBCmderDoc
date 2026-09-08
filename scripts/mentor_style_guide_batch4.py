#!/usr/bin/env python3
"""
scripts/mentor_style_guide_batch4.py
Localized ASCII diagrams and mentor terminology for Batch 4:
- faq_howtos.md
- download.md
- privacy_policy.md
"""

from typing import Dict

BATCH4_TERMINOLOGY_REPLACEMENTS: Dict[str, Dict[str, str]] = {
    "zh": {
        "完全磁盘访问权限": "完全磁盘访问权限",
        "操作指南与常见问题": "实用技巧与排错指引",
    },
    "zh-hant": {
        "完全磁碟訪問許可權": "完全磁碟取用權限",
        "磁碟訪問許可權": "磁碟取用權限",
        "訪問許可權": "取用權限",
        "操作指南與常見問題": "實用技巧與排錯指引",
        "分支檢視": "展開檢視",
        "指令碼": "腳本",
        "DMG 映象": "DMG 映像檔",
        "映象": "映像檔",
    },
    "ja": {
        "一括複数名前変更": "マルチ一括リネーム (Multi-Rename)",
        "実用的な現実世界のレシピ": "実践ワークフロー・クックブック",
        "アーカイブメンバー": "アーカイブ内ファイル",
        "アーカイブメンバーを編集します": "アーカイブ内のファイルを直接編集します",
        "セキュア ワイプ (細断)": "完全消去・シュレッド (Wipe)",
        "細断": "完全消去 (Wipe)",
        "トラブルシューティング ガイドと FAQ": "トラブルシューティングとよくある質問",
    },
    "de": {
        "Flacher Astblick": "Flache Verzeichnisansicht (Flat Branch View)",
        "Klassischer Commander-Schlüssel": "Klassische Commander-Taste",
        "In-Place-Bearbeitung archivieren": "Direktbearbeitung in Archiven (In-Place Edit)",
        "Archivmitglied": "Archiv-Eintrag",
        "Sicheres Löschen (Schreddern)": "Sicheres Löschen / Schreddern (Wipe)",
        "Praktische Rezepte aus der Praxis": "Praxis-Rezepte & Workflows",
    },
    "fr": {
        "Clé de commandant classique": "Touche Commander classique",
        "Vue de branche plate": "Vue arborescente plate (Flat Branch View)",
        "Archiver la modification sur place": "Édition directe dans l'archive",
        "membre de l'archive": "élément de l'archive",
        "Essuyage sécurisé (déchiquetage)": "Effacement sécurisé (Broyage définitif)",
        "Recettes pratiques du monde réel": "Recettes pratiques & cas d'usage réels",
    },
    "es": {
        "Llave de comandante clásica": "Tecla Commander clásica",
        "Vista de sucursal plana": "Vista de árbol plano (Flat Branch View)",
        "Archivar edición in situ": "Edición directa en archivo comprimido",
        "miembro del archivo": "elemento del archivo",
        "Borrado seguro (triturar)": "Borrado seguro (Wipe)",
        "Recetas prácticas del mundo real": "Recetas prácticas y flujos de trabajo",
        "Acceso directo a macOS": "Atajo de teclado en macOS",
    },
    "pt": {
        "Chave do Comandante Clássico": "Tecla Commander Clássica",
        "Vista plana da filial": "Visualização em árvore plana (Flat Branch View)",
        "Arquivar edição no local": "Edição direta no arquivo compactado",
        "membro do arquivo": "item do arquivo",
        "Limpeza segura (fragmentar)": "Exclusão segura permanente (Wipe)",
        "Receitas práticas do mundo real": "Receitas práticas e fluxos de trabalho",
    },
    "ko": {
        "내부 편집 보관": "압축 파일 내 직접 편집 (In-Place Edit)",
        "아카이브 회원을 편집합니다": "압축 파일 내 항목을 직접 편집합니다",
        "아카이브 회원": "압축 파일 내 항목",
        "보안 삭제(세단)": "안전 영구 삭제 (Wipe)",
        "실용적인 현실 세계의 조리법": "실전 워크플로 레시피",
        "실용적인 현실 세계의 레시피": "실전 워크플로 레시피",
        "클래식 커맨더 키": "클래식 커맨더 단축키",
    },
    "ru": {
        "Классический ключ командира": "Классическая клавиша Commander",
        "Плоский вид на ветку": "Плоский вид дерева (Flat Branch View)",
        "члена архива": "файл внутри архива",
        "Безопасное удаление (Уничтожить)": "Безопасное стирание (Wipe)",
        "Ярлык macOS": "Сочетание клавиш macOS",
        "Практические рецепты из реальной жизни": "Практические рецепты и готовые сценарии",
    },
    "it": {
        "Chiave del comandante classico": "Tasto Commander classico",
        "Vista ramo piatto": "Vista ad albero piatto (Flat Branch View)",
        "Modifica sul posto dell'archivio": "Modifica diretta nell'archivio",
        "membro dell'archivio": "elemento dell'archivio",
        "Cancellazione sicura (distruggi)": "Cancellazione sicura permanente (Wipe)",
        "Ricette pratiche del mondo reale": "Ricette pratiche e flussi de lavoro",
    }
}

ASCII_FAQ_ROUTING: Dict[str, str] = {
    "en": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           EVERYDAY TASK & DIAGNOSTIC ROUTER                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TASK / GOAL                               TOOL / METHOD            KEYSTROKE          │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Mirror local projects to backup       Directory Synchronizer  Shift+F12 (⇧F12)    │
│  [2] Reorganize photo libraries by date    Batch Multi-Rename Tool Ctrl+M (⌃M)         │
│  [3] Mount home/office NAS or server       Network VFS Manager     cm_ManageConnections│
│  [4] Update config file in .zip archive    Archive VFS + Lister    Enter ➔ F4 ➔ Save   │
│  [5] Reclaim disk space from nested clutter Flat Branch View       Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  ISSUE / SYMPTOM                           ROOT CAUSE              RESOLUTION          │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  "Operation not permitted" error           macOS Sandbox / TCC     cm_GrantAccess      │
│  Panels don't update external drives       FSEvents missing on FAT attr_poll_interval  │
│  Want to experiment without risk           Production XML safety   ATBCmder_test.sh    │
│  F-keys change brightness or volume        macOS hardware F-keys   Fn key or Settings  │
│  Move takes long time across drives        Cross-volume Copy+Delete Verify free space  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              日常任务与排错快速指引路由表                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  任务目标                                  推荐工具 / 方法          快捷键             │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] 将本地项目镜像备份到移动硬盘或 NAS    文件夹同步工具          Shift+F12 (⇧F12)    │
│  [2] 按拍摄日期和序号批量规整照片文件      多重批量重命名工具      Ctrl+M (⌃M)         │
│  [3] 挂载家庭/办公 NAS、网盘或云服务器     网络连接管理器          cm_ManageConnections│
│  [4] 直接修改 .zip 压缩包内的配置文件      压缩包 VFS + 编辑器     Enter ➔ F4 ➔ 保存   │
│  [5] 揪出并清理多层深处的大文件释放磁盘    扁平展开视图 / 高级搜索 Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  常见故障 / 异常现象                       根本原因                解决方案            │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  提示 "Operation not permitted" 权限错误   macOS 沙盒 / TCC 拦截   cm_GrantAccess      │
│  外接移动硬盘或 U 盘内容未自动刷新更新     FAT/exFAT 缺少内核事件 调小轮询间隔或刷新   │
│  想大胆测试配置但担心破坏原有正常设置      生产 XML 隔离保护       运行测试脚本        │
│  按 F1–F12 变成了调节屏幕亮度和音量        macOS 默认占用了媒体键 配合 Fn 键或系统设置 │
│  跨磁盘移动超大文件耗时明显变长            跨卷物理“复制+校验+删除” 确保目标空间充裕   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              日常任務與排錯快速指引路由表                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  任務目標                                  推薦工具 / 方法          快捷鍵             │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] 將本機專案鏡像備份到外接硬碟或 NAS    資料夾同步工具          Shift+F12 (⇧F12)    │
│  [2] 按拍攝日期和序號批次整理照片檔案      多重批次重新命名工具    Ctrl+M (⌃M)         │
│  [3] 掛載家庭/辦公 NAS、網盤或雲端伺服器   網路連線管理器          cm_ManageConnections│
│  [4] 直接修改 .zip 壓縮檔內的設定檔        壓縮檔 VFS + 編輯器     Enter ➔ F4 ➔ 儲存   │
│  [5] 揪出並清理多層深處的大檔案釋放磁碟    扁平展開檢視 / 進階搜尋 Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  常見故障 / 異常現象                       根本原因                解決方案            │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  提示 "Operation not permitted" 權限錯誤   macOS 沙盒 / TCC 攔截   cm_GrantAccess      │
│  外接隨身硬碟或隨身碟未自動重新整理        FAT/exFAT 缺少內核事件 調小輪詢間隔或重整   │
│  想大膽測試設定但擔心破壞原有正常設定      生產 XML 隔離保護       執行測試指令碼      │
│  按 F1–F12 變成了調節螢幕亮度和音量        macOS 預設佔用了媒體鍵 配合 Fn 鍵或系統設定 │
│  跨磁碟移動超大檔案耗时明顯變長            跨卷物理「複製+校驗+刪除」 確保目標空間充裕 │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     日常タスク＆トラブルシューティング案内ルーター                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  タスク / 目標                             推奨ツール / 手法        ショートカット     │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] プロジェクトを外付けHDD/NASへ同期     ディレクトリ同期ツール  Shift+F12 (⇧F12)    │
│  [2] 撮影日時や連番で写真の一括リネーム    マルチ一括リネーム      Ctrl+M (⌃M)         │
│  [3] 自宅・社内NASやクラウドをマウント     ネットワーク接続管理    cm_ManageConnections│
│  [4] .zip 書庫内の設定ファイルを直接編集   書庫 VFS + エディタ     Enter ➔ F4 ➔ 保存   │
│  [5] 深層の大容量ファイルを発掘・整理      フラットビュー / 検索   Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  トラブル現象 / エラー                     根本原因                解決策              │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  "Operation not permitted" 権限エラー      macOS Sandbox / TCC 制限 cm_GrantAccess     │
│  外付けドライブで自動更新が反映されない    FAT/exFAT で通知なし    ポーリング調整/更新 │
│  設定を汚さずに安全に実験したい            本番 XML 隔離保護       テストスクリプト実行│
│  F1〜F12 が音量や輝度調節になる            macOS のメディアキー    Fn併用または設定変更│
│  ドライブ間の大容量移動に時間がかかる      物理「コピー+検証+削除」 空き容量の事前確認 │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                    ALLTÄGLICHE AUFGABEN & FEHLERBEHEBUNG-LEITFADEN                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  AUFGABE / ZIEL                            WERKZEUG / METHODE       TASTENKÜRZEL       │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Lokale Projekte auf NAS/HDD spiegeln  Verzeichnissynchronisation Shift+F12 (⇧F12) │
│  [2] Fotobibliotheken nach Datum umbenennen Multi-Umbennungs-Tool  Ctrl+M (⌃M)         │
│  [3] NAS oder Server im Netzwerk einbinden Netzwerk-VFS-Manager    cm_ManageConnections│
│  [4] Konfig in .zip direkt bearbeiten      Archiv-VFS + Editor     Enter ➔ F4 ➔ Save   │
│  [5] Tiefe Speicherfresser aufspüren       Flache Zweigansicht     Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLEM / SYMPTOM                         URSACHE                 LÖSUNG              │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Fehler "Operation not permitted"          macOS-Sandbox / TCC     cm_GrantAccess      │
│  Externe Laufwerke nicht aktuell           Keine FSEvents auf FAT attr_poll_interval   │
│  Risikofrei Konfigurationen testen         Produktions-XML-Schutz ATBCmder_test.sh     │
│  F-Tasten regeln Systemfunktionen          macOS-Medientasten      Fn-Taste / Settings │
│  Verschieben über Laufwerke träge          Kopieren + Löschen      Freien Platz prüfen │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌────────────────────────────────────────────────────────────────────────────────────────┐
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
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                 ENRUTADOR DE TAREAS DIARIAS Y RESOLUCIÓN DE PROBLEMAS                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TAREA / OBJETIVO                          HERRAMIENTA / MÉTODO     ATAJO              │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Sincronizar proyectos a NAS o disco ext. Sincronizador carpetas Shift+F12 (⇧F12)  │
│  [2] Renombrar fotos por fecha y lote      Renombrado múltiple     Ctrl+M (⌃M)         │
│  [3] Montar NAS, servidor o nube           Gestor VFS de red       cm_ManageConnections│
│  [4] Editar archivos dentro de .zip        VFS archivos + Editor   Enter ➔ F4 ➔ Guardar│
│  [5] Hallar archivos grandes anidados      Vista plana             Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLEMA / SÍNTOMA                        CAUSA RAÍZ              RESOLUCIÓN          │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Error "Operation not permitted"           Sandbox de macOS / TCC cm_GrantAccess       │
│  Discos externos no se actualizan solos    Sin FSEvents en FAT/exFAT attr_poll_interval│
│  Probar ajustes sin riesgo alguno          Protección XML producción ATBCmder_test.sh  │
│  Teclas F cambian brillo o volumen         Teclas multimedia macOS Tecla Fn o Ajustes  │
│  Mover entre volúmenes tarda bastante      Copia física + Borrado Verificar espacio    │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  ROTEADOR DE TAREFAS DIÁRIAS E RESOLUÇÃO DE PROBLEMAS                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TAREFA / OBJETIVO                         FERRAMENTA / MÉTODO      ATALHO             │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Espelhar projetos para backup/NAS     Sincronizador de pastas Shift+F12 (⇧F12)    │
│  [2] Reorganizar fotos por data em lote    Renomeação múltipla     Ctrl+M (⌃M)         │
│  [3] Montar NAS, servidor ou nuvem         Gerenciador VFS de rede cm_ManageConnections│
│  [4] Editar arquivo dentro de um .zip      VFS de arquivos + Editor Enter ➔ F4 ➔ Salvar│
│  [5] Encontrar arquivos grandes aninhados  Visualização plana      Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLEMA / SINTOMA                        CAUSA RAIZ              RESOLUÇÃO           │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Erro "Operation not permitted"            Sandbox do macOS / TCC cm_GrantAccess       │
│  Discos externos não atualizam sozinhos    FSEvents ausente no FAT attr_poll_interval  │
│  Testar configurações sem riscos           Proteção do XML original ATBCmder_test.sh   │
│  Teclas F mudam brilho ou volume           Teclas de mídia do macOS Tecla Fn ou Ajustes│
│  Mover entre volumes demora muito          Cópia física + Exclusão Checar espaço livre │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                       일상 업무 및 문제 해결 빠른 가이드 라우터                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  작업 목표                                 추천 도구 / 방법         단축키             │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] 로컬 프로젝트를 외장하드/NAS로 동기화 폴더 동기화 도구        Shift+F12 (⇧F12)    │
│  [2] 촬영 날짜별 사진 대량 일괄 이름 변경  다중 일괄 이름 변경     Ctrl+M (⌃M)         │
│  [3] 가정/사무실 NAS 및 원격 서버 마운트   네트워크 연결 관리자    cm_ManageConnections│
│  [4] .zip 압축 해제 없이 설정 파일 직접 수정 압축 VFS + 에디터     Enter ➔ F4 ➔ 저장   │
│  [5] 깊숙한 대용량 파일 발굴 및 디스크 정리 플랫 브랜치 뷰 / 검색  Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  문제 현상 / 오류                          근본 원인               해결 방법           │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  "Operation not permitted" 권한 오류       macOS 샌드박스 / TCC 차단 cm_GrantAccess    │
│  외장 드라이브 내용이 자동 갱신 안 됨      FAT 파일시스템 한계     폴링 조정 또는 갱신 │
│  기존 설정 손상 없이 안전하게 테스트       운영 XML 격리 보호      테스트 스크립트 실행│
│  F1~F12 키가 음량이나 밝기 조절            macOS 기본 미디어 키    Fn 키 병용 또는 설정│
│  드라이브 간 대용량 이동 시간 지연         볼륨 간 복사+검증+삭제 여유 공간 사전 확인  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   МАРШРУТИЗАТОР ПОВСЕДНЕВНЫХ ЗАДАЧ И РЕШЕНИЯ ПРОБЛЕМ                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  ЗАДАЧА / ЦЕЛЬ                             ИНСТРУМЕНТ / МЕТОД       ГОРЯЧАЯ КЛАВИША    │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Синхронизация проектов с бэкапом/NAS  Синхронизация каталогов Shift+F12 (⇧F12)    │
│  [2] Пакетное переименование фото по дате  Групповое переименование Ctrl+M (⌃M)        │
│  [3] Подключение офисного/домашнего NAS    Менеджер сетевых VFS    cm_ManageConnections│
│  [4] Правка файла в архиве .zip            Архивный VFS            Enter ➔ F4 ➔ Save   │
│  [5] Поиск тяжелых файлов в глубине        Плоский вид (Branch)    Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  ПРОБЛЕМА / СИМПТОМ                        ПРИЧИНА                 РЕШЕНИЕ             │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Ошибка "Operation not permitted"          Песочница macOS / TCC   cm_GrantAccess      │
│  Внешние диски не обновляются сами         Нет FSEvents на FAT/exFAT attr_poll_interval│
│  Безопасное тестирование настроек          Защита рабочего XML     ATBCmder_test.sh    │
│  F-клавиши меняют звук/яркость             Медиа-клавиши macOS     Fn или Настройки    │
│  Долгое перемещение между дисками          Копирование + удаление Проверить свободное  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  ROUTER DI ATTIVITÀ QUOTIDIANE E RISOLUZIONE PROBLEMI                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  ATTIVITÀ / OBIETTIVO                      STRUMENTO / METODO       SCORCIATOIA        │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Sincronizzare progetti su NAS/backup  Sincronizzazione cartelle Shift+F12 (⇧F12)  │
│  [2] Riorganizzare foto per data in blocco Rinomina multipla       Ctrl+M (⌃M)         │
│  [3] Montare NAS o server aziendale        Gestore VFS di rete     cm_ManageConnections│
│  [4] Modificare file dentro un archivio .zip VFS archivi + Editor  Enter ➔ F4 ➔ Salva  │
│  [5] Trovare file pesanti annidati         Vista piatta (Branch)   Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLEMA / SINTOMO                        CAUSA PRINCIPALE        RISOLUZIONE         │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Errore "Operation not permitted"          Sandbox di macOS / TCC cm_GrantAccess       │
│  Dischi esterni non si aggiornano da soli  FSEvents assente su FAT attr_poll_interval  │
│  Provare configurazioni senza rischi       Protezione XML originale ATBCmder_test.sh   │
│  I tasti F regolano volume o luminosità    Tasti multimediali Mac Tasto Fn / Opzioni   │
│  Spostamento lento tra dischi diversi      Copia + Cancellazione   Verifica spazio     │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

}

ASCII_FAQ_GRANT_ACCESS: Dict[str, str] = {
    "en": """┌─────────────────────────────────────────────────────────────┐
│  Grant Filesystem Access                                [x] │
├─────────────────────────────────────────────────────────────┤
│  Because this version of ATBCmder runs inside a secure      │
│  macOS Sandbox, it needs your permission to access          │
│  critical folders.                                          │
│                                                             │
│  [  Grant Access to Root Directory (/)  ]                   │
│                                                             │
│  [  Grant Access to External Disks (/Volumes)  ]            │
│                                                             │
│  [  Open Full Disk Access Settings…  ]                      │
│                                                             │
│  Root directory access is required by the App Sandbox.      │
│  Full Disk Access is a separate macOS permission for        │
│  protected user data.                                       │
│                                                   [ Done ]  │
└─────────────────────────────────────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────┐
│  授予磁盘读写权限 (Grant Filesystem Access)             [x] │
├─────────────────────────────────────────────────────────────┤
│  为了确保系统安全，本版本 ATBCmder 运行在 macOS 沙盒环境中。│
│  需要您的明确授权才能正常读写系统关键文件夹与外置驱动器。   │
│                                                             │
│  [  授予根目录读写权限 (/)  ]                               │
│                                                             │
│  [  授予外接磁盘读写权限 (/Volumes)  ]                      │
│                                                             │
│  [  打开系统完全磁盘访问权限设置…  ]                        │
│                                                             │
│  根目录授权是 App 沙盒正常工作的基本要求。                  │
│  完全磁盘访问权限是针对受保护用户数据的额外系统设置。       │
│                                                   [ 完成 ]  │
└─────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────┐
│  授予磁碟讀寫權限 (Grant Filesystem Access)             [x] │
├─────────────────────────────────────────────────────────────┤
│  為了確保系統安全，本版本 ATBCmder 運行在 macOS 沙盒環境中。│
│  需要您的明確授權才能正常讀寫系統關鍵資料夾與外接磁碟。     │
│                                                             │
│  [  授予根目錄讀寫權限 (/)  ]                               │
│                                                             │
│  [  授予外接磁碟讀寫權限 (/Volumes)  ]                      │
│                                                             │
│  [  打開系統完整磁碟取用權限設定…  ]                        │
│                                                             │
│  根目錄授權是 App 沙盒正常工作的基本要求。                  │
│  完整磁碟取用權限是針對受保護使用者資料的額外系統設定。     │
│                                                   [ 完成 ]  │
└─────────────────────────────────────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────┐
│  ファイルアクセス許可 (Grant Filesystem Access)         [x] │
├─────────────────────────────────────────────────────────────┤
│  安全確保のため ATBCmder は macOS Sandbox 内で動作します。  │
│  重要フォルダと外付けドライブへのアクセス許可が必要です。   │
│                                                             │
│  [  ルートディレクトリ (/) へのアクセスを許可  ]            │
│                                                             │
│  [  外付けディスク (/Volumes) へのアクセスを許可  ]         │
│                                                             │
│  [  フルディスクアクセス設定を開く…  ]                      │
│                                                             │
│  ルートアクセスは App Sandbox の基本要件です。              │
│  フルディスクアクセスは保護された個人データ用の権限です。   │
│                                                   [ 完了 ]  │
└─────────────────────────────────────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────┐
│  Dateisystemzugriff gewähren (Filesystem Access)        [x] │
├─────────────────────────────────────────────────────────────┤
│  Da ATBCmder in sicherer macOS-Sandbox ausgeführt wird,     │
│  benötigt es Ihre Erlaubnis für den Zugriff auf wichtige    │
│  Systemordner und externe Laufwerke.                        │
│                                                             │
│  [  Zugriff auf Stammverzeichnis (/) gewähren  ]            │
│                                                             │
│  [  Zugriff auf externe Laufwerke (/Volumes) gewähren  ]    │
│                                                             │
│  [  Festplattenvollzugriff-Einstellungen öffnen…  ]         │
│                                                             │
│  Stammverzeichnis-Zugriff wird von der Sandbox benötigt.    │
│  Festplattenvollzugriff schützt sensible Benutzerdaten.     │
│                                                 [ Fertig ]  │
└─────────────────────────────────────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────┐
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
└─────────────────────────────────────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────┐
│  Conceder acceso al sistema (Filesystem Access)         [x] │
├─────────────────────────────────────────────────────────────┤
│  Dado que ATBCmder opera en una Sandbox segura de macOS,    │
│  requiere su autorización expresa para acceder a carpetas   │
│  críticas y discos externos.                                │
│                                                             │
│  [  Conceder acceso al directorio raíz (/)  ]               │
│                                                             │
│  [  Conceder acceso a discos externos (/Volumes)  ]         │
│                                                             │
│  [  Abrir ajustes de Acceso total al disco…  ]              │
│                                                             │
│  El acceso a la raíz es requerido por la Sandbox.           │
│  Acceso total al disco protege los datos privados.          │
│                                                  [ Listo ]  │
└─────────────────────────────────────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────┐
│  Conceder Acesso ao Disco (Filesystem Access)           [x] │
├─────────────────────────────────────────────────────────────┤
│  Como o ATBCmder executa na Sandbox segura do macOS, ele    │
│  precisa de sua autorização para ler e gravar em pastas     │
│  críticas e discos externos.                                │
│                                                             │
│  [  Conceder acesso ao diretório raiz (/)  ]                │
│                                                             │
│  [  Conceder acesso a discos externos (/Volumes)  ]         │
│                                                             │
│  [  Abrir Ajustes de Acesso Total ao Disco…  ]              │
│                                                             │
│  O acesso à raiz é exigido pela Sandbox do aplicativo.      │
│  O Acesso Total ao Disco protege dados pessoais seguros.    │
│                                              [ Concluído ]  │
└─────────────────────────────────────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────┐
│  파일 시스템 접근 권한 허용 (Filesystem Access)         [x] │
├─────────────────────────────────────────────────────────────┤
│  ATBCmder는 macOS 샌드박스 보안 환경에서 실행되므로,        │
│  핵심 시스템 폴더 및 외장 드라이브 접근에 대한              │
│  사용자의 명시적 승인이 필요합니다.                         │
│                                                             │
│  [  루트 디렉토리 (/) 접근 권한 허용  ]                     │
│                                                             │
│  [  외장 디스크 (/Volumes) 접근 권한 허용  ]                │
│                                                             │
│  [  전체 디스크 접근 권한 설정 열기…  ]                     │
│                                                             │
│  루트 접근 승인은 앱 샌드박스 구동에 필수입니다.            │
│  전체 디스크 접근 권한은 사용자 데이터를 보호합니다.        │
│                                                   [ 완료 ]  │
└─────────────────────────────────────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────┐
│  Предоставить доступ к диску (Filesystem Access)        [x] │
├─────────────────────────────────────────────────────────────┤
│  Так как ATBCmder работает в изолированной песочнице macOS, │
│  требуется ваше разрешение для доступа к системным папкам   │
│  и внешним накопителям.                                     │
│                                                             │
│  [  Предоставить доступ к корню (/)  ]                      │
│                                                             │
│  [  Предоставить доступ к дискам (/Volumes)  ]              │
│                                                             │
│  [  Открыть настройки полного доступа к диску…  ]           │
│                                                             │
│  Доступ к корню обязателен для песочницы приложения.        │
│  Полный доступ к диску защищает личные данные.              │
│                                                 [ Готово ]  │
└─────────────────────────────────────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────┐
│  Accesso al File System (Filesystem Access)             [x] │
├─────────────────────────────────────────────────────────────┤
│  Poiché ATBCmder opera in una Sandbox sicura di macOS,      │
│  richiede la tua autorizzazione per gestire cartelle di     │
│  sistema e volumi esterni.                                  │
│                                                             │
│  [  Concedi accesso alla directory principale (/)  ]        │
│                                                             │
│  [  Concedi accesso ai dischi esterni (/Volumes)  ]         │
│                                                             │
│  [  Apri impostazioni Accesso completo al disco…  ]         │
│                                                             │
│  L'accesso alla root è richiesto dalla Sandbox dell'app.    │
│  Accesso completo protegge i dati utente riservati.         │
│                                                   [ Fine ]  │
└─────────────────────────────────────────────────────────────┘""",

}

ASCII_FAQ_FUNCTION_KEYS: Dict[str, str] = {
    "en": """┌─────────────────────────────────────────────────────────────┐
│  Keyboard Shortcuts                                         │
├──────────────────────────────┬──────────────────────────────┤
│  Keyboard Navigation         │  Use F1, F2, etc. keys as    │
│  Modifier Keys               │  standard function keys  [ON]│
│  Function Keys          ◄─── │                              │
│  Spotlight                   │  When this option is on,     │
│  Mission Control             │  press the Fn key to use the │
│  App Shortcuts               │  special features printed    │
│                              │  on each key.                │
│                              │                     [ Done ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "zh": """┌─────────────────────────────────────────────────────────────┐
│  键盘快捷键                                                 │
├──────────────────────────────┬──────────────────────────────┤
│  键盘导览                    │  将 F1、F2 等键用作          │
│  修饰键                      │  标准功能键             [开] │
│  功能键                ◄───  │                              │
│  聚焦 (Spotlight)            │  开启此选项后，按住 Fn 键    │
│  调度中心                    │  可使用印在各键上的          │
│  App 快捷键                  │  特殊多媒体功能。            │
│                              │                              │
│                              │                     [ 完成 ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "zh-hant": """┌─────────────────────────────────────────────────────────────┐
│  鍵盤快速鍵                                                 │
├──────────────────────────────┬──────────────────────────────┤
│  鍵盤導覽                    │  將 F1、F2 等鍵用作          │
│  按鍵修飾鍵                  │  標準功能鍵             [開] │
│  功能鍵                ◄───  │                              │
│  聚焦 (Spotlight)            │  開啟此選項後，按住 Fn 鍵    │
│  指揮中心 (Mission)          │  可使用印在各鍵上的          │
│  App 快速鍵                  │  特殊多媒體功能。            │
│                              │                              │
│                              │                     [ 完成 ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "ja": """┌─────────────────────────────────────────────────────────────┐
│  キーボードショートカット                                   │
├──────────────────────────────┬──────────────────────────────┤
│  キーボードナビゲーション    │  F1、F2 などのキーを         │
│  修飾キー                    │  標準機能キーとして使用  [入]│
│  ファンクションキー     ◄─── │                              │
│  Spotlight                   │  このオプションがオンの時は  │
│  Mission Control             │  Fn キーを押して印字された   │
│  アプリケーション            │  特殊機能を使用します。      │
│                              │                              │
│                              │                     [ 完了 ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "de": """┌─────────────────────────────────────────────────────────────┐
│  Tastaturkurzbefehle                                        │
├──────────────────────────────┬──────────────────────────────┤
│  Tastaturnavigation          │  Die Tasten F1, F2 usw. als  │
│  Sondertasten                │  Standard-Tasten nutzen [EIN]│
│  Funktionstasten        ◄─── │                              │
│  Spotlight                   │  Wenn diese Option aktiv ist,│
│  Mission Control             │  drücken Sie die Fn-Taste,   │
│  App-Kurzbefehle             │  um die aufgedruckten Sonder-│
│                              │  funktionen zu nutzen.       │
│                              │                   [ Fertig ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "fr": """┌─────────────────────────────────────────────────────────────┐
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
└──────────────────────────────┴──────────────────────────────┘""",

    "es": """┌─────────────────────────────────────────────────────────────┐
│  Atajos de teclado                                          │
├──────────────────────────────┬──────────────────────────────┤
│  Navegación por teclado      │  Usar teclas F1, F2 como     │
│  Teclas de modificación      │  función estándar        [SÍ]│
│  Teclas de función      ◄─── │                              │
│  Spotlight                   │  Con esta opción activa,     │
│  Mission Control             │  pulse Fn para usar las      │
│  Atajos de la app            │  funciones especiales        │
│                              │  impresas en cada tecla.     │
│                              │                    [ Listo ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "pt": """┌─────────────────────────────────────────────────────────────┐
│  Atalhos de Teclado                                         │
├──────────────────────────────┬──────────────────────────────┤
│  Navegação por Teclado       │  Usar teclas F1, F2, etc.    │
│  Teclas Modificadoras        │  como tecla padrão      [SIM]│
│  Teclas de Função       ◄─── │                              │
│  Spotlight                   │  Com esta opção ativada,     │
│  Mission Control             │  pressione a tecla Fn para   │
│  Atalhos de Aplicativos      │  usar os recursos impressos  │
│                              │  em cada tecla.              │
│                              │                [ Concluído ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "ko": """┌─────────────────────────────────────────────────────────────┐
│  키보드 단축키                                              │
├──────────────────────────────┬──────────────────────────────┤
│  키보드 내비게이션           │  F1, F2 등의 키를 표준       │
│  보조 키                     │  기능 키로 사용          [켬]│
│  기능 키               ◄───  │                              │
│  Spotlight                   │  옵션 활성화 시 Fn 키를 눌러 │
│  Mission Control             │  눌러 각 키에 인쇄된 특수    │
│  앱 단축키                   │  동작을 실행합니다.          │
│                              │                              │
│                              │                     [ 완료 ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "ru": """┌─────────────────────────────────────────────────────────────┐
│  Сочетания клавиш                                           │
├──────────────────────────────┬──────────────────────────────┤
│  Навигация с клавиатуры      │  Использовать F1, F2 как     │
│  Клавиши модификаторы        │  стандартные клавиши    [ВКЛ]│
│  Функциональные клавиши ◄─── │                              │
│  Spotlight                   │  Если этот параметр включен, │
│  Mission Control             │  нажмите клавишу Fn для      │
│  Сочетания клавиш apps       │  специальных медиа-функций   │
│                              │  на каждой клавише.          │
│                              │                   [ Готово ] │
└──────────────────────────────┴──────────────────────────────┘""",

    "it": """┌─────────────────────────────────────────────────────────────┐
│  Abbreviazioni da tastiera                                  │
├──────────────────────────────┬──────────────────────────────┤
│  Navigazione da tastiera     │  Usa i tasti F1, F2 come     │
│  Tasti modificatori          │  tasti funzione standard [SÌ]│
│  Tasti funzione         ◄─── │                              │
│  Spotlight                   │  Quando è attiva, premi il   │
│  Mission Control             │  tasto Fn per usare le       │
│  Abbreviazioni app           │  funzioni speciali stampate  │
│                              │  su ciascun tasto.           │
│                              │                     [ Fine ] │
└──────────────────────────────┴──────────────────────────────┘""",

}

ASCII_FAQ_INTRA_VOLUME: Dict[str, str] = {
    "en": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           INTRA-VOLUME MOVE (SAME PARTITION)                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso   ➔ Target: /Users/brain/Movies/          │
│                                                                                        │
│   1. POSIX rename() system call updates filesystem inode directory table.              │
│   2. Physical data blocks on the SSD are NEVER touched or copied.                      │
│   3. Execution time: < 5 milliseconds. Free disk space required: 0 bytes.              │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             同物理分区内移动（毫秒级完成）                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   源路径: /Users/brain/Downloads/BigFile.iso   ➔ 目标路径: /Users/brain/Movies/        │
│                                                                                        │
│   1. 发起 POSIX rename() 原子系统调用，仅仅修改文件系统目录树中的指针记录。            │
│   2. SSD 固态硬盘上存储的真实数据块完全不需要物理读写或迁移。                          │
│   3. 耗时：小于 5 毫秒。额外磁盘可用空间需求：0 字节。                                 │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             同物理分區內移動（毫秒級完成）                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   來源: /Users/brain/Downloads/BigFile.iso ➔ 目標: /Users/brain/Movies/                │
│                                                                                        │
│   1. 發起 POSIX rename() 原子系統呼叫，僅僅修改檔案系統目錄樹中的指標紀錄。            │
│   2. SSD 固態硬碟上儲存的真實資料塊完全不需要物理讀寫或搬移。                          │
│   3. 耗時：小於 5 毫秒。額外磁碟可用空間需求：0 位元組。                               │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      同一パーティション内の移動（ミリ秒級で完了）                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   移動元: /Users/brain/Downloads/BigFile.iso ➔ 移動先: /Users/brain/Movies/            │
│                                                                                        │
│   1. POSIX rename() システムコールでファイルシステムの i-node 目録のみを更新。         │
│   2. SSD 上の実際の物理データブロックには一切読み書きも複製も発生しません。            │
│   3. 所要時間: 5 ミリ秒未満。必要な追加ディスク容量: 0 バイト。                        │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                VERSCHIEBEN AUF GLEICHEM VOLUME (MILLISEKUNDEN-SCHNELL)                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Quelle: /Users/brain/Downloads/BigFile.iso ➔ Ziel: /Users/brain/Movies/              │
│                                                                                        │
│   1. POSIX rename() aktualisiert lediglich den Inode-Verzeichniseintrag im Dateisystem.│
│   2. Physische Datenblöcke auf der SSD werden WEDER gelesen noch kopiert.              │
│   3. Ausführungszeit: < 5 Millisekunden. Erforderlicher freier Speicher: 0 Bytes.      │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   DÉPLACEMENT SUR LE MÊME VOLUME (EN MILLISECONDES)                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso ➔ Cible: /Users/brain/Movies/             │
│                                                                                        │
│   1. L'appel système POSIX rename() met simplement à jour l'entrée d'inode du système. │
│   2. Les blocs de données physiques sur le SSD ne sont JAMAIS lus ni copiés.           │
│   3. Temps d'exécution : < 5 ms. Espace disque supplémentaire requis : 0 octet.        │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      MOVER EN EL MISMO VOLUMEN (EN MILISEGUNDOS)                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origen: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Users/brain/Movies/           │
│                                                                                        │
│   1. La llamada POSIX rename() solo actualiza la tabla de inodos del directorio.       │
│   2. Los bloques de datos físicos en el SSD NUNCA se leen ni se copian.                │
│   3. Tiempo de ejecución: < 5 milisegundos. Espacio libre requerido: 0 bytes.          │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        MOVER NO MESMO VOLUME (EM MILISSEGUNDOS)                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origem: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Users/brain/Movies/           │
│                                                                                        │
│   1. A chamada de sistema POSIX rename() apenas atualiza o registro do inode.          │
│   2. Os blocos de dados físicos no SSD NUNCA são lidos ou copiados.                    │
│   3. Tempo de execução: < 5 milissegundos. Espaço livre necessário: 0 bytes.           │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  동일 볼륨 파티션 내 파일 이동 (밀리초 내 즉각 완료)                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   원본: /Users/brain/Downloads/BigFile.iso ➔ 대상: /Users/brain/Movies/                │
│                                                                                        │
│   1. POSIX rename() 원자적 시스템 호출이 파일시스템 inode 디렉토리 포인터만 갱신.      │
│   2. SSD에 기록된 실제 데이터 블록은 물리적으로 전혀 복사되거나 읽히지 않습니다.       │
│   3. 소요 시간: 5 밀리초 미만. 추가로 요구되는 디스크 여유 공간: 0 바이트.             │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     ПЕРЕМЕЩЕНИЕ В ПРЕДЕЛАХ ОДНОГО ТОМА (МГНОВЕННО)                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Источник: /Users/brain/Downloads/BigFile.iso ➔ Цель: /Users/brain/Movies/            │
│                                                                                        │
│   1. Вызов POSIX rename() лишь обновляет запись inode в файловой системе.              │
│   2. Физические блоки данных на SSD НИКОГДА не считываются и не копируются повторно.   │
│   3. Время выполнения: < 5 миллисекунд. Требуемое свободное место: 0 байт.             │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   SPOSTAMENTO SULLO STESSO VOLUME (IN MILLISECONDI)                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Sorgente: /Users/brain/Downloads/BigFile.iso ➔ Target: /Users/brain/Movies/          │
│                                                                                        │
│   1. La chiamata POSIX rename() aggiorna solo la tabella degli inode nel file system.  │
│   2. I blocchi fisici di dati sull'SSD NON vengono MAI letti o copiati.                │
│   3. Tempo di esecuzione: < 5 millisecondi. Spazio libero su disco richiesto: 0 byte.  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

}

ASCII_FAQ_CROSS_VOLUME: Dict[str, str] = {
    "en": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           CROSS-VOLUME MOVE (ACROSS DRIVES)                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso   ➔ Target: /Volumes/ExternalSSD/Movie/   │
│                                                                                        │
│   Stage 1: Binary Stream Copy (Read from Source SSD ➔ Write to Target External SSD)    │
│   Stage 2: Verification and Flush (fsync ensures complete write to external media)     │
│   Stage 3: Source Deletion (Source file is unlinked only after Stage 2 succeeds)       │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                            跨物理磁盘分区移动（物理流水线）                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   源路径: /Users/brain/Downloads/BigFile.iso   ➔ 目标路径: /Volumes/ExternalSSD/Movie/ │
│                                                                                        │
│   阶段 1: 二进制数据流拷贝（从内置固态硬盘流式读出 ➔ 写入外接移动硬盘）                │
│   阶段 2: 完整性核对与磁盘落盘刷盘 (fsync 确保外接设备物理写入完成)                    │
│   阶段 3: 安全移除源文件（只有当阶段 2 验证无误后，才解除源文件占用）                  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "zh-hant": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             跨物理磁碟分區移動（物理管線）                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   來源: /Users/brain/Downloads/BigFile.iso ➔ 目標: /Volumes/ExternalSSD/Movie/         │
│                                                                                        │
│   階段 1: 二進位資料流複製（從內建固態硬碟串流讀出 ➔ 寫入外接隨身硬碟）                │
│   階段 2: 完整性核對與磁碟刷盤 (fsync 確保外接設備物理寫入完成)                        │
│   階段 3: 安全移除來源檔案（只有當階段 2 驗證無誤後，才解除來源檔案占用）              │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ja": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                       異なるドライブ間の移動（物理パイプライン）                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   移動元: /Users/brain/Downloads/BigFile.iso ➔ 移動先: /Volumes/ExternalSSD/Movie/     │
│                                                                                        │
│   フェーズ 1: バイナリストリームコピー（内蔵 SSD から読み出し ➔ 外付け SSD へ書き込み）│
│   フェーズ 2: 整合性検証とフラッシュ (fsync により外付け媒体への物理書き込みを保証)    │
│   フェーズ 3: 安全な元ファイル削除（フェーズ 2 の検証成功後にのみ元ファイルを削除）    │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "de": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  LAUFWERKSÜBERGREIFENDES VERSCHIEBEN (DATENPIPELINE)                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Quelle: /Users/brain/Downloads/BigFile.iso ➔ Ziel: /Volumes/ExternalSSD/Movie/       │
│                                                                                        │
│   Phase 1: Binärer Stream-Transfer (Interne SSD lesen ➔ Auf externes Medium schreiben) │
│   Phase 2: Verifikation & Flush (fsync sichert vollständiges Schreiben)                │
│   Phase 3: Sicheres Löschen (Quelldatei wird erst nach Stufe 2 gelöscht)               │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "fr": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     DÉPLACEMENT ENTRE DEUX VOLUMES (FLUX PHYSIQUE)                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso ➔ Cible: /Volumes/ExternalSSD/Movie/      │
│                                                                                        │
│   Étape 1 : Copie du flux binaire (Lecture SSD interne ➔ Écriture SSD externe)         │
│   Étape 2 : Vérification et vidage (fsync garantit l'écriture physique complète)       │
│   Étape 3 : Suppression sécurisée de la source (le fichier source n'est délié qu'après)│
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "es": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   MOVER ENTRE VOLÚMENES DIFERENTES (FLUJO DE DATOS)                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origen: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Volumes/ExternalSSD/Movie/    │
│                                                                                        │
│   Fase 1: Copia de flujo binario (Lectura del SSD interno ➔ Escritura en SSD externo)  │
│   Fase 2: Verificación y volcado (fsync garantiza la escritura física en el medio)     │
│   Fase 3: Eliminación segura del origen (el archivo origen se borra solo tras el éxito)│
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "pt": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     MOVER ENTRE VOLUMES DIFERENTES (FLUXO FÍSICO)                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origem: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Volumes/ExternalSSD/Movie/    │
│                                                                                        │
│   Etapa 1: Cópia do fluxo binário (Leitura do SSD interno ➔ Gravação no SSD externo)   │
│   Etapa 2: Verificação e gravação física (fsync garante a gravação completa na mídia)  │
│   Etapa 3: Exclusão segura da origem (o arquivo original só é removido após sucesso)   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ko": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  다른 물리 드라이브 간 이동 (물리적 파이프라인 단계)                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   원본: /Users/brain/Downloads/BigFile.iso ➔ 대상: /Volumes/ExternalSSD/Movie/         │
│                                                                                        │
│   1단계: 바이너리 스트림 복사 (내장 SSD에서 스트리밍 읽기 ➔ 외장 SSD로 직접 쓰기)      │
│   2단계: 무결성 검증 및 디스크 플러시 (fsync를 통해 외장 매체에 물리적 쓰기 완료 보장) │
│   3단계: 원본 파일 안전 삭제 (2단계가 완벽하게 성공한 후에만 원본 연결 해제)           │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "ru": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      ПЕРЕМЕЩЕНИЕ МЕЖДУ ДИСКАМИ (КОНВЕЙЕР ДАННЫХ)                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Источник: /Users/brain/Downloads/BigFile.iso ➔ Цель: /Volumes/ExternalSSD/Movie/     │
│                                                                                        │
│   Этап 1: Потоковое копирование (Чтение с SSD ➔ Запись на внешний SSD)                 │
│   Этап 2: Проверка целостности и сброс (fsync гарантирует завершение физической записи)│
│   Этап 3: Безопасное удаление источника (Исходный файл удаляется только после Этапа 2) │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

    "it": """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     SPOSTAMENTO TRA VOLUMI DIVERSI (PIPELINE DATI)                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Sorgente: /Users/brain/Downloads/BigFile.iso ➔ Target: /Volumes/ExternalSSD/Movie/   │
│                                                                                        │
│   Fase 1: Copia flusso binario (Lettura da SSD interno ➔ Scrittura su SSD externo)     │
│   Fase 2: Verifica e flush su disco (fsync garantisce la scrittura fisica completa)    │
│   Fase 3: Eliminazione sicura sorgente (il file sorgente viene rimosso solo dopo)      │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘""",

}
