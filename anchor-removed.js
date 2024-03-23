function removeUrlAnchor(url){
    return url.indexOf('#') == -1 ? url : url.slice(0, url.indexOf('#'));
}


//   console.log(removeUrlAnchor("www.codewars.com#234"))


function removeUrlAnchor(url){
    return url.split('#')[0];
  }


  console.log(removeUrlAnchor("www.codewars.com"))