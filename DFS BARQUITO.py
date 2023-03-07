import matplotlib.pyplot as plt
import networkx as nx
#Iniciamos creando el grafo dado y el nodo inicial
grafo= {
    'wglf|': ['gl|fw', 'wl|fg','wg|fl'],
    'gl|fw': [],
    'wl|fg': ['wlf|g','wlfg|'],
    'wg|fl': [],
    'wlf|g': ['w|flg','l|fwg','wl|fg'],
    'wlfg|': [],
    'w|flg': ['wfl|g','wfg|l'],
    'l|fwg': ['lfw|g','lfg|w'],
    'wl|fg': [],
    'wfl|g': [],
    'wfg|l': ['g|wfl','w|flg'],
    'lfw|g': [],
    'lfg|w': ['g|flw','l|fwg'],
    'w|flg': [],
    'g|wfl': ['fg|wl'],
    'g|flw': ['fg|wl'],
    'fg|wl': ['|fgwl'],
}
inicio = 'wglf|'
final = '|fgwl'

# Función DFS para un grafo de enteros
def dfs(grafo, inicio, final):
    visitados = set()
    pila = [(inicio, 0)]  # Agregar el nivel del nodo al recorrido
    while pila:
     (nodo, camino) = pila.pop()
     if nodo not in visitados:
        if nodo == final:
           return camino
        visitados.add(nodo)
        for adyacente in grafo[nodo]:
                pila.append((adyacente, camino + [adyacente]))
    return visitados


# Función para calcular las distancias del nodo inicial a los demás nodos del grafo
def calcular_distancias(grafo, inicio):
    distancias = {inicio: 0}  # Inicializar la distancia del nodo inicial como 0
    cola = [inicio]  # Inicializar la cola con el nodo inicial
    while cola:
        nodo = cola.pop(0)
        for adyacente in grafo.get(nodo, []):
            if adyacente not in distancias:
                distancias[adyacente] = distancias[nodo] + 1
                cola.append(adyacente)
    return distancias

# Función para graficar el grafo
def graficar_nodos(grafo):
    plt.title("Grafo y sus distancias usando DFS")#Titulo al grafico de los NODOS
    G = nx.DiGraph()  # Crear un grafo dirigido y lo almacena en la variable G
    # Agregar nodos al grafo
    for nodo in grafo:#Agregamos los Nodos del grafo a la variable G
        G.add_node(nodo)
    # Agregar aristas al grafo
    for nodo, adyacentes in grafo.items():#Agrega las aristas del grafo mediante el diccionario de distancias (adyacentes)
        for adyacente in adyacentes:
            G.add_edge(nodo, adyacente)
    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    # Agregar etiquetas de distancia
    for nodo, distancia in distancias.items():
        pos_nodo = pos[nodo]
        plt.text(pos_nodo[0], pos_nodo[1]+0.1, str(distancia), horizontalalignment='center')
    plt.show()#Muestra el grafico



# Impresion de DFS, Distancia y grafico con la libreria Matplotlib
print("\nRecorrido DFS:")
dfs(grafo, inicio)
print("\nDistancia del nodo inicial:")
distancias = calcular_distancias(grafo, inicio)
for nodo, distancia in distancias.items():
   print("Nodo: {} - Distancia: {}".format(nodo, distancia))
print("\nGrafica del grafo:")
graficar_nodos(grafo)