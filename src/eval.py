from chips import *

def eval(chip):
    chip.clear()
    chip.eval()
    return chip.values

class Counter(Chip):
    def __init__(self, n):
        super(Chip, self).__init__(f"counter{n}")
        self.counter = 0
        self.n = n
        self.max = 2**n
    def O(self):
        C = "{0:b}".format(self.counter)
        C = '0'*(self.n-len(C))+C
        return [0 if c=='0' else 1 for c in C]
    def inc(self):
        self.counter = (self.counter+1) % self.max

if __name__ == '__main__':
    C = Counter(2)
    for i in range(20):
        print("C.O()=", C.O())
        C.inc()
    '''
    a = 0; b=0;
    #g1 = And(a,b)
    #g1 = Or(a,b)
    g1 = Xor(a,b)
    for t in range(1, 10):
        print(f"a={a} b={b} o={eval(g1)}")
        if t%1==0: b=(b+1)%2
        if t%2==0: a=(a+1)%2
        g1.inputs={"a":a, "b":b}
    '''
    '''
    c = 0; a = 0; b=0
    #g1 = And(a,b)
    #g1 = Or(a,b)
    g1 = Xor(a,b)
    for t in range(1, 10):
        print(f"a={a} b={b} o={eval(g1)}")
        if t%1==0: b=(b+1)%2
        if t%2==0: a=(a+1)%2
        if t%4==0: c=(c+1)%2
        g1.inputs={"a":a, "b":b}
    '''
    sel = Value(1); a = Value(1); b = Value(0)
    and1 = And(a,b)
    print('and1=', and1)
    print('eval(and1)=', eval(and1))
    or1 = Or(a,b)
    print('or1=', or1)
    print('eval(or1)=', eval(or1))
    mux = Mux(sel, a, b)
    print('mux=', mux)
    print('eval(mux)=', eval(mux))
