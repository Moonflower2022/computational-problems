const fs = require("fs")

// Read the file synchronously
const filePath = "./puzzle_input.txt" // path to your puzzle_input.txt
const fileContent = fs.readFileSync(filePath, "utf-8")

// Split the content by lines and then each line by characters
const puzzle = fileContent.split("\n").map((line) => line.split(""))

function isNumber(value) {
    return typeof value === "number" && !isNaN(value)
}

function getLayeredNeighbors(x, y, length) {
    let layeredNeighbors = [[], [], []]

    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
            if (
                0 <= x + i &&
                x + i < length &&
                0 <= y + j &&
                y + j < length &&
                !(i === 0 && j === 0)
            ) {
                layeredNeighbors[i + 1].push([x + i, y + j])
            }
        }
    }

    return layeredNeighbors
}

function extendNumber(startIndices, puzzle) {
    let newIndices = [...startIndices]

    while (
        0 <= newIndices[0][1] - 1 &&
        isNumber(parseInt(puzzle[newIndices[0][0]][newIndices[0][1] - 1]))
    ) {
        newIndices.unshift([newIndices[0][0], newIndices[0][1] - 1])
    }

    while (
        newIndices[newIndices.length - 1][1] + 1 < puzzle.length &&
        isNumber(
            parseInt(
                puzzle[newIndices[newIndices.length - 1][0]][
                    newIndices[newIndices.length - 1][1] + 1
                ]
            )
        )
    ) {
        newIndices.push([
            newIndices[newIndices.length - 1][0],
            newIndices[newIndices.length - 1][1] + 1,
        ])
    }

    return newIndices
}

function getConsecutiveNumbers(indices, puzzle) {
    let result = []
    let currentGroup = []

    // Iterate over the list of indices
    for (let i = 0; i < indices.length; i++) {
        const [x, y] = indices[i]

        if (isNumber(parseInt(puzzle[x][y]))) {
            currentGroup.push([x, y]) // Add to current group if it's a number
        } else {
            // If not a number and there's a current group with two or more numbers, push it to the result
            if (currentGroup.length >= 2) {
                result.push([...currentGroup])
            }
            currentGroup = [] // Reset the current group
        }
    }

    // Check if there's a valid group remaining after the loop
    if (currentGroup.length >= 2) {
        result.push([...currentGroup])
    }

    // Return any individual number indices as well, if not part of a group
    for (let i = 0; i < indices.length; i++) {
        const [x, y] = indices[i]
        if (
            isNumber(parseInt(puzzle[x][y])) &&
            !result.flat().some(([a, b]) => a === x && b === y)
        ) {
            result.push([[x, y]])
        }
    }

    return result
}

function getNumber(indices, puzzle) {
    let indicesCopy = indices.slice()
    let total = 0
    for (let [x, y] of indicesCopy.reverse()) {
        total += parseInt(puzzle[x][y]) * 10 ** (indicesCopy[0][1] - y)
    }
    return total
}

let total = 0

for (let i = 0; i < puzzle.length; i++) {
    for (let j = 0; j < puzzle[i].length; j++) {
        if (puzzle[i][j] === "*") {
            let layeredNeighbors = getLayeredNeighbors(i, j, puzzle.length)
            let topConsecutiveNumbers = getConsecutiveNumbers(
                layeredNeighbors[0],
                puzzle
            )
            let bottomConsecutiveNumbers = getConsecutiveNumbers(
                layeredNeighbors[2],
                puzzle
            )

            if (
                topConsecutiveNumbers.length +
                    bottomConsecutiveNumbers.length +
                    isNumber(
                        parseInt(
                            puzzle[layeredNeighbors[1][0][0]][
                                layeredNeighbors[1][0][1]
                            ]
                        )
                    ) +
                    isNumber(
                        parseInt(
                            puzzle[layeredNeighbors[1][1][0]][
                                layeredNeighbors[1][1][1]
                            ]
                        )
                    ) ===
                2
            ) {
                let gearRatio = 1
                for (let numberGroup of [
                    ...topConsecutiveNumbers,
                    ...bottomConsecutiveNumbers,
                ]) {
                    console.log(
                        getNumber(extendNumber(numberGroup, puzzle), puzzle)
                    )
                    gearRatio *= getNumber(
                        extendNumber(numberGroup, puzzle),
                        puzzle
                    )
                }
                for (let [x, y] of layeredNeighbors[1]) {
                    if (isNumber(parseInt(puzzle[x][y]))) {
                        console.log(
                            getNumber(extendNumber([[x, y]], puzzle), puzzle)
                        )
                        gearRatio *= getNumber(
                            extendNumber([[x, y]], puzzle),
                            puzzle
                        )
                    }
                }
                total += gearRatio
            }
        }
    }
}

// find gears (done)
// for each gear, get neighbors
// check redundant neighbors
// if there are two, get numbers and return prod

console.log("total:", total)
