const num = 5;
const rates = [ 
    { a: 3, b: 2 },
    { a: 1, b: 4 },
    { a: 4, b: 1 },
    { a: 2, b: 3 },
    { a: 5, b: 5 },
];

const a = rates[0].a;

function cal(one, others) {
    let i;
    for (i=0; i<num; i++) {
        if(one < others ) {
            break;
        }
    }

    if (i === num) {
        return true;
    } else {
        return false;
    }
}

for (let i=0; i<num; i++) {
    
}