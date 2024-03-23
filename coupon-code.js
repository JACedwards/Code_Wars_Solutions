


function checkCoupon(enteredCode, correctCode, currentDate, expirationDate){

    console.log('date parse', Date.parse(currentDate))

    if (enteredCode != correctCode || new Date(currentDate).valueOf()  > new Date(expirationDate).valueOf()) {
        return false;
    }
        
    return true;
      
    }
    
      
    console.log(checkCoupon('123','123','September 5, 2014','October 1, 2013'))

    // function checkCoupon(enteredCode, correctCode, currentDate, expirationDate){
   
    //     return enteredCode === correctCode || new Date(expirationDate)  > new Date(currentDate) 
                      
    //     }
        
          
    //     console.log(checkCoupon('123','123','September 5, 2014','October 1, 2013'))