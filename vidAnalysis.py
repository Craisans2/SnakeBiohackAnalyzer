import cv2 as cv
import numpy as np
import tensorflow as tf
import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image

# Load the pre-trained DETR model and processor
model_name = "facebook/detr-resnet-50"
processor = DetrImageProcessor.from_pretrained(model_name)
model = DetrForObjectDetection.from_pretrained(model_name)

# Path to the image you want to analyze
image_path = Image.open("Users\davidbutz\Desktop\IMG_0018.jpeg")

# Load and preprocess the image
image = processor(images=image_path, return_tensors="pt")
outputs = model(**image)

# Get the predicted boxes and labels
pred_boxes = outputs.logits["pred_boxes"]
pred_logits = outputs.logits["pred_logits"]

# Threshold for detection confidence
detection_threshold = 0.5

# Filter detections based on confidence score
detections = pred_boxes[0][pred_logits[0][:, 0] > detection_threshold]

# You can now work with the detected bounding boxes (detections)
# You may want to visualize or process the results further as needed

# Example: Print the coordinates of detected scalpel boxes
for box in detections:
    print("Box Coordinates:", box.tolist())

# Example: Visualize the detected boxes (you can use a library like matplotlib)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

image = Image.open(image_path)
plt.imshow(image)

ax = plt.gca()
for box in detections:
    xmin, ymin, xmax, ymax = box.tolist()
    rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor="r", facecolor="none")
    ax.add_patch(rect)

plt.show()

