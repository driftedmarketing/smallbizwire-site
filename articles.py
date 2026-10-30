"""SmallBizWire article content. Facts about Drifted and Housefly come only from their own published sites."""

D = '<a href="https://driftedmarketing.com">Drifted Marketing</a>'
H = '<a href="https://heyhousefly.com">Housefly</a>'

ARTICLES = [
dict(slug="how-small-businesses-should-use-ai-assistants", kicker="AI at work",
title="How small businesses should actually use AI assistants",
dek="Skip the novelty. The useful jobs are drafting, remembering and reminding, with a human saying yes before anything goes out.",
housefly=True,
body=f"""
<p>Most small businesses meet AI assistants the same way: someone asks a chatbot to write a caption, the result is fine but bland, and the tool gets filed under "interesting." That is a waste. The owners getting real value use assistants for a narrower, duller set of jobs, and they set firm rules about what the assistant may do on its own.</p>
<h2>Start with the jobs that eat your week</h2>
<p>The best first uses are the ones you already do by hand, repeatedly, and resent:</p>
<ul>
<li><strong>First drafts.</strong> Replies to common customer questions, follow-up emails after a call, a quote cover note, a product description. You edit; the blank page is gone.</li>
<li><strong>Summaries.</strong> A long email thread, a supplier contract, a meeting transcript, boiled down to what was promised and by whom.</li>
<li><strong>Memory.</strong> What you told a client last month, which supplier is late, which invoice is unpaid. An assistant that keeps this is worth more than one that writes beautifully.</li>
<li><strong>Prompts to act.</strong> A reminder that arrives before the deadline, not a dashboard you have to remember to open.</li>
</ul>
<h2>Keep a human on every send</h2>
<p>The rule that separates a helpful assistant from a liability is simple: <strong>it drafts, you send</strong>. Anything that emails a customer, spends money, changes a live account or publishes in your name should stop and ask first, and the question should state plainly what will happen. "Send the revised quote to this client from your email?" is a good question. "Proceed?" is not.</p>
<p>This matters because AI models are confident even when wrong. A wrong draft costs you thirty seconds of editing. A wrong email sent automatically costs you a client.</p>
<h2>Be careful what you feed it</h2>
<p>Before pasting customer data into any tool, check three things: whether your inputs are used to train the provider's models, how long conversations are stored, and whether other people in a shared workspace can see them. Business tiers of the major assistants generally offer stronger data terms than free consumer plans. Read them; they differ.</p>
<p>Never paste passwords, card numbers or government ID numbers into a chat window. No legitimate workflow needs them there.</p>
<h2>Choose the shape that fits how you work</h2>
<p>General chat assistants such as ChatGPT, Claude, Gemini and Microsoft Copilot are flexible and inexpensive, and they suit owners who will sit down and use them deliberately. Some newer products take a different shape: an assistant you text, which keeps a running memory of your business and speaks up when something needs you. {H}, made by SmallBizWire's publisher, is one example. We compare the options in <a href="/best-ai-assistants-for-small-business/">our guide to AI assistants for small business</a>.</p>
<h2>A one-week trial plan</h2>
<ol>
<li>Pick three recurring tasks from the list above.</li>
<li>Use an assistant for each, every time it comes up, for five working days.</li>
<li>Note how long each took before and after, and how much editing the drafts needed.</li>
<li>Keep what saved time. Drop what did not.</li>
</ol>
<p>That small test tells you more than any demo.</p>
""",
faq=[("Should an AI assistant send emails for my business automatically?", "Generally no. Let it draft, and keep a person approving anything that goes to a customer, spends money or changes an account."),
     ("Is it safe to put customer information into an AI chatbot?", "It depends on the provider's data terms. Check whether inputs are used for training, how long they are retained and who can see them, and never paste passwords or payment details."),
     ("What is the best first task to give an AI assistant?", "A repetitive writing job you already do weekly, such as follow-up emails or answers to common customer questions.")]),

dict(slug="spf-dkim-dmarc-explained", kicker="Email deliverability",
title="SPF, DKIM and DMARC, explained for people who just want their email delivered",
dek="Three DNS records decide whether Gmail and Outlook trust mail from your domain. Here is what each one does and how to set them up.",
body="""
<p>If your invoices land in spam or your cold emails vanish, the cause is often not your wording. It is that the receiving mail server cannot verify the message really came from you. Three records in your domain's DNS settings solve that: SPF, DKIM and DMARC.</p>
<h2>SPF: who is allowed to send</h2>
<p>A Sender Policy Framework record is a single line of text (a TXT record) listing the services permitted to send mail for your domain, such as Google Workspace, Microsoft 365 or your newsletter tool. A typical record looks like <code>v=spf1 include:_spf.google.com ~all</code>.</p>
<ul>
<li>You may have only <strong>one</strong> SPF record per domain. If you add a new sending tool, edit the existing record rather than creating a second one.</li>
<li>SPF allows at most ten DNS lookups. Stacking many <code>include:</code> entries can silently break it.</li>
</ul>
<h2>DKIM: a signature on every message</h2>
<p>DomainKeys Identified Mail adds a cryptographic signature to each email. Your mail provider generates a key pair; you publish the public half in DNS (usually as a TXT or CNAME record under a name like <code>google._domainkey</code>), and the provider signs outgoing mail with the private half. Receivers check that the signature matches, which proves the message was not altered and was authorised by your domain.</p>
<p>Each sending service needs its own DKIM setup. Turning it on in Google Workspace does not cover your email marketing platform.</p>
<h2>DMARC: the policy that ties them together</h2>
<p>DMARC tells receivers what to do when a message fails SPF and DKIM alignment, and where to send reports. Start gently:</p>
<p><code>v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com</code></p>
<p>With <code>p=none</code>, nothing is blocked; you simply receive reports showing who is sending as your domain. Once the reports show only your legitimate services, move to <code>p=quarantine</code> and eventually <code>p=reject</code>, which also protects you from people spoofing your domain.</p>
<h2>Why this is no longer optional</h2>
<p>In 2024 Google and Yahoo began enforcing requirements for bulk senders (Google defines these as those sending around 5,000 or more messages a day to personal Gmail accounts): authenticate with SPF and DKIM, publish a DMARC record, offer one-click unsubscribe on marketing mail, and keep reported spam rates low. Smaller senders are expected to authenticate too. Without these records, even modest volumes get filtered.</p>
<h2>How to check your setup</h2>
<ol>
<li>Send a message to a Gmail address, open it, and choose "Show original." Look for SPF, DKIM and DMARC each marked PASS.</li>
<li>Use a free checker such as MXToolbox or Google's Admin Toolbox to inspect the records.</li>
<li>Read your first DMARC reports after a week. Unknown senders are either a tool you forgot or someone impersonating you.</li>
</ol>
<p>Authentication is step one. For outbound sales email, read <a href="/cold-email-warm-up-guide/">our warm-up guide</a> and the <a href="/cold-email-deliverability-checklist/">deliverability checklist</a> next.</p>
""",
faq=[("Do I need SPF, DKIM and DMARC for a small business?", "Yes. Major mailbox providers expect all senders to authenticate, and bulk senders to Gmail and Yahoo are required to."),
     ("Can I have two SPF records?", "No. A domain should have exactly one SPF record. Combine all sending services into it."),
     ("What DMARC policy should I start with?", "Start with p=none to collect reports, then move to quarantine and reject once only legitimate senders appear.")]),

dict(slug="cold-email-warm-up-guide", kicker="Email deliverability",
title="Cold email warm-up: how to build sender reputation without burning your domain",
dek="A new mailbox that sends hundreds of emails on day one looks like spam. Warm-up is the slow, boring fix.",
body="""
<p>Mailbox providers judge senders on history. A brand-new address with no track record that suddenly sends a large batch of messages to strangers matches the pattern of a spammer, and gets treated like one. Warm-up means building that history gradually.</p>
<h2>Protect your main domain first</h2>
<p>Many businesses run cold outreach from a <strong>separate, similar domain</strong> (for example, a "get" or "hello" variant of the brand name) rather than the domain used for invoices and customer support. If outreach damages that domain's reputation, your everyday mail keeps flowing. The secondary domain should still be honest about who you are, carry its own SPF, DKIM and DMARC records, and ideally redirect visitors to your main website.</p>
<h2>A sensible ramp</h2>
<p>There is no official schedule, but practitioners broadly agree on the shape:</p>
<ul>
<li><strong>Weeks one and two:</strong> send only genuine, low-volume mail. A handful a day to people likely to reply: colleagues, partners, existing contacts.</li>
<li><strong>Weeks three and four:</strong> begin small cold batches, increasing gradually, and watch bounces and replies closely.</li>
<li><strong>After that:</strong> hold a steady daily volume per mailbox rather than spiking. If you need more volume, add mailboxes rather than pushing one harder.</li>
</ul>
<p>Automated warm-up services, which exchange messages between networks of inboxes, are common. They can help, but they are no substitute for real replies from real people, which are the strongest positive signal you can earn.</p>
<h2>What hurts reputation fastest</h2>
<ul>
<li><strong>Bounces.</strong> Verify every list before sending. Purchased or scraped lists are full of dead and trap addresses.</li>
<li><strong>Spam complaints.</strong> Google advises keeping reported spam rates below 0.1% and never letting them reach 0.3%.</li>
<li><strong>Identical messages.</strong> Hundreds of word-for-word copies look automated. Write for a specific segment and reference something real about the recipient.</li>
<li><strong>Heavy links and images.</strong> A first-touch email works best as plain text with one link at most.</li>
</ul>
<h2>Measure the right thing</h2>
<p>Open rates are increasingly unreliable because of privacy features that pre-load images. Track replies, positive replies and bounces instead. Check Google Postmaster Tools, which is free, for your domain's reputation once volume is high enough to register.</p>
<h2>Stay on the right side of the law</h2>
<p>Rules differ by country. In the United States, CAN-SPAM requires accurate sender details, a physical postal address and a working opt-out. In the UK and EU, rules on unsolicited email are stricter, particularly for individuals rather than companies. If you sell across borders, check the rules where your recipients are.</p>
<p>Before you start, make sure your <a href="/spf-dkim-dmarc-explained/">authentication records</a> are in place, then work through the <a href="/cold-email-deliverability-checklist/">full checklist</a>.</p>
""",
faq=[("How long does email warm-up take?", "Most practitioners allow three to four weeks of gradually increasing volume before sending at full pace, and keep volume steady afterwards."),
     ("Should I send cold email from my main domain?", "Many businesses use a separate, clearly related domain for outreach so their everyday mail is protected if reputation suffers."),
     ("Do warm-up tools work?", "They can help build history, but genuine replies from real recipients are a stronger signal and cannot be replaced.")]),

dict(slug="cold-email-deliverability-checklist", kicker="Email deliverability",
title="The cold-email deliverability checklist",
dek="Twenty checks to run before your next outbound campaign, from DNS records to the wording of your first line.",
body="""
<p>Use this as a pre-flight list. Every item is something that commonly causes good emails to land in spam or bounce.</p>
<h2>Domain and DNS</h2>
<ol>
<li>One valid SPF record covering every service that sends for the domain.</li>
<li>DKIM enabled for each sending service, and passing.</li>
<li>A DMARC record published, at minimum <code>p=none</code> with a reporting address.</li>
<li>The "From" domain aligns with the domain that signs DKIM.</li>
<li>The outreach domain has a working website or redirect, so it does not look abandoned.</li>
<li>Custom tracking domain configured, if your tool tracks clicks, rather than a shared one.</li>
</ol>
<h2>Mailboxes</h2>
<ol start="7">
<li>Each mailbox has been warmed for several weeks (see <a href="/cold-email-warm-up-guide/">warm-up guide</a>).</li>
<li>A real name, photo and signature on each sender.</li>
<li>Daily volume per mailbox held steady, not spiking.</li>
<li>Replies are monitored by a person every working day.</li>
</ol>
<h2>List</h2>
<ol start="11">
<li>Every address verified with a verification service before sending.</li>
<li>No purchased or scraped "bulk" lists.</li>
<li>Role addresses (info@, sales@) used sparingly; they bounce and complain more.</li>
<li>A suppression list of past unsubscribes and bounces applied to every campaign.</li>
</ol>
<h2>Message</h2>
<ol start="15">
<li>Plain text, short, with at most one link and no attachments on first touch.</li>
<li>The first line is about the recipient, and true.</li>
<li>No spam-trigger theatrics: all-caps subject lines, excess punctuation, fake "Re:" prefixes.</li>
<li>A clear, easy way to opt out, and it is honoured promptly.</li>
<li>Your business name and postal address included where the law requires them.</li>
</ol>
<h2>Measurement</h2>
<ol start="20">
<li>Track bounces, reply rate and positive reply rate per campaign; pause anything with rising bounces or complaints, and check Google Postmaster Tools.</li>
</ol>
<h2>The point of all this</h2>
<p>Deliverability is not a trick. Mailbox providers are trying to deliver mail people want. Every item above is either proving who you are or showing that recipients welcome your messages. If you are short on time, prioritise <a href="/spf-dkim-dmarc-explained/">authentication</a>, list verification and relevance, in that order.</p>
"""),

dict(slug="shopify-seo-guide", kicker="Ecommerce SEO",
title="Shopify SEO for small stores: what actually moves rankings",
dek="Shopify handles the technical basics. What it cannot do for you is decide what each page is about.",
body="""
<p>Shopify gives every store a solid technical base: a sitemap at <code>/sitemap.xml</code>, a sensible robots.txt, canonical tags, SSL and fast hosting. That is why most small-store SEO problems are not technical. They are about content, structure and the details that only the owner can fill in.</p>
<h2>1. Write titles and descriptions for every page that matters</h2>
<p>Each product, collection and blog post has a "Search engine listing" section in the admin. By default Shopify fills it from your product title and description, which is often too long, too vague, or identical across similar products. Write a title of roughly 50–60 characters that names the product the way a buyer would search for it, and a description of about 150 characters that gives a reason to click.</p>
<h2>2. Treat collection pages as your main landing pages</h2>
<p>People search for categories ("linen bath towels", "vintage brass lamps") more often than for one exact product. Collection pages are where those searches should land. Give each one a short, useful introduction above or below the grid: what is in it, who it is for, how to choose. Two or three helpful paragraphs beat a wall of keywords.</p>
<h2>3. Fix the image basics</h2>
<ul>
<li>Add alt text to every product image describing what is shown. It helps image search and screen-reader users.</li>
<li>Compress images before upload. Large images are the most common cause of slow Shopify pages.</li>
<li>Name files descriptively before uploading, rather than <code>IMG_4417.jpg</code>.</li>
</ul>
<h2>4. Watch your apps and theme</h2>
<p>Every app can add scripts to every page. Remove apps you no longer use, and check that uninstalled apps have not left code in your theme. Test key pages with Google PageSpeed Insights after any change.</p>
<h2>5. Handle duplicates and dead ends</h2>
<p>Shopify can reach the same product through several URLs (for example, via a collection path). Its canonical tags handle this, but internal links should point at the clean <code>/products/</code> URL where your theme allows. When you delete a product, create a URL redirect (Online Store → Navigation → URL Redirects) to the closest alternative instead of leaving a 404.</p>
<h2>6. Add structured data</h2>
<p>Most modern themes include basic Product schema. Check with Google's Rich Results Test that price, availability and reviews (only real ones) appear correctly. Accurate structured data helps search engines and AI assistants understand your catalogue.</p>
<h2>7. Publish content that answers buyer questions</h2>
<p>A blog is useful when it answers what buyers actually ask: sizing, care, comparisons, gift guides. Link each post to the relevant collection. For individual listings, see <a href="/shopify-product-page-seo/">our product page guide</a>.</p>
<p>Finally, connect Google Search Console, submit your sitemap, and look at the queries you already appear for. The fastest gains usually come from pages ranking on page two that need a better title or a clearer introduction.</p>
""",
faq=[("Is Shopify good for SEO?", "Yes. It handles sitemaps, canonical tags, SSL and hosting. Most improvement comes from better titles, descriptions, collection content and image optimisation."),
     ("Where do I edit SEO titles in Shopify?", "On each product, collection or page, scroll to the Search engine listing section and choose Edit."),
     ("What should I do when I delete a Shopify product?", "Add a URL redirect to the closest alternative so visitors and search engines are not sent to a 404 page.")]),

dict(slug="shopify-product-page-seo", kicker="Ecommerce SEO",
title="How to write a Shopify product page that ranks and sells",
dek="A product page has two readers: a search engine deciding what it is about, and a buyer deciding whether to trust you.",
body="""
<p>The same page has to satisfy two audiences. Fortunately, what helps one usually helps the other: clarity, specifics and honest detail.</p>
<h2>The title</h2>
<p>Lead with what the item is, then the distinguishing detail: material, size, colour or model. "Hand-embroidered cotton cushion cover, 18 inch, sage" tells both a shopper and a search engine exactly what is on offer. Keep brand names and clever product nicknames secondary.</p>
<h2>The description</h2>
<ul>
<li><strong>Open with the benefit</strong> in one or two sentences: what problem it solves or what it is for.</li>
<li><strong>Follow with specifics</strong> in a scannable list: dimensions, materials, care, what is in the box.</li>
<li><strong>Answer objections</strong>: delivery times, returns, sizing advice.</li>
<li><strong>Write it yourself.</strong> Manufacturer copy is duplicated across dozens of sites and gives search engines no reason to prefer yours.</li>
</ul>
<h2>Photographs</h2>
<p>Show scale, texture and the product in use. Add descriptive alt text to each image. Compress files so the page loads quickly on a phone, which is where most shoppers will see it.</p>
<h2>Variants</h2>
<p>Where colours or sizes are variants of one product, keep them on one page rather than creating near-identical listings that compete with each other.</p>
<h2>Reviews</h2>
<p>Genuine reviews help shoppers and can appear in search results through structured data. Never write or buy reviews; it breaches platform and search policies and, in many countries, consumer law. Ask real customers after delivery instead.</p>
<h2>The search listing</h2>
<p>Edit the SEO title and meta description in Shopify's "Search engine listing" panel. Use the description to state the reason to click: free delivery threshold, handmade, ships in two days, whatever is true and distinctive.</p>
<h2>Internal links</h2>
<p>Link from the product to its collection and to one or two related items. Link to the product from relevant blog posts and guides. Pages that nothing links to are harder for search engines to find and judge.</p>
<p>For the store-wide picture, read <a href="/shopify-seo-guide/">Shopify SEO for small stores</a>.</p>
"""),

dict(slug="landing-page-anatomy", kicker="Conversion",
title="The anatomy of a landing page that converts",
dek="One page, one audience, one action. Most underperforming landing pages break at least one of the three.",
body="""
<p>A landing page exists to turn a specific visitor into a specific action: a booked call, a signup, a purchase. It is not a homepage. Everything on it should either explain the offer or remove a reason to hesitate.</p>
<h2>Match the promise that brought them</h2>
<p>If an ad promises "same-week kitchen quotes in Leeds", the page headline should say the same thing. When the page does not match the click, visitors leave. Build separate pages for meaningfully different audiences or offers.</p>
<h2>The first screen</h2>
<ul>
<li><strong>Headline:</strong> what you offer and who it is for, in plain words.</li>
<li><strong>Subhead:</strong> the main outcome or the main difference from alternatives.</li>
<li><strong>One primary button</strong> with a specific label ("Book a 30-minute call", not "Submit").</li>
<li><strong>A real image</strong> of the product, the team or the result. Stock photos of handshakes add nothing.</li>
</ul>
<h2>Below the fold</h2>
<ol>
<li><strong>How it works</strong> in three short steps.</li>
<li><strong>Proof:</strong> real testimonials with names and permission, real numbers with sources, logos only of clients who agreed. If you have no proof yet, say what you guarantee instead. Never invent it.</li>
<li><strong>Price or what determines it.</strong> Hiding price entirely tends to filter out good leads along with bad ones.</li>
<li><strong>Objections answered</strong>, often as an FAQ.</li>
<li><strong>The button again.</strong></li>
</ol>
<h2>Remove friction</h2>
<ul>
<li>Ask only for the form fields you will use. Every extra field costs completions.</li>
<li>Remove the main site navigation, or keep it minimal, so there is one obvious path.</li>
<li>Test on a phone. Most paid social traffic arrives on mobile.</li>
<li>Check load speed. A slow page wastes the ad spend that bought the click.</li>
</ul>
<h2>Test one thing at a time</h2>
<p>Headline and offer changes usually matter far more than button colours. Run tests long enough to reach meaningful numbers; a few dozen visitors is not enough to call a winner.</p>
<p>If you are hiring help to build or run these pages, our <a href="/how-to-choose-a-marketing-agency/">agency selection guide</a> covers what to ask.</p>
""",
faq=[("What is the difference between a landing page and a homepage?", "A homepage serves many visitors and paths. A landing page serves one audience and asks for one action."),
     ("How many form fields should a landing page have?", "Only the ones you will actually use to follow up. Fewer fields generally mean more completions.")]),

dict(slug="how-to-choose-a-marketing-agency", kicker="Hiring help",
title="How to choose a marketing agency when you are a small business",
dek="Ten questions that separate agencies who will move your numbers from those who will send you reports.",
drifted=True,
body=f"""
<p>Hiring an agency is one of the larger cheques a small business writes, and it is hard to judge before you sign. The questions below are designed to expose how an agency actually works.</p>
<h2>Before you talk to anyone</h2>
<p>Write down the one number you want to move (leads, sales, booked calls) and the date you need it by. An agency that cannot engage with that number is selling activity, not outcomes.</p>
<h2>Ten questions to ask</h2>
<ol>
<li><strong>What exactly will you measure, and against what target?</strong> Good answers name a metric and a date.</li>
<li><strong>Who will do the work?</strong> Ask to meet them. In some agencies the people on the sales call are not the people running your account.</li>
<li><strong>Whose ad accounts are they?</strong> Insist the ad accounts, pixels, analytics and domains are in your name. Leaving should not mean losing your data.</li>
<li><strong>Can I see work for a business like mine</strong>, with permission to contact that client?</li>
<li><strong>How do you report?</strong> Monthly reports should show the target, the result and what changes next.</li>
<li><strong>What is the minimum term</strong>, and what is the notice period?</li>
<li><strong>What is included in the fee</strong>, and what costs extra: creative, ad spend, software, revisions?</li>
<li><strong>What will you need from me</strong> each week? Agencies stall waiting for approvals and assets.</li>
<li><strong>What would make you recommend we stop?</strong> Honest agencies have an answer.</li>
<li><strong>What happens in the first 30 days?</strong></li>
</ol>
<h2>Warning signs</h2>
<ul>
<li>Guaranteed rankings or guaranteed returns.</li>
<li>Reluctance to put accounts in your name.</li>
<li>Case studies with no client named and no way to verify.</li>
<li>Long lock-in contracts before any results.</li>
</ul>
<h2>Specialist or full-service?</h2>
<p>A specialist (only paid search, only SEO) is often stronger in its lane. A small full-service team can be better when your ads, content and website need to work together and you would rather have one point of contact. Our list of <a href="/best-marketing-agencies-for-small-business/">agencies for small business</a> includes both kinds. One of them is {D}, SmallBizWire's publisher, which says on its site that it writes one metric and one date into its contracts and keeps ad spend in the client's own account. Those are exactly the kinds of commitments to ask any agency for.</p>
""",
faq=[("What should I ask a marketing agency before hiring?", "Ask what they will measure and by when, who will do the work, who owns the ad accounts, what the fee includes, and what the notice period is."),
     ("Should my ad accounts be in my name or the agency's?", "Yours. Owning the accounts, pixels and analytics means you keep your data if you change agencies.")]),

dict(slug="best-marketing-agencies-for-small-business", kicker="Buyer's guide",
title="Marketing agencies for small business: six worth a look",
dek="A short, honest list across different specialisms and price points, with notes on who each suits.",
drifted=True,
body=f"""
<p>There is no single best agency. The right choice depends on what you need most: paid ads, search, content or a team that does several. Below are six agencies of different kinds. We have not ranked them on results, because we cannot independently verify any agency's client results, including our publisher's. Use the <a href="/how-to-choose-a-marketing-agency/">ten questions</a> with whichever you contact.</p>
<p><em>How this list was made:</em> agencies were chosen to cover a range of specialisms and to be well established or clearly described in public. Descriptions are based on what each agency publishes about itself. Nobody paid to be included.</p>
<h2>Drifted Marketing</h2>
<p class="disclosure-inline"><strong>Disclosure:</strong> Drifted Marketing publishes SmallBizWire.</p>
<p>{D} describes itself as a growth studio for ads, content and AI apps, based in Karachi and working on New York hours. Its site says the same people plan, shoot, cut and run the work, with no account-management layer in between, that one metric and one date are written into the contract, and that ad spend stays in the client's own account. <strong>Suits:</strong> small businesses that want ads, short-form content and custom software from one team. <a href="/drifted-marketing-profile/">Read our profile.</a></p>
<h2>WebFX</h2>
<p>A large US digital agency offering SEO, paid media, web design and its own marketing software platform. <strong>Suits:</strong> businesses that want a broad menu of services and established processes.</p>
<h2>Disruptive Advertising</h2>
<p>A US agency focused on paid media, including Google and Meta advertising, with conversion-rate work alongside. <strong>Suits:</strong> businesses where paid ads are the main growth channel.</p>
<h2>Single Grain</h2>
<p>A US agency known for content marketing, SEO and paid acquisition, and for its founder's marketing podcast. <strong>Suits:</strong> companies investing in content and search over the long term.</p>
<h2>Ignite Visibility</h2>
<p>A San Diego agency offering SEO, paid media, social and email. <strong>Suits:</strong> businesses wanting a multi-channel US-based team.</p>
<h2>A freelancer or small local studio</h2>
<p>Often overlooked: for a business with a modest budget, a skilled independent specialist found through referrals, Upwork or Clutch can be the best value. <strong>Suits:</strong> a single, well-defined job such as a Shopify rebuild or setting up Google Ads.</p>
<h2>How to decide</h2>
<p>Shortlist two or three, ask each the same questions, and compare the answers on who does the work, who owns the accounts and what they will be measured on. Price matters less than clarity on those three.</p>
""",
faq=[("What is the best marketing agency for a small business?", "It depends on the main channel you need. Shortlist agencies that specialise in it, and compare who does the work, who owns the accounts and what they commit to measuring."),
     ("Is Drifted Marketing independent of SmallBizWire?", "No. Drifted Marketing publishes SmallBizWire, which is disclosed wherever it is featured.")]),

dict(slug="best-ai-assistants-for-small-business", kicker="Buyer's guide",
title="AI assistants for small business: the main options compared",
dek="General chat tools, office-suite assistants and a newer kind you text. What each is good at, and who it suits.",
housefly=True,
body=f"""
<p>AI assistants now come in several shapes. The right one depends less on which model is "smartest" and more on where you already work and how much you want the assistant to remember. Prices and features change often; check each provider's site before buying.</p>
<p><em>How this list was made:</em> we included the most widely used general assistants plus one product made by our publisher, described from public information. Nobody paid to be included.</p>
<h2>ChatGPT (OpenAI)</h2>
<p>The best-known general assistant, with free and paid tiers including team and business plans. Strong at drafting, brainstorming and analysing files, with a large ecosystem of custom GPTs. <strong>Suits:</strong> owners who want one flexible tool for many jobs.</p>
<h2>Claude (Anthropic)</h2>
<p>A general assistant known for long-document work and careful writing, with team and enterprise plans and project workspaces for shared context. <strong>Suits:</strong> businesses that work through contracts, reports and long email threads.</p>
<h2>Google Gemini</h2>
<p>Built into Google Workspace for business plans, working inside Gmail, Docs and Sheets. <strong>Suits:</strong> teams already running on Google Workspace.</p>
<h2>Microsoft Copilot</h2>
<p>Integrated with Microsoft 365, including Outlook, Word, Excel and Teams. <strong>Suits:</strong> businesses on Microsoft 365 that want help inside the apps they already use.</p>
<h2>Housefly Concierge</h2>
<p class="disclosure-inline"><strong>Disclosure:</strong> Housefly is made by Drifted Marketing, which publishes SmallBizWire.</p>
<p>{H} takes a different shape: rather than an app you open, it is an assistant you text, iMessage first. It keeps track of what you promised clients and what they owe you, prepares a brief before calls, and speaks up when something needs you. Anything that sends, pays or changes an account is stated in one sentence and waits for your yes. Each member's memory is sealed so no other member sees it, and it carries no ads. It is offered as ten founding seats, priced on its site at $3,000 or $6,000 a quarter. <strong>Suits:</strong> founders who want a proactive assistant with private memory and are willing to pay a premium for it. <a href="/housefly-profile/">Read our profile.</a></p>
<h2>How to choose</h2>
<ul>
<li><strong>Already on Google or Microsoft?</strong> Start with the assistant built into your suite.</li>
<li><strong>Need a flexible all-rounder?</strong> Try ChatGPT or Claude for a week on real tasks.</li>
<li><strong>Want something that remembers and reminds, without you opening an app?</strong> Look at texted, memory-first assistants such as Housefly.</li>
</ul>
<p>Whatever you pick, apply the rules in <a href="/how-small-businesses-should-use-ai-assistants/">our guide to using assistants well</a>: it drafts, you approve.</p>
""",
faq=[("Which AI assistant is best for a small business?", "Start with the one built into the office suite you use. For flexibility try ChatGPT or Claude; for a proactive texted assistant with private memory, consider products like Housefly."),
     ("How much does Housefly cost?", "Its site lists founding seats at $3,000 or $6,000 a quarter, with ten founding seats.")]),

dict(slug="drifted-marketing-profile", kicker="Profile",
title="Profile: Drifted Marketing, a growth studio for ads, content and AI apps",
dek="What the agency says it does, how it says it works, and the questions a prospective client should ask.",
drifted=True,
body=f"""
<p>{D} is a marketing agency based in Karachi that works on New York hours. It describes itself as a growth studio covering three disciplines: ads, content and AI apps. It is also the publisher of SmallBizWire, which is why this profile is written from the agency's own published claims rather than from independent testing.</p>
<h2>What it offers</h2>
<ul>
<li><strong>Ads:</strong> Meta and Google advertising, plus the creative that feeds it. The agency states that spend stays in the client's own ad account.</li>
<li><strong>Content:</strong> short-form video, carousels and posts aimed at reaching people beyond existing followers.</li>
<li><strong>AI apps:</strong> custom software for clients, with the revenue model decided before design begins, according to its site.</li>
</ul>
<h2>How it says it works</h2>
<p>Three commitments stand out on the agency's site, and they map closely onto the questions in our <a href="/how-to-choose-a-marketing-agency/">agency selection guide</a>:</p>
<ul>
<li><strong>A number and a date in the contract.</strong> The agency says it writes one metric and one target date into each contract and reports against it.</li>
<li><strong>No account layer.</strong> The same people plan, shoot, edit and run the work.</li>
<li><strong>Client-owned accounts.</strong> Ad spend stays in the client's own account.</li>
</ul>
<p>Its site also publishes client results with each client named beside the figure. We do not repeat them here, as SmallBizWire cannot independently verify them; readers can review them at the source and ask the agency for references.</p>
<h2>Its own products</h2>
<p>Drifted Marketing also makes {H}, a texted AI assistant, covered in <a href="/housefly-profile/">a separate profile</a>, and runs <a href="https://hellodrifted.com">hellodrifted.com</a>.</p>
<h2>Who it may suit</h2>
<p>Small and growing businesses that want ads, content and custom software from one small team, and that value working directly with the people doing the work. Businesses that need a large, local, in-person team may prefer an agency in their own city.</p>
<h2>Questions to ask before hiring</h2>
<ol>
<li>Which metric and date would you write into our contract?</li>
<li>Who exactly will work on our account, and when are they available in our timezone?</li>
<li>Can we speak with a current client in a similar business?</li>
</ol>
<p>A 30-minute call can be booked through <a href="https://driftedmarketing.com">driftedmarketing.com</a>.</p>
"""),

dict(slug="housefly-profile", kicker="Profile",
title="Profile: Housefly, a private AI assistant you text",
dek="A memory-first assistant from Drifted Marketing, offered as ten founding seats. What it does and what it will not do.",
housefly=True,
body=f"""
<p>{H} is an AI assistant made by Drifted Marketing, SmallBizWire's publisher. Its paid offering, Housefly Concierge, is being opened to ten founding members. This profile is based on Housefly's published site.</p>
<h2>The idea</h2>
<p>Most assistants wait to be opened. Housefly is designed to be texted like a person, iMessage first, and to learn the member's memory and taste from those conversations. It also speaks first: when something needs attention before a call or a deadline, it sends a message rather than waiting to be asked.</p>
<h2>What it keeps track of</h2>
<ul>
<li>What the member has promised clients.</li>
<li>What clients still owe the member.</li>
<li>A brief before each call.</li>
<li>The member's inbox, store and ad numbers, read.</li>
</ul>
<h2>What it will not do on its own</h2>
<p>Anything that sends, pays or changes an account is named in a single sentence, and then Housefly waits for the member's yes. This "drafts, you approve" pattern is the same one we recommend for every assistant in <a href="/how-small-businesses-should-use-ai-assistants/">our guide</a>.</p>
<h2>Sealed memory</h2>
<p>Each member's memory is kept separately. According to its site, no other member and no shared brain sees inside it. The service carries no ads, and the site states that member data is not for sale; the business model is the member's subscription.</p>
<h2>When it hits a wall</h2>
<p>For jobs an assistant cannot finish, such as design, video and outreach, Drifted Marketing's own team picks them up.</p>
<h2>Price and availability</h2>
<p>The site lists two tiers, Solo at $3,000 a quarter and Operator at $6,000 a quarter, paid up front each quarter, with founding members keeping their price for life in exchange for a short weekly feedback call. There are ten founding seats. The site notes that the difference between the two tiers is still to be defined, and that there are not yet member testimonials to share.</p>
<h2>Who it may suit</h2>
<p>Founders and operators juggling many clients who want an assistant that remembers and reminds, and who place a high value on privacy. Owners who want a low-cost general tool will find the mainstream assistants in <a href="/best-ai-assistants-for-small-business/">our comparison</a> a better fit.</p>
<p>A call can be booked through <a href="https://heyhousefly.com">heyhousefly.com</a>.</p>
""",
faq=[("What is Housefly?", "A texted AI assistant made by Drifted Marketing that keeps a private memory of a member's business and asks before anything is sent, paid or changed."),
     ("Is Housefly memory shared between members?", "According to its site, each member's memory is sealed and no other member or shared brain sees it.")]),

dict(slug="google-business-profile-local-seo", kicker="Local search",
title="Google Business Profile: the local SEO job most small businesses leave half-done",
dek="For anyone serving a local area, this free listing often matters more than the website.",
body="""
<p>When someone searches "plumber near me" or "cafe open now", the map results usually appear before any website. Those results come from Google Business Profile. It is free, and most profiles are incomplete.</p>
<h2>Get the basics exactly right</h2>
<ul>
<li><strong>Name:</strong> your real business name. Adding keywords to the name breaches Google's guidelines and can get a listing suspended.</li>
<li><strong>Category:</strong> the primary category matters a great deal. Choose the most specific accurate one, then add secondary categories.</li>
<li><strong>Address or service area:</strong> show an address only if customers visit you there.</li>
<li><strong>Hours,</strong> including holiday hours. Wrong hours generate bad reviews quickly.</li>
<li><strong>Phone and website</strong>, matching what is on your site.</li>
</ul>
<h2>Fill in what competitors skip</h2>
<ul>
<li>Services or products with short descriptions and prices where sensible.</li>
<li>Real photos: the outside (so people can find you), the inside, the team, the work.</li>
<li>Attributes such as accessibility and payment options.</li>
<li>The business description, written for people rather than keywords.</li>
</ul>
<h2>Reviews</h2>
<p>Ask every satisfied customer, with a direct link to your review form. Reply to every review, good or bad, briefly and professionally. Do not offer incentives for reviews and never post fake ones; both break Google's policies, and fake reviews are increasingly targeted by consumer-protection regulators.</p>
<h2>Keep it alive</h2>
<p>Post updates, offers or events occasionally, answer the Questions section, and update photos seasonally. An active profile signals a business that is open and cared for.</p>
<h2>Connect it to your website</h2>
<p>Make sure your name, address and phone number appear identically on your website, and add LocalBusiness structured data. Consistency across the web helps Google trust the details. For broader visibility, including in AI assistants' answers, see <a href="/ai-search-visibility-for-small-business/">our guide to AI search</a>.</p>
""",
faq=[("Is Google Business Profile free?", "Yes. Creating and managing a profile costs nothing."),
     ("Can I add keywords to my business name on Google?", "No. Google's guidelines require your real business name, and keyword stuffing can lead to suspension.")]),

dict(slug="ai-search-visibility-for-small-business", kicker="AI search",
title="Getting your business mentioned in AI answers: a practical guide",
dek="ChatGPT, Perplexity and Google's AI Overviews now answer many questions directly. Here is how to be part of the answer.",
body="""
<p>A growing share of searches end without a click, because an AI-generated answer appears first. Sometimes called generative engine optimisation (GEO) or answer engine optimisation (AEO), the work of appearing in those answers overlaps heavily with good SEO, with a few differences.</p>
<h2>Let the crawlers in</h2>
<p>AI services use their own crawlers, such as OpenAI's GPTBot and OAI-SearchBot, Anthropic's ClaudeBot, and PerplexityBot. Check your robots.txt does not block them if you want to be cited. Some website builders and security services block them by default.</p>
<h2>Answer the question directly</h2>
<p>AI systems favour passages that answer a question clearly and can be quoted on their own. Put a one- or two-sentence direct answer near the top of the relevant page, then expand. Use the question as a heading where it reads naturally.</p>
<h2>Be specific and factual</h2>
<ul>
<li>State what you do, where, for whom and at what price range in plain sentences.</li>
<li>Use real numbers only when you can source them.</li>
<li>Keep facts consistent across your website, Google Business Profile and directory listings.</li>
</ul>
<h2>Use structured data</h2>
<p>Organization, LocalBusiness, Product, Article and FAQPage schema help machines understand who you are and what a page says. Validate it with Google's Rich Results Test.</p>
<h2>Consider an llms.txt file</h2>
<p>llms.txt is a proposed convention: a plain Markdown file at your site root that summarises the site and links to its key pages for language models. Adoption by AI companies is uneven and it is not a ranking factor, but it is cheap to add and harmless.</p>
<h2>Be mentioned elsewhere</h2>
<p>AI answers draw on what many sources say. Genuine mentions in industry directories, local press, partner sites and review platforms make your business more likely to be named. Earn them honestly; fabricated reviews and paid fake articles carry legal and reputational risk.</p>
<h2>Check what the assistants say now</h2>
<p>Ask ChatGPT, Claude, Perplexity and Gemini the questions your customers ask. Note whether you appear and what they get wrong, then fix the source pages. Repeat monthly.</p>
<p>For the local side of this, see our <a href="/google-business-profile-local-seo/">Google Business Profile guide</a>.</p>
""",
faq=[("What is GEO or AEO?", "Generative or answer engine optimisation: making your content easy for AI systems to find, understand and cite in generated answers."),
     ("Does llms.txt improve rankings?", "It is not a ranking factor and adoption is uneven, but it is a low-cost way to summarise your site for language models.")]),
]
