import json
import os

I18N_DIR = "landing/i18n"

pricing_data = {
    "en": {
        "nav_pricing": "Pricing",
        "theme6_title": "Transparent, One-Time Pricing. No Subscriptions, Ever.",
        "theme6_desc": "Experience all professional features with a 90-day unrestricted free trial. One purchase grants lifetime authorization across all your Mac devices.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Lifetime License",
        "pricing_price": "$6.99",
        "pricing_price_sub": "One-time purchase · Lifetime ownership",
        "pricing_feat_1": "90-Day Free Trial — Full access to all Pro features with zero upfront commitment",
        "pricing_feat_2": "Tied to Your Apple ID — Seamless license management via the Mac App Store without third-party registration",
        "pricing_feat_3": "One-Time Purchase, Lifetime License — Buy once and own forever; all future updates included without monthly fees",
        "pricing_feat_4": "Multi-Machine Authorization — Run on all your Mac computers under the same Apple ID and Family Sharing",
        "pricing_btn_cta": "Get ATBCmder Pro on Mac App Store",
        "pricing_guarantee_note": "Secure checkout through Apple · Instant activation · Family Sharing supported"
    },
    "zh": {
        "nav_pricing": "价格",
        "theme6_title": "透明清晰，一次购买。告别反复订阅，永久拥抱极客效率。",
        "theme6_desc": "全功能免费试用 90 天，充分体验毫无保留。单次购买即可绑定 Apple 账号永久授权，并在您的多台 Mac 设备上通用。",
        "pricing_tier_title": "ATBCmder 专业版",
        "pricing_tier_badge": "终身买断",
        "pricing_price": "¥48.00",
        "pricing_price_sub": "一次性购买 · 永久授权使用",
        "pricing_feat_1": "免费试用 90 天 — 毫无保留体验全部 Pro 高级特性，试用期内无任何功能限制",
        "pricing_feat_2": "绑定 Apple 账号 — 授权直接与 Apple ID 关联，依托 Mac App Store 安全托管，无需注册额外账户",
        "pricing_feat_3": "一经购买，永久授权 — 终身享有 Pro 权益与后续功能更新，告别令人厌烦的按月循环扣费",
        "pricing_feat_4": "支持多台设备授权 — 同一 Apple ID 下的所有 Mac 设备均可通用，并完全支持家人共享",
        "pricing_btn_cta": "在 Mac App Store 获取专业版",
        "pricing_guarantee_note": "经由 Apple 官方安全结算 · 即买即用 · 支持家人共享"
    },
    "zh-hant": {
        "nav_pricing": "價格",
        "theme6_title": "透明清晰，一次購買。告別反覆訂閱，永久擁抱極客效率。",
        "theme6_desc": "全功能免費試用 90 天，充分體驗毫無保留。單次購買即可綁定 Apple 帳號永久授權，並在您的多台 Mac 裝置上通用。",
        "pricing_tier_title": "ATBCmder 專業版",
        "pricing_tier_badge": "終身買斷",
        "pricing_price": "NT$ 220",
        "pricing_price_sub": "一次性購買 · 永久授權使用",
        "pricing_feat_1": "免費試用 90 天 — 毫無保留體驗全部 Pro 高級特性，試用期內無任何功能限制",
        "pricing_feat_2": "綁定 Apple 帳號 — 授權直接與 Apple ID 關聯，依託 Mac App Store 安全託管，無需註冊額外帳戶",
        "pricing_feat_3": "一經購買，永久授權 — 終身享有 Pro 權益與後續功能更新，告別令人厭煩的按月循環扣費",
        "pricing_feat_4": "支援多台裝置授權 — 同一 Apple ID 下的所有 Mac 裝置均可通用，並完全支援家人共享",
        "pricing_btn_cta": "在 Mac App Store 獲取專業版",
        "pricing_guarantee_note": "經由 Apple 官方安全結算 · 即買即用 · 支援家人共享"
    },
    "ja": {
        "nav_pricing": "価格",
        "theme6_title": "明瞭な買い切り価格。サブスクリプションは一切不要。",
        "theme6_desc": "90日間の全機能無料トライアル。1回の購入でApple IDに紐づく永久ライセンスを獲得し、複数のMacで自由にお使いいただけます。",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "永久ライセンス",
        "pricing_price": "¥1,100",
        "pricing_price_sub": "買い切り · 一度の支払いで永久利用",
        "pricing_feat_1": "90日間の無料トライアル — すべてのPro機能を制限なく存分にお試しいただけます",
        "pricing_feat_2": "Apple IDに直接紐付け — サードパーティ登録不要、Mac App Storeで安全にライセンスを一元管理",
        "pricing_feat_3": "一度の購入で永久ライセンス — 月額課金なし。将来のアップデートもそのまま永久にご利用可能",
        "pricing_feat_4": "複数台のMacを認証可能 — 同じApple IDを使用するすべてのMacおよびファミリー共有に対応",
        "pricing_btn_cta": "Mac App Store で ATBCmder Pro を入手",
        "pricing_guarantee_note": "Apple公式の安全な決済 · 即時アクティベーション · ファミリー共有対応"
    },
    "de": {
        "nav_pricing": "Preise",
        "theme6_title": "Transparente Einmalzahlung. Für immer ohne Abonnement.",
        "theme6_desc": "90 Tage unverbindliche, voll funktionsfähige Testphase. Einmaliger Kauf für eine lebenslange Lizenz, gekoppelt an Ihre Apple-ID für all Ihre Macs.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Lebenslange Lizenz",
        "pricing_price": "7,99 €",
        "pricing_price_sub": "Einmaliger Kauf · Dauerhafte Nutzung",
        "pricing_feat_1": "90 Tage kostenlose Testversion — Voller Zugriff auf alle Pro-Funktionen ohne Einschränkungen",
        "pricing_feat_2": "An Ihre Apple-ID gekoppelt — Sichere Verwaltung über den Mac App Store, keine Registrierung bei Drittanbietern",
        "pricing_feat_3": "Einmaliger Kauf, lebenslange Lizenz — Keine monatlichen Gebühren; inklusive aller künftigen Funktionsupdates",
        "pricing_feat_4": "Multi-Geräte-Autorisierung — Auf allen Ihren Macs unter derselben Apple-ID und via Familienfreigabe nutzbar",
        "pricing_btn_cta": "ATBCmder Pro im Mac App Store holen",
        "pricing_guarantee_note": "Sichere Zahlung über Apple · Sofortige Aktivierung · Familienfreigabe unterstützt"
    },
    "fr": {
        "nav_pricing": "Tarifs",
        "theme6_title": "Un tarif unique et transparent. Aucun abonnement, jamais.",
        "theme6_desc": "Profitez d'un essai gratuit complet de 90 jours. Un achat unique lié à votre identifiant Apple pour une licence perpétuelle sur tous vos Mac.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Licence perpétuelle",
        "pricing_price": "7,99 €",
        "pricing_price_sub": "Achat unique · Utilisation à vie",
        "pricing_feat_1": "Essai gratuit complet de 90 jours — Accès illimité à toutes les fonctionnalités Pro sans engagement préalable",
        "pricing_feat_2": "Lié à votre identifiant Apple — Gestion transparente via le Mac App Store, sans inscription sur un compte tiers",
        "pricing_feat_3": "Achat unique, licence à vie — Aucun abonnement récurrent ; toutes les futures mises à jour incluses",
        "pricing_feat_4": "Autorisation multi-postes — Valable sur tous vos Mac avec le même identifiant Apple et le partage familial",
        "pricing_btn_cta": "Obtenir ATBCmder Pro sur le Mac App Store",
        "pricing_guarantee_note": "Paiement sécurisé via Apple · Activation immédiate · Partage familial pris en charge"
    },
    "es": {
        "nav_pricing": "Precios",
        "theme6_title": "Precio único y transparente. Sin suscripciones, para siempre.",
        "theme6_desc": "Disfruta de una prueba gratuita de 90 días con todas las funciones. Una compra única vinculada a tu cuenta de Apple para una licencia de por vida en todos tus Mac.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Licencia de por vida",
        "pricing_price": "7,99 €",
        "pricing_price_sub": "Compra única · Uso de por vida",
        "pricing_feat_1": "Prueba gratuita de 90 días — Acceso completo y sin restricciones a todas las funciones Pro",
        "pricing_feat_2": "Vinculado a tu Apple ID — Gestión segura en el Mac App Store sin necesidad de registrar cuentas de terceros",
        "pricing_feat_3": "Compra única, licencia perpetua — Sin cuotas mensuales recurrentes; incluye actualizaciones futuras",
        "pricing_feat_4": "Autorización para múltiples equipos — Válido en todos tus Mac con el mismo Apple ID y En familia",
        "pricing_btn_cta": "Obtener ATBCmder Pro en el Mac App Store",
        "pricing_guarantee_note": "Pago seguro a través de Apple · Activación instantánea · Compatible con En familia"
    },
    "pt": {
        "nav_pricing": "Preços",
        "theme6_title": "Preço único e transparente. Sem assinaturas, para sempre.",
        "theme6_desc": "Aproveite um teste gratuito de 90 dias com todos os recursos. Uma compra única vinculada ao seu ID Apple para licença vitalícia em todos os seus Macs.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Licença vitalícia",
        "pricing_price": "R$ 49,90",
        "pricing_price_sub": "Compra única · Uso vitalício",
        "pricing_feat_1": "90 dias de teste gratuito — Acesso irrestrito a todas as funcionalidades Pro durante a avaliação",
        "pricing_feat_2": "Vinculado ao seu ID Apple — Gerenciamento simplificado pela Mac App Store sem cadastro adicional",
        "pricing_feat_3": "Compra única, licença vitalícia — Sem mensalidades recorrentes; inclui futuras atualizações",
        "pricing_feat_4": "Autorização para vários Macs — Válido em todos os seus computadores sob o mesmo ID Apple e Compartilhamento Familiar",
        "pricing_btn_cta": "Obter ATBCmder Pro na Mac App Store",
        "pricing_guarantee_note": "Pagamento seguro pela Apple · Ativação imediata · Compatível com Compartilhamento Familiar"
    },
    "ko": {
        "nav_pricing": "가격",
        "theme6_title": "명확한 1회성 영구 구매. 반복 구독 없는 완벽한 소프트웨어.",
        "theme6_desc": "모든 기능을 제한 없이 90일간 무료로 체험하세요. 한 번 구매로 Apple 계정에 영구 라이선스가 귀속되어 여러 대의 Mac에서 자유롭게 사용 가능합니다.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "평생 소장 라이선스",
        "pricing_price": "₩11,000",
        "pricing_price_sub": "1회 구매 · 평생 영구 소장",
        "pricing_feat_1": "90일 무제한 무료 체험 — 모든 Pro 고급 기능을 제약 없이 완전하게 경험",
        "pricing_feat_2": "Apple 계정 자동 연동 — 외부 회원가입 없이 Mac App Store를 통해 안전하고 간편하게 라이선스 관리",
        "pricing_feat_3": "1회 구매, 평생 영구 소장 — 매달 결제되는 구독료 없이 향후 기능 업데이트까지 지속 제공",
        "pricing_feat_4": "다중 기기 인증 지원 — 동일한 Apple ID로 로그인된 모든 Mac 기기 및 가족 공유 지원",
        "pricing_btn_cta": "Mac App Store에서 ATBCmder Pro 다운로드",
        "pricing_guarantee_note": "Apple 공식 보안 결제 · 즉각 활성화 · 가족 공유 지원"
    },
    "ru": {
        "nav_pricing": "Цены",
        "theme6_title": "Прозрачная разовая покупка. Навсегда без подписок.",
        "theme6_desc": "Полнофункциональный бесплатный пробный период на 90 дней. Разовая покупка привязывается к Apple ID, давая пожизненную лицензию для всех ваших Mac.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Пожизненная лицензия",
        "pricing_price": "599 ₽",
        "pricing_price_sub": "Разовый платёж · Бессрочное использование",
        "pricing_feat_1": "90 дней бесплатного пробного периода — Полный доступ ко всем возможностям Pro без каких-либо ограничений",
        "pricing_feat_2": "Привязка к Apple ID — Безопасное управление лицензией через Mac App Store без сторонней регистрации",
        "pricing_feat_3": "Разовая покупка, бессрочная лицензия — Без ежемесячных подписок; включает все будущие обновления",
        "pricing_feat_4": "Авторизация на нескольких Mac — Работает на всех ваших компьютерах под одним Apple ID и с семейным доступом",
        "pricing_btn_cta": "Получить ATBCmder Pro в Mac App Store",
        "pricing_guarantee_note": "Безопасная оплата через Apple · Мгновенная активация · Поддержка семейного доступа"
    },
    "it": {
        "nav_pricing": "Prezzi",
        "theme6_title": "Prezzo unico e trasparente. Senza abbonamenti, per sempre.",
        "theme6_desc": "Prova tutte le funzionalità senza limiti con una prova gratuita di 90 giorni. Un acquisto unico legato al tuo ID Apple per una licenza a vita su tutti i tuoi Mac.",
        "pricing_tier_title": "ATBCmder Pro",
        "pricing_tier_badge": "Licenza a vita",
        "pricing_price": "7,99 €",
        "pricing_price_sub": "Acquisto unico · Utilizzo a vita",
        "pricing_feat_1": "Prova gratuita di 90 giorni — Accesso illimitato a tutte le funzionalità Pro senza limitazioni",
        "pricing_feat_2": "Associato al tuo ID Apple — Gestione sicura tramite Mac App Store senza registrazione di account terzi",
        "pricing_feat_3": "Acquisto unico, licenza a vita — Nessun abbonamento ricorrente; tutti gli aggiornamenti futuri inclusi",
        "pricing_feat_4": "Autorizzazione multi-dispositivo — Utilizzabile su tutti i tuoi Mac con lo stesso ID Apple e 'In famiglia'",
        "pricing_btn_cta": "Ottieni ATBCmder Pro su Mac App Store",
        "pricing_guarantee_note": "Pagamento sicuro tramite Apple · Attivazione immediata · Supporta 'In famiglia'"
    }
}

for lang, new_keys in pricing_data.items():
    file_path = os.path.join(I18N_DIR, f"{lang}.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Merge new keys
        data.update(new_keys)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Updated {file_path} with {len(new_keys)} pricing keys.")

print("All language dictionaries successfully updated.")
