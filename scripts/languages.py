"""
scripts/languages.py
Single Source of Truth for ATBCmder Documentation i18n metadata.
"""

from typing import Any, Dict, List, Optional

NAV_ORDER: List[str] = [
    "index.md",
    "getting_started.md",
    "navigation_and_tabs.md",
    "file_operations.md",
    "viewers_and_editors.md",
    "power_tools.md",
    "network_and_vfs.md",
    "preferences_and_customization.md",
    "keyboard_shortcuts.md",
    "faq_howtos.md",
    "download.md",
    "privacy_policy.md",
]

DEFAULT_LANGUAGE: str = "en"

LANGUAGES: List[Dict[str, Any]] = [
    {
        "code": "en",
        "name": "English",
        "english_name": "English",
        "description": "The Dual-Panel File Manager for macOS",
        "theme_lang": "en",
        "browser_prefixes": ["en"],
        "nav_titles": {
            "index.md": "Welcome to ATBCmder",
            "getting_started.md": "Chapter 1: Fundamentals & macOS Setup",
            "navigation_and_tabs.md": "Chapter 2: Navigation & Folder Tabs",
            "file_operations.md": "Chapter 3: Daily File Operations & Background Queue",
            "viewers_and_editors.md": "Chapter 4: Universal Lister & Built-in Editors",
            "power_tools.md": "Chapter 5: Power Tools & Automation",
            "network_and_vfs.md": "Chapter 6: Virtual File Systems & Network",
            "preferences_and_customization.md": "Chapter 7: Preferences & Customization",
            "keyboard_shortcuts.md": "Chapter 8: Master Keyboard Shortcut Reference",
            "faq_howtos.md": "Chapter 9: Real-World Recipes & Troubleshooting",
            "download.md": "Chapter 10: Download & Installation",
            "privacy_policy.md": "Privacy Policy",
        },
    },
    {
        "code": "zh",
        "name": "简体中文",
        "english_name": "Simplified Chinese",
        "description": "macOS 双栏文件管理器与键盘流效率工具",
        "theme_lang": "zh",
        "browser_prefixes": ["zh-cn", "zh-sg", "zh-hans", "zh"],
        "nav_titles": {
            "index.md": "欢迎使用 ATBCmder",
            "getting_started.md": "第 1 章：基础概念与 macOS 系统配置",
            "navigation_and_tabs.md": "第 2 章：极速导航与多标签工作区",
            "file_operations.md": "第 3 章：日常文件操作与后台异步队列",
            "viewers_and_editors.md": "第 4 章：全能万用查看器与内置编辑器",
            "power_tools.md": "第 5 章：高阶生产力工具与自动化",
            "network_and_vfs.md": "第 6 章：虚拟文件系统与网络互联",
            "preferences_and_customization.md": "第 7 章：偏好设置与深度个性化定制",
            "keyboard_shortcuts.md": "第 8 章：终极快捷键全书",
            "faq_howtos.md": "第 9 章：实战场景解决方案与故障排查",
            "download.md": "第 10 章：软件下载与安装指南",
            "privacy_policy.md": "隐私政策",
        },
    },
    {
        "code": "zh-hant",
        "name": "繁體中文",
        "english_name": "Traditional Chinese",
        "description": "macOS 雙欄檔案管理器與鍵盤流效率工具",
        "theme_lang": "zh-TW",
        "browser_prefixes": ["zh-tw", "zh-hk", "zh-mo", "zh-hant"],
        "nav_titles": {
            "index.md": "歡迎使用 ATBCmder",
            "getting_started.md": "第 1 章：基礎概念與 macOS 系統配置",
            "navigation_and_tabs.md": "第 2 章：極速導覽與多分頁工作區",
            "file_operations.md": "第 3 章：日常檔案操作與後台異步隊列",
            "viewers_and_editors.md": "第 4 章：全能萬用檢視器與內建編輯器",
            "power_tools.md": "第 5 章：進階生產力工具與自動化",
            "network_and_vfs.md": "第 6 章：虛擬檔案系統與網路互連",
            "preferences_and_customization.md": "第 7 章：偏好設定與深度個性化自訂",
            "keyboard_shortcuts.md": "第 8 章：終極快速鍵全書",
            "faq_howtos.md": "第 9 章：實戰場景解決方案與疑難排解",
            "download.md": "第 10 章：軟體下載與安裝指南",
            "privacy_policy.md": "隱私政策",
        },
    },
    {
        "code": "ja",
        "name": "日本語",
        "english_name": "Japanese",
        "description": "macOS向けデュアルパネル・ファイルマネージャー",
        "theme_lang": "ja",
        "browser_prefixes": ["ja"],
        "nav_titles": {
            "index.md": "ATBCmder へようこそ",
            "getting_started.md": "第1章：基本概念と macOS の初期設定",
            "navigation_and_tabs.md": "第2章：高速ナビゲーションとフォルダータブ",
            "file_operations.md": "第3章：日常のファイル操作と非同期バックグラウンドキュー",
            "viewers_and_editors.md": "第4章：万能ビューアーと内蔵エディター",
            "power_tools.md": "第5章：高度なツールと自動化",
            "network_and_vfs.md": "第6章：仮想ファイルシステムとネットワーク",
            "preferences_and_customization.md": "第7章：環境設定とカスタマイズ",
            "keyboard_shortcuts.md": "第8章：マスターキーボードショートカット一覧",
            "faq_howtos.md": "第9章：実践レシピとトラブルシューティング",
            "download.md": "第10章：ダウンロードとインストール",
            "privacy_policy.md": "プライバシーポリシー",
        },
    },
    {
        "code": "de",
        "name": "Deutsch",
        "english_name": "German",
        "description": "Der Zwei-Fenster-Dateimanager für macOS",
        "theme_lang": "de",
        "browser_prefixes": ["de"],
        "nav_titles": {
            "index.md": "Willkommen bei ATBCmder",
            "getting_started.md": "Kapitel 1: Grundlagen & macOS-Einrichtung",
            "navigation_and_tabs.md": "Kapitel 2: Navigation & Ordner-Tabs",
            "file_operations.md": "Kapitel 3: Dateioperationen & Hintergrundwarteschlange",
            "viewers_and_editors.md": "Kapitel 4: Universeller Betrachter & Editoren",
            "power_tools.md": "Kapitel 5: Power-Tools & Automatisierung",
            "network_and_vfs.md": "Kapitel 6: Virtuelle Dateisysteme & Netzwerk",
            "preferences_and_customization.md": "Kapitel 7: Einstellungen & Anpassung",
            "keyboard_shortcuts.md": "Kapitel 8: Tastaturkurzbefehle-Referenz",
            "faq_howtos.md": "Kapitel 9: Praxislösungen & Fehlerbehebung",
            "download.md": "Kapitel 10: Download & Installation",
            "privacy_policy.md": "Datenschutzerklärung",
        },
    },
    {
        "code": "fr",
        "name": "Français",
        "english_name": "French",
        "description": "Le gestionnaire de fichiers à double panneau pour macOS",
        "theme_lang": "fr",
        "browser_prefixes": ["fr"],
        "nav_titles": {
            "index.md": "Bienvenue sur ATBCmder",
            "getting_started.md": "Chapitre 1: Notions de base et configuration macOS",
            "navigation_and_tabs.md": "Chapitre 2: Navigation et onglets de dossiers",
            "file_operations.md": "Chapitre 3: Opérations de fichiers et file d'attente en arrière-plan",
            "viewers_and_editors.md": "Chapitre 4: Visionneuse universelle et éditeurs intégrés",
            "power_tools.md": "Chapitre 5: Outils avancés et automatisation",
            "network_and_vfs.md": "Chapitre 6: Systèmes de fichiers virtuels et réseau",
            "preferences_and_customization.md": "Chapitre 7: Préférences et personnalisation",
            "keyboard_shortcuts.md": "Chapitre 8: Répertoire principal des raccourcis clavier",
            "faq_howtos.md": "Chapitre 9: Recettes pratiques et dépannage",
            "download.md": "Chapitre 10: Téléchargement et installation",
            "privacy_policy.md": "Politique de confidentialité",
        },
    },
    {
        "code": "es",
        "name": "Español",
        "english_name": "Spanish",
        "description": "El administrador de archivos de doble panel para macOS",
        "theme_lang": "es",
        "browser_prefixes": ["es"],
        "nav_titles": {
            "index.md": "Bienvenido a ATBCmder",
            "getting_started.md": "Capítulo 1: Fundamentos y configuración de macOS",
            "navigation_and_tabs.md": "Capítulo 2: Navegación y pestañas de carpetas",
            "file_operations.md": "Capítulo 3: Operaciones de archivos y cola en segundo plano",
            "viewers_and_editors.md": "Capítulo 4: Visor universal y editores integrados",
            "power_tools.md": "Capítulo 5: Herramientas avanzadas y automatización",
            "network_and_vfs.md": "Capítulo 6: Sistemas de archivos virtuales y red",
            "preferences_and_customization.md": "Capítulo 7: Preferencias y personalización",
            "keyboard_shortcuts.md": "Capítulo 8: Referencia maestra de atajos de teclado",
            "faq_howtos.md": "Capítulo 9: Soluciones prácticas y resolución de problemas",
            "download.md": "Capítulo 10: Descarga e instalación",
            "privacy_policy.md": "Política de privacidad",
        },
    },
    {
        "code": "pt",
        "name": "Português",
        "english_name": "Portuguese",
        "description": "O gerenciador de arquivos de painel duplo para macOS",
        "theme_lang": "pt",
        "browser_prefixes": ["pt", "pt-br", "pt-pt"],
        "nav_titles": {
            "index.md": "Bem-vindo ao ATBCmder",
            "getting_started.md": "Capítulo 1: Fundamentos e configuração do macOS",
            "navigation_and_tabs.md": "Capítulo 2: Navegação e abas de pastas",
            "file_operations.md": "Capítulo 3: Operações de arquivos e fila em segundo plano",
            "viewers_and_editors.md": "Capítulo 4: Visualizador universal e editores integrados",
            "power_tools.md": "Capítulo 5: Ferramentas avançadas e automação",
            "network_and_vfs.md": "Capítulo 6: Sistemas de arquivos virtuais e rede",
            "preferences_and_customization.md": "Capítulo 7: Preferências e personalização",
            "keyboard_shortcuts.md": "Capítulo 8: Referência mestre de atalhos de teclado",
            "faq_howtos.md": "Capítulo 9: Receitas práticas e solução de problemas",
            "download.md": "Capítulo 10: Download e instalação",
            "privacy_policy.md": "Política de privacidade",
        },
    },
    {
        "code": "ko",
        "name": "한국어",
        "english_name": "Korean",
        "description": "macOS용 듀얼 패널 파일 관리자",
        "theme_lang": "ko",
        "browser_prefixes": ["ko"],
        "nav_titles": {
            "index.md": "ATBCmder 에 오신 것을 환영합니다",
            "getting_started.md": "제1장: 기본 개념 및 macOS 설정",
            "navigation_and_tabs.md": "제2장: 내비게이션 및 폴더 탭",
            "file_operations.md": "제3장: 일상 파일 작업 및 백그라운드 큐",
            "viewers_and_editors.md": "제4장: 만능 뷰어 및 내장 편집기",
            "power_tools.md": "제5장: 고급 도구 및 자동화",
            "network_and_vfs.md": "제6장: 가상 파일 시스템 및 네트워크",
            "preferences_and_customization.md": "제7장: 환경설정 및 사용자 정의",
            "keyboard_shortcuts.md": "제8장: 마스터 키보드 단축키 레퍼런스",
            "faq_howtos.md": "제9장: 실전 문제 해결 및 레시피",
            "download.md": "제10장: 다운로드 및 설치 가이드",
            "privacy_policy.md": "개인정보 처리방침",
        },
    },
    {
        "code": "ru",
        "name": "Русский",
        "english_name": "Russian",
        "description": "Двухпанельный файловый менеджер для macOS",
        "theme_lang": "ru",
        "browser_prefixes": ["ru"],
        "nav_titles": {
            "index.md": "Добро пожаловать в ATBCmder",
            "getting_started.md": "Глава 1: Основные концепции и настройка macOS",
            "navigation_and_tabs.md": "Глава 2: Навигация и вкладки папок",
            "file_operations.md": "Глава 3: Операции с файлами и фоновая очередь",
            "viewers_and_editors.md": "Глава 4: Универсальный просмотрщик и редакторы",
            "power_tools.md": "Глава 5: Инструменты продуктивности и автоматизация",
            "network_and_vfs.md": "Глава 6: Виртуальные файловые системы и сеть",
            "preferences_and_customization.md": "Глава 7: Настройки и персонализация",
            "keyboard_shortcuts.md": "Глава 8: Справочник горячих клавиш",
            "faq_howtos.md": "Глава 9: Практические рецепты и устранение неполадок",
            "download.md": "Глава 10: Скачивание и установка",
            "privacy_policy.md": "Политика конфиденциальности",
        },
    },
    {
        "code": "it",
        "name": "Italiano",
        "english_name": "Italian",
        "description": "Il file manager a doppio pannello per macOS",
        "theme_lang": "it",
        "browser_prefixes": ["it"],
        "nav_titles": {
            "index.md": "Benvenuto in ATBCmder",
            "getting_started.md": "Capitolo 1: Concetti fondamentali e configurazione di macOS",
            "navigation_and_tabs.md": "Capitolo 2: Navigazione e schede delle cartelle",
            "file_operations.md": "Capitolo 3: Operazioni quotidiane sui file e coda in background",
            "viewers_and_editors.md": "Capitolo 4: Visualizzatore universale ed editor integrati",
            "power_tools.md": "Capitolo 5: Strumenti avanzati e automazione",
            "network_and_vfs.md": "Capitolo 6: File system virtuali e rete",
            "preferences_and_customization.md": "Capitolo 7: Preferenze e personalizzazione",
            "keyboard_shortcuts.md": "Capitolo 8: Guida rapida alle scorciatoie da tastiera",
            "faq_howtos.md": "Capitolo 9: Ricette pratiche e risoluzione dei problemi",
            "download.md": "Capitolo 10: Download e installazione",
            "privacy_policy.md": "Informativa sulla privacy",
        },
    },
]

LANGUAGE_MAP: Dict[str, Dict[str, Any]] = {lang["code"]: lang for lang in LANGUAGES}


def get_language(code: str) -> Optional[Dict[str, Any]]:
    """Retrieve language metadata dict by code."""
    return LANGUAGE_MAP.get(code)


def get_language_codes() -> List[str]:
    """Retrieve list of all 11 language codes."""
    return [lang["code"] for lang in LANGUAGES]


if __name__ == "__main__":
    import json
    import sys

    if "--codes" in sys.argv:
        print(" ".join(get_language_codes()))
    elif "--json" in sys.argv:
        print(json.dumps(LANGUAGES, ensure_ascii=False, indent=2))
    else:
        print(f"Total languages configured: {len(LANGUAGES)}")
        for lang in LANGUAGES:
            print(
                f"  - [{lang['code']:<7}] {lang['name']:<10} ({lang['english_name']}) -> "
                f"theme_lang: {lang['theme_lang']}, chapters: {len(lang['nav_titles'])}"
            )
