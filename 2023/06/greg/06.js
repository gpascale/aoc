const _ = require('lodash')

function solvePart1(input) {
  const lines = input.split('\n').map(line => line.trim())
  console.log(lines)
  const T = lines[0].split(':')[1].trim().split(/\s+/).map(Number)
  const D = lines[1].split(':')[1].trim().split(/\s+/).map(Number)
  let ret = 1
  for (var i = 0; i < T.length; ++i) {
    const time = T[i]
    const distance = D[i]
    let numSolutions = 0
    for (var j = 1; j <= time; ++j) {
      const speed = j
      const distanceCovered = speed * (time - j)
      if (distanceCovered > distance) {
        ++numSolutions
      }
    }
    ret *= numSolutions
  }
  console.log('Part 1: ', ret)
}

function solvePart2() {
  // const time = 71530
  // const distance = 940200
  const time = 45988373
  const distance = 295173412781210
  let numSolutions = 0
  for (var j = 1; j <= time; ++j) {
    const speed = j
    const distanceCovered = speed * (time - j)
    if (distanceCovered > distance) {
      ++numSolutions
    }
  }
  console.log('Part 2: ', numSolutions)
}

solvePart1(require('./input').exampleInput)
solvePart2()
// solvePart2LessShittily(require('./input').input)
