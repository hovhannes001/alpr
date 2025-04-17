import cv2
import sys
from pathlib import Path
custom_path = Path("./image_and_videos").resolve()
sys.path.append(str(custom_path))

 	
# video = cv2.VideoCapture("traffic.webm")
# fps = video.get(7)
# print(fps)
# while(video.isOpened()):
#     ret, frame = video.read()
#     if ret == True:
#         cv2.imshow("frame",frame)
#         key = cv2.waitKey(1)

#         if key == ord('q'):
#             break
#     else:
#         break
    
# video.release()
# cv2.destroyAllWindows()

#video write

video2 = cv2.VideoCapture("video.mp4")

frame_width = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_height , frame_width)

fps2 = video2.get(7)
forcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("record_camera.avi", cv2.VideoWriter_fourcc(*"XVID"), fps2,(frame_width, frame_height))  

while(video2.isOpened()):
    ret, frame = video2.read()
    if ret == True:
        output.write(frame)
        key = cv2.waitKey(1)
        cv2.imshow("f",frame)
        if(key == ord('q')):
            break
    else:
        break

# video.release()
video = cv2.VideoCapture("record_camera.avi")
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow("frame",frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
    else:
        break
    