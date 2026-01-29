#GRAPH-PYTHON  HASAN KÖSTEK-22370031028
#VERİ ÖDEVİ#
class Graph:
    def __init__(self, weighted, directed):
        self.weighted = weighted
        self.directed = directed
        self.graphDict = {}

    def addNode(self, nodeName):
        if nodeName not in self.graphDict:
            self.graphDict[nodeName] = []

    def addEdge(self, node1, node2, weight):
        if node1 not in self.graphDict or node2 not in self.graphDict:
            return

        if self.directed is False:
            self.graphDict[node1].append((node2, weight))
            self.graphDict[node2].append((node1, weight))
        else:
            self.graphDict[node1].append((node2, weight))

# Graph sınıfının bir örneğini oluşturun
gr = Graph(False, False)   #Burada F-F yi değiştirebiliriz.(T-T,T-F de yapabiliriz.)

# Düğüm ekle
gr.addNode("A")
gr.addNode("B")
gr.addNode("C")
gr.addNode("D")
gr.addNode("E")

# Kenar ekle
gr.addEdge("A", "B", -1)
gr.addEdge("A", "C", -1)
gr.addEdge("A", "D", -1)
gr.addEdge("B", "D", -1)
gr.addEdge("E", "D", -1)
gr.addEdge("C", "D", -1)
gr.addEdge("D", "D", -1)

# Grafiği yazdır
for key, value in gr.graphDict.items():
    print(key + " => ", end=(' '))
    for i in value:
        print(str(i[0]) + " : " + str(i[1]), end=(' '))
    print("")
