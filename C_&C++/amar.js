function get_count(list){
    let playerOneWins = 0;
    let playerTwoWins = 0;
    for(let num of list){
        if (num ===1){
            playerOneWins++;
        }
        else{
            playerTwoWins++;
        }
    }
    if(playerTwoWins < playerOneWins){
        return playerOneWins;
    }else{
        return playerTwoWins;
    }

}
console.log(get_count([1,2,2,1,1]))
console.log(get_count([1,2,1,2,2,2,1]))
console.log(get_count([1,2,1,2]))