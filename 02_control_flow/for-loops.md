# `for` loops

## Theory

A **`for`** loop repeats a block of code **once for each item** in an **iterable**—something you can loop over (string, list, `range`, etc.). The syntax is:

```python
for variable_name in iterable:
    # indented block
```

On each iteration, `variable_name` is bound to the **next** item. The loop ends when there are no more items.

`for` is the usual choice when you know **how many times** you will iterate (or you are walking a collection). If the stopping rule is more about a condition than a collection, you might use `while` (next lesson). Square brackets `[2, 4, 6]` build a **list**; a later section covers lists in detail.

## Counting with `range()`

**`range`** builds a **sequence of integers** for looping with `for`. In Python 3, `range(...)` returns a **range object** (memory-friendly), not a full list—but you iterate it like any iterable.

| Call | Meaning |
|------|---------|
| `range(stop)` | integers from **0** up to **stop - 1** |
| `range(start, stop)` | from **start** up to **stop - 1** |
| `range(start, stop, step)` | same, with **step** between values (can be negative) |

**Stop is exclusive:** `range(3)` yields `0`, `1`, `2`—not `3`. To include **1 through 10**, use `range(1, 11)`.

If you need a real list (for printing or debugging), use `list(range(...))`.

## Beginner-friendly notes

- The loop variable name is yours: `for letter in word`, `for n in numbers`, etc.
- Use **`range`** when you need a **numeric run** (indices, counts, “repeat N times”).
- Do not modify the thing you are iterating over in tricky ways as a beginner—iterate a copy or rebuild lists later when you learn more.

## Example

```python
word = "Hi"
for ch in word:
    print(ch)

numbers = [2, 4, 6]
total = 0
for n in numbers:
    total = total + n
print("sum:", total)

print(list(range(5)))
for i in range(2, 5):
    print("i =", i)
```

## Expected output

```text
H
i
sum: 12
[0, 1, 2, 3, 4]
i = 2
i = 3
i = 4
```

## Mini practice

1. Use `for` to print each character of your first name on its own line.
2. Use `for n in range(3):` to print `n` three times (you should see `0`, then `1`, then `2`).
3. Use `for n in range(1, 6):` to print the numbers **1** through **5**.

Continue with `while-loops.md`.
