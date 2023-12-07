const _ = require('lodash')

const cards = '23456789TJQKA'
const nc = 'abcdefghijklm'

const freq = h =>
  h.split('').reduce((a, v) => ({ ...a, [v]: a[v] ? a[v] + 1 : 1 }), {})

const rank = hand => _.sum(Object.values(freq(hand)).map(x => x * x * x))

const compare = ({ hand: a }, { hand: b }) =>
  rank(a) === rank(b) ? (a < b ? -1 : 1) : rank(a) - rank(b)

function solve(input) {
  hands = input.split('\n').map(line => ({
    hand: [...line.split(' ')[0]].map(card => nc[cards.indexOf(card)]).join(''),
    bid: parseInt(line.split(' ')[1])
  }))
  hands.sort(compare)
  console.log(_.sum(hands.map((h, i) => (i + 1) * h.bid)))
}

solve(require('./input').input)
