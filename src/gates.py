from node import *

class Chip(Node):
    def __init__(self, tag, inputs=[]):
        super(Chip, self).__init__(tag, inputs)

def Not(a):
    return Chip("not", [a])

def Nand(a,b):
    return Chip("nand", [a,b])

def And(a,b):
    return Chip("and", [a,b])

def Or(a,b):
    return Chip("or", [a,b])

def Xor(a,b):
    return Chip("xor", [a,b])

def Mux(sel,a,b):
    # c = Chip("mux", [sel,a,b])
    return Or(And(Not(sel),a), And(sel, b))

def If(cond,a,b):
    return Mux(cond, b, a)

def DMux(i,sel):
    nsel = Not(sel)
    a = And(nsel, i)
    b = And(sel, i)
    return a,b

def map2(f,A,B):
    R = [0]*len(A)
    for i in range(len(A)):
        R[i] = f(A[i], B[i])
    return R

def NOT(A):
    return map(Not, A)

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
    return Or(Or8Way(A[0:8]), Or8Way(A[8:15]))

def FullAdder(a,b,c):
    sum = Xor(Xor(a,b),c)
    carry = Or(Or(And(a,b), And(b,c)), And(a,c))
    return sum, carry

def ADD(A,B,c0):
    C = [0]*(len(A)+1)
    C[0] = c0
    for i in range(0, len(A)):
        S[i], C[i+1] = FullAdder(A[i], B[i], C[i])
    return S, C[len(A)]

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
    mo = Mux(ro, a, load)
    reg = Dff(mo)
    return reg

Reg = Bit

def REG(A, load):
    return map(lambda x:Reg(x, load), A)

def INC(A):
    B = [0]*len(A)
    B[0] = 1
    return ADD(A, B)
