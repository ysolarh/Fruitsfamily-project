const currTime = document.getElementById("curr_time");
const timer = document.getElementById("timer");

function countdown() {
  const now = new Date();
  const yearEnd = Date.parse("2024/01/01 00:00:00");
  const diff = yearEnd - now;
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor(diff / (1000 * 60 * 60));
  const mins = Math.floor(diff / (1000 * 60));
  const secs = Math.floor(diff / 1000);
  const h = hours - days * 24;
  const m = mins - hours * 60;
  const s = secs - mins * 60;

  currTime.innerText = `현재 날짜와 시간: ${now}`;
  timer.innerText = `올해의 남은 시간: ${days}일 ${h}시간 ${m}분 ${s}초 남았습니다.`;
}

setInterval(countdown, 1000);
