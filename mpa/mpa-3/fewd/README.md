## Problem Statement

Build the **async data layer** for a small music app called **TuneFetch** — the layer
that talks to an API and hands clean data back to the rest of the app. You write **no
HTML**: all of your code goes in `src/app.js`.

You implement **10 functions**. Every one returns a **Promise** — either because you
build one directly, or because you mark the function `async`. Some of them call
`fetch(url)` and read JSON back, exactly like the real Fetch API.

`index.html` **is** a **Jasmine Spec Runner** — open it in a browser and it
automatically runs the 10 tests against your functions. All 10 start **red**; make
every one **green**.

## There is no real network

The tests install a **fake `fetch`** for you, so you don't need a server or an internet
connection. Your functions just call the global `fetch(url)` the normal way:

```js
const response = await fetch(url);   // response has .ok, .status
if (!response.ok) throw new Error(); // handle failures
const data = await response.json();  // parse the JSON body
```

The fake API serves this playlist at `/api/songs`:

```js
[
  { id: 1, title: "Levitating",      artist: "Dua Lipa",     plays: 120 },
  { id: 2, title: "Blinding Lights", artist: "The Weeknd",   plays: 200 },
  { id: 3, title: "As It Was",       artist: "Harry Styles", plays: 150 }
]
```

## Tasks — functions to implement in `src/app.js`

| # | Function | Must do |
|---|----------|---------|
| 1 | `resolveWith(value)` | return a Promise that **resolves** to `value` |
| 2 | `rejectWith(message)` | return a Promise that **rejects** with `new Error(message)` |
| 3 | `delay(ms)` | return a Promise that resolves **after `ms` milliseconds** (`setTimeout`) |
| 4 | `doubleAsync(n)` | an **`async`** function that returns `n * 2` |
| 5 | `fetchJSON(url)` | `await fetch(url)`, then return the **parsed JSON** |
| 6 | `fetchJSON(url)` | if `response.ok` is **false**, **throw** an `Error` instead |
| 7 | `getSongTitles(url)` | resolve to an array of **every song's `.title`** |
| 8 | `getSongById(url, id)` | resolve to the song whose `.id === id`, or **`null`** if none |
| 9 | `fetchAll(urls)` | fetch every url at once with **`Promise.all`**; resolve to all results |
| 10 | `safeFetch(url)` | return the data on success, or **`null`** if anything fails (`try`/`catch`) |

## Instructions

- Edit **only** `src/app.js`. Do not edit `index.html`, `main.css`, or
  `tests/FunctionsTest.js`.
- Open `index.html` in your browser — it **is** the Jasmine Spec Runner. No build tools
  and no server are needed. Refresh after each change to re-run the specs.
- Use **Promises**, **`async`/`await`**, **`fetch`**, and `response.json()`. No external
  libraries and no CDN links — plain JavaScript only.
- A spec turns **green** when the matching behaviour is correct. Aim for all 10 green.

## Test Cases

| # | Test | Concept | Marks |
|---|------|---------|-------|
| 1 | `resolveWith(value)` returns a Promise that resolves to `value` | creating Promises | 2 |
| 2 | `rejectWith(message)` rejects with an `Error` | rejecting Promises | 2 |
| 3 | `delay(ms)` resolves after the delay | Promise + `setTimeout` | 2 |
| 4 | `doubleAsync(n)` is `async` and resolves to `n * 2` | `async`/`await` basics | 2 |
| 5 | `fetchJSON(url)` fetches and returns parsed JSON | `fetch` + `.json()` | 2 |
| 6 | `fetchJSON(url)` throws when `response.ok` is false | error handling | 2 |
| 7 | `getSongTitles(url)` resolves to an array of titles | `await` + `fetch` + `map` | 2 |
| 8 | `getSongById(url, id)` resolves to the song or `null` | `find` + null handling | 2 |
| 9 | `fetchAll(urls)` uses `Promise.all` for all results | concurrent fetches | 2 |
| 10 | `safeFetch(url)` returns data on success, `null` on failure | `try`/`catch` | 2 |

## Submission Guidelines

- Submit your completed **`src/app.js`** (keep the folder structure — `tests/`, `src/`,
  and `index.html` stay where they are).
- Before submitting, open `index.html` and confirm **all 10 specs are green** — your
  score is the number of green specs × 2 (out of 20).
- Do **not** modify `tests/FunctionsTest.js`, `index.html`, or `main.css`.
- No external libraries, no CDN links — plain JavaScript only.

## Files

| File | You edit? | Purpose |
|------|-----------|---------|
| `src/app.js` | ✅ yes | the 10 async functions you build |
| `index.html` | ❌ no | the Jasmine Spec Runner (empty page on purpose) |
| `main.css` | ❌ no | page styling (not graded) |
| `tests/FunctionsTest.js` | ❌ no | the 10 automated specs + the fake `fetch` |

## How it runs

Open `index.html` in the browser — it **is** the Jasmine Spec Runner. The specs install
a fake `fetch`, call your functions, and check what their Promises resolve (or reject)
with. Jasmine loads from `jasmine/jasmine-2.8.0/` (provided by the platform, same as
every other assignment). No build tools, no server.
