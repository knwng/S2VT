import cv2,os,sys

print 'cv2 path: ', cv2.__file__
video_path = os.path.join('YouTubeClips_train', 'rnawC5C8gSI_82_90.avi')
cap = cv2.VideoCapture(video_path)
print 'VideoCapture is opened: ', cap.isOpened()

i = 0
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    print 'processing frame ', i
    cv2.imwrite('video_'+str(i)+'.jpg', frame)
    i += 1

