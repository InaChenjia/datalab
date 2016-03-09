try:
    import cPickle as pickle
except ImportError:
    import pickle

dumpfile = ''
f = open(dumpfile, 'rb')
G = pickle.load(f)
f.close()

import networkx as nx

print nx.info(G)
print G.nodes()
print neighbors

%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=20)
nx.draw_networkx_edges(G,pos,edge_color='r') 
nx.draw_networkx_labels(G,pos,fontsize=5)
plt.show()