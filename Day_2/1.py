from Day_2.read_intcode import read_intcode

if __name__ == '__main__':
    f = open('input.txt', 'r')
    intcode = [int(i) for i in f.read().split(',')]
    status, result = read_intcode(intcode, {1: 12, 2: 2})
    print(status, result[0])
