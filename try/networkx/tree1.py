import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

T = nx.balanced_tree(2, 5)

# pos = graphviz_layout(T, prog="twopi")
# pos = graphviz_layout(T, prog="dot")
pos = graphviz_layout(T, prog="circo")
nx.draw(T, pos)
plt.show()
