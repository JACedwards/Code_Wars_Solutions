//https://stackoverflow.com/questions/66000005/how-to-create-a-range-of-numbers-from-1-to-5-in-an-array

//cata name:  Don't give me five!
function dontGiveMeFive(start, end) {

   let count = 0

   for (let i = start; i <= end; i++)

      if (!/5/.test(i)) {
         
         count += 1
      }

      return count;

   }
   

console.log(dontGiveMeFive(4,17))

// function dontGiveMeFive(start, end) {

//    let count = start;
//    let char = ''
//    let output = [];


//    while (count <= end ) {
//       char = count.toString()

//       if (char.indexOf('5') === -1) {
//          output.push(char);
//       }

//       count += 1
//    }
   
//    return output.length;
// }

// console.log(dontGiveMeFive(4,17))


// function dontGiveMeFive(start, end) {

//    let count = start;
//    let arr = [];

//    while (count <= end ) {

//       arr.push(count);
//       count += 1
//    }
//    arr = arr.map((e) => e.toString());
//    let output = [];

//    for (let i = 0; i < arr.length; i++) {
   
//       if (arr[i].indexOf('5') === -1) {
//          output.push(arr[i]);
//       }
//    }
//    return output.length;
// }

// console.log(dontGiveMeFive(4,17))
