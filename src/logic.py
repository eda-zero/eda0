from node import *

class Exp(Node):
    def __init__(self, tag, inputs=[]):
        super(Exp, self).__init__(tag, inputs)
    def __and__(self, b):
        return Exp("and", [self, b])
    def __or__(self, b):
        return Exp("or", [self, b])
    def __xor__(self, b):
        return Exp("xor", [self, b])
    def __invert__(self):
        return Exp("not", [self])

def vars(line):
    vnames = line.split(" ")
    vlist = []
    for v in vnames:
        vlist.append(Exp(v))
    return vlist

if __name__ == '__main__':
    a, b, c = vars("a b c")
    print('a&b=', a&b)
    print('a&b|c=', a&b|c)
    print('a&(b|c)=', a&(b|c))
    print('~a&(b|c)=', ~a&(b|c))

# 三元組如何用 NAND 做出來
# https://introtcs.org/public/lec_03a_computing_every_function.html
'''
def IF(cond,a,b):
    notcond = NAND(cond,cond)
    temp = NAND(b,notcond)
    temp1 = NAND(a,cond)
    return NAND(temp,temp1)
'''
