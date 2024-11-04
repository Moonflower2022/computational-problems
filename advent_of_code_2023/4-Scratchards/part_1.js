const fs = require("fs")

// Read the file synchronously
const filePath = "./puzzle_input.txt" // path to your puzzle_input.txt
const fileContent = fs.readFileSync(filePath, "utf-8")

const scratchcards = fileContent.split("\n").map((line) =>
    line
        .slice(9)
        .split("|")
        .map((side) => side.trim().split(/\s+/).map((numberString) => parseInt(numberString)))
)

let total = 0

for (let [winningNumbers, myNumbers] of scratchcards) {

    let scratchcardTotal = 0

    for (let winningNumber of winningNumbers) {
        if (myNumbers.includes(winningNumber)) {
            scratchcardTotal += 1
        }
    }
    
    if (scratchcardTotal > 0) {
        total += 2 ** (scratchcardTotal - 1)
    }
}

console.log(total)