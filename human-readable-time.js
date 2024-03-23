function humanReadable (seconds) {
    let hours = Math.floor(seconds / 3600).toString().padStart(2,'0');
    seconds = seconds - (hours * 3600);
    
    let minutes = Math.floor(seconds / 60).toString().padStart(2, '0');
    
    seconds = (seconds - (minutes * 60)).toString().padStart(2, '0');

    return `${hours}:${minutes}:${seconds}`
    

  }

  console.log(humanReadable(3599))

  console.log(3599 % 60);

  //'00:59:00'


  function humanReadable(seconds) {
    var pad = function(x) { return (x < 10) ? "0"+x : x; }
    return pad(parseInt(seconds / (60*60))) + ":" +
           pad(parseInt(seconds / 60 % 60)) + ":" +
           pad(seconds % 60)
  }