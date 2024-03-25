function firstNonRepeatingLetter(s) {
    if (s.length == 1) {
        return s
    }

    let sLower = s.toLowerCase()
    let lowerSet = new Set (sLower);
    
    if (lowerSet.size == 1 || s.length == 0) {
        return '';
    }
    
    let currentSlice = '';
    
    for (let i = 0; i <= s.length; i++) {

        currentSlice = `${sLower.slice(0,i)}${sLower.slice(i+1)}`;
        // console.log(currentSlice);
        // // console.log(currentSlice.indexOf(s[i]))
        // console.log(s[i])
        if(currentSlice.indexOf(s[i]) == -1) {
            return s[i]
        }
    }

}

console.log(firstNonRepeatingLetter('aaAaa'))  //'T'

// function firstNonRepeatingLetter(s) {
//     sLower = s.toLowerCase()
    
//     for (let i = 0; i <= s.length; i++) {

//         if((sLower.slice(i+1)).indexOf(s[i]) == -1) {
//             return s[i]
//         }
//     }

// }

// console.log(firstNonRepeatingLetter('moonmen'))  //'T'