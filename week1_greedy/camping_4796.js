const dayInRow = 8;
const availableDay = 5;
const holiday = 17;
let usedDay;

function main() {
    usedDay = parseInt(holiday / dayInRow) * availableDay;

    if (holiday % dayInRow > 0) {
        usedDay += holiday % dayInRow;
    }
    console.log(usedDay);
}

main();