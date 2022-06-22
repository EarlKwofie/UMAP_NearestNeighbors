# This is a sample Python script.
# Press the green button in the gutter to run the script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import math
import os
from PIL import Image

def printData(j_file):
    #file = json.dumps(j_file);
    print(j_file)

f = open("test.txt", "w")
f.write("Hello")
f = open("test.txt", "r")
file = f.read()
f.close()

printData(file)

# simple method to convert json data to array of strings
f_json = open("umap-e960482e-f0bc-11ec-a9d0-38fc985d69ec.json")
f_data = json.load(f_json)
#for i in f_data:
    #print(i)

# simple method to convert all the images in a file into an array and displays them in order
f_images = []
for image in os.listdir("./images/"):
    if image.endswith(".jpg"):
        f_images.append(image)

for image in f_images:
    image_file = os.path.basename(image)
    display = Image.open("./images/" + image_file, 'r')
    #display.show()

# way to calculate the distance between 2 image indexes
def getDistance(im_1, im_2):
    image1_x = f_data[im_1][0]
    image1_y = f_data[im_1][1]

    image2_x = f_data[im_2][0]
    image2_y = f_data[im_2][1]

    diff_x = image1_x - image2_x
    diff_y = image1_y - image2_y

    square = diff_x * diff_x + diff_y * diff_y
    return math.sqrt(square)

print(getDistance(0,2))

# Returns the 5 closest points on the UMAP to a point of focus on the UMAP
def getNearestNeighbors(image_index):
    distances = []
    image_indexes = []
    for i in range(25):
        distances.append(getDistance(image_index, i))
        image_indexes.append(i)

        # for i in range(1, len(distances)):
        #     key = distances[i]
        #     j = i - 1
        #     while j >= 0:
        #         if distances[j] > key:
        #             key_2 = distances[j]
        #             i_key = image_indexes[i]
        #             i_key_2 = image_indexes[j]
        #
        #             distances[i] = key_2
        #             distances[j] = key
        #
        #             image_indexes[i] = i_key_2
        #             image_indexes[j] = i_key
        #             j -= 1
        #         else:
        #             continue

    for i in range(25):
        base = distances[i]
        base_index = image_indexes[i]
        j = i - 1
        while j >= 0 and distances[j] > base:
            distances[j + 1] = distances[j]
            image_indexes[j + 1] = image_indexes[j]
            j -= 1
            distances[j + 1] = base
            image_indexes[j + 1] = base_index

    return image_indexes[1 : 6]


print(getNearestNeighbors(5))











