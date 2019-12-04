class PasswordGuess:
    def __init__(self, part):
        self.valid_numbers = []
        self.part = part

    def determinate(self, number):
        str_num = str(number)
        double = False
        for index in range(0, len(str_num) - 1):
            if str_num[index + 1] < str_num[index]:
                return (int(str_num[index]) - int(str_num[index + 1])) * (10 ** (len(str_num) - index - 2))
            elif str_num.count(str_num[index]) == 2 and self.part == 2:
                double = True
            elif str_num.count(str_num[index]) >= 2 and self.part == 1:
                double = True

        if double:
            self.valid_numbers.append(number)
        return 1

    def result(self):
        print('Result is:', len(self.valid_numbers))
