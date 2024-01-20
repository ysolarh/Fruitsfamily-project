const form = document.getElementById('signup-form');

form.onsubmit = function() {
    const userInfo = document.getElementsByTagName('input');
    const location = document.querySelector('.location').value;
    const infoArr = [];
    let i = 0;

    for (let i = 0; i < userInfo.length - 3; i++) {
        infoArr.push(userInfo[i].value);
    }
    infoArr.push(location);
    infoArr.push(userInfo[7].checked);
    infoArr.push(userInfo[8].checked);
    for (let i = 0; i < infoArr.length; i++) {
        console.log(infoArr[i]);
    }
    console.log(`email: ${infoArr[0]}, id: ${infoArr[1]}, pw1: ${infoArr[2]}, pw2: ${infoArr[3]}, phone1: ${infoArr[4]}, phone2: ${infoArr[5]}, phone3: ${infoArr[6]}, location: ${infoArr[7]}, isWoman: ${infoArr[8]}, isMan: ${infoArr[9]}`);
    // console.log(infoArr);
    return false;
}

// form.onsubmit = function() {
//     const email = document.getElementById('email');
//     const name = document.getElementsByName('name');
//     const password = document.getElementsByClassName('password');
//     const phone = document.querySelectorAll('.phone');
//     const location = document.querySelector('.location');
//     const gender = document.getElementsByName('gender');
    
//     console.log(email.value);
//     console.log(name[0].value);
//     console.log(password[0].value);
//     console.log(password[1].value);
//     console.log(phone[0].value);
//     console.log(phone[1].value);
//     console.log(phone[2].value);
//     console.log(location.value);
//     console.log(gender[0].checked);
//     console.log(gender[1].checked);
//     return false;
// }