"""產生小小花品牌網站的所有頁面。改內容只要改這支檔案，再執行 python3 build.py。"""
import json
from pathlib import Path

# 放在 repo 的 _src/xiaoxiaohua/ 時，輸出到 repo 的 xiaoxiaohua/；單獨放時輸出到同一個資料夾。
_here = Path(__file__).resolve().parent
ROOT = _here.parents[1] / "xiaoxiaohua" if _here.parent.name == "_src" else _here
SITE = "https://yy7yy7kimo-code.github.io/xiaoxiaohua"   # 上線時換成實際網址（不含結尾斜線）
SHOP = "https://shopee.tw/yy7yy7kimo"
def sp(pid): return f"https://shopee.tw/product/12494/{pid}"

SOCIAL = [("蝦皮賣場", SHOP), ("Facebook", "https://www.facebook.com/yy7yy7kimo"),
          ("Instagram", "https://www.instagram.com/xiaoxian9681/"),
          ("Threads", "https://www.threads.com/@xiaoxian9681"),
          ("YouTube", "https://www.youtube.com/@littleflowerbakery")]

NAV = [("index.html", "首頁"), ("menu.html", "今日出爐"), ("gifts.html", "送禮指南"),
       ("journal.html", "烘焙日誌"), ("about.html", "關於小小花"), ("faq.html", "常見問題")]

# ---- 商品資料（價格照蝦皮 2026/11/09 售價） ----
PRODUCTS = [
  dict(slug="macadamia-tart", name="夏威夷豆塔", tagline="整顆夏威夷豆，一顆一顆排上塔皮",
       img="tart-board.jpg", gallery=["hero.jpg", "tart-box.jpg", "tart-12.jpg", "box24.jpg"],
       intro="酥脆的塔皮裡是焦糖蔓越莓內餡，上面鋪滿整顆夏威夷豆，烤到表面微微金黃。單顆約 30 克，一口咬下是堅果香和塔皮的酥。",
       detail=["塔皮與內餡每天手工製作，小量出爐。",
               "禮盒有粉色提盒與粉綠色禮盒兩種，送人不用再另外包裝。",
               "單顆獨立包裝也有，適合先試吃、婚禮小物或團購分送。"],
       options=[("10 入粉色提盒", 390, sp(51524156)), ("12 入禮盒", 499, sp(134073)),
                ("24 入豪華提盒", 999, sp(51524156)), ("單顆獨立包裝", 39, sp(1665727))],
       keep="收到後請放在陰涼乾燥處，避免陽光直射，並盡早享用。實際保存期限以包裝標示為準。",
       good_for="拜訪長輩、節日送禮、彌月、企業贈禮"),
  dict(slug="nougat-cracker", name="蔥軋餅（牛軋餅）", tagline="蔥香餅皮夾 Q 軟牛軋",
       img="nougat.jpg", gallery=["nougat-close.jpg", "nougat-box.jpg"],
       intro="鹹香的蔥餅皮，夾進軟 Q 的牛軋糖，甜鹹剛好，一片接一片。每片單獨密封，再用紙盒排好。",
       detail=["單片密封，放在辦公桌、包包裡都方便。",
               "16、24、40 片三種規格，40 片有禮盒附提袋。",
               "成份：麵粉、奶油、海藻糖、奶粉、蛋白霜、麥芽糖、蔥。"],
       options=[("16 片", 192, sp(2547801)), ("24 片", 288, sp(2547801)), ("40 片禮盒附提袋", 480, sp(2547801))],
       keep="保存期限 15 天。收到後請放在陰涼乾燥處，開封後盡快食用。",
       good_for="辦公室分享、團購、拜訪親友"),
  dict(slug="almond-boat", name="杏仁船餅", tagline="焦糖杏仁片鋪滿小船",
       img="almond-photo.jpg", gallery=["almond.jpg"],
       intro="船型的餅乾底，鋪上滿滿焦糖杏仁片，烤到香脆。單片獨立包裝，配一杯熱茶剛好。",
       detail=["單片獨立包裝，方便分送。", "適合下午茶、茶點盤與團購點心。"],
       options=[("單片", 18, sp(1138396690))],
       keep="收到後請放在陰涼乾燥處，開封後盡快食用。實際保存期限以包裝標示為準。",
       good_for="下午茶、團購分送"),
  dict(slug="salted-nougat", name="鹽牛軋餅", tagline="帶一點鹽香的牛軋夾心",
       img="salt-nougat.jpg", gallery=[],
       intro="酥香餅乾夾入牛軋糖，帶一點鹽香，不會太甜。單片獨立包裝。",
       detail=["單片獨立包裝。", "想一次嚐多種口味，可以和杏仁船餅、單顆豆塔一起搭配。"],
       options=[("單片", 12, sp(1005122348))],
       keep="收到後請放在陰涼乾燥處，開封後盡快食用。實際保存期限以包裝標示為準。",
       good_for="婚禮小物、團購分送"),
]

