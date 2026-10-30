#!/usr/bin/env python3
"""Builds SmallBizWire as static HTML. Run: python3 build.py"""
import json, html, re, os
from articles import ARTICLES

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
{ld}
</head>
<body>
<header class="mast">
  <div class="mast-in">
    <a class="logo" href="/">Small<em>Biz</em>Wire</a>
    <nav><a href="/#latest">Latest</a><a href="/best-ai-assistants-for-small-business/">Tools</a><a href="/best-marketing-agencies-for-small-business/">Agencies</a><a href="/about/">About</a></nav>
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
    <p><a href="/about/">About &amp; editorial policy</a> · <a href="/sitemap.xml">Sitemap</a> · <a href="/llms.txt">llms.txt</a></p>
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
           "author": {"@type": "Organization", "name": "SmallBizWire Editors", "url": SITE + "/about/"},
           "publisher": PUB, "articleSection": a["kicker"]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": NAME, "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": a["title"], "item": SITE + path}]}]
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
    related = [ARTICLES[(idx + k) % len(ARTICLES)] for k in (1, 2, 3)]
    rel = '<section class="related"><h2>Read next</h2><div class="rel-grid">' + "".join(
        f'<a class="card" href="/{r["slug"]}/"><span class="kick">{r["kicker"]}</span><span class="ct">{r["title"]}</span></a>'
        for r in related) + "</div></section>"
    mins = max(2, round(words(a["body"]) / 230))
    body = f"""<article class="post">
  <div class="post-head">
    <span class="kick">{a['kicker']}</span>
    <h1>{a['title']}</h1>
    <p class="dek">{a['dek']}</p>
    <p class="meta">SmallBizWire Editors · <time datetime="{DATE}">30 October 2026</time> · {mins} min read</p>
  </div>
  <div class="prose">
    {disc}
    {a['body']}
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

def main():
    total = 0
    for i, a in enumerate(ARTICLES):
        write(f"/{a['slug']}/", article_page(a, i)); total += words(a["body"]) + sum(words(q + x) for q, x in a.get("faq", []))
    write("/", index_page()); write("/about/", about_page())
    urls = ["/", "/about/"] + [f"/{a['slug']}/" for a in ARTICLES]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "CCBot", "meta-externalagent"]
    open(os.path.join(ROOT, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    llms = [f"# {NAME}", "", "> A small-business marketing publication. SmallBizWire is published by Drifted Marketing (https://driftedmarketing.com), which also makes Housefly (https://heyhousefly.com). Articles that feature either carry a disclosure.", "", "## Articles", ""]
    llms += [f"- [{a['title']}]({SITE}/{a['slug']}/): {a['dek']}" for a in ARTICLES]
    llms += ["", "## About", "", f"- [About and editorial policy]({SITE}/about/)", "- [Drifted Marketing](https://driftedmarketing.com)", "- [Housefly](https://heyhousefly.com)", "- [hellodrifted.com](https://hellodrifted.com)", ""]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms))
    print("articles", len(ARTICLES), "words", total)

if __name__ == "__main__":
    main()
