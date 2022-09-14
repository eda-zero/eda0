class Node:
    count = 0
    def __init__(self, tag, inputs=[]):
        self.id = Node.count
        self.tag = tag
        self.inputs = inputs
        Node.count += 1
    def exp(self):
        nodeMap = {}
        return exp(self, nodeMap)
    def __str__(self):
        return self.exp()
    def allNodes(self):
        nodes = []
        allNodes(self, nodes)
        return nodes

def exp(node, nodeMap):
    if not isinstance(node, Node): return str(node)
    if not nodeMap.get(node.id) is None: return f"#G{node.id}"
    nodeMap[node.id] = node
    plist = []
    for input in node.inputs:
        if isinstance(input, Node):
            plist.append(exp(input, nodeMap))
        else:
            plist.append(str(input))
    if len(plist)==0: # leaf node
        return f"{node.tag}"
    else: # node with inputs
        return f"{node.tag}({','.join(plist)})"

def allNodes(node, nodes):
    nodes.append(node)
    for input in node.inputs:
        if isinstance(input, Node):
            allNodes(input, nodes)

def allNodeMap(node, nodeMap):
    if not nodeMap.get(node.id) is None:return # 不要重複展開
    nodeMap[node.id] = node
    for input in node.inputs:
        if isinstance(input, Node):
            allNodeMap(input, nodeMap)
