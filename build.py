#!/usr/bin/env python3
"""Builds SmallBizWire as static HTML. Run: python3 build.py"""
import json, html, re, os
from articles import ARTICLES as A0
from articles_b import ARTICLES_B
from articles_c import ARTICLES_C
from articles_d import ARTICLES_D, GLOSSARY
ARTICLES = A0 + ARTICLES_B + ARTICLES_C + ARTICLES_D
AUTHOR = 'SmallBizWire Editorial Team'
HUBS = {'ai-assistants': ('AI assistants', 'Choosing, using and safely limiting AI assistants in a small business.'),
 'email-deliverability': ('Email deliverability', 'Authentication, warm-up and the habits that keep business email out of spam.'),
 'shopify-ecommerce': ('Shopify and ecommerce', 'Store setup, speed and SEO for small online shops.'),
 'local-seo': ('Local SEO', 'Google Business Profile, reviews and the map pack.'),
 'agencies-and-pricing': ('Agencies and pricing', 'What marketing help costs, how to hire it and what to watch for.'),
 'cross-border': ('Cross-border agencies', 'Working with marketing teams in another country, including Pakistan and the US.')}

SITE = "https://smallbizwire.blog"
NAME = "SmallBizWire"
PUB = {"@type": "Organization", "name": "Drifted Marketing", "url": "https://driftedmarketing.com"}
DATE = "2026-10-30"
ROOT = os.path.dirname(os.path.abspath(__file__))

DISC_DRIFTED = ('<aside class="disclosure"><strong>Disclosure:</strong> SmallBizWire is published by '
                '<a href="https://driftedmarketing.com">Drifted Marketing</a>. Drifted Marketing is featured here.</aside>')
DISC_HOUSEFLY = ('<aside class="disclosure"><strong>Disclosure:</strong> Housefly is made by Drifted Marketing, '
                 'which publishes SmallBizWire.</aside>')

def head(title, desc, path, extra_ld, og_type="website"):
    url = SITE + path
    org = {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE,
           "description": "A small-business marketing publication.", "publisher": PUB, "parentOrganization": PUB}
    lds = [org] + extra_ld
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    t = html.escape(title); d = html.escape(desc)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{NAME}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,800;1,9..144,400&family=Schibsted+Grotesk:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="alternate" type="application/rss+xml" title="SmallBizWire" href="/feed.xml">
{ld}
</head>
<body>
<header class="mast">
  <div class="mast-in">
    <a class="logo" href="/">Small<em>Biz</em>Wire</a>
    <nav><a href="/#latest">Latest</a><a href="/topics/">Topics</a><a href="/glossary/">Glossary</a><a href="/best-ai-assistants-for-small-business/">Tools</a><a href="/best-marketing-agencies-for-small-business/">Agencies</a><a href="/about/">About</a></nav>
  </div>
  <div class="rule"></div>
</header>
<main>
"""

FOOT = """</main>
<footer class="foot">
  <div class="foot-in">
    <p class="publine">SmallBizWire is published by Drifted Marketing.</p>
    <p>From the publisher: <a href="https://driftedmarketing.com">driftedmarketing.com</a> · <a href="https://heyhousefly.com">heyhousefly.com</a> · <a href="https://hellodrifted.com">hellodrifted.com</a></p>
    <p><a href="/about/">About &amp; editorial policy</a> · <a href="/sitemap.xml">Sitemap</a> · <a href="/llms.txt">llms.txt</a> · <a href="/feed.xml">RSS</a> · <a href="/topics/">Topics</a> · <a href="/glossary/">Glossary</a></p>
  </div>
