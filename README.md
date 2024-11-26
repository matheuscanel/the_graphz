# The Graphz

**The Graphz** é uma aplicação Python que permite aos usuários criar e visualizar gráficos simples, sem arestas paralelas ou laços. Através de uma interface gráfica amigável, os usuários podem adicionar vértices e arestas, definir pesos para as arestas e visualizar o gráfico resultante em formato gráfico. A aplicação também oferece funcionalidades adicionais, como verificação de grafos direcionados, valorados, e Eulerianos.

## Requisitos do Sistema

### Funcionalidades:

1. **Criação de Grafo:**
   - O usuário pode interagir com o sistema para criar um grafo inserindo um item de cada vez (vértices e arestas).
   
2. **Criação de Grafo em Lote:**
   - O usuário pode inserir as informações em lote, ou seja, tudo de uma vez só, como um arquivo ou um grande string com as informações de todos os vértices e arestas.
   
3. **Grafo Direcionado e Valorado:**
   - O usuário pode criar grafos direcionados ou não-direcionados, e grafos valorados ou não-valorados.

4. **Visualização do Grafo:**
   - O usuário poderá visualizar o grafo em formato textual (como uma lista de adjacência, matriz de adjacência) ou gráfico, com a opção de exibir como imagem na tela ou permitir o download do arquivo de imagem. 

5. **Informações do Grafo:**
   - O usuário poderá obter informações sobre a ordem e o tamanho do grafo criado.

6. **Lista de Vértices Adjacentes:**
   - O sistema informará a lista de vértices adjacentes de um dado vértice. Para grafos direcionados, será possível informar tanto a lista de vértices adjacentes de entrada quanto a lista de vértices adjacentes de saída.

7. **Grau de um Vértice:**
   - O sistema informará o grau de um vértice. Para grafos direcionados, o grau será apresentado separadamente como grau de entrada e grau de saída. 

8. **Verificação de Adjacência:**
   - O sistema informará se dois vértices são adjacentes ou não. 

9. **Caminho Mais Curto:**
   - O sistema informará o caminho mais curto entre dois vértices, incluindo o valor do custo do menor caminho e a sequência de vértices desse caminho. Considera-se que os pesos das arestas são sempre números positivos (não há arestas com pesos negativos). 

10. **Verificação de Grafo Euleriano:**
    - O sistema deverá informar se o grafo criado no sistema é um Grafo Euleriano ou não. 

## Como executar a aplicação:

#### Passo a Passo para Configuração e Execução:

1. **Baixar o repositório:**
   - Baixe o repositório ou faça o download do arquivo ZIP através do [GitHub](#).

2. **Criar um ambiente virtual:**
   - Crie um ambiente virtual para isolar as dependências do projeto, utilizando o seguinte comando no terminal:

     **No Windows:**
     ```bash
     python -m venv venv
     ```

     **No macOS ou Linux:**
     ```bash
     python3 -m venv venv
     ```

3. **Ativar o ambiente virtual:**
   - Ative o ambiente virtual para começar a trabalhar com ele.

     **No Windows:**
     ```bash
     venv\Scripts\activate
     ```

     **No macOS ou Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Instalar as dependências:**
   - Instale todas as dependências necessárias para o projeto com o comando:

     ```bash
     pip install -r requirements.txt
     ```

     Isso instalará todas as bibliotecas listadas no arquivo `requirements.txt`, como `tkinter`, `networkx`, `matplotlib`, entre outras.

5. **Executar a aplicação:**
   - Agora, basta rodar o arquivo `main.py` para iniciar a aplicação. Execute o seguinte comando no terminal:

     **No Windows:**
     ```bash
     python main.py
     ```

     **No macOS ou Linux:**
     ```bash
     python3 main.py
     ```

   Isso iniciará a interface gráfica onde você poderá criar e visualizar gráficos.

### Dependências

As dependências necessárias para o funcionamento da aplicação estão listadas no arquivo `requirements.txt`. Se você seguir o passo 4, elas serão automaticamente instaladas.
