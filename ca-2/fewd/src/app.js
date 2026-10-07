/*
 * Module 2 Practice Assessment — Task Tracker data utilities
 * ------------------------------------------------------------------
 * Implement the 10 functions below. Each one is checked by a Jasmine
 * spec in tests/FunctionsTest.js (10 specs x 2 marks = 20).
 *
 * A "task" is a plain object shaped like:
 *   { title: "Buy milk", status: "todo", done: false, priority: "high" }
 *
 * Rules:
 *   - Do NOT rename the functions and do NOT change their parameters.
 *   - Do NOT edit index.html, main.css, or tests/FunctionsTest.js.
 *   - Keep each function pure: return a value, do not print or mutate
 *     the inputs unless the task explicitly says to.
 * ------------------------------------------------------------------
 */

// 1. greet(name) -> a greeting built with a TEMPLATE LITERAL.
//    greet("Aisha") must return exactly:  "Hi, Aisha! Welcome back."
function greet(name) {
  return `Hi, ${name}! Welcome back.`;
}

// 2. isPassing(score) -> true if score is 40 or more, else false.
function isPassing(score) {
  return score >= 40;
}

// 3. sumScores(scores) -> the sum of all numbers in the array.
//    sumScores([]) must return 0.
function sumScores(scores) {
  return scores.reduce((total, score) => total + score, 0);
}

// 4. highScores(scores, min) -> a NEW array with only the scores
//    strictly greater than min.  highScores([10,50,90], 40) -> [50,90]
function highScores(scores, min) {
  return scores.filter(score => score > min);
}

// 5. titles(tasks) -> an array of every task's .title, in order.
function titles(tasks) {
  return tasks.map(task => task.title);
}

// 6. countByStatus(tasks, status) -> how many tasks have that .status.
function countByStatus(tasks, status) {
  return tasks.filter(task => task.status === status).length;
}

// 7. toggleDone(task) -> a NEW task object identical to the input but
//    with .done flipped. The ORIGINAL object must not be changed.
function toggleDone(task) {
  return { ...task, done: !task.done };
}

// 8. longestTitle(tasks) -> the single .title string with the most
//    characters. Assume at least one task; ties may return either.
function longestTitle(tasks) {
  return tasks.reduce((longest, task) =>
    task.title.length > longest.length ? task.title : longest
  );
}

// 9. averageScore(scores) -> the average of the numbers.
//    averageScore([]) must return 0 (do not divide by zero).
function averageScore(scores) {
  if (scores.length === 0) {
    return 0;
  }

  return sumScores(scores) / scores.length;
}

// 10. formatTask(task) -> a display line built with a TEMPLATE LITERAL:
//     done tasks start with "[x] ", not-done with "[ ] ", then the
//     title, then " (priority)".
//     { title:"Ship", done:true, priority:"low" } -> "[x] Ship (low)"
function formatTask(task) {
  const marker = task.done ? "[x]" : "[ ]";
  return `${marker} ${task.title} (${task.priority})`;
}
