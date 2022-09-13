import pydot

graphs = pydot.graph_from_dot_file("example.dot")
graph = graphs[0]
raw_dot = graph.to_string()
print(raw_dot)
graph.write_svg("example.svg")
