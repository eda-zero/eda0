from chips import *

def ALU(X, Y, zx, nx, zy, ny, f, no):
    chip = Chip("ALU", {"X":X, "Y":Y, "zx":zx, "nx":nx, "zy":zy, "ny":ny, "f":f, "no":no})
    Zero = [0]*16
    X1 = IF(zx, Zero, X).O()
    Y1 = IF(zy, Zero, Y).O()
    X2 = IF(nx, NOT(X1).O(), X1).O()
    Y2 = IF(ny, NOT(Y1).O(), Y1).O()
    O1 = IF(f, ADD(X2,Y2,0).outputs["SUM"], AND(X2,Y2).O()).O()
    O = IF(no, NOT(O1).O(), O1).O()
    zr = Not(Or16Way(O))
    ng = O[15]
    chip.outputs = {"O": O, "zr":zr, "ng":ng}
    return chip

def CPU(IM, I, reset):
    # decoder
    isC = I[15]; a=I[12]; 
    c1=I[11]; c2=I[10]; c3=I[9]; c4=I[8]; c5=I[7]; c6=I[6]
    d1 = I[5]; d2=I[4]; d3=I[3]; j1=I[2]; j2=I[1]; j3=I[0]
    # Control Logic
    isA = Not(isC)
    AluToA = And(isC, d1)
    Aload = Or(isA, AluToA)
    Ain = IF(isC, ALU_OUT, I)
    A = REG(Ain, Aload)
    ADDRESS = A[0:15]
    Dload = And(isC, d2)
    D = REG(ALU_OUT, Dload)
    # ALU
    AM = MUX(A, IM)
    ALU_OUT, zr, ng = ALU(D, AM, c1, c2, c3, c4, c5, c6)
    OUT_M = ALU_OUT
    # JUMP
    ngzr = Or(ng, zr)
    gt = Not(ngzr)
    passLT = And(ng, j1)
    passEQ = And(zr, j2)
    passGT = And(gt, j3)
    passLE = Or(passLT, passEQ)
    passJump = Or(passLE, passGT)
    PCload = And(isC, passJump)
    PC_OUT = PC(Aout, PCload, 1, reset)
    writeM = And(isC, d3); 
    return OUT_M, writeM, ADDRESS, PC_OUT[0:15]

if __name__ == '__main__':
    sel="sel"; a = "a"; b= "b"; c="c"; d="d"; load="load"
    A = [f"A{i}" for i in range(16)]
    B = [f"B{i}" for i in range(16)]
    dump("ALU", ALU(A,B,"zx","nx","zy","ny","f","no"))

