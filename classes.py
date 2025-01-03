import heapq  # Adicione esta linha para importar o módulo heapq

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

    def caminho_mais_curto(self, origem, destino):
        """Usa o algoritmo de Dijkstra para calcular o caminho mais curto entre dois vértices."""
        if origem not in self.vertices or destino not in self.vertices:
            return None, None  # Retorna None se algum vértice não existir

        # Inicializa a distância de todos os vértices como infinita
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[origem] = 0  # A distância para a origem é 0

        # Inicializa o dicionário para armazenar os predecessores de cada vértice
        predecessores = {vertice: None for vertice in self.vertices}

        # Fila de prioridade (min-heap) para selecionar o próximo vértice a ser visitado
        fila = [(0, origem)]  # (distância, vértice)

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            # Se chegamos no destino, paramos
            if vertice_atual == destino:
                break

            for vizinho in self.adjacentes(vertice_atual):
                # Calcular o custo da aresta entre o vértice atual e o vizinho
                peso_aresta = next(aresta.peso for aresta in self.arestas
                                   if (aresta.vertice1 == vertice_atual and aresta.vertice2 == vizinho) or
                                   (aresta.vertice2 == vertice_atual and aresta.vertice1 == vizinho))
                nova_distancia = distancia_atual + peso_aresta

                # Se encontramos uma distância melhor, atualizamos
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        # Reconstruir o caminho a partir do destino
        caminho = []
        atual = destino
        while atual is not None:
            caminho.insert(0, atual)
            atual = predecessores[atual]

        # Se o caminho para o destino não foi encontrado, retorna None
        if distancias[destino] == float('inf'):
            return None, None

        return caminho, distancias[destino]


    def euleriano(self):
        """Verifica se o grafo é Euleriano."""
        # Verifica se todos os vértices têm grau par
        for vertice in self.vertices.values():
            if len(self.adjacentes(vertice.nome)) % 2 != 0:
                return False  # Se algum vértice tiver grau ímpar, não é Euleriano

        # Verifica se o grafo é conexo (apenas para grafos não direcionados)
        if not self.grafo_conexo():
            return False

        return True

    def grafo_conexo(self):
        """Verifica se o grafo é conexo (apenas para grafos não direcionados)."""
        visitados = set()

        def dfs(v):
            visitados.add(v)
            for adj in self.adjacentes(v):
                if adj not in visitados:
                    dfs(adj)

        # Começa a busca em profundidade a partir de qualquer vértice
        if self.vertices:
            dfs(next(iter(self.vertices)))

        # Verifica se todos os vértices foram visitados
        return len(visitados) == len(self.vertices)