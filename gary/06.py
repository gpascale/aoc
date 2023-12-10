
def parse_data(data):
  lines = data.splitlines()
  times = lines[0].split(':')[1].strip().split()
  times = [int(x) for x in times]
  dists = lines[1].split(':')[1].strip().split()
  dists = [int(x) for x in dists]
  return times, dists

def get_wins(time, best):
  wins = []
  for speed in range(1, time):
    dist = speed * (time - speed)
    if dist > best:
      wins.append((dist, speed))
  return wins

def main():
  times, bests = parse_data(new_data)
  prod = 1
  for time, best in zip(times, bests):
    wins = get_wins(time, best)
  print(len(wins))


new_test_data = """\
Time:      71530
Distance:  940200
"""

test_data = """\
Time:      7  15   30
Distance:  9  40  200
"""

data = """\
Time:        46     68     98     66
Distance:   358   1054   1807   1080
"""

new_data = """\
Time:        46689866
Distance:   358105418071080
"""

main()
