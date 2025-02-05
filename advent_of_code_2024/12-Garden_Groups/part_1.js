import { DisjointSet, elementsEqual } from "./disjoint_set.js"
import fs from "fs"

function incrementPerimiters(perimiters, key, amount) {
    if (key in perimiters) {
        perimiters[key] += amount
    } else {
        perimiters[key] = amount
    }
}

function getPerimiter(location, disjointSet) {
    let perimiter = 0
    const differences = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for (const [dy, dx] of differences) {
        const new_location = [location[0] + dy, location[1] + dx]
        const inPuzzle = 0 <= new_location[0] && new_location[0] < puzzle.length && 0 <= new_location[1] && new_location[1] < puzzle[0].length
        if (inPuzzle) {
            const isNotSame = !elementsEqual(disjointSet.findRepresentative(new_location), disjointSet.findRepresentative(location))
            if (isNotSame) perimiter += 1
        } else {
            perimiter += 1
        }
    }
    return perimiter
}

function getPerimiters(disjointSet) {
    let perimiters = {}
    for (const key of Object.keys(disjointSet.parents)) {
        const location = key.split(",").map((string) => parseInt(string))
        const perimiter = getPerimiter(location, disjointSet)
        
        incrementPerimiters(perimiters, disjointSet.findRepresentative(key), perimiter)
    }
    return perimiters
}

const filePath = "./puzzle_input.txt" // path to your puzzle_input.txt
const fileContent = fs.readFileSync(filePath, "utf-8")

const puzzle = fileContent.split("\n").map((line) => line.split(""))

// start by getting all positions, make set for each
// from a corner, check in waves like
// #$%
// $$%
// %%%
// with each checking if it is the same symbol with the thing to the right and the thing to the bottom
// for last layer, only check bottom
// area is easy, how to get perimiter?

const disjointSet = new DisjointSet()

for (let y = 0; y < puzzle.length; y += 1) {
    for (let x = 0; x < puzzle[0].length; x += 1) {
        disjointSet.makeSet([y, x])
    }
}
for (let y = 0; y < puzzle.length; y += 1) {
    for (let x = 0; x < puzzle[0].length; x += 1) {
        if (y === puzzle.length - 1 && x === puzzle[0].length - 1) {
            continue
        }
        if (y === puzzle.length - 1) {
            if (puzzle[y][x] === puzzle[y][x + 1]) {
                disjointSet.union([y, x], [y, x + 1])
            }
            continue
        }

        if (x === puzzle[0].length - 1) {
            if (puzzle[y][x] === puzzle[y + 1][x]) {
                disjointSet.union([y, x], [y + 1, x])
            }
            continue
        }
        if (puzzle[y][x] === puzzle[y][x + 1]) {
            disjointSet.union([y, x], [y, x + 1])
        }
        if (puzzle[y][x] === puzzle[y + 1][x]) {
            disjointSet.union([y, x], [y + 1, x])
        }
    }
}

const perimiters = getPerimiters(disjointSet)

console.log("sizes:", disjointSet.sizes)
console.log("perimeters:", perimiters)
 
let totalPrice = 0

for (const key of Object.keys(perimiters)) {
    totalPrice += perimiters[key] * disjointSet.sizes[key]
}

console.log(totalPrice)