from Day_1.fuel_calculator import fuel_calculator

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split()
    result = 0

    for w in input:
        fuel = fuel_calculator(int(w))
        while fuel > 0:
            result += fuel if fuel > 0 else 0
            fuel = fuel_calculator(fuel)

    print('Result is:', result)