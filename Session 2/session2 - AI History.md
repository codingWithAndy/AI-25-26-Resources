---
marp: true
theme: gaia
class: |
    - invert

math: mathjax
size: 16:9

style: |
    /* @theme ai-fun-level5 */

    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Share+Tech+Mono&display=swap');

    :root {
    font-family: 'Roboto', sans-serif;
    color: #f2f7ff;

    /* AI colour palette */
    --bg-dark: #0b1020;
    --bg-mid: #11182e;
    --grid: rgba(0, 224, 255, 0.08);
    --dot: rgba(255, 0, 212, 0.10);
    --text-main: #f2f7ff;
    --text-soft: #c9d4e8;
    --highlight: #00e0ff;
    --highlight-2: #ff00d4;
    --highlight-3: #8aff00;
    --panel: rgba(255, 255, 255, 0.08);
    --panel-strong: rgba(255, 255, 255, 0.12);
    --ai-accent: linear-gradient(90deg, #00e0ff, #7a5cff, #ff00d4);

    background:
        linear-gradient(90deg, var(--grid) 1px, transparent 1px),
        linear-gradient(180deg, var(--grid) 1px, transparent 1px),
        radial-gradient(circle, var(--dot) 1px, transparent 1px),
        radial-gradient(circle at top left, #16213f 0%, var(--bg-dark) 55%, #05070d 100%);
    background-size:
        60px 60px,
        60px 60px,
        28px 28px,
        cover;
    background-position:
        0 0,
        0 0,
        14px 14px,
        center;
    }

    /* Base slide styling */
    section {
    padding: 55px 70px;
    font-size: 30px;
    line-height: 1.35;
    color: var(--text-main);
    position: relative;
    }

    /* Decorative glow strip */
    section::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 8px;
    width: 100%;
    background: var(--ai-accent);
    box-shadow: 0 0 18px rgba(0, 224, 255, 0.45);
    }

    /* Optional subtle badge */
    section::after {
    content: "AI • Level 5";
    position: absolute;
    top: 18px;
    right: 28px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.45em;
    letter-spacing: 0.08em;
    color: rgba(255,255,255,0.55);
    border: 1px solid rgba(255,255,255,0.18);
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.04);
    }

    /* Headings */
    h1, h2, h3 {
    font-family: 'Share Tech Mono', monospace;
    margin-top: 0;
    margin-bottom: 0.45em;
    line-height: 1.1;
    }

    h1 {
    font-size: 1.95em;
    background: var(--ai-accent);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow:
        0 0 12px rgba(0, 224, 255, 0.35),
        0 0 22px rgba(255, 0, 212, 0.18);
    }

    h2 {
    font-size: 1.45em;
    color: #8defff;
    text-shadow: 0 0 10px rgba(0, 224, 255, 0.2);
    }

    h3 {
    font-size: 1.1em;
    color: #ffd6fb;
    }

    /* Lead slides */
    section.lead {
    text-align: center;
    justify-content: center;
    background:
        radial-gradient(circle at centre, rgba(0,224,255,0.08) 0%, rgba(0,0,0,0) 45%),
        radial-gradient(circle at 30% 20%, rgba(255,0,212,0.14) 0%, rgba(0,0,0,0) 30%),
        linear-gradient(135deg, #11182e 0%, #05070d 100%);
    }

    section.lead h1,
    section.lead h2,
    section.lead h3 {
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
    color: white;
    text-shadow: 0 2px 18px rgba(0, 0, 0, 0.7);
    }

    section.lead::after {
    content: "Artificial Intelligence";
    top: auto;
    bottom: 24px;
    right: 24px;
    }

    /* Paragraphs */
    p, li {
    color: var(--text-soft);
    }

    /* Strong text */
    strong {
    color: #ffffff;
    background: linear-gradient(90deg, rgba(0,224,255,0.22), rgba(255,0,212,0.16));
    padding: 0.04em 0.2em;
    border-radius: 6px;
    }

    /* Lists */
    ul, ol {
    font-size: 1em;
    line-height: 1.5;
    padding-left: 1.1em;
    }

    ul li::marker,
    ol li::marker {
    color: var(--highlight);
    font-weight: 700;
    }

    /* Blockquotes / callouts */
    blockquote {
    border-left: 6px solid var(--highlight);
    background: rgba(255,255,255,0.06);
    padding: 18px 22px;
    border-radius: 14px;
    color: #ffffff;
    }

    /* Code */
    code {
    font-family: 'Share Tech Mono', monospace;
    background: rgba(255, 255, 255, 0.08);
    color: #8defff;
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-size: 0.9em;
    }

    pre {
    font-family: 'Share Tech Mono', monospace;
    background: rgba(10, 15, 28, 0.95);
    color: #8defff;
    border: 1px solid rgba(0, 224, 255, 0.25);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
    }

    /* Tables */
    table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.75em;
    background: rgba(255,255,255,0.05);
    border-radius: 14px;
    overflow: hidden;
    }

    th {
    background: linear-gradient(90deg, rgba(0,224,255,0.85), rgba(122,92,255,0.85));
    color: #08101f;
    padding: 12px;
    text-align: left;
    }

    td {
    padding: 12px;
    border-top: 1px solid rgba(255,255,255,0.08);
    }

    tr:nth-child(even) td {
    background: rgba(255,255,255,0.03);
    }

    /* Links */
    a {
    color: #8defff;
    text-decoration: none;
    border-bottom: 1px solid rgba(141,239,255,0.4);
    }

    /* Horizontal rule */
    hr {
    border: none;
    height: 2px;
    background: var(--ai-accent);
    opacity: 0.45;
    margin: 24px 0;
    }

    /* Small highlight box */
    .note {
    background: rgba(138, 255, 0, 0.12);
    border-left: 6px solid var(--highlight-3);
    padding: 16px 20px;
    border-radius: 14px;
    }

    /* Image placement helpers */
    img {
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.35);
    }

    img[alt~="right-centre"] {
    position: absolute;
    bottom: 140px;
    right: 70px;
    width: 350px;
    }

    img[alt~="right-centre-pip"] {
    position: absolute;
    bottom: 145px;
    right: 75px;
    width: 320px;
    }

    img[alt~="right-side"] {
    position: absolute;
    top: 170px;
    right: 10px;
    width: 470px;
    }

    img[alt~="bottom-left"] {
    position: absolute;
    bottom: 40px;
    left: 75px;
    width: 220px;
    }

    img[alt~="bottom-centre"] {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    }

    img[alt~="bottom-right"] {
    position: absolute;
    bottom: 40px;
    right: 75px;
    width: 240px;
    }

    img[alt~="right-centre-lib"] {
    position: absolute;
    bottom: 60px;
    right: 90px;
    width: 520px;
    }

    /* Two-column utility */
    .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    }

    /* Panel/card utility */
    .panel {
    background: var(--panel);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.22);
    }

    /* Task slides */
    section.task {
    background:
        linear-gradient(135deg, rgba(255,140,0,0.18), rgba(255,0,90,0.18)),
        radial-gradient(circle at top right, rgba(255,255,255,0.08), transparent 30%),
        linear-gradient(135deg, #2b0f0f 0%, #140707 100%);
    color: #fff4e8;
    border: 4px solid #ff8c00;
    }

    section.task::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 10px;
    width: 100%;
    background: linear-gradient(90deg, #ffcc00, #ff8c00, #ff2d55);
    box-shadow: 0 0 22px rgba(255, 140, 0, 0.6);
    }

    section.task::after {
    content: "TASK";
    position: absolute;
    top: 18px;
    right: 24px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8em;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #1a0a00;
    background: linear-gradient(90deg, #ffcc00, #ff8c00);
    padding: 8px 16px;
    border-radius: 999px;
    box-shadow: 0 0 18px rgba(255, 140, 0, 0.45);
    }

    section.task h1,
    section.task h2,
    section.task h3 {
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
    color: #ffd6a5;
    text-shadow: 0 0 16px rgba(255, 140, 0, 0.35);
    }

    section.task h1 {
    font-size: 2.1em;
    }

    section.task p,
    section.task li {
    color: #fff4e8;
    font-size: 1.02em;
    }

    section.task strong {
    color: #1a0a00;
    background: linear-gradient(90deg, #ffcc00, #ff8c00);
    padding: 0.08em 0.28em;
    border-radius: 6px;
    }

    section.task code {
    background: rgba(255,255,255,0.1);
    color: #ffd6a5;
    border: 1px solid rgba(255,255,255,0.12);
    }

    section.task ul li::marker,
    section.task ol li::marker {
    color: #ffcc00;
    }

    /* Summary / Key Points slides */
    section.summary {
    background:
        linear-gradient(135deg, rgba(0,255,180,0.12), rgba(0,200,255,0.12)),
        radial-gradient(circle at bottom left, rgba(0,255,200,0.15), transparent 35%),
        linear-gradient(135deg, #061a1a 0%, #020909 100%);
    color: #eafffb;
    border: 3px solid rgba(0,255,200,0.5);
    }

    /* Top glow bar */
    section.summary::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 8px;
    width: 100%;
    background: linear-gradient(90deg, #00ffc8, #00e0ff);
    box-shadow: 0 0 20px rgba(0,255,200,0.6);
    }

    /* Label badge */
    section.summary::after {
    content: "KEY POINTS";
    position: absolute;
    top: 18px;
    right: 24px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75em;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #002a26;
    background: linear-gradient(90deg, #00ffc8, #00e0ff);
    padding: 6px 14px;
    border-radius: 999px;
    box-shadow: 0 0 14px rgba(0,255,200,0.4);
    }

    /* Headings */
    section.summary h1,
    section.summary h2,
    section.summary h3 {
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
    color: #b6fff3;
    text-shadow: 0 0 12px rgba(0,255,200,0.25);
    }

    section.summary h1 {
    font-size: 2em;
    }

    /* Text */
    section.summary p,
    section.summary li {
    color: #eafffb;
    font-size: 1.05em;
    }

    /* Strong emphasis */
    section.summary strong {
    color: #002a26;
    background: linear-gradient(90deg, #00ffc8, #00e0ff);
    padding: 0.08em 0.3em;
    border-radius: 6px;
    }

    /* List markers */
    section.summary ul li::marker,
    section.summary ol li::marker {
    color: #00ffc8;
    }

    /* Optional boxed recap items */
    section.summary .panel {
    background: rgba(0,255,200,0.08);
    border: 1px solid rgba(0,255,200,0.25);
    border-radius: 16px;
    }

    /* Optional "remember this" callout */
    section.summary .highlight {
    background: rgba(0,255,200,0.12);
    border-left: 6px solid #00ffc8;
    padding: 16px 20px;
    border-radius: 12px;
    color: #ffffff;
    }



footer: "Session 2: What is AI? History, paradigms, and literature review"
paginate: true

---

<!-- _class: lead -->

![bg](../assets/session2.jpg)

# CPU5006-20: Artificial Intelligence
## Session 2: What is AI?
#### History, paradigms, and literature review

<!-- _footer: "![]()" -->

---

## Learning Outcomes

By the end of this session, you should be able to:

- explain key stages in the history of AI
- distinguish between major AI paradigms
- describe what a literature review does in a scientific report
- begin shaping a research question for S1
- identify relevant sources for rule-based AI research

---

## Course Overview

Week | Session | |
-----|------|----|
2 | History of AI & conducting a literature review |
3 | Rule-Based AI Systems |
4 | S1 Assessment Workshop |
5 | Supervised Learning |
RW | Reading Week |
6 | Unsupervised Learning | S1
7 | Artificial Neural Networks |
8 | Convolutional NN & Computer Vision |
9 | Recurrent NN & NLP |
10 | S2 Assessment Workshop |
11 | Generative AI | S2
12 | Building AI Agents |

---

## Session Overview

<span style="font-size: 0.7em">

### Part 1 — What is AI?
- history of AI
- key paradigms
- why definitions matter

### Part 2 — How do we study AI?
- literature reviews
- critical reading
- finding research gaps

### Part 3 — Your S1 assignment
- topic ideas
- datasets
- getting started in Overleaf

</span>

---

## Starter Activity: Is this AI? 
<!-- (5 mins) -->

<span style="font-size: 0.8em">

In pairs, decide whether each example is:

- definitely AI
- maybe AI
- probably not AI

Examples:
- a calculator
- a rule-based chatbot
- a spam filter
- ChatGPT
- Netflix recommendations

Be ready to justify **why**.

</span>

<!-- 
1. Calculator
👉 Probably not AI
- Follows fixed rules (arithmetic operations)
- No learning, no adaptation
- Same input → same output every time
💡 Good teaching point:
- Not all “smart” software is AI

2. Rule-based chatbot
👉 Maybe AI (or weak AI)
Uses predefined rules (if user says X → respond Y)
No learning or generalisation
Historically considered AI (symbolic AI)
💡 Link to next session:
This is exactly what you’ll build in Session 3

3. Spam filter
👉 Definitely AI (modern view)
Typically uses machine learning
Learns patterns from data
Improves over time
⚠️ Caveat:
Early spam filters were rule-based → could be “maybe AI”
💡 Good discussion point:
Same task, different approaches → different “AI-ness”

4. ChatGPT
👉 Definitely AI
Uses large language models
Learns from massive datasets
Generates new content (not just rules)
💡 Extension:
This is generative AI — a key modern paradigm

5. Netflix recommendations
👉 Definitely AI
Uses machine learning/recommender systems
Learns user preferences
Predicts behaviour
💡 Link: This connects to supervised/unsupervised learning later
 -->

---

<!-- _class: lead -->

## Part 1: What is AI?

![bg](../assets/image-69.png)

<!-- _footer: "![]()" -->

---

## Why study the history of AI?

- it shows that AI is **not one single thing**
- different approaches have become popular at different times
- ideas from the past still influence systems today
- understanding this helps you evaluate AI critically

---

## Early Beginnings

- the idea of artificial beings is much older than computers
- stories of mechanical or intelligent artefacts appear in ancient cultures
- modern AI emerges when computing, logic, and mathematics come together in the 20th century

---

![bg](../assets/ai-birth.png)

<!-- _footer: "![]()" -->

---

## Birth of AI (1956)

- the term **Artificial Intelligence** was popularised by John McCarthy in 1956
- the Dartmouth workshop is often seen as the formal starting point of AI as a field
- early optimism led to substantial funding and bold predictions

<!-- 
In 1956, the field of Artificial Intelligence was officially born at a conference at Dartmouth College. Here, John McCarthy coined the term 'Artificial Intelligence,' marking a pivotal moment in the development of the field. This event sparked early optimism, with researchers believing that, within a few decades, we would have machines capable of human-level intelligence. As a result, there was a significant influx of funding and research during this time, as people hoped AI would revolutionise the world in a short span of time.
 -->

---

## Early Optimism

- researchers believed human-like intelligence might be achieved quickly
- early systems showed promise in logic and problem solving
- expectations rose faster than the technology could support

---

![bg](../assets/image-71.png)

<!-- _footer: "![]()" -->

---

## AI Winter (1974–1980)

- progress was slower than expected
- computing power and data were limited
- confidence and funding dropped

### Key lesson:
AI progress is shaped by both ideas **and** practical constraints.

<!-- 
However, AI's early promise didn’t pan out as quickly as expected. Progress was much slower than anticipated, and the limitations of early computers became apparent. By the mid-1970s, disillusionment set in. Funding for AI research dried up, and the field entered what is now known as the 'AI Winter.' During this period, both public and scientific interest in AI waned, as many concluded that true artificial intelligence was far more challenging than they had initially thought.
 -->


---

![bg](../assets/ai-spring.png)

<!-- _footer: "![]()" -->

---

## AI Spring (1980–1987)

- expert systems revived interest in AI
- commercial applications increased
- organisations saw value in narrow, domain-specific intelligence

<!-- 
But the story of AI didn’t end with the AI Winter. The 1980s brought a new wave of interest in artificial intelligence, often referred to as the 'AI Spring.' This resurgence was driven by the rise of expert systems—software that could emulate the decision-making abilities of a human expert in specific fields. Coupled with advances in computing power, this period saw a renewed optimism, and investments in AI research once again began to flow, reinvigorating the field.
 -->

---

![bg](../assets/moderan_ai.png)

<!-- _footer: "![]()" -->

---

## Modern AI (21st Century)

- machine learning and deep learning transformed the field
- better hardware, larger datasets, and improved algorithms accelerated progress
- AI now appears in search, vision, speech, recommendation, and generative tools

<!-- 
Fast forward to the 21st century, and we are now in the midst of a major AI boom. Advances in machine learning, particularly deep learning, have led to breakthroughs that were previously unimaginable. AI is no longer just a research field; it has become an integral part of our daily lives, from personal assistants like Siri and Alexa to recommendation algorithms on platforms like Netflix and YouTube. The rapid pace of innovation in AI has transformed industries across the board, from healthcare to transportation, and its growth shows no sign of slowing.
 -->

---


![bg](../assets/ai-future.png)

<!-- _footer: "![]()" -->

---

## Future of AI

- The future of AI holds much promise and uncertainty.
- Ethical considerations are becoming increasingly important.

<!-- 
Looking ahead, the future of AI holds immense potential but also significant challenges. As AI continues to evolve, it will unlock new possibilities in fields such as autonomous vehicles, personalised medicine, and even creative industries like art and music. However, along with these advancements come critical ethical questions—how do we ensure AI systems are fair, transparent, and accountable? How can we prevent AI from being misused? As we move forward, addressing these ethical considerations will be crucial in shaping the future of AI for the benefit of all.

Also Provide final overview:

- The history of AI is a fascinating journey of ups and downs.
- As we look to the future, it's important to learn from the past.
 -->


---


## Paradigms of AI

| Paradigm | Core idea | Example |
|---|---|---|
| Symbolic AI | rules, logic, knowledge representation | expert systems |
| Statistical / Machine Learning | patterns learned from data | classifiers, regressors |
| Deep / Generative AI | layered representations and generation | image models, LLMs |

---

## Why paradigms matter

<span style="font-size: 0.7em">

Two AI systems can solve the **same problem** in very different ways.



Example:
- a **rule-based** system may use explicit `IF-THEN` rules
- a **machine learning** system may learn patterns from examples

This matters for:
- accuracy
- explainability
- data requirements
- ethics
- implementation choices

</span>

---

<!-- _class: task -->

## Task: Sort the examples 
<!-- (8 mins) -->

<span style="font-size: 0.6em">

Classify each example as mainly:

- **symbolic AI**
- **machine learning**
- **deep / generative AI**

Examples:
- medical expert system
- handwritten digit classifier
- ChatGPT
- chess program using fixed rules
- fraud detector trained on historical transactions

### Stretch:
Which of these are easiest to explain to a user?

</span>

<!-- 
Symbolic AI = AI that thinks using rules and logic instead of learning from data

Symbolic AI systems use:
Symbols → represent things (e.g. "fever", "high_income")
Rules → define relationships

Key characteristics
✅ Human-readable rules
✅ Transparent decisions (you can explain why)
❌ No learning from data
❌ Hard to scale for complex problems
 -->

---

## Why this matters for your assignment

<span style="font-size: 0.9em">

For S1 you will investigate **rule-based AI**.

That means you are working mainly within the **symbolic AI** tradition.

Your report should show that you understand:

- where rule-based systems fit in the history of AI
- what their strengths are
- what their limitations are
- how they compare with other approaches

</span>

---

<!-- _class: summary -->

## Quick Reflection

Complete this sentence:

> Rule-based AI is useful when...

Then complete this one:

> Rule-based AI may struggle when...

Share one idea with the class.

<!--
Rule-based AI is useful when…
If students struggle, give hints:
- when problems are well-defined
- when there are clear rules
- when decisions need to be transparent/explainable
- when the environment is stable (doesn’t change much)

Examples:
- loan approval rules
- basic chatbots
- safety systems

Rule-based AI may struggle when…
Guide them toward:
- complex or messy data
- uncertainty or ambiguity
- problems requiring learning from data
- situations with too many rules to manage

Examples:
- image recognition
- natural language understanding
- unpredictable environments
-->

---

## S1 Assessment Overview

<span style="font-size: 0.8em">

You will:

- design and implement a rule-based AI system
- test it on a chosen dataset
- evaluate how well it works
- write up the work as a scientific paper

### Deliverables
- a scientific paper
- code implementation

</span>

---

<!-- _class: summary -->

## Report Structure for S1

- Introduction
- Literature Review
- Methodology
- Results and Discussion
- Conclusion
- References

---

## Marking Criteria

- Introduction and Literature Review (25%)
- Methodology (25%)
- Results and Discussion (25%)
- Conclusion (15%)
- Report Depth and Presentation (10%)*

<span class="small">

*This weighting affects the overall score if presentation quality is below the required standard.

</span>

---

## Available Datasets

- **Car Evaluation Dataset** — classification using structured attributes
- **Credit Risk Dataset** — decision making / classification
- **Adult Dataset** — income category prediction
- **Food Dataset** — rule-based classification or recommendation style tasks

---

## Example Research Directions

- compare two rule-based approaches on the same dataset
- investigate the interpretability of a rule-based system
- explore the trade-off between simplicity and accuracy
- test how rule design affects classification performance

---

## Task 2: Build a research question (10 mins)

<span style="font-size: 0.75em">

Choose **one dataset** and draft:

1. your dataset
2. the problem you want to solve
3. one possible research question

### Example starter:
> "How accurately can a rule-based system classify ... ?"

</span>

<span style="font-size: 0.6em">

### Stretch:
Write a second question that focuses on **interpretability**, not just accuracy.

</span>

---

<!-- _class: lead -->

## Part 2: How do we study AI?

![bg](../assets/image-70.png)

---

## What is a literature review?

A literature review is not just a list of papers.

It should:

- explain what is already known
- compare different approaches or findings
- identify strengths, weaknesses, and debates
- show the gap your own work will address

---

## Literature Review in THIS Module

For this assignment, your literature review should help answer:

- What are rule-based AI systems?
- Where are they effective?
- What are their limitations?
- How have researchers evaluated them?
- What gap or angle will my project explore?

---

## Step 1: Define your scope

Be specific.

Instead of:
> "I will review AI in finance."

Try:
> "I will review research on rule-based methods for credit risk classification."

A good scope is:
- focused
- relevant to your dataset
- linked to your research question

---

## Task 3: Narrow the topic (5 mins)

Turn each broad topic into a better literature review scope:

- AI in healthcare
- AI in finance
- AI in education

### Stretch:
Convert one of your improved scopes into a draft research title.

---

## Step 2: Search for relevant sources

<span style="font-size: 0.7em">

Useful databases:
- IEEE Xplore
- ACM Digital Library
- Google Scholar
- your university library databases

Example search strings:
- `"rule-based system" AND "credit risk"`
- `"expert system" AND classification`
- `"decision rules" AND interpretability`

</span>

---

## Task 4: Search string builder (8 mins)



Using your chosen dataset, write:

- **two keyword searches**
- **one Boolean search** using AND / OR
- **one alternative search** using a synonym

### Stretch:
Which search is likely to return the most focused results? Why?

---

## Step 3: Summarise and synthesise

<div style="display: flex; gap: 40px;">

<div style="width: 50%;">

<span style="font-size: 0.7em">

### ❌ Do not write:

- Paper 1 says...
- Paper 2 says...
- Paper 3 says...

### ✅ Instead, group sources by:

- theme  
- method  
- dataset  
- findings  
- limitations  

</span>

</div>

<div style="width: 50%;">

<span style="font-size: 0.7em">

<br>
<br>
<br>
<br>
<br>

### Example themes

- accuracy of rule-based systems  
- interpretability and transparency  
- comparison with machine learning models  

</span>

</div>

</div>

---

## Step 4: Critically evaluate

Ask questions like:

- What did the authors do well?
- What evidence supports their claims?
- What are the limitations?
- Is the method suitable for real-world use?
- Can the results be compared fairly with other studies?

---

## Task 5: Quick critical reading (10 mins)

<span style="font-size: 0.7em">

Read the paper called `research_paper.pdf`:

- the research aim
- the method used
- one strength
- one limitation
- one sentence you could use in a literature review

### Stretch:
How does this source help justify your own project?

</span>

---

## Step 5: Identify gaps and opportunities

A good literature review leads to a gap.

Examples:
- limited comparison of rule-based methods on this dataset
- strong focus on accuracy, but not explainability
- few studies using simple rules for transparent decision making

Your project should respond to a gap, not repeat old work without purpose.

---

## Mini Writing Frame

A suggested writing structure:

1. introduce the theme  
2. compare what studies found  
3. evaluate strengths / weaknesses  
4. identify a gap  
5. link to your project  

---

## Task 6: Draft a synthesis paragraph (10 mins)

Write 4–6 sentences that:

- introduce a theme linked to your topic
- compare at least two ideas or sources
- identify one limitation or gap

### Stretch:
Add a final sentence that links the gap directly to your S1 study.

---

## Writing a Scientific Paper

- **Introduction** — what problem are you studying and why?
- **Literature Review** — what is already known?
- **Methodology** — what did you do?
- **Results and Discussion** — what happened and what does it mean?
- **Conclusion** — what can be taken from the study?
- **References** — what sources did you use?

---

## Part 3: Getting Started with Tools

- use **Overleaf** to structure and write your report
- use a reference manager or `.bib` file to store citations
- keep notes on papers as you read them
- record full reference details from the start

---

## LaTeX

![bg 50% 50%](../assets/image.png)

---

## LaTeX and Overleaf

- LaTeX is widely used for scientific and technical writing
- Overleaf provides an online editor with templates and collaboration features
- it is well suited to reports with references, figures, tables, and equations

---

## Useful Starting Templates

- Harvard style template
- Two-column scientific paper template

### Tip:
Pick **one** template early and keep the structure consistent.

---

## Getting `.bib` References

![bg](../assets/gscholar.png)

<!-- _footer: "![]()" -->

---

![bg](../assets/gscholar_paper_select.png)

<!-- _footer: "![]()" -->

---

![bg](../assets/gscholar_cite_select.png)

<!-- _footer: "![]()" -->

---

![](../assets/gscholar_cite_collect.png)

<!-- _footer: "![]()" -->

---

## Task

<span style="font-size: 0.8em">

Before next week, make a start on all four:

- read the S1 brief carefully
- choose a dataset
- draft a research question
- find at least **3 relevant academic sources**

### Stretch:
Set up your Overleaf document and add your first references.

</span>

---

## Key Takeaways

- AI has evolved through multiple waves and paradigms
- rule-based AI sits within the symbolic tradition
- literature reviews compare, evaluate, and identify gaps
- your S1 report should connect theory, implementation, and evaluation

---

## Next Session

- Rule-Based AI Systems
- Introduction to Methodology
- Designing rules from data
