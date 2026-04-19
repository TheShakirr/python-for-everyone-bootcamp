# Assignment 1: Mini quiz program

**Due:** Wednesday, April 22, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** One runnable program that uses variables, `input`/`print`, branching, and at least one loop—covering the core outcomes of Sections 1 and 2.

**Sections covered:** **Section 1 — Python Foundations** and **Section 2 — Control Flow**

Build a small **text-based quiz** in Python. You combine ideas from both sections: variables, input and output, strings and numbers, comments, then branching, comparisons, and at least one loop.

---

## What you will practice

| From Section 1 | From Section 2 |
|----------------|----------------|
| Running a `.py` script | `if` / `elif` / `else` |
| `print` and `input()` | Comparisons (`==`, etc.) |
| Variables and clear names | `for` or `while` (your choice where it fits) |
| Comments (`# ...`) | Optional: `and` / `or`, `break`, or `range` if helpful |

---

## Requirements

Submit **`quiz.py`** only (one file).

1. **Greeting** — Ask the user for their **name** with `input()` and print a one-line welcome that uses their name.
2. **At least three questions** — You choose the topic (for example: silly facts, Python basics, or your own hobby). Each question should:
   - Show the question with `print`.
   - Read the answer with `input()`.
   - Decide if the answer is **correct** using `if` / `elif` / `else` (or nested `if`s). You may accept one correct answer or a few spellings—say in a **comment** what you accept.
3. **Score** — Use an **integer variable** (start at `0`). Each correct answer should **increase** the score (use `+=` or `score = score + 1`).
4. **Final message** — After the last question, print the user’s **name** and **final score** (for example: `3 out of 3` or `2 out of 3`).
5. **Comments** — Add a short comment at the top of the file (your name or alias, and one line describing the program).

**Stretch (optional):** **Play again** with a **`while`** loop, or number questions with **`for`** + **`range`**.

---

## Example session (shape only—your wording will differ)

```text
What is your name? Sam
Welcome, Sam!

Q1: What keyword prints text to the screen? print
Correct!

Q2: ...

Sam, you scored 2 out of 3.
```

---

## Submitting

Follow **`submissions/README.md`**: fork the repo, add **`quiz.py`** to **`submissions/<your-github-username>/`**, then open a pull request.

---

## Checklist before you submit

- [ ] Script runs without errors with `python quiz.py` or `python3 quiz.py`.
- [ ] Uses **both** `input` and `print`, and at least one **`if`** (or `elif` / `else`).
- [ ] Score updates when the answer is correct.
- [ ] Code is readable: sensible variable names and a few helpful comments.
