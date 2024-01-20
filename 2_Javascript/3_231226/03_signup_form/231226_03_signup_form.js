const form = document.getElementById("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  // const userId = e.target[0].value; // 이것도 됨.
  const userId = e.target.id.value;
  const userPw1 = e.target.pw1.value;
  const userPw2 = e.target.pw2.value;
  const userName = e.target.name.value;
  const userPhone = e.target.phone.value;
  const userPosition = e.target.position.value;

  if (userPw1 !== userPw2) {
    alert("비밀번호가 틀렸습니다.");
    return;
  }

  // document.body.innerHTML = "";
  document.write(`
    <h1>${userId}님 환영합니다.</h1>
    <p>회원 가입 시 입력하신 내역은 다음과 같습니다.</p>
    <ul>
      <li>아이디: ${userId}</li>
      <li>이름: ${userName}</li>
      <li>전화번호: ${userPhone}</li>
      <li>원하는 직무: ${userPosition}</li>
    </ul>
    `);
});
