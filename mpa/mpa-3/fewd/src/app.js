/*
 * TuneFetch — build the async "data layer" for a music app here.
 * ------------------------------------------------------------------
 * Implement 10 functions. Every one returns a Promise — either because
 * you build one directly, or because you mark the function `async`.
 *
 * The tests provide a FAKE global `fetch`, so call `fetch(url)` exactly
 * like the real Fetch API: `await fetch(url)` gives a response with
 * `.ok`, `.status`, and a `.json()` method that returns a Promise of
 * the parsed data. No real network or server is involved.
 *
 * Each behaviour is checked by a Jasmine spec in tests/FunctionsTest.js
 * (10 specs x 2 marks = 20).
 *
 * Rules:
 *   - Do NOT edit index.html, main.css, or tests/FunctionsTest.js.
 *   - Use Promises, async/await, and fetch — no external libraries.
 * ------------------------------------------------------------------
 */

function resolveWith(value) {
  return Promise.resolve(value);
}

function rejectWith(message) {
  return Promise.reject(new Error(message));
}

function delay(ms) {
  return new Promise(function (resolve) {
    setTimeout(resolve, ms);
  });
}

async function doubleAsync(n) {
  return n * 2;
}

async function fetchJSON(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error("Request failed: " + response.status);
  }

  return response.json();
}

async function getSongTitles(url) {
  const songs = await fetchJSON(url);
  return songs.map(function (song) {
    return song.title;
  });
}

async function getSongById(url, id) {
  const songs = await fetchJSON(url);
  const song = songs.find(function (song) {
    return song.id === id;
  });

  return song || null;
}

function fetchAll(urls) {
  return Promise.all(urls.map(function (url) {
    return fetchJSON(url);
  }));
}

async function safeFetch(url) {
  try {
    return await fetchJSON(url);
  } catch (error) {
    return null;
  }
}