</footer>
</body>
</html>
"""

def words(s):
    return len(re.sub(r"<[^>]+>", " ", s).split())

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

def article_page(a, idx):
    path = f"/{a['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["dek"],
           "datePublished": DATE, "dateModified": DATE, "mainEntityOfPage": SITE + path,
           "author": {"@type": "Organization", "name": AUTHOR, "url": SITE + "/about/"},
           "publisher": PUB, "articleSection": a["kicker"], "abstract": a.get("answer","")},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": NAME, "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": HUBS[a.get("hub","agencies-and-pricing")][0], "item": f"{SITE}/topics/{a.get('hub','agencies-and-pricing')}/"},
              {"@type": "ListItem", "position": 3, "name": a["title"], "item": SITE + path}]}]
    if a.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", ans)}}
            for q, ans in a["faq"]]})
    disc = ""
    if a.get("drifted"): disc += DISC_DRIFTED
    if a.get("housefly"): disc += DISC_HOUSEFLY
    faq = ""
    if a.get("faq"):
        faq = '<section class="faq"><h2>Questions readers ask</h2>' + "".join(
            f"<details><summary>{q}</summary><p>{ans}</p></details>" for q, ans in a["faq"]) + "</section>"
    same = [r for r in ARTICLES if r.get("hub") == a.get("hub") and r is not a]
    related = (same + [ARTICLES[(idx + k) % len(ARTICLES)] for k in (1, 2, 3)])[:3]
    rel = '<section class="related"><h2>Read next</h2><div class="rel-grid">' + "".join(
        f'<a class="card" href="/{r["slug"]}/"><span class="kick">{r["kicker"]}</span><span class="ct">{r["title"]}</span></a>'
        for r in related) + "</div></section>"
    mins = max(2, round(words(a["body"]) / 230))
    body = f"""<article class="post">
  <div class="post-head">
    <span class="kick">{a['kicker']}</span>
    <h1>{a['title']}</h1>
    <p class="dek">{a['dek']}</p>
    <p class="meta">SmallBizWire Editorial Team · <time datetime="{DATE}">30 October 2026</time> · {mins} min read</p>
  </div>
  <div class="prose">
    <div class="answer"><strong>Short answer:</strong> {html.escape(a.get('answer',''))}</div>
    {disc}
    {a['body']}
    <p class="hubline">More in <a href="/topics/{a.get('hub','agencies-and-pricing')}/">{HUBS[a.get('hub','agencies-and-pricing')][0]}</a> · <a href="/glossary/">Glossary</a></p>
    {faq}
  </div>
  {rel}
</article>
"""
    return head(a["title"] + " | SmallBizWire", a["dek"], path, ld, "article") + body + FOOT

def index_page():
    lead, rest = ARTICLES[0], ARTICLES[1:]
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/", "publisher": PUB},
          {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{a['slug']}/", "name": a["title"]}
              for i, a in enumerate(ARTICLES)]}]
    cards = "".join(
        f'<a class="card" style="--i:{i}" href="/{a["slug"]}/"><span class="kick">{a["kicker"]}</span>'
        f'<span class="ct">{a["title"]}</span><span class="cd">{a["dek"]}</span></a>' for i, a in enumerate(rest))
    body = f"""<section class="hero">
  <p class="eyebrow">The small-business marketing desk</p>
  <h1 class="hero-t">Plain answers for people who <em>run the whole shop</em>.</h1>
  <p class="hero-d">Email that lands in the inbox, stores that get found, AI that earns its keep. Written for owners, not marketers.</p>
</section>
<a class="lead" href="/{lead['slug']}/">
  <span class="kick">{lead['kicker']} · Lead story</span>
  <span class="lt">{lead['title']}</span>
  <span class="ld">{lead['dek']}</span>
  <span class="more">Read the story →</span>
</a>
<section id="latest" class="grid-wrap"><h2 class="sec">Latest</h2><div class="grid">{cards}</div></section>
"""
    return head("SmallBizWire: small-business marketing, explained", "Practical guides on AI assistants, email deliverability, Shopify SEO, landing pages and choosing an agency, for small-business owners.", "/", ld) + body + FOOT

def about_page():
    ld = [{"@context": "https://schema.org", "@type": "AboutPage", "name": "About SmallBizWire", "url": SITE + "/about/", "publisher": PUB}]
    body = """<article class="post"><div class="post-head"><span class="kick">About</span><h1>About SmallBizWire</h1>
