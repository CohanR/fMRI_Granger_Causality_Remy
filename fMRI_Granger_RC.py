import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import grangercausalitytests
import seaborn as sns
import networkx as nx

# Data generation
np.random.seed(0)
roi1 = np.random.randn(100)
roi2 = roi1 + np.random.randn(100) * 0.5
roi3 = np.roll(roi1, shift=2) + np.random.randn(100)
data = np.column_stack([roi1, roi2, roi3])

# Plot the data
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(roi1, label="ROI 1")
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(roi2, label="ROI 2")
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(roi3, label="ROI 3")
plt.legend()
plt.tight_layout()
plt.show()

# Granger causality test
max_lag = 5
roi_names = ["ROI 1", "ROI 2", "ROI 3"]
gc_values = {}
for i in range(data.shape[1]):
    for j in range(data.shape[1]):
        if i != j:
            print(f"Testing if {roi_names[j]} Granger-causes {roi_names[i]}:")
            gc_test = grangercausalitytests(data[:, [j, i]], max_lag, verbose=True)
            min_p_value = min([test[0]['ssr_ftest'][1] for test in gc_test.values()])
            gc_values[(roi_names[j], roi_names[i])] = min_p_value

# Visualize Granger causality relationships with edge labels
gc_graph = nx.DiGraph()
for roi in roi_names:
    gc_graph.add_node(roi)

significance_level = 0.05
for (roi_j, roi_i), p_value in gc_values.items():
    if p_value < significance_level:
        gc_graph.add_edge(roi_j, roi_i, weight=-np.log10(p_value))

plt.figure(figsize=(10, 8))
pos_gc = nx.circular_layout(gc_graph)
nx.draw_networkx_nodes(gc_graph, pos_gc, node_size=3000, node_color='lightcoral')
nx.draw_networkx_labels(gc_graph, pos_gc, font_size=15)
edges = nx.draw_networkx_edges(gc_graph, pos_gc, arrowstyle='-|>', arrowsize=20)
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in gc_graph.edges(data=True)}
nx.draw_networkx_edge_labels(gc_graph, pos_gc, edge_labels=edge_labels, font_size=10)
plt.title("Granger Causality Network (Edge labels represent -log10(p-value))")
plt.show()

# Correlation matrix
correlation_matrix = np.corrcoef(data, rowvar=False)

print("\nCorrelation Matrix:")
for i, roi_i in enumerate(roi_names):
    for j, roi_j in enumerate(roi_names):
        if i != j:
            print(f"Correlation between {roi_i} and {roi_j}: {correlation_matrix[i, j]:.3f}")


# Visualization of correlation matrix
graph = nx.Graph()
for roi in roi_names:
    graph.add_node(roi)
for i in range(correlation_matrix.shape[0]):
    for j in range(i + 1, correlation_matrix.shape[1]):
        if abs(correlation_matrix[i, j]) > 0.0: 
            graph.add_edge(roi_names[i], roi_names[j], weight=correlation_matrix[i, j])

# Adjust layout for triangle
pos = {
    "ROI 1": np.array([-1, 0]),
    "ROI 2": np.array([1, 0]),
    "ROI 3": np.array([0, 1.5])
}

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.margins(0.15)
nx.draw_networkx_nodes(graph, pos, node_size=3000, node_color='skyblue', ax=ax)
nx.draw_networkx_labels(graph, pos, font_size=15, ax=ax)
edges = nx.draw_networkx_edges(graph, pos, width=[abs(graph[u][v]['weight'])*2 for u, v in graph.edges()], ax=ax)
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in graph.edges(data=True)}
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, ax=ax)
plt.title('Network Correlation Map')
plt.tight_layout()
plt.show()
