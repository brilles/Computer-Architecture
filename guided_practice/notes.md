LS-8 computer:

- 8-bit computer with 8-bit memory addressing
- With 8 bits the CPU has a total of 256 bytes of memory and can compute values up to 255

0b1101 == 13 decimal (base 10)

8 + 4 + 1 == 13

0b10101011 == ??

128 + 32 + 8 + 2 + 1 == 171

16 + 1 == 17

0b10000 + 0b1 = 0b10001

Take advantage of alignments - every four bits represents 1 hex digit
Ob1111 == 15
0x == hex
0xF == 15

101000100
0b 1010 00100
0x A 4 hex

0x C 8
0b 1100 1000
0xC8 == 0b11001000

0b1111 15 (one less than 16)
0b10000 16
0b11111111 == 255 (1 less than 256)
0x 1111 1111
F F
ip4v are bytes

registers are like variables that are built into the CPU
fixed number and they can only hold so much(physical contraint of CPU wires)

--- Day 2 ---
A B A XOR B (Exclusive or - only one)

---

0 0 0
0 1 1
1 0 1
1 1 0

## A B A AND B

0 0 0
0 1 0
1 0 0
1 1 1

1101011
& 1010010

---

1000010

    Boolean  Bitwise

OR or |
AND and &
XOR N/A ^
NOT not ~

And Masking
101010101
& 111100000 <- AND mask (allows us ti select a few bits in a number, everywhere 1s are in the first, they are preserved) / turn bits off

---

101000000

10100000 AND
& 11000000

---

10000000
^^
1000000
100000
10000
1000
100
0000010

ir = 0b10100000 AND
num_oprands = (ir & 0b1100000) >> 6
mask out the bits -> shift to right

setting a bit to 1:
0001100
| 0000111

---

000111

---DAY 3---
Stack needs
PUSH
POP
size/count
find?

---DAY 4---
python module called the disassembler
it will show you the python assembly code that goes along with it
