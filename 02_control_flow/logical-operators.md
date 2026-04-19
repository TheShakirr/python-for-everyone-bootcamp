# Logical operators

## Theory

**Logical operators** combine boolean values:

| Operator | Meaning |
|----------|---------|
| `and` | True if **both** sides are true |
| `or` | True if **at least one** side is true |
| `not` | True if the operand is false |

Python uses **short-circuit** evaluation:

- For `a and b`, if `a` is false, `b` is not evaluated.
- For `a or b`, if `a` is true, `b` is not evaluated.

**Truthiness:** In `if` and `while`, Python can use non-boolean values; they are converted using truthiness (e.g. empty string `""` is false, non-zero numbers are true). Prefer explicit comparisons for clarity until you are comfortable.

## Beginner-friendly notes

- Use **parentheses** when mixing `and` / `or` so the meaning is obvious: `(a or b) and c` vs `a or (b and c)`.
- `not (x == y)` is the same as `x != y` for numbers and strings; use whichever reads better.

## Example

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Can enter.")
else:
    print("Cannot enter.")

score = 85
if score < 60 or score > 100:
    print("Invalid score range")
else:
    print("Score OK")

ready = False
print(not ready)
```

## Expected output

```text
Can enter.
Score OK
True
```

## Mini practice

1. Set `username = "alex"` and `logged_in = True`. If both are set that way, print `"Dashboard"`; otherwise print `"Go away"`.
2. Set `day = "Saturday"`. Print `"Weekend!"` if `day` is `"Saturday"` **or** `"Sunday"`, else print `"Weekday"`.

Continue with `if-elif-else.md`.
