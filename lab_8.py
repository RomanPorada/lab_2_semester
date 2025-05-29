import csv
import matplotlib.pyplot as plt
import networkx as nx

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_b] = root_a
        return True

def read_edges_from_csv(filename):
    edges = []
    nodes = set()

    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                continue
            k1, k2, dist_str = row
            try:
                dist = int(dist_str)
            except ValueError:
                continue
            edges.append((dist, k1, k2))
            nodes.update([k1, k2])
    return edges, nodes

def draw_graph(edges, title, mst_edges=None):
    G = nx.Graph()
    for dist, u, v in edges:
        G.add_edge(u, v, weight=dist)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if mst_edges:
        mst_graph = nx.Graph()
        for dist, u, v in mst_edges:
            mst_graph.add_edge(u, v)
        nx.draw_networkx_edges(G, pos, edgelist=mst_graph.edges(), edge_color='red', width=2)

    plt.title(title)
    plt.axis('off')
    plt.show()

def kruskal_mst(filename):
    edges, nodes = read_edges_from_csv(filename)
    if not nodes:
        return -1

    for i in range(len(edges)):
        for j in range(0, len(edges)-i-1):
            if edges[j] > edges[j+1]:
                edges[j], edges[j+1] = edges[j+1], edges[j]

    uf = UnionFind(nodes)
    mst_weight = 0
    mst_edges = []

    for dist, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((dist, u, v))
            mst_weight += dist
            if len(mst_edges) == len(nodes) - 1:
                break

    root_set = set(uf.find(node) for node in nodes)
    if len(root_set) > 1:
        return -1, edges, []
    return mst_weight, edges, mst_edges

if __name__ == "__main__":
    filename = 'communication_wells.csv'
    result, all_edges, mst_edges = kruskal_mst(filename)

    print("Вага мінімального остового дерева (MST):", result if result != -1 else "Граф не зв'язний")

    draw_graph(all_edges, "Повний граф з файлу", mst_edges=None)
    draw_graph(all_edges, "Мінімальне остове дерево (MST)", mst_edges=mst_edges)
