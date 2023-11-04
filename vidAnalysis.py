import cv2 as cv
#hello world
#imports
#Function to seperate the video into images
def imageParser(video_file):
    vidMedCap = cv2.VideoCapture(video_file)
    frameNum = 0
    frames = [] 
    while(True):
        #process the frames
        
        success,frame = vidMedCap.read()
        if success:
            cv2.imwrite(frames,frame)
        else:
            break
        
        frameNum=frameNum+1
vidMedCap.release()

#

#Presurgery Risk factors that increase infection risk
highrisk = False
hasDiabetes = True
hasInfectionHistory = False
hasObesity = False
hasSmokes = False
if hasDiabetes or hasInfectionHistory or hasObesity or hasDiabetes or hasSmokes:
    highrisk = True