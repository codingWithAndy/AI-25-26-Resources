---
marp: true
theme: gaia
class: |
    - invert

math: mathjax
size: 16:9

style: |
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Share+Tech+Mono&display=swap');

    :root {
        font-family: 'Roboto', sans-serif;
        color: #e0e0e0;
        background: 
            /* circuit-like lines */
            linear-gradient(90deg, rgba(0,255,200,0.05) 1px, transparent 1px),
            linear-gradient(180deg, rgba(0,255,200,0.05) 1px, transparent 1px),
            /* faint dotted "vias" */
            radial-gradient(circle, rgba(0,255,200,0.07) 1px, transparent 1px),
            /* base gradient */
            radial-gradient(circle at 30% 30%, #1a1a1a 0%, #000000 100%);
        background-size: 
            60px 60px, 60px 60px, 30px 30px, cover;
        background-position: 
            0 0, 0 0, 15px 15px, center;
        --ai-accent: linear-gradient(90deg, #00e0ff, #ff00d4);
    }

    /* Headings */
    h1, h2, h3 {
        font-family: 'Share Tech Mono', monospace;
        background: var(--ai-accent);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 15px rgba(0, 224, 255, 0.5), 
                     0 0 25px rgba(255, 0, 212, 0.3);
    }

    h1 {
        font-size: 2em;
        margin-bottom: 0.5em;
    }

    h2 {
        font-size: 1.5em;
    }

    h3 {
        font-size: 1.2em;
        color: #66ffff;
    }

    /* Override for lead slides */
    section.lead h1,
    section.lead h2,
    section.lead h3 {
        background: none;
        -webkit-background-clip: initial;
        -webkit-text-fill-color: initial;
        color: white;
        text-shadow: black 1px 2px 10px
    }

    /* Lists */
    ul, ol {
        font-size: 1.1em;
        line-height: 1.6em;
    }

    /* Code blocks */
    code, pre {
        font-family: 'Share Tech Mono', monospace;
        background: rgba(255, 255, 255, 0.05);
        padding: 0.3em 0.6em;
        border-radius: 6px;
        color: #00e0ff;
    }

    /* Slide content spacing */
    section {
        padding: 60px;
    }

    table {
 
    width: 100%;
    font-size: 20px;
    }
    th {
        color: black;
        background-color: #857c7cff;
    }


footer: "Session 2: History of AI & How to write a Literature Review"
paginate: true

---

<!-- _class: lead -->

![bg](../assets/session2.jpg)

# CPU5006-20: Artificial Intelligence
## Session 2: History of AI 
## & How to write a Literature Review

<!-- _footer: "![]()" -->

---

## Course Overview

Week | Session | |
-----|------|----|
2 | The history of AI & Conducting Liturature Review |
3 | Rule-Based AI Systems |
4 | S1 Assessment Workshop |
5 | Supervised Learning |
RW | Reading Week |
6 | Unsupervised Learning |  S1
7 | Artificial Neural Networks |  
8 | Convolutional NN & Computer Vision |
9 | Recurrent NN & NLP |
10 | S2 Assessment Workshop |
11 | Generative AI | S2
12 | Building AI Agents |

---

## Overview

- Histroy of AI
- S1 Introduction
- How to Write a Liturature Review

---

<!-- _class: lead -->

## History of AI

![bg](../assets/image-69.png)

---

## Early Beginnings

- The concept of artificial beings dates back to ancient times.
- In the 20th century, we see the birth of the field of AI research.

<!-- 
The concept of artificial beings dates back to ancient civilisations. From Greek myths about automatons to medieval alchemists who dreamed of creating life, humanity has long been fascinated by the idea of intelligent machines. But it wasn’t until the 20th century that we see the birth of what we now call Artificial Intelligence. This was a time when the rapid development of computers sparked ideas about machines that could actually think, learn, and reason, much like a human brain. And so, the journey of AI research began.
 -->

---

![bg](../assets/ai-birth.png)

---

## Birth of AI (1956)

- The term "Artificial Intelligence" was first coined by John McCarthy in 1956.
- Early optimism for the field led to significant funding and research.

<!-- 
In 1956, the field of Artificial Intelligence was officially born at a conference at Dartmouth College. Here, John McCarthy coined the term 'Artificial Intelligence,' marking a pivotal moment in the development of the field. This event sparked early optimism, with researchers believing that, within a few decades, we would have machines capable of human-level intelligence. As a result, there was a significant influx of funding and research during this time, as people hoped AI would revolutionise the world in a short span of time.
 -->

---

![bg](../assets/image-71.png)

---

## AI Winter (1974 - 1980)

- A period of disappointment in AI 
- Progress led to reduced funding and interest

<!-- 
However, AI's early promise didn’t pan out as quickly as expected. Progress was much slower than anticipated, and the limitations of early computers became apparent. By the mid-1970s, disillusionment set in. Funding for AI research dried up, and the field entered what is now known as the 'AI Winter.' During this period, both public and scientific interest in AI waned, as many concluded that true artificial intelligence was far more challenging than they had initially thought.
 -->


---

![bg](../assets/ai-spring.png)

---

## AI Spring (1980 - 1987)

- Renewed optimism and advancements 
- Led to what is known as the "AI Spring"

<!-- 
But the story of AI didn’t end with the AI Winter. The 1980s brought a new wave of interest in artificial intelligence, often referred to as the 'AI Spring.' This resurgence was driven by the rise of expert systems—software that could emulate the decision-making abilities of a human expert in specific fields. Coupled with advances in computing power, this period saw a renewed optimism, and investments in AI research once again began to flow, reinvigorating the field.
 -->

---

![bg](../assets/moderan_ai.png)

---

## Modern AI (21st Century)

- Significant advancements in machine learning and other technologies have led to the current boom in AI.

<!-- 
Fast forward to the 21st century, and we are now in the midst of a major AI boom. Advances in machine learning, particularly deep learning, have led to breakthroughs that were previously unimaginable. AI is no longer just a research field; it has become an integral part of our daily lives, from personal assistants like Siri and Alexa to recommendation algorithms on platforms like Netflix and YouTube. The rapid pace of innovation in AI has transformed industries across the board, from healthcare to transportation, and its growth shows no sign of slowing.
 -->

---

![bg](../assets/ai-future.png)

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

## S1 Introduction

- Max word count of 3000 words
- A scientific paper & code implementation
- Generative AI can be used for  all aspects of the assignment (code and report).
<!-- - Video explaining code implementation -->

--- 

## S1 Report Contents

- Introduction
- Liturature Review
- Methodology
- Results & Discussion
- Conclusion
- References

---

## Marking Criteria

- Introduction and Lit Review (25%)
- Methodology (25%)
- Results and Discussion (25%)
- Conclusion (15%)
- Report Depth and Presentation (10%) *

<span style="font-size:0.6em">
* This will apply a weighting effect to your overall score if $<70$ .

</span>

---

## Assesment S1 Requirements

Your task is to write a scientific paper on a research experiment regarding rule-based (RB) AI algorithm(s) you have created.

You are to create a research question that you are trying to solve by using the RB AI systems, with one of the provided datasets. You have the freedom to decide on what your research question should be, as long as it is related to the required dataset that has been chosen. 

---

## Datasets

- Car Evaluation Dataset
- Credit Risk Dataset
- Adult Dataset
- Food Dataset

---

## Assignment Example Topics

- Create two RB AI systems and see which one has the better accuracy
- Investigating the interprability of the RB AI systems decision making
- Using two diiferent RB approaches to determine which approach has performed better based on chosen metrics

---

![bg](../assets/image-70.png)

---

## Writing a Scientific Paper

- Introduction
- Liturature Review
- Methodology
- Results
- Discssion
- Conclusion
- References

---

## Writing a Introduction

- Setting the scene of your study
- What did you do? 
- Why did you do it?
- A summary of what you found

---

## Writing a Liturature Review

- Purpose is to gain an understanding of the existing research and debates relevant to a particular topic or area of study, and to present that knowledge in the form of a written report. 
- Conducting a literature review helps you build your knowledge in your field.

---

## Writing a Liturature Review

1. Define your scope

Example: “I will review research on machine learning algorithms for real-time fraud detection in financial transactions.”

---

## Writing a Liturature Review

2. Search for relevant sources 

Use IEEE Xplore, ACM Digital Library, Google Scholar.

Example search terms: ``"edge computing" AND "IoT security"``, ``"neural networks" AND "image classification"``.

---

## Writing a Liturature Review

3. Summarise and synthesise

Don’t just list papers — group them by theme, method, or findings.
Example:
Theme 1: Accuracy improvements in convolutional neural networks (CNNs) for medical imaging.
Theme 2: Trade-offs between model complexity and inference speed in embedded systems.

---

## Writing a Liturature Review

4. Critically evaluate

Highlight strengths, weaknesses, and limitations.
Example: “While Smith et al. (2022) achieved 98% accuracy, their model required GPU acceleration, limiting deployment on mobile devices.”

---

## Writing a Liturature Review

5. Identify gaps and opportunities

Example: “Few studies address the energy consumption of blockchain consensus algorithms in IoT networks — an area ripe for exploration.”

---

## Writing a Liturature Review

Example excerpt:

Recent studies on federated learning (Kairouz et al., 2021; Li et al., 2022) emphasise privacy-preserving model training across distributed devices. While these approaches reduce data transfer, they often suffer from communication bottlenecks. Emerging work on compression techniques (Zhu et al., 2023) shows promise in mitigating this, but empirical evaluations in low-bandwidth rural networks remain scarce.

---

## Writing a Liturature Review

Tips for Computing Students

<span style="font-size: 0.8em">

- Use diagrams or tables to compare algorithms, architectures, or datasets.
- Keep technical terms precise — define acronyms on first use.
- Balance breadth (covering the field) with depth (analysing the most relevant work).
- Always link your review back to your research question or project aim.
</span>

---

## LaTeX

![bg 50% 50%](../assets/image.png)

---

## LaTeX

- LaTeX is a high-quality typesetting system
    - it includes features designed for the production of technical and scientific documentation. 
- LaTeX is the de facto standard for the communication and publication of scientific documents.

---

## Overleaf

![bg 50% 50%](https://images.ctfassets.net/nrgyaltdicpt/5doLOtX69is0i6WIiY4um/6cc9be15c75155e7b93cd4823b742e44/overleaf_wide_colour_green_bg.png)

---

## Overleaf

- templates
    - [Harvard]()
    - [Two-Column Template]()

---

## Getting .bib References

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

- Read S1 Brief
- Select a Topic
- Research into the Topic
- Starting writing report using Overleaf

---

## Next Session

- Rule-Based AI Systems
- How to write a methodology

