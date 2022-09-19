from node import *
import json
from operator import itemgetter

# Chip 則是通用的，包含了《線 Wire，單輸出的 Gate 與多輸出的晶片》
class Chip(Node):
    def __init__(self, tag, inputs={}):
        super(Chip, self).__init__(tag, inputs)
        self.show = "?"
    def o(self):
        return self.outputs["o"]
    def O(self):
        return self.outputs["O"]
    def str(self, show=""):
        head = f"{self.tag}({','.join(self.inputs.keys())})"
        if show == 'exp':
            expMap = {}
            for k,v in self.outputs.items():
                expMap[k] = v.exp()
            return f"{head}=>{json.dumps(expMap)}"
        else:
            return f"{head}=>{','.join(self.outputs.keys())}"
    def __str__(self):
        return self.str(self.show)

# 只有一個輸出的基本 Chip 稱為 Gate，像是 Not, And, Or, Xor, Mux
# 從源頭追蹤回去 inputs 可以取得所有輸入元件
def Gate(tag, inputs):
    chip = Chip(tag, inputs)
    chip.show = 'exp'
    chip.outputs = {'o':chip}
    return chip

def Wire(a):
    return Gate("wire", {"a", a})

def Not(a):
    return Gate("not", {"a":a})

def Nand(a,b):
    return Gate("nand", {"a":a,"b":b})

def And(a,b):
    return Gate("and", {"a":a,"b":b})

def Or(a,b):
    return Gate("or", {"a":a,"b":b})

def Xor(a,b):
    return Gate("xor", {"a":a,"b":b})

def Mux(sel,a,b):
    chip = Chip("mux", {"sel":sel, "a":a, "b":b})
    chip.show = 'exp'
    chip.outputs = {"o":Or(And(Not(sel),chip.inputs["a"]), And(sel, chip.inputs["b"]))}
    return chip

def If(cond,a,b):
    chip = Chip("if", {"cond":cond, "a":a, "b":b})
    chip.show = 'exp'
    chip.outputs = {"o":Or(And(cond,a), And(Not(cond), b))}
    return chip

def DMux(i,sel):
    chip = Chip("dmux", {"i":i, "sel":sel})
    nsel = Not(sel)
    a = And(nsel, i)
    b = And(sel, i)
    chip.outputs = {"a":a, "b":b}
    return chip

def map1(f,A):
    R = [0]*len(A)
    for i in range(len(A)):
        R[i] = f(A[i])
    return R

def map2(f,A,B):
    R = [0]*len(A)
    for i in range(len(A)):
        R[i] = f(A[i], B[i])
    return R

def gateArray1(name, gate, A):
    chip = Chip(f"{name}{len(A)}", {"A":A})
    chip.outputs={"O":map1(gate, A)}
    return chip

def gateArray2(name, gate, A, B):
    chip = Chip(f"{name}{len(A)}", {"A":A, "B":B})
    chip.outputs={"O":map2(gate, A, B)}
    return chip

def WIRE(A):
    return gateArray1("wire", Wire, A)

def BUS(n):
    A = [0]*n
    return WIRE(A)

def ZERO(n):
    A = [0]*n
    return WIRE(A)

def ONE(n):
    A = [1]*n
    return WIRE(A)

def NOT(A):
    return gateArray1("not", Not, A)

def AND(A,B):
    return gateArray2("and", And, A, B)

def OR(A,B):
    return gateArray2("or", Or, A, B)

def XOR(A,B):
    return gateArray2("xor", Xor, A, B)

def MUX(sel,A,B):
    return gateArray2("mux", lambda a,b:Mux(sel,a,b).o(), A, B)

def IF(cond,A,B):
    return gateArray2("if", lambda a,b:If(cond,a,b).o(), A, B)

def Or8Way(A):
    assert len(A)==8
    chip = Chip("Or8Way", {"A":A})
    chip.show = 'exp'
    or76 = Or(A[7], A[6])
    or54 = Or(A[5], A[4])
    or32 = Or(A[3], A[2])
    or10 = Or(A[1], A[0])
    or74 = Or(or76, or54)
    or30 = Or(or32, or10)
    chip.outputs = {"o": Or(or74, or30)}
    return chip

def Or16Way(A):
    assert len(A)==16
    chip = Chip("Or16Way", {"A":A})
    chip.show = 'exp'
    chip.outputs = {"o":Or(Or8Way(A[0:8]), Or8Way(A[8:16]))}
    return chip

def FullAdder(a,b,c):
    chip = Chip("FullAdder", {"a":a, "b":b, "c":c})
    sum = Xor(Xor(a,b),c)
    carry = Or(Or(And(a,b), And(b,c)), And(a,c))
    chip.outputs = {"sum":sum, "carry":carry}
    return chip

def ADD(A,B,cin):
    assert len(A)==len(B)
    chip = Chip(f"ADD{len(A)}", {"A":A, "B":B, "cin":cin})
    S = [0]*len(A)
    C = [0]*(len(A)+1)
    C[0] = cin
    for i in range(0, len(A)):
        o = FullAdder(A[i], B[i], C[i]).outputs
        S[i] = o['sum']
        C[i+1] = o['carry']
    chip.outputs = {"O":S, "cout":C[len(A)]}
    return chip

class Dff(Chip):
    def __init__(self, a):
        super(Dff, self).__init__("dff", {"a":a})
        self.q = 'X'
        self.outputs = {"o":self.q}
    def clock():
        q0 = self.q
        self.q = self.inputs["a"].o()
        return q0

def Bit(a, load):
    chip = Chip(f"Bit", {"a":a, "load":load})
    mux = Mux("_", a, load)
    reg = Dff(mux.o())
    mux.inputs["a"] = reg.o()
    chip.outputs={"o":reg.o()}
    return chip

Reg = Bit

def REG(A, load):
    chip = Chip(f"reg{len(A)}", {"A":A, "load":load})
    chip.outputs={"O":map1(lambda x:Reg(x, chip.inputs["load"]), A)}
    return chip

def INC(A):
    B = [0]*len(A)
    return ADD(A, B, 1)

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
    dump("And", And(a, b))
    dump("Mux", Mux(sel, a, b))
    dump("If", If(sel, a, b))
    dump("DMux", DMux(sel, a).str('exp'))
    dump("NOT16", NOT(A))
    dump("AND16", AND(A,B))
    dump("OR16", OR(A,B))
    dump("XOR16", XOR(A,B))
    dump("MUX16", MUX(sel,A,B))
    dump("Or8Way", Or8Way(A[0:8]))
    dump("Or16Way", Or16Way(A))
    dump("FullAdder", FullAdder(a,b,c).str('exp'))
    dump("Add16", ADD(A,B,c))
    dump("Dff", Dff(a))
    # dump("Bit", Bit(a, load))