FAQ = [
  ("要去哪裡買？", "請到蝦皮賣場「小小花手工烘焙」下單，我們從台中手工現烤後寄出，下單後 3 天內出貨。"),
  ("下單後多久出貨？", "每天手工現烤、每日限量，蝦皮下單後 3 天內出貨。需要指定日期，請在訂單備註寫明。"),
  ("可以大量訂購嗎？公司贈禮、團購怎麼訂？", "可以。請在蝦皮聊聊告訴我們品項、數量和希望收到的日期，確認產能後會回覆可以出貨的時間。"),
  ("蔥軋餅可以放多久？", "所有商品都是常溫保存。蔥軋餅保存期限 15 天，其他商品請以包裝標示為準，收到後放陰涼乾燥處並盡早享用。"),
  ("運費怎麼算？", "運費依蝦皮結帳時選的物流方式計算，例如萊爾富取貨 NT$50、7-ELEVEN 取貨 NT$60，宅配依重量計價，實際金額以蝦皮結帳畫面為準。"),
  ("收到不滿意可以退貨嗎？", "可以。收到商品覺得不滿意，只要在保存期限內把商品寄回，我們直接退款。"),
  ("禮盒需要另外包裝嗎？", "不用。夏威夷豆塔有粉色提盒和禮盒，蔥軋餅 40 片附禮盒和提袋，收到就能直接送人。"),
  ("台中有什麼適合送禮的伴手禮？", "如果要送長輩或拜訪親友，夏威夷豆塔提盒最體面；送同事、辦公室分享，單片密封的蔥軋餅最方便。兩種都是小小花在台中每天手工現烤。"),
]

ARTICLES = [
  dict(slug="lunar-new-year-gift-guide", date="2026-11-11", title="過年伴手禮怎麼準備？年節送禮的預購時程與份量",
       desc="過年前大家都在搶訂，手工點心產量有限。整理年節送禮要提早多久訂、送長輩和送客戶各挑什麼、份量怎麼抓。",
       img="box24.jpg",
       body=[("h2", "手工點心，過年前要提早訂"),
             ("p", "農曆年前是一年訂單最多的時候。手工烘焙每天能烤的數量固定，越接近過年越容易排不進去。建議過年前兩到三週就先預購，並在訂單備註寫上希望收到的日期。"),
             ("h2", "依送禮對象挑選"),
             ("h3", "回家過年、拜訪長輩"),
             ("p", "選拿出來體面、口感不會太硬的禮盒。小小花的夏威夷豆塔 10 入粉色提盒、12 入禮盒，提著就能出門，長輩也咬得動。"),
             ("h3", "公司年終、送客戶"),
             ("p", "一次要送很多份，選規格一致、外觀大方的禮盒。24 入豪華提盒適合重要客戶；數量多時請先在蝦皮聊聊確認出貨日。"),
             ("h3", "辦公室開工、團拜"),
             ("p", "開工第一天帶點心進辦公室，選單片密封、大家拿了就走的。蔥軋餅 24 片、40 片禮盒附提袋最方便。"),
             ("h2", "份量怎麼抓"),
             ("ul", ["一個家庭：豆塔 10～12 入一盒", "重要客戶：24 入豪華提盒", "20 人左右辦公室：蔥軋餅 24～40 片", "想多種口味：單顆豆塔、杏仁船餅、鹽牛軋餅混搭"]),
             ("h2", "收到後怎麼放"),
             ("p", "放在陰涼乾燥處，避免陽光直射和高溫的車內。蔥軋餅保存期限 15 天，其他品項以包裝標示為準。離送禮日還有一段時間，就在備註指定出貨日，收到時最新鮮。")]),
  dict(slug="how-to-store-handmade-cookies", date="2026-11-11", title="手工餅乾、豆塔怎麼保存？收到後這樣放最好吃",
       desc="手工點心沒有大量添加防腐，放法對了才會一直酥脆。整理收到後的擺放位置、開封後怎麼收、哪些地方不要放。",
       img="tart-single.jpg",
       body=[("h2", "收到後先放陰涼乾燥處"),
             ("p", "手工烘焙點心最怕潮濕和高溫。收到後放在室內陰涼、通風的地方，像櫃子裡或桌面陰影處，避開窗邊陽光和電器散熱口。"),
             ("h2", "這些地方不要放"),
             ("ul", ["夏天的車內：溫度很高，牛軋糖會變軟、塔皮會出油", "浴室或廚房水槽旁：濕氣重，餅皮容易受潮", "冰箱冷藏：拿出來會反潮，口感變軟"]),
             ("h2", "開封後怎麼收"),
             ("p", "單片包裝的蔥軋餅、杏仁船餅，拆一片吃一片，沒拆的繼續放盒子裡就好。整盒開過的，把盒蓋蓋好，或放進密封袋擠出空氣，並盡早吃完。"),
             ("h2", "保存期限看包裝"),
             ("p", "蔥軋餅保存期限 15 天，其他品項以包裝上的標示為準。要送人的話，記得把收到的日期算進去；送禮日還沒到，可以在蝦皮訂單備註指定出貨日。"),
             ("h2", "受潮了怎麼辦"),
             ("p", "餅乾類如果放到有點軟，可以用烤箱低溫烤 2～3 分鐘再放涼，酥脆感會回來一些。牛軋夾心的品項不建議回烤，以免牛軋融化。")]),
  dict(slug="how-to-choose-taichung-gift", date="2026-11-09", title="台中伴手禮怎麼挑？依送禮對象選對點心",
       desc="送長輩、送同事、送客戶，適合的伴手禮不一樣。整理挑選時可以看的四件事：對象、份量、包裝、保存。",
       img="tart-box.jpg",
       body=[("h2", "先想清楚送給誰"),
             ("p", "伴手禮最常見的三種場合：拜訪長輩親友、辦公室分享、公司送客戶。對象不同，要看的重點也不同。"),
             ("h3", "拜訪長輩、親友"),
             ("p", "選有提盒、拿出來好看的禮盒。口感不要太硬，份量一盒 10～12 顆剛好，不會吃不完。小小花的夏威夷豆塔附粉色提盒，提著就能出門。"),
             ("h3", "辦公室分享"),
             ("p", "選單片密封的點心，大家各拿一片不用分。份量要夠多，16～40 片依人數挑。蔥軋餅單片密封，甜鹹都有人喜歡。"),
             ("h3", "公司送客戶、企業贈禮"),
             ("p", "選外觀體面、可以大量訂的品項，並提早確認出貨日期。手工點心產量有限，建議至少提前一週詢問。"),
             ("h2", "下單前確認保存期限"),
             ("p", "手工點心沒有大量防腐，保存期限通常比較短。例如小小花的蔥軋餅保存期限 15 天。送禮時間還沒到，可以在備註指定出貨日，收到時最新鮮。"),
             ("h2", "小小花的建議組合"),
             ("ul", ["送長輩：夏威夷豆塔 10 入粉色提盒", "送同事：蔥軋餅 24 片", "送客戶：夏威夷豆塔 12 入禮盒或 24 入豪華提盒", "先試吃：單顆豆塔 + 杏仁船餅 + 鹽牛軋餅"])]),
  dict(slug="office-group-order-guide", date="2026-11-09", title="辦公室團購點心怎麼訂才不手忙腳亂",
       desc="團購點心最怕數量算錯、到貨日不對。從統計人數到指定出貨日，一次整理好。",
       img="nougat-box.jpg",
       body=[("h2", "先統計人數，再決定規格"),
             ("p", "每人一到兩片是最常見的份量。20 人左右的辦公室，蔥軋餅 24 片或 40 片就夠；想多種口味，可以加單顆夏威夷豆塔和杏仁船餅。"),
             ("h2", "選單片包裝"),
             ("p", "單片密封的點心不用拆分，拿了就走，也比較衛生。小小花的蔥軋餅、杏仁船餅、單顆豆塔、鹽牛軋餅都是單片包裝。"),
             ("h2", "提早說好到貨日"),
             ("p", "小小花每天手工現烤、每日限量，一般下單後 3 天內出貨。數量多或指定日期，請先在蝦皮聊聊告訴我們品項、數量和日期，確認產能後回覆。"),
             ("h2", "下單步驟"),
             ("ol", ["到蝦皮賣場「小小花手工烘焙」", "用聊聊告訴我們品項、數量、希望收到的日期", "確認出貨日後下單，備註寫上日期", "收到後放陰涼乾燥處，盡早分享"])]),
]

