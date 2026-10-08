import json
import os

I18N_DIR = "landing/i18n"

fixes = {
    "zh": {
        "btn_user_guide": "用户指南",
        "btn_contact": "联系支持",
        "hero_btn_guide": "用户指南",
        "conversion_btn_guide": "用户指南",
        "t1_tab_tree_views": "左右独立目录树",
        "theme1_badge_3": "[Alt+F1/F2] 磁盘与卷宗快速切换",
        "theme2_title": "告别繁重的独立应用。一键极速预览 Retina 高清大图、文档与音视频。",
        "hero_badge_1": "⚡ 100% 纯键盘驱动 · 双手无需离开主键盘区",
        "theme4_title": "洞察每一 GB 空间。全盘容量全景透视、应用深度清理与精准同步。",
        "theme4_badge_2": "深入根除残留缓存与配置文件",
        "theme1_badge_2": "[Cmd+B] 一键平铺所有嵌套子目录",
        "theme2_badge_1": "[Cmd+Q / 空格] 100ms 极速防抖预览",
        "theme4_badge_1": "毫秒级全盘大文件极速扫描",
        "hero_title_h1": "两个面板，告别鼠标。",
        "hero_title_h2": "重新将 Mac 文件系统完全掌控于指尖",
        "t4_tab_app_uninstaller": "应用深度卸载"
    },
    "zh-hant": {
        "btn_user_guide": "使用指南",
        "btn_contact": "聯絡我們",
        "hero_btn_guide": "使用指南",
        "conversion_btn_guide": "使用指南",
        "t1_tab_tree_views": "左右獨立目錄樹",
        "theme1_badge_3": "[Alt+F1/F2] 磁碟與卷宗快速切換",
        "theme2_title": "告別繁重的獨立 App。一鍵極速預覽 Retina 高畫質圖片、文件與影音。",
        "hero_badge_1": "⚡ 100% 純鍵盤驅動 · 雙手無需離開主鍵盤區",
        "theme4_title": "洞察每一 GB 容量。全盤空間全景透視、App 深度移除與精準同步。",
        "theme4_badge_2": "深入根除殘留快取與設定檔",
        "theme1_badge_2": "[Cmd+B] 一鍵平鋪所有巢狀子目錄",
        "theme2_badge_1": "[Cmd+Q / 空白鍵] 100ms 極速防抖預覽",
        "theme4_badge_1": "毫秒級全盤大檔案極速掃描",
        "hero_title_h1": "兩個面板，告別滑鼠。",
        "hero_title_h2": "重新將 Mac 檔案系統完全掌控於指尖",
        "t4_tab_app_uninstaller": "App 深度徹底移除"
    },
    "ja": {
        "btn_user_guide": "ユーザーガイド",
        "btn_contact": "お問い合わせ",
        "hero_btn_guide": "ユーザーガイド",
        "conversion_btn_guide": "ユーザーガイド",
        "t1_tab_tree_views": "左右独立ディレクトリツリー",
        "theme1_badge_3": "[Alt+F1/F2] ドライブ＆ボリュームの高速切り替え",
        "theme2_title": "重い個別アプリの起動は不要。キーを叩くだけで、Retina高精細画像・文書・メディアが瞬時に展開。",
        "hero_badge_1": "⚡ 100% キーボード操作 · ホームポジションから手を離さずに完了",
        "theme4_title": "ストレージの1GBも無駄にしない。全ドライブ容量分析・徹底アプリ削除・フォルダ同期。",
        "theme4_badge_2": "残留キャッシュ・設定ファイルを根こそぎ完全消去",
        "theme1_badge_2": "[Cmd+B] ネストされたサブフォルダを瞬時にフラット展開",
        "theme2_badge_1": "[Cmd+Q / Space] 100msの超高速クイックルック",
        "theme4_badge_1": "全ドライブの巨大ファイルをミリ秒単位で高速スキャン",
        "hero_title_h1": "2画面・マウス不要。指先ひとつで完結。",
        "hero_title_h2": "Macのファイルシステムを、完全に支配下に。",
        "t3_tab_samba_share": "Samba リモート共有"
    },
    "de": {
        "btn_user_guide": "Benutzerhandbuch",
        "btn_contact": "Kontakt",
        "hero_btn_guide": "Benutzerhandbuch",
        "conversion_btn_guide": "Benutzerhandbuch",
        "t1_tab_tree_views": "Zwei unabhängige Verzeichnisbäume",
        "theme1_badge_3": "[Alt+F1/F2] Schnelle Volume- & Laufwerksauswahl",
        "theme2_title": "Vergiss ressourcenfressende Einzel-Apps. Ein Tastendruck genügt für die Vorschau von Retina-Bildern, Dokumenten und Medien.",
        "hero_badge_1": "⚡ 100% tastaturgesteuert · Hände bleiben auf der Grundstellung",
        "theme4_title": "Volle Kontrolle über jedes Gigabyte. Speicherplatz-Analyse, gründliche App-Bereinigung und Synchronisation.",
        "theme4_badge_2": "Gründliches Entfernen von Rest-Caches und Konfigurationsdateien",
        "theme1_badge_2": "[Cmd+B] Verschachtelte Unterordner sofort flach anzeigen",
        "theme2_badge_1": "[Cmd+Q / Leertaste] 100ms verzögerungsfreie Schnellansicht",
        "theme4_badge_1": "Blitzschnelle Analyse großer Dateien über das gesamte Laufwerk",
        "hero_title_h1": "Zwei Panels. Null Klicks.",
        "hero_title_h2": "Hole dir die volle Kontrolle über dein Mac-Dateisystem zurück.",
        "t1_tab_branch_view": "Branch View (Verzeichnis flach anzeigen)",
        "t2_tab_epub": "EPUB E-Book"
    },
    "fr": {
        "btn_user_guide": "Guide de l'utilisateur",
        "btn_contact": "Nous contacter",
        "hero_btn_guide": "Guide de l'utilisateur",
        "conversion_btn_guide": "Guide de l'utilisateur",
        "t1_tab_tree_views": "Deux arborescences indépendantes",
        "theme1_badge_3": "[Alt+F1/F2] Sélection ultra-rapide des disques et volumes",
        "theme2_title": "Oubliez les applications lourdes. Appuyez sur une touche pour inspecter vos images Retina, documents et médias.",
        "hero_badge_1": "⚡ 100 % au clavier · Ne quittez jamais la rangée de base",
        "theme4_title": "Le contrôle de chaque gigaoctet. Analyse panoramique du disque, nettoyage approfondi des apps et synchronisation.",
        "theme4_badge_2": "Éradication complète des résidus de cache et de configuration",
        "theme1_badge_2": "[Cmd+B] Aplatir instantanément les sous-dossiers imbriqués",
        "theme2_badge_1": "[Cmd+Q / Espace] Coup d'œil instantané et ultra-fluide (100 ms)",
        "theme4_badge_1": "Analyse ultra-rapide des gros fichiers sur tout le disque",
        "hero_title_h1": "Deux panneaux. Zéro clic.",
        "hero_title_h2": "Reprenez le contrôle absolu du système de fichiers de votre Mac.",
        "nav_remote_vfs": "Système de fichiers distant"
    },
    "es": {
        "btn_user_guide": "Guía del usuario",
        "btn_contact": "Contacto",
        "hero_btn_guide": "Guía del usuario",
        "conversion_btn_guide": "Guía del usuario",
        "t1_tab_tree_views": "Doble árbol de directorios independiente",
        "theme1_badge_3": "[Alt+F1/F2] Selección rápida de discos y volúmenes",
        "theme2_title": "Olvídate de aplicaciones pesadas. Presiona una tecla para previsualizar imágenes Retina, documentos y multimedia.",
        "hero_badge_1": "⚡ 100% controlado por teclado · Sin mover las manos de la posición de reposo",
        "theme4_title": "Control total de cada gigabyte. Análisis panorámico del disco, limpieza profunda de apps y sincronización.",
        "theme4_badge_2": "Limpieza a fondo de cachés residuales y archivos de configuración",
        "theme1_badge_2": "[Cmd+B] Aplanar subcarpetas anidadas al instante",
        "theme2_badge_1": "[Cmd+Q / Espacio] Vista rápida con respuesta instantánea de 100 ms",
        "theme4_badge_1": "Análisis ultrarrápido de archivos de gran tamaño en todo el disco",
        "hero_title_h1": "Dos paneles. Cero clics.",
        "hero_title_h2": "Recupera el control absoluto de tu sistema de archivos en Mac."
    },
    "pt": {
        "btn_user_guide": "Guia do Usuário",
        "btn_contact": "Contato",
        "hero_btn_guide": "Guia do Usuário",
        "conversion_btn_guide": "Guia do Usuário",
        "t1_tab_tree_views": "Árvores de Diretórios Duplas e Independentes",
        "theme1_badge_3": "[Alt+F1/F2] Seleção rápida de discos e volumes",
        "theme2_title": "Esqueça os aplicativos pesados. Pressione uma tecla para visualizar imagens Retina, documentos e mídia em alta resolução.",
        "hero_badge_1": "⚡ 100% Controlado pelo Teclado · Sem Tirar as Mãos da Posição Base",
        "theme4_title": "Controle de cada gigabyte. Análise panorâmica do disco, limpeza profunda de apps e sincronização.",
        "theme4_badge_2": "Remoção Completa de Caches e Resíduos de Configuração",
        "theme1_badge_2": "[Cmd+B] Achatar subpastas aninhadas instantaneamente",
        "theme2_badge_1": "[Cmd+Q / Espaço] Visualização rápida com resposta instantânea de 100 ms",
        "theme4_badge_1": "Análise ultrarrápida de arquivos grandes em todo o disco",
        "hero_title_h1": "Dois painéis. Zero cliques.",
        "hero_title_h2": "Retome o controle absoluto do sistema de arquivos do seu Mac.",
        "theme1_badge_1": "[Tab] Alternância Imediata de Foco entre Painéis",
        "t4_tab_app_uninstaller": "Desinstalador Completo de Apps"
    },
    "ko": {
        "btn_user_guide": "사용자 가이드",
        "btn_contact": "문의하기",
        "hero_btn_guide": "사용자 가이드",
        "conversion_btn_guide": "사용자 가이드",
        "t1_tab_tree_views": "좌우 독립 디렉토리 트리",
        "theme1_badge_3": "[Alt+F1/F2] 드라이브 및 볼륨 빠른 선택",
        "theme2_title": "무거운 개별 앱 실행은 이제 그만. 키 하나로 Retina 고해상도 이미지, 문서, 미디어를 즉시 확인하세요.",
        "hero_badge_1": "⚡ 100% 키보드 중심 · 홈 포지션에서 손을 뗄 필요 없는 완벽한 조작",
        "theme4_title": "단 1GB의 공간도 놓치지 않는 정밀함. 전체 디스크 용량 분석, 앱 완전 삭제, 폴더 동기화까지.",
        "theme4_badge_2": "잔여 캐시와 설정 파일까지 완벽 제거",
        "theme1_badge_2": "[Cmd+B] 중첩된 하위 폴더를 즉시 평면화하여 나열",
        "theme2_badge_1": "[Cmd+Q / Space] 100ms 초고속 훑어보기",
        "theme4_badge_1": "밀리초 단위의 전체 디스크 대용량 파일 초고속 분석",
        "hero_title_h1": "두 개의 패널. 마우스는 필요 없습니다.",
        "hero_title_h2": "Mac 파일 시스템의 완전한 통제권을 되찾으세요."
    },
    "ru": {
        "btn_user_guide": "Руководство пользователя",
        "btn_contact": "Контакты",
        "hero_btn_guide": "Руководство пользователя",
        "conversion_btn_guide": "Руководство пользователя",
        "t1_tab_tree_views": "Два независимых дерева папок",
        "theme1_badge_3": "[Alt+F1/F2] Быстрый выбор томов и дисков",
        "theme2_title": "Забудьте о тяжёлых отдельных приложениях. Одно нажатие — и ваши Retina-изображения, документы и медиа открыты для просмотра.",
        "hero_badge_1": "⚡ 100% управление с клавиатуры · Руки остаются в основной позиции",
        "theme4_title": "Контроль над каждым гигабайтом. Панорамный анализ диска, глубокая очистка приложений и синхронизация.",
        "theme4_badge_2": "Полное удаление остаточного кэша и конфигурационных файлов",
        "theme1_badge_2": "[Cmd+B] Мгновенное разворачивание всех вложенных папок в единый список",
        "theme2_badge_1": "[Cmd+Q / Пробел] Быстрый просмотр с мгновенным откликом (100 мс)",
        "theme4_badge_1": "Мгновенный анализ крупных файлов на всём диске",
        "hero_title_h1": "Две панели. Ноль кликов.",
        "hero_title_h2": "Верните полный контроль над файловой системой вашего Mac."
    },
    "it": {
        "btn_user_guide": "Guida dell'utente",
        "btn_contact": "Contatti",
        "hero_btn_guide": "Guida dell'utente",
        "conversion_btn_guide": "Guida dell'utente",
        "t1_tab_tree_views": "Due alberi di directory indipendenti",
        "theme1_badge_3": "[Alt+F1/F2] Selezione rapida di volumi e dischi",
        "theme2_title": "Dimentica le pesanti app dedicate. Premi un tasto per visualizzare immagini Retina, documenti e contenuti multimediali.",
        "hero_badge_1": "⚡ 100% guidato dalla tastiera · Mani sempre sui tasti base",
        "theme4_title": "Pieno controllo di ogni gigabyte. Analisi panoramica del disco, pulizia profonda delle app e sincronizzazione.",
        "theme4_badge_2": "Rimozione radicale di cache residue e file di configurazione",
        "theme1_badge_2": "[Cmd+B] Appiattisci istantaneamente le sottocartelle nidificate",
        "theme2_badge_1": "[Cmd+Q / Spazio] Visualizzazione rapida istantanea a 100 ms",
        "theme4_badge_1": "Analisi ultra-rapida di file di grandi dimensioni sull'intero disco",
        "hero_title_h1": "Due pannelli. Zero clic.",
        "hero_title_h2": "Riprendi il controllo totale del file system del tuo Mac.",
        "theme1_badge_1": "[Tab] Cambio istantaneo di fuoco tra i due pannelli"
    }
}

for lang, overrides in fixes.items():
    p = os.path.join(I18N_DIR, f"{lang}.json")
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Apply overrides
        for k, v in overrides.items():
            if k in data:
                data[k] = v
        
        # Ensure en.json keys order
        with open(os.path.join(I18N_DIR, "en.json"), 'r', encoding='utf-8') as f:
            en_data = json.load(f)
            
        ordered_data = {k: data[k] for k in en_data.keys()}
        
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(ordered_data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Updated {lang}.json")

print("All files updated successfully.")
