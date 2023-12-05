const _ = require('lodash')

const types = [
  'seed',
  'soil',
  'fertilizer',
  'water',
  'light',
  'temperature',
  'humidity',
  'location'
]

let maps

function buildMaps(lines) {
  maps = new Array(types.length).fill(0).map(x => [])
  curMapIdx = -1
  for (var i = 0; i < lines.length; ++i) {
    if (lines[i].indexOf('-') > -1) {
      curMapIdx = types.indexOf(lines[i].substring(0, lines[i].indexOf('-')))
      continue
    } else if (!lines[i]) {
      continue
    }
    if (curMapIdx === -1) {
      continue
    }
    const map = maps[curMapIdx]
    const [dstStart, srcStart, len] = lines[i].trim().split(' ').map(Number)
    map.push({
      srcStart,
      srcEnd: srcStart + len - 1,
      dstStart,
      dstEnd: dstStart + len - 1
    })
  }
  for (var i = 0; i < maps.length; ++i) {
    maps[i].sort((a, b) => a.srcStart - b.srcStart)
  }
}

function getSeedLocation(seed) {
  let nextVal = seed
  for (var i = 0; i < maps.length; ++i) {
    const map = maps[i]
    for (const mapping of map) {
      if (nextVal >= mapping.srcStart && nextVal <= mapping.srcEnd) {
        nextVal = mapping.dstStart + (nextVal - mapping.srcStart)
        break
      }
    }
  }
  return nextVal
}

function solvePart1(input) {
  const lines = input.split('\n').map(line => line.trim())
  const seeds = lines[0].replace('seeds: ', '').trim().split(' ').map(Number)

  buildMaps(lines.slice(1))

  let ret = 9999999999999
  for (const seed of seeds) {
    ret = Math.min(getSeedLocation(seed), ret)
  }

  console.log('Part 1: ', ret)
}

function solvePart2(input) {
  const lines = input.split('\n').map(line => line.trim())
  const nums = lines[0].replace('seeds: ', '').trim().split(' ').map(Number)
  const seedRanges = _.chunk(nums, 2).map(([start, len]) => [
    start,
    start + len
  ])

  let ret = 9999999999999
  for (const seedRange of seedRanges) {
    for (let seed = seedRange[0]; seed < seedRange[1]; ++seed) {
      ret = Math.min(getSeedLocation(seed), ret)
    }
  }

  console.log('Part 2: ', ret)
}

function dfs(state, level) {
  if (state[0] === 0) console.log(state, level)
  if (level === maps.length) {
    // console.log(level, state)
    return [state]
  }

  let result = []

  const map = maps[level]
  let [start, end] = state
  for (const mapping of map) {
    let { srcStart, srcEnd, dstStart } = mapping
    if (srcEnd < start) continue
    if (srcStart > end) break
    const overlapStart = Math.max(start, srcStart)
    const overlapEnd = Math.min(end, srcEnd)
    result = [
      ...result,
      ...dfs(
        [dstStart + overlapStart - srcStart, dstStart + overlapEnd - srcStart],
        level + 1
      )
    ]
    if (overlapStart > start) {
      result = [...result, ...dfs([start, overlapStart - 1], level + 1)]
    }
    if (overlapEnd < end) {
      start = overlapEnd + 1
    } else {
      return result
    }
  }

  result = [...result, ...dfs([start, end], level + 1)]
  return result
}

function solvePart2LessShittily(input) {
  const lines = input.split('\n').map(line => line.trim())
  const nums = lines[0].replace('seeds: ', '').trim().split(' ').map(Number)
  const seedRanges = _.chunk(nums, 2).map(([start, len]) => [
    start,
    start + len
  ])
  buildMaps(lines.slice(1))

  let results = []
  for (const r of seedRanges) {
    results = [...results, ...dfs([r[0], r[1]], 0)]
  }

  const result = _.min(results.map(x => x[0]))
  console.log('Part 2: ', result)
}

solvePart1(require('./input').input)
// solvePart2(require('./input').input)
solvePart2LessShittily(require('./input').input)
