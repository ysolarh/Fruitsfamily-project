const form = document.getElementById("input__form");
const hint = document.querySelectorAll(".hint");
const retryBtn = document.querySelector(".retry__btn");
const randNum = Math.floor(Math.random() * 100 + 1);

function clickBtn() {
  const inputNum = document.querySelector(".input__num").value;
  let inputIntNum = parseInt(inputNum);

  if (inputIntNum > 100 || inputIntNum < 0) {
    hint[0].style.display = "none";
    hint[1].style.display = "none";
    hint[2].style.display = "block";
  } else {
    if (inputIntNum === randNum) {
      alert("정답!");
      retryBtn.style.display = "block";
      hint[0].style.display = "none";
      hint[1].style.display = "none";
      hint[2].style.display = "none";
    } else if (inputIntNum < randNum) {
      hint[0].style.display = "block";
      hint[1].style.display = "none";
      hint[2].style.display = "none";
    } else {
      hint[0].style.display = "none";
      hint[1].style.display = "block";
      hint[2].style.display = "none";
    }
  }
  return false;
}

function clickReset() {
  location.reload();
  return false;
}
