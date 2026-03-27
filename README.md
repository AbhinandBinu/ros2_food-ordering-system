

## 📌 Overview

This repo deals with the implementation of a food delivering system using ROS2 services , where I explored the transition from **Services to Actions**.

The goal of this phase is to understand how ROS 2 handles **long-running tasks** using Actions and how they differ from Services.

---

## 🧠 What I Learned

### 🔹 ROS 2 Service
- Synchronous communication
- Client sends request → waits → receives response
- Suitable for quick operations

### 🔹 ROS 2 Action
- Asynchronous communication
- Supports:
  - Goal
  - Feedback
  - Result
- Ideal for long-running tasks

---

## ⚡ Key Difference

| Feature | Service | Action |
|--------|--------|--------|
| Execution | Blocking | Non-blocking |
| Feedback | ❌ No | ✅ Yes |
| Cancellation | ❌ No | ✅ Yes |
| Use Case | Simple tasks | Long tasks |

---

## 🍽 Example Concept (Food Ordering System)

### Service Version
