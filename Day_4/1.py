from Day_4.password_guess import PasswordGuess

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split('-')

    pg = PasswordGuess(1)
    number = int(input[0])
    while number <= int(input[1]) + 1:
        number += pg.determinate(number)

    pg.result()

