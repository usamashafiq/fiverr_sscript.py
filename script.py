import os
import cv2
import glob
import matplotlib.pyplot as plt
import numpy as np
import PIL
from more_itertools import chunked
from PIL import Image
import cv2
import numpy as np

pathfiles = input("Enter the files path .png : ")
list_files = os.listdir(pathfiles)
list_files_final = []
for x in list_files:
    if x.endswith(".png"):
        # Prints only text file present in My Folder
        list_files_final.append(x)

path_letter = input("Enter the letter file path .txt ")



def generator(path):
    word = ''
    with open(path) as file:
        while True:
            char = file.read(1)
            if char.isspace():
                if word:
                    yield word
                    word = ''
            elif char == '':
                if word:
                    yield word
                break
            else:
                word += char


# Instantiate the word generator.
words = generator(path_letter)
a = []
# Print the  words.
for word in words:
    a.append(word)


def combine_horizontally(image_names, padding=50):
    images = []
    max_height = 0  # find the max height of all the images
    total_width = 0  # the total width of the images (horizontal stacking)

    for name in image_names:
        # open all images and find their sizes
        img = cv2.imread(name)
        images.append(img)

        image_height = img.shape[0]
        image_width = img.shape[1]

        if image_height > max_height:
            max_height = image_height

        # add all the images widths
        total_width += image_width

    # create a new array with a size large enough to contain all the images
    # also add padding size for all the images except the last one
    final_image = np.zeros((max_height, (len(image_names) - 1) * padding + total_width, 3), dtype=np.uint8)

    current_x = 0  # keep track of where your current image was last placed in the x coordinate
    for image in images:
        # add an image to the final array and increment the x coordinate
        height = image.shape[0]
        width = image.shape[1]
        final_image[:height, current_x:width + current_x, :] = image
        # add the padding between the images
        current_x += width + padding

    return final_image


list_final = []
for i in range(len(a)):
    words = a[i].split()
    for i in words:
        for j in i:
            if j == '?' or j == ',' or j == '.' or j == "'" or j == '!' or j == '’' or j == '(' or j == ')':
                continue
            alpha = str(j).lower() + ".png"
            for k in range(len(list_files_final)):
                if alpha == list_files_final[k]:
                    list_final.append(list_files_final[k])

    final_image = combine_horizontally(list_final, padding=10)
    cv2.imshow(i, final_image)
    cv2.imwrite(str(i) + ".png", final_image)
    list_final.clear()


