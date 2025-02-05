import { DisjointSet } from "./disjoint_set.js"
import fs from "fs"

function getSideInfos(disjointSet) {
    let sideInfos = {}
    for (const key of Object.keys(disjointSet.parents)) {
        const location = key.split(",").map((string) => parseInt(string))

        if (!(disjointSet.findRepresentative(location) in sideInfos)) {
            sideInfos[disjointSet.findRepresentative(location)] = {
                left: [],
                top: [],
                right: [],
                bottom: [],
            }
        }
        let relevantSideInfo =
            sideInfos[disjointSet.findRepresentative(location)]
        // left
        if (location[0] in relevantSideInfo.left) {
            if (relevantSideInfo.left[location[0]] > location[1]) {
                relevantSideInfo.left[location[0]] = location[1]
            }
        } else {
            relevantSideInfo.left[location[0]] = location[1]
        }
        // right
        if (location[0] in relevantSideInfo.right) {
            if (relevantSideInfo.right[location[0]] < location[1]) {
                relevantSideInfo.right[location[0]] = location[1]
            }
        } else {
            relevantSideInfo.right[location[0]] = location[1]
        }
        // top
        if (location[1] in relevantSideInfo.top) {
            if (relevantSideInfo.top[location[1]] > location[0]) {
                relevantSideInfo.top[location[1]] = location[0]
            }
        } else {
            relevantSideInfo.top[location[1]] = location[0]
        }
        // bottom
        if (location[1] in relevantSideInfo.bottom) {
            if (relevantSideInfo.bottom[location[1]] < location[0]) {
                relevantSideInfo.bottom[location[1]] = location[0]
            }
        } else {
            relevantSideInfo.bottom[location[1]] = location[0]
        }
    }
    return sideInfos
}

const filePath = "./example_puzzle_input.txt" // path to your puzzle_input.txt
const fileContent = fs.readFileSync(filePath, "utf-8")

const puzzle = fileContent.split("\n").map((line) => line.split(""))

// start by getting all positions, make set for each
// from a corner, check in waves like
// #$%
// $$%
// %%%
// with each checking if it is the same symbol with the thing to the right and the thing to the bottom
// for last layer, only check bottom

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

function keysEqual(object1, object2) {
    for (const key of Object.keys(object1)) {
        if (!(object1[key].length === object2[key].length)) {
            return false
        }
    }
    for (const key of Object.keys(object2)) {
        if (!(object1[key].length === object2[key].length)) {
            return false
        }
    }
    return true
}

function getNumChanges(altitudes) {
    let numChanges = 0
    let lastElement = null
    for (const index in altitudes) {
        if (lastElement != null) {
            numChanges += lastElement != altitudes[index]
        }
        lastElement = altitudes[index]
    }
    return numChanges
}

const sideInfos = getSideInfos(disjointSet)

console.log(disjointSet)
console.log(sideInfos)

for (const key of Object.keys(sideInfos)) {
    if (
        keysEqual(sideInfos[key], { left: [], right: [], top: [], bottom: [] })
    ) {
        console.log(key)
    }
}

let totalPrice = 0

for (const key of Object.keys(sideInfos)) {
    let numSides =
        4 +
        getNumChanges(sideInfos[key].left) +
        getNumChanges(sideInfos[key].right) +
        getNumChanges(sideInfos[key].bottom) +
        getNumChanges(sideInfos[key].top)
    console.log(disjointSet.sizes[key], numSides)
    totalPrice += numSides * disjointSet.sizes[key]
}

console.log(totalPrice)

// TODO: DOES NOT COVER CASE OF SOMETHING LIKE (CONCAVE SHAPE)
// ##
// %#
// ##
// IDEA: ex for left side: keep track of y level for each x value that exists
// like y[x]
// to find sides, first purge values that dont add anything in the y-lists
// ex: in a shape like `###` the second two #s dont contribute to the number of left sides
// then somehow iterate though and find the number of sides