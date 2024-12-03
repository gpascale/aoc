const _ = require('lodash')
const input = require('./input').split(',')
const example = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(',')

const hash = s =>
  s.split('').map((_c, i) => s.charCodeAt(i)).reduce((a, c) => ((a + c) * 17) % 256, 0)

const solve1 = () => console.log('part 1:', _.sum(input.map(hash)))

const solve2 = () => {
  b = Array(256).fill(-1).map(_c => [])
  input.forEach(s => {
    const [_m, lbl, op, foc] = s.match(/([a-z]+)([=-])(\d+)?/)
    const box = hash(lbl)
    if (op === '-') {
      b[box] = b[box].filter(x => x[0] !== lbl)
    } else {
      const idx = b[box].findIndex(x => x[0] === lbl)
      b[box] =
        idx == -1
          ? [...b[box], [lbl, foc]]
          : [...b[box].slice(0, idx), [lbl, foc], ...b[box].slice(idx + 1)]
    }
  })
  console.log(
    'part 2:',
    _.sum(
      b.flatMap((arr, box) =>
        arr.map((a, i) => (box + 1) * (i + 1) * parseInt(a[1]))
      )
    )
  )
}

solve1()
solve2()
