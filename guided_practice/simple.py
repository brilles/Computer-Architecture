import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE_REGISTER = 4
PRINT_REGISTER = 5
SP = 7
PUSH = 6
POP = 7
CALL = 8
RET = 9

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

register[SP] = 127

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

    elif command == PUSH:
        register[SP] -= 1  # decrement SP
        regnum = memory[pc + 1]  # get the register number operand
        value = register[regnum]  # get the valie from that register
        memory[register[SP]] = value  # store the valie in the memory at SP
        pc += 2

    elif command == POP:
        value = memory[register[SP]]
        regnum = memory[pc + 1]
        register[regnum] = value
        register[SP] += 1
        pc += 2

    elif command == CALL:
        # get address of instruction right after this CALL inst
        return_addr = pc + 2

        # push return address on stack
        register[SP] -= 1  # decrement SP
        # store that value in memory at the SP
        memory[register[SP]] = return_addr

        # CALL and RET dont auto go to next instr (arbitrary place in mem)
        # set the PC to the subroutine addr
        regnum = memory[pc + 1]
        subroutine_addr = register[regnum]
        pc = subroutine_addr

    elif command == RET:
        # pop the return address off the stack
        return_addr = memory[register[SP]]
        register[SP] += 1

        pc = return_addr

    elif command == HALT:
        running = False
        pc += 1

    else:
        print(f"unknown instruction {command}")
        sys.exit(1)
