// 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정합니다.
// 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리르 작성해 볼 수 있음
const data = [
  // { category: "상의", brand: "Supreme", product: "슈프림 박스로고 후드티", price: "390,000"},
  // { category: "하의", brand: "DIESEL", product: "디젤 트랙 팬츠", price: "188,000" },
  // { category: "신발", brand: "Nike", product: "에어포스 1", price: "137,000" },
  // { category: "패션잡화", brand: "Music&Goods", product: "키링", price: "29,000" },
  // ...
  { category: "상의", brand: "nike", product: "nike 상의", price: 123, url: "http://www.naver.com" },
];

const base_url = "https://fruitsfamily.com/";
const category_url = base_url + "discover/product/";
const brand_url = base_url + "brand/";

const dateH3 = document.querySelector(".date");
const dataTable = document.getElementById("data-table");

const today = new Date();
dateH3.innerHTML = `
  ${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(today.getDate()).padStart(2, "0")}
`;

function handle_checkbox(item_id) {
  const itemTr = document.querySelector(`.item${item_id}`);
  itemTr.classList.toggle("checked-item");
}

// data.forEach((item) => {
//   const row = dataTable.insertRow();
//   row.insertCell(0).innerHTML = "<input type='checkbox'>";
//   row.insertCell(1).innerHTML = `<a href=${\{\{category_url + item.category\}\}} target='_blank'>${{{item.category}}}</a>`;
//   row.insertCell(2).innerHTML = `<a href=${brand_url + item.brand} target='_blank'>${item.brand}</a>`;
//   row.insertCell(3).innerHTML = `<a href=${item.link} target='_blank'>${item.product}</a>`;
//   row.insertCell(4).innerHTML = item.price;
// });
