import cv2

video2 = cv2.VideoCapture("traffic.webm")

frame_width = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = video2.get(cv2.CAP_PROP_FPS)


frame_size = (frame_width, frame_height)


output = cv2.VideoWriter("record_camera1.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps2,frame_size)


while video2.isOpened():
    ret, frame = video2.read()
    if ret:
        output.write(frame)
        cv2.imshow("Recording", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

video2.release()
output.release()
cv2.destroyAllWindows()


video = cv2.VideoCapture("record_camera1.mp4")
while video.isOpened():
    ret, frame = video.read()
    if ret:
        cv2.imshow("Playback", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
