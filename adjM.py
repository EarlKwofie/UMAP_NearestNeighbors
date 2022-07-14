import json
import numpy as np
from sklearn.neighbors import NearestNeighbors

#convert json file object into numpy array
f_json = open("standardized.json")
f_data = json.load(f_json)
f_data_numpy = np.array(f_data)
x= f_data_numpy.shape
rowsize = x[0]
print(rowsize)

nbrs = NearestNeighbors(n_neighbors = 3, algorithm= 'ball_tree').fit(f_data_numpy)
adjM = nbrs.kneighbors_graph(f_data_numpy).toarray()