# ------------------------------------------------------------------
CSS_V = "4"

def head(title, desc, path, extra_ld=None, og_img="og.jpg"):
    url = f"{SITE}/{'' if path=='index.html' else path}"
    ld = ""
    if extra_ld:
        ld = '<script type="application/ld+json">' + json.dumps(extra_ld, ensure_ascii=False) + "</script>"
    depth = path.count("/")
    pre = "../" * depth
    return f"""<!doctype html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="zh_TW">
<meta property="og:site_name" content="小小花手工烘焙坊">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2A3530">
<link rel="icon" href="{pre}images/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC:wght@400;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}style.css?v={CSS_V}">
{ld}
</head>
<body>
<a class="skip" href="#main">跳到主要內容</a>
"""

def header(path):
    depth = path.count("/"); pre = "../" * depth
    cur = path if depth == 0 else ("menu.html" if path.startswith("products/") else "journal.html")
    links = "".join(
        f'<a href="{pre}{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}</a>' for h, t in NAV[1:])
    return f"""<header class="site-head">
  <div class="wrap head-row">
    <a class="logo" href="{pre}index.html"><img src="{pre}images/logo.jpg" alt="" width="64" height="30"><span>小小花手工烘焙坊</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">選單</button>
    <nav id="site-nav" class="site-nav">{links}<a class="nav-shop" href="{SHOP}" rel="noopener">蝦皮選購</a></nav>
  </div>
</header>
<main id="main">
"""

