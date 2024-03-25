
function moveZeros(arr) {

    let noZeros = arr.filter((e) => e !== 0);

    return [...noZeros, ...Array(arr.length - noZeros.length).fill(0)];

  }

console.log(moveZeros([false,1,0,1,2,0,1,3,"a"]))

//Array.concat version.
// function moveZeros(arr) {

//     let noZeros = arr.filter((e) => e !== 0);

//     return noZeros.concat(Array(arr.length - noZeros.length).fill(0));

//   }

// console.log(moveZeros([false,1,0,1,2,0,1,3,"a"]))

// function moveZeros(arr) {

//     let output = arr.filter((e) => e !== 0);

//     let zeros = Array(arr.length - output.length).fill(0);
     

//     output = output.concat(zeros)


//     return output;
//   }

// console.log(moveZeros([false,1,0,1,2,0,1,3,"a"]))
//moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

//long version
// function moveZeros(arr) {

//     let output = [];
//     let zeroCount = 0;
    
//     for (let i = 0; i < arr.length; i++) {

//         if (arr[i] !== 0) {
//             output.push(arr[i]);
//         }
//         else {

//             zeroCount +=1
//         }

//     }

//     for (let j = 0; j < zeroCount; j++) {
//         output.push(0);
//     }

//     return output;
//   }

// console.log(moveZeros([false,1,0,1,2,0,1,3,"a"]))
