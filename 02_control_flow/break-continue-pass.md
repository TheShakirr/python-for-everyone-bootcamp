# `break`, `continue`, `pass`

## Theory

These three keywords change control flow inside loops (`for` or `while`):

- **`break`** — Exit the **nearest** loop immediately. Execution continues after the loop body.
- **`continue`** — Skip the rest of the **current** iteration and go to the **next** iteration of the same loop.
- **`pass`** — Does **nothing**. It is a placeholder where syntax requires a statement (e.g. empty `if` block, stub function). It is **not** a loop control like `continue`.

## Beginner-friendly notes

- `break` is useful for “search until found” or menu “quit” options.
- `continue` is useful for “skip bad items and keep going” (e.g. skip even numbers).
- Too many `break`/`continue` in one loop can hurt readability—sometimes an `if`/`else` is clearer.

## Example

```python
# break: stop when we find 4
for n in [1, 2, 3, 4, 5]:
    if n == 4:
        print("found 4, stopping")
        break
    print(n)

# continue: skip even numbers
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)

# pass: placeholder (runs without error)
for n in range(3):
    pass  # TODO: handle n later
print("done")
```

## Expected output

```text
1
2
3
found 4, stopping
1
3
5
done
```

(First loop prints `1`, `2`, `3`, then `found 4, stopping`. Second loop prints odd numbers `1`, `3`, `5`. Third loop prints nothing from `pass`, then `done`.)

## Mini practice

1. Use `for n in range(10):`. Print `n`, but use **`break`** so the loop stops right after printing **`3`** (you should see `0`, `1`, `2`, `3` only).
2. Use `for n in range(6):`. Print `n` unless `n` is **`2`**—in that case use **`continue`** so nothing prints for that round (you should see `0`, `1`, `3`, `4`, `5`).
3. Write an `if False:` block whose body is only **`pass`** so the file still runs without error.

**End of Section 2 lessons.** Complete `homework.md`, then continue when your instructor publishes the next section.
