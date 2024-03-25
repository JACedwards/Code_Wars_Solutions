function scramble(str1, str2) {
   for (let i = 0; i < str2.length; i++){

        console.log('string1 before', str1);
        console.log(str1.indexOf(str2[i]))
        if (str1.indexOf(str2[i]) == -1) {
            return false;
        }

        else {
            str1 = str1.replace(str2[i], '');
        }
   }
   return true;
}

  
  console.log(scramble('cedewaraaossoqqyt', 'codewars'))

  