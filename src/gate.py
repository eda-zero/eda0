class Node:
    count = 0
    def __init__(self, tag, childs=[]):
        self.id = Node.count
        self.tag = tag
        self.childs = childs
        Node.count += 1
    def __and__(self, b):
        return Node("and", [self.v, b.v])
    def __or__(self, b):
        return Node("or", [self.v, b.v])
    def __xor__(self, b):
        return Node("xor", [self.v, b.v])
    def __not__(self, b):
        return Node("not", [self.v])
    def exp(self):
        plist = []
        for child in self.childs:
            if isinstance(child, Node):
                plist.append(child.exp())
            else:
                plist.append(child)
        if len(plist)==0:
            return f"{self.tag}"
        else:
            return f"{self.tag}({','.join(plist)})"
    def allNodes(self):
        nodes = []
        allNodes(self, nodes)
        return nodes

def allNodes(node, nodes):
    nodes.append(node)
    for child in node.childs:
        if isinstance(child, Node):
            allNodes(child, nodes)

def Not(a):
    return Node("not", [a])

def Nand(a,b):
    return Node("nand", [a,b])

def And(a,b):
    return Node("and", [a,b])

def Or(a,b):
    return Node("or", [a,b])

def Xor(a,b):
    return Node("xor", [a,b])

def vars(line):
    values = line.split(" ")
    vlist = []
    for v in values:
        vlist.append(Node(v))
    return vlist
