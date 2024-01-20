const stopBtn = document.querySelector(".stop");
const startBtn = document.querySelector(".start");
const images = document.querySelectorAll(".img");

function changeImg() {
  const randNum = Math.floor(Math.random() * 3);
  images[randNum].classList.add("on");
  for (let i = 0; i < images.length; i++) {
    if (i !== randNum) {
      images[i].classList.remove("on");
    }
  }
}

let intervalId;
startBtn.addEventListener("click", () => {
  intervalId = setInterval(changeImg, 10);
  stopBtn.classList.toggle("display");
  startBtn.classList.toggle("display");
});

stopBtn.addEventListener("click", () => {
  clearInterval(intervalId);
  stopBtn.classList.toggle("display");
  startBtn.classList.toggle("display");
});