def footer(path):
    pre = "../" * path.count("/")
    soc = "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in SOCIAL)
    pages = "".join(f'<li><a href="{pre}{h}">{t}</a></li>' for h, t in NAV)
    return f"""</main>
<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <p class="foot-name">小小花手工烘焙坊</p>
      <p>台中・每天手工現烤・每日限量<br>蝦皮下單，3 天內出貨。</p>
      <a class="btn btn-light" href="{SHOP}" rel="noopener">到蝦皮賣場下單</a>
    </div>
    <div><p class="foot-h">網站</p><ul>{pages}</ul></div>
    <div><p class="foot-h">找到我們</p><ul>{soc}</ul></div>
  </div>
  <p class="wrap foot-note">© 2026 小小花手工烘焙坊</p>
</footer>
<script>
const b=document.querySelector('.nav-toggle'),n=document.getElementById('site-nav');
b.addEventListener('click',()=>{{const o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',String(!o));n.classList.toggle('open',!o);}});
</script>
</body>
</html>
"""

BRAND_LD = {
  "@type": ["Organization", "Brand"], "@id": f"{SITE}/#brand", "name": "小小花手工烘焙坊",
  "alternateName": ["小小花手工烘焙", "Little Flower Bakery", "小小花烘焙"],
  "url": f"{SITE}/", "logo": f"{SITE}/images/logo.jpg",
  "description": "台中的手工烘焙品牌，每天手工現烤、每日限量，招牌是夏威夷豆塔與蔥軋餅（牛軋餅），在蝦皮賣場「小小花手工烘焙」販售。",
  "address": {"@type": "PostalAddress", "addressLocality": "台中市", "addressCountry": "TW"},
  "areaServed": {"@type": "Country", "name": "台灣"},
  "sameAs": [u for _, u in SOCIAL],
  "knowsAbout": ["夏威夷豆塔", "蔥軋餅", "牛軋餅", "杏仁船餅", "台中伴手禮", "手工餅乾"]}

# 運費：蝦皮後台物流設定顯示的超商取貨運費（2026-11-13）；宅配依重量另計，不列入。
SHIPPING = [{"@type": "OfferShippingDetails", "shippingLabel": label,
             "shippingRate": {"@type": "MonetaryAmount", "value": str(fee), "currency": "TWD"},
             "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "TW"}}
            for label, fee in [("萊爾富取貨", 50), ("7-ELEVEN 取貨", 60)]]
# 退貨：店家說明「不滿意在保存期限內寄回直接退款」；保存期限 15 天，以 15 天為退貨期間上限。
RETURNS = {"@type": "MerchantReturnPolicy", "applicableCountry": "TW",
           "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
           "merchantReturnDays": 15, "returnMethod": "https://schema.org/ReturnByMail"}

def product_ld(p):
    prices = [o[1] for o in p["options"]]
    offer = ({"@type": "Offer", "price": str(prices[0])} if len(prices) == 1 else
             {"@type": "AggregateOffer", "lowPrice": str(min(prices)), "highPrice": str(max(prices)), "offerCount": len(prices)})
    offer.update({"priceCurrency": "TWD", "availability": "https://schema.org/InStock", "url": p["options"][0][2],
                  "shippingDetails": SHIPPING, "hasMerchantReturnPolicy": RETURNS})
    return {"@type": "Product", "name": p["name"], "description": p["intro"],
            "image": [f"{SITE}/images/{p['img']}"] + [f"{SITE}/images/{g}" for g in p["gallery"]],
            "brand": {"@type": "Brand", "name": "小小花手工烘焙坊"}, "offers": offer,
            "url": f"{SITE}/products/{p['slug']}.html"}

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}/{u}"} for i, (n, u) in enumerate(items)]}

def graph(*nodes): return {"@context": "https://schema.org", "@graph": list(nodes)}

def price_txt(p):
    ps = [o[1] for o in p["options"]]
    return f"NT${min(ps)}" if len(ps) == 1 else f"NT${min(ps)} 起"

def menu_board(pre, heading_level="h2"):
    rows = []
    for p in PRODUCTS:
        opts = "".join(f'<li><span class="m-opt">{n}</span><span class="m-dots" aria-hidden="true"></span><span class="m-price">NT${pr}</span></li>' for n, pr, _ in p["options"])
        rows.append(f"""<div class="m-item">
      <{heading_level} class="m-name"><a href="{pre}products/{p['slug']}.html">{p['name']}</a></{heading_level}>
      <p class="m-tag">{p['tagline']}</p>
      <ul class="m-opts">{opts}</ul>
    </div>""")
    return "\n".join(rows)

pages = {}

# ---------------- 首頁 ----------------
pre = ""
home = head("小小花手工烘焙坊｜台中伴手禮・夏威夷豆塔・蔥軋餅（牛軋餅）",
            "台中的手工烘焙坊，每天手工現烤、每日限量。夏威夷豆塔禮盒、蔥軋餅（牛軋餅）、杏仁船餅，送長輩、辦公室分享、企業贈禮都適合。網路販售，蝦皮下單 3 天內出貨。",
            "index.html", graph(BRAND_LD, {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "小小花手工烘焙坊", "inLanguage": "zh-Hant-TW", "publisher": {"@id": f"{SITE}/#brand"}}, faq_ld(FAQ[:3])))
