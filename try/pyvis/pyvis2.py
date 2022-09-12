from pyvis.network import Network
net = Network()

net.add_nodes(["a", "b", "c", "d"], shape="box", x=0)
net.add_node("e", shape="box", x=1)

net.add_edges([["a", "b"], ["a", "c"], ["a", "d"], ["b", "d"]])

net.show('net0.html')
