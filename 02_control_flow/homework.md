# Homework — Section 2: Control Flow

Complete these tasks after you finish all lessons in this section (through `break-continue-pass.md`). They follow the same ideas as the **Mini practice** steps in each lesson—just a bit longer and using `input()` where it helps.

Submit according to your instructor’s format (files, screenshots, or a short write-up).

Use **`range`** with **`for`** loops the way it is shown in `for-loops.md`.

---

## Assignment 1: Temperature from the user

Write `temperature_input.py` that:

1. Asks the user for a **temperature** as an integer (use `input()` and `int(...)`).
2. Uses **`if` / `elif` / `else`** with the **same thresholds** as the `if-elif-else` lesson mini practice: **25 or above** → print `"warm"`; **15 or above** (but below 25) → print `"ok"`; otherwise → print `"cold"`.

**Deliverable:** `temperature_input.py` + one example run pasted (any integer you type is fine).

---

## Assignment 2: Nested questions (admin gate)

Write `admin_gate.py` that:

1. Asks for a **username** with `input()`.
2. If the username is **`"admin"`**, asks for a **password**. If the password is **`"secret"`**, prints **`"Access granted"`**. Otherwise prints **`"Wrong password"`**.
3. If the username is **not** `admin`, prints **`"Unknown user"`** and does **not** ask for a password.

This matches the nested-conditions lesson mini practice, using the same strings.

**Deliverable:** `admin_gate.py` + two example runs: one that reaches `"Access granted"`, and one that shows `"Unknown user"` or `"Wrong password"`.

---

## Assignment 3: Loops review

Write `loops_review.py` one file with **three** labeled parts (use comments like `# Part A`):

**Part A — `for` over text**  
Ask the user for a **short word** (or use a variable). Print **each character** on its own line, like the `for-loops` mini practice with your name.

**Part B — `for` with `range`**  
Use `for` and `range` to print the numbers **1** through **10**, each on its own line.

**Part C — `while` counter**  
Set `count = 1`. Use a **`while`** loop to print `count` from **1** to **5** inclusive, then stop (same idea as the `while-loops` mini practice).

**Deliverable:** `loops_review.py` + pasted output showing all three parts.

---

## Self-check

- [ ] Every `if` / `elif` / `else` lines up the way you intend (watch indentation).
- [ ] You used `==` for comparisons, not `=` inside conditions.
- [ ] Loops stop when they should (no accidental infinite `while`).
- [ ] `range` start/stop matches what you want (remember: the **stop** value is not included).

After you finish this homework, you are ready to go to the **next** section of the bootcamp.
