import numpy as np
import cv2
import win32con,win32gui
import time

import morphsnakes as ms
from example import visual_callback_2d

cap = cv2.VideoCapture('project_2乳腺肿瘤视频.avi')
windowName1='original'
windowName2='processed'

startTime=time.time()
#np.hstack((frameLeft, frameRight))#在水平方向上拼接两帧图片
while (cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        break
    frame=frame[132:600, 191:794]
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #开始处理
    gimg = ms.inverse_gaussian_gradient(frame, alpha=1000, sigma=5.48)
    init_ls = ms.circle_level_set(frame.shape, (100, 126), 20)
    callback = visual_callback_2d(frame)
    ms.morphological_geodesic_active_contour(gimg, iterations=45, 
                                         init_level_set=init_ls,
                                         smoothing=1, threshold=0.31,
                                         balloon=1, iter_callback=callback)
    

##    scharrx=cv2.Scharr(frame,cv2.CV_64F,dx=1,dy=0)
##    scharrx=cv2.convertScaleAbs(scharrx)
##    scharry=cv2.Scharr(frame,cv2.CV_64F,dx=0,dy=1)
##    scharry=cv2.convertScaleAbs(scharry)
##    processedFrame=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

##    ret, binary = cv2.threshold(processedFrame,127,255,cv2.THRESH_BINARY) 
##    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
##    cv2.drawContours(processedFrame,contours,-1,(0,0,255),3)
##    processedFrame=cv2.adaptiveThreshold(frame,255,\
##                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
##    ret,processedFrame = cv2.threshold(processedFrame,100,255,cv2.THRESH_BINARY)
    #结束处理
    #frame=np.hstack((frame, processedFrame))
    cv2.imshow(windowName1, frame)
    cv2.imshow(windowName2, processedFrame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
    if cv2.waitKey(40) & 0xFF == ord('s'):
        cv2.waitKey(0)
    if win32gui.FindWindow(None,windowName1) and win32gui.FindWindow(None,windowName2):
        pass
    else:
        cv2.destroyAllWindows()
        break
endTime=time.time()
print(endTime-startTime,'s')

cap.release()
cv2.destroyAllWindows()
