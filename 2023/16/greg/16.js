const _ = require('lodash')

let G = []
let reached = []
let visited = []

function getNext(dx, dy, c) {
  if (c == '.') return [[dx, dy]]
  if (c == '|') return dx == 0 ? [[0, dy]] : [ [0, -1], [0, 1] ]
  if (c == '-') return dy == 0 ? [[dx, 0]] : [ [-1, 0], [1, 0] ]
  return c == '\\' ? [[dy, dx]] : [[-dy, -dx]]
}

function bfs(start) {
  let q = [start]
  while (q.length) {
    const [[x, y, dx, dy], ...rest] = q
    q = rest
    if (x < 0 || x >= G[0].length || y < 0 || y >= G.length) continue
    if (visited[y][x][dx + 1][dy + 1]) continue
    visited[y][x][dx + 1][dy + 1] = 1
    reached[y][x] = 1
    for (const [nx, ny] of getNext(dx, dy, G[y][x])) {
      q.push([x + nx, y + ny, nx, ny])
    }
  }
}

function createNDimArray(dims) {
  return dims.length == 1
    ? Array(dims[0]).fill(0)
    : Array(dims[0]).fill(0).map(__ => createNDimArray(dims.slice(1)))
}

function solve1(input) {
  G = input.split('\n').filter(x => x).map(line => line.split(''))
  visited = createNDimArray([G.length, G[0].length, 3, 3])
  reached = createNDimArray([G.length, G[0].length])
  bfs([0, 0, 1, 0])
  console.log('part 1:', _.sum(reached.map(x => _.sum(x))))
}

function solve2(input) {
  G = input.split('\n').filter(x => x).map(line => line.split(''))
  ret = 0
  starts = []
  for (let y = 0; y < G.length; y++) {
    starts = [...starts, ...[[0, y, 1, 0], [G[0].length - 1, y, -1, 0]]]
  }
  for (let x = 0; x < G[0].length; x++) {
    starts = [...starts, ...[[x, 0, 0, 1], [x, G.length - 1, 0, -1]]]
  }
  for (c of starts) {
    visited = createNDimArray([G.length, G[0].length, 3, 3])
    reached = createNDimArray([G.length, G[0].length])
    bfs(c)
    ret = Math.max(ret, _.sum(reached.map(c => _.sum(c))))
  }
  console.log('part 2:', ret)
}

solve1(require('./input'))
solve2(require('./input'))
