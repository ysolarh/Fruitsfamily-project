const result = document.querySelector(".result");
let restart = false;
let buffer = "";

function inputClear() {
  buffer = "";
  result.value = "";
}

function input(strValue) {
  if (restart) {
    inputClear();
    restart = false;
  }
  buffer += strValue;
  result.value += strValue;
}

function inputEq() {
  let func = new Function("return " + buffer);
  result.value = func();
  restart = true;
}
