for noun in range(100):
    for verb in range(100):
        with open('input2.txt', 'r') as f:
            program = f.read()

        program = program.split(',')
        program = [int(x) for x in program]
        program[1] = noun
        program[2] = verb

        loc = 0
        while True:
            opcode = program[loc]
            if opcode == 99:
                break
            first = program[program[loc+1]]
            second = program[program[loc+2]]
            at = program[loc+3]

            if opcode == 1:
                res = first + second
            elif opcode == 2:
                res = first * second
            else:
                print('Uh oh, opcode {} found'.format(opcode))
                print(program)
                break

            program[at] = res
            loc += 4

        if program[0] == 19690720:
            print('Noun: {}, Verb: {}'.format(noun, verb))

