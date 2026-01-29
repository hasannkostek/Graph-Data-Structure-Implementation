# Graph Data Structure Implementation 📊

Bu proje, **Veri Yapıları** dersi kapsamında Python kullanılarak **Graph (Çizge)** veri yapısının sıfırdan (from scratch) implementasyonunu içerir. Herhangi bir hazır kütüphane kullanılmadan, nesne yönelimli yaklaşımla geliştirilmiştir.

## 🚀 Özellikler
Bu Graph sınıfı aşağıdaki yapıları destekler:
* **Weighted / Unweighted:** Ağırlıklı veya ağırlıksız kenarlar.
* **Directed / Undirected:** Yönlü veya yönsüz bağlantılar.

## 🛠️ Metotlar (Methods)
* `addNode(nodeName)`: Grafa yeni bir düğüm ekler.
* `addEdge(node1, node2, weight)`: İki düğüm arasında bağlantı kurar.
* `removeNode(nodeName)`: Düğümü ve bağlantılarını siler.
* `removeEdge(node1, node2)`: Bağlantıyı kaldırır.
* **Traversal:** (Varsa) BFS ve DFS algoritmaları entegre edilmiştir.

## 💻 Kullanım Örneği
```python
from graph_structure import Graph

# Yönlü ve Ağırlıklı bir graf oluştur
myGraph = Graph(weighted=True, directed=True)

myGraph.addNode("A")
myGraph.addNode("B")
myGraph.addEdge("A", "B", 10)
```

👨‍💻 Geliştirici
Hasan Köstek
