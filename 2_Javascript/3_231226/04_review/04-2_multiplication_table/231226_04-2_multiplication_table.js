const td = document.querySelectorAll("td");

function multiply(num) {
  for (let i = 1; i <= 9; i++) {
    const p = document.createElement("p");
    p.textContent = `${num} * ${i} = ${num * i}`;
    td[num - 2].append(p);
  }
}

for (let i = 2; i <= 9; i++) {
  multiply(i);
  console.log(i);
}
