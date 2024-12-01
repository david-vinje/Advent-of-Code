import fs from 'node:fs';

function partOne (lines: number[]) {
    for (const a of lines) {
        for (const b of lines) {
            if (a + b === 2020) {
                console.log(a*b)
                return         
            }
        }
    }
}

function partTwo(lines: number[]) {
    for (const a of lines) {
        for (const b of lines) {
            for (const c of lines) {
                if (a + b + c === 2020) {
                    console.log(a*b*c)
                    return         
                }
            }
        }
    }
}

fs.readFile(__dirname + '/../input/day1.txt', (_, data) => {
    const lines = data.toString()
        .split('\n')
        .map(Number)
    partOne(lines)
    partTwo(lines)
})
