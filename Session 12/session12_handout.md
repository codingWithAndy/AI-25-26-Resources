# 🧠 Demo: Building a Simple AI Agent in Python

This example shows how to build a very simple **AI agent** using the classic  
**Sense → Think → Act** model.

The agent lives in a 10x10 grid and tries to reach a goal position.

---

## 1. Creating the Agent

We start by defining a class:

- The **position** of the agent  
- The **goal**  
- The three functions an AI agent needs:

### ✔ sense()  
Look at the world.

### ✔ think()  
Pick an action based on a simple policy.

### ✔ act()  
Update the agent’s state.

---

## 2. Sense Step

The agent compares its coordinates to the goal coordinates:

```python
def sense(self):
    px, py = self.position
    gx, gy = self.goal

    return {
        "goal_left": gx < px,
        "goal_right": gx > px,
        "goal_up": gy < py,
        "goal_down": gy > py
    }

```

This produces a perception dictionary like:

``` python
{"goal_right": True, "goal_down": True, ...}
```

----

## 3. Think Step (Policy)
The agent decides what to do next.

```python
def think(self, perception):
    if perception["goal_right"]:
        return "MOVE_RIGHT"
    if perception["goal_left"]:
        return "MOVE_LEFT"
    if perception["goal_up"]:
        return "MOVE_UP"
    if perception["goal_down"]:
        return "MOVE_DOWN"
    return "STAY"
```
This is a simple rule-based policy.

---

4. Act Step
The agent updates its position:

```python
def act(self, action):
    x, y = self.position

    if action == "MOVE_RIGHT":
        self.position = (x + 1, y)
    elif action == "MOVE_LEFT":
        self.position = (x - 1, y)
    elif action == "MOVE_UP":
        self.position = (x, y - 1)
    elif action == "MOVE_DOWN":
        self.position = (x, y + 1)
```

---

## 5. Running the Agent

The agent repeatedly:
1. Senses
2. Thinks
3. Acts

Until it reaches the goal.

---

## 6. Visualising the Grid

- A simple grid display prints:
- A for the agent
- G for the goal
- . for empty cells

---

## 7. Suggested Extensions

Students can try:
Adding obstacles
Adding random movement
Using utility-based action scoring
Turning it into a reinforcement learning task
Making multiple agents interact