import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE_REGISTER = 4
PRINT_REGISTER = 5

# instructions
memory = [
    PRINT_BEEJ,
    SAVE_REGISTER,
    177,  # store 177
    2,  # in register 2
    PRINT_REGISTER,
    2,  # print value in register 2
    HALT
]

register = [0] * 8  # 8 registers

pc = 0  # Program counter, points  to currently-executing instruction

running = True

while running:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("BeeJ!")
        pc += 1

    elif command == PRINT_NUM:
        operand = memory[pc + 1]
        print(operand)
        pc += 2

    elif command == SAVE_REGISTER:
        value = memory[pc + 1]
        regnum = memory[pc + 2]
        register[regnum] = value
        pc += 3  # bc 3 byte instruction

    elif command == PRINT_REGISTER:
        regnum = memory[pc + 1]
        print(register[regnum])
        pc += 2

    elif command == HALT:
        running = False
        pc += 1

    else:
        print(f"unknown instruction {command}")
        sys.exit(1)
