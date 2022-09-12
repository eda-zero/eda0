class Node:
    count = 0
    def __init__(self, tag, childs=[]):
        self.id = Node.count
        self.tag = tag
        self.childs = childs
        Node.count += 1
    def exp(self):
        plist = []
        for child in self.childs:
            if isinstance(child, Node):
                plist.append(child.exp())
            else:
                plist.append(child)
        if len(plist)==0: # leaf node
            return f"{self.tag}"
        else: # node with childs
            return f"{self.tag}({','.join(plist)})"
    def __str__(self):
        return self.exp()
    def allNodes(self):
        nodes = []
        allNodes(self, nodes)
        return nodes

def allNodes(node, nodes):
    nodes.append(node)
    for child in node.childs:
        if isinstance(child, Node):
            allNodes(child, nodes)
