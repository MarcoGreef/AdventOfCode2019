from Day_2.read_intcode import read_intcode

if __name__ == '__main__':
    f = open('input.txt', 'r')
    intcode_str = f.read()

    for noun in range(0, 100):
        for verb in range(0, 100):
            status, result = read_intcode([int(i) for i in intcode_str.split(',')], {1: noun, 2: verb})
            if result[0] == 19690720:
                print('Solution found! Verb: {}, Noun: {}, Answer: {}'.format(verb, noun, 100* noun + verb))
                break