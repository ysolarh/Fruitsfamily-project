const stopwatch = document.querySelector(".stopwatch");
const startBtn = document.querySelector(".start");
const stopBtn = document.querySelector(".stop");
const resetBtn = document.querySelector(".reset");

let time = 0;
let timeoutId;

function makeDoubleDigits(num) {
  return String(num).padStart(2, "0");
}

function getTime() {
  hour = Math.floor(time / (100 * 60 * 60));
  min = Math.floor((time / (100 * 60)) % 60);
  sec = Math.floor((time / 100) % 60);
  ms = Math.floor(time % 100);
  return `${makeDoubleDigits(hour)}:${makeDoubleDigits(min)}:${makeDoubleDigits(sec)}:${makeDoubleDigits(ms)}`;
}

function printTime() {
  stopwatch.innerText = `${getTime()}`;
}

stopwatch.innerText = `${getTime()}`;
function startStopwatch() {
  time += 1;
  printTime();
  stopStopwatch();
  timeoutId = setTimeout(startStopwatch, 10);
}

function stopStopwatch() {
  printTime();
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
}

function resetStopwatch() {
  stopStopwatch();
  time = 0;
  printTime();
}

function handleClick(e) {
  if (e.target.className == "start") {
    startStopwatch();
  } else if (e.target.className == "stop") {
    stopStopwatch();
  } else if (e.target.className == "reset") {
    resetStopwatch();
  }
}

startBtn.addEventListener("click", handleClick);
stopBtn.addEventListener("click", handleClick);
resetBtn.addEventListener("click", handleClick);
