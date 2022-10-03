from chips import *

def clear(chip):
    if isinstance(chip, list): # list of chips
        for x in chip: clear(x)
        return
    assert isinstance(chip, Node)
    if chip.values is None: return
    for k, v in chip.outputs.items():
        if v != chip: clear(v)
    chip.values = None

def eval(chip):
    if isinstance(chip, list): return {'o':map1(lambda x:eval(x)['o'], chip)}
    assert isinstance(chip, Node)
    if chip.values is not None: return chip.values
    op = chip.tag
    o = None
    if op == "not":
        a = chip.inputs['a']; eval(a); a = a.values['o']
        o = 0 if a==1 else 1
        chip.values = {"o":o}
    elif op in ["and", "or", "xor"]:
        a = chip.inputs['a']; eval(a); a = a.values['o']
        b = chip.inputs['b']; eval(b); b = b.values['o']
        if op == "and":
            o = 1 if a==1 and b==1 else 0
        elif op == "or":
            o = 1 if a==1 or b==1 else 0
        elif op == "xor":
            o = 1 if a!=b else 0
        # print(f'{chip.tag}({a},{b})={o}')
        chip.values = {"o":o}
    else:
        # print('chip.tag=', chip.tag)
        values = {}
        for k, v in chip.outputs.items():
            if v == chip: continue
            values[k] = eval(v)["o"]
        chip.values = values
    return chip.values

def run(chip):
    clear(chip)
    return eval(chip)

if __name__ == '__main__':
    '''
    sel = Value(1); a = Value(1); b = Value(0); c = Value(1)
    and1 = And(a,b)
    print('and1=', and1)
    print('run(and1)=', run(and1))
    or1 = Or(a,b)
    print('or1=', or1)
    print('run(or1)=', run(or1))
    mux1 = Mux(sel, a, b)
    print('mux1=', mux1)
    print('run(mux1)=', run(mux1))
    if1 = If(sel, a, b)
    print('if1=', if1)
    print('run(if1)=', run(if1))
    fa1 = FullAdder(a,b,c)
    print('fa1=', fa1)
    print('run(fa1)=', run(fa1))
    
    A1 = VALUE([1,1,0,0])
    B1 = VALUE([1,0,1,0])
    print("A1=", A1)
    print("B1=", B1)

    NOT1 = NOT(A1)
    print("NOT1=", NOT1)
    print("run(NOT(A1))=", run(NOT1))

    OR1 = OR(A1, B1)
    print("OR1=", OR1)
    print("run(OR(A1,B1))=", run(OR1))

    AND1 = AND(A1, B1)
    print("AND1=", AND1)
    print("run(AND(A1,B1))=", run(AND1))

    XOR1 = XOR(A1, B1)
    print("XOR1=", XOR1)
    print("run(XOR(A1,B1))=", run(XOR1))
    '''
    A1 = VALUE([0,1,0,0])
    B1 = VALUE([1,0,1,0])
    c = Value(1)
    ADD1 = ADD(A1, B1, c)
    print("A1=", map1(str, A1))
    print("B1=", map1(str, B1))
    print("c=", c)
    print("ADD1=", ADD1)
    print("run(ADD1)=", run(ADD1)) # run(ADD1)= {'o': [0, 0, 0, 1], 'cout': 0}, 從左到右反著看

