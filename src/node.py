class Node:
    count = 0
    def __init__(self, tag, childs=[]):
        self.id = Node.count
        self.tag = tag
        self.childs = childs
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
    for child in node.childs:
        if isinstance(child, Node):
            plist.append(exp(child, nodeMap))
        else:
            plist.append(str(child))
    if len(plist)==0: # leaf node
        return f"{node.tag}"
    else: # node with childs
        return f"{node.tag}({','.join(plist)})"

def allNodes(node, nodes):
    nodes.append(node)
    for child in node.childs:
        if isinstance(child, Node):
            allNodes(child, nodes)

def allNodeMap(node, nodeMap):
    if not nodeMap.get(node.id) is None:return # 不要重複展開
    nodeMap[node.id] = node
    for child in node.childs:
        if isinstance(child, Node):
            allNodeMap(child, nodeMap)
