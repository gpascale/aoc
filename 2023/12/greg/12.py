import re

cache = None
line = None
segs = None


def count(pos, seg_pos, prev_used):
    cache_key = tuple([pos, seg_pos, prev_used])
    if cache_key in cache:
        return cache[cache_key]

    # end of line - we're done if all segments used
    if pos == len(line):
        cache[cache_key] = 1 if seg_pos == len(segs) else 0
        return cache[cache_key]

    # fail if we have adjacent segments
    if prev_used and line[pos] == '#':
        cache[cache_key] = 0
        return cache[cache_key]

    ret = 0

    # try skipping if we don't have to place a segment
    if line[pos] in ['?', '.']:
        ret += count(pos + 1, seg_pos, 0)

    # try to place a segment if we can
    if not prev_used and seg_pos < len(segs):
        seg_len = segs[seg_pos]
        if pos + seg_len <= len(line):
            if re.fullmatch(r'[#?]+', line[pos:pos + seg_len]):
                ret += count(pos + seg_len, seg_pos + 1, 1)
    cache[cache_key] = ret
    return cache[cache_key]


def solve(part_2):
    global line
    global segs
    global cache
    L = [s.strip() for s in open("./input.txt").readlines()]
    ret = 0
    for l in L:
        line, segs = (l.split(' ')[0], list(
            map(int, l.split(' ')[1].split(','))))
        if part_2:
            line = f'{line}?{line}?{line}?{line}?{line}'
            segs = [*segs, *segs, *segs, *segs, *segs]
        cache = {}
        ret += count(0, 0, 0)
    return ret


print('part 1:', solve(part_2=False))
print('part 2:', solve(part_2=True))
