# dot language

* http://www.graphviz.org/doc/info/lang.html
* http://www.graphviz.org/pdf/dotguide.pdf

## 安裝 cli

http://www.graphviz.org/download/

```
dot -Tps filename.dot -o outfile.ps
dot -Tsvg filename.dot -o outfile.svg
```

除了 dot 之外，還有 neato/fdp/circo/... 等 layout engine

* https://graphviz.org/docs/layouts/

其中 neato/fdp 可以指定節點位置 (pos) 。

* https://graphviz.org/docs/attrs/pos/

## 使用 pydot

參考 pydot1.py

```py
import pydot

graphs = pydot.graph_from_dot_file("example.dot")
graph = graphs[0]
raw_dot = graph.to_string()
print(raw_dot)
graph.write_svg("example.svg")
```

## more

* https://github.com/magjac/d3-graphviz
* https://stackoverflow.com/questions/11588667/how-to-influence-layout-of-graph-items
* https://stackoverflow.com/questions/64323943/graphviz-and-dot-files-horizontal-and-vertical-node-alignment-intervening-node
