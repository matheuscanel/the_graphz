import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from classes import Grafo

class App:
    def __init__(self):
        self.grafo = Grafo()  # Inicializa o grafo
        self.root = tk.Tk()
        self.root.title("The Graphz - Criar Grafo")

        # Configurar a interface gráfica
        self.setup_ui()

    def setup_ui(self):
        # Campo para inserir o nome do vértice
        self.vertice_label = tk.Label(self.root, text="Adicionar Vértice:")
        self.vertice_label.pack()
        self.vertice_entry = tk.Entry(self.root)
        self.vertice_entry.pack()
        self.add_vertice_button = tk.Button(self.root, text="Adicionar Vértice", command=self.adicionar_vertice)
        self.add_vertice_button.pack()

        # Campo para inserir arestas
        self.aresta_label = tk.Label(self.root, text="Adicionar Aresta (formato: vertice1 vertice2 peso):")
        self.aresta_label.pack()
        self.aresta_entry = tk.Entry(self.root)
        self.aresta_entry.pack()
        self.add_aresta_button = tk.Button(self.root, text="Adicionar Aresta", command=self.adicionar_aresta)
        self.add_aresta_button.pack()

        # Botão para visualizar o grafo
        self.visualizar_button = tk.Button(self.root, text="Visualizar Grafo", command=self.visualizar_grafo)
        self.visualizar_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def adicionar_vertice(self):
        nome = self.vertice_entry.get()
        self.grafo.adicionar_vertice(nome)
        self.vertice_entry.delete(0, tk.END)  # Limpa o campo de entrada
        self.result_label.config(text=f"Vértice '{nome}' adicionado com sucesso!")

    def adicionar_aresta(self):
        dados = self.aresta_entry.get().split()
        if len(dados) == 3:
            nome1, nome2, peso = dados[0], dados[1], dados[2]
            try:
                peso = float(peso)  # Converte o peso para float
                self.grafo.adicionar_aresta(nome1, nome2, peso)
                self.aresta_entry.delete(0, tk.END)  # Limpa o campo de entrada
                self.result_label.config(text=f"Aresta de '{nome1}' a '{nome2}' adicionada com peso {peso}!")
            except ValueError:
                self.result_label.config(text="Por favor, insira um peso válido.")
        else:
            self.result_label.config(text="Por favor, insira 'vertice1 vertice2 peso'.")

    def visualizar_grafo(self):
        G = nx.Graph()  # Cria um novo grafo não-direcionado
        for vertice in self.grafo.vertices:
            G.add_node(vertice)  # Adiciona vértices
        for aresta in self.grafo.arestas:
            G.add_edge(aresta.vertice1, aresta.vertice2, weight=aresta.peso)  # Adiciona arestas

        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)  # Define a posição dos nós
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Visualização do Grafo")
        plt.show()  # Exibe o grafo

    def run(self):
        self.root.mainloop()  # Inicia a interface
