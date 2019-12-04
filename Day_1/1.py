from Day_1.fuel_calculator import fuel_calculator

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split()
    result = 0
    for i in input:
        result += fuel_calculator(int(i))
    print('Result is:', result)


