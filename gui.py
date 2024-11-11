import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import networkx as nx
from classes import Grafo

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Esconde a janela principal até que o usuário finalize a configuração

        self.grafo = Grafo()  # Inicializa o grafo

        # Inicializando as variáveis para direcionado e valorado
        self.direcionado = tk.BooleanVar(value=False)  # Direcionado ou não
        self.valorado = tk.BooleanVar(value=False)  # Valorado ou não

        # Configuração do menu inicial
        self.show_initial_menu()

    def show_initial_menu(self):
        """Mostra o menu inicial para seleção de tipo de grafo."""
        self.initial_window = tk.Toplevel(self.root)
        self.initial_window.title("Configuração do Grafo")

        tk.Label(self.initial_window, text="Selecione o tipo de grafo:", font=("Arial", 14)).pack(pady=10)

        # Campo para escolher se o grafo é direcionado
        tk.Label(self.initial_window, text="Grafo Direcionado:").pack()
        tk.Radiobutton(self.initial_window, text="Sim", variable=self.direcionado, value=True).pack(anchor=tk.W)
        tk.Radiobutton(self.initial_window, text="Não", variable=self.direcionado, value=False).pack(anchor=tk.W)

        # Campo para escolher se o grafo é valorado
        tk.Label(self.initial_window, text="Grafo Valorado:").pack()
        tk.Radiobutton(self.initial_window, text="Sim", variable=self.valorado, value=True).pack(anchor=tk.W)
        tk.Radiobutton(self.initial_window, text="Não", variable=self.valorado, value=False).pack(anchor=tk.W)

        # Botão para prosseguir
        self.proceed_button = tk.Button(self.initial_window, text="Prosseguir", command=self.setup_ui, bg="lightgreen")
        self.proceed_button.pack(pady=20)

    def setup_ui(self):
        """Configura a interface gráfica principal."""
        self.initial_window.destroy()  # Fecha o menu inicial

        # Agora, mostra a janela principal
        self.root.deiconify()  # Torna a janela principal visível novamente

        # Frame para entrada de vértices
        vertex_frame = ttk.LabelFrame(self.root, text="Adicionar Vértice Ex: (A)")
        vertex_frame.pack(padx=10, pady=10, fill="both", expand="yes")
        
        self.vertice_entry = tk.Entry(vertex_frame)
        self.vertice_entry.pack(padx=10, pady=10)
        self.add_vertice_button = tk.Button(vertex_frame, text="Adicionar Vértice", command=self.adicionar_vertice, bg="lightblue")
        self.add_vertice_button.pack(pady=5)

        # Frame para entrada de arestas
        edge_frame = ttk.LabelFrame(self.root, text="Adicionar Aresta Ex: (A B 2)")
        edge_frame.pack(padx=10, pady=10, fill="both", expand="yes")

        self.aresta_entry = tk.Entry(edge_frame)
        self.aresta_entry.pack(padx=10, pady=10)
        self.add_aresta_button = tk.Button(edge_frame, text="Adicionar Aresta", command=self.adicionar_aresta, bg="lightblue")
        self.add_aresta_button.pack(pady=5)

        # Frame para inserção em lote
        batch_frame = ttk.LabelFrame(self.root, text="Inserir em Lote Ex:(A, B 2; B C 3)")
        batch_frame.pack(padx=10, pady=10, fill="both", expand="yes")

        self.batch_entry = tk.Entry(batch_frame)
        self.batch_entry.pack(padx=10, pady=10)
        self.batch_button = tk.Button(batch_frame, text="Adicionar em Lote", command=self.adicionar_em_lote, bg="lightblue")
        self.batch_button.pack(pady=5)

        # Botão para visualizar o grafo
        self.visualizar_button = tk.Button(self.root, text="Visualizar Grafo", command=self.visualizar_grafo, bg="lightblue")
        self.visualizar_button.pack(pady=5)

        # Botão para obter informações do grafo
        self.info_button = tk.Button(self.root, text="Obter Informações do Grafo", command=self.mostrar_informacoes, bg="lightblue")
        self.info_button.pack(pady=5)

        # Novo botão para mostrar adjacentes e grau
        self.adjacente_grau_button = tk.Button(self.root, text="Mostrar Adjacentes e Grau", command=self.show_adjacentes_grau, bg="lightblue")
        self.adjacente_grau_button.pack(pady=5)

        # Novo botão para verificar se dois vértices são adjacentes
        self.verificar_adj_button = tk.Button(self.root, text="Verificar Adjacência", command=self.verificar_adjacencia, bg="lightblue")
        self.verificar_adj_button.pack(pady=5)

        # Novo botão para limpar o grafo
        self.limpar_grafo_button = tk.Button(self.root, text="Limpar Grafo", command=self.limpar_grafo, bg="lightcoral")
        self.limpar_grafo_button.pack(pady=5)

        # Label de status
        self.result_label = tk.Label(self.root, text="", fg="green")
        self.result_label.pack(pady=10)

    def limpar_grafo(self):
        """Limpa todos os vértices e arestas do grafo."""
        self.grafo.vertices.clear()  # Limpa o dicionário de vértices
        self.grafo.arestas.clear()  # Limpa a lista de arestas
        self.result_label.config(text="Grafo limpo com sucesso!")

    def show_adjacentes_grau(self):
        """Abre uma nova tela onde o usuário pode inserir um vértice e ver seus adjacentes e grau."""
        self.adjacente_grau_window = tk.Toplevel(self.root)
        self.adjacente_grau_window.title("Adjacentes e Grau")

        # Entrada de vértice
        self.adjacente_vertice_label = tk.Label(self.adjacente_grau_window, text="Inserir Vértice:")
        self.adjacente_vertice_label.pack(pady=5)
        self.adjacente_vertice_entry = tk.Entry(self.adjacente_grau_window)
        self.adjacente_vertice_entry.pack(pady=5)
        
        # Botão para verificar adjacentes e grau
        self.check_button = tk.Button(self.adjacente_grau_window, text="Verificar", command=self.verificar_adjacentes_grau, bg="lightblue")
        self.check_button.pack(pady=5)

        # Resultado
        self.adjacente_result_label = tk.Label(self.adjacente_grau_window, text="")
        self.adjacente_result_label.pack(pady=10)

    def verificar_adjacentes_grau(self):
        """Verifica os adjacentes e o grau do vértice inserido."""
        vertice = self.adjacente_vertice_entry.get().strip()

        if vertice not in self.grafo.vertices:
            self.adjacente_result_label.config(text="Vértice não encontrado!")
            return

        adjacentes_entrada = self.grafo.adjacentes_entrada(vertice) if self.direcionado.get() else self.grafo.adjacentes(vertice)
        adjacentes_saida = self.grafo.adjacentes_saida(vertice) if self.direcionado.get() else adjacentes_entrada
        grau = self.grafo.grau(vertice, self.direcionado.get())

        adjacentes_texto = f"Adjacentes de Entrada: {', '.join(adjacentes_entrada)}\n" if adjacentes_entrada else ""
        adjacentes_texto += f"Adjacentes de Saída: {', '.join(adjacentes_saida)}\n" if adjacentes_saida else ""
        grau_texto = f"Grau de {vertice}: {grau}"

        self.adjacente_result_label.config(text=f"{adjacentes_texto}{grau_texto}")

    def adicionar_vertice(self):
        nome = self.vertice_entry.get()
        self.grafo.adicionar_vertice(nome)
        self.vertice_entry.delete(0, tk.END)  # Limpa o campo de entrada
        self.result_label.config(text=f"Vértice '{nome}' adicionado com sucesso!")

    def adicionar_aresta(self):
        dados = self.aresta_entry.get().split()
        if len(dados) < 2:
            self.result_label.config(text="Por favor, insira 'vertice1 vertice2 [peso]'.")
            return

        nome1, nome2 = dados[0], dados[1]
        
        if self.valorado.get():
            peso = float(dados[2]) if len(dados) == 3 else 1  
        else:
            peso = 0  # Para grafo não valorizado, não precisa de peso

        if self.direcionado.get():
            self.grafo.adicionar_aresta(nome1, nome2, peso)  # Adiciona aresta direcionada
        else:
            self.grafo.adicionar_aresta(nome1, nome2, peso)  # Adiciona aresta não direcionada

        self.aresta_entry.delete(0, tk.END)  # Limpa o campo de entrada
        self.result_label.config(text=f"Aresta de '{nome1}' a '{nome2}' adicionada com peso {peso}!")

    def adicionar_em_lote(self):
        dados = self.batch_entry.get().strip().split(';')
        if len(dados) < 2:
            self.result_label.config(text="Formato inválido. Use: 'vértice1, vértice2; aresta1 aresta2 peso; ...'")
            return
        
        vertices = dados[0].split(',')
        for vertice in vertices:
            self.grafo.adicionar_vertice(vertice.strip())

        for aresta in dados[1:]:
            aresta_info = aresta.split()
            if len(aresta_info) >= 2:
                nome1, nome2 = aresta_info[0], aresta_info[1]
                peso = float(aresta_info[2]) if self.valorado.get() and len(aresta_info) == 3 else 1
                if self.direcionado.get():
                    self.grafo.adicionar_aresta(nome1.strip(), nome2.strip(), peso)
                else:
                    self.grafo.adicionar_aresta(nome1.strip(), nome2.strip(), peso)

        self.batch_entry.delete(0, tk.END)
        self.result_label.config(text="Vértices e arestas adicionados com sucesso!")

    def checar_adjacencia(self):
        """Checa se os dois vértices inseridos são adjacentes."""
        vertice1 = self.vertice1_entry.get().strip()
        vertice2 = self.vertice2_entry.get().strip()

        # Verifica se ambos os vértices existem no grafo
        if vertice1 not in self.grafo.vertices or vertice2 not in self.grafo.vertices:
            self.adjacencia_result_label.config(text="Um ou ambos os vértices não existem no grafo.")
            return

        # Verifica se são adjacentes
        if vertice2 in self.grafo.vertices[vertice1].adjacentes:
            self.adjacencia_result_label.config(text=f"Os vértices {vertice1} e {vertice2} são adjacentes!")
        else:
            self.adjacencia_result_label.config(text=f"Os vértices {vertice1} e {vertice2} não são adjacentes.")

    def verificar_adjacencia(self):
        """Verifica se dois vértices são adjacentes."""
        # Criar uma nova janela para a entrada dos dois vértices
        self.adjacencia_window = tk.Toplevel(self.root)
        self.adjacencia_window.title("Verificar Adjacência")

        # Entrada para o primeiro vértice
        self.vertice1_label = tk.Label(self.adjacencia_window, text="Inserir primeiro vértice:")
        self.vertice1_label.pack(pady=5)
        self.vertice1_entry = tk.Entry(self.adjacencia_window)
        self.vertice1_entry.pack(pady=5)

        # Entrada para o segundo vértice
        self.vertice2_label = tk.Label(self.adjacencia_window, text="Inserir segundo vértice:")
        self.vertice2_label.pack(pady=5)
        self.vertice2_entry = tk.Entry(self.adjacencia_window)
        self.vertice2_entry.pack(pady=5)

        # Botão para verificar adjacência
        self.check_adj_button = tk.Button(self.adjacencia_window, text="Verificar Adjacência", command=self.checar_adjacencia, bg="lightblue")
        self.check_adj_button.pack(pady=5)

        # Resultado
        self.adjacencia_result_label = tk.Label(self.adjacencia_window, text="")
        self.adjacencia_result_label.pack(pady=10)






    def visualizar_grafo(self):
        G = nx.DiGraph() if self.direcionado.get() else nx.Graph()
        for vertice in self.grafo.vertices:
            G.add_node(vertice)
        for aresta in self.grafo.arestas:
            G.add_edge(aresta.vertice1, aresta.vertice2, weight=aresta.peso)

        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        if edge_labels:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Visualização do Grafo")
        plt.show()

    def mostrar_informacoes(self):
        ordem = self.grafo.ordem()
        tamanho = self.grafo.tamanho()
        messagebox.showinfo("Informações do Grafo", f"Ordem: {ordem}\nTamanho: {tamanho}")

    def run(self):
        self.root.mainloop()  # Inicia a interface

# Para executar a aplicação, você pode adicionar:
if __name__ == "__main__":
    app = App()
    app.run()
