
function checkDigit(n){
    while (n > 10){
        curr_sum  = 0
        str_n = n.toString()
        for(var i = 0; i < str_n.length; i++){
            curr_sum += parseInt(str_n[i])
        }
        n = curr_sum
    }
    return n
}

console.log(checkDigit(12345))