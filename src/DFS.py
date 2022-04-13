from collections import defaultdict

from src.enum.Cor import Cor
from src.Grafo import Grafo

class DFS(object):
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.cor = defaultdict(lambda: Cor.BRANCO)
        self.tempo = 0
        self.timeProcess = defaultdict(list) # indice 0 = incio, indice 1 = fim
        self.hasCycle = False

    def dfs_visit(self, u):
        self.cor[u] = Cor.CINZA
        self.tempo += 1
        self.timeProcess[u].insert(0, self.tempo)
        for v in self.grafo.vizinhos(u):
            if self.cor[v] == Cor.BRANCO:
                self.dfs_visit(v)
            elif self.cor[v] == Cor.CINZA:
                self.hasCycle = True

        self.cor[u] = Cor.PRETO
        self.tempo =+ 1
        self.timeProcess[u].insert(1, self.tempo)


    def dfs(self):
        for u in self.grafo.get_vertices():
            if self.cor[u] == Cor.BRANCO:
                self.dfs_visit(u)