home += header("index.html")
home += f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="hero-place">台中的手工烘焙坊</p>
      <h1>今天的豆塔，<br>剛出爐。</h1>
      <p class="hero-lead">整顆夏威夷豆排上酥脆塔皮，蔥香餅皮夾著 Q 軟牛軋。小小花每天手工現烤，烤多少、賣多少。</p>
      <div class="hero-cta">
        <a class="btn" href="{SHOP}" rel="noopener">到蝦皮選購</a>
        <a class="btn btn-line" href="menu.html">看今日出爐</a>
      </div>
    </div>
    <figure class="hero-photo">
      <img src="images/hero.jpg" alt="木砧板上剛出爐的夏威夷豆塔，整顆夏威夷豆鋪滿塔皮" width="1000" height="979" fetchpriority="high">
      <figcaption>夏威夷豆塔，單顆約 30 克</figcaption>
    </figure>
  </div>
</section>

<section class="board" aria-labelledby="board-h">
  <div class="wrap">
    <div class="board-head">
      <h2 id="board-h">今日出爐</h2>
      <p>每日限量，蝦皮下單後 3 天內出貨</p>
    </div>
    <div class="menu-grid">
{menu_board(pre, "h3")}
    </div>
    <p class="board-foot"><a href="menu.html">看每一款的介紹與保存方式</a></p>
  </div>
</section>

<section class="occasions wrap" aria-labelledby="occ-h">
  <h2 id="occ-h" class="sec-h">送給誰，挑哪一盒</h2>
  <div class="occ">
    <figure class="occ-img"><img src="images/tart-box.jpg" alt="粉色提盒裝的夏威夷豆塔禮盒" loading="lazy" width="800" height="800"></figure>
    <div class="occ-text">
      <h3>拜訪長輩、親友</h3>
      <p>夏威夷豆塔 10 入粉色提盒。提著就能出門，打開來整齊漂亮，不用再另外包裝。</p>
      <a class="text-link" href="products/macadamia-tart.html">夏威夷豆塔介紹</a>
    </div>
  </div>
  <div class="occ occ-rev">
    <figure class="occ-img"><img src="images/nougat-box.jpg" alt="單片密封的蔥軋餅放在紅色紙盒" loading="lazy" width="900" height="900"></figure>
    <div class="occ-text">
      <h3>辦公室分享、團購</h3>
      <p>蔥軋餅每片單獨密封，大家各拿一片不用分。16、24、40 片依人數挑。</p>
      <a class="text-link" href="journal/office-group-order-guide.html">辦公室團購怎麼訂</a>
    </div>
  </div>
  <div class="occ">
    <figure class="occ-img"><img src="images/box24.jpg" alt="夏威夷豆塔 24 入豪華提盒" loading="lazy" width="800" height="800"></figure>
    <div class="occ-text">
      <h3>公司送客戶、企業贈禮</h3>
      <p>12 入禮盒或 24 入豪華提盒。數量多請先聊聊，我們確認產能後回覆出貨日。</p>
      <a class="text-link" href="gifts.html">看送禮指南</a>
    </div>
  </div>
</section>

<section class="note-band">
  <div class="wrap note">
    <p class="note-big">烤多少，<br>賣多少。</p>
    <p>小小花在台中，小量手工製作，每天出爐的數量有限。把心力放在烤箱前，點心烤好、包好，就準時寄出。想吃的時候，到蝦皮賣場下單就好。</p>
  </div>
</section>

<section class="wrap journal-teaser" aria-labelledby="jt-h">
  <h2 id="jt-h" class="sec-h">烘焙日誌</h2>
  <div class="jt-list">
""" + "".join(f"""    <a class="jt" href="journal/{a['slug']}.html">
      <img src="images/{a['img']}" alt="" loading="lazy" width="600" height="600">
      <span class="jt-title">{a['title']}</span>
      <span class="jt-desc">{a['desc']}</span>
    </a>
""" for a in ARTICLES) + """  </div>
</section>
"""
home += footer("index.html")
pages["index.html"] = home

# ---------------- 今日出爐（商品總覽） ----------------
pre = ""
mp = head("今日出爐｜小小花手工烘焙坊 商品與價格",
          "小小花手工烘焙坊全部商品：夏威夷豆塔（10入、12入、24入、單顆）、蔥軋餅（16、24、40片）、杏仁船餅、鹽牛軋餅。價格與蝦皮購買連結。",
          "menu.html", graph(BRAND_LD, {"@type": "ItemList", "name": "小小花手工烘焙坊 商品",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": product_ld(p)} for i, p in enumerate(PRODUCTS)]},
            crumbs_ld([("首頁", ""), ("今日出爐", "menu.html")])))
mp += header("menu.html")
mp += f"""
<section class="page-head wrap">
  <h1>今日出爐</h1>
  <p>每天手工現烤、每日限量。點商品名稱看介紹與保存方式，點價格旁的按鈕到蝦皮下單。</p>
