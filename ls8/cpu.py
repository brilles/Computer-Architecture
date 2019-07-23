"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b1010010


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256  # instructions
        self.register = [0] * 8  # 8 registers
        self.PC = 0  # program counter, points to currently executing instructions

    def load(self):
        """Load a program into memory."""

        address = 0

        # handle command line args
        if len(sys.argv) != 2:
            print(f"usage: {sys.argv[0]} filename")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    num = line.split('#', 1)[0]
                    if num.strip() == '':
                        continue

                    # print(num)
                    self.ram[address] = int(num, 2)  # ,2
                    address += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        # should accept a value to writen and the adress to write it to
        self.ram[address] = value

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        running = True
        while running:
            IR = self.ram[self.PC]  # instruction register
            operand_a = self.ram[self.PC + 1]
            operand_b = self.ram[self.PC + 2]

            # if-else cascade
            if IR == HLT:
                running = False
                self.PC += 1

            elif IR == LDI:
                self.register[operand_a] = 8
                self.PC += 3

            elif IR == PRN:
                print(self.register[operand_a])
                self.PC += 2

            elif IR == MUL:
                # ALU nultiply and store
                MULVAL = alu(
                    self, 'MUL', self.register[operand_a], self.register[operand_b])
                print("mulval", MULVAL)
                self.pc += 3

            else:
                print(f"unknown instruction {IR}")
                sys.exit(1)
