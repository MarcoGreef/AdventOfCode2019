def read_intcode(intcode):
    index = 0
    while index < len(intcode):
        opcode = int(str(intcode[index])[-2:])
        if opcode == 99:
            print('1202 program alarm')
            break

        parameter_mode = '000' if intcode[index] <= 99 else str(intcode[index])[:-2].zfill(3)
        param_a = intcode[index + 1] if parameter_mode[2] == '1' else intcode[intcode[index + 1]]
        try:
            param_b = intcode[index + 2] if parameter_mode[1] == '1' else intcode[intcode[index + 2]]
        except:
            param_b = None
        try:
            param_c = intcode[index + 3] if parameter_mode[0] == '1' else intcode[index + 3]
        except:
            param_c = None

        if opcode == 1:
            intcode[param_c] = param_a + param_b
            index += 4
        elif opcode == 2:
            intcode[param_c] = param_a * param_b
            index += 4
        elif opcode == 3:
            intcode[intcode[index + 1]] = int(input("Enter your value: "))
            index += 2
        elif opcode == 4:
            print('Ouput:', param_a)
            index += 2
            if intcode[index] == '99':
                print('Halt')
                break