#!/usr/bin/env python3



import os
from PIL import Image
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# Path to the directory containing the images
directory = './Preprocessed_Data/train/Input_images/images_folder'
noise_direct='./Preprocessed_Data_noise/train/Input_images/images_folder'
os.makedirs(noise_direct, exist_ok=True)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Open the image using PIL
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)
        image_array=np.asarray(image)
        #print(image_array.shape)
        
        noise = np.random.normal(scale=10, size=image_array.shape)
        noisy_image_array = image_array + noise
        noisy_image_array = np.clip(noisy_image_array, 0, 255).astype(np.uint8)
        noisy_image=Image.fromarray(noisy_image_array)
        #noisy_image.show()
        
        output_path = os.path.join(noise_direct, filename)
        
        noisy_image.save(output_path)
        # Do something with the image
        # For example, display the image
        #image.show()

        
        
        
        
directory = './Preprocessed_Data/test/Input_images/images_folder'
noise_direct='./Preprocessed_Data_noise/test/Input_images/images_folder'
os.makedirs(noise_direct, exist_ok=True)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Open the image using PIL
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)
        image_array=np.asarray(image)
        #print(image_array.shape)
        
        noise = np.random.normal(scale=10, size=image_array.shape)
        noisy_image_array = image_array + noise
        noisy_image_array = np.clip(noisy_image_array, 0, 255).astype(np.uint8)
        noisy_image=Image.fromarray(noisy_image_array)
        #noisy_image.show()
        
        output_path = os.path.join(noise_direct, filename)
        
        noisy_image.save(output_path)
        # Do something with the image
        # For example, display the image
        #image.show()

