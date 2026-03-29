# Level 5 AI Module – AI Agents Worksheet

**Student Name:** ___________________________  
**Date:** _______________

---

## 1. Core Concepts (Short Answer)

### a. What is an AI agent?  
### b. What are the three core components of an agent?  
### c. Explain the difference between a reactive agent and a model-based agent.  
### d. What is a policy, and why is it important?  

---

## 2. Sense–Think–Act Cycle

A warehouse robot moves boxes from shelves to packing stations.

- Sensors (Sense):  
- Decision process (Think):  
- Actions (Act):  

---

## 3. Types of Agents

Match the descriptions:

| Description | Agent Type |
|------------|------------|
| Spotify-style recommender | |
| Robot turning on bump | |
| Navigation system | |
| Learns from feedback | |
| Self-driving car with map | |

---

## 4. Smart Campus Agent

### a. What is the environment?  
### b. List sensors:  
1.  
2.  
3.  
### c. List actuators:  
1.  
2.  
3.  
### d. Suitable agent types and why:  

---

## 5. Design Your Own Agent

- Agent Name  
- Environment  
- Sensors  
- Actuators  
- Goals  
- Challenges  

---

## 6. Coding Challenges

### Challenge 1: Reactive Agent

```python
def reactive_vacuum(dirt, obstacle):
    # Your code here
    pass
```

### Challenge 2: Model-Based Agent

```python
class ModelBasedVacuum:
    def __init__(self):
        self.visited = set()

    def step(self, location, dirt):
        # TODO
        pass
```

### Challenge 3: Goal-Based Search

```python
def find_path(grid, start, goal):
    pass
```

### Challenge 4: Utility-Based Decision Making

```python
actions = {
    "study": 0.9,
    "sleep": 0.5,
    "play_games": 0.3,
    "exercise": 0.8
}

def choose_best_action(actions):
    # TODO: implement selection
    pass

print("Available actions and utilities:")
for action, utility in actions.items():
    print(f"{action}: {utility}")

print("\nBest action chosen by the agent:")
print(choose_best_action(actions))
```

### Challenge 5: Learning Agent

```python
def q_update(Q, state, action, reward, next_state, alpha=0.1, gamma=0.9):
    pass
```

---

## 7. Stretch Task  
Explain how your agent could be improved using advanced AI concepts.

---

## 8. Ethical Question  
Explain one ethical concern with AI agents and how it can be reduced.
