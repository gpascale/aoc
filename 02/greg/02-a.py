import re

num_cubes = { 'red': 12, 'green': 13, 'blue': 14 }

def is_valid(line):
    matches = re.findall(r'(\d+) (red|green|blue)', line)
    return all([int(num) <= num_cubes[color] for num, color in matches])

def main():
    lines = open('./02.input').readlines()
    result = sum([i + 1 if is_valid(l) else 0 for i, l in enumerate(lines)])
    print(result)

if __name__ == '__main__':
    main()