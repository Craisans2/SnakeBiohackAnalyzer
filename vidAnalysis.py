import cv2 as cv
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

imageParser('C:/Users/dylan/OneDrive/Desktop/Biohack/IMG_4688.MOV')
