from gate import *


class Var(Gate):
    def __init__(self, value="_"):
        self.op = value
    def __and__(self, b):
        return Gate("and", [self.v, b.v])
    def __or__(self, b):
        return Gate("or", [self.v, b.v])
    def __xor__(self, b):
        return Gate("xor", [self.v, b.v])
    def __not__(self, b):
        return Gate("not", [self.v])

def vars(line):
    values = line.split(" ")
    vlist = []
    for v in values:
        vlist.append(Var(v))
    return vlist

if __name__ == '__main__':
    a,b,c = vars("_ 0 1")
    print('(a&b)|c=', (a&b)|c)
