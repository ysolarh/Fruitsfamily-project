const body = document.querySelector('body');
const carousel = document.querySelector('.carousel');
const numList = document.querySelectorAll('.number');

let idx = 0;
const maxIdx = 2;

function darkmode() {
    body.classList.toggle("active");
    for(let i = 0; i < numList.length; i++) {
        numList[i].classList.toggle("active");
    }
}

function switchImage(idx) {
    carousel.style.transform = `translate3d(-${500 * idx}px, 0, 0)`;
}

function clickPrev() {
    if (idx === 0) {
        idx = maxIdx;
    }
    else {
        idx -= 1;
    }
    switchImage(idx);
}

function clickNext() {
    if (idx === maxIdx) {
        idx = 0;
    }
    else {
        idx += 1;
    }
    switchImage(idx)
}

function clickButton(number) {
    idx = number - 1;
    switchImage(idx);
}