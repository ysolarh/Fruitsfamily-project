const one = document.querySelector('.one_result');
const two = document.querySelector('.two_result');
const three = document.querySelector('.three_result');

for (let i = 1; i <= 5; i += 1) {
    const box = document.createElement('div');
    box.textContent = '';
    for (let j = 1; j <= i; j += 1) {
        box.textContent += '*';
    }
    one.append(box);
}

for (let i = 1; i <= 5; i += 1) {
    const box = document.createElement('div');
    box.textContent = '';
    for (let j = 1; j <= i; j += 1) {
        box.textContent += '*';
    }
    two.append(box);
}
for (let i = 5; i >= 1; i -= 1) {
    const box = document.createElement('div');
    box.textContent = '';
    for (let j = 1; j <= i; j += 1) {
        box.textContent += '*';
    }
    two.append(box);
}

for (let i = 1; i <= 5; i += 1) {
    const box = document.createElement('div');
    box.textContent = '';
    for (let j = 1; j <= 5 - i ; j += 1){
        box.textContent += '\u00A0';
    }
    for (let j = 1; j <= i * 2 - 1; j += 1) {
        box.textContent += '*';
    }
    three.append(box);
}
for (let i = 4; i >= 1; i -= 1) {
    const box = document.createElement('div');
    box.textContent = '';
    for (let j = 1; j <= 5 - i ; j += 1){
        box.textContent += '\u00A0';
    }
    for (let j = 1; j <= i * 2 - 1; j += 1) {
        box.textContent += '*';
    }
    three.append(box);
}