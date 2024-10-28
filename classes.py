# Vertice
class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []

# Aresta
class Aresta:
    def __init__(self, vertice1, vertice2, peso=1):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso

# Grafo
class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []

    def adicionar_vertice(self, nome):

        # Verifica se o vértice já existe
        if nome not in self.vertices:
            vertice = Vertice(nome)  # Cria um novo objeto Vértice
            self.vertices[nome] = vertice  # Adiciona o vértice ao dicionário
            print(f"Vértice '{nome}' adicionado.")

        else:
            print(f"Vértice '{nome}' já existe.")  # Informa que o vértice já está presente

    def adicionar_aresta(self, nome1, nome2, peso=1):

          # Verifica se ambos os vértices existem no grafo
        if nome1 in self.vertices and nome2 in self.vertices:
            aresta = Aresta(nome1, nome2, peso) # Cria uma nova aresta entre os dois vértices
            self.arestas.append(aresta)  # Adiciona a aresta à lista de arestas

            # Adiciona o vértice adjacente na lista de adjacência de cada vértice
            self.vertices[nome1].adjacentes.append(nome2)  # Para vértice1
            self.vertices[nome2].adjacentes.append(nome1)  # Para vértice2 
            print(f"Aresta de '{nome1}' a '{nome2}' adicionada com peso {peso}.")

        else:
            print("Um ou ambos os vértices não existem.")  # Informa que um ou mais vértices não estão presentes
