from src.Grafo import Grafo
from src.DFS import DFS

def main():
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('B', 'D'), ('D', 'C'), ('B', 'X'), ('X', 'D')]
    grafo = Grafo(arestas, direcionado=True)
    dfs = DFS(grafo)
    dfs.dfs()
    print(dfs.hasCycle)

main()