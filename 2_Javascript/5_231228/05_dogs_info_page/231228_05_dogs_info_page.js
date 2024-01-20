const apiRandomDogs = "https://dog.ceo/api/breeds/image/random/45";
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all";

const main = document.getElementById("main");
const filterInput = document.getElementById("filter-text");
const filterButton = document.getElementById("filter-button");
const filterSelect = document.getElementById("filter-select");
const reset = document.getElementById("reset");
const more = document.getElementById("more");
const tothetop = document.getElementById("tothetop");

let request1;
let request2;
let currentDogs = [];

function displayDogs(item) {
  const dogImgDiv = document.createElement("div");
  dogImgDiv.classList.add("flex-item");
  dogImgDiv.innerHTML = `<img src=${item}>`;
  main.appendChild(dogImgDiv);
}

function parseResponse() {
  const response = JSON.parse(request1.response);
  response.message.forEach((item) => {
    currentDogs.push(item);
    displayDogs(item);
  });
}

window.addEventListener("load", () => {
  // 개 사진 불러오기
  request1 = new XMLHttpRequest();
  request1.open("get", apiRandomDogs);
  request1.addEventListener("load", () => {
    parseResponse();
  });
  request1.send();

  // select에 견종 채우기
  request2 = new XMLHttpRequest();
  request2.open("get", apiAllBreeds);
  request2.addEventListener("load", () => {
    const response = JSON.parse(request2.response);
    Object.keys(response.message).forEach((item) => {
      const option = document.createElement("option");
      option.textContent = item;
      option.value = item;
      filterSelect.appendChild(option);
    });
  });
  request2.send();
});

// 검색하기
filterButton.addEventListener("click", () => {
  main.innerHTML = "";
  const filteredDogs = currentDogs.filter((item) => {
    return item.indexOf(filterInput.value) !== -1;
  });
  filterInput.value = "";
  filteredDogs.forEach((item) => {
    displayDogs(item);
  });
});

// 선택하기
filterSelect.addEventListener("change", () => {
  main.innerHTML = "";
  const filteredDogs = currentDogs.filter((item) => {
    return item.indexOf(filterSelect.value) !== -1;
  });
  filteredDogs.forEach((item) => {
    displayDogs(item);
  });
});

// 새로운 세트 불러오기
reset.addEventListener("click", () => {
  request1 = new XMLHttpRequest();
  request1.open("get", apiRandomDogs);
  request1.addEventListener("load", () => {
    main.innerHTML = "";
    currentDogs = [];
    parseResponse();
  });
  request1.send();
  filterSelect.value = "All";
});

// 더 불러오기
more.addEventListener("click", () => {
  request1 = new XMLHttpRequest();
  request1.open("get", apiRandomDogs);
  request1.addEventListener("load", () => {
    parseResponse();
  });
  request1.send();
});

// 맨 위로 이동
tothetop.addEventListener("click", () => {
  window.scrollTo({ top: 0 });
});
