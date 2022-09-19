from chips import *
from operator import itemgetter

def ALU(X, Y, zx, nx, zy, ny, f, no):
    chip = Chip("ALU", {"X":X, "Y":Y, "zx":zx, "nx":nx, "zy":zy, "ny":ny, "f":f, "no":no})
    Z16 = ZERO(16).O()
    X1 = IF(zx, Z16, X).O()
    Y1 = IF(zy, Z16, Y).O()
    X2 = IF(nx, NOT(X1).O(), X1).O()
    Y2 = IF(ny, NOT(Y1).O(), Y1).O()
    O1 = IF(f, ADD(X2,Y2,0).O(), AND(X2,Y2).O()).O()
    O = IF(no, NOT(O1).O(), O1).O()
    zr = Not(Or16Way(O))
    ng = O[15]
    chip.outputs = {"O": O, "zr":zr, "ng":ng}
    return chip

def PC(A, load, inc, reset):
    chip = Chip("PC", {"A":A, "load":load, "inc":inc, "reset":reset})
    IF3 = BUS(16).O()
    R = REG(IF3, 1)
    O = R.O()
    O1 = INC(O).O()
    IF1 = MUX(inc, O, O1).O()
    IF2 = MUX(load, IF1, A).O()
    IF3 = MUX(reset, IF2, [0]*16).O()
    R.inputs["A"] = IF3
    chip.outputs={"O":O}
    return chip

def CPU(IM, I, reset):
    chip = Chip("HackCPU", {"IM":IM, "I":I, "reset":reset})
    ALU_OUT = BUS(16).O()
    # decoder
    isC = I[15]; a=I[12]
    c1=I[11]; c2=I[10]; c3=I[9]; c4=I[8]; c5=I[7]; c6=I[6]
    d1 = I[5]; d2=I[4]; d3=I[3]; j1=I[2]; j2=I[1]; j3=I[0]
    # === Control Logic ===
    # A register
    isA = Not(isC)
    AluToA = And(isC, d1)
    Aload = Or(isA, AluToA)
    Ain = IF(isC, ALU_OUT, I)
    A = REG(Ain.O(), Aload)
    ADDRESS = A.O()[0:15]
    # D register
    Dload = And(isC, d2)
    D = REG(ALU_OUT, Dload)
    # ALU
    AM = MUX(a, A.O(), IM)
    ALU1 = ALU(D.O(), AM.O(), c1, c2, c3, c4, c5, c6)
    ALU_OUT, zr, ng = itemgetter('O', 'zr', 'ng')(ALU1.outputs)
    Ain.inputs["ALU_OUT"] = ALU_OUT
    D.inputs["ALU_OUT"] = ALU_OUT
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
    PC_OUT = PC(A.O(), PCload, 1, reset).O()
    writeM = And(isC, d3)
    chip.outputs = {"OUT_M":OUT_M, "writeM":writeM, "ADDRESS":ADDRESS, "PC_OUT":PC_OUT[0:15]}
    return chip

if __name__ == '__main__':
    sel="sel"; a = "a"; b= "b"; c="c"; d="d"; 
    load="load"; inc="inc"; reset="reset"
    A = [f"A{i}" for i in range(16)]
    B = [f"B{i}" for i in range(16)]
    IM = [f"IM{i}" for i in range(16)]
    I = [f"I{i}" for i in range(16)]
    dump("ALU", ALU(A,B,"zx","nx","zy","ny","f","no"))
    dump("PC", PC(A, load, inc, reset))
    dump("CPU", CPU(IM, I, "reset"))
