import cv2 as cv

#hello world
#imports
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
    

def imageAnalyzer():
    #here


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
    