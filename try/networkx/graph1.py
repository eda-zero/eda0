import networkx as nx
import pylab as plt
ER = nx.random_graphs.erdos_renyi_graph(10, 0.3)
pos = nx.shell_layout(ER)
s = [str(i) for i in range(1,11)]
s = dict(zip(range(10), s))
nx.draw(ER, pos, labels=s); plt.show()
