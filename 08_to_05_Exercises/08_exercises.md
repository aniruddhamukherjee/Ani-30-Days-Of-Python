<div align="center">
  <h1>30 Days Of Python: Days 05–08 Exercises</h1>
  <p><strong>Mastery Challenges covering Lists, Tuples, Sets, and Dictionaries</strong></p>
</div>

---

## 📌 Overview

These exercises are designed to push beyond elementary syntax into algorithmic problem solving, memory semantics, and composite data structure design using concepts introduced in **Days 05 through 08**:
- **Day 05 (Lists):** In-place mutations vs. new list allocations, multi-dimensional list matrices, two-pointer techniques, sorting strategies with custom keys, shallow vs. deep copy semantics, and sliding windows.
- **Day 06 (Tuples):** Immutability guarantees, hashable composite keys, structural unpacking, tuple packing, coordinate systems, and immutable state representation.
- **Day 07 (Sets):** Mathematical set theory (unions, intersections, differences, symmetric differences), fast $O(1)$ membership testing, set algebra pipelines, deduplication without ordering guarantees, and hashability prerequisites.
- **Day 08 (Dictionaries):** Hash table lookups, deep nested structure traversal, schema validation, grouping and inversion, key collisions, dictionary views (`keys`, `values`, `items`), and building multi-index catalogs without external libraries.

---

## 📋 Table of Contents

