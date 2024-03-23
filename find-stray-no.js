function stray(numbers) {
    let numArr = Array.from(new Set (numbers));

    return numbers.filter((e) => e == numArr[0]).length === 1 ? numArr[0] : numArr[1]
       
}

console.log(stray([1,1,2]))


// function stray(numbers) {
//     let numArr = Array.from(new Set (numbers));

//     return numArr[0] == numbers[0] && numArr[0] == numbers[1] ? numArr[1] : numArr[0]
       
// }

// console.log(stray([1,1,2]))

function stray(numbers){
    for (var i in numbers){
       if (numbers.indexOf(numbers[i]) === numbers.lastIndexOf(numbers[i])){return numbers[i]}
    }
  }