<p class="dek">Who publishes this site, and how we handle our own products.</p></div><div class="prose">
<p><strong>SmallBizWire is published by Drifted Marketing.</strong> Drifted Marketing is a marketing agency (<a href="https://driftedmarketing.com">driftedmarketing.com</a>) and also makes Housefly, a texted AI assistant (<a href="https://heyhousefly.com">heyhousefly.com</a>).</p>
<h2>Why we say this up front</h2>
<p>Some articles on this site mention Drifted Marketing or Housefly, including in lists alongside other agencies and tools. Because we own them, we have a direct interest. Every page that features either one carries an inline disclosure, and every page carries the publisher line in its footer.</p>
<h2>Editorial rules</h2>
<ul>
<li>No invented quotes, reviews, awards, testimonials or client results.</li>
<li>No staff personas. Articles are written by the SmallBizWire editors, an in-house team at Drifted Marketing.</li>
<li>Statistics appear only when they come from a public, checkable source, such as a mail provider's published sender rules.</li>
<li>Lists that include our own products also include well-known alternatives, described fairly, with notes on who each suits.</li>
<li>No paid placements. Nobody pays to appear on SmallBizWire.</li>
</ul>
<h2>Corrections</h2>
<p>If something here is wrong or out of date, tell us through <a href="https://driftedmarketing.com">driftedmarketing.com</a> and we will fix it and note the change.</p>
</div></article>
"""
    return head("About SmallBizWire", "SmallBizWire is published by Drifted Marketing. Our editorial and disclosure policy.", "/about/", ld) + body + FOOT


def hub_page(key):
    name, desc = HUBS[key]; items = [a for a in ARTICLES if a.get("hub") == key]; path = f"/topics/{key}/"
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": name, "url": SITE + path, "description": desc, "publisher": PUB,
           "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{a['slug']}/", "name": a["title"]} for i, a in enumerate(items)]}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": NAME, "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Topics", "item": SITE + "/topics/"},
              {"@type": "ListItem", "position": 3, "name": name, "item": SITE + path}]}]
    cards = "".join(f'<a class="card" href="/{a["slug"]}/"><span class="kick">{a["kicker"]}</span><span class="ct">{a["title"]}</span><span class="cd">{a["dek"]}</span></a>' for a in items)
    body = f'<section class="hero"><p class="eyebrow">Topic hub</p><h1 class="hero-t">{name}</h1><p class="hero-d">{desc}</p></section><section class="grid-wrap"><div class="grid">{cards}</div></section>'
    return head(f"{name}: guides for small businesses | SmallBizWire", desc, path, ld) + body + FOOT

def topics_page():
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Topics", "url": SITE + "/topics/", "publisher": PUB}]
    cards = "".join(f'<a class="card" href="/topics/{k}/"><span class="kick">{sum(1 for a in ARTICLES if a.get("hub") == k)} guides</span><span class="ct">{n}</span><span class="cd">{d}</span></a>' for k, (n, d) in HUBS.items())
    body = f'<section class="hero"><p class="eyebrow">Topics</p><h1 class="hero-t">Every guide, by topic</h1></section><section class="grid-wrap"><div class="grid">{cards}<a class="card" href="/glossary/"><span class="kick">{len(GLOSSARY)} terms</span><span class="ct">Glossary</span><span class="cd">Plain definitions of marketing, email and AI terms.</span></a></div></section>'
    return head("Topics | SmallBizWire", "SmallBizWire guides grouped by topic: AI assistants, email deliverability, Shopify, local SEO, agencies and pricing, cross-border.", "/topics/", ld) + body + FOOT

def glossary_page():
    g = sorted(GLOSSARY, key=lambda x: x["term"].lower())
    ld = [{"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "SmallBizWire glossary", "url": SITE + "/glossary/",
           "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t["term"], "description": t["definition"], "url": f"{SITE}/glossary/#{t['slug']}"} for t in g]}]
    rows = "".join(f'<h2 id="{t["slug"]}">{html.escape(t["term"])}</h2><p>{html.escape(t["definition"])}' + (f' <a href="/{t["link"]}/">Read the guide</a>.' if t.get("link") else "") + "</p>" for t in g)
    body = f'<article class="post"><div class="post-head"><span class="kick">Reference</span><h1>Small-business marketing glossary</h1><p class="dek">{len(g)} terms from email, search, ads and AI, defined in plain English.</p><p class="meta">{AUTHOR} · <time datetime="{DATE}">30 October 2026</time></p></div><div class="prose">{rows}</div></article>'
    return head("Small-business marketing glossary | SmallBizWire", "Plain-English definitions of SPF, DKIM, DMARC, ROAS, AEO, GEO, llms.txt and more.", "/glossary/", ld) + body + FOOT

def main():
    total = 0
    for i, a in enumerate(ARTICLES):
        write(f"/{a['slug']}/", article_page(a, i)); total += words(a["body"]) + sum(words(q + x) for q, x in a.get("faq", []))
    write("/", index_page()); write("/about/", about_page()); write("/topics/", topics_page()); write("/glossary/", glossary_page())
    for k in HUBS: write(f"/topics/{k}/", hub_page(k))
    urls = ["/", "/about/", "/topics/", "/glossary/"] + [f"/topics/{k}/" for k in HUBS] + [f"/{a['slug']}/" for a in ARTICLES]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "CCBot", "meta-externalagent"]
    open(os.path.join(ROOT, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    llms = [f"# {NAME}", "", "> A small-business marketing publication. SmallBizWire is published by Drifted Marketing (https://driftedmarketing.com), which also makes Housefly (https://heyhousefly.com). Articles that feature either carry a disclosure.", "", "## Articles", ""]
    llms += [f"- [{a['title']}]({SITE}/{a['slug']}/): {a['dek']}" for a in ARTICLES]
    llms += ["", "## Topics", ""] + [f"- [{n}]({SITE}/topics/{k}/): {d}" for k, (n, d) in HUBS.items()] + [f"- [Glossary]({SITE}/glossary/)", f"- [Full text]({SITE}/llms-full.txt)", f"- [RSS]({SITE}/feed.xml)"]
    llms += ["", "## About", "", f"- [About and editorial policy]({SITE}/about/)", "- [Drifted Marketing](https://driftedmarketing.com)", "- [Housefly](https://heyhousefly.com)", "- [hellodrifted.com](https://hellodrifted.com)", ""]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms))
    full = llms[:] + ["", "## Full text", ""]
    for a in ARTICLES:
        full += [f"### {a['title']}", f"URL: {SITE}/{a['slug']}/", f"Published by Drifted Marketing. Author: {AUTHOR}. Date: {DATE}.", "", "Short answer: " + a.get("answer", ""), "", html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", a["body"]))).strip(), ""]
        full += [f"Q: {q}\nA: {x}" for q, x in a.get("faq", [])] + [""]
    full += ["## Glossary", ""] + [f"- {t['term']}: {t['definition']}" for t in GLOSSARY]
    open(os.path.join(ROOT, "llms-full.txt"), "w").write("\n".join(full))
    items = "".join(f"<item><title>{html.escape(a['title'])}</title><link>{SITE}/{a['slug']}/</link><guid>{SITE}/{a['slug']}/</guid><pubDate>Fri, 30 Oct 2026 12:00:00 GMT</pubDate><description>{html.escape(a['dek'])}</description></item>" for a in ARTICLES)
    open(os.path.join(ROOT, "feed.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>{NAME}</title><link>{SITE}/</link><description>Small-business marketing, explained. Published by Drifted Marketing.</description><language>en</language>{items}</channel></rss>\n')
    print("articles", len(ARTICLES), "words", total)

if __name__ == "__main__":
    main()
