import matplotlib.pyplot as plt
import networkx as nx

# 1. Criar o grafo direcionado
G = nx.DiGraph()

# 2. Adicionar as conexões entre páginas (arestas)
edges = [('1', '2'), ('1', '3'), ('2','1') , ('2', '3'), ('2', '4'), ('3', '1'), ('3','4'), ('4','1'), ('4', '2') ]
G.add_edges_from(edges)

# 3. Layout dos nós no plano 2D
pos = nx.spring_layout(G, seed=42)  # layout com física de mola (reprodutível)

# 4. Desenhar o grafo
plt.figure(figsize=(6, 4))
nx.draw_networkx(G, pos,
                 node_color='skyblue',
                 arrows=True,
                 with_labels=True,
                 edge_color='gray')

# 5. Ajustes visuais
plt.title("Grafo de Páginas e Links")
plt.axis('off')
plt.tight_layout()

# 6. Salvar a imagem
plt.savefig('web_grafo.png')
plt.show()
