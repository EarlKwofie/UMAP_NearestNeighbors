import json
import os
from tracemalloc import start
import numpy as np
import matplotlib.pyplot as plt

#get image name from a path 
def get_image_name(path):
    list = path.split("/")
    nameapos= list[-1]
    imagename = nameapos[:-1]
    return imagename

def get_key(dict, val):
    for key, value in dict.items():
     if val == value:
         return key


#get file object
fjson = open("output/data/layouts/umap-47646dc8-0787-11ed-b3ec-3af9d3c7419a.json", "r")
#from file object get json object
umapjson = json.load(fjson)

#make dict of json objects
indexjson = {}
for i in range (0,len(umapjson)):
    indexjson[i] = umapjson[i]

#make dict of images 
templistimages = os.listdir("output/data/originals")
listimages = sorted(templistimages)
indeximage = {}
for i in range (0, len(listimages)):
    indeximage[i] = listimages[i]

#get starting coordinates
startimagepath = input("Enter starting image :")
startimage = get_image_name(startimagepath)
indexstartimage = get_key(indeximage, startimage)
startcoord = indexjson[indexstartimage]

#get ending coordinates
endimagepath = input("Enter ending image :")
endimage = get_image_name(endimagepath)
indexendimage = get_key(indeximage, endimage)
endcoord = indexjson[indexendimage]

x = [startcoord[0], endcoord[0]]
y = [startcoord[1], endcoord[1]]

coefficients = np.polyfit(x,y,1)
#gives line in ax + b form
polynomial = np.poly1d(coefficients)
print(polynomial)














