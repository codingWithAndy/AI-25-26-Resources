---
marp: true
theme: gaia
class: |
    - invert

math: mathjax
size: 16:9
footer: "Session 4: S1 Workshop"
paginate: true
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

---

<!-- _class: lead -->
![bg](../assets/session4.jpg)

<div style="width: 55%; position: absolute;
    right: 75px; top: 150px">

# CPU5006-20: 
## Artificial Intelligence

### Session 4: S1 Workshop

</div>


<!-- _footer: "![]()" -->

---

## Course Overview

Week | Session | |
-----|------|---|
4 | S1 Assessment Workshop |
5 | Supervised Learning |
RW | Reading Week |
6 | Unsupervised Learning |  S1
7 | Artificial Neural Networks |  
8 | Convolutional NN & Computer Vision |
9 | S2 Assessment Workshop |
10 | Recurrent NN & NLP | S2
WB | Winter Break |
11 | Generative AI | 
12 | Building AI Agents |

---

## Overview

- How to write a Results and Discussion Section
- How to write a Conclusion
- Dedicated Assessment S1 time/Gain verbal feedback

---

## Writing a Results

- Responds to the question "What have you found?" 
- Hence, only representative results from your research should be presented. 
- The results should be essential for discussion.

---

## Writing a Discssion

<span style="font-size: 0.8em;">

- Here you must respond to what the results mean. Probably it is the easiest section to write, but the hardest section to get right. 
- This is because it is the most important section of your article. 
- Here you get the chance to sell your data's findings.
- You need to make the Discussion corresponding to the Results, but do not reiterate the results. 
- Never ignore work in disagreement with yours, in turn, you must confront it and convince the reader that you are correct or better.
</span>

---

## Writing a Conclusion

<span style="font-size:0.8em">

- Shows how the work advances the field from the present state of knowledge. 
- Without a clear conclusion section, reviewers and readers will find it difficult to judge your work and whether it merits publication.
- A common error in this section is repeating the abstract, or just listing experimental results. 
- Trivial statements of your results are unacceptable in this section.
</span>

---

<!-- _class: summary -->

## S1: Reminders

- Due: $X^{th}$ November 2026 - 11:59am
- Max 3,000 words 

---

## S1 Dedicated Time

- Use this time to progress further in your S1 assignment and ask any questions.
- Additionally, use this time to gain **verbal feedback** on your work.

---

<!-- _class: summary -->

## Next Session

- Supervised Learning
- Regression Methods
- Classification Methods
