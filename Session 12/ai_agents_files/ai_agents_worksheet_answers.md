# Level 5 AI Module – AI Agents Worksheet  
## Answer Sheet

---

## 1. Core Concepts

a. An AI agent senses its environment, makes decisions, and takes actions.  
b. Sensors, actuators, and a policy/decision mechanism.  
c. Reactive: uses only current input; Model-based: uses memory.  
d. A policy maps percepts to actions; it defines behaviour.

---

## 2. Sense–Think–Act

- Sensors: camera, barcode reader, proximity sensor  
- Think: plan route, avoid obstacles  
- Act: move, lift, transport boxes  

---

## 3. Types of Agents

| Description | Agent Type |
|------------|------------|
| Spotify-style recommender | Utility-Based |
| Robot turning on bump | Reactive |
| Navigation system | Goal-Based |
| Learns from feedback | Learning |
| Self-driving car with map | Model-Based |

---

## 4. Smart Campus Agent

Environment: campus + digital systems  
Sensors: timetable API, Wi-Fi location, student queries  
Actuators: notifications, text output, route suggestions  
Suitable agent types: model-based + goal-based + utility-based  

---

## 5. Example Agent

CampusGuide: helps students navigate and study efficiently.

---

## 6. Coding Challenge Answers

### Challenge 1

```python
def reactive_vacuum(dirt, obstacle):
    if dirt:
        return "CLEAN"
    if obstacle:
        return "TURN_RIGHT"
    return "MOVE_FORWARD"
```

### Challenge 2

```python
class ModelBasedVacuum:
    def __init__(self):
        self.visited = set()

    def step(self, location, dirt):
        self.visited.add(location)
        if dirt:
            return "CLEAN"
        if location in self.visited:
            return "CHOOSE_NEW_DIRECTION"
        return "MOVE_FORWARD"
```

### Challenge 3

```python
from collections import deque

def find_path(grid, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
```

### Challenge 4

```python
def choose_best_action(actions):
    return max(actions, key=actions.get)
```

### Challenge 5

```python
def q_update(Q, state, action, reward, next_state, alpha=0.1, gamma=0.9):
    max_next = max(Q[next_state].values())
    old = Q[state][action]
    Q[state][action] = old + alpha * (reward + gamma * max_next - old)
    return Q
```

---

## 7. Stretch  
Use RL, multi-agent systems, or world models.

---

## 8. Ethics  
Bias, privacy issues, lack of transparency.
