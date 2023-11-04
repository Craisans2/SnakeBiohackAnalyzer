import cv as cv2
#hello world
#imports
#dylan  testing if his stupid code works
imageParser('C:/Users/dylan/OneDrive/Desktop/Biohack/IMG_4688.MOV')
#Function to seperate the video into images
def imageParser(video_file):
    vidMedCap = cv2.VideoCapture(video_file)
    frameNum = 0
    while(True):
        #process the frames
        
        success,frame = vidMedCap.read()
        if success:
            cv2.imwrite(f'C:/Users/dylan/OneDrive/Desktop/Biohack/Images',frame)
        else:
            break
        
        frameNum=frameNum+1
    vidMedCap.release()