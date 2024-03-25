function domainName(url){
    if (url.indexOf('www') !== -1) {

        return url.slice(12, url.indexOf('.com'))
    }
    else {
        return url.slice(8, url.indexOf('.com'))
    }
}

console.log(domainName('https://gooober.com'))
