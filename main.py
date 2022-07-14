# This is a sample Python script.
# Press the green button in the gutter to run the script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import math
import os
#import cv2
import numpy as np
from sklearn.metrics import adjusted_rand_score
from sklearn.neighbors import NearestNeighbors
from PIL import Image
from matplotlib import pyplot as plt

def traverse(adjacency_matrix, startNodeNum, visited):
    x= adjacency_matrix.shape
    size = x[0]
    #mark starting node as visited
    visited[startNodeNum] = True 
    for i in range(0,size):
        if adjacency_matrix[startNodeNum][i] and not visited[i]:
                traverse(adjacency_matrix, i,visited)

def isConnected(adjacency_matrix,startNodeNum):
    x= adjacency_matrix.shape
    size = x[0]
    visited = [False for i in range(0, size)]
    for i in range(startNodeNum,size):
        for j in range(0, size):
            visited[j] = False
            traverse(adjacency_matrix,i, visited)
        for i in range(0, size):
            if not visited[i]:
                print("The Graph is Not Connected")
                return False
            return True
            print("The Graph is Connected")

#convert json file object into numpy array
f_json = open("standardized.json")
f_data = json.load(f_json)
f_data_numpy = np.array(f_data)
x= f_data_numpy.shape
rowsize = x[0]
print(rowsize)

# # put image files in array
# # check out the enumerate function within the python library

f_images = []
f_imagepath = []
for image in os.listdir("./images/"):
    if image.endswith(".jpg"):
        f_images.append(image)


for image in f_images:
    image_file = os.path.basename(image)
    display = Image.open("./images/" + image_file, 'r')
    f_imagepath.append("./images/" + image_file)
    # display.show()

# use NearestNeighbors
nbrs = NearestNeighbors(n_neighbors = 3, algorithm= 'ball_tree').fit(f_data_numpy)
adjM = nbrs.kneighbors_graph(f_data_numpy).toarray()

#check to see if adjancency matrix is connected so that we can do djikstras
isConnected(adjM, 0)

# # way to calculate the distance between 2 image indexes

# def getDistance(im_1, im_2):
#     image1_x = f_data[im_1][0]
#     image1_y = f_data[im_1][1]

#     image2_x = f_data[im_2][0]
#     image2_y = f_data[im_2][1]

#     diff_x = image1_x - image2_x
#     diff_y = image1_y - image2_y

#     square = diff_x * diff_x + diff_y * diff_y
#     return math.sqrt(square)


# print(getDistance(0, 2))


# # Returns the 5 closest points on the UMAP to a point of focus on the UMAP
# # Still look into the way that we can use an existing nearest neighbors function - it's probably faster

# def getNearestNeighbors(image_index):
#     distances = []
#     image_indexes = []
#     for i in range(len(f_images)):
#         distances.append(getDistance(image_index, i))
#         image_indexes.append(i)

#     for i in range(len(f_images)):
#         base = distances[i]
#         base_index = image_indexes[i]
#         j = i - 1
#         while j >= 0 and distances[j] > base:
#             distances[j + 1] = distances[j]
#             image_indexes[j + 1] = image_indexes[j]
#             j -= 1
#             distances[j + 1] = base
#             image_indexes[j + 1] = base_index

#     return image_indexes[0: 6]


# print(getNearestNeighbors(5))

# # returns the images that are nearest to a given image index
# # need a method to copy all the images to a folder in order of how close they are to the given image

# def displayNeighbors(neighbors):
#     print(len(f_images))
#     neighbor_image = []
#     for n in range(len(neighbors)):
#         image_collection = os.path.basename(f_images[neighbors[n]])
#         neighbor_images = Image.open("./images/" + image_collection, 'r')
#         neighbor_images.show()
#         neighbor_image.append(image_collection)

# #displayNeighbors(getNearestNeighbors(5))

# # A simple algorithm for the 'image walk'
# # determines a path between two image indexes by jumping between images

# def getTransformation(image_1, image_2):
#         im_index = image_1
#         transformation = [image_1]
#         i = 0
#         # still need to make this more efficient, also there is not verification to insure an image isnt selected twice
#         for i in range(6):
#             neighbors = getNearestNeighbors(im_index)
#             neighbor_distance = []
#             for n in neighbors:
#                 neighbor_distance.append(getDistance(image_2, n))

#             for n in range(len(neighbor_distance)):
#                 base = neighbor_distance[n]
#                 base_index = neighbors[n]
#                 j = i - 1
#                 while j >= 0 and neighbors[j] > base:
#                     neighbor_distance[j + 1] = neighbor_distance[j]
#                     neighbors[j + 1] = neighbors[j]
#                     j -= 1
#                     neighbor_distance[j + 1] = base
#                     neighbors[j + 1] = base_index

#             # also curious about what the sorting is putting first in the list, the closest? or the furthest?
#             im_index = neighbors[1]

#             if im_index in transformation:
#                 k = 0
#                 while im_index in transformation and k < 6:
#                         im_index = neighbors[k]
#                         k+=1

#             if im_index in transformation:
#                 break

#             else:
#                 transformation.append(im_index)

#         transformation.append(image_2)
#         return transformation
#         #displayNeighbors(transformation)

# def displayTransformation (neighbors):
#     print(neighbors)
#     images = []

#     for n in range(len(neighbors)):
#         image = cv2.imread(f_imagepath[neighbors[n]])
#         images.append(image)

#     return images


# output = displayTransformation(getTransformation(234, 1000))

# rows = 1
# columns = len(output)

# fig = plt.figure(figsize=(15,15))

# index = 0
# for o in output:
#     fig.add_subplot(rows, columns, index + 1)
#     plt.imshow(output[index])
#     plt.axis("off")
#     index = index + 1

# plt.waitforbuttonpress()

# plt.close(fig)



