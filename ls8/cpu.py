"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
SP = 7


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256  # instructions
        self.register = [0] * 8  # 8 registers
        self.PC = 0  # program counter, points to currently executing instructions
        self.branchtable = {}
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[MUL] = self.handle_MUL
        self.branchtable[PUSH] = self.handle_PUSH
        self.branchtable[POP] = self.handle_POP

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

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        # should accept a value to writen and the adress to write it to
        self.ram[address] = value

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        elif op == "MUL":
            self.register[reg_a] *= self.register[reg_b]
            return self.register[reg_a]
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

    def handle_HLT(self, a, b):
        self.running = False
        self.PC += 1

    def handle_LDI(self, a, b):
        self.register[a] = b
        self.PC += 3

    def handle_PRN(self, a, b):
        print(self.register[a])
        self.PC += 2

    def handle_MUL(self, a, b):
        self.alu('MUL', a, b)
        self.PC += 3

    def handle_PUSH(self, a, b):
        # decrement the stack pointer
        self.register[SP] -= 1
        # copy the value in the given register to the address pointed to by SP
        value = self.register[a]
        # push onto stack ( in mem at SP)
        self.ram[self.register[SP]] = value
        self.PC += 2

    def handle_POP(self, a, b):
        # get value from mem
        value = self.ram[self.register[SP]]
        # store the value from the stack in the register
        self.register[a] = value
        # increment SP
        self.register[SP] += 1
        self.PC += 2

    def run(self):
        """Run the CPU."""

        self.register[SP] = 244
        self.running = True
        while self.running:
            ir = self.ram[self.PC]
            operand_a = self.ram[self.PC + 1]
            operand_b = self.ram[self.PC + 2]
            try:
                self.branchtable[ir](operand_a, operand_b)
            except:
                print(f"unknown instruction {ir}")
                sys.exit(1)
