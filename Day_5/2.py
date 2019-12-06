from Day_5.read_intcode_part_2 import read_intcode

if __name__ == '__main__':
    f = open('input.txt', 'r')
    intcode = [int(i) for i in f.read().split(',')]
    read_intcode(intcode)
