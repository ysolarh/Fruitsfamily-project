const todaySpan = document.getElementById("today");
const numbersDiv = document.querySelector(".numbers");
const drawBtn = document.getElementById("draw");
const resetBtn = document.getElementById("reset");

const lotto = [];
let randNum;

const todayDate = new Date();
const year = todayDate.getFullYear();
const month = todayDate.getMonth() + 1;
const date = todayDate.getDate();

todaySpan.textContent = `${year}년 ${month}월 ${date}일 `;

function printNum(num) {
  const lottoNumDiv = document.createElement("div");
  lottoNumDiv.classList.add("lotto__num");
  lottoNumDiv.textContent = num;
  numbersDiv.append(lottoNumDiv);
}

drawBtn.addEventListener("click", () => {
  numbersDiv.innerHTML = "";
  lotto.splice(0, 6);
  while (lotto.length < 6) {
    randNum = Math.floor(Math.random() * 45) + 1;
    if (lotto.indexOf(randNum) === -1) {
      lotto.push(randNum);
      printNum(randNum);
    }
  }
});

resetBtn.addEventListener("click", () => {
  numbersDiv.innerHTML = "";
  lotto.splice(0, 6);
});
