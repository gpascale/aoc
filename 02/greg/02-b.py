import re

def get_power(line):
    r = { 'red': 0, 'green': 0, 'blue': 0 }
    matches = re.findall(r'(\d+) (red|green|blue)', line)
    for num, color in matches:
        r[color] = max(r[color], int(num))
    return r['red'] * r['green'] * r['blue']

def main():
    lines = open('./02.input').readlines()
    result = sum([get_power(line) for line in lines])
    print(result)

if __name__ == '__main__':
    main()