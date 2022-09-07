import random
from gateLib import *
from collections import Counter

def mapMin(goal, gateLib):
    pass

def addLibPart(gate, part, gateLib):
    partExp = part.normalForm()
    g = gateLib.find(partExp)
    if g:
        gate.partMap[partExp]=g

# 一開始先亂選 node，然後才呼叫 randomTree 遞迴生長
def randomParts(gate, glib, n): # 隨機取得 n 個子樹 (可重複取得同一個數次)。
    nodes = gate.allNodes() # 取得 gate 的所有子節點
    partMap = {} 
    for i in range(n):
        chooseNode = random.choice(nodes)
        prob = random.random()
        rTree = randomGrowTree(chooseNode, prob)
        rExp = rTree.normalForm()
        if glib.find(rExp):
            partStr = f'{chooseNode.id}:{rExp}'
            # print(partStr)
            if partMap.get(partStr) is None:
                partMap[partStr] = {'node':chooseNode, 'part':rTree}
                # print(partStr)
    return partMap

def randomGrowTree(root, prob):
    if not isinstance(root, Gate): return node
    tree = Gate(root.name, [])
    for param in root.params:
        if isinstance(param, Gate):
            child = '_' if random.random() < prob else randomGrowTree(param, prob)
        else:
            child = '_'
        tree.params.append(child)
    return tree

if __name__ == '__main__':
    glib = GateLib(gateLib)
    # glib.dump()
    # print(glib.find('not(_)'))
    # 以下這種寫法很冗長，若用 operator override 寫，應該可以短很多
    # 另外，用迪摩根定律把 and, or, not 的算式改寫成 nand+not 的優化版，應該會有需要
    goal = \
    Nand(
        Not(
            Nand(
                Not(
                    Nand(
                        Nand(Nand(a,b),
                             Not(c)
                            ),
                        Not(d)
                        )
                    ),
                Nand(
                    Not(Nand(e,f)),
                    g)
                )
            )
        ,h)
    # print(goal.normalForm())
    partMap = randomParts(goal, glib, 10000)
    print('\n'.join(partMap.keys()))
