from collections import OrderedDict

class Node:
    count = 0
    def __init__(self, tag, inputs={}):
        self.id = Node.count
        self.tag = tag
        self.inputs = OrderedDict(inputs) # 按順序排，轉成 exp() 才會有固定順序。 self.inputs = inputs.copy()
        self.values = None
        self.outputs = {}
        Node.count += 1
    def clear():
        raise
    def eval():
        raise
    def o():
        return self.outputs.get('o')
    def exp(self):
        nodeMap = {}
        return exp(self, nodeMap)
    def str(self):
        return exp()
    def __str__(self):
        return self.str()
    def allNodes(self):
        nodes = []
        allNodes(self, nodes)
        return nodes

def exp(node, nodeMap):
    if not isinstance(node, Node): return str(node)
    if not nodeMap.get(node.id) is None: return f"#G{node.id}"
    nodeMap[node.id] = node
    plist = []
    for n in node.inputs.values():
        if isinstance(n, Node):
            plist.append(exp(n, nodeMap))
        else:
            plist.append(str(n))
    if len(plist)==0: # leaf node
        return f"{node.tag}"
    else: # node with inputs
        return f"{node.tag}({','.join(plist)})"

def allNodes(node, nodes):
    nodes.append(node)
    for node in node.inputs.values():
        if isinstance(node, Node):
            allNodes(node, nodes)

def allNodeMap(node, nodeMap):
    if not nodeMap.get(node.id) is None:return # 不要重複展開
    nodeMap[node.id] = node
    for node in node.inputs.values():
        if isinstance(node, Node):
            allNodeMap(node, nodeMap)
