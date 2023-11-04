import cv2 as cv
#pip install tensorflow
#pip install tf_slim
#pip install tf-models-official
#pip install opencv-python

#hello world
#imports
#dylan  testing if his stupid code works
#Function to seperate the video into images
def imageParser(video_file,imageFile):
    vidMedCap = cv.VideoCapture(video_file)
    frameNum = 0
    while(True):
        #process the frames
        
        success,frame = vidMedCap.read()
        if success:
            cv.imwrite(f'{imageFile}frame_{frameNum}.jpg',frame)
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
hasDiabetes = bool(input("does the patient have diabetes: enter 1 or 0: "))
hasInfectionHistory = bool(input("does the patient have prior infection history: enter 1 or 0: "))
hasObesity = bool(input("does the patient have obesity: enter 1 or 0: "))
hasSmokes = bool(input("does the patient smoke: enter 1 or 0: "))
hasCancer = bool(input("does the patient have cancer or is in remission: enter 1 or 0: "))

if hasDiabetes or hasInfectionHistory or hasObesity or hasDiabetes or hasSmokes or hasCancer:
    highrisk = True

videoFile = str(input("please enter the video you wish to analyze"))
imageFile = str(input("Please enter the place where you wish for the files to emerge from :D"))
imageParser(videoFile, imageFile)
