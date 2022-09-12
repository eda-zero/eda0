from pyvis.network import Network
net = Network()
'''
for i in range(10):
    net.add_node(i, label=f"{i}")
'''
net.add_nodes(["a", "b", "c", "d"])
net.add_node("e", shape="box")
'''
g.add_nodes([1,2,3], value=[10, 100, 400],
                         title=['I am node 1', 'node 2 here', 'and im node 3'],
                         x=[21.4, 54.2, 11.2],
                         y=[100.2, 23.54, 32.1],
                         label=['NODE 1', 'NODE 2', 'NODE 3'],
                         color=['#00ff1e', '#162347', '#dd4b39'])
'''
net.add_edges([["a", "b"], ["a", "c"], ["a", "d"], ["b", "d"]])
'''
net.add_edge("a", "b")
net.add_edge("a", "c")
net.add_edge("a", "d")
net.add_edge("b", "d")
'''
net.show('net0.html')
