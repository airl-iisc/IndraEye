import json
import os
from PIL import Image, ImageDraw
import cv2
import torch
import numpy as np


def instance_gry(img, ann, file_name):
    # Convert the image to a numpy array if it's a PIL Image

    img = np.array(img)
    count = 1
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gry = np.array([0.2989, 0.5870, 0.1140])
    
    image = img

    img_height, img_width = img.shape[:2]
    
    tmp = img.copy()

    # Get image dimensions
    
    # Iterate through the annotations (bounding boxes)
    for i, annotation in enumerate(ann):
        # Extract bounding box coordinates

        ########### TO Ignore conversion to gray color for any class object  ##############################
        if annotation["category_id"] == 6:
            tmp = tmp
        
        else:
            x_min, y_min, tmp_x_max, tmp_y_max = annotation['bbox']


            x_max = x_min + tmp_x_max
            y_max = y_min + tmp_y_max
        
            # Ensure coordinates are integers
            x_min, y_min, x_max, y_max = map(int, [x_min, y_min, x_max, y_max])
        
            # Ensure coordinates are within image boundaries
            x_min = max(0, min(x_min, img_width - 1))
            y_min = max(0, min(y_min, img_height - 1))
            x_max = max(x_min + 1, min(x_max, img_width))
            y_max = max(y_min + 1, min(y_max, img_height))

            cropped_img = img[y_min:y_max, x_min:x_max].copy()
            print("Converting RGB To gry image....")
            intermediate = cropped_img
            tmp[y_min:y_max, x_min:x_max] = torch.Tensor(np.stack((intermediate, intermediate, intermediate), axis=0)).permute(1,2,0)
        
            # Ensure the cropped image is not empty
            if cropped_img.size == 0:
                print(f"Warning: Skipping empty crop for annotation {i}")

        count += 1
        
        
    print("Converted " + str(count) + "Images...")
    
    cv2.imwrite("/home/jarvis/Desktop/EO_IR/LLVIP/visible/train/inst_images/" + file_name, tmp)
    return None
    
    
    


def load_coco_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def process_images(coco_data, image_dir):
    # Create a dictionary to map image IDs to their file names
    image_id_to_file = {img['id']: img['file_name'] for img in coco_data['images']}
    
    # Group annotations by image ID
    annotations_by_image = {}
    for ann in coco_data['annotations']:
    
        image_id = ann['image_id']
        if image_id not in annotations_by_image:
            annotations_by_image[image_id] = []
        annotations_by_image[image_id].append(ann)
    
    # Process each image
    for image_id, annotations in annotations_by_image.items():
        image_file = os.path.join(image_dir, image_id_to_file[image_id])
        
        # Open the image
        with Image.open(image_file) as img:
            file_name = image_file.split("/")[-1]
            instance_gry(img, annotations, file_name)

# Usage
coco_json_file = '/home/jarvis/Desktop/EO_IR/LLVIP/visible/train/annotations/instances_default_new.json'
image_directory = '/home/jarvis/Desktop/EO_IR/LLVIP/visible/train/images/'

coco_data = load_coco_json(coco_json_file)
process_images(coco_data, image_directory)
