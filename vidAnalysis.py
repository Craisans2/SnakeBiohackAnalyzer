import cv2 as cv
#pip install tensorflow
#pip install tf_slim
#pip install tf-models-official
#pip install opencv-python

#hello world
#imports
#dylan  testing if his stupid code works
#Function to seperate the video into images
def imageParser(video_file):
    vidMedCap = cv.VideoCapture(video_file)
    frameNum = 0
    while(True):
        #process the frames
        
        success,frame = vidMedCap.read()
        if success:
            cv.imwrite(f'C:/Users/dylan/OneDrive/Desktop/Biohack/Images',frame)
        else:
            break
        
        frameNum=frameNum+1
    vidMedCap.release()

#

#Presurgery Risk factors that increase infection risk
highrisk = False

hasDiabetes = False
hasInfectionHistory = False
hasObesity = False
hasSmokes = False

#Inputs for Risks
hasDiabetes = boolean(input("does the patient have diabetes: enter 1 or 0: "))
hasInfectionHistory = boolean(input("does the patient have prior infection history: enter 1 or 0: "))
hasObesity = boolean(input("does the patient have obesity: enter 1 or 0: "))
hasSmokes = boolean(input("does the patient smoke: enter 1 or 0: "))
hasCancer = boolean(input("does the patient have cancer or is in remission: enter 1 or 0: "))

if hasDiabetes or hasInfectionHistory or hasObesity or hasDiabetes or hasSmokes or hasCancer:
    highrisk = True

