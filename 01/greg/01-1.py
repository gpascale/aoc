import re

def decode_line(line):
    first_digit = int(re.search(r'^[^\d]*(\d)', line).group(1))
    last_digit = int(re.search(r'(\d)[^\d]*$', line).group(1))
    return 10 * first_digit + last_digit

def main():
    with open('./01.input') as f:
        result = sum([decode_line(line) for line in f.readlines()])
    print (result)
    
if __name__ == '__main__':
    main()