- [Section 1: Advanced List Surgery & Algorithmic Manipulation (Day 05)](#-section-1-advanced-list-surgery--algorithmic-manipulation-day-05)
  - [Challenge 1: Dutch National Flag & In-Place Partitioning](#challenge-1-dutch-national-flag--in-place-partitioning)
  - [Challenge 2: Irregular Nested List Flattener & Matrix Transposition](#challenge-2-irregular-nested-list-flattener--matrix-transposition)
  - [Challenge 3: Dynamic Sliding Window & Moving Statistics Buffer](#challenge-3-dynamic-sliding-window--moving-statistics-buffer)
- [Section 2: Tuple Packing, Immutability & Composite Keys (Day 06)](#-section-2-tuple-packing-immutability--composite-keys-day-06)
  - [Challenge 4: Immutable State Machine & Transaction Ledger](#challenge-4-immutable-state-machine--transaction-ledger)
  - [Challenge 5: Spatial Coordinate Hashing & Manhattan Geometry](#challenge-5-spatial-coordinate-hashing--manhattan-geometry)
  - [Challenge 6: The "Mutable Inside Immutable" Paradox & Hash Diagnostics](#challenge-6-the-mutable-inside-immutable-paradox--hash-diagnostics)
- [Section 3: Mathematical Set Algebra & Relational Operations (Day 07)](#-section-3-mathematical-set-algebra--relational-operations-day-07)
  - [Challenge 7: Jaccard Similarity & Profile Affinity Matcher](#challenge-7-jaccard-similarity--profile-affinity-matcher)
  - [Challenge 8: Role-Based Access Control (RBAC) & Permission Venn Engine](#challenge-8-role-based-access-control-rbac--permission-venn-engine)
  - [Challenge 9: Multi-Environment Configuration Drift Detector](#challenge-9-multi-environment-configuration-drift-detector)
- [Section 4: Dictionary Architectures, Nested Traversal & Inversion (Day 08)](#-section-4-dictionary-architectures-nested-traversal--inversion-day-08)
  - [Challenge 10: Multi-Map Inverter with Collision Resolution](#challenge-10-multi-map-inverter-with-collision-resolution)
  - [Challenge 11: Deep Nested Pathfinder, Flattener, and Unflattener](#challenge-11-deep-nested-pathfinder-flattener-and-unflattener)
  - [Challenge 12: Manual Frequency Counter & Multi-Key Secondary Index](#challenge-12-manual-frequency-counter--multi-key-secondary-index)
- [Section 5: Cross-Collection Synergy & Polyglot Structures (Days 05–08)](#-section-5-cross-collection-synergy--polyglot-structures-days-0508)
  - [Challenge 13: Social Graph Network Analyzer](#challenge-13-social-graph-network-analyzer)
  - [Challenge 14: Multi-Warehouse Inventory Allocation & Order Fulfillment](#challenge-14-multi-warehouse-inventory-allocation--order-fulfillment)
  - [Challenge 15: Inverted Search Index & Boolean Query Evaluator](#challenge-15-inverted-search-index--boolean-query-evaluator)
- [Section 6: Comprehensive Capstone Projects](#-section-6-comprehensive-capstone-projects)
  - [Challenge 16: In-Memory Relational Engine (Join, Filter, Aggregate)](#challenge-16-in-memory-relational-engine-join-filter-aggregate)
  - [Challenge 17: LRU (Least Recently Used) Cache Simulator](#challenge-17-lru-least-recently-used-cache-simulator)
- [Checklist for Completion](#-checklist-for-completion)

---

## 🧩 Section 1: Advanced List Surgery & Algorithmic Manipulation (Day 05)

### Challenge 1: Dutch National Flag & In-Place Partitioning
**Topic:** In-place modifications, two-pointer / three-pointer approach, element swapping without secondary allocation.

- **Background:**
  Given a list containing items of three distinct categories (e.g., `'red'`, `'white'`, `'blue'` or integers `0`, `1`, `2`), sort them in-place in linear time $O(n)$ with constant auxiliary space $O(1)$.
- **Requirements:**
  1. Do **not** use `list.sort()`, `sorted()`, or auxiliary list allocations (like list comprehension or extra copies).
  2. Implement a three-pointer partition algorithm:
     - `low`: boundary for the lower category (`0`).
     - `mid`: current element scanner (`1`).
     - `high`: boundary for the higher category (`2`).
  3. Swap elements in-place using Python's tuple-based simultaneous assignment: `nums[i], nums[j] = nums[j], nums[i]`.
- **Sample Input:**
  ```python
  tokens = [2, 0, 1, 2, 1, 0, 0, 2, 1, 0, 2, 1]
  ```
- **Expected Output:**
  ```python
  # tokens modified in place:
  [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
  ```
- **Edge Cases to Test:**
  - Already sorted list: `[0, 0, 1, 2, 2]`
  - Reverse sorted list: `[2, 2, 1, 0, 0]`
  - Homogeneous lists: `[1, 1, 1]`, `[0]`, `[]`

---

### Challenge 2: Irregular Nested List Flattener & Matrix Transposition
**Topic:** Nested lists, jagged/ragged lists, matrix manipulation, indexing boundary checks.

- **Problem A: Ragged Matrix Transposition**
  Given a non-square, jagged 2D list (rows have varying lengths), compute the transposed matrix. Empty cells must be filled with a configurable sentinel value (e.g., `None`).
  ```python
  ragged_matrix = [
      [1, 2, 3, 4],
      [5, 6],
      [7, 8, 9]
  ]
  # Expected Transposed Output (fill_value=None):
  [
      [1, 5, 7],
      [2, 6, 8],
      [3, None, 9],
      [4, None, None]
  ]
  ```
- **Problem B: Arbitrary Depth Flattener (Iterative or Non-Import Recursive)**
  Given a list with arbitrarily deep nesting of lists, flatten it into a single one-dimensional list without using external packages (`itertools`, `numpy`).
  ```python
  nested = [1, [2, [3, 4], 5], [[6]], 7, [8, [9, [10]]]]
  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

---

### Challenge 3: Dynamic Sliding Window & Moving Statistics Buffer
**Topic:** Slicing, `list.append()`, `list.pop()`, list arithmetic, performance trade-offs.

- **Problem:**
  Build a sliding window aggregator that processes a sequence of numerical readings (e.g., stock prices or temperature sensors).
  - Given a raw list of integers/floats and a window size $k$:
    1. Calculate the sliding window **mean**, **median**, and **range** ($\max - \min$) for each contiguous sublist of length $k$.
    2. Maintain an in-place circular ring buffer using a fixed-length list to simulate real-time stream consumption where old elements are overwritten.
- **Sample Run:**
  ```python
  readings = [10, 12, 15, 11, 9, 14, 18, 20, 16]
  k = 3
  # Window 1: [10, 12, 15] -> mean: 12.33, median: 12, range: 5
  # Window 2: [12, 15, 11] -> mean: 12.67, median: 12, range: 4
  # ...
  ```

---

## 🔒 Section 2: Tuple Packing, Immutability & Composite Keys (Day 06)

### Challenge 4: Immutable State Machine & Transaction Ledger
**Topic:** Tuples as immutable records, tuple unpacking, multi-value returns, history preservation.

- **Problem:**
  Build a financial transaction ledger where each block or entry is an immutable tuple:
  `transaction = (tx_id, sender, recipient, amount, fee)`
  1. Write a function `apply_transaction(balances, tx)` that takes an existing state (a tuple of account balance records) and a transaction tuple.
  2. Because tuples are immutable, the function must compute and return a **new tuple of updated balances** without modifying any prior tuple structures.
  3. Validate balances: if `sender` balance $< (\text{amount} + \text{fee})$, return the original state alongside an error message tuple: `(original_state, False, "INSUFFICIENT_FUNDS")`.
  4. Build an audit log as a tuple of tuples containing the cumulative history of all states.

---

### Challenge 5: Spatial Coordinate Hashing & Manhattan Geometry
**Topic:** Tuple indexing, composite keys, immutable vectors, distance calculation.

- **Problem:**
  In a 3D grid, points are represented as 3-tuples: `Point = (x, y, z)`.
  1. Define a list of 10 points in 3D space.
  2. Implement functions using pure tuples:
     - `manhattan_distance(p1, p2)`: $|x_1 - x_2| + |y_1 - y_2| + |z_1 - z_2|$
     - `euclidean_distance(p1, p2)`: $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}$
  3. Create an algorithm to find the **closest pair of points** from the list, returning a 3-tuple:
     `((p1_x, p1_y, p1_z), (p2_x, p2_y, p2_z), minimum_distance)`
  4. Find the center of mass (centroid) as a tuple of floats rounded to 2 decimal places.

---

### Challenge 6: The "Mutable Inside Immutable" Paradox & Hash Diagnostics
**Topic:** Memory addresses (`id()`), hashability (`hash()`), shallow copies, `TypeError: unhashable type`.

- **Investigation & Coding:**
  Consider the following code snippet:
  ```python
  a = (1, 2, [3, 4])
  ```
  1. What happens if you run `a[2].append(5)`? Does it raise an error? Inspect `a` and `id(a[2])`.
  2. What happens if you execute `a[2] += [6, 7]`? Explain why it both raises a `TypeError` and *still modifies* the list!
  3. Attempt to use `a` as a key in a dictionary or element in a set. Why does `hash(a)` fail?
  4. Write a sanitizing function `deep_freeze(item)`:
     - If the item is a `list`, convert it and all nested lists into `tuples`.
     - If the item is a `set`, convert it into a `frozenset`.
     - If the item is a `dict`, convert it into a tuple of sorted `(key, deep_freeze(value))` pairs.
     - Test that the output of `deep_freeze(a)` is validly hashable and can be added to a set!

---

## ⚡ Section 3: Mathematical Set Algebra & Relational Operations (Day 07)

### Challenge 7: Jaccard Similarity & Profile Affinity Matcher
**Topic:** Set operations (`intersection`, `union`, `len`), membership testing, set difference.

- **Background:**
  The Jaccard similarity coefficient measures similarity between two finite sample sets $A$ and $B$:
  $$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
- **Problem:**
  Given a collection of user skill profiles represented as sets of tags:
  ```python
  users = {
      "Alice": {"python", "sql", "git", "fastapi", "docker", "aws"},
      "Bob": {"python", "javascript", "react", "git", "css"},
      "Charlie": {"python", "sql", "docker", "kubernetes", "aws", "terraform"},
      "Diana": {"react", "javascript", "typescript", "css", "html"}
  }
  ```
  1. Compute the pairwise Jaccard similarity index between all pairs of users.
  2. For any chosen user (e.g., `"Bob"`), find which other user is most similar.
  3. Identify the **Skill Gap**: What skills does the most similar user have that `"Bob"` lacks (`set difference`)?
  4. Identify the **Exclusive Skills**: Skills possessed by only one person in the entire group.

---

### Challenge 8: Role-Based Access Control (RBAC) & Permission Venn Engine
**Topic:** `issubset`, `issuperset`, `isdisjoint`, `symmetric_difference`.

- **Scenario:**
  An enterprise system defines permissions as atomic string sets:
  ```python
  all_permissions = {
      "view_reports", "create_reports", "delete_reports",
      "manage_users", "assign_roles", "audit_logs",
      "deploy_production", "restart_servers", "billing_access"
  }

  roles = {
      "Viewer": {"view_reports"},
      "Editor": {"view_reports", "create_reports"},
      "Admin": {"view_reports", "create_reports", "delete_reports", "manage_users", "assign_roles", "audit_logs"},
      "DevOps": {"view_reports", "deploy_production", "restart_servers", "audit_logs"}
  }
  ```
- **Tasks:**
  1. Write a function `check_authorization(user_permissions, required_permissions)`:
     - Returns `True` if `required_permissions` is a subset of `user_permissions`.
  2. Detect **Conflicting Duties**: If an employee has both `"billing_access"` and `"deploy_production"`, flag a compliance violation (`intersection` check).
  3. Calculate the **Role Overlap Matrix**: For every pair of roles, find:
     - Shared permissions (`A & B`)
     - Unique permissions to each role (`A - B` and `B - A`)
     - Symmetric difference (`A ^ B`)
  4. Find the minimal combination of roles needed to cover all permissions in `all_permissions`.

---

### Challenge 9: Multi-Environment Configuration Drift Detector
**Topic:** `symmetric_difference`, `difference`, set transformations.

- **Scenario:**
  You manage configurations across three environments: `Development`, `Staging`, and `Production`. Each configuration is a set of key-value tuples: `(config_key, config_value)`.
  ```python
  env_dev = {("DEBUG", "true"), ("DATABASE_URL", "dev-db"), ("CACHE", "redis"), ("TIMEOUT", "60")}
  env_staging = {("DEBUG", "false"), ("DATABASE_URL", "stage-db"), ("CACHE", "redis"), ("TIMEOUT", "60")}
  env_prod = {("DEBUG", "false"), ("DATABASE_URL", "prod-db"), ("CACHE", "redis"), ("TIMEOUT", "30"), ("SSL", "true")}
  ```
- **Requirements:**
  1. Identify keys that exist in all three environments (universal keys).
  2. Identify variables present in `env_prod` that were never configured in `env_dev` or `env_staging`.
  3. Identify configuration drift: keys where the value changes between `env_staging` and `env_prod`.
  4. Generate a clean markdown drift report detailing missing, extra, and differing values.

---

## 📖 Section 4: Dictionary Architectures, Nested Traversal & Inversion (Day 08)

### Challenge 10: Multi-Map Inverter with Collision Resolution
**Topic:** Dictionary iteration, `.items()`, key collisions, dict-of-lists transformation.

- **Problem:**
  Given a dictionary mapping students to the courses they are enrolled in:
  ```python
  student_enrollments = {
      "Alice": ["CS101", "MATH201", "PHYS101"],
      "Bob": ["CS101", "MATH201"],
      "Charlie": ["PHYS101", "BIO101"],
      "David": ["CS101", "BIO101"],
      "Eve": ["MATH201"]
  }
  ```
  1. **Invert the Dictionary**: Create a new dictionary `course_roster` mapping each course to a sorted list of enrolled students.
  2. Implement without using `collections.defaultdict`: handle key creation dynamically using `.get()` or `in` checks.
  3. Compute Course Statistics:
     - Course with the highest enrollment.
     - Pair of courses that have the highest number of co-enrolled students.

---

### Challenge 11: Deep Nested Pathfinder, Flattener, and Unflattener
**Topic:** Nested dictionaries, key paths, recursion/iteration, dynamic key construction.

- **Task A: Deep Flattener**
  Convert a deeply nested dictionary into a flattened dictionary with dot-delimited (`.`) keys.
  ```python
  nested_config = {
      "app": {
          "server": {
              "host": "127.0.0.1",
              "port": 8080
          },
          "logging": {
              "level": "INFO",
              "handlers": {
                  "console": True,
                  "file": False
              }
          }
      },
      "database": {
          "primary": {
              "host": "db.internal",
              "credentials": {
                  "user": "root"
              }
          }
      }
  }
  ```
  *Flattened Target:*
  ```python
  {
      "app.server.host": "127.0.0.1",
      "app.server.port": 8080,
      "app.logging.level": "INFO",
      "app.logging.handlers.console": True,
      "app.logging.handlers.file": False,
      "database.primary.host": "db.internal",
      "database.primary.credentials.user": "root"
  }
  ```

- **Task B: Deep Unflattener (Reverse)**
  Write the inverse function `unflatten_dict(flat_dict)` that reconstructs the exact nested structure from dot-delimited keys.

- **Task C: Safe Keypath Getter**
  Implement `deep_get(dictionary, "app.server.port", default=None)` which safely traverses any path without throwing `KeyError` or `AttributeError`.

---

### Challenge 12: Manual Frequency Counter & Multi-Key Secondary Index
**Topic:** Dictionary frequency aggregation, secondary indexing, sorting dictionary items.

- **Problem:**
  Given a log of HTTP access requests formatted as a list of dictionaries:
  ```python
  logs = [
      {"ip": "192.168.1.1", "status": 200, "method": "GET", "endpoint": "/index"},
      {"ip": "192.168.1.2", "status": 404, "method": "GET", "endpoint": "/favicon.ico"},
      {"ip": "192.168.1.1", "status": 200, "method": "POST", "endpoint": "/login"},
      {"ip": "192.168.1.3", "status": 500, "method": "POST", "endpoint": "/api/v1/pay"},
      {"ip": "192.168.1.1", "status": 200, "method": "GET", "endpoint": "/dashboard"},
      {"ip": "192.168.1.2", "status": 200, "method": "GET", "endpoint": "/index"}
  ]
  ```
  1. Build a frequency distribution dictionary counting requests per `ip`.
  2. Build a composite secondary index mapping `(method, status)` tuple keys to lists of endpoints:
     ```python
     # Example entry:
     # ("GET", 200): ["/index", "/dashboard", "/index"]
     ```
  3. Identify the Top-N most active endpoints without using the `collections` module. Sort the dictionary entries by frequency descending using `sorted()` with a custom lambda/itemgetter key.

---

## 🌐 Section 5: Cross-Collection Synergy & Polyglot Structures (Days 05–08)

### Challenge 13: Social Graph Network Analyzer
**Topic:** Dictionaries of sets, lists of tuples, graph traversal, set intersections.

- **Data Representation:**
  Represent an undirected friendship graph as an adjacency dictionary where keys are user strings and values are sets of friends:
  ```python
  network = {
      "Alice": {"Bob", "Charlie", "David"},
      "Bob": {"Alice", "David", "Eve"},
      "Charlie": {"Alice", "David", "Frank"},
      "David": {"Alice", "Bob", "Charlie", "Grace"},
      "Eve": {"Bob", "Grace"},
      "Frank": {"Charlie", "Grace"},
      "Grace": {"David", "Eve", "Frank", "Heidi"},
      "Heidi": {"Grace"}
  }
  ```
- **Requirements:**
  1. **Mutual Friends:** Given any two users, return the set of their mutual friends.
  2. **Friend Recommendations:** For user $U$, recommend users who are *friends of friends* but not already friends with $U$, ranked by the number of mutual connections.
  3. **Degrees of Separation:** Write a breadth-first search using a list as a queue and a set for visited nodes to calculate the shortest path (as a tuple of names) between any two individuals (e.g., `"Alice"` to `"Heidi"`).
  4. **Triangles (Cliques of 3):** Find all unique 3-tuples of users `(A, B, C)` where all three are friends with each other. Ensure no duplicate permutations (i.e., `(A, B, C)` is the same as `(B, A, C)`).

---

### Challenge 14: Multi-Warehouse Inventory Allocation & Order Fulfillment
**Topic:** Nested dictionaries, list of orders, set filtering, atomic dictionary deductions.

- **Scenario:**
  An online retailer has stock spread across multiple regional warehouses:
  ```python
  warehouses = {
      "Warehouse_East": {"laptop": 12, "mouse": 45, "keyboard": 18, "monitor": 5},
      "Warehouse_West": {"laptop": 8, "mouse": 20, "keyboard": 35, "monitor": 15},
      "Warehouse_Central": {"laptop": 15, "mouse": 60, "keyboard": 0, "monitor": 8}
  }

  orders = [
      {"order_id": "ORD001", "items": {"laptop": 5, "mouse": 10}},
      {"order_id": "ORD002", "items": {"monitor": 18, "keyboard": 5}},
      {"order_id": "ORD003", "items": {"laptop": 25, "keyboard": 40}}
  ]
  ```
- **Tasks:**
  1. **Inventory Totals:** Compute total available stock across all warehouses for each product as a single dictionary.
  2. **Fulfillment Strategy:** For each order:
     - Check if total stock is sufficient. If not, mark order as `BACKORDERED` with a tuple indicating missing items and quantities.
     - If sufficient, fulfill the order using the minimum number of warehouse splits (prefer fulfilling from one warehouse; if impossible, split across warehouses).
     - Atomically update warehouse inventories when an order is successfully fulfilled.
  3. Return a detailed fulfillment ledger mapping `order_id` to the list of allocations: `[(warehouse_name, item, qty), ...]`.

---

### Challenge 15: Inverted Search Index & Boolean Query Evaluator
**Topic:** Tokenization, dictionary of sets, set algebra (`&`, `|`, `-`), query parsing.

- **Background:**
  Search engines index documents by building an *inverted index* mapping words to the set of document IDs containing those words.
- **Documents Dataset:**
  ```python
  documents = {
      "doc1": "Python is a dynamic programming language known for readable code",
      "doc2": "Functional programming in Python emphasizes pure functions and immutability",
      "doc3": "High performance computing in Python relies on vectorization and sets",
      "doc4": "Sets and dictionaries provide fast hash table lookups in Python",
      "doc5": "Data structures like lists and tuples maintain ordered sequences"
  }
  ```
- **Requirements:**
  1. **Index Construction:**
     - Clean and normalize each document: lowercase, remove punctuation, split into word tokens.
     - Construct an inverted index dictionary: `index[word] = {doc_id1, doc_id2, ...}`.
  2. **Query Evaluator:**
     Build a query engine supporting three boolean operations using Python set operators:
     - `AND(word1, word2)` $\rightarrow$ `index[word1] & index[word2]`
     - `OR(word1, word2)` $\rightarrow$ `index[word1] | index[word2]`
     - `NOT(word)` $\rightarrow$ `all_docs - index[word]`
  3. **Complex Query:**
     Evaluate compound queries like:
     `( "python" AND "sets" ) AND NOT "functional"`
     Return the matching document IDs along with the original document excerpts.

---

## 🏆 Section 6: Comprehensive Capstone Projects

### Challenge 16: In-Memory Relational Engine (Join, Filter, Aggregate)
**Topic:** Polyglot data modeling (lists of dictionaries, tuple keys, set lookups), relational algebra.

Build a mini relational query engine that operates directly on Python lists and dictionaries:

```python
users_table = [
    {"user_id": 1, "name": "Alice", "dept_id": 10},
    {"user_id": 2, "name": "Bob", "dept_id": 20},
    {"user_id": 3, "name": "Charlie", "dept_id": 10},
    {"user_id": 4, "name": "Diana", "dept_id": 30},
    {"user_id": 5, "name": "Evan", "dept_id": 99} # No matching department
]

departments_table = [
    {"dept_id": 10, "dept_name": "Engineering", "budget": 500000},
    {"dept_id": 20, "dept_name": "Marketing", "budget": 200000},
    {"dept_id": 30, "dept_name": "Finance", "budget": 350000},
    {"dept_id": 40, "dept_name": "Human Resources", "budget": 150000}
]

salaries_table = [
    {"user_id": 1, "salary": 120000},
    {"user_id": 2, "salary": 85000},
    {"user_id": 3, "salary": 115000},
    {"user_id": 4, "salary": 95000}
]
```

- **Operations to Implement:**
  1. `inner_join(table_a, table_b, key_a, key_b)`:
     - Merge rows on equality of `key_a` and `key_b`.
     - Optimize using a hash index: build a dictionary on `table_b` keyed by `key_b` before iterating through `table_a`.
  2. `left_outer_join(table_a, table_b, key_a, key_b)`:
     - Preserve all records from `table_a`, populating missing `table_b` attributes with `None`.
  3. `group_by_aggregate(table, group_key, agg_field, agg_func)`:
     - Group rows by `group_key` (e.g., `"dept_name"`).
     - Compute aggregate statistics (`"sum"`, `"avg"`, `"max"`, `"count"`).
  4. **End-to-End Query:**
     Run a single pipeline that computes the **average salary per department** for all valid departments, sorted descending by average salary.

---

### Challenge 17: LRU (Least Recently Used) Cache Simulator
**Topic:** Double-ended list tracking, dictionary fast lookups, eviction policies, capacity management.

- **Problem:**
  Design and implement a data structure for a **Least Recently Used (LRU) Cache** with a fixed capacity $N$, using only built-in `list` and `dict` (do **not** use `collections.OrderedDict`).
- **Specifications:**
  - `cache = LRUCache(capacity=3)`
  - `cache.get(key)`:
    - If `key` exists in cache, return its value and mark `key` as most recently used (move to the front/end of access order).
    - If `key` does not exist, return `-1`.
    - Must perform lookup in $O(1)$ time using a dictionary.
  - `cache.put(key, value)`:
    - Update the value if `key` exists and mark it as most recently used.
    - If `key` is new and the cache has reached maximum capacity, **evict the least recently used key** from both the tracker list and the dictionary before inserting the new entry.
- **Trace Test Scenario:**
  ```python
  # Capacity = 2
  # put("a", 1)  -> cache: {"a": 1}, order: ["a"]
  # put("b", 2)  -> cache: {"a": 1, "b": 2}, order: ["a", "b"]
  # get("a")     -> returns 1, order refreshed: ["b", "a"]
  # put("c", 3)  -> evicts "b"! cache: {"a": 1, "c": 3}, order: ["a", "c"]
  # get("b")     -> returns -1 (evicted)
  # put("d", 4)  -> evicts "a"! cache: {"c": 3, "d": 4}, order: ["c", "d"]
  # get("a")     -> returns -1
  # get("c")     -> returns 3
  # get("d")     -> returns 4
  ```

---

## 🏆 Checklist for Completion

- [ ] **Section 1: Lists**
  - [ ] Dutch National Flag in-place 3-pointer partition
  - [ ] Ragged matrix transposition & arbitrary depth flattener
  - [ ] Sliding window mean, median, and range buffer
- [ ] **Section 2: Tuples**
  - [ ] Immutable financial transaction ledger & state machine
  - [ ] 3D spatial coordinate distance & closest-pair algorithm
  - [ ] Investigation of mutable objects inside tuples & `deep_freeze()`
- [ ] **Section 3: Sets**
  - [ ] Jaccard similarity & skill gap affinity engine
  - [ ] RBAC permission Venn diagram & conflict analyzer
  - [ ] Multi-environment configuration drift detector
- [ ] **Section 4: Dictionaries**
  - [ ] Course enrollment inverter with collision resolution
  - [ ] Deep nested dictionary flattener, unflattener, and safe path traversal
  - [ ] HTTP access log frequency counter & secondary indexing
- [ ] **Section 5: Cross-Collection Synergy**
  - [ ] Social graph network degrees of separation & triangle cliques
  - [ ] Multi-warehouse inventory allocation & order fulfillment
  - [ ] Inverted text index & boolean query engine (`AND`, `OR`, `NOT`)
- [ ] **Section 6: Capstone Projects**
  - [ ] In-memory relational engine (`JOIN`, `GROUP BY`, aggregate)
  - [ ] LRU Cache simulator with capacity eviction
