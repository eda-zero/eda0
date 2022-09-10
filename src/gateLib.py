class Gate:
    count = 0
    def __init__(self, op, params):
        self.op = op
        self.params = params
        self.id = Gate.count
        Gate.count += 1
    def exp(self):
        plist = []
        for param in self.params:
            if isinstance(param, Gate):
                plist.append(param.exp())
            else:
                plist.append(param)
        return f"{self.op}({','.join(plist)})"
    def allNodes(self):
        nodes = []
        allNodes(self, nodes)
        return nodes

def allNodes(gate, nodes):
    nodes.append(gate)
    for param in gate.params:
        if isinstance(param, Gate):
            allNodes(param, nodes)

def Not(a):
    return Gate("not", [a])

def Nand(a,b):
    return Gate("nand", [a,b])

class GateLib:
    def __init__(self, gateLib):
        self.gateLib = gateLib
        self.nameMap = {}
        self.expMap = {}
        for name, array in gateLib.items():
            area = array[0]; gates=array[1:]
            for gate in gates:
                g = {'name':name, 'area':area, 'gate':gate }
                self.nameMap[name] = g
                self.expMap[gate.exp()] = g

    def dump(self):
        for name, array in gateLib.items():
            area = array[0]; gates=array[1:]
            print(name, ' ', area, end =" ")
            for g in gates:
                print(g.exp(), end=" ")
            print()

    def findByName(self, name):
        return self.nameMap.get(name)

    def findByExp(self, exp):
        # gexp = g.exp() if isinstance(g, Gate) else g
        # return self.gmap.get(gexp)
        return self.expMap.get(exp)

a = "_"; b= "_"; c="_"; d="_"; e="_"; f="_"; g="_"; h="_"

gateLib = {
"NOT"    :[2, Not(a)],
"NAND"   :[3, Nand(a,b)],
"NAND3"  :[4, Nand(Not(Nand(a,b)),c)],
"NAND4"  :[5, Nand(Not(Nand(Not(Nand(a,b)),c)),d),
              Nand(Not(Nand(a,b)),Not(Nand(c,d)))],
"AOI21"  :[4, Not(Nand(Nand(a,b),Not(c)))],
"AOI22"  :[5, Not(Nand(Nand(a,b),Nand(c,d)))]
}

if __name__ == '__main__':
    glib = GateLib(gateLib)
    glib.dump()
    print('NAND=', glib.findByName('NAND'))
    print('NAND4=', glib.findByName('NAND4'))
    print('not(_)=', glib.findByExp('not(_)'))
    print('nand(not(nand(not(nand(_,_)),_)),_)=', glib.findByExp('nand(not(nand(not(nand(_,_)),_)),_)'))
    print('exp:xxx=', glib.findByExp('exp:xxx'))
    print('name:xxx=', glib.findByName('name:xxx'))

