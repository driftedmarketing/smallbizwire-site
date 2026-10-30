"""SmallBizWire articles, batch C: Shopify and local SEO. Generic, well-known facts only."""

ARTICLES_C = [
dict(slug="how-to-speed-up-a-shopify-store", kicker="Shopify", hub="shopify-ecommerce",
title="How do I speed up a Shopify store?",
dek="Most slow Shopify stores are slow for the same three reasons: too many apps, oversized images and a heavy theme.",
answer="Start by removing apps you no longer use, because many inject scripts on every page even after you stop using them. Then compress and correctly size your images, keep video off the top of the homepage, and choose a lean, well-maintained theme. Measure before and after with Google PageSpeed Insights so you know what actually helped.",
body="""
<p>A slow store costs you in two places. Shoppers on a phone with a weak signal give up before the page finishes loading, and search engines treat page experience as one of many signals when deciding what to show. The good news is that Shopify handles the hard infrastructure for you: hosting, a content delivery network and SSL are included on every plan. What is left in your hands is what you put on the page, and that is where nearly all of the slowness comes from.</p>
<p>This guide walks through the fixes in the order that usually gives the most improvement for the least effort. Exact gains vary from store to store, so treat any number you read online, including the rough ranges here, as a hint rather than a promise. The only number that matters is the one you measure on your own store.</p>

<h2>How do I measure my store's speed first?</h2>
<p>Before changing anything, take a baseline. Three free tools cover most needs:</p>
<ul>
<li><strong>Google PageSpeed Insights.</strong> Paste in your homepage, a collection page and a product page separately. It reports lab results and, when your store has enough traffic, real-user data from the Chrome User Experience Report.</li>
<li><strong>Shopify's own web performance report.</strong> In the admin, under Online Store or Analytics depending on your version, Shopify shows Core Web Vitals for your store. It is based on real visits rather than a single test.</li>
<li><strong>Your own phone.</strong> Load the store on mobile data, not office wifi. If it feels slow to you, it feels slow to customers.</li>
</ul>
<p>Write the results down. Test the same three pages after each change, because a fix that helps the homepage can do nothing for product pages, and the reverse.</p>

<h2>Which Core Web Vitals should I care about?</h2>
<p>Google's Core Web Vitals are three measurements of how a page feels to use:</p>
<table>
<thead><tr><th>Metric</th><th>What it measures</th><th>Usual culprit on Shopify</th></tr></thead>
<tbody>
<tr><td>Largest Contentful Paint (LCP)</td><td>How long until the main content, often the hero image, appears</td><td>A huge hero image or an autoplaying video banner</td></tr>
<tr><td>Interaction to Next Paint (INP)</td><td>How quickly the page responds when someone taps or clicks</td><td>Too much JavaScript from apps and tracking scripts</td></tr>
<tr><td>Cumulative Layout Shift (CLS)</td><td>How much the layout jumps around while loading</td><td>Pop-ups, banners and images without set dimensions</td></tr>
</tbody>
</table>
<p>Google publishes target thresholds for each one in its documentation. You do not need to memorise them; PageSpeed Insights colours each result green, amber or red for you.</p>

<h2>Why do apps slow a Shopify store down?</h2>
<p>Apps are the single most common cause of a slow Shopify store. Each app that adds something to your storefront, such as reviews, upsells, chat widgets, currency switchers or pop-ups, usually loads its own JavaScript and sometimes its own stylesheet. One app is rarely the problem. Fifteen apps, each loading on every page, add up quickly.</p>
<p>There is a second, quieter problem. On older themes, some apps edited your theme code directly when you installed them. Uninstalling the app did not always remove that code, so the store keeps trying to load files from a service you no longer pay for. Newer apps built on Shopify's theme app extensions are easier to remove cleanly, but leftovers from years past are still common.</p>
<p>A practical app audit:</p>
<ol>
<li>List every installed app and write down what it does and whether anyone still uses it.</li>
<li>Uninstall anything unused. Then check the app's documentation for any manual cleanup steps.</li>
<li>Look for overlap. Two apps doing reviews, or three doing pop-ups, is a common find.</li>
<li>Ask whether a built-in feature now covers the job. Shopify has added native features over the years that replaced the need for some apps.</li>
<li>Retest the same three pages.</li>
</ol>
<p>If you are comfortable in the theme editor, you can also search the theme code for script tags pointing to apps you have removed. If you are not, a developer can do this in an hour or two.</p>

<h2>How should I handle product and banner images?</h2>
<p>Images are usually the heaviest thing on a store page. Shopify's content delivery network automatically serves resized and modern-format versions of images to supporting browsers, which helps a great deal, but it cannot fix every habit.</p>
<ul>
<li><strong>Do not upload enormous originals.</strong> A photo straight from a modern camera can be several thousand pixels wide and many megabytes. Resize to a sensible width for your theme before uploading. Your theme documentation usually recommends sizes.</li>
<li><strong>Compress before upload.</strong> Free tools can cut file size noticeably with little visible loss. Do it once, at the source.</li>
<li><strong>Keep the hero simple.</strong> A single well-compressed image loads faster than a slideshow of five. Slideshows also tend to hurt layout shift and are often ignored by shoppers anyway.</li>
<li><strong>Be careful with video at the top.</strong> An autoplaying background video is one of the most expensive things you can put above the fold. If you want video, consider placing it lower on the page or showing a still image with a play button.</li>
<li><strong>Write alt text.</strong> It does not affect speed, but while you are in there it helps accessibility and image search. Our <a href="/shopify-product-page-seo/">guide to Shopify product page SEO</a> covers it in more detail.</li>
</ul>

<h2>Does my Shopify theme affect speed?</h2>
<p>Yes, and more than many owners expect. Shopify's Online Store 2.0 themes, including its free default themes, are generally built with performance in mind. Some third-party themes pack in dozens of features, animations and sections, and every one of them carries code even if you do not use it.</p>
<p>Things to check in your theme:</p>
<ul>
<li><strong>Is it maintained?</strong> A theme that has not been updated in years may not use current performance techniques.</li>
<li><strong>How many sections are on the homepage?</strong> Every section is more images and more code. Remove the ones that do not earn their place.</li>
<li><strong>Are you using custom fonts?</strong> Each font weight is a separate download. Two weights of one family is usually plenty.</li>
<li><strong>Is the theme heavily customised?</strong> Years of edits by different developers can leave duplicated or dead code behind.</li>
</ul>
<p>Switching themes is a bigger project than an app audit, so do it last, and only if measurements still point to the theme after you have cleaned up apps and images. Test a new theme on an unpublished copy first.</p>

<h2>What about tracking pixels and third-party scripts?</h2>
<p>Analytics, advertising pixels and heatmap tools all add JavaScript. Shopify's customer events and its built-in integrations for major ad platforms can reduce the need to paste raw code into your theme. Review what is installed, remove duplicates (the same pixel installed twice is common), and keep only the tools someone actually looks at.</p>

<h2>What speed fixes are not worth chasing?</h2>
<p>Some advice is wasted effort on Shopify. You cannot change the hosting, so offers to "move to faster servers" do not apply. Chasing a perfect score of 100 is rarely worth the cost; a store that feels fast on a phone and passes Core Web Vitals is in good shape. Be wary of apps that promise to speed up your store by adding yet another script; read reviews carefully and measure before and after, because some help and some simply add weight.</p>

<h2>What order should I do all this in?</h2>
<ol>
<li>Measure three page types and write the results down.</li>
<li>Audit and remove unused or duplicate apps.</li>
<li>Fix the hero area: one compressed image, no autoplaying video.</li>
<li>Resize and compress product and collection images going forward.</li>
<li>Remove duplicate pixels and unused scripts.</li>
<li>Trim homepage sections and font weights.</li>
<li>Only then consider a theme change.</li>
</ol>
<p>Speed is also one part of a wider picture. Once the store is quick, our <a href="/shopify-seo-guide/">Shopify SEO guide</a> covers the content and structure that help it get found, and the <a href="/landing-page-anatomy/">anatomy of a landing page</a> covers what to put on a fast page so it actually sells.</p>
<p>Recheck speed every few months, and every time you install a new app. Stores rarely get slow in one day; they get slow one small addition at a time.</p>
""",
faq=[
("Does Shopify host my store on fast servers?", "Yes. Hosting and a global content delivery network are included on every Shopify plan, so speed problems almost always come from what is on the page rather than the server."),
("How many apps is too many?", "There is no fixed number. What matters is how many load code on your storefront and whether each one is still used. Audit them and measure before and after removing any."),
("Will a speed optimisation app fix my store?", "Sometimes, but some add their own scripts. Measure your pages before and after installing one and keep it only if the numbers improve."),
("Do I need a perfect PageSpeed score?", "No. Aim for passing Core Web Vitals and a store that feels quick on a phone. A perfect score is rarely worth the cost."),
("Should I switch themes to get faster?", "Only after removing unused apps and fixing images. If measurements still point to the theme, test a lean, maintained theme on an unpublished copy first."),
],
drifted=False, housefly=False),

dict(slug="shopify-vs-woocommerce-vs-squarespace", kicker="Platforms", hub="shopify-ecommerce",
title="Shopify vs WooCommerce vs Squarespace: which is best for a small shop?",
dek="A fair comparison of the three platforms small shops most often choose between, and the questions that decide it.",
answer="Shopify suits most shops that want to sell seriously without managing technology, because hosting, checkout and security are handled for you. WooCommerce suits owners who want full control and are comfortable maintaining a WordPress site. Squarespace suits businesses whose shop is a smaller part of a design-led website. Check each platform's current pricing before deciding.",
body="""
<p>Choosing an ecommerce platform is one of the few decisions in a small business that is genuinely painful to reverse. Moving products, customers, order history and search rankings from one platform to another is possible, but it takes time and carries risk. So it is worth an hour of honest thinking before you start.</p>
<p>Shopify, WooCommerce and Squarespace are three of the most common choices for small shops. They are built on very different ideas, and each is the right answer for some businesses and the wrong answer for others. This comparison sticks to well-known, stable differences. Prices, fees and plan names change often, so check each platform's own pricing page on the day you decide rather than trusting any figure in an article, including this one.</p>

<h2>What is the basic difference between the three?</h2>
<ul>
<li><strong>Shopify</strong> is a hosted platform built specifically for selling. You pay a monthly subscription and Shopify runs the servers, security, checkout and updates.</li>
<li><strong>WooCommerce</strong> is a free, open-source plugin that turns a WordPress website into a shop. The software is free, but you arrange and pay for hosting, and you are responsible for updates, security and backups, or for paying someone to handle them.</li>
<li><strong>Squarespace</strong> is a hosted website builder known for polished templates, with commerce features built in. It is a website-first tool that also sells, rather than a shop-first tool.</li>
</ul>

<h2>How do they compare side by side?</h2>
<table>
<thead><tr><th>Question</th><th>Shopify</th><th>WooCommerce</th><th>Squarespace</th></tr></thead>
<tbody>
<tr><td>Who runs hosting and security?</td><td>Shopify</td><td>You or your host</td><td>Squarespace</td></tr>
<tr><td>Software cost</td><td>Monthly subscription</td><td>Plugin is free; hosting, theme and extensions cost extra</td><td>Monthly subscription; commerce on selected plans</td></tr>
<tr><td>Ease of setup</td><td>Easy</td><td>Moderate; WordPress familiarity helps</td><td>Easy</td></tr>
<tr><td>Control over code and data</td><td>Good, within Shopify's rules</td><td>Highest; you own the whole stack</td><td>More limited</td></tr>
<tr><td>Extensions</td><td>Large app store</td><td>Very large plugin ecosystem</td><td>Smaller set of extensions</td></tr>
<tr><td>Best fit</td><td>Shops where selling is the main business</td><td>Owners wanting full control or already on WordPress</td><td>Design-led sites with a modest catalogue</td></tr>
</tbody>
</table>
<p>None of these rows is a winner on its own. A row that looks like a weakness for one business is a strength for another.</p>

<h2>What does each platform really cost?</h2>
<p>The headline monthly price rarely tells the whole story. When comparing, add up:</p>
<ol>
<li><strong>The base plan.</strong> Shopify and Squarespace publish tiered plans. WooCommerce itself is free.</li>
<li><strong>Hosting.</strong> Included with Shopify and Squarespace. For WooCommerce, quality managed WordPress hosting is a real monthly cost, and cheap shared hosting can make a busy shop slow.</li>
<li><strong>Payment processing.</strong> All three charge or pass on card processing fees. Shopify has historically charged an extra transaction fee when you use a third-party payment provider instead of its own; check whether that applies to you and in your country.</li>
<li><strong>Themes.</strong> Free themes exist on all three. Premium themes are a one-off or annual cost.</li>
<li><strong>Apps, plugins and extensions.</strong> This is where costs creep. Many useful apps charge monthly.</li>
<li><strong>Your time or a developer's time.</strong> WooCommerce in particular needs ongoing maintenance: plugin updates, compatibility checks and backups.</li>
</ol>
<p>A fair comparison is a year's total cost of the setup you actually need, not the cheapest plan on each pricing page.</p>

<h2>When is Shopify the right choice?</h2>
<p>Shopify tends to suit businesses where the shop is the business. Its strengths are a fast, trusted checkout, built-in inventory and order management, a large app store, and the fact that you never have to think about servers or security patches. It handles growth well: a store with ten products and a store with thousands run on the same system.</p>
<p>The trade-offs are that you work within Shopify's structure. Some URL patterns are fixed, deep checkout customisation is limited on lower plans, and monthly app costs can add up. If you go this way, our <a href="/shopify-seo-guide/">Shopify SEO guide</a> covers how to work with its structure rather than against it.</p>

<h2>When is WooCommerce the right choice?</h2>
<p>WooCommerce suits owners who want full ownership. Because it runs on WordPress, you can change almost anything, move to any host, and use WordPress's very strong publishing tools for a content-heavy site. If your business already runs on WordPress, adding WooCommerce can be the simplest path.</p>
<p>The trade-off is responsibility. You, or someone you pay, must keep WordPress, WooCommerce, the theme and every plugin updated and compatible. Security is your job. Performance depends on your hosting. For a business without technical help, that responsibility is the real cost.</p>

<h2>When is Squarespace the right choice?</h2>
<p>Squarespace suits businesses whose website is mostly about presentation, with selling as one part: a photographer selling prints, a studio selling a few classes, a restaurant selling gift cards, a maker with a small catalogue. Its templates are polished and its editor is easy for non-technical owners.</p>
<p>The trade-off is depth. For larger catalogues, complex variants, wholesale pricing or heavy integrations, owners often find they outgrow it. That is not a flaw so much as a matter of focus.</p>

<h2>What questions should decide it for my shop?</h2>
<ul>
<li><strong>How many products will you sell in two years?</strong> A handful favours simplicity; hundreds favour a commerce-first platform.</li>
<li><strong>Who will maintain it?</strong> If the answer is "nobody technical," lean toward a hosted platform.</li>
<li><strong>How important is content?</strong> If blogging and long articles are central, WordPress's publishing tools are a real advantage.</li>
<li><strong>Where do you sell besides your site?</strong> Check which platforms connect cleanly with the marketplaces and social channels you use.</li>
<li><strong>What payment providers work in your country?</strong> Availability varies by region. Check before you commit.</li>
<li><strong>What is your total yearly budget?</strong> Including apps and help, not just the base plan.</li>
</ul>

<h2>How hard is it to switch later?</h2>
<p>All three let you export products and customers, and migration tools and services exist. The hard parts are usually redirects from old URLs to new ones (so you keep your search rankings), rebuilding design, reconnecting apps and re-testing checkout. Planning redirects properly is the single most important step. Whatever you choose, build a clear page for each product from the start; our <a href="/shopify-product-page-seo/">product page guide</a> covers principles that apply on any platform.</p>
<p>Most platforms offer a free trial. Use it seriously: add five real products, run a test order, and try editing a page on your phone. An afternoon of hands-on testing will tell you more than any comparison table.</p>
""",
faq=[
("Is WooCommerce really free?", "The plugin is free, but you pay for hosting, and often for a premium theme, extensions and maintenance. Compare a full year's cost, not the software price alone."),
("Which platform is easiest for a beginner?", "Shopify and Squarespace are generally easier because hosting and security are handled for you. WooCommerce is easier if you already know WordPress."),
("Does Shopify charge transaction fees?", "Shopify has historically added a fee when you use a third-party payment provider instead of its own. Check its current pricing page for your plan and country."),
("Can I move from Squarespace to Shopify later?", "Yes. Products and customers can be exported. Plan redirects from old URLs to new ones carefully so you keep your search rankings."),
("Which is best for SEO?", "All three can rank well. Content quality, structure and speed matter far more than the platform choice for most small shops."),
],
drifted=False, housefly=False),

dict(slug="shopify-collection-page-seo", kicker="Shopify SEO", hub="shopify-ecommerce",
title="How do I write Shopify collection pages that rank?",
dek="Collection pages often target the search terms with the most buyers. Most stores leave them as a bare grid of products.",
answer="Treat each collection as a landing page for one clear search term. Give it a descriptive title and handle, a short intro above the products that tells shoppers what is in the collection, helpful copy below, and a unique meta description. Link to it from navigation and related products, and avoid near-duplicate collections competing for the same term.",
body="""
<p>When someone searches "linen bath towels" or "women's leather ankle boots," they usually want to see a range, not a single product. That is exactly what a collection page is. In many stores, collection pages are the pages best matched to the searches with the most buying intent, yet they are often the thinnest pages on the site: a heading, a grid of thumbnails and nothing else.</p>
<p>This guide covers how to turn a Shopify collection into a page that search engines understand and shoppers find useful. It complements our <a href="/shopify-product-page-seo/">guide to Shopify product page SEO</a>, which handles the individual product level.</p>

<h2>What makes a collection page rank?</h2>
<p>Search engines are trying to show the page that best answers a query. For a collection, that means three things:</p>
<ul>
<li><strong>Clear relevance.</strong> The page is plainly about one kind of product, and its title, heading and copy say so.</li>
<li><strong>Usefulness.</strong> It helps a shopper choose: a good range, sensible filters, and a little guidance.</li>
<li><strong>Signals of importance.</strong> Your own site links to it prominently, and ideally other sites link to it too.</li>
</ul>
<p>None of this is a trick. It is the same thing a good shop assistant does: put the right products together, label the shelf, and point people to it.</p>

<h2>How do I choose the search term for each collection?</h2>
<p>Each collection should target one main term and its close variations. Start by listing how customers actually describe the products. Use your own site search data, questions customers ask, and the suggestions that appear as you type into Google. Free and paid keyword tools can give rough search volumes, but treat them as estimates.</p>
<p>A good collection term is specific enough to match intent and broad enough to justify a range. "Towels" may be too broad to win; "cotton bath towels" is a clearer target; "blue cotton bath towel 70x140" is probably a single product.</p>
<p>Write the plan down in a simple table:</p>
<table>
<thead><tr><th>Collection</th><th>Main search term</th><th>Close variations</th></tr></thead>
<tbody>
<tr><td>Cotton bath towels</td><td>cotton bath towels</td><td>100% cotton towels, soft bath towels</td></tr>
<tr><td>Kids' bath towels</td><td>kids hooded towels</td><td>children's bath towels, toddler towels</td></tr>
<tr><td>Beach towels</td><td>beach towels</td><td>large beach towels, sand-free towels</td></tr>
</tbody>
</table>
<p>If two collections want the same term, merge them or make their focus clearly different. Two near-identical collections split your effort and can confuse search engines about which one to show.</p>

<h2>What should go in the title, handle and meta description?</h2>
<ul>
<li><strong>Collection title.</strong> This becomes the page heading in most themes. Use the plain name customers search for: "Cotton Bath Towels," not "The Cloud Edit."</li>
<li><strong>SEO title.</strong> Set in the collection's search engine listing section. Lead with the term, then the brand: "Cotton Bath Towels | Your Store Name." Keep it short enough that it is not cut off in results.</li>
<li><strong>Handle (URL).</strong> Shopify collection URLs follow the pattern /collections/handle. Keep the handle short and descriptive: cotton-bath-towels. If you change an existing handle, make sure a redirect from the old URL is in place; Shopify offers to create one when you edit it.</li>
<li><strong>Meta description.</strong> One or two sentences that say what is in the collection and why to click. Google may rewrite it, but a good one often gets used.</li>
</ul>

<h2>How much text should a collection page have?</h2>
<p>Enough to help, not so much that it buries the products. A pattern that works on most themes:</p>
<ol>
<li><strong>A short intro above the grid.</strong> Two to four sentences that confirm what the collection is and who it is for. Shoppers should see products without scrolling far.</li>
<li><strong>The product grid</strong>, with filters that match how people choose: size, colour, material, price.</li>
<li><strong>Longer, useful copy below the grid.</strong> How to choose between options, care instructions, sizing guidance, and answers to common questions. Many themes support a section below products; if yours does not, a developer can add one using a metafield.</li>
</ol>
<p>Write for a shopper, not for a search engine. Repeating the search term in every sentence reads badly and does not help. Mention it naturally in the heading, the intro and once or twice below.</p>

<h2>How do I avoid duplicate content on collections?</h2>
<p>Shopify can produce several URLs for the same product, such as a product URL nested under a collection path. Shopify's themes generally set a canonical tag pointing to the main product URL, which tells search engines which version to treat as the original. Check that your theme does this; most current themes do.</p>
<p>Filtered and sorted views of collections can also generate many URL variations. Shopify's native filtering is generally handled sensibly, but if you use a third-party filter app, check how it creates URLs and whether those pages are being indexed. Google Search Console's page indexing report is the place to look.</p>
<p>Finally, avoid copying the same intro text across many collections. Each collection should have its own words.</p>

<h2>How should I link to my collections?</h2>
<p>Internal links tell search engines which pages you consider important. Your most valuable collections should be:</p>
<ul>
<li>In the main navigation or a clear sub-menu.</li>
<li>Linked from the homepage, where it makes sense.</li>
<li>Linked from related product pages, for example "See all cotton bath towels."</li>
<li>Linked from blog posts or guides on related topics, using descriptive anchor text rather than "click here."</li>
</ul>
<p>Breadcrumbs, which many themes include, also help both shoppers and search engines understand where a page sits.</p>

<h2>Should I add structured data to collection pages?</h2>
<p>Structured data helps search engines read a page's content. On collection pages, breadcrumb markup is the most widely useful. Product markup belongs on individual product pages. Many themes include basic structured data already; check with Google's Rich Results Test before adding more, so you do not duplicate it.</p>

<h2>How do I keep collections working over time?</h2>
<ul>
<li><strong>Keep them stocked.</strong> A collection full of sold-out products is a poor result for a shopper. Consider sorting in-stock items first.</li>
<li><strong>Do not delete seasonal collections every year.</strong> A collection that ranks for "Christmas gift sets" can be refreshed and reused rather than rebuilt from scratch, keeping its history.</li>
<li><strong>Review in Search Console.</strong> See which collections appear for which searches, and whether click-through is low (a sign the title or description could be clearer).</li>
<li><strong>Keep the page fast.</strong> Large grids of big images slow things down. Our guide on <a href="/how-to-speed-up-a-shopify-store/">speeding up a Shopify store</a> covers the fixes.</li>
</ul>
<p>Collection pages are rarely glamorous work. They are also some of the most reliable pages a small store can improve, because the demand already exists; the page just needs to answer it clearly. For the wider picture of structure and content across your store, see our <a href="/shopify-seo-guide/">Shopify SEO guide</a>.</p>
""",
faq=[
("Should collection pages have text?", "Yes. A short intro above the products and helpful copy below helps shoppers choose and helps search engines understand what the page is about."),
("Can I change a collection's URL handle?", "Yes, but set up a redirect from the old URL so you keep any rankings and links. Shopify offers to create one when you edit the handle."),
("Do filtered collection URLs cause duplicate content?", "They can, depending on the filter app. Check how it builds URLs and review Google Search Console's page indexing report for unwanted pages."),
("How long should a collection intro be?", "Two to four sentences above the grid is usually enough. Put longer guidance below the products so shoppers see items first."),
("Should two collections target the same keyword?", "No. Merge them or give each a clearly different focus, so they do not compete with each other."),
],
drifted=False, housefly=False),

dict(slug="how-to-get-more-google-reviews", kicker="Local SEO", hub="local-seo",
title="How do I get more Google reviews without breaking the rules?",
dek="Asking every customer is allowed. Paying for reviews, offering discounts for them, or only asking happy customers is not.",
answer="Ask every customer, at the right moment, with a direct link to your review form, and make it quick. Google's policies prohibit offering incentives for reviews and selectively asking only satisfied customers, a practice called review gating. Reply to every review, good and bad, and never post fake reviews or have staff review the business.",
body="""
<p>Reviews on your Google Business Profile do two jobs at once. They help potential customers decide whether to trust you, and Google lists review count and score among the things that contribute to a business's prominence in local results. So it is natural to want more of them.</p>
<p>The problem is that many common tactics break Google's rules, and the consequences can include reviews being removed, restrictions on your profile, or in some cases warnings shown to the public. In several countries, fake or misleading reviews are also a consumer protection issue. This guide covers what is allowed, what is not, and a simple system for steadily earning genuine reviews.</p>
<p>Google's policies change over time, so read the current version of its prohibited and restricted content policy for maps reviews before you set up any process. What follows reflects its long-standing positions.</p>

<h2>What does Google prohibit when it comes to reviews?</h2>
<ul>
<li><strong>Incentives.</strong> Offering money, discounts, free products, entry into a prize draw or anything else in exchange for a review. This applies even if you do not ask for a positive review.</li>
<li><strong>Review gating.</strong> Asking customers first whether they had a good experience, then only sending the happy ones to Google and the unhappy ones to a private feedback form.</li>
<li><strong>Fake reviews.</strong> Reviews from people who were not customers, reviews you write yourself, or reviews bought from a service.</li>
<li><strong>Conflicts of interest.</strong> Owners or staff reviewing their own business, or reviewing competitors.</li>
<li><strong>Bulk or on-site review stations</strong> that produce many reviews from one device or location can be flagged as suspicious, so let customers review on their own devices.</li>
</ul>
<p>Some review platforms other than Google have their own, sometimes stricter, rules about asking at all. Check each platform's policy separately.</p>

<h2>What is allowed?</h2>
<p>Quite a lot. You can:</p>
<ul>
<li>Ask every customer for a review, as long as you ask them all, not only the ones you expect to be happy.</li>
<li>Make it easy with a direct link or QR code to your review form.</li>
<li>Remind customers once, politely, if they have not left one.</li>
<li>Reply publicly to reviews.</li>
<li>Flag reviews that genuinely break Google's policies, such as spam or off-topic content, for Google to assess.</li>
</ul>
<p>The principle is simple: you may invite feedback, but you may not buy it, filter it or fake it.</p>

<h2>How do I get my review link?</h2>
<p>Google lets you share a short link that opens the review form for your business directly. You can find it from your Business Profile, usually under an option labelled something like "Ask for reviews" or "Get more reviews." The exact menu wording has changed over the years, so look in your profile's management view in Google Search or Maps. Google can also generate a QR code for the same link.</p>
<p>Use that one link everywhere. Do not send customers to your profile and hope they find the review button.</p>

<h2>When is the best time to ask for a review?</h2>
<p>Ask when the customer has just experienced the value and the memory is fresh:</p>
<table>
<thead><tr><th>Type of business</th><th>Good moment to ask</th><th>How</th></tr></thead>
<tbody>
<tr><td>Restaurant or café</td><td>As the bill is settled</td><td>A small card or QR code on the table or receipt</td></tr>
<tr><td>Tradesperson or home service</td><td>When the job is finished and checked</td><td>A text message with the link the same day</td></tr>
<tr><td>Clinic, salon or studio</td><td>After the appointment</td><td>A follow-up email or text</td></tr>
<tr><td>Online shop with local pickup</td><td>A few days after delivery or collection</td><td>An order follow-up email</td></tr>
<tr><td>Professional service</td><td>At a natural milestone, such as project handover</td><td>A personal email from the person they worked with</td></tr>
</tbody>
</table>

<h2>What should the request say?</h2>
<p>Short, personal and specific. A good request:</p>
<ol>
<li>Thanks them by name.</li>
<li>Mentions what you did for them.</li>
<li>Asks for an honest review, not a five-star one.</li>
<li>Includes the direct link.</li>
<li>Says it takes a minute or two.</li>
</ol>
<p>For example: "Thanks again for choosing us for your kitchen repair, Sam. If you have a minute, we'd really value an honest review on Google. It helps other people nearby find us. Here's the link." Asking for an "honest" review keeps you clearly on the right side of the rules and tends to read as more trustworthy.</p>

<h2>How do I build this into a routine?</h2>
<p>Reviews come from consistency, not from occasional campaigns. A burst of reviews followed by silence can also look odd. Set a simple routine:</p>
<ul>
<li>Decide the single moment you will ask, for every customer.</li>
<li>Add the request to your checklist, booking system, or invoicing tool so it happens automatically or as part of a habit.</li>
<li>Train staff to mention it verbally too, without pressure.</li>
<li>Send one reminder after a few days to anyone who has not reviewed. Then stop.</li>
<li>Check monthly how many requests went out and how many reviews came in.</li>
</ul>

<h2>How should I reply to reviews?</h2>
<p>Reply to every review, positive and negative. Replies show prospective customers that a real person is paying attention.</p>
<ul>
<li><strong>Positive reviews:</strong> thank them, mention something specific from their review, and keep it short.</li>
<li><strong>Negative reviews:</strong> stay calm and polite, acknowledge the experience, avoid sharing private details, and offer to resolve it offline with a contact method. Future customers read how you handle complaints more closely than the complaint itself.</li>
<li><strong>Reviews that break policy:</strong> you can flag them for Google to assess. Google decides; it does not remove reviews simply because they are negative.</li>
</ul>
<p>Never offer a customer something in exchange for changing or removing a review. That is also an incentive.</p>

<h2>What about review software and agencies?</h2>
<p>Many tools automate review requests, and plenty work within the rules. Before using one, check that it sends requests to all customers rather than filtering by a satisfaction score first. Avoid any service that offers to supply reviews. If something sounds like a shortcut, it probably breaks the policy.</p>
<p>Reviews are one part of your wider local presence. Our <a href="/google-business-profile-local-seo/">guide to Google Business Profile and local SEO</a> covers the rest of the profile, and our explainer on <a href="/how-to-rank-in-the-google-map-pack/">ranking in the Google map pack</a> shows where reviews fit among the factors Google names.</p>
""",
faq=[
("Can I offer a discount for a Google review?", "No. Google's policies prohibit offering incentives of any kind in exchange for reviews, even if you do not ask for a positive one."),
("What is review gating?", "Asking customers whether they were happy first, then only sending satisfied ones to Google. Google prohibits it. Ask every customer instead."),
("Can my staff leave reviews for the business?", "No. Reviews from owners or employees are a conflict of interest under Google's policies."),
("Can I get a negative review removed?", "Only if it breaks Google's policies, such as spam or off-topic content. You can flag it, and Google decides. Replying calmly is usually the better response."),
("Is it okay to send a reminder?", "Yes. One polite reminder to customers who have not left a review is fine. Repeated pressure is not a good look."),
],
drifted=False, housefly=False),

dict(slug="what-is-nap-consistency", kicker="Local SEO", hub="local-seo",
title="What is NAP consistency and why does it matter for local SEO?",
dek="NAP stands for name, address and phone number. When they differ across the web, customers and search engines both get confused.",
answer="NAP consistency means your business name, address and phone number appear the same way everywhere they are listed online: your website, Google Business Profile, directories and social profiles. Consistent details help search engines confidently match listings to one real business, and they stop customers calling an old number or driving to an old address.",
body="""
<p>NAP is one of the oldest ideas in local search, and it remains one of the most practical. The acronym stands for <strong>name, address and phone number</strong>. Some people add a W for website, making it NAPW. The idea is that these core details should be identical, or as close to identical as possible, everywhere your business appears online.</p>
<p>This article explains why that matters, what counts as inconsistent, and how to audit and fix your listings without spending a fortune.</p>

<h2>Why does NAP consistency matter?</h2>
<p>There are two audiences: people and search engines.</p>
<p><strong>For people,</strong> the reason is obvious. If a directory lists your old phone number, someone who finds you there calls a dead line or, worse, your previous tenant. If an old address appears on a map app, a customer drives to the wrong place and is unlikely to give you a second chance.</p>
<p><strong>For search engines,</strong> the reason is about confidence. Google and other search engines gather information about local businesses from many sources: your Business Profile, your website, directories, data aggregators and more. When those sources agree, it is easier to be confident they describe one real business at one real location. When they disagree, the picture gets muddier. Google lists prominence, which it describes as how well known a business is, including information from across the web, among the factors in local ranking.</p>
<p>How much NAP consistency directly moves rankings today is debated among practitioners, and nobody outside Google can measure it precisely. What is not in doubt is that wrong details cost real customers. That alone justifies the work.</p>

<h2>What counts as an inconsistency?</h2>
<p>Some differences matter more than others:</p>
<table>
<thead><tr><th>Type of difference</th><th>Example</th><th>How serious</th></tr></thead>
<tbody>
<tr><td>Wrong or old phone number</td><td>A number you stopped using last year</td><td>Serious; loses calls</td></tr>
<tr><td>Wrong or old address</td><td>Your previous premises</td><td>Serious; loses visits and confuses maps</td></tr>
<tr><td>Different business name</td><td>An old trading name or added keywords</td><td>Serious; can look like two businesses</td></tr>
<tr><td>Formatting differences</td><td>"Street" vs "St.", "Suite 4" vs "#4"</td><td>Minor; search engines usually handle these</td></tr>
<tr><td>Tracking or call-forwarding numbers</td><td>A different number on each directory</td><td>Can be moderate; see below</td></tr>
</tbody>
</table>
<p>Do not lose sleep over abbreviations. Focus first on anything that is factually wrong.</p>

<h2>What should my "official" NAP be?</h2>
<p>Before you fix anything, decide on a single, canonical version and write it down:</p>
<ul>
<li><strong>Name:</strong> your real-world business name, as on your signage and paperwork. Do not add keywords or locations that are not part of the name; Google's guidelines for Business Profiles specifically warn against this.</li>
<li><strong>Address:</strong> formatted the way your national postal service formats it. If you are a service-area business that does not serve customers at your address, you may hide the address on Google; see our <a href="/local-seo-checklist-for-service-area-businesses/">local SEO checklist for service-area businesses</a>.</li>
<li><strong>Phone:</strong> a local number where possible, the one you actually answer.</li>
<li><strong>Website:</strong> the exact main URL, consistently with or without "www."</li>
</ul>
<p>Every listing you create or correct from now on should match this record.</p>

<h2>Where does my NAP appear online?</h2>
<p>More places than most owners realise. Common ones include:</p>
<ul>
<li>Your Google Business Profile.</li>
<li>Your own website, especially the footer and contact page.</li>
<li>Apple Business Connect, which feeds Apple Maps, and Bing Places for Business.</li>
<li>Social profiles such as Facebook and Instagram.</li>
<li>General directories and review sites relevant to your country.</li>
<li>Industry-specific directories and trade associations.</li>
<li>Local chamber of commerce, council or community listings.</li>
<li>Old listings created automatically by data providers that you never claimed.</li>
</ul>

<h2>How do I audit my listings?</h2>
<ol>
<li><strong>Search for your business name</strong> in Google, then your name plus your city, and note every listing on the first few pages.</li>
<li><strong>Search for your old phone numbers and old addresses.</strong> This finds listings that use your previous details, which a name search can miss.</li>
<li><strong>Check the major maps platforms</strong> directly: Google, Apple and Bing.</li>
<li><strong>Record everything in a spreadsheet:</strong> the site, the URL, what it shows, whether you control it, and what needs fixing.</li>
<li><strong>Prioritise</strong> by how many people are likely to see each listing. The big maps platforms first, then the directories that rank for your name.</li>
</ol>
<p>Paid listing-management services can scan and update many directories at once. They can save time, especially for multi-location businesses, but they are not required for a small business with a handful of listings. If you use one, check what happens to your listings if you stop paying.</p>

<h2>How do I fix incorrect listings?</h2>
<ul>
<li><strong>Listings you control:</strong> log in and update them.</li>
<li><strong>Listings you can claim:</strong> most directories have a "claim this business" process, often with verification by phone, email or post.</li>
<li><strong>Listings you cannot claim:</strong> look for a "suggest an edit" or contact option.</li>
<li><strong>Duplicates:</strong> if Google shows two profiles for your business, Google's support documentation explains how to request that duplicates be merged or removed.</li>
</ul>
<p>Corrections can take weeks to show up, and some directories pull data from aggregators, so an old number may reappear until the source is fixed. Keep the spreadsheet and recheck after a month or two.</p>

<h2>What about call tracking numbers?</h2>
<p>Many businesses want to know which listing or campaign generated a call, so they use different tracking numbers. Using many different numbers across directories works against NAP consistency. A common approach is to keep your main number as the primary number on your Google Business Profile and directories, and use tracking numbers only in ads or campaigns where you control them. Google Business Profile also allows additional phone numbers; check its current guidance before setting this up.</p>

<h2>What should I do when I move or change my number?</h2>
<p>This is when consistency breaks most often. Make a list from your spreadsheet before the change, update the maps platforms and your website on the day, and work through directories within the following weeks. Keep the old number forwarding for a while if you can.</p>
<p>NAP consistency is not exciting, but it is foundational. It sits underneath everything in our <a href="/google-business-profile-local-seo/">guide to Google Business Profile and local SEO</a>, and it supports the prominence factor covered in our article on <a href="/how-to-rank-in-the-google-map-pack/">ranking in the Google map pack</a>.</p>
""",
faq=[
("What does NAP stand for?", "Name, address and phone number. Some people add website and call it NAPW."),
("Do abbreviations like St. versus Street matter?", "Usually not much. Search engines generally handle formatting differences. Focus on details that are actually wrong, such as an old number or address."),
("Should I use a tracking number on my Google Business Profile?", "Be careful. A common approach is to keep your main number as primary and use tracking numbers only in campaigns you control. Check Google's current guidance."),
("Do I need a paid listing management service?", "Not usually for a small business with a few listings. It can save time for multi-location businesses. Check what happens to listings if you stop paying."),
("How long do corrections take to appear?", "Often weeks. Some directories pull data from aggregators, so recheck after a month or two and fix the source if old details return."),
],
drifted=False, housefly=False),

dict(slug="how-to-rank-in-the-google-map-pack", kicker="Local SEO", hub="local-seo",
title="How do I rank in the Google map pack?",
dek="Google says local results are based mainly on relevance, distance and prominence. Here is what you can influence in each.",
answer="Google says local results depend mainly on three factors: relevance (how well your profile matches the search), distance (how far you are from the searcher or the searched location) and prominence (how well known your business is). You cannot change distance, so focus on a complete, accurate Business Profile, genuine reviews, a strong website and real local reputation.",
body="""
<p>The map pack is the block of local businesses, usually three, that appears with a map near the top of Google results when someone searches for something like "plumber near me" or "coffee in Clifton." For many local businesses, it is the most valuable spot on the internet. It is also the subject of a great deal of confident guesswork.</p>
<p>The useful starting point is what Google itself says. In its Business Profile help documentation, Google states that local results are based mainly on three factors: <strong>relevance, distance and prominence</strong>. It also says there is no way to request or pay for a better local ranking. Everything else in this article builds on those three factors.</p>

<h2>What are the three factors Google names?</h2>
<table>
<thead><tr><th>Factor</th><th>What Google means</th><th>Can you influence it?</th></tr></thead>
<tbody>
<tr><td>Relevance</td><td>How well a local profile matches what someone is searching for</td><td>Yes, through a complete and accurate profile</td></tr>
<tr><td>Distance</td><td>How far each result is from the location used in the search</td><td>Not really; your location is your location</td></tr>
<tr><td>Prominence</td><td>How well known a business is, including information from across the web, reviews and ratings</td><td>Yes, over time</td></tr>
</tbody>
</table>
<p>Google has also said that a business's position in general web results is a factor in prominence. In other words, your website's overall search performance can help your map visibility too.</p>

<h2>How do I improve relevance?</h2>
<p>Relevance is about giving Google a clear, complete picture of what you do. Most of it lives in your Google Business Profile.</p>
<ul>
<li><strong>Choose the right primary category.</strong> This is one of the most important choices on the profile. Pick the most specific category that describes your core business, then add a few accurate secondary categories. Do not add categories for services you do not really offer.</li>
<li><strong>Fill in every relevant field.</strong> Hours, services or products, attributes, service areas, description and opening date. Google says complete, accurate information helps it match you to searches.</li>
<li><strong>Use your real business name.</strong> Adding keywords to the name breaks Google's guidelines and can get a profile suspended.</li>
<li><strong>List your services clearly.</strong> Where the profile allows services or products, add them with plain descriptions that match how customers speak.</li>
<li><strong>Keep hours accurate,</strong> including holiday hours. A business shown as closed is unlikely to be shown for "open now" searches.</li>
<li><strong>Make your website match.</strong> Your site should have clear pages for your main services and your location, with your name, address and phone number consistent with your profile.</li>
</ul>
<p>Our <a href="/google-business-profile-local-seo/">guide to Google Business Profile and local SEO</a> walks through setting up each section.</p>

<h2>What can I do about distance?</h2>
<p>Very little, and that is worth accepting. If someone searches "dentist" while standing across town, a dentist next to them has an advantage. If they search "dentist in [your neighbourhood]," Google uses that location instead.</p>
<p>What you should not do is create fake addresses, virtual offices or mailbox addresses to appear in more places. Google's guidelines prohibit listing a location where you do not have a real, staffed presence that meets its eligibility rules, and profiles that break this can be removed. Service-area businesses, such as tradespeople who travel to customers, have a legitimate way to show the areas they cover; see our <a href="/local-seo-checklist-for-service-area-businesses/">local SEO checklist for service-area businesses</a>.</p>
<p>The honest approach to distance is to compete hardest where you actually are, and to use your website and other marketing to reach further.</p>

<h2>How do I build prominence?</h2>
<p>Prominence is the slowest factor to build and the hardest for a competitor to copy. It reflects how well known and well regarded your business is, online and off.</p>
<ul>
<li><strong>Reviews.</strong> Google explicitly mentions review count and rating. Ask every customer, make it easy, and reply to every review. Our guide on <a href="/how-to-get-more-google-reviews/">getting more Google reviews without breaking the rules</a> covers the method.</li>
<li><strong>Consistent listings.</strong> Accurate name, address and phone details across the web help Google connect information to your business. See <a href="/what-is-nap-consistency/">what NAP consistency is</a>.</li>
<li><strong>Links and mentions.</strong> Local press coverage, sponsorships, partnerships, trade associations and community organisations that mention or link to you.</li>
<li><strong>A strong website.</strong> Since Google says web ranking feeds into prominence, a useful, fast, well-structured site helps.</li>
<li><strong>Real-world reputation.</strong> Google describes prominence as reflecting how well known a business is offline too. Famous local landmarks and well-known brands tend to be more prominent. You cannot fake this, but you can earn it.</li>
</ul>

<h2>Do photos and posts help?</h2>
<p>Google encourages businesses to add photos and keep information up to date, and it says that adding photos helps customers. Whether posts or photos directly change rankings is not something Google states, and claims that they do are mostly speculation. They do, however, help the people looking at your profile decide to call you, which is the point of ranking in the first place. Add real photos of your premises, team and work, and keep them current.</p>

<h2>What gets businesses penalised?</h2>
<ul>
<li>Keyword-stuffed business names.</li>
<li>Fake or ineligible addresses.</li>
<li>Duplicate profiles for the same location.</li>
<li>Fake reviews, paid reviews or incentivised reviews.</li>
<li>Categories that do not match the real business.</li>
</ul>
<p>Some competitors get away with these tactics for a while, which is frustrating. Google provides a way to suggest edits to listings and report policy violations. Use those tools rather than copying the behaviour.</p>

<h2>How long does it take to rank in the map pack?</h2>
<p>There is no reliable timeline. Relevance improvements, such as fixing a wrong category, can show effects relatively quickly. Prominence builds over months and years. Competition matters too: a new café in a street full of established cafés faces a different challenge from the only electrician in a small town.</p>

<h2>What is a sensible plan?</h2>
<ol>
<li>Claim and verify your Business Profile.</li>
<li>Choose the most accurate primary category and complete every relevant field.</li>
<li>Make sure your name, address and phone match everywhere.</li>
<li>Set up a routine to ask every customer for a review.</li>
<li>Build website pages for your main services and location.</li>
<li>Earn local mentions through genuine community and industry involvement.</li>
<li>Review your profile monthly and keep it accurate.</li>
</ol>
<p>None of this is secret. The businesses that win the map pack over time are usually the ones that do these unglamorous things consistently, while competitors chase shortcuts.</p>
""",
faq=[
("What are Google's three local ranking factors?", "Google says local results are based mainly on relevance, distance and prominence."),
("Can I pay Google to rank higher in the map pack?", "No. Google says you cannot pay for a better organic local ranking. Local ads are separate and labelled as ads."),
("Does adding keywords to my business name help?", "It breaks Google's Business Profile guidelines and can lead to suspension. Use your real business name."),
("Can I use a virtual office to rank in another area?", "Google's guidelines do not allow ineligible addresses such as virtual offices without a real staffed presence. Profiles that break this can be removed."),
("Do reviews affect map pack rankings?", "Google says review count and score factor into local ranking as part of prominence."),
("How long does it take to rank?", "There is no fixed timeline. Fixing relevance issues can help quickly, while prominence builds over months and depends on your competition."),
],
drifted=False, housefly=False),

dict(slug="local-seo-checklist-for-service-area-businesses", kicker="Local SEO", hub="local-seo",
title="Local SEO checklist for service-area businesses",
dek="Plumbers, cleaners, electricians and mobile services play by slightly different local SEO rules. Here is the checklist.",
answer="A service-area business serves customers at their location rather than its own. Set up your Google Business Profile as a service-area business, hide your address if customers do not visit, and list the areas you really serve. Then keep your details consistent, build a page for each main service, earn reviews from every job, and avoid fake addresses.",
body="""
<p>A service-area business is one that goes to its customers rather than having customers come to it. Plumbers, electricians, cleaners, mobile mechanics, pest control, gardeners, dog walkers, mobile hairdressers and many consultants fall into this group. Some have a shop or office customers can visit as well; many work from home or a yard.</p>
<p>Google treats these businesses a little differently in its Business Profile guidelines, and the differences matter. Get them wrong and a profile can be suspended. Get them right and you can compete in local results across the area you actually serve. This checklist covers the essentials in order. Google updates its guidelines from time to time, so read the current version of its Business Profile guidelines before making changes.</p>

<h2>Is my business a service-area business?</h2>
<table>
<thead><tr><th>Situation</th><th>How Google treats it</th><th>Show your address?</th></tr></thead>
<tbody>
<tr><td>You visit customers and they never come to you</td><td>Service-area business</td><td>No; hide it and set service areas</td></tr>
<tr><td>You visit customers and also have premises they can visit during staffed hours</td><td>Hybrid business</td><td>Yes, and add service areas</td></tr>
<tr><td>Customers only come to your premises</td><td>Storefront business</td><td>Yes</td></tr>
<tr><td>You work entirely online with no in-person contact</td><td>Generally not eligible for a Business Profile</td><td>Not applicable</td></tr>
</tbody>
</table>
<p>If you work from home and customers do not visit, Google's guidelines say you should not show your home address on your profile.</p>

<h2>Checklist: Google Business Profile setup</h2>
<ul>
<li><strong>Claim and verify the profile.</strong> Google offers several verification methods; which ones you see depends on your business. Service-area businesses still need a real address for verification even though it will be hidden.</li>
<li><strong>Use your real business name.</strong> No added keywords or town names that are not part of your legal or trading name.</li>
<li><strong>Choose the most specific primary category</strong> for your main service, and a few accurate secondary categories.</li>
<li><strong>Hide your address</strong> if customers do not visit you.</li>
<li><strong>Set your service areas.</strong> Add the cities, towns or postcodes you genuinely serve. Google limits how many areas you can add and advises keeping the overall area to a reasonable distance from your base. Listing the whole country does not help and is not what the feature is for.</li>
<li><strong>Set accurate hours,</strong> including when you take calls if that differs from when you work on site.</li>
<li><strong>Add your services</strong> with plain descriptions in customers' words.</li>
<li><strong>Write a clear description</strong> of what you do and where. Keep it factual.</li>
<li><strong>Add real photos:</strong> your van, your team, your equipment and examples of finished work, with the customer's permission where their property is visible.</li>
</ul>
<p>Our <a href="/google-business-profile-local-seo/">guide to Google Business Profile and local SEO</a> goes deeper on each field.</p>

<h2>Checklist: what not to do</h2>
<ul>
<li>Do not use a virtual office, mailbox service or a friend's address to appear in another town. Google's guidelines treat these as ineligible, and they are a common reason for suspension.</li>
<li>Do not create multiple profiles for the same business to cover more areas.</li>
<li>Do not stuff town names into your business name.</li>
<li>Do not buy reviews or offer incentives for them.</li>
</ul>
<p>Competitors who do these things sometimes appear to get away with it. You can report policy violations through Google's tools. Copying them puts your own profile at risk.</p>

<h2>Checklist: consistent details across the web</h2>
<ul>
<li>Decide on one official version of your business name, phone number and website.</li>
<li>For a hidden address, keep the address consistent on listings where an address is required, or leave it off where the directory allows.</li>
<li>Update Apple Business Connect and Bing Places, not only Google.</li>
<li>Claim relevant directories and trade association listings.</li>
<li>Search for old phone numbers and old trading names, and fix listings that use them.</li>
</ul>
<p>Our explainer on <a href="/what-is-nap-consistency/">NAP consistency</a> covers how to audit and fix listings step by step.</p>

<h2>Checklist: your website</h2>
<p>For a service-area business, the website does much of the work of reaching beyond the map pack. Google has said that how well a business ranks in web results feeds into its local prominence.</p>
<ul>
<li><strong>A page for each main service.</strong> "Boiler repair," "bathroom installation" and "emergency call-outs" each deserve a clear page explaining what is included, how it works and how to book.</li>
<li><strong>A clear statement of the areas you serve,</strong> on a dedicated page or in the footer.</li>
<li><strong>Area pages only if they are genuinely useful.</strong> A page for a town you serve can work if it says something real: typical jobs there, travel times, local regulations or examples of work. Dozens of near-identical pages with only the town name swapped are thin content and can do more harm than good.</li>
<li><strong>Your phone number visible and tappable</strong> on mobile, at the top of every page.</li>
<li><strong>A simple contact or quote form</strong> that asks only what you need.</li>
<li><strong>Fast loading on phones,</strong> since many service searches happen on mobile, often urgently.</li>
<li><strong>LocalBusiness structured data,</strong> with service area information where appropriate. Test it with Google's Rich Results Test.</li>
</ul>
<p>The <a href="/landing-page-anatomy/">anatomy of a landing page</a> covers how to make each service page persuade as well as rank.</p>

<h2>Checklist: reviews from every job</h2>
<ul>
<li>Ask every customer when the job is finished and checked, ideally the same day.</li>
<li>Send a direct link to your review form by text or email.</li>
<li>Ask for an honest review, not a five-star one.</li>
<li>Do not filter who you ask based on whether they seemed happy.</li>
<li>Reply to every review. Mentioning the type of job naturally in replies can help readers, but do not force keywords.</li>
</ul>
<p>Our guide to <a href="/how-to-get-more-google-reviews/">getting more Google reviews without breaking the rules</a> has example wording.</p>

<h2>Checklist: earning local prominence</h2>
<ul>
<li>Join relevant trade associations and accreditation schemes that list members.</li>
<li>Support local events, sports clubs or charities where it fits your business.</li>
<li>Work with complementary businesses; a kitchen fitter and an electrician can genuinely refer each other.</li>
<li>Share useful local advice, such as preparing pipes for a cold snap, on your website and social channels.</li>
<li>Keep vans and uniforms branded with your real name; offline recognition is part of how well known you are.</li>
</ul>

<h2>Checklist: monthly maintenance</h2>
<ol>
<li>Check your Business Profile for suggested edits from Google or the public, and correct anything wrong.</li>
<li>Update holiday hours ahead of time.</li>
<li>Add a few new photos of recent work.</li>
<li>Reply to any new reviews.</li>
<li>Check the profile's performance figures for calls and website clicks.</li>
<li>Review your service areas; if you have stopped covering a town, remove it.</li>
</ol>
<p>Service-area businesses often feel at a disadvantage in local search because they cannot show a shopfront. In practice, the ones that follow the rules, keep details accurate and collect reviews from every job tend to do well over time. For how these pieces fit Google's own ranking factors, see <a href="/how-to-rank-in-the-google-map-pack/">how to rank in the Google map pack</a>.</p>
""",
faq=[
("Should I show my home address on Google?", "If customers do not visit you, Google's guidelines say to hide the address and set service areas instead."),
("How many service areas can I add?", "Google sets a limit and advises keeping the overall area within a reasonable distance of your base. Add only areas you genuinely serve."),
("Can I use a virtual office to appear in another town?", "No. Google treats virtual offices and mailbox addresses as ineligible, and they are a common reason for profile suspension."),
("Do I need a separate page for every town I serve?", "Only if each page says something genuinely useful. Many near-identical pages with the town name swapped are thin content."),
("Do service-area businesses still need to verify their profile?", "Yes. Google still verifies the business, using a real address that stays hidden from the public."),
],
drifted=False, housefly=False),
]
