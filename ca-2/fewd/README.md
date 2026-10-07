
## Problem Statement

Implement **10 JavaScript functions** for a small **Task Tracker** — the data layer
behind a to-do app. You write **no HTML**: all your code goes in `src/app.js`.

A **task** is a plain object shaped like:

```js
{ title: "Buy milk", status: "todo", done: false, priority: "high" }
```

`index.html` **is** a **Jasmine Spec Runner** — open it in a browser and it
automatically runs the 10 tests against your functions. All 10 start **red**; make
every one **green**.

## Tasks — functions to implement in `src/app.js`

| # | Function | Must return |
|---|----------|-------------|
| 1 | `greet(name)` | a **template-literal** greeting: `greet("Aisha")` → `"Hi, Aisha! Welcome back."` |
| 2 | `isPassing(score)` | `true` when `score >= 40`, else `false` |
| 3 | `sumScores(scores)` | sum of the number array; `[]` → `0` |
| 4 | `highScores(scores, min)` | a **new** array of scores strictly `> min` (original untouched) |
| 5 | `titles(tasks)` | array of every task's `.title`, in order |
| 6 | `countByStatus(tasks, status)` | how many tasks have that `.status` |
| 7 | `toggleDone(task)` | a **new** object with `.done` flipped — original **not** mutated |
| 8 | `longestTitle(tasks)` | the `.title` string with the most characters |
| 9 | `averageScore(scores)` | the average; `[]` → `0` (no divide-by-zero) |
| 10 | `formatTask(task)` | **template-literal** line: `"[x] Ship (low)"` / `"[ ] Buy milk (high)"` |

## Instructions

- Edit **only** `src/app.js`. Do not rename the functions or change their parameters.
- **Do not edit** `index.html`, `main.css`, or `tests/FunctionsTest.js`.
- Open `index.html` in your browser — it **is** the Jasmine Spec Runner. No build
  tools and no server are needed. Refresh after each change to re-run the specs.
- Keep each function **pure**: return a value; don't `console.log` and don't mutate
  the inputs unless the task explicitly says to (tasks 4 and 7 must not mutate).
- A spec turns **green** when its function is correct. Aim for all 10 green.

## Test Cases

| # | Test | Concept | Marks |
|---|------|---------|-------|
| 1 | `greet` returns the exact greeting | template literals | 2 |
| 2 | `isPassing` true only for `>= 40` | comparison operators / conditionals | 2 |
| 3 | `sumScores` totals the array, `[]`→0 | loops / `reduce` | 2 |
| 4 | `highScores` filters `> min`, no mutation | array `filter` | 2 |
| 5 | `titles` maps tasks to titles | array `map` + objects | 2 |
| 6 | `countByStatus` counts matches | filter/loop + objects | 2 |
| 7 | `toggleDone` returns a new, unmutated object | objects + spread | 2 |
| 8 | `longestTitle` finds the longest title | loops + comparison | 2 |
| 9 | `averageScore` averages, `[]`→0 | edge-case handling | 2 |
| 10 | `formatTask` builds the display line | template literals + conditional | 2 |

## Submission Guidelines

- Submit your completed **`src/app.js`** (keep the folder structure — `tests/`,
  `src/`, and `index.html` stay where they are).
- Before submitting, open `index.html` and confirm **all 10 specs are green** — your
  score is the number of green specs × 2 (out of 20).
- Do **not** modify `tests/FunctionsTest.js`, `index.html`, or `main.css`.
- No external libraries, no CDN links — plain JavaScript only.



## Files

| File | Student edits? | Purpose |
|------|----------------|---------|
| `src/app.js` | ✅ yes | the 10 functions you implement |
| `index.html` | ❌ no | the Jasmine Spec Runner |
| `main.css` | ❌ no | page styling (not graded) |
| `tests/FunctionsTest.js` | ❌ no | the 10 automated specs |

## How it runs

Open `index.html` in the browser — it **is** the Jasmine Spec Runner. Jasmine loads
from `jasmine/jasmine-2.8.0/` (provided by the platform, same as every other
assignment). No build tools, no server.
