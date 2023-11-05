import cv2 as cv
import numpy as np
import tensorflow as tf
import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
import matplotlib.pyplot as plt
import matplotlib.patches as patchess
from PIL import Image

#sectionImages
def processIm(imPath,i):
    # Load the pre-trained DETR model and processor
    model_name = "facebook/detr-resnet-50"
    processor = DetrImageProcessor.from_pretrained(model_name)
    model = DetrForObjectDetection.from_pretrained(model_name)

    # Path to the image you want to analyze
    imStr = f'{imPath}/frame_{i}.jpg'
    print(imStr)
    image_path = Image.open(imStr)

    # Load and preprocess the image
    image = processor(images=image_path, return_tensors="pt")
    outputs = model(**image)

    # Check the structure of the output tensors
    # Get the predicted boxes and labels for the first image in the batch
    pred_boxes = outputs.logits[0, :, :4]  # Assuming the first 4 values in the third dimension represent box coordinates
    pred_logits = outputs.logits[0, :, 4:]  # Assuming the remaining values represent logits for each class

    # Get the predicted boxes and labels
    pred_boxes = outputs.logits["pred_boxes"]
    pred_logits = outputs.logits["pred_logits"]

    # Threshold for detection confidence
    detection_threshold = 0.5

    # Filter detections based on confidence score
    detections = pred_boxes[pred_logits[:, 0] > detection_threshold]

    # You can now work with the detected bounding boxes (detections)
    # You may want to visualize or process the results further as needed

    # Example: Print the coordinates of detected scalpel boxes
    for box in detections:
        print("Box Coordinates:", box.tolist())

    # Example: Visualize the detected boxes (you can use a library like matplotlib)

    plt.imshow(image_path)

    ax = plt.gca()
    for box in detections:
        xmin, ymin, xmax, ymax = box.tolist()
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor="r", facecolor="none")
        ax.add_patch(rect)

    plt.show()

#Function to seperate the video into images
def imageParser(video_file,imageFile):
    vidMedCap = cv.VideoCapture(video_file)
    frameNum = 0
    while(True):
        #process the frames
        
        success,frame = vidMedCap.read()
        if success:
            cv.imwrite(f'{imageFile}/frame_{frameNum}.jpg',frame)
        else:
            break
        frameNum=frameNum+1
    vidMedCap.release()
    return frameNum  

#Presurgery Risk factors that increase infection risk
highrisk = False


#Inputs for Risks
hasDiabetes = bool(input("does the patient have diabetes: enter 1 or 0: "))
hasInfectionHistory = bool(input("does the patient have prior infection history: enter 1 or 0: "))
hasObesity = bool(input("does the patient have obesity: enter 1 or 0: "))
hasSmokes = bool(input("does the patient smoke: enter 1 or 0: "))
hasCancer = bool(input("does the patient have cancer or is in remission: enter 1 or 0: "))

if hasDiabetes or hasInfectionHistory or hasObesity or hasDiabetes or hasSmokes or hasCancer:
    highrisk = True
    



#Inputs for postsurgery infection signs
hasSepsis = bool(input("does the patient show signs of brain fog, fever or clammy skin: enter 1 or 0: "))
hasPus = bool(input("Is there pus buildup around the incision: enter 1 or 0: "))
hasSwell = bool(input("does the patient have excess swelling around the incision site: enter 1 or 0: "))

if hasSepsis or hasInfectionHistory or hasSwell:
    highrisk = True

videoFile = input("Enter a video to analyze: ")
imageFile = input("Enter a file to save images to: ")
frameNum = imageParser(videoFile,imageFile)
i = 0
while i<frameNum:
    processIm(imageFile,i)
    i=i+1

