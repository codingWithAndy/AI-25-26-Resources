---
marp: true
theme: gaia
class: |
    - invert

math: mathjax
size: 16:9
footer: "Session 12: AI Agents"
paginate: true
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
        text-shadow: darkgreen 5px 2px 10px
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
    height: 15%;
    width: 100%;
    font-size: 20px;
    }
    th {
        color: black;
        background-color: #857c7cff;
    }
    img[alt~="km"] {
        position: absolute;
        bottom: 0px;
        right: 300px;
    }


---

<!-- _class: lead -->

![bg](../assets/agents.png)



# CPU5006-20: Artificial Intelligence
## Session 12: AI Agents

------------------------------------------------------------------------

## Course Overview

Week | Session | |
-----|------|---|
12 | Building AI Agents |

---

# **What Is an AI Agent?**

- An **AI agent** is a system that can **sense** its environment and **act** within it.
- It tries to **achieve goals** by choosing good actions.
- It can learn, plan, make decisions, or follow rules.

**In short:**  
➡️ *An agent is something that does things for you, intelligently.*

---

# **Key Parts of an AI Agent**

<span style="font-size: 0.8em">

- **Environment**  
  The world the agent is working in (real or digital).

- **Sensors**  
  How the agent gets information (e.g., camera, text input, logs).

- **Actions/Actuators**  
  What the agent can do (e.g., move, send messages, make changes).

- **Policy**  
  The strategy for deciding what action to take.

</span>

---

# **Examples of AI Agents**

- A chess-playing program deciding the best move.  
- A self-driving car sensing the road and steering.  
- A home assistant responding to voice commands.  
- A chatbot that plans a long conversation or task.  
- A game character controlled by AI.

---

# **Types of Agents**

<div style="display: flex; gap: 40px; font-size: 0.65em;">

<div style="flex: 1;">

### **1. Reactive Agents**
- Respond instantly to the environment  
- No memory of the past  
- *Example:* a robot that avoids obstacles  

### **2. Model-Based Agents**
- Keep track of the world  
- Use memory to make better decisions  



</div>

<div style="flex: 1;">

### **3. Goal-Based Agents**
- Choose actions to reach a specific goal  
- *Example:* GPS navigation  

### **4. Utility-Based Agents**
- Try to **maximise usefulness**  
- *Example:* recommendation systems  

### **5. Learning Agents**
- Improve over time through experience  
- *Example:* reinforcement learning agents  

</div>

</div>


---

# **How AI Agents Work**

Most agents follow this loop:

<span style="font-size:0.8em">

1. **Observe** the environment  
2. **Think** about what the observation means  
3. **Choose an action**  
4. **Act**  
5. **Learn** from the result (optional)

This is known as the **Sense–Think–Act** cycle.

</span>

---

# **Modern AI Agents (LLM Agents)**

Today’s agents often use **large language models (LLMs)** like GPT:

<span style="font-size:0.6em">

- They can read, write, plan, and reason using text.
- They can break tasks into steps.
- They can call tools (e.g., search the web, run code).
- They can work autonomously for long tasks.

These are sometimes called:

- **Autonomous agents**  
- **AI assistants**  
- **Task-based agents**  
- **Multi-agent systems** (when many agents work together)

</span>

---

# **What Can AI Agents Do?**

<span style="font-size:0.8em">

- Plan itineraries or projects  
- Analyse data  
- Write and revise code  
- Search for information  
- Simulate teams (e.g., marketing, design, research)  
- Automate workflows

Agents can save time and reduce repetitive work.

</span>

---

# **Limitations of AI Agents**

- They may make mistakes or “hallucinate”.  
- They need clear goals.  
- They can get stuck without feedback.  
- Safety controls are important to avoid harmful actions.  
- They often need human guidance for important decisions.

---

# **Why AI Agents Matter**

<div style="display: flex; gap: 40px; font-size:0.7em;">

<div style="flex: 1;">

AI agents allow computers to:
- Work **independently**  
- Make **adaptable** decisions  
- Help with **complex, multi-step tasks**  
- Reduce manual effort  
- Provide **personalised** support  

</div>

<div style="flex: 1;">

They are becoming central in:
- Education  
- Healthcare  
- Business automation  
- Robotics  
- Research  
- Creative industries  

</div>

</div>


---

# Demo

---

# Task

Complete the ai_agents_worksheet.md that is uploaded to Ultra.

---

# **Summary**

- AI agents **sense**, **decide**, and **act**.  
- They can be simple or very advanced.  
- Modern agents often use **LLMs** to reason and plan.  
- They support automation, problem-solving, and creativity.  
- They still require **oversight** and good design.

---

# **Thank You!**  

I hope you have enjoyed the content covered in this AI module to introduce you into the concepts of AI.

I would greatly appreciate your End of Module Feedback.

Have a great Winter Break!
