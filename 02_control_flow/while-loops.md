# `while` loops

## Theory

A **`while`** loop repeats a block **as long as** a condition is true:

```python
while condition:
    # indented block
```

Before each iteration, Python evaluates `condition`. If it is true, the block runs; then the condition is checked again. If it becomes false, the loop exits.

**Risk:** If the condition never becomes false, you get an **infinite loop**. Always ensure something inside the loop can eventually make the condition false (or use `break` in a controlled way).

Use `while` when the number of iterations is **not known in advance** (e.g. “until user types quit”) or when you are modeling “keep going while X.”

## Beginner-friendly notes

- `while True:` with a **`break`** inside is a common pattern for menus (exit when user chooses quit).
- Make sure variables used in the condition **change** inside the loop when needed.
- Compare: `for` = “for each item”; `while` = “as long as this holds.”

## Example

```python
n = 3
while n > 0:
    print(n)
    n = n - 1
print("lift off")
```

## Expected output

```text
3
2
1
lift off
```

## Mini practice

1. Set `count = 1`. Use `while` to print `count` from **1** to **5**, then stop.
2. Set `n = 0`. Use `while` to print `"tick"` exactly **three** times (add `1` to `n` each time until you have printed three lines).

Continue with `break-continue-pass.md`.