</section>
<section class="board board-page">
  <div class="wrap menu-grid">
{menu_board(pre)}
  </div>
</section>
<section class="wrap prod-list">
""" + "".join(f"""  <article class="prod">
    <a href="products/{p['slug']}.html" class="prod-img"><img src="images/{p['img']}" alt="{p['name']}" loading="lazy" width="800" height="800"></a>
    <div class="prod-text">
      <h2><a href="products/{p['slug']}.html">{p['name']}</a></h2>
      <p class="prod-tag">{p['tagline']}</p>
      <p>{p['intro']}</p>
      <p class="prod-meta">適合：{p['good_for']}・{price_txt(p)}</p>
      <div class="prod-cta"><a class="btn btn-sm" href="{p['options'][0][2]}" rel="noopener">蝦皮購買</a><a class="text-link" href="products/{p['slug']}.html">完整介紹</a></div>
    </div>
  </article>
""" for p in PRODUCTS) + "</section>\n"
mp += footer("menu.html")
pages["menu.html"] = mp

# ---------------- 商品頁 ----------------
for p in PRODUCTS:
    path = f"products/{p['slug']}.html"; pre = "../"
    h = head(f"{p['name']}｜{p['tagline']}｜小小花手工烘焙坊（台中）",
             f"{p['name']}：{p['intro'][:70]}價格 {price_txt(p)}，蝦皮下單 3 天內出貨。",
             path, graph(product_ld(p), crumbs_ld([("首頁", ""), ("今日出爐", "menu.html"), (p['name'], path)])), og_img=p['img'])
    h += header(path)
    gal = "".join(f'<img src="../images/{g}" alt="{p["name"]}" loading="lazy" width="600" height="600">' for g in p["gallery"])
    opts = "".join(f'<li><span class="m-opt">{n}</span><span class="m-dots" aria-hidden="true"></span><span class="m-price">NT${pr}</span><a class="btn btn-sm" href="{u}" rel="noopener">購買</a></li>' for n, pr, u in p["options"])
    others = "".join(f'<a class="jt" href="{o["slug"]}.html"><img src="../images/{o["img"]}" alt="" loading="lazy" width="600" height="600"><span class="jt-title">{o["name"]}</span><span class="jt-desc">{o["tagline"]}</span></a>' for o in PRODUCTS if o is not p)
    h += f"""
<nav class="crumbs wrap" aria-label="目前位置"><a href="../index.html">首頁</a> / <a href="../menu.html">今日出爐</a> / <span>{p['name']}</span></nav>
<section class="wrap pd">
  <figure class="pd-photo"><img src="../images/{p['img']}" alt="{p['name']}，{p['tagline']}" width="900" height="900"></figure>
  <div class="pd-text">
    <h1>{p['name']}</h1>
    <p class="pd-tag">{p['tagline']}</p>
    <p class="pd-intro">{p['intro']}</p>
    <ul class="pd-points">{''.join(f'<li>{d}</li>' for d in p['detail'])}</ul>
    <div class="pd-buy">
      <h2>規格與價格</h2>
      <ul class="m-opts m-opts-buy">{opts}</ul>
      <p class="small">價格以蝦皮賣場頁面為準。數量多或指定日期，請先在蝦皮聊聊詢問。</p>
    </div>
  </div>
</section>
<section class="wrap pd-more">
  <div><h2>適合的場合</h2><p>{p['good_for']}</p></div>
  <div><h2>保存方式</h2><p>{p['keep']}</p></div>
  <div><h2>出貨</h2><p>每天手工現烤、每日限量，蝦皮下單後 3 天內出貨。需要指定日期請在訂單備註寫明。</p></div>
</section>
{f'<section class="wrap pd-gal">{gal}</section>' if gal else ''}
<section class="wrap journal-teaser"><h2 class="sec-h">也可以搭配</h2><div class="jt-list">{others}</div></section>
"""
    h += footer(path)
    pages[path] = h

# ---------------- 送禮指南 ----------------
pre = ""
g = head("台中伴手禮送禮指南｜送長輩、同事、客戶怎麼挑｜小小花手工烘焙坊",
         "依送禮對象挑伴手禮：拜訪長輩選夏威夷豆塔提盒、辦公室分享選單片密封蔥軋餅、企業贈禮選 12 入或 24 入禮盒。附份量建議與訂購方式。",
         "gifts.html", graph(BRAND_LD, crumbs_ld([("首頁", ""), ("送禮指南", "gifts.html")])))
g += header("gifts.html")
rows = [("拜訪長輩、親友", "夏威夷豆塔 10 入粉色提盒", "NT$390", "macadamia-tart", "tart-box.jpg", "提盒拿著好看，豆塔一顆約 30 克，長輩吃也不會太大塊。"),
        ("辦公室分享（10～20 人）", "蔥軋餅 24 片", "NT$288", "nougat-cracker", "nougat-box.jpg", "單片密封，每人一到兩片剛好。甜鹹口味，大家都容易接受。"),
        ("辦公室分享（20～40 人）", "蔥軋餅 40 片禮盒附提袋", "NT$480", "nougat-cracker", "nougat-close.jpg", "人多選 40 片，附禮盒和提袋，直接放在茶水間就好。"),
        ("公司送客戶", "夏威夷豆塔 12 入禮盒", "NT$499", "macadamia-tart", "tart-12.jpg", "粉綠色禮盒，正式又不俗氣。數量多請提早一週聊聊確認出貨。"),
        ("重要客戶、大型聚會", "夏威夷豆塔 24 入豪華提盒", "NT$999", "macadamia-tart", "box24.jpg", "最大份量的提盒，適合多人分享或重要場合。"),
        ("想先試吃、婚禮小物", "單顆豆塔、杏仁船餅、鹽牛軋餅", "NT$12 起", "almond-boat", "almond-photo.jpg", "都是單片或單顆包裝，可以各買幾個先嚐，也適合當小物分送。")]
g += """
<section class="page-head wrap">
  <h1>送禮指南</h1>
  <p>同樣是伴手禮，送長輩、送同事、送客戶，適合的點心不一樣。依對象和人數，挑一盒剛好的。</p>
