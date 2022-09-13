from pyvis.network import Network
net = Network("500px", "500px")
net.from_DOT("./test.dot")
net.show("test.html")