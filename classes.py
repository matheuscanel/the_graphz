# Vértice
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
            aresta = Aresta(nome1, nome2, peso)  # Cria uma nova aresta entre os dois vértices
            self.arestas.append(aresta)  # Adiciona a aresta à lista de arestas

            # Adiciona o vértice adjacente na lista de adjacência de cada vértice
            self.vertices[nome1].adjacentes.append(nome2)  # Para vértice1
            self.vertices[nome2].adjacentes.append(nome1)  # Para vértice2 
            print(f"Aresta de '{nome1}' a '{nome2}' adicionada com peso {peso}.")
        else:
            print("Um ou ambos os vértices não existem.")  # Informa que um ou mais vértices não estão presentes

    def adjacentes(self, vertice):
        """Retorna a lista de vértices adjacentes a um vértice (para grafos não direcionados)."""
        if vertice in self.vertices:
            return self.vertices[vertice].adjacentes
        return []

    def adjacentes_entrada(self, vertice):
        """Retorna a lista de vértices adjacentes de entrada (para grafos direcionados)."""
        adjacentes_entrada = []
        for aresta in self.arestas:
            if aresta.vertice2 == vertice:
                adjacentes_entrada.append(aresta.vertice1)
        return adjacentes_entrada

    def adjacentes_saida(self, vertice):
        """Retorna a lista de vértices adjacentes de saída (para grafos direcionados)."""
        adjacentes_saida = []
        for aresta in self.arestas:
            if aresta.vertice1 == vertice:
                adjacentes_saida.append(aresta.vertice2)
        return adjacentes_saida

    def grau(self, vertice, direcionado):
        """Retorna o grau de um vértice, considerando se o grafo é direcionado ou não."""
        if direcionado:
            # Para grafos direcionados, o grau é a soma dos adjacentes de entrada e saída
            return len(self.adjacentes_entrada(vertice)) + len(self.adjacentes_saida(vertice))
        else:
            # Para grafos não direcionados, o grau é o número de adjacentes
            return len(self.adjacentes(vertice))

    def ordem(self):
        """Retorna a ordem do grafo (número de vértices)."""
        return len(self.vertices)

    def tamanho(self):
        """Retorna o tamanho do grafo (número de arestas)."""
        return len(self.arestas)

