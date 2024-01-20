const reportTable = document.getElementById("report");
const highScoreStH2 = document.getElementById("high-score");

const tableValue = Array.from(reportTable.rows).slice(1);
// const scores = {};
const highScoreStudents = [];

// tableValue -> scores
// tableValue.forEach((item) => {
//   scores[item.cells[0].innerHTML] = parseInt(item.cells[1].innerHTML);
// });

// 75점 이상 추출
// for (const name in scores) {
//   if (scores[name] >= 75) {
//     highScoreStudents.push([name, scores[name]]);
//   }
// }

// 75점 이상 추출
tableValue.forEach((item) => {
  let cell0 = item.cells[0].innerHTML;
  let cell1 = parseInt(item.cells[1].innerHTML);
  if (cell1 >= 75) {
    highScoreStudents.push([cell0, parseInt(cell1)]);
  }
});

// 점수 높은 순으로 나열
highScoreStudents.sort((a, b) => {
  return b[1] - a[1];
});

// 화면에 출력
for (const name of highScoreStudents) {
  highScoreStH2.textContent += name[0] + " ";
}
