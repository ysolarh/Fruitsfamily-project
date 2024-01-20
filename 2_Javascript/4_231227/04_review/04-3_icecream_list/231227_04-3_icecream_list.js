const listH2 = document.getElementById("icecream__list");
const addBtn = document.querySelector(".add");
const printBtn = document.querySelector(".print");
const listBtn = document.querySelector(".list");

const iceList = [];

addBtn.addEventListener("click", (e) => {
  const icecreamName = prompt("추가하고 싶은 아이스크림 이름 입력");
  iceList.push(icecreamName);
});

printBtn.addEventListener("click", () => {
  let i = 0;
  while (iceList[i]) {
    alert(`${iceList[i]}`);
    i++;
  }
});

listBtn.addEventListener("click", () => {
  listH2.textContent = iceList.join(", ");
});
