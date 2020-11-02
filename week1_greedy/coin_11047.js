const TYPENUM = 10;
const AMOUNT = 4200;
let coinType = [];
let divCnt = 0;

for (let i = 0; i < TYPENUM; i++) {
    if (i === 0) {
        coinType.push(1);
    } else if (i%2 === 0) {
        coinType.push(coinType[i-1]*2);
    } else {
        coinType.push(coinType[i-1]*5);
    }
}

for (let i = TYPENUM-1; i >= 0; i--) {
    if (AMOUNT >= coinType[i]) {
        while(AMOUNT % coinType[i])
    }
}