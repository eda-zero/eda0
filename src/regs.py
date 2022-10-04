from chips import *

class Clock:
    def __init__(self):
        self.dffs = []
    def posedge(self):
        for dff in self.dffs:
            dff.posedge()

clock = Clock()

class Dff(Chip):
    def __init__(self, a):
        global clock
        super(Dff, self).__init__("dff", {"a":a})
        self.q = 'X'; self.q0 = 'X'
        self.outputs = {"o":self}
        clock.dffs.append(self)

    def exp(self):
        return f"dff:#{self.id}:q={self.q} q0={self.q0}"
    def posedge(self):
        self.q0 = self.q
        # print('dff.inputs[a]=', self.inputs['a'])
        clear(self.inputs['a'])
        ev = eval(self.inputs['a'])
        print('self.inputs[a]=', self.inputs['a'])
        print('ev=', ev)
        self.q = ev['o'] # self.inputs["a"].values['o']


def Bit(a, load):
    chip = Chip(f"Bit", {"a":a, "load":load})
    dff = Dff(None)
    mux = Mux(dff.o(), a, load)
    chip.dff = dff
    dff.inputs['a'] = mux.o()
    chip.outputs={"o":dff.o()}
    return chip

Reg = Bit

def REG(A, load):
    chip = Chip(f"reg{len(A)}", {"A":A, "load":load})
    chip.outputs={"o":map1(lambda x:Reg(x, load), A)}
    return chip

def COUNTER(n):
    chip = Chip(f"counter{n}", {})
    reg1 = REG([None]*n, Value(1))
    inc1 = INC(reg1.o())
    for i in range(n):
        reg1.o()[i].dff.q = 0
    reg1.inputs["A"] = inc1.outputs["o"]
    chip.outputs={"o":reg1.o()}
    return chip

if __name__ == '__main__':
    '''
    a = Value(1)
    dff1 = Dff(a)
    dump("Dff", dff1)
    print(dff1.eval())
    # dff1.posedge()
    clock.posedge()
    print(dff1.eval())
    a.assign(0)
    print(dff1.eval())
    clock.posedge()
    # dff1.posedge()
    print(dff1.eval())
    '''
    a = Value(1)
    load = Value(1)
    print('a=', a, 'load=', load)
    bit1 = Bit(a, load)
    print(bit1.eval())
    clock.posedge()
    print(bit1.eval())
    a.assign(0)
    print('a=', a)
    print(bit1.eval())
    clock.posedge()
    print(bit1.eval())
    clock.posedge()
    print(bit1.eval())
    clock.posedge()
    print(bit1.eval())
    '''
    counter = COUNTER(2)
    for i in range(10):
        print(counter.eval())
        clock.posedge()
    '''
