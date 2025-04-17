import cv2
import sys
from pathlib import Path
custom_path = Path("./image_and_videos").resolve()
sys.path.append(str(custom_path))

 	
video = cv2.VideoCapture(0)
fpn = video.get(7)

while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow("frame",frame)
        key = cv2.waitKey(100)

        if key == ord('q'):
            break
    else:
        break
    
