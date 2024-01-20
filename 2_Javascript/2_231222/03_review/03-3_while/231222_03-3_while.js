const multiple = document.querySelector('.multiple');

let i = 4;
while (i <= 500) {
    const arr = [];
    const line = document.createElement('div');
    j = 0;
    while (j < 5) {
        if (i > 500) 
            break
        arr.push(i);
        i += 4;
        j += 1
    }
    line.textContent = arr.join(' ');
    multiple.append(line);
}