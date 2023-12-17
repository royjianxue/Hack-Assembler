## Hack Assembler
ASM is an assembler for the Hack language implemented in python.

Although Hack assembly language is very simple, the assembly works with strings to parse instructions and translate to machine code. I have documented my code fairly well so that everyone who is interested can take a look.

## Examples of Hack assembly instructions
Below's an example program that determines the larger number of two given numbers, authored by Shimon Schocken and Noam Nisan, the creators of the Hack language and computer architecture. I have also included a PongL.asm file along with its hack output file in machine code.
```
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/Max.asm

// Computes R2 = max(R0, R1)  (R0,R1,R2 refer to  RAM[0],RAM[1],RAM[2])

  @R0
  D=M              // D = first number
  @R1
  D=D-M            // D = first number - second number
  @OUTPUT_FIRST
  D;JGT            // if D>0 (first is greater) goto output_first
  @R1
  D=M              // D = second number
  @OUTPUT_D
  0;JMP            // goto output_d
(OUTPUT_FIRST)
  @R0             
  D=M              // D = first number
(OUTPUT_D)
  @R2
  M=D              // M[2] = D (greatest number)
(INFINITE_LOOP)
  @INFINITE_LOOP
  0;JMP            // infinite loop

```
## Three instructions:
1. A-instructions
2. C-instructions
3. L-instructions.

A-instructions are addressing instructions, and start with an '@', followed by either a direct address, a location, or a variable. For example:

@100

@LOCATION

@var

C-instructions are compute instructions, and are used for general purpose commands, including storing values, performing computations, and jumping to memory locations. Examples include:

D=A

D=D-M

0; JMP

D; JGT

L-instructions, or labels, are psuedo commands only used by the assembler to determine address locations. These are not converted into machine code. Examples:

(LOOP)

(END)

(JUMP_HERE)

For more information, visit: http://nand2tetris.org/

## Usage
$ python ASM.py <inputfile></inputfile>.asm

## Download
Clone the repository: `git clone https://github.com/royjianxue/hackAssembly.git`
