import random
from node import *
from chips import *
from gateLib import *
from collections import Counter
from improveLoop import *
import sys

def costMin(goal, gateLib):
    nodes = goal.allNodes() # 取得 gate 的所有子節點
    singleMap = singlePartMap(nodes, gateLib)
    sol = {'goal':goal, 'nodes':nodes, 'singleMap':singleMap, 
           'partMap':singleMap, 'cost':cost(singleMap)}
    print('cost=', sol['cost'])
    printPartMap(singleMap)
    improveLoop(sol, partImprove, 10000, 1000)

def printPartMap(partMap):
    for part in partMap.values():
        g = part['libGate']
        print(part['rootId'], part['nidSet'], g['name'], g['area'])

def cost(partMap):
    totalCost = 0
    for part in partMap.values():
        libGate = part['libGate']
        totalCost += libGate['area']
    return totalCost

successCount = 0

def partImprove(sol):
    global successCount
    goal = sol['goal']; nodes = sol['nodes']; singleMap = sol['singleMap']; 
    partMap = sol['partMap']; costNow = sol['cost']
    # print('sol=', sol)
    # sys.exit(1)
    addPartExp = ''
    while addPartExp.count('(')<2:
        pickNode = random.choice(nodes)
        prob = random.random()
        addPart = randomGrowTree(pickNode, prob)
        addPartExp = addPart.exp()
    # print('addPartExp=', addPartExp)
    # sys.exit(1)
    libGate = glib.findByExp(addPartExp)
    if libGate is None: return False
    # print('libGate=', libGate)
    # 創建新的分割 (newPartMap)
    newPartMap = partMap.copy()
    addPartSet = set()
    for node in addPart.allNodes():
        addPartSet.add(node.id)
    # print('addPartSet=', addPartSet)
    removeSet = set()
    # 將所有衝突的 parts 都移除
    for part in partMap.values():
        if addPartSet.intersection(part['nidSet']):
            newPartMap.pop(part['rootId'], None)
            # print('remove:id=', part['rootId'], 'area=', part['libGate']['area'])
            removeSet = removeSet.union(part['nidSet'])
    # 將新的 newPart 加入 newPartMap
    newPartMap[addPart.id] = {
        'rootId':addPart.id,
        'part': addPart,
        'libGate':libGate, 
        'nidSet': addPartSet
    }
    # 然後將移除後產生的洞用 NAND,NOT 補起來。
    # for nid in removeSet.difference(addPartSet):
    for nid in removeSet.difference(addPartSet):
        part = singleMap[nid]
        newPartMap[nid] = part
    # print('newPartMap.keys()=', newPartMap.keys())
    newCost = cost(newPartMap)
  
    if newCost >= costNow: return False
    sol['partMap'] = newPartMap; sol['cost'] = newCost
    successCount += 1
    print("==========successCount(", successCount, ")=============")
    print('removeSet=', removeSet)
    print('addPartSet=', addPartSet)
    printPartMap(newPartMap)
    print("cost=", newCost)
    return True

def singlePartMap(nodes, glib):
    partMap = {}
    for node in nodes:
        name = node.tag.upper()
        part = Node(node.tag)
        part.id = node.id
        partMap[part.id] = {
            'rootId': part.id,
            'part': part,
            'libGate':glib.findByName(name),
            'nidSet':{node.id}
        }
    return partMap

def randomGrowTree(root, prob):
    if not isinstance(root, Node): return root
    tree = Node(root.tag)
    tree.id = root.id
    for k,n in root.inputs.items():
        if isinstance(n, Node):
            n = '_' if random.random() > prob else randomGrowTree(n, prob)
        else:
            n = '_'
        tree.inputs[k] = n
    return tree

if __name__ == '__main__':
    from gateLib1 import gateLib1
    a='_'; b='_'; c='_'; d='_'; e='_'; f='_'; g='_'; h='_'
    random.seed(172346547)
    glib = GateLib(gateLib1)
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
    # print(goal.exp())
    costMin(goal, glib)
