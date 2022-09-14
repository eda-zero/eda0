from gates import *

def Mux(sel,a,b):
    return Or(And(Not(sel),a), And(sel, b))

def If(cond,a,b):
    return Mux(cond, b, a)

def DMux(i,sel):
    nsel = Not(sel)
    a = And(nsel, i)
    b = And(sel, i)
    return a,b

def map1(f, A):
    return list(map(f,A))

def map2(f,A,B):
    R = [0]*len(A)
    for i in range(len(A)):
        R[i] = f(A[i], B[i])
    return R

def NOT(A):
    return map1(Not, A)

def AND(A,B):
    return map2(And, A, B)

def OR(A,B):
    return map2(Or, A, B)

def XOR(A,B):
    return map2(Xor, A, B)

def MUX(sel,A,B):
    return map2(lambda a,b:Mux(sel,a,b), A, B)

def IF(cond,A,B):
    return MUX(cond, B, A)

def Or8Way(A):
    or76 = Or(A[7], A[6])
    or54 = Or(A[5], A[4])
    or32 = Or(A[3], A[2])
    or10 = Or(A[1], A[0])
    or74 = Or(or76, or54)
    or30 = Or(or32, or10)
    return Or(or74, or30)

def Or16Way(A):
    return Or(Or8Way(A[0:8]), Or8Way(A[8:16]))

def FullAdder(a,b,c):
    sum = Xor(Xor(a,b),c)
    carry = Or(Or(And(a,b), And(b,c)), And(a,c))
    return sum, carry

def ADD(A,B,c0):
    C = [0]*(len(A)+1)
    C[0] = c0
    S = [0]*(len(A))
    for i in range(0, len(A)):
        S[i], C[i+1] = FullAdder(A[i], B[i], C[i])
    # return S[len(A)-1], C[len(A)]
    return S

class Dff(Chip):
    def __init__(self, a):
        super(Dff, self).__init__("dff", [a])
        self.q = 'X'
    def clock():
        q0 = self.q
        self.q = a.out()
        return q0
    def out():
        return self.q

def Bit(a, load):
    reg = Dff("")
    mo = Mux(reg.q, a, load)
    reg.inputs[0] = mo
    return reg

Reg = Bit

def REG(A, load):
    return map1(lambda x:Reg(x, load), A)

def INC(A):
    B = [0]*len(A)
    B[0] = 1
    return ADD(A, B)

def ALU(X, Y, zx, nx, zy, ny, f, no):
    Zero = [0]*16
    X1 = IF(zx, Zero, X)
    Y1 = IF(zy, Zero, Y)
    X2 = IF(nx, NOT(X1), X1)
    Y2 = IF(ny, NOT(Y1), Y1)
    O1 = IF(f, ADD(X2,Y2,0), AND(X2,Y2))
    O2 = IF(no, NOT(O1), O1)
    zr = Not(Or16Way(O2))
    ng = O2[15]
    return O2, zr, ng

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

def dump(name, chips):
    print(f"============{name}============")
    if isinstance(chips, list) or isinstance(chips, tuple):
        r = []
        for chip in chips:
            r.append(str(chip))
        print(r)
    else:
        print(chips)

if __name__ == '__main__':
    sel="sel"; a = "a"; b= "b"; c="c"; d="d"; load="load"
    A = [f"A{i}" for i in range(16)]
    B = [f"B{i}" for i in range(16)]
    dump("Mux", Mux(sel, a, b))
    dump("If", If(sel, a, b))
    dump("DMux", DMux(sel, a))
    dump("NOT16", NOT(A))
    dump("AND16", AND(A,B))
    dump("OR16", OR(A,B))
    dump("XOR16", XOR(A,B))
    dump("MUX16", MUX(sel,A,B))
    dump("Or16Way", Or16Way(A))
    dump("FullAdder", FullAdder(a,b,c))
    dump("Add16", ADD(A,B,c))
    dump("Dff", Dff(a))
    dump("Bit", Bit(a, load))
    dump("Register", REG(A, load))
    O, zr, ng = ALU(A,B,"zx","nx","zy","ny","f","no")
    dump("ALU.ng", ng)
