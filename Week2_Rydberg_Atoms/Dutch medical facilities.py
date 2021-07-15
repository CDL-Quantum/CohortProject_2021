import shapefile as shp
import seaborn as sns
import geopandas as gpd
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import dwave_networkx as dnx
from dwave_qbsolv import QBSolv


## Dutch medical facilities distribution
# Optimal distribution of medical facilities across a country is a problem that with given simplifications (e.g. uniform
# density of population) can be exactly mapped to the UD-MIS problem.
# For instance, given a set of cities where it is possible to build a hospital, the goal is to find the maximum
# independent set of cities under the constraint that the cities are at least e.g. 50km apart.
# Quantum annealing can be used for this task.

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10, 6))

gemeente_shp_path = "./Week2_Rydberg_Atoms/data/Gemeentegrenzen__voorlopig____kustlijn.shp"
provincie_shp_path = "./Week2_Rydberg_Atoms/data/Provinciegrenzen_2019.shp"

gemeente_sf = shp.Reader(gemeente_shp_path)

gemeente_df = gpd.read_file(gemeente_shp_path)
provincie_df = gpd.read_file(provincie_shp_path)

fig, ax = plt.subplots()
provincie_df.plot(ax=ax, color='gray', edgecolor='black')
ax.set_aspect(1.5)
plt.show()

cities = ['Utrecht', 'Amsterdam', 'Rotterdam', 'Eindhoven',
          'Zundert', 'Nijmegen', 'Arnhem', 'Groningen',
          'Amersfoort', 'Zwolle']

data_dist = []
G = nx.Graph()

for city in cities:
    G.add_node(city)
    gemeente_idx = gemeente_df[gemeente_df.Gemeentena == city].index.values[0]
    x_pts = gemeente_sf.shape(gemeente_idx).points[0][0]
    y_pts = gemeente_sf.shape(gemeente_idx).points[0][1]
    plt.scatter(x_pts, y_pts, c='r')
    ax.annotate(city, (x_pts, y_pts))
    distances = []
    for other_city in cities:
        if city == other_city:
            distances.append(0)
        else:
            other_gemeente_idx = gemeente_df[gemeente_df.Gemeentena == other_city].index.values[0]
            x2_pts = gemeente_sf.shape(other_gemeente_idx).points[0][0]
            y2_pts = gemeente_sf.shape(other_gemeente_idx).points[0][1]
            dist = np.ceil(np.sqrt((x_pts - x2_pts)**2 + (y_pts - y2_pts)**2)*100)
            distances.append(dist)
            if dist <= 50: # less than 50 km distant
                G.add_edge(city, other_city)

    data_dist.append(distances)

sampler = QBSolv()

indep_nodes = dnx.maximum_independent_set(G, sampler)

print(f'Independent nodes: {indep_nodes}')

plt.figure()
# plot MIS nodes with different color
pos = nx.circular_layout(G)  # positions for all nodes

# nodes from MIS
nx.draw_networkx_nodes(G, pos, nodelist=indep_nodes, node_size=700, node_color='red')
nx.draw_networkx_nodes(G, pos, nodelist=[n for n in list(G.nodes) if n not in indep_nodes], node_size=700)
# edges
nx.draw_networkx_edges(G, pos)
# labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
plt.axis("off")
plt.show()

# plot results on map
fig, ax = plt.subplots()
provincie_df.plot(ax=ax, color='gray', edgecolor='black')
ax.set_aspect(1.5)
plt.show()

for city in cities:
    gemeente_idx = gemeente_df[gemeente_df.Gemeentena == city].index.values[0]
    x_pts = gemeente_sf.shape(gemeente_idx).points[0][0]
    y_pts = gemeente_sf.shape(gemeente_idx).points[0][1]
    if city in indep_nodes:
        plt.scatter(x_pts, y_pts, s=300, c='red')
    else:
        plt.scatter(x_pts, y_pts, s=30, c='b')
    ax.annotate(city, (x_pts, y_pts))
