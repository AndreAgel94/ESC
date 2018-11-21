//C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_0
D; JEQ
D=0
@CONTINUE_0
0; JMP
(TRUE_0)
D=-1
(CONTINUE_0)
@SP
A=M-1
M=D
//C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_1
D; JEQ
D=0
@CONTINUE_1
0; JMP
(TRUE_1)
D=-1
(CONTINUE_1)
@SP
A=M-1
M=D
//C_PUSH constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_2
D; JEQ
D=0
@CONTINUE_2
0; JMP
(TRUE_2)
D=-1
(CONTINUE_2)
@SP
A=M-1
M=D
//C_PUSH constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_3
D; JLT
D=0
@CONTINUE_3
0; JMP
(TRUE_3)
D=-1
(CONTINUE_3)
@SP
A=M-1
M=D
//C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_4
D; JLT
D=0
@CONTINUE_4
0; JMP
(TRUE_4)
D=-1
(CONTINUE_4)
@SP
A=M-1
M=D
//C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_5
D; JLT
D=0
@CONTINUE_5
0; JMP
(TRUE_5)
D=-1
(CONTINUE_5)
@SP
A=M-1
M=D
//C_PUSH constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_6
D; JGT
D=0
@CONTINUE_6
0; JMP
(TRUE_6)
D=-1
(CONTINUE_6)
@SP
A=M-1
M=D
//C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_7
D; JGT
D=0
@CONTINUE_7
0; JMP
(TRUE_7)
D=-1
(CONTINUE_7)
@SP
A=M-1
M=D
//C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@TRUE_8
D; JGT
D=0
@CONTINUE_8
0; JMP
(TRUE_8)
D=-1
(CONTINUE_8)
@SP
A=M-1
M=D
//C_PUSH constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D+M
@SP
A=M-1
M=D
//C_PUSH constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@SP
A=M-1
M=D
//neg
@SP
A=M-1
M=-M
//and
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D&M
@SP
A=M-1
M=D
//C_PUSH constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D|M
@SP
A=M-1
M=D
//not
@SP
A=M-1
M=!M