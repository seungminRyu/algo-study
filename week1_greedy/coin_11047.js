const qeury = "node ./week1_greedy/coin_11047.js"

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let input = [];
    
    rl.on('line', function (line) {
        input = line.split(' ').map((el) => parseInt(el));
    })
    .on('close', function () {
        cal(input[0], input[1]);
        process.exit();
    });
}

function cal(_typeNum, _amount) {
    const typeNum = _typeNum;
    let amount = _amount;
    let coinType = [];
    let divCnt = 0;
    
    for (let i = 0; i < typeNum; i++) {
        if (i === 0) {
            coinType.push(1);
        } else if (i%2 === 0) {
            coinType.push(coinType[i-1]*2);
        } else {
            coinType.push(coinType[i-1]*5);
        }
    }
    
    for (let i = typeNum; i > 0; i--) {
        if (amount >= coinType[i-1]) {
            while(amount >= coinType[i-1]) {
                amount = amount - coinType[i-1];
                divCnt++;
            };
        }
    }
   
    console.log(divCnt);      
}

main();