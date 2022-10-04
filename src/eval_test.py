from chips import *
from hackCpu import *

if __name__ == '__main__':
    sel = Value(1); a = Value(1); b = Value(0); c = Value(1)
    and1 = And(a,b)
    print('and1=', and1)
    print('eval(and1)=', and1.eval())
    or1 = Or(a,b)
    print('or1=', or1)
    print('eval(or1)=', or1.eval())
    mux1 = Mux(sel, a, b)
    print('mux1=', mux1)
    print('eval(mux1)=', mux1.eval())
    if1 = If(sel, a, b)
    print('if1=', if1)
    print('eval(if1)=', if1.eval())
    fa1 = FullAdder(a,b,c)
    print('fa1=', fa1)
    print('eval(fa1)=', fa1.eval())
    
    A1 = VALUE([1,1,0,0])
    B1 = VALUE([1,0,1,0])
    print("A1=", map1(str, A1))
    print("B1=", map1(str, B1))

    NOT1 = NOT(A1)
    print("NOT1=", NOT1)
    print("eval(NOT(A1))=", NOT1.eval())

    OR1 = OR(A1, B1)
    print("OR1=", OR1)
    print("eval(OR(A1,B1))=", OR1.eval())

    AND1 = AND(A1, B1)
    print("AND1=", AND1)
    print("eval(AND(A1,B1))=", AND1.eval())

    XOR1 = XOR(A1, B1)
    print("XOR1=", XOR1)
    print("eval(XOR(A1,B1))=", XOR1.eval())

    A1 = VALUE([0,1,0,0])
    B1 = VALUE([1,0,1,0])
    c = Value(1)
    ADD1 = ADD(A1, B1, c)
    print("A1=", map1(str, A1))
    print("B1=", map1(str, B1))
    print("c=", c)
    print("ADD1=", ADD1)
    print("eval(ADD1(A1,B1,c))=", ADD1.eval()) # eval(ADD1)= {'o': [0, 0, 0, 1], 'cout': 0}, 從左到右反著看

    A1 = VALUE([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    B1 = VALUE([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    zx = Value(0); nx = Value(0)
    zy = Value(0); ny = Value(0)
    f  = Value(1); no = Value(0)
    ALU1 = ALU(A1, B1, zx, nx, zy, ny, f, no)
    print("A1=", map1(str, A1))
    print("B1=", map1(str, B1))
    print("ALU1=", ALU1)
    print("eval(ALU1(A1,B1,000000))=", ALU1.eval())