</section>
<section class="wrap gift-table">
""" + "".join(f"""  <article class="gift">
    <img src="images/{im}" alt="{pick}" loading="lazy" width="600" height="600">
    <div>
      <h2>{who}</h2>
      <p class="gift-pick"><a href="products/{slug}.html">{pick}</a><span>{price}</span></p>
      <p>{why}</p>
    </div>
  </article>
""" for who, pick, price, slug, im, why in rows) + f"""</section>
<section class="note-band">
  <div class="wrap note">
    <p class="note-big">數量多？<br>先聊聊再下單。</p>
    <div><p>手工點心每天產量有限。公司贈禮、團購需要一次訂比較多，請在蝦皮聊聊告訴我們品項、數量和希望收到的日期，確認產能後回覆出貨時間。</p>
    <a class="btn" href="{SHOP}" rel="noopener">到蝦皮聊聊</a></div>
  </div>
</section>
"""
g += footer("gifts.html")
pages["gifts.html"] = g

# ---------------- 日誌列表與文章 ----------------
j = head("烘焙日誌｜伴手禮挑選與團購小知識｜小小花手工烘焙坊",
         "小小花手工烘焙坊的烘焙日誌：台中伴手禮怎麼挑、辦公室團購點心怎麼訂。", "journal.html",
         graph(BRAND_LD, crumbs_ld([("首頁", ""), ("烘焙日誌", "journal.html")])))
j += header("journal.html")
j += """<section class="page-head wrap"><h1>烘焙日誌</h1><p>送禮、團購、保存，烤箱旁邊想到的事，寫下來給你參考。</p></section>
<section class="wrap journal-teaser"><div class="jt-list">""" + "".join(f"""
  <a class="jt" href="journal/{a['slug']}.html"><img src="images/{a['img']}" alt="" loading="lazy" width="600" height="600"><span class="jt-title">{a['title']}</span><span class="jt-desc">{a['desc']}</span></a>""" for a in ARTICLES) + "</div></section>\n"
j += footer("journal.html")
pages["journal.html"] = j

def render_body(body):
    out = []
    for kind, val in body:
        if kind in ("h2", "h3", "p"): out.append(f"<{kind}>{val}</{kind}>")
        else: out.append(f"<{kind}>" + "".join(f"<li>{x}</li>" for x in val) + f"</{kind}>")
    return "\n".join(out)

for a in ARTICLES:
    path = f"journal/{a['slug']}.html"
    h = head(f"{a['title']}｜小小花手工烘焙坊", a["desc"], path,
             graph({"@type": "Article", "headline": a["title"], "description": a["desc"],
                    "image": f"{SITE}/images/{a['img']}", "inLanguage": "zh-Hant-TW",
                    "datePublished": a["date"], "author": {"@type": "Organization", "name": "小小花手工烘焙坊"},
                    "publisher": {"@type": "Organization", "name": "小小花手工烘焙坊", "logo": {"@type": "ImageObject", "url": f"{SITE}/images/logo.jpg"}},
                    "mainEntityOfPage": f"{SITE}/{path}"},
                   crumbs_ld([("首頁", ""), ("烘焙日誌", "journal.html"), (a["title"], path)])), og_img=a["img"])
    h += header(path)
    h += f"""
<nav class="crumbs wrap" aria-label="目前位置"><a href="../index.html">首頁</a> / <a href="../journal.html">烘焙日誌</a> / <span>{a['title']}</span></nav>
<article class="post">
  <header class="post-head wrap-narrow">
    <h1>{a['title']}</h1>
    <p class="post-lead">{a['desc']}</p>
    <p class="post-date">{int(a['date'][:4])} 年 {int(a['date'][5:7])} 月 {int(a['date'][8:])} 日</p>
  </header>
  <figure class="post-photo wrap-narrow"><img src="../images/{a['img']}" alt="" width="900" height="900"></figure>
  <div class="post-body wrap-narrow">
{render_body(a['body'])}
    <p class="post-cta"><a class="btn" href="{SHOP}" rel="noopener">到蝦皮賣場看看</a></p>
  </div>
