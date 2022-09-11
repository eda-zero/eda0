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
        for name, array in self.gateLib.items():
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
