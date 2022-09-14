# from chips import *

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
