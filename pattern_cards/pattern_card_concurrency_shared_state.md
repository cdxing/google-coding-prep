# Pattern Card — Concurrency, Shared Mutable State, and Race Conditions

## 1. Core problem

When multiple threads or workers read and write the same object at the same time, the final result may depend on timing rather than logic.

This can cause:

- lost updates
- corrupted shared state
- inconsistent intermediate state
- nondeterministic output
- bugs that disappear when debugging
- results that look successful but are silently wrong

Core sentence:

> The danger of concurrency bugs is not only crashing. The more dangerous case is silently producing unreliable results.

---

## 2. Key concepts

### Shared mutable state

A data structure or object that multiple workers can modify.

Examples:

- shared list
- shared dict/map
- shared counter
- shared cache
- shared model state
- shared file handle
- shared database row

### Race condition

A bug where the output depends on the order/timing of operations across threads.

Example:

```text
counter = 0
Thread A reads counter = 0
Thread B reads counter = 0
Thread A writes counter = 1
Thread B writes counter = 1
Expected result: 2
Actual result: 1
```

### Critical section

The smallest piece of code that must not be executed by two threads at the same time.

Example:

```python
with lock:
    shared_counter += 1
```

---

## 3. First principle

Do not start by adding locks everywhere.

Use this priority order:

1. Avoid shared mutable state.
2. Use local results and merge later.
3. Use a single writer.
4. Use a thread-safe queue.
5. Use a lock/mutex around the smallest critical section.
6. Use atomic operations for simple counters/flags.
7. Use transactions or optimistic locking for database/distributed updates.

Core sentence:

> First avoid sharing. If sharing is unavoidable, control the write path.

---

## 4. Best default pattern: local result + deterministic reduce

This is the safest interview answer for many ML/data pipeline problems.

### Idea

Each worker:

- receives an input item
- computes a local result
- returns `JobResult`
- does not mutate shared global objects

The main thread:

- collects results
- preserves input order if needed
- merges results deterministically

### Python sketch

```python
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Optional

@dataclass
class JobResult:
    index: int
    ok: bool
    value: Optional[Any] = None
    error: Optional[str] = None


def process_one(index: int, item: Any) -> JobResult:
    try:
        # Do work locally. Do not mutate shared global state.
        value = item * item
        return JobResult(index=index, ok=True, value=value)
    except Exception as e:
        return JobResult(index=index, ok=False, error=str(e))


def process_jobs(items: list[Any], max_workers: int = 4) -> list[JobResult]:
    results: list[Optional[JobResult]] = [None] * len(items)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_one, i, item) for i, item in enumerate(items)]

        for future in as_completed(futures):
            result = future.result()
            results[result.index] = result

    return [r for r in results if r is not None]
```

### Why this is good

- worker logic is isolated
- failures are local
- no shared mutation inside worker
- result order can be preserved
- easy to test
- easy to extend with retry/timeout/logging

---

## 5. Lock / mutex pattern

Use when workers must update shared state.

### Python sketch

```python
import threading

lock = threading.Lock()
shared_counts = {}


def worker(key: str) -> None:
    local_value = 1

    # Keep the critical section small.
    with lock:
        shared_counts[key] = shared_counts.get(key, 0) + local_value
```

### Rules

- lock only the minimum code needed
- do not perform slow I/O under lock
- do not call external services under lock
- avoid nested locks unless absolutely necessary
- document what the lock protects

---

## 6. Queue + single writer pattern

Use when many workers produce outputs, but only one process should update shared state, write a file, or commit to a database.

### Idea

- workers produce messages
- a thread-safe queue holds messages
- one writer consumes messages and updates shared state

This pattern is strong for:

- ML data pipelines
- logging systems
- batch job result aggregation
- database writes
- file writes

Core sentence:

> Multiple producers are okay. Shared writes should often go through one controlled writer.

---

## 7. Atomic operations

Use for very simple shared state:

- counter
- flag
- reference swap

In C++:

```cpp
#include <atomic>

std::atomic<int> counter{0};

void worker() {
    counter.fetch_add(1, std::memory_order_relaxed);
}
```

Use atomic when the operation is simple. For compound updates involving multiple fields, use a lock or redesign the state flow.

---

## 8. C++ mutex sketch

```cpp
#include <mutex>
#include <unordered_map>
#include <string>

std::mutex mtx;
std::unordered_map<std::string, int> counts;

void update_count(const std::string& key) {
    int local_value = 1;

    {
        std::lock_guard<std::mutex> guard(mtx);
        counts[key] += local_value;
    }
}
```

Rules:

- use RAII (`std::lock_guard`) to avoid forgetting unlock
- keep locked region small
- avoid holding lock during slow computation
- prefer local computation before acquiring lock

---

## 9. How to test concurrency bugs

Concurrency bugs may not appear every time. Test by increasing pressure.

Strategies:

- run the same test many times
- use many workers
- use random sleeps
- compare parallel result with sequential baseline
- test large inputs
- test failure cases
- assert deterministic output

### Test principle

```text
parallel_result should equal sequential_result
for many repeated runs
under random timing
```

---

## 10. Interview answer framework

When asked about multiple threads modifying the same object:

1. Clarify whether workers need to share state.
2. Clarify whether output order matters.
3. Prefer local result + deterministic reduce.
4. If shared state is unavoidable, use a lock or single-writer queue.
5. Keep critical sections small.
6. Add stress tests.
7. Explain tradeoffs.

### 30-second answer

> I would first identify whether multiple workers are modifying the same shared state. If possible, I would avoid shared mutation by letting each worker produce a local result and then merge the results in a deterministic reduce step. If shared state is unavoidable, I would protect the smallest critical section with a lock, or use a queue with a single writer. Finally, I would compare the parallel output against a sequential baseline and run stress tests to make sure the result is deterministic.

---

## 11. Connection to ML/data pipelines

In ML/data infrastructure, shared-state bugs can affect:

- dataset manifests
- training logs
- evaluation metrics
- checkpoint metadata
- feature store updates
- model registry entries
- output files

Safe design principle:

> Workers should compute. Coordinators should commit.

---

## 12. Claude Code practice prompt

Use this prompt for coding practice:

```text
Implement a Python job processor.

Requirements:
1. Input is a list of jobs, where each job has an id and payload.
2. Start with a sequential implementation.
3. Add a ThreadPoolExecutor version with bounded concurrency.
4. Preserve input order in the returned results.
5. Each worker must not mutate shared global state.
6. Return a structured JobResult with job_id, index, ok, value, and error.
7. Add random sleep and random failure to simulate real jobs.
8. Add a sequential baseline check and run the parallel version multiple times to confirm deterministic output shape.
9. Explain how this design avoids race conditions.
```
