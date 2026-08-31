# Queue

What is a **queue**?
A queue is a _linear data structure_ which models a real world queue by having two primary operations, namely **enqueue** and **dequeue**.

![Queue Structure](https://media.geeksforgeeks.org/wp-content/uploads/20250827110558739481/Dequeue-Operation-in-Queue-1.webp)

## Operations on a Queue

1. **Enqueue** - this refers to **adding a new element at the back** of the queue. (also known as _adding_ or _offering_.)

2. **Dequeue** - this refers to **removing an element from the front** of the queue. (also known as _removing_ or _polling_.)

## When and where is a queue used?

- Any **waiting line models** a queue, for example a lineup at a movie theatre.

- Can be used to efficiently keep track of the **_x_ most recently added elements**.

- Web server request management where you want **first come first serve**.

- **Breadth First Search (BFS)** graph traversal.

## Complexity Analysis

```
+----------+------+
| Enqueue  | O(1) |
+----------+------+
| Dequeue  | O(1) |
+----------+------+
| Peeking  | O(1) |
+----------+------+
| Contains | O(n) |
+----------+------+
| Removal  | O(n) |
+----------+------+
| Is Empty | O(1) |
+----------+------+
```
