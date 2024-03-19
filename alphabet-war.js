function alphabetWar(fight)
{
   let left = {'w':4, 'p':3, 'b':2, 's': 1};
   let right = {'m': 4, 'q':3, 'd':2, 'z': 1};
   let leftCount = 0;
   let rightCount = 0;

   for (let i = 0; i < fight.length; i++) {
    

        if (left.hasOwnProperty(fight[i])) {
            leftCount = leftCount + left[fight[i]]
        }
        
        else if (right.hasOwnProperty(fight[i])) {
            rightCount = rightCount + right[fight[i]]
        }

        else {
            continue;
        }
   }

//    if (leftCount == rightCount) {
//     return "Let's fight again!" 
//     }

//     return leftCount < rightCount ? 'Right side wins!' : 'Left side wins!';

   return leftCount < right


}


console.log(alphabetWar("nqsgbqcwmfb"));