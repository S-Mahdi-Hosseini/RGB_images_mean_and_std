import os
import numpy as np
import matplotlib.pyplot as plt
import glob

def imgs_mean(*args):
    #use glob imported from glob module to create a list of image path and give this list as arguments of this function
    img_list = []
    for lists in args:
        img_list = img_list + list(lists)
    mean = [0 , 0 , 0]  # [R , G , B]
    for i , img in enumerate(img_list):   # shapes of images are   H * W * D
        image = plt.imread(img)
        
        mean[0] = (mean[0]*i + np.mean(image[:,:,0]))/(i+1)
        mean[1] = (mean[1]*i + np.mean(image[:,:,1]))/(i+1)
        mean[2] = (mean[2]*i + np.mean(image[:,:,2]))/(i+1)
    return mean

def imgs_std(*args):
    #use glob imported from glob module to create a list of image path and give this list as arguments of this function
    img_list = []
    std  = [0 , 0 , 0]  # [R , G , B]
    for lists in args:
        img_list = img_list + list(lists)
    std  = [0 , 0 , 0]  # [R , G , B]
    for i , img in enumerate(img_list):   # shapes of images are   H * W * D
        image = plt.imread(img)

        std[0] = (std[0]*i + np.std(image[:,:,0]))/(i+1)
        std[1] = (std[1]*i + np.std(image[:,:,1]))/(i+1)
        std[2] = (std[2]*i + np.std(image[:,:,2]))/(i+1)
    return std
