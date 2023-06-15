#!/usr/bin/env python3



import os
from PIL import Image
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# Path to the directory containing the images
directory = './Preprocessed_Data_noise/test/Input_images/images_folder'
no_noise_directory='./Preprocessed_Data/test/Input_images/images_folder'
noise_direct='./Preprocessed_Data_denoised/test/Input_images/images_folder'
os.makedirs(noise_direct, exist_ok=True)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Open the image using PIL
        image_path = os.path.join(directory, filename)
        img = cv2.imread(image_path)
        
        image_path_normal=image_path = os.path.join(no_noise_directory, filename)
        img_normal = cv2.imread(image_path_normal)
        
        dst = cv2.fastNlMeansDenoisingColored(img,None,5,5)
        output_path=os.path.join(noise_direct, filename)
        cv2.imwrite(output_path,dst)
        #plt.subplot(131),plt.imshow(img)
        #plt.subplot(132),plt.imshow(dst)
        #plt.subplot(133),plt.imshow(img_normal)
        #plt.show()
        
        
        
        
directory = './Preprocessed_Data_noise/train/Input_images/images_folder'
no_noise_directory='./Preprocessed_Data/train/Input_images/images_folder'
noise_direct='./Preprocessed_Data_denoised/train/Input_images/images_folder'
os.makedirs(noise_direct, exist_ok=True)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Open the image using PIL
        image_path = os.path.join(directory, filename)
        img = cv2.imread(image_path)
        
        image_path_normal=image_path = os.path.join(no_noise_directory, filename)
        img_normal = cv2.imread(image_path_normal)
        
        dst = cv2.fastNlMeansDenoisingColored(img,None,5,5)
        output_path=os.path.join(noise_direct, filename)
        cv2.imwrite(output_path,dst)
        #plt.subplot(131),plt.imshow(img)
        #plt.subplot(132),plt.imshow(dst)
        #plt.subplot(133),plt.imshow(img_normal)
        #plt.show()