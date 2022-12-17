import cv2
import numpy as np
import random 

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, -2)
cam.set(cv2.CAP_PROP_AUTO_WB, 0)

random_colors = ["blue", "red", "green"]
random.shuffle(random_colors)
print(random_colors)
    
lower_blue = np.array([95, 70, 140])
upper_blue = np.array([105, 255, 255])

lower_green = np.array([50, 20, 120])
upper_green = np.array([90, 120, 255])

lower_red = np.array([170, 100, 90])
upper_red= np.array([255, 255, 255])


while(cam.isOpened):
    _, frame = cam.read()
    linebal = {}
    frame = cv2.GaussianBlur(frame,(11,11),0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2= cv2.inRange(hsv, lower_red, upper_red)
    mask3 = cv2.inRange(hsv, lower_green, upper_green)

    contours1 = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours2= cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours3 = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    #contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    #if len(contours) > 0:
    #    c = max(contours, key=cv2.contourArea)
    #    (x, y), radius = cv2.minEnclosingCircle(c)
    #    if radius > 20:
    #        cv2.circle(frame, (int(x), int(y)),int(radius),
    #                                       (0, 255, 255, 0), 0)
    for i in range(3):
        if len(contours1) > 0:
            c = max(contours1, key=cv2.contourArea)
            (x,y), radius = cv2.minEnclosingCircle(c)
            if radius > 20:
                cv2.circle(frame, (int(x), int(y)), int(radius), 
                                                  (0,255,255,0), 0)
                color1="blue"
                linebal[color1]=x
        if len(contours2) > 0:
            c = max(contours2, key=cv2.contourArea)
            (x,y), radius = cv2.minEnclosingCircle(c)
            if radius > 20:
                cv2.circle(frame, (int(x), int(y)), int(radius), 
                                                  (0,255,255,0), 0)
                color2="red"
                linebal[color2]=x
        if len(contours3) > 0:
            c = max(contours3, key=cv2.contourArea)
            (x,y), radius = cv2.minEnclosingCircle(c)
            if radius > 20:
                cv2.circle(frame, (int(x), int(y)), int(radius), 
                                                (0,255,255, 0), 0)
                color3="green"
                linebal[color3]=x
    linebal_sort = sorted(linebal,key=linebal.get)
    
    if len(linebal_sort)==3:
        print("Right")
    else:
        print("False")

    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
cv2.destroyAllWindows()