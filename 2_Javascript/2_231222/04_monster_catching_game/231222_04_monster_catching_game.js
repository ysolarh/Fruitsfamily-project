let monsterHP = 100;
let attackDamage = parseInt(prompt("1회 공격시 데미지는? (양의 정수)"));
let countAttack = 0;
const container = document.getElementById("container");
const h1 = document.createElement("h1");

if (attackDamage > 0) {
  h1.textContent = "몬스터 잡기 게임을 시작합니다!";
  container.append(h1);
  while (monsterHP > 0) {
    monsterHP -= attackDamage;
    countAttack += 1;
    if (monsterHP < 0) {
      monsterHP = 0;
    }
    const p = document.createElement("p");
    const strong = document.createElement("strong");
    p.textContent = `몬스터를 ${countAttack}회 공격했다!`;
    strong.textContent = `몬스터의 남은 HP은 ${monsterHP}입니다!`;
    container.append(p, strong);
  }
  const h2 = document.createElement("h2");
  h2.textContent = "몬스터 잡기 완료! 수고하셨습니다!";
  h2.style.color = "red";
  h2.title = "게임을 다시 시작하고 싶으면 새로고침하세요.";
  container.append(h2);
} else {
  alert("데미지는 양의 정수만 가능! 다시 입력하세요.");
  h1.textContent = "새로고침하고 다시 시작하세요!";
  container.append(h1);
}
