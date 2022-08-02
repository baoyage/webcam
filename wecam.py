import cv2
from datetime import date
from pathlib import Path

import datetime
now = datetime.datetime.now() # current date and time
date_time = now.strftime("%m-%d-%Y %H-%M-%S")
HIGH_VALUE = 10000
WIDTH = HIGH_VALUE
HEIGHT = HIGH_VALUE
#Capture video from webcam
vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
width = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

output = cv2.VideoWriter("F:/webcam/"+date_time+".mp4", vid_cod, 20, (width,height))
while(True):
     # Capture each frame of webcam video
    ret,frame = vid_capture.read()
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
 
        # Get date and time and
        # save it inside a variable
    dt = str(datetime.datetime.now())
 
        # put the dt variable over the
        # video frame
    frame = cv2.putText(frame, dt,
                            (10, 100),
                            font, 1,
                            (210, 155, 155),
                            4, cv2.LINE_8)
    cv2.imshow("My cam video", frame)
    output.write(frame)
     # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) &0XFF == ord('x'):
        break
# close the already opened camera
vid_capture.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()