</article>
"""
    h += footer(path)
    pages[path] = h

# ---------------- 關於 ----------------
ab = head("關於小小花手工烘焙坊｜台中的手工烘焙小店", "小小花手工烘焙坊在台中，小量手工製作、每天現烤、每日限量，在蝦皮賣場販售。",
          "about.html", graph(BRAND_LD, crumbs_ld([("首頁", ""), ("關於小小花", "about.html")])))
ab += header("about.html")
ab += f"""
<section class="page-head wrap"><h1>關於小小花</h1></section>
<section class="wrap about">
  <figure><img src="images/tart-board.jpg" alt="剛出爐的夏威夷豆塔" width="800" height="520"></figure>
  <div class="about-text">
    <p class="note-big">手工的，就慢慢來。</p>
    <p>小小花手工烘焙坊在台中，是一間小小的手工烘焙坊。塔皮、內餡、餅皮都自己做，每天小量出爐，所以每日限量。</p>
    <p>每一批都在烤箱前看著出爐，再仔細包裝、準時寄出。想吃的時候，到蝦皮賣場「小小花手工烘焙」下單就好。</p>
    <p>我們相信一盒好吃的點心，就是最直接的心意：送長輩、謝謝同事，或是犒賞努力了一整天的自己。</p>
  </div>
</section>
<section class="wrap pd-more">
  <div><h2>每天手工現烤</h2><p>小量製作，新鮮出爐後包裝寄出，下單後 3 天內出貨。</p></div>
  <div><h2>送禮不用再包</h2><p>夏威夷豆塔附提盒或禮盒，蔥軋餅 40 片附禮盒和提袋。</p></div>
  <div><h2>大量訂購先聊聊</h2><p>公司贈禮、團購請先在蝦皮聊聊，確認產能後回覆出貨日。</p></div>
</section>
"""
ab += footer("about.html")
pages["about.html"] = ab

# ---------------- 常見問題 ----------------
fq = head("常見問題｜出貨、保存、大量訂購｜小小花手工烘焙坊", "小小花手工烘焙坊常見問題：在哪裡買、多久出貨、可以大量訂購嗎、蔥軋餅保存多久、禮盒需要另外包裝嗎。",
          "faq.html", graph(faq_ld(FAQ), crumbs_ld([("首頁", ""), ("常見問題", "faq.html")])))
fq += header("faq.html")
fq += """<section class="page-head wrap"><h1>常見問題</h1><p>找不到答案，歡迎在蝦皮聊聊或 Facebook 粉絲頁私訊。</p></section>
<section class="wrap-narrow faq">""" + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ) + "</section>\n"
fq += footer("faq.html")
pages["faq.html"] = fq

# ---------------- 輸出 ----------------
_newest = max(a["date"] for a in ARTICLES)
LASTMOD = {"index.html": _newest, "journal.html": _newest}
LASTMOD.update({f"journal/{a['slug']}.html": a["date"] for a in ARTICLES})
for path, html in pages.items():
    out = ROOT / path; out.parent.mkdir(parents=True, exist_ok=True); out.write_text(html, encoding="utf-8")
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{SITE}/{'' if p=='index.html' else p}</loc><lastmod>{LASTMOD.get(p, '2026-11-09')}</lastmod></url>\n" for p in pages) + "</urlset>\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

# llms.txt：給 ChatGPT、Perplexity 等 AI 搜尋讀的網站摘要（https://llmstxt.org 格式）
def _price(o): return f"NT${o[1]:,}"
llms = ["# 小小花手工烘焙坊", "",
        "> 台中的手工烘焙坊，每天手工現烤、每日限量。主打夏威夷豆塔、蔥軋餅（牛軋餅）、杏仁船餅、鹽牛軋餅，在蝦皮賣場「小小花手工烘焙」販售，下單後 3 天內出貨。適合送長輩、辦公室分享、團購與企業贈禮。", "",
        f"- 蝦皮賣場：{SHOP}", "- 大量訂購、指定日期：請在蝦皮聊聊或 Facebook 粉絲頁私訊", "",
        "## 商品"]
for pr in PRODUCTS:
    llms.append(f"- [{pr['name']}]({SITE}/products/{pr['slug']}.html)：{pr['tagline']}。規格：" + "、".join(f"{o[0]} {_price(o)}" for o in pr["options"]) + f"。適合：{pr['good_for']}。")
llms += ["", "## 頁面",
         f"- [今日出爐（菜單與價格）]({SITE}/menu.html)", f"- [送禮指南]({SITE}/gifts.html)",
         f"- [常見問題]({SITE}/faq.html)", f"- [關於小小花]({SITE}/about.html)", "", "## 烘焙日誌"]
llms += [f"- [{a['title']}]({SITE}/journal/{a['slug']}.html)：{a['desc']}" for a in ARTICLES]
llms += ["", "## 常見問題"] + [f"- {q} {a}" for q, a in FAQ]
(ROOT / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
print("built", len(pages), "pages")
