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

const numScratchcards = scratchcards.length

let counts = Array(numScratchcards).fill(1)

for (let [i, [winningNumbers, myNumbers]] of scratchcards.entries()) {
    let numWinningNumbers = 0

    for (let winningNumber of winningNumbers) {
        if (myNumbers.includes(winningNumber)) {
            numWinningNumbers += 1
        }
    }
    
    for (let j = 1; j < numWinningNumbers + 1; j++) {
        if (i + j < numScratchcards) {
            counts[i + j] += counts[i]
        }
    }
}

console.log(counts.reduce((a, b) => a + b, 0))