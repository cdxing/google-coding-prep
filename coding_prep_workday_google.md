# Coding Prep — Workday + Google Week

Created: 2026-06-29 (Sun evening)
Target: Workday Coding Wed Jul 1 10:00 AM (Victor Ardulov, HackerRank CodePair)
Secondary: Google Behavioral Tue Jun 30 12:30 PM

---

## Interview Ritual (every problem)

```text
1. Clarify: restate problem, ask about edge cases, constraints
2. Brute force: say it out loud, state complexity
3. Optimized: name the pattern, explain WHY it works
4. Code: clean Python, talk while typing
5. Test: walk through 2-3 examples including edge case
6. Complexity: time and space, one sentence each
```

Never silently type. Always explain before writing.

---

## Tonight: Sun Jun 29, 9:15–10:30 PM

### Goal: warm up Python hands + interview flow, not new patterns

Pick 2 from:

#### Option A: Two Sum (hashmap warmup, 15-20 min)

```text
Pattern: hashmap lookup
Key idea: for each num, check if target - num is in the map
Edge: duplicates, negative numbers, single element
```

#### Option B: Subarray Sum Equals K (prefix sum, 25-30 min)

```text
Pattern: prefix sum + hashmap
Key idea: at each index, count how many previous prefix sums equal current_sum - k
Edge: k=0, all zeros, negative numbers, empty array
Already have pattern card: /Users/dchenmac/Desktop/Jun2026/28/pattern_card_subarray_sum_prefix_hashmap.md
```

#### Option C: Merge Intervals (interval pattern, 25-30 min)

```text
Pattern: sort by start, merge overlapping
Key idea: sort intervals, extend end if overlap, else append new
Edge: single interval, fully nested, touching edges, empty input
```

**Minimum success tonight:**
1. Complete 1 medium problem end-to-end in Python
2. Say the interview ritual out loud for each
3. Write 1 pattern card

---

## Tomorrow: Mon Jun 30

### 9:00–10:30 AM — Coding Block 1

| # | Problem | Pattern | Target | Priority |
|---|---------|---------|--------|----------|
| 1 | Two Sum | hashmap | 10 min | warmup |
| 2 | Longest Consecutive Sequence | hashset | 20 min | P0 |
| 3 | Subarray Sum Equals K | prefix sum + hashmap | 15 min | P0 |
| 4 | Max Subarray (Kadane's) | running max | 15 min | P1 |
| 5 | Sliding Window Maximum | sliding window | 20 min | P1 |

After block: write pattern cards for any new patterns.

### 11:00–12:00 PM — Google Behavioral Final Practice

```text
- Read cheat sheet once: /Users/dchenmac/Desktop/Jun2026/28/google_behavioral_cheat_sheet.md
- Practice Story B (Bob disagreement) out loud x1
- Practice Story A (Afterburner 2x2 matrix) out loud x1
- Each story: 15-sec summary hook → STAR → learning, under 3 min
- Review "Tell me about yourself" and "Why Google"
```

### 12:30–1:15 PM — Google Behavioral Interview

### 2:30–4:00 PM — Coding Block 2

| # | Problem | Pattern | Target | Priority |
|---|---------|---------|--------|----------|
| 1 | Merge Intervals | sort + merge | 20 min | P0 |
| 2 | Insert Interval | binary search / scan | 20 min | P1 |
| 3 | Valid Parentheses | stack | 10 min | warmup |
| 4 | Daily Temperatures | monotonic stack | 20 min | P1 |
| 5 | Number of Islands | BFS/DFS grid | 20 min | P1 |

### 7:30–8:30 PM — Coding Mock

```text
Pick 1 unsolved medium
Set 45-min timer
Full interview ritual: clarify → brute → optimize → code → test → complexity
No hints, no looking up
```

---

## Pattern Cards Template

For each pattern, write:

```text
## [Pattern Name]

When to use:
  [1 sentence: what problem shape triggers this pattern]

Core idea:
  [1-2 sentences: the key insight]

Edge cases:
  [3-4 bullet points]

One-sentence interview explanation:
  [What you say when the interviewer asks "why this approach?"]
```

---

## Patterns to Cover This Week

| Pattern | Key Problem | Status |
|---------|-------------|--------|
| HashMap lookup | Two Sum | review |
| Prefix Sum + HashMap | Subarray Sum = K | card done |
| Sliding Window | Max subarray of size k | todo |
| Sort + Merge | Merge Intervals | todo |
| Stack | Valid Parentheses, Daily Temps | todo |
| BFS/DFS grid | Number of Islands | todo |
| Two Pointers | Container With Most Water | stretch |
| Binary Search | Search in Rotated Array | stretch |

---

## Workday CodePair Specifics

```text
Platform: HackerRank CodePair
Recording: BrightHire
Language: Python
Style: collaborative, explain reasoning out loud
Interviewer: Victor Ardulov

Key behaviors:
- Talk through the problem BEFORE writing code
- Accept hints gracefully
- Ask "does this direction make sense?" before coding
- State assumptions explicitly
- Test with examples on screen
```

---

## Minimum Success Metrics

### Tonight (Sun)
- [ ] 1 medium solved end-to-end
- [ ] Interview ritual spoken out loud
- [ ] 1 pattern card written

### Tomorrow morning (Mon)
- [ ] 3+ problems completed in Coding Block 1
- [ ] Pattern cards for hashmap, sliding window

### Tomorrow afternoon (Mon)
- [ ] Google behavioral interview done
- [ ] 3+ problems completed in Coding Block 2
- [ ] Pattern cards for intervals, stack

### Tomorrow evening (Mon)
- [ ] 45-min mock completed
- [ ] Total patterns with cards: 6+
