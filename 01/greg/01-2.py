import re

digs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dig_re = rf'(?=(\d|{"|".join(digs)}))'

def decode_digit(d):
    return digs.index(d) + 1 if d in digs else int(d)

def decode_line(line):
    matches = [m.group(1) for m in re.finditer(dig_re, line)]
    return 10 * decode_digit(matches[0]) + decode_digit(matches[-1])

def main():
    with open('./01.input', 'r') as f:
        result = sum([decode_line(line) for line in f.readlines()])
    print(result)

if __name__ == '__main__':
    main()