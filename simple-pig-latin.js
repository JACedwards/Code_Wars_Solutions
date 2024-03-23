function pigIt(str){

    str = str.split(' ');
    let pigified = '';
    let pigArr = [];
    let regex = /\p{P}/gu;
    
    for (let i = 0; i < str.length; i++) {
        console.log(`${str[i].slice(1)}${str[i][0]}ay`)


        if (regex.test(str[i])) {
            pigified = str[i];
        }
        else {

            pigified = `${str[i].slice(1)}${str[i][0]}ay` // is
        }
        pigArr.push(pigified);
    }
    return pigArr.join(' ');

}

console.log(pigIt('Hello World !'))