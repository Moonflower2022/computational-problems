const fs = require("fs")

// Read the file synchronously
const filePath = "./puzzle_input.txt" // path to your puzzle_input.txt
const fileContent = fs.readFileSync(filePath, "utf-8")

// Split the content by lines and then each line by characters
const puzzle = fileContent.split("\n").map((line) => line.split(""))

function isSymbol(char) {
    return char !== "." && isNaN(parseInt(char))
}

function isNumber(value) {
    return typeof value === 'number' && !isNaN(value)
}

function getNeighbors(x, y, length) {
    let neighbors = []

    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
            if (0 <= x + i && x + i < length && 0 <= y + j && y + j < length) {
                neighbors.push([x + i, y + j])   
            }
        }
    }

    return neighbors
}

function isPartNumber(puzzle, indices) {
    for (let [i, j] of indices) {
        for (let [x, y] of getNeighbors(i, j, puzzle.length)) {
            if (isSymbol(puzzle[x][y])) {
                return true
            }
        }
    }
    return false
}

function getNumber(puzzle, indices) {
    let indicesCopy = indices.slice()
    let total = 0
    for (let [x, y] of indicesCopy.reverse()) {
        total +=
            parseInt(puzzle[x][y]) * 10 ** (indicesCopy[0][1] - y)
    }
    return total
}

let total = 0

for (let i = 0; i < puzzle.length; i++) {
    let j = 0
    while (j < puzzle[i].length) {
        if (isNumber(parseInt(puzzle[i][j]))) {
            let numberLength = 1
            let numberIndices = [[i, j]]
            while (
                j + numberLength < puzzle[i].length &&
                isNumber(parseInt(puzzle[i][j + numberLength]))
            ) {
                numberIndices.push([i, j + numberLength])
                numberLength++
            }
            console.log(getNumber(puzzle, numberIndices), isPartNumber(puzzle, numberIndices))

            total += isPartNumber(puzzle, numberIndices)
                ? getNumber(puzzle, numberIndices)
                : 0
            
            j += numberLength
        } else {
            j++
        }
    }
}

console.log("total:", total)