"""SmallBizWire article content. Facts about Drifted and Housefly come only from their own published sites."""

D = '<a href="https://driftedmarketing.com">Drifted Marketing</a>'
H = '<a href="https://heyhousefly.com">Housefly</a>'

ARTICLES = [
dict(slug='how-small-businesses-should-use-ai-assistants',
kicker='AI at work',
title='How small businesses should actually use AI assistants',
dek='Skip the novelty. The useful jobs are drafting, remembering and reminding, with a human saying yes before anything goes out.',
housefly=True,
answer='Use an AI assistant for drafting, summarising, remembering and reminding, not for acting alone. Let it write first drafts of replies and follow-ups, condense long threads and contracts, and track promises and deadlines. Keep a person approving anything that goes to a customer, spends money or changes an account, and never paste in data you would not share.',
hub='ai-assistants',
body="""
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
<p>General chat assistants such as ChatGPT, Claude, Gemini and Microsoft Copilot are flexible and inexpensive, and they suit owners who will sit down and use them deliberately. Some newer products take a different shape: an assistant you text, which keeps a running memory of your business and speaks up when something needs you. <a href="https://heyhousefly.com">Housefly</a>, made by SmallBizWire's publisher, is one example. We compare the options in <a href="/best-ai-assistants-for-small-business/">our guide to AI assistants for small business</a>.</p>
<h2>A one-week trial plan</h2>
<ol>
<li>Pick three recurring tasks from the list above.</li>
<li>Use an assistant for each, every time it comes up, for five working days.</li>
<li>Note how long each took before and after, and how much editing the drafts needed.</li>
<li>Keep what saved time. Drop what did not.</li>
</ol>
<p>That small test tells you more than any demo.</p>
<h2>How do I set rules for what an AI assistant can do?</h2>
<p>Before you hand an assistant any real work, write down three short lists. It takes ten minutes and saves most of the mistakes owners make in the first month.</p>
<table>
<thead><tr><th>Category</th><th>Examples</th><th>Rule</th></tr></thead>
<tbody>
<tr><td>Free to do</td><td>Drafting, summarising, searching your own notes, preparing a call brief</td><td>No approval needed; you read the output before using it</td></tr>
<tr><td>Ask first</td><td>Sending an email, posting on social media, replying to a review, booking a meeting</td><td>The assistant prepares it and waits for a clear yes</td></tr>
<tr><td>Never</td><td>Moving money, changing ad budgets, deleting records, sharing passwords</td><td>A person does these by hand, every time</td></tr>
</tbody>
</table>
<p>The middle row is where most of the value and most of the risk sit. A good assistant makes the "ask first" step fast: it states what it is about to do in one plain sentence, and you approve or reject it. If a tool cannot show you exactly what it will send before it sends it, keep it in the first row only.</p>
<h2>What should I never paste into an AI chatbot?</h2>
<p>Treat a general-purpose chatbot like an email to a contractor you have not vetted. Check the provider's data policy, and look for a business or team plan if you will be sharing customer details, since these often come with stronger commitments about training and retention than free consumer plans. As a working rule, keep these out of any chat window:</p>
<ul>
<li>Passwords, API keys and login codes.</li>
<li>Card numbers, bank details and government ID numbers.</li>
<li>Health information or anything covered by a confidentiality agreement.</li>
<li>Full customer lists exported from your CRM or store.</li>
</ul>
<p>If you need the assistant to work with sensitive material, strip names and numbers first, or use a tool built to keep each business's data separate.</p>
<h2>How do I get better drafts out of an assistant?</h2>
<p>Bland output usually comes from a bland request. Give the assistant the same briefing you would give a new employee:</p>
<ol>
<li><strong>Who it is for.</strong> "A returning customer who complained about late delivery."</li>
<li><strong>What you want to happen.</strong> "Keep the order, not refund it."</li>
<li><strong>Your voice.</strong> Paste two or three real emails you have written and say "write like this."</li>
<li><strong>Constraints.</strong> Length, what not to promise, any facts that must be included.</li>
</ol>
<p>Save the best of these briefings as reusable templates. After a few weeks you will have a small library that covers most of your routine writing.</p>
<h2>How do I measure whether it is working?</h2>
<p>Pick one job, such as replying to quote requests, and note roughly how long it takes for two weeks before and two weeks after. Also note how often you had to rewrite the draft heavily. If the time saved is real and the rewrites are falling, expand to the next job. If not, the task may be too judgement-heavy for an assistant, and that is useful to know.</p>
<p>Email is the job most owners start with, and it only helps if your messages actually arrive, so it is worth setting up <a href="/spf-dkim-dmarc-explained/">SPF, DKIM and DMARC</a> properly before you scale up drafting. When you are ready to choose a tool, our <a href="/best-ai-assistants-for-small-business/">comparison of the main AI assistants</a> sets out the trade-offs.</p>
<h2>A first-month plan</h2>
<ul>
<li><strong>Week 1:</strong> Write your three lists. Choose one drafting job.</li>
<li><strong>Week 2:</strong> Build two or three briefing templates for that job and use them daily.</li>
<li><strong>Week 3:</strong> Add summaries of long threads or calls.</li>
<li><strong>Week 4:</strong> Review time saved and errors caught, then decide whether to add reminders and memory.</li>
</ul>
""",
faq=[('Should an AI assistant send emails for my business automatically?', 'Generally no. Let it draft, and keep a person approving anything that goes to a customer, spends money or changes an account.'),
('Is it safe to put customer information into an AI chatbot?', "It depends on the provider's data terms. Check whether inputs are used for training, how long they are retained and who can see them, and never paste passwords or payment details."),
('What is the best first task to give an AI assistant?', 'A repetitive writing job you already do weekly, such as follow-up emails or answers to common customer questions.'),
('Do I need a paid AI plan for my business?', "Not to start. Free plans are fine for testing drafting on non-sensitive material. Move to a business plan once you share customer details or need the provider's stronger data commitments."),
('Will customers know my emails were drafted by AI?', 'Only if the drafts read generically. Briefing the assistant with your own past emails and editing every draft before sending keeps your voice.')]),
dict(slug='spf-dkim-dmarc-explained',
kicker='Email deliverability',
title='SPF, DKIM and DMARC, explained for people who just want their email delivered',
dek='Three DNS records decide whether Gmail and Outlook trust mail from your domain. Here is what each one does and how to set them up.',
answer="SPF lists the servers allowed to send mail for your domain, DKIM adds a cryptographic signature proving a message was not altered, and DMARC tells receiving providers what to do when those checks fail. Google and Yahoo's 2024 bulk sender requirements made all three effectively mandatory for anyone sending at volume, and they help every small business.",
hub='email-deliverability',
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
<h2>How do SPF, DKIM and DMARC compare?</h2>
<table>
<thead><tr><th></th><th>SPF</th><th>DKIM</th><th>DMARC</th></tr></thead>
<tbody>
<tr><td>What it checks</td><td>Was this sent from an approved server?</td><td>Was this message signed by the domain and left unaltered?</td><td>Do SPF or DKIM pass and align with the visible From domain?</td></tr>
<tr><td>Where it lives</td><td>One TXT record on your domain</td><td>A TXT record per sending service, under a selector name</td><td>One TXT record at <code>_dmarc.yourdomain.com</code></td></tr>
<tr><td>Common mistake</td><td>Two SPF records, or too many lookups</td><td>Never switching it on in the sending tool</td><td>Jumping straight to reject before reading reports</td></tr>
</tbody>
</table>
<h2>How do I set them up, step by step?</h2>
<ol>
<li><strong>List every service that sends as your domain.</strong> Your mailbox provider, your newsletter tool, your store platform, your invoicing app, your help desk. Missing one is the most common cause of failures later.</li>
<li><strong>Write one SPF record.</strong> Combine each service's <code>include:</code> into a single TXT record ending in <code>~all</code> or <code>-all</code>. SPF allows a maximum of ten DNS lookups; if you exceed it, the check fails.</li>
<li><strong>Turn on DKIM in each service.</strong> Each tool gives you a record to add to your DNS. Add it, then press the verify button in the tool.</li>
<li><strong>Publish DMARC at monitoring level.</strong> A starting record looks like <code>v=DMARC1; p=none; rua=mailto:reports@yourdomain.com</code>.</li>
<li><strong>Read the reports for two to four weeks.</strong> They show which sources pass and fail. Fix anything legitimate that fails.</li>
<li><strong>Tighten the policy.</strong> Move to <code>p=quarantine</code>, then <code>p=reject</code> once legitimate mail passes consistently.</li>
</ol>
<h2>What does "alignment" mean in DMARC?</h2>
<p>DMARC does not just ask whether SPF or DKIM passed. It asks whether the domain that passed matches the domain your recipient sees in the From line. A newsletter tool might pass SPF for its own domain while your From line shows yours; that pass does not count for DMARC. Setting up DKIM with your own domain in each tool is usually the simplest way to get aligned passes.</p>
<h2>How do I check my records are working?</h2>
<ul>
<li>Send a message to a Gmail address, open it, choose "Show original" and look for PASS next to SPF, DKIM and DMARC.</li>
<li>Use a free DNS lookup tool to confirm there is exactly one SPF record.</li>
<li>Register with Google Postmaster Tools if you send meaningful volume to Gmail users, to watch spam rate and domain reputation.</li>
</ul>
<p>Authentication is the foundation, not the whole job. If you send outreach, read our <a href="/cold-email-warm-up-guide/">guide to warming up a new domain</a> and run through the <a href="/cold-email-deliverability-checklist/">cold-email deliverability checklist</a> before each campaign.</p>
<h2>What happens if I get it wrong?</h2>
<p>Usually nothing dramatic at first: some messages land in spam, invoices go unread, and nobody tells you. With a strict DMARC policy and a forgotten sending service, that service's mail can be rejected outright. That is why monitoring comes before enforcement. Make a note of every DNS change you make and the date, so that if delivery drops you can trace it back.</p>
""",
faq=[('Do I need SPF, DKIM and DMARC for a small business?', 'Yes. Major mailbox providers expect all senders to authenticate, and bulk senders to Gmail and Yahoo are required to.'),
('Can I have two SPF records?', 'No. A domain should have exactly one SPF record. Combine all sending services into it.'),
('What DMARC policy should I start with?', 'Start with p=none to collect reports, then move to quarantine and reject once only legitimate senders appear.'),
('How do I know if my DMARC record is working?', 'Open a message you sent in Gmail, choose Show original, and check for DMARC PASS. Your DMARC aggregate reports will also list passing and failing sources.'),
('Does SPF alone stop spoofing?', 'No. SPF checks the hidden envelope sender, not the From line people see. DMARC is what ties the checks to the visible From domain.')]),
dict(slug='cold-email-warm-up-guide',
kicker='Email deliverability',
title='Cold email warm-up: how to build sender reputation without burning your domain',
dek='A new mailbox that sends hundreds of emails on day one looks like spam. Warm-up is the slow, boring fix.',
answer='Warm up a new cold-email domain by sending small, slowly rising volumes of real, wanted mail for several weeks before outreach. Use a separate domain from your main one, authenticate it with SPF, DKIM and DMARC, start with a handful of messages a day, increase gradually, and pause the moment bounces or spam complaints rise.',
hub='email-deliverability',
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
<h2>What does a sensible warm-up schedule look like?</h2>
<p>There is no official schedule, and mailbox providers do not publish thresholds, so treat any plan as a cautious guide rather than a rule. The principle is gradual growth with no sudden jumps. A conservative pattern for a single new inbox might look like this:</p>
<table>
<thead><tr><th>Period</th><th>Daily sends per inbox</th><th>What to send</th></tr></thead>
<tbody>
<tr><td>Week 1</td><td>Very low, single digits</td><td>Real conversations with colleagues, partners and people who will reply</td></tr>
<tr><td>Week 2</td><td>Low, rising slowly</td><td>More real conversations; replies to inbound messages</td></tr>
<tr><td>Weeks 3–4</td><td>Moderate</td><td>First small batches of carefully targeted outreach</td></tr>
<tr><td>After week 4</td><td>Hold steady</td><td>Scale by adding inboxes, not by pushing one inbox harder</td></tr>
</tbody>
</table>
<h2>How do I set up a domain for cold email?</h2>
<ol>
<li>Register a domain close to your main brand, so prospects recognise it.</li>
<li>Point its website to your main site, so it does not look abandoned.</li>
<li>Create one or a few named inboxes with a real person's name, photo and signature.</li>
<li>Publish SPF, DKIM and DMARC, as explained in our <a href="/spf-dkim-dmarc-explained/">plain-English authentication guide</a>.</li>
<li>Wait a little before sending; brand-new domains are often treated with suspicion.</li>
</ol>
<h2>What signals tell me warm-up is going wrong?</h2>
<ul>
<li><strong>Bounces climbing.</strong> Usually a list problem. Verify addresses before sending and remove anything that bounces.</li>
<li><strong>Spam complaints.</strong> Google's 2024 bulk sender guidance asks senders to keep reported spam rates low, and below 0.3% at the very most. Cold mail should aim far lower.</li>
<li><strong>Replies drying up.</strong> If people who replied before stop replying, your mail may be landing in spam.</li>
<li><strong>Postmaster data.</strong> Google Postmaster Tools can show domain reputation once you send enough volume to Gmail.</li>
</ul>
<p>When any of these move the wrong way, cut volume, fix the cause, and only then resume.</p>
<h2>Do automated warm-up tools help?</h2>
<p>Automated warm-up networks send messages between participating inboxes and mark them as important. Opinions differ on how much providers credit this activity, and some providers' terms frown on artificial engagement. They are not a substitute for a clean list, relevant messages and patient volume. If you use one, treat it as a supplement and keep sending real mail too.</p>
<h2>How do I keep a domain healthy after warm-up?</h2>
<ul>
<li>Keep daily volume per inbox steady rather than spiky.</li>
<li>Write short, plain-text messages that refer to something specific about the recipient.</li>
<li>Include a simple way to opt out, and honour it immediately.</li>
<li>Stop sequences when someone replies.</li>
<li>Rest a domain if its numbers deteriorate, instead of pushing through.</li>
</ul>
<p>Before each campaign, run through the <a href="/cold-email-deliverability-checklist/">deliverability checklist</a>. Most damage happens in the first campaign after warm-up, when excitement leads to sending too much, too fast.</p>
<h2>What does a good warm-up message look like?</h2>
<p>The best warm-up mail is mail you would send anyway. Reply to suppliers from the new inbox, send meeting confirmations, introduce yourself to partners and ask colleagues to reply with a real sentence rather than a one-word acknowledgement. Conversations with back-and-forth replies are a stronger positive signal than one-way announcements. Avoid sending the same template to dozens of friendly contacts, which looks like the bulk pattern you are trying to avoid. Keep a short note of what you sent each day and how many replies arrived, so that when outreach begins you have a baseline to compare against. If the baseline was healthy and outreach numbers fall, the change in behaviour is the likely cause.</p>
""",
faq=[('How long does email warm-up take?', 'Most practitioners allow three to four weeks of gradually increasing volume before sending at full pace, and keep volume steady afterwards.'),
('Should I send cold email from my main domain?', 'Many businesses use a separate, clearly related domain for outreach so their everyday mail is protected if reputation suffers.'),
('Do warm-up tools work?', 'They can help build history, but genuine replies from real recipients are a stronger signal and cannot be replaced.'),
('How many cold emails can I send per day per inbox?', 'No provider publishes a safe number. Keep per-inbox volume modest and steady, and grow by adding inboxes and domains rather than pushing one inbox harder.'),
('What should I do if my domain lands in spam?', 'Pause outreach, check authentication, clean the list, and send only real conversations at low volume until replies and inbox placement recover.')]),
dict(slug='cold-email-deliverability-checklist',
kicker='Email deliverability',
title='The cold-email deliverability checklist',
dek='Twenty checks to run before your next outbound campaign, from DNS records to the wording of your first line.',
answer='Before any cold-email campaign, confirm one SPF record, passing DKIM, a published DMARC record and alignment; use a warmed, separate sending domain; verify every address; keep volume steady per inbox; write short, specific plain-text messages with an easy opt-out; and watch bounces, complaints and replies daily, pausing at the first warning sign.',
hub='email-deliverability',
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
<h2>How do I use this checklist?</h2>
<p>Run through it before the first send of every campaign, not once a year. Most deliverability problems are introduced by a change: a new sending tool, a bought list, a new template with heavy tracking. Tick each item off or write down why it does not apply.</p>
<h2>Which items matter most?</h2>
<table>
<thead><tr><th>Item</th><th>Why it matters</th><th>Quick check</th></tr></thead>
<tbody>
<tr><td>Authentication</td><td>Major providers expect SPF, DKIM and DMARC from bulk senders since their 2024 requirements</td><td>Gmail "Show original" shows PASS for all three</td></tr>
<tr><td>List verification</td><td>High bounce rates are a strong negative signal</td><td>Run the list through a verification service before import</td></tr>
<tr><td>Warmed domain</td><td>New domains carry little reputation</td><td>The domain has weeks of real, low-volume sending behind it</td></tr>
<tr><td>Opt-out</td><td>Complaints damage reputation, and laws such as CAN-SPAM require a way to opt out of commercial email</td><td>Every message has a clear, working opt-out line</td></tr>
</tbody>
</table>
<h2>What should I check on the day of sending?</h2>
<ol>
<li>Send a test to your own Gmail and Outlook addresses and confirm they land in the inbox.</li>
<li>Click every link and confirm none point to a broken or unrelated page.</li>
<li>Check personalisation fields for blanks; "Hi {first_name}" undoes everything else.</li>
<li>Confirm the sending schedule spreads messages through the working day rather than in one burst.</li>
<li>Confirm that replies stop the sequence for that contact.</li>
</ol>
<h2>What should I watch in the first 72 hours?</h2>
<ul>
<li><strong>Bounce rate.</strong> If it is clearly higher than your test lists, stop and re-verify.</li>
<li><strong>Spam complaints.</strong> Any visible rise is a reason to pause.</li>
<li><strong>Reply rate.</strong> A sudden drop compared with earlier campaigns can mean spam-folder placement.</li>
<li><strong>Out-of-office and auto-replies.</strong> These confirm delivery and sometimes reveal a better contact.</li>
</ul>
<h2>What are the most common mistakes?</h2>
<ul>
<li>Sending from the main business domain, so a bad campaign hurts invoices and customer mail.</li>
<li>Using bought or scraped lists without verification.</li>
<li>Heavy HTML, images and multiple tracking links in a first-touch email.</li>
<li>Long sequences that keep emailing people who never engaged.</li>
<li>Scaling volume the week warm-up ends.</li>
</ul>
<p>If any authentication item is unclear, our <a href="/spf-dkim-dmarc-explained/">SPF, DKIM and DMARC explainer</a> walks through each record. For new domains, the <a href="/cold-email-warm-up-guide/">warm-up guide</a> explains how to build reputation before the first campaign.</p>
<h2>What should I record after each campaign?</h2>
<p>Keep a simple log: date, domain, inboxes used, number sent, bounces, complaints, replies and anything you changed. Over a few campaigns this log tells you which domains are healthy, which templates work and which list sources to drop. It is also the first thing to read when results suddenly fall.</p>
<p>Finally, remember that the message itself is part of deliverability. A short note that clearly relates to the recipient's business earns replies, and replies are among the best signals a sender can earn. Write for one person, not for a list.</p>
<h2>How do I keep my list clean between campaigns?</h2>
<p>Lists decay. People change jobs, companies close and inboxes are abandoned, so an address that was valid six months ago may bounce today. Re-verify any list older than a few months before reusing it. Remove hard bounces immediately and never retry them. Add anyone who asks to stop to a suppression list that every tool and every domain checks before sending, so a person who opted out on one domain is not contacted from another. Remove contacts who have received a full sequence without opening or replying; continuing to email them adds risk and almost no chance of a reply. Finally, record where each list came from. When one source produces high bounces or complaints, you can drop it without discarding the rest. A smaller list of the right people will usually outperform a bigger list of uncertain ones, both in replies and in the long-term health of your domains.</p>
""",
faq=[('What is a good bounce rate for cold email?', 'As low as you can get it. Verify every address first; a noticeably higher bounce rate than your previous campaigns is a reason to stop and clean the list.'),
('Should cold emails include images or tracking?', 'Keep first-touch emails plain text with few or no links. Heavy HTML, images and tracking links look like bulk marketing and can hurt placement.'),
('How often should I run this checklist?', 'Before every campaign, and whenever you change a sending tool, domain, list source or template.'),
('Is cold email legal?', 'Rules vary by country. In the US, CAN-SPAM allows commercial email with honest headers, a physical address and a working opt-out; stricter consent rules apply in places such as the EU and Canada.')]),
dict(slug='shopify-seo-guide',
kicker='Ecommerce SEO',
title='Shopify SEO for small stores: what actually moves rankings',
dek='Shopify handles the technical basics. What it cannot do for you is decide what each page is about.',
answer='Shopify SEO for small stores comes down to a few jobs: write unique titles and meta descriptions for products and collections, build collection pages around what customers search, fix duplicate and thin content, redirect deleted products, compress images with descriptive alt text, keep the theme fast, and earn links and reviews. Technical basics are largely handled by Shopify itself.',
hub='shopify-ecommerce',
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
<h2>What does Shopify handle for me, and what do I have to do?</h2>
<table>
<thead><tr><th>Handled by Shopify</th><th>Your job</th></tr></thead>
<tbody>
<tr><td>Automatic sitemap.xml</td><td>Submitting it in Google Search Console</td></tr>
<tr><td>Canonical tags on product variants and collection paths</td><td>Avoiding near-duplicate products and copied descriptions</td></tr>
<tr><td>SSL certificate</td><td>Making sure every link and image uses the HTTPS address</td></tr>
<tr><td>Editable title, meta description and URL fields</td><td>Writing them well for every product and collection</td></tr>
<tr><td>A URL redirect tool</td><td>Adding a redirect whenever you delete or rename a page</td></tr>
</tbody>
</table>
<h2>How should I plan collections for search?</h2>
<p>Collection pages are often a small store's best chance to rank, because they match broader searches such as "linen bedding" or "leather dog collars." Plan them from search demand, not just from your internal stock categories:</p>
<ol>
<li>List the phrases customers actually type. Google's autocomplete and the "related searches" at the foot of the results page are free starting points.</li>
<li>Group phrases that mean the same thing into one collection.</li>
<li>Give each collection a clear title, a unique meta description and a short introduction of genuinely useful copy, such as how to choose between options.</li>
<li>Link related collections to each other and from your navigation.</li>
</ol>
<h2>Which technical issues should I check?</h2>
<ul>
<li><strong>Speed.</strong> Every app can add scripts. Remove apps you no longer use, and check that their code has gone too. Test key pages with Google's PageSpeed Insights.</li>
<li><strong>Images.</strong> Compress before upload, and write alt text that describes the image plainly.</li>
<li><strong>Broken links.</strong> Deleted products and changed handles create 404 pages. Use Shopify's redirects to point them at the closest live page.</li>
<li><strong>Indexing.</strong> Search Console's page indexing report shows what Google has and has not indexed, and why.</li>
<li><strong>Structured data.</strong> Many themes output product schema; check with Google's Rich Results Test that price, availability and reviews appear correctly.</li>
</ul>
<h2>Should my Shopify store have a blog?</h2>
<p>Only if you will publish useful pieces regularly. Buying guides, care instructions and comparison posts can rank for questions your product pages cannot answer, and they can link to the right collection. A blog with three posts from two years ago does little harm, but it does no good either. Pick a small number of genuine customer questions and answer them thoroughly.</p>
<h2>What is a sensible monthly SEO routine?</h2>
<ul>
<li>Check Search Console for new indexing errors and pages losing clicks.</li>
<li>Fix any 404s with redirects.</li>
<li>Improve the titles and descriptions of the five products with the most impressions and the fewest clicks.</li>
<li>Add or refresh one collection introduction or guide.</li>
<li>Ask recent customers for reviews.</li>
</ul>
<p>The product page itself is where rankings turn into sales; our guide to <a href="/shopify-product-page-seo/">writing Shopify product pages that rank and sell</a> covers it in detail. And if paid traffic lands on your store, the <a href="/landing-page-anatomy/">landing page anatomy guide</a> explains what visitors need to see first.</p>
""",
faq=[('Is Shopify good for SEO?', 'Yes. It handles sitemaps, canonical tags, SSL and hosting. Most improvement comes from better titles, descriptions, collection content and image optimisation.'),
('Where do I edit SEO titles in Shopify?', 'On each product, collection or page, scroll to the Search engine listing section and choose Edit.'),
('What should I do when I delete a Shopify product?', 'Add a URL redirect to the closest alternative so visitors and search engines are not sent to a 404 page.'),
('How long does Shopify SEO take to show results?', 'Usually months rather than weeks, depending on competition and how much the site changes. Track impressions and clicks in Search Console to see early movement.'),
('Do Shopify SEO apps help?', 'Some save time on alt text, redirects or schema, but none replace good titles, useful copy and a fast theme. Remove apps you stop using, since leftover scripts slow the store.')]),
dict(slug='shopify-product-page-seo',
kicker='Ecommerce SEO',
title='How to write a Shopify product page that ranks and sells',
dek='A product page has two readers: a search engine deciding what it is about, and a buyer deciding whether to trust you.',
answer="A Shopify product page that ranks and sells has a clear, searchable product title, a unique SEO title and meta description, an original description that answers buyers' real questions, compressed photos with descriptive alt text, visible price, shipping and returns information, genuine reviews, and structured data so search engines can show price and availability.",
hub='shopify-ecommerce',
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
<h2>What should a product page include, from top to bottom?</h2>
<ol>
<li><strong>Product title.</strong> What it is, in the words buyers use, plus the key differentiator: material, size or use.</li>
<li><strong>Photos.</strong> Several angles, scale against something familiar, and the product in use.</li>
<li><strong>Price and options.</strong> Clear variant selectors, with stock status visible.</li>
<li><strong>Short benefit summary.</strong> Two or three lines that say why this one, for whom.</li>
<li><strong>Add to cart.</strong> Visible without scrolling on a phone.</li>
<li><strong>Details.</strong> Dimensions, materials, care, what is in the box.</li>
<li><strong>Shipping and returns.</strong> Costs, times and the returns window, stated near the button.</li>
<li><strong>Reviews.</strong> Real ones, including the critical ones.</li>
<li><strong>Related products.</strong> Accessories or alternatives that genuinely fit.</li>
</ol>
<h2>How do I write a product description that is not copied?</h2>
<p>Manufacturer descriptions appear on every store selling the same item, so they give search engines no reason to prefer yours. Write your own using this sequence:</p>
<ul>
<li>Start with who it is for and the problem it solves.</li>
<li>Answer the questions customers ask you in messages and returns. Those are the doubts stopping other people from buying.</li>
<li>Give specifics: measurements, weights, materials, compatibility.</li>
<li>Be honest about limits. "Not dishwasher safe" prevents returns and builds trust.</li>
</ul>
<h2>How do I write the SEO title and meta description?</h2>
<table>
<thead><tr><th>Field</th><th>Aim</th><th>Example pattern</th></tr></thead>
<tbody>
<tr><td>SEO title</td><td>Roughly 50–60 characters, main phrase first</td><td>Product type, key feature | Store name</td></tr>
<tr><td>Meta description</td><td>Roughly 150–160 characters, a reason to click</td><td>What it is, one benefit, one reassurance such as delivery or returns</td></tr>
<tr><td>URL handle</td><td>Short, lowercase, hyphenated</td><td>/products/product-type-key-feature</td></tr>
<tr><td>Image alt text</td><td>Plain description of the image</td><td>Colour, product, and what is shown</td></tr>
</tbody>
</table>
<p>Google may rewrite titles and descriptions, so treat these as strong suggestions, not guarantees. Write them for a person deciding which result to click.</p>
<h2>How do variants affect SEO?</h2>
<p>Keep sizes and colours of the same item as variants on one product, not as separate products with near-identical text. That concentrates reviews and links on one page. Create separate products only when the items are genuinely different and people search for them separately.</p>
<h2>What should I do when a product goes out of stock?</h2>
<ul>
<li>Temporarily out of stock: keep the page live, show the status and offer a back-in-stock alert.</li>
<li>Permanently discontinued: redirect the URL to the closest replacement or its collection.</li>
<li>Never leave a popular page returning a 404.</li>
</ul>
<h2>A quick audit for your top products</h2>
<p>Open your ten best-selling products on a phone and check: is the price, button and delivery information visible quickly? Is the description your own? Does every image have alt text? Are reviews showing? Fix the gaps on these ten first, as they carry most of the revenue.</p>
<p>For the store-wide picture, including collections, redirects and speed, see our <a href="/shopify-seo-guide/">Shopify SEO guide</a>. The same principles of clarity and a single next step apply to any page you send ad traffic to, as set out in <a href="/landing-page-anatomy/">the anatomy of a landing page that converts</a>.</p>
<h2>Which mistakes cost the most?</h2>
<ul>
<li>Leaving the default SEO title, which is often just the product name with no context.</li>
<li>Uploading huge, uncompressed photos that slow the page on mobile.</li>
<li>Hiding delivery costs until checkout, which drives abandoned carts.</li>
<li>Creating a new product for every colour, splitting reviews across pages.</li>
<li>Deleting products without redirecting their URLs.</li>
<li>Copying the same description across several similar products.</li>
</ul>
<p>Each of these is quick to fix and worth more than any app or plugin. Work through your best-selling products first, then apply the same pattern to new products as you add them, so the catalogue improves steadily instead of in occasional large clean-ups.</p>
""",
faq=[('How long should a Shopify product description be?', 'Long enough to answer real buyer questions. A few short paragraphs plus a details list suits most products; thin one-liners and copied text are the bigger problems.'),
("Can I use the manufacturer's product description?", 'You can, but it duplicates every other store selling the item. An original description written around customer questions gives search engines and buyers a reason to choose you.'),
('Should each colour be a separate product?', 'Usually no. Keep colours and sizes as variants of one product so reviews and links build up on a single page.'),
('Do reviews help product page SEO?', 'Genuine reviews add fresh, original text and reassure buyers. With correct structured data, review ratings can also appear in search results, though Google decides when to show them.')]),
dict(slug='landing-page-anatomy',
kicker='Conversion',
title='The anatomy of a landing page that converts',
dek='One page, one audience, one action. Most underperforming landing pages break at least one of the three.',
answer='A landing page that converts has one goal and one call to action, a headline that matches the ad or link that brought the visitor, a short explanation of the benefit, proof such as genuine reviews, answers to the main objections, a short form or simple button, fast loading on mobile, and no navigation that leads visitors away.',
hub='shopify-ecommerce',
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
<h2>What goes in each section of a landing page?</h2>
<table>
<thead><tr><th>Section</th><th>Job</th><th>Common mistake</th></tr></thead>
<tbody>
<tr><td>Headline</td><td>Confirm the visitor is in the right place</td><td>A clever line that does not match the ad</td></tr>
<tr><td>Subheadline</td><td>Say what they get and why it matters</td><td>Listing features instead of outcomes</td></tr>
<tr><td>Call to action</td><td>One clear next step</td><td>Three competing buttons</td></tr>
<tr><td>Proof</td><td>Show that others trust you</td><td>Vague or unattributable testimonials</td></tr>
<tr><td>Objections</td><td>Answer price, time and risk doubts</td><td>Hiding terms until checkout</td></tr>
<tr><td>Final call to action</td><td>Catch people who read to the end</td><td>Ending on a footer full of links</td></tr>
</tbody>
</table>
<h2>Why does message match matter so much?</h2>
<p>A visitor clicking an ad already has a promise in mind. If the ad says "same-day boiler repair" and the page opens with "Welcome to our heating and plumbing family," the visitor has to work out whether they are in the right place, and many will not bother. Repeat the ad's key phrase in the headline. If you run several ads with different promises, give each its own page or headline.</p>
<h2>How do I write a call to action people click?</h2>
<ul>
<li>Describe what happens next: "Get my quote," "Book a 15-minute call," "See prices."</li>
<li>Reduce the perceived risk beside the button: "No card needed," "Reply within one working day."</li>
<li>Keep the button visible early on a phone, and repeat it after the proof and again at the end.</li>
</ul>
<h2>What proof should I use if I am new?</h2>
<p>Never invent reviews or results. If you have little social proof yet, use what is true: your qualifications, years in the trade, a guarantee you will honour, photos of real work, a clear named person behind the business, and specific details of how the service works. Genuine reviews can be added as they arrive. Fabricated ones are a legal and reputational risk, and regulators such as the US Federal Trade Commission have rules against fake reviews.</p>
<h2>How fast does a landing page need to be?</h2>
<p>As fast as you can make it, especially on mobile data. Compress images, avoid autoplaying video at the top, and remove unnecessary scripts. Google's PageSpeed Insights gives a free report with specific fixes. A slow page wastes ad spend before the visitor has read a word.</p>
<h2>How do I test and improve a landing page?</h2>
<ol>
<li>Set up conversion tracking so you know what counts as a success.</li>
<li>Watch where people drop off, using your analytics or a session recording tool if your privacy policy allows it.</li>
<li>Change one major element at a time: headline, offer, form length or proof.</li>
<li>Give each test enough traffic and time before deciding; small samples mislead.</li>
</ol>
<h2>A pre-launch checklist</h2>
<ul>
<li>Headline matches the ad.</li>
<li>One goal, one main button.</li>
<li>Navigation removed or reduced.</li>
<li>Form asks only what you need right now.</li>
<li>Contact details, terms and privacy policy linked.</li>
<li>Tested on a real phone, on mobile data.</li>
<li>Conversion tracking fires on a test submission.</li>
</ul>
<p>If the landing page is a product page in your store, the advice in our guide to <a href="/shopify-product-page-seo/">Shopify product pages</a> applies too. And if you hire help to build or run the campaign, our guide to <a href="/how-to-choose-a-marketing-agency/">choosing a marketing agency</a> lists the questions to ask about tracking and ownership.</p>
<h2>How long should the form be?</h2>
<p>Ask only for what you need to take the next step. For a quote request that is often a name, a contact method and one or two details about the job. Every extra field asks the visitor for more effort before they have received anything, and some will leave. If you need more information later, ask for it in the follow-up. Label each field clearly, show errors next to the field that caused them, and confirm what happens after submission, such as "We will reply within one working day." Test the form yourself on a phone, including what happens when you make a mistake. Broken or confusing forms are one of the most common and least noticed reasons a page underperforms.</p>
""",
faq=[('What is the difference between a landing page and a homepage?', 'A homepage serves many visitors and paths. A landing page serves one audience and asks for one action.'),
('How many form fields should a landing page have?', 'Only the ones you will actually use to follow up. Fewer fields generally mean more completions.'),
('Should a landing page have navigation?', 'Usually minimal or none. Every extra link is a way to leave without converting, though contact details, terms and a privacy policy should still be reachable.'),
('How long should a landing page be?', "As long as it takes to answer the visitor's main doubts. Simple, cheap offers can be short; expensive or unfamiliar ones usually need more proof and objection handling."),
('What should I test first on a landing page?', 'Start with the element most likely to matter: usually the headline and offer, then form length, then proof. Change one thing at a time.')]),
dict(slug='how-to-choose-a-marketing-agency',
kicker='Hiring help',
title='How to choose a marketing agency when you are a small business',
dek='Ten questions that separate agencies who will move your numbers from those who will send you reports.',
drifted=True,
answer='Choose a marketing agency by agreeing one measurable goal and date before signing, confirming who will actually do the work, making sure ad accounts, pixels and analytics are in your name, checking references from similar businesses, understanding the full cost including ad spend and fees, and agreeing exit terms and reporting in writing before work begins.',
hub='agencies-and-pricing',
body="""
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
<p>A specialist (only paid search, only SEO) is often stronger in its lane. A small full-service team can be better when your ads, content and website need to work together and you would rather have one point of contact. Our list of <a href="/best-marketing-agencies-for-small-business/">agencies for small business</a> includes both kinds. One of them is <a href="https://driftedmarketing.com">Drifted Marketing</a>, SmallBizWire's publisher, which says on its site that it writes one metric and one date into its contracts and keeps ad spend in the client's own account. Those are exactly the kinds of commitments to ask any agency for.</p>
<h2>What should be in a marketing agency contract?</h2>
<table>
<thead><tr><th>Clause</th><th>What to look for</th><th>Red flag</th></tr></thead>
<tbody>
<tr><td>Goal</td><td>A specific metric and target date</td><td>"Increase brand awareness" with no measure</td></tr>
<tr><td>Scope</td><td>Deliverables per month, listed</td><td>"Ongoing marketing support"</td></tr>
<tr><td>Ownership</td><td>Accounts, creative and data belong to you</td><td>Ads run from the agency's account</td></tr>
<tr><td>Fees</td><td>Fee separate from ad spend, all extras listed</td><td>Undisclosed markups on media</td></tr>
<tr><td>Term and exit</td><td>Reasonable notice period, handover steps</td><td>Long lock-ins with no performance exit</td></tr>
<tr><td>Reporting</td><td>Regular reports against the agreed goal</td><td>Reports full of vanity metrics only</td></tr>
</tbody>
</table>
<h2>How do I compare agency pricing models?</h2>
<ul>
<li><strong>Monthly retainer.</strong> Predictable, suits ongoing work. Make sure the scope is written down so the retainer buys something specific.</li>
<li><strong>Project fee.</strong> Suits a website, a launch or a one-off campaign. Agree what counts as finished.</li>
<li><strong>Percentage of ad spend.</strong> Common in paid media. It can reward spending more rather than spending well, so pair it with a performance goal.</li>
<li><strong>Performance-based.</strong> Attractive in principle, but define the measure carefully and agree how it is tracked.</li>
</ul>
<p>Whatever the model, ask for the total monthly cost including ad spend, tools and production, not just the fee.</p>
<h2>How do I check an agency's claims?</h2>
<ol>
<li>Ask for case studies with the client named, and then ask to speak to that client.</li>
<li>Look at the agency's own marketing. An agency selling content should publish good content.</li>
<li>Check that the people on the sales call are the people who will do the work.</li>
<li>Ask what went wrong on a past project and how they handled it. A candid answer is a good sign.</li>
<li>Be wary of guaranteed rankings or guaranteed returns; nobody controls search engines or markets.</li>
</ol>
<h2>What should happen in the first 90 days?</h2>
<ul>
<li><strong>First two weeks:</strong> access set up in your name, tracking checked, goal and baseline written down.</li>
<li><strong>First month:</strong> first campaigns or content live, first report against the goal.</li>
<li><strong>By day 90:</strong> a clear view of what is working, what is not and what changes next.</li>
</ul>
<p>If after 90 days you cannot tell whether the work is moving the agreed number, that is the conversation to have, calmly and with the contract in hand.</p>
<h2>Agency, freelancer or in-house?</h2>
<p>An agency gives you several skills at once. A freelancer can be cheaper and very good for one discipline. An in-house hire gives you full attention but needs managing and a full salary. Many small businesses start with a freelancer or small agency for a defined goal and bring work in-house once they know what works.</p>
<p>For a starting shortlist, see our roundup of <a href="/best-marketing-agencies-for-small-business/">marketing agencies for small business</a>. If your marketing depends on email, ask any agency how they handle <a href="/spf-dkim-dmarc-explained/">SPF, DKIM and DMARC</a> and domain reputation; vague answers there are a warning sign.</p>
<h2>What should I prepare before talking to agencies?</h2>
<ul>
<li>The one number you most want to move, and by when.</li>
<li>Your current monthly marketing spend, including ads and tools.</li>
<li>A list of the accounts you own: ad platforms, analytics, website, store, email.</li>
<li>What you have tried before and roughly how it went.</li>
<li>Who in your business will make the decision and approve work.</li>
</ul>
<p>Sending the same short brief to every agency makes their answers comparable and shortens every first call.</p>
""",
faq=[('What should I ask a marketing agency before hiring?', 'Ask what they will measure and by when, who will do the work, who owns the ad accounts, what the fee includes, and what the notice period is.'),
("Should my ad accounts be in my name or the agency's?", 'Yours. Owning the accounts, pixels and analytics means you keep your data if you change agencies.'),
('How much should a small business spend on a marketing agency?', 'It depends on goals, market and scope. Ask each agency for the full monthly cost including ad spend, tools and production, and compare against what the agreed goal is worth to you.'),
('How long should I give an agency before judging results?', 'Agree a review point in the contract, often around 90 days for ads and longer for SEO. By then you should at least see clear movement against the agreed measure.'),
('Is a long contract with an agency a bad sign?', 'Not always, but make sure it includes a notice period and handover steps, and that accounts and data stay yours if you leave.')]),
dict(slug='best-marketing-agencies-for-small-business',
kicker="Buyer's guide",
title='Marketing agencies for small business: six worth a look',
dek='A short, honest list across different specialisms and price points, with notes on who each suits.',
drifted=True,
answer='There is no single best marketing agency for every small business. The right one matches your main channel, budget and timezone, keeps ad accounts and data in your name, commits to a measurable goal, and lets you work with the people doing the work. Shortlist two or three, ask the same questions, and call their references.',
hub='agencies-and-pricing',
body="""
<p>There is no single best agency. The right choice depends on what you need most: paid ads, search, content or a team that does several. Below are six agencies of different kinds. We have not ranked them on results, because we cannot independently verify any agency's client results, including our publisher's. Use the <a href="/how-to-choose-a-marketing-agency/">ten questions</a> with whichever you contact.</p>
<p><em>How this list was made:</em> agencies were chosen to cover a range of specialisms and to be well established or clearly described in public. Descriptions are based on what each agency publishes about itself. Nobody paid to be included.</p>
<h2>Drifted Marketing</h2>
<p class="disclosure-inline"><strong>Disclosure:</strong> Drifted Marketing publishes SmallBizWire.</p>
<p><a href="https://driftedmarketing.com">Drifted Marketing</a> describes itself as a growth studio for ads, content and AI apps, based in Karachi and working on New York hours. Its site says the same people plan, shoot, cut and run the work, with no account-management layer in between, that one metric and one date are written into the contract, and that ad spend stays in the client's own account. <strong>Suits:</strong> small businesses that want ads, short-form content and custom software from one team. <a href="/drifted-marketing-profile/">Read our profile.</a></p>
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
<h2>How should I build a shortlist?</h2>
<ol>
<li><strong>Name your main goal.</strong> More leads, more online sales, a new website, or better local visibility. Different agencies are strong at different jobs.</li>
<li><strong>Pick the channel.</strong> Paid social, search ads, SEO, email or content. A generalist is fine for small budgets; a specialist suits one dominant channel.</li>
<li><strong>Set a realistic budget.</strong> Include the agency fee, ad spend and production.</li>
<li><strong>Decide on working hours.</strong> A remote agency can work well if its hours overlap with yours.</li>
<li><strong>Find two or three candidates</strong> through referrals, directories and agencies whose own content you have found useful.</li>
</ol>
<h2>How do I compare agencies side by side?</h2>
<table>
<thead><tr><th>Question</th><th>Why ask it</th></tr></thead>
<tbody>
<tr><td>What metric and date would you commit to?</td><td>Tests whether they think in outcomes</td></tr>
<tr><td>Who will do the work, and can I meet them?</td><td>Reveals whether the work is passed to juniors or subcontractors</td></tr>
<tr><td>Whose name are the accounts in?</td><td>Protects your data and history if you leave</td></tr>
<tr><td>What is the total monthly cost?</td><td>Avoids surprises in ad spend and production</td></tr>
<tr><td>Can I speak with a current client?</td><td>The best check on any claim</td></tr>
<tr><td>What happens if we part ways?</td><td>Shows how they handle handover</td></tr>
</tbody>
</table>
<p>Score each answer simply: clear, vague or missing. The agency with the fewest vague answers is usually the safer choice, even if another has a more impressive portfolio.</p>
<h2>What are the warning signs?</h2>
<ul>
<li>Guaranteed first-page rankings or guaranteed returns.</li>
<li>Reluctance to put accounts in your name.</li>
<li>Case studies with no client names and no way to check them.</li>
<li>Reports focused on impressions and followers with no link to sales or leads.</li>
<li>Pressure to sign quickly or commit to a long term up front.</li>
</ul>
<h2>Should a small business use a local or remote agency?</h2>
<p>Local agencies can meet in person and may know the local market well, which matters for trades and local services. Remote agencies widen the choice and can cost less. What matters most is responsiveness and overlap in working hours. Ask when you can expect replies and who covers when your main contact is away.</p>
<h2>How do I start without a big commitment?</h2>
<p>Ask for a defined first project with a clear end: an audit, a single campaign or a landing page. It shows how the agency communicates and delivers before you sign a retainer. Agree in advance what you will judge it on.</p>
<p>Our full guide to <a href="/how-to-choose-a-marketing-agency/">choosing a marketing agency</a> covers contracts, pricing models and the first 90 days in more detail. If the agency will build pages for ad traffic, compare their approach with <a href="/landing-page-anatomy/">the anatomy of a landing page that converts</a>. SmallBizWire's publisher is one of the agencies listed above, and its own <a href="/drifted-marketing-profile/">profile</a> is written from its published claims.</p>
<h2>What should I do after choosing?</h2>
<p>Write down the goal, the date, the budget and the reporting schedule in one short document and share it with the agency on day one. Set up every account in your own name and give the agency access, rather than the other way round. Book a review meeting at the end of the first month and another around day 90. Keep the questions and scores you used to choose, too: if the relationship ends, they make the next search faster, and they remind you what you were promised. A good agency will welcome this structure, because it makes their results visible.</p>
""",
faq=[('What is the best marketing agency for a small business?', 'It depends on the main channel you need. Shortlist agencies that specialise in it, and compare who does the work, who owns the accounts and what they commit to measuring.'),
('Is Drifted Marketing independent of SmallBizWire?', 'No. Drifted Marketing publishes SmallBizWire, which is disclosed wherever it is featured.'),
('How many agencies should I talk to before choosing?', 'Two or three is usually enough. Ask each the same questions so the answers can be compared fairly.'),
('Are agency directories and rankings reliable?', 'Treat them as a starting list, not a verdict. Some rank by paid placement or self-submitted reviews, so check references yourself.'),
('What is a good first project with a new agency?', 'Something defined with a clear end, such as an audit, one campaign or one landing page, judged on a measure agreed in advance.')]),
dict(slug='best-ai-assistants-for-small-business',
kicker="Buyer's guide",
title='AI assistants for small business: the main options compared',
dek='General chat tools, office-suite assistants and a newer kind you text. What each is good at, and who it suits.',
housefly=True,
answer='The main AI assistants for small business are general chatbots such as ChatGPT, Claude and Gemini, assistants built into office suites like Microsoft Copilot and Gemini for Google Workspace, and specialised assistants. The best choice depends on the tools you already use, how sensitive your data is, your budget, and whether you need drafting only or memory and reminders too.',
hub='ai-assistants',
body="""
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
<p><a href="https://heyhousefly.com">Housefly</a> takes a different shape: rather than an app you open, it is an assistant you text, iMessage first. It keeps track of what you promised clients and what they owe you, prepares a brief before calls, and speaks up when something needs you. Anything that sends, pays or changes an account is stated in one sentence and waits for your yes. Each member's memory is sealed so no other member sees it, and it carries no ads. It is offered as ten founding seats, priced on its site at $3,000 or $6,000 a quarter. <strong>Suits:</strong> founders who want a proactive assistant with private memory and are willing to pay a premium for it. <a href="/housefly-profile/">Read our profile.</a></p>
<h2>How to choose</h2>
<ul>
<li><strong>Already on Google or Microsoft?</strong> Start with the assistant built into your suite.</li>
<li><strong>Need a flexible all-rounder?</strong> Try ChatGPT or Claude for a week on real tasks.</li>
<li><strong>Want something that remembers and reminds, without you opening an app?</strong> Look at texted, memory-first assistants such as Housefly.</li>
</ul>
<p>Whatever you pick, apply the rules in <a href="/how-small-businesses-should-use-ai-assistants/">our guide to using assistants well</a>: it drafts, you approve.</p>
<h2>How do the main types of assistant compare?</h2>
<table>
<thead><tr><th>Type</th><th>Strengths</th><th>Watch for</th></tr></thead>
<tbody>
<tr><td>General chatbots</td><td>Flexible drafting, summarising, brainstorming; low-cost entry plans</td><td>Data settings differ between free, paid and business plans; memory may be limited</td></tr>
<tr><td>Office-suite assistants</td><td>Work inside the email, documents and calendar you already use</td><td>Usually an add-on cost per user; only as good as your files are organised</td></tr>
<tr><td>Built-in tool assistants</td><td>AI features inside your store, CRM or help desk, close to your data</td><td>Each one only sees its own tool</td></tr>
<tr><td>Specialised or concierge assistants</td><td>Built around a particular job, such as tracking promises or briefing before calls</td><td>Higher prices; check how data is kept and who can see it</td></tr>
</tbody>
</table>
<h2>Which questions should I ask before choosing?</h2>
<ol>
<li><strong>Where does my data go?</strong> Read the provider's policy on training, retention and who can access your conversations, and check whether a business plan changes it.</li>
<li><strong>What does it connect to?</strong> Email, calendar, documents, store, CRM. An assistant that cannot see the information has to be fed it by hand.</li>
<li><strong>What can it do without asking?</strong> Prefer tools that draft and wait for approval before sending or changing anything.</li>
<li><strong>Does it remember?</strong> Some assistants keep context between conversations; others start fresh each time.</li>
<li><strong>What does it cost per person?</strong> Include add-ons and usage limits.</li>
</ol>
<h2>How do I run a fair trial?</h2>
<ul>
<li>Pick two candidates and the same three real tasks, such as a customer reply, a meeting summary and a weekly plan.</li>
<li>Use non-sensitive material during the trial.</li>
<li>Score each result on accuracy, how much editing it needed and how long it took.</li>
<li>Note anything it got confidently wrong. Confident errors cost more than obvious ones.</li>
<li>Decide after two weeks, not after the first impressive answer.</li>
</ul>
<h2>Do I need more than one assistant?</h2>
<p>Often, yes, in a modest way. Many businesses use a general chatbot for writing and the AI features built into their existing tools for everything else. Avoid paying for several overlapping general tools; pick one and learn it well.</p>
<h2>What should stay in human hands?</h2>
<p>Whatever you choose, keep a person approving anything that goes to a customer, spends money, or changes an account. Our guide to <a href="/how-small-businesses-should-use-ai-assistants/">how small businesses should actually use AI assistants</a> sets out a simple three-list approach for this. If you are considering a specialised assistant, read its terms on memory and data closely; our <a href="/housefly-profile/">Housefly profile</a> is one example, written from that product's published site by its own publisher.</p>
<h2>A quick decision guide</h2>
<ul>
<li>Mostly writing and ideas, tight budget: start with a general chatbot's paid individual plan.</li>
<li>Team lives in Microsoft 365 or Google Workspace: trial that suite's assistant first.</li>
<li>Most work happens in one platform, such as a store or help desk: try its built-in AI.</li>
<li>Juggling many clients and promises, high value on privacy: compare specialised assistants carefully.</li>
</ul>
<h2>How do I roll an assistant out to a small team?</h2>
<p>Start with one or two people who will actually use it, not the whole team at once. Agree the three lists of what the assistant may do freely, what needs approval and what it must never do, and write them where everyone can see them. Share the best prompts and templates in one place. After a month, compare time saved and errors caught before adding more seats. A slower rollout costs little and avoids paying for licences nobody opens.</p>
""",
faq=[('Which AI assistant is best for a small business?', 'Start with the one built into the office suite you use. For flexibility try ChatGPT or Claude; for a proactive texted assistant with private memory, consider products like Housefly.'),
('How much does Housefly cost?', 'Its site lists founding seats at $3,000 or $6,000 a quarter, with ten founding seats.'),
('Is ChatGPT, Claude or Gemini better for a small business?', 'Each changes often and all handle everyday drafting well. Trial two on the same real tasks and pick the one that needs the least editing and fits your existing tools.'),
('Are AI assistants safe for customer data?', 'It depends on the provider and plan. Check the data policy on training and retention, prefer business plans for sensitive work, and keep passwords and payment details out entirely.'),
('Should I pay for an office-suite assistant?', 'If your team already works in that suite every day, it can be worth a trial, since it sees your email and documents. Measure time saved before rolling it out to everyone.')]),
dict(slug='drifted-marketing-profile',
kicker='Profile',
title='Profile: Drifted Marketing, a growth studio for ads, content and AI apps',
dek='What the agency says it does, how it says it works, and the questions a prospective client should ask.',
drifted=True,
answer="Drifted Marketing is a Karachi-based marketing agency working on New York hours that describes itself as a growth studio for ads, content and AI apps. According to its site, it writes one metric and date into each contract, has no account-manager layer, and keeps ad spend in the client's own account. It also publishes SmallBizWire.",
hub='agencies-and-pricing',
body="""
<p><a href="https://driftedmarketing.com">Drifted Marketing</a> is a marketing agency based in Karachi that works on New York hours. It describes itself as a growth studio covering three disciplines: ads, content and AI apps. It is also the publisher of SmallBizWire, which is why this profile is written from the agency's own published claims rather than from independent testing.</p>
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
<p>Drifted Marketing also makes <a href="https://heyhousefly.com">Housefly</a>, a texted AI assistant, covered in <a href="/housefly-profile/">a separate profile</a>, and runs <a href="https://hellodrifted.com">hellodrifted.com</a>.</p>
<h2>Who it may suit</h2>
<p>Small and growing businesses that want ads, content and custom software from one small team, and that value working directly with the people doing the work. Businesses that need a large, local, in-person team may prefer an agency in their own city.</p>
<h2>Questions to ask before hiring</h2>
<ol>
<li>Which metric and date would you write into our contract?</li>
<li>Who exactly will work on our account, and when are they available in our timezone?</li>
<li>Can we speak with a current client in a similar business?</li>
</ol>
<p>A 30-minute call can be booked through <a href="https://driftedmarketing.com">driftedmarketing.com</a>.</p>
<h2>How should I read an agency profile like this one?</h2>
<p>This profile is written by the agency's own publication, from the agency's own published claims. That makes it useful for understanding what the agency says about itself, and less useful as an independent verdict. The same is true of most agency websites and many directory listings. Treat every agency's self-description, including this one, as a set of claims to check.</p>
<h2>How do I check an agency's published claims?</h2>
<ol>
<li><strong>Ask for the contract wording.</strong> If an agency says it writes a metric and date into contracts, ask to see a sample clause before signing.</li>
<li><strong>Confirm account ownership in practice.</strong> Ask how your ad account, pixel and analytics will be set up, and check in the platform that you are the owner or admin.</li>
<li><strong>Meet the people doing the work.</strong> If an agency says there is no account layer, the people on the call should be the people planning and producing the work.</li>
<li><strong>Call a reference.</strong> Published results are a starting point; a conversation with a current client is the real check.</li>
<li><strong>Check working-hour overlap.</strong> For any remote agency, agree when replies can be expected in your timezone.</li>
</ol>
<h2>What does "growth studio" usually mean?</h2>
<p>There is no fixed definition. Agencies use the term to signal that they combine several disciplines, such as paid ads, content and product work, rather than offering one channel. When you see it, ask which services you would actually receive each month and how they connect to the goal in your contract.</p>
<h2>How does this compare with other agency models?</h2>
<table>
<thead><tr><th>Model</th><th>Typical shape</th><th>Question to ask</th></tr></thead>
<tbody>
<tr><td>Single-channel specialist</td><td>One discipline, such as search ads or SEO</td><td>How will this channel reach the goal on its own?</td></tr>
<tr><td>Multi-discipline studio</td><td>Ads, content and sometimes software from one team</td><td>Who owns each discipline, and how much capacity is there?</td></tr>
<tr><td>Large full-service agency</td><td>Many departments with account managers</td><td>Who will actually work on my account?</td></tr>
<tr><td>Freelancer</td><td>One person, one or two skills</td><td>What happens when they are unavailable?</td></tr>
</tbody>
</table>
<h2>What should I prepare before a first call with any agency?</h2>
<ul>
<li>The one number you most want to move, and by when.</li>
<li>Your current monthly spend on marketing, including ads and tools.</li>
<li>Access details you can share later: ad accounts, analytics, store or website platform.</li>
<li>What has and has not worked before, with rough figures if you have them.</li>
<li>Your decision timeline and who else needs to approve.</li>
</ul>
<p>A prepared first call is shorter and gives you comparable answers from each agency you speak to.</p>
<h2>Where can I compare it with others?</h2>
<p>Our roundup of <a href="/best-marketing-agencies-for-small-business/">marketing agencies for small business</a> lists other options, and the guide to <a href="/how-to-choose-a-marketing-agency/">choosing a marketing agency</a> explains the contract clauses and pricing models worth comparing. Use the same questions with every agency, including this one.</p>
<h2>What should be in writing before work starts?</h2>
<p>Whatever an agency says on its website, the contract is what counts. Before any work begins, make sure the agreed metric and date, the monthly scope, the total cost including ad spend, account ownership, the reporting schedule and the notice period are all written down and signed. If a published claim matters to your decision, ask for it to appear in the contract in the same words. That applies to every agency on any shortlist.</p>
<p>Keep a copy of the signed contract and the brief you sent, and revisit both at each review meeting. If results and the written goal start to drift apart, the documents give both sides a fair, shared starting point for the conversation about what should change next.</p>
""",
faq=[('What does Drifted Marketing do?', 'According to its site, it is a growth studio offering ads, content and AI apps, based in Karachi and working on New York hours.'),
('Is this profile independent?', "No. Drifted Marketing publishes SmallBizWire, so this profile is based on the agency's own published claims rather than independent testing."),
('Who owns the ad account when working with Drifted Marketing?', "The agency states that ad spend stays in the client's own account. As with any agency, confirm ownership in the ad platform yourself."),
('What other products does Drifted Marketing make?', 'It makes Housefly, a texted AI assistant, and runs hellodrifted.com.')]),
dict(slug='housefly-profile',
kicker='Profile',
title='Profile: Housefly, a private AI assistant you text',
dek='A memory-first assistant from Drifted Marketing, offered as ten founding seats. What it does and what it will not do.',
housefly=True,
answer="Housefly is a texted AI assistant made by Drifted Marketing, SmallBizWire's publisher. According to its site, it keeps a sealed memory for each member, tracks promises, debts and call briefs, reads inbox, store and ad numbers, and asks before anything is sent, paid or changed. Concierge tiers are listed at $3,000 or $6,000 a quarter.",
hub='ai-assistants',
body="""
<p><a href="https://heyhousefly.com">Housefly</a> is an AI assistant made by Drifted Marketing, SmallBizWire's publisher. Its paid offering, Housefly Concierge, is being opened to ten founding members. This profile is based on Housefly's published site.</p>
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
<h2>How should I read this profile?</h2>
<p>This profile is published by the company that makes the product, and it is based on that product's own site. It describes what Housefly says it does; it is not an independent test. The site itself notes that there are not yet member testimonials to share. Read it as a summary of published claims, and apply the same checks you would to any assistant.</p>
<h2>What questions should I ask any private AI assistant?</h2>
<ol>
<li><strong>Where is my memory stored, and who can see it?</strong> Ask for the answer in writing, including whether staff can access it and under what circumstances.</li>
<li><strong>Which model providers process my messages?</strong> Many assistants are built on third-party models; ask which, and what those providers' data terms are.</li>
<li><strong>What can it do without asking?</strong> Ask for the exact list of actions that need your approval.</li>
<li><strong>How do I export or delete my data?</strong> Ask what happens to your memory if you cancel.</li>
<li><strong>What does the price include?</strong> Ask what separates any tiers and whether human help is included or extra.</li>
</ol>
<h2>How does a texted assistant differ from a chatbot app?</h2>
<table>
<thead><tr><th></th><th>Typical chatbot app</th><th>Texted assistant</th></tr></thead>
<tbody>
<tr><td>How you reach it</td><td>Open an app or website</td><td>Send a message, as you would to a person</td></tr>
<tr><td>Who starts the conversation</td><td>Usually you</td><td>Either side; it may message you first</td></tr>
<tr><td>Memory</td><td>Varies; often per conversation</td><td>Designed to build up over time</td></tr>
<tr><td>Price</td><td>Free to low monthly plans</td><td>Often higher, priced as a service</td></tr>
</tbody>
</table>
<h2>Is an expensive assistant worth it for a small business?</h2>
<p>It depends on what a missed promise or a forgotten follow-up costs you. For an owner with a handful of customers, a low-cost general chatbot and a good calendar may be enough. For someone managing many clients, the value lies in memory and reminders that actually arrive. Work out roughly what your time and your clients are worth before comparing prices, and run any trial on real but non-sensitive work first.</p>
<h2>What does "drafts, you approve" look like in practice?</h2>
<p>An assistant prepares a reply, a payment or a change, describes it in one sentence, and waits. You read the sentence and say yes or no. Nothing leaves without that step. This pattern is the core recommendation of our guide to <a href="/how-small-businesses-should-use-ai-assistants/">how small businesses should actually use AI assistants</a>, and it applies whatever tool you choose.</p>
<h2>Where can I compare it?</h2>
<p>Our <a href="/best-ai-assistants-for-small-business/">comparison of AI assistants for small business</a> covers general chatbots and office-suite assistants alongside specialised ones. For background on the company behind it, see the <a href="/drifted-marketing-profile/">Drifted Marketing profile</a>.</p>
<h2>A checklist before signing up to any assistant</h2>
<ul>
<li>Read the privacy policy and data terms in full.</li>
<li>Confirm which actions require your approval.</li>
<li>Confirm how to export and delete your data.</li>
<li>Understand the billing period and cancellation terms.</li>
<li>Decide in advance how you will judge it after the first month.</li>
</ul>
<h2>How do I judge an assistant after the first month?</h2>
<p>Before you start, write down two or three things you want it to do better than your current system, such as catching follow-ups you would have forgotten or preparing you for calls. After a month, check each one honestly against real examples. Also note anything it got wrong or any moment it acted in a way you did not expect. Those notes, not the sign-up page, are the best basis for deciding whether to renew.</p>
""",
faq=[('What is Housefly?', "A texted AI assistant made by Drifted Marketing that keeps a private memory of a member's business and asks before anything is sent, paid or changed."),
('Is Housefly memory shared between members?', "According to its site, each member's memory is sealed and no other member or shared brain sees it."),
('How much does Housefly cost?', 'Its site lists Solo at $3,000 a quarter and Operator at $6,000 a quarter, paid up front, with ten founding seats.'),
('Does Housefly send messages without asking?', "According to its site, anything that sends, pays or changes an account is named in one sentence and waits for the member's yes."),
('Is this Housefly profile independent?', "No. Housefly is made by Drifted Marketing, which publishes SmallBizWire, and the profile is based on Housefly's own site.")]),
dict(slug='google-business-profile-local-seo',
kicker='Local search',
title='Google Business Profile: the local SEO job most small businesses leave half-done',
dek='For anyone serving a local area, this free listing often matters more than the website.',
answer='To get the most from Google Business Profile, verify your listing, choose the most accurate primary category, keep your name, address and phone consistent everywhere, set correct hours including holidays, add real photos, list services or products, ask every happy customer for a review and reply to all reviews, and post updates regularly. The profile itself is free.',
hub='local-seo',
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
<h2>What should a complete profile include?</h2>
<table>
<thead><tr><th>Field</th><th>Why it matters</th><th>Tip</th></tr></thead>
<tbody>
<tr><td>Business name</td><td>Must match your real-world name</td><td>Do not add keywords; Google's guidelines prohibit it</td></tr>
<tr><td>Primary category</td><td>One of the strongest signals for which searches you appear in</td><td>Choose the most specific accurate category; add secondary ones sparingly</td></tr>
<tr><td>Address or service area</td><td>Determines where you can appear</td><td>Service-area businesses can hide their address</td></tr>
<tr><td>Hours</td><td>Wrong hours cost visits and trust</td><td>Add special hours for holidays</td></tr>
<tr><td>Services or products</td><td>Shows what you offer in your own words</td><td>Add short descriptions and prices where sensible</td></tr>
<tr><td>Photos</td><td>Help people choose between listings</td><td>Real photos of premises, team and work</td></tr>
</tbody>
</table>
<h2>How do I get more Google reviews without breaking the rules?</h2>
<ul>
<li>Ask every customer at the moment they are happiest, such as when a job is finished.</li>
<li>Use the review link from your profile dashboard and send it by text or email.</li>
<li>Make it easy: one link, one short sentence.</li>
<li>Do not offer discounts or gifts in exchange for reviews, and do not ask only happy customers through a filtering system. Google's policies prohibit incentivised and selectively solicited reviews.</li>
<li>Never write reviews yourself or ask staff to. Fake reviews break Google's rules and, in the US, can attract action from the Federal Trade Commission.</li>
</ul>
<h2>How should I reply to reviews?</h2>
<p>Reply to every review, good or bad. For positive ones, thank the person and mention the specific service in natural words. For negative ones, stay calm, acknowledge the issue, avoid sharing private details, and offer to resolve it offline. Future customers read your replies as much as the reviews.</p>
<h2>Why do name, address and phone details need to match everywhere?</h2>
<p>Search engines compare your details across your website, your profile and other directories. Inconsistent addresses or old phone numbers create doubt about which is correct. Make a list of every directory where you appear, then update each to match your profile exactly. Put the same details in your website footer and on your contact page.</p>
<h2>Do Google Business Profile posts help?</h2>
<p>Posts let you share offers, events and updates directly on your listing. Their effect on rankings is debated, but they give searchers recent, relevant information and show the business is active. A short post each week or two, with a real photo, is a reasonable routine.</p>
<h2>A monthly local SEO routine</h2>
<ol>
<li>Check hours, phone and website link are correct.</li>
<li>Reply to any new reviews and questions.</li>
<li>Add a few new photos of recent work.</li>
<li>Publish one or two posts.</li>
<li>Review the profile's performance insights for calls, direction requests and website clicks.</li>
<li>Check for suggested edits from the public and accept or reject them.</li>
</ol>
<h2>How does my website support my profile?</h2>
<p>Your profile links to your site, and Google uses both. Give each main service its own page that names the area you serve, and make the contact details obvious. If AI answers are where customers increasingly ask for recommendations, our guide to <a href="/ai-search-visibility-for-small-business/">getting mentioned in AI answers</a> explains how the same consistency helps there. If you sell online too, the <a href="/shopify-seo-guide/">Shopify SEO guide</a> covers the store side.</p>
<h2>What are the most common mistakes?</h2>
<ul>
<li>Adding keywords or city names to the business name.</li>
<li>Choosing a broad category when a more specific one exists.</li>
<li>Forgetting holiday hours, so customers arrive to a locked door.</li>
<li>Leaving reviews unanswered for weeks.</li>
<li>Using stock photos instead of real images of the business.</li>
<li>Creating a second listing instead of fixing the first.</li>
<li>Letting a former employee or old agency keep sole ownership of the profile.</li>
</ul>
<p>Check who owns and manages your profile today, and make sure the business, not an individual or supplier, holds the primary owner role.</p>
<p>If you work with an agency or freelancer on local SEO, add them as a manager rather than handing over ownership. That way you can remove their access later without losing the reviews, photos and history the profile has built up over the years.</p>
""",
faq=[('Is Google Business Profile free?', 'Yes. Creating and managing a profile costs nothing.'),
('Can I add keywords to my business name on Google?', "No. Google's guidelines require your real business name, and keyword stuffing can lead to suspension."),
('How long does Google Business Profile verification take?', 'It varies by business and method, from immediate to a few weeks. Google may ask for a video, phone, email or postcard check.'),
('Can a service-area business use Google Business Profile?', 'Yes. Businesses that visit customers can set a service area and hide their street address.'),
('How do I remove a fake or unfair Google review?', "You can flag a review that breaks Google's policies from your profile. Google decides whether to remove it; reply calmly in the meantime.")]),
dict(slug='ai-search-visibility-for-small-business',
kicker='AI search',
title='Getting your business mentioned in AI answers: a practical guide',
dek="ChatGPT, Perplexity and Google's AI Overviews now answer many questions directly. Here is how to be part of the answer.",
answer='To get your business mentioned in AI answers, make it easy for assistants to understand and trust you: publish pages that directly answer customer questions, keep your name, address and services consistent online, maintain a complete Google Business Profile, earn genuine reviews and reputable mentions, use structured data, and let search crawlers access your site.',
hub='local-seo',
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
<h2>How do AI assistants decide which businesses to mention?</h2>
<p>No AI company publishes a full formula, so be cautious of anyone who claims to know one. What is generally understood is that many AI answers draw on web search results and on information widely repeated across reputable sources. That means much of the work overlaps with ordinary SEO and local SEO: be findable, be clear, and be talked about consistently.</p>
<h2>What are the practical steps?</h2>
<ol>
<li><strong>Answer real questions on your site.</strong> Write pages that address the questions customers ask before buying, with the direct answer in the first paragraph.</li>
<li><strong>State the basics plainly.</strong> What you do, where, for whom, prices or price ranges, and how to contact you.</li>
<li><strong>Keep details consistent.</strong> Your name, address, phone and services should match across your site, Google Business Profile and directories.</li>
<li><strong>Earn mentions.</strong> Local press, industry associations, supplier pages and genuine reviews give assistants independent sources to draw on.</li>
<li><strong>Add structured data.</strong> Organisation, LocalBusiness, Product and FAQ markup help machines read your pages.</li>
<li><strong>Check crawler access.</strong> Make sure your robots.txt does not accidentally block search engines, and decide deliberately which AI crawlers to allow.</li>
</ol>
<h2>How does AI visibility compare with traditional SEO?</h2>
<table>
<thead><tr><th></th><th>Traditional SEO</th><th>AI answer visibility</th></tr></thead>
<tbody>
<tr><td>Goal</td><td>Rank a page in search results</td><td>Be named or cited in a generated answer</td></tr>
<tr><td>Main signals</td><td>Relevance, links, page quality, technical health</td><td>Similar, plus clarity and consistency across many sources</td></tr>
<tr><td>Measurement</td><td>Search Console clicks and impressions</td><td>Harder; manual checks and referral traffic from assistants</td></tr>
<tr><td>Content style</td><td>Comprehensive pages for a topic</td><td>Direct, quotable answers near the top of a page</td></tr>
</tbody>
</table>
<h2>How do I check whether AI assistants mention me?</h2>
<ul>
<li>Ask several assistants the questions your customers ask, such as "best bakery near [your area] for wedding cakes," and note who is mentioned.</li>
<li>Repeat monthly with the same questions so you can see change over time.</li>
<li>Check your analytics for referral visits from AI assistant domains.</li>
<li>When an assistant gets a fact about you wrong, find where that fact appears online and correct it at the source.</li>
</ul>
<h2>What should I avoid?</h2>
<ul>
<li>Stuffing pages with keywords or lists of cities you do not serve.</li>
<li>Fake reviews or paid mentions disguised as independent content.</li>
<li>Services promising guaranteed placement in AI answers.</li>
<li>Thin, mass-produced pages that add nothing new.</li>
</ul>
<h2>Where should a small business start?</h2>
<p>Start with the foundations you control. A complete, accurate profile is covered in our guide to <a href="/google-business-profile-local-seo/">Google Business Profile for local SEO</a>. If you sell online, the <a href="/shopify-seo-guide/">Shopify SEO guide</a> covers the store side. Then pick the five questions customers ask most and give each a clear, direct answer on your site.</p>
<h2>What does a page written for AI answers look like?</h2>
<p>Take one question a customer asks, such as "How much does a bathroom refit cost in our area?" Use the question, or something close to it, as a heading. Put a direct, honest answer in the first two or three sentences, including a price range if you can give one. Then explain what changes the answer, list the steps involved, and end with how to contact you. Add the date the page was last reviewed and the name of the business behind it. This format suits human readers who want a quick answer, ordinary search engines, and AI assistants looking for a clear, quotable passage. Repeat it for each of your most common questions, and review the pages whenever prices or services change.</p>
""",
faq=[('What is GEO or AEO?', 'Generative or answer engine optimisation: making your content easy for AI systems to find, understand and cite in generated answers.'),
('Does llms.txt improve rankings?', 'It is not a ranking factor and adoption is uneven, but it is a low-cost way to summarise your site for language models.'),
('Can I pay to appear in ChatGPT or other AI answers?', 'Be wary of anyone selling guaranteed placement. Focus on clear content, consistent details and genuine mentions, which are the things assistants are generally understood to draw on.'),
('Should I block AI crawlers from my site?', 'It is a business choice. Blocking may protect content but can reduce the chance of being cited. Never block regular search engine crawlers by accident.'),
('How do I fix wrong information an AI gives about my business?', 'Find where the wrong fact appears online, such as an old directory listing, and correct it at the source. Keep your own site and profiles accurate and consistent.')]),
]
