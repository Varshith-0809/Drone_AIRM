from ultralytics import YOLO
import cv2
import math
import cvzone

model = YOLO('../Yolo-weights/yolov8n.pt') #using nano model
classNames = r"C:\Users\varsh\PycharmProjects\droneod\coco.names"

cap = cv2.VideoCapture(0)
cap.set(3, 480) # the size of the screen width
cap.set(4, 480) # the size of the screen height

while True:
    success, img = cap.read() # capturing through the video cam
    results = model(img, stream = True)
    for r in results:   #your creating a box around the object whihc is created
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2-y1
            cvzone.cornerRect(img, (x1, y1, w, h), l=15)
            conf = math.ceil(box.conf[0]*100)/100 #confidence values
            print(conf)

            cls = int(box.cls[0]) #class id
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1) #conf and classnames


    cv2.imshow("img", img) #show the capturing
    cv2.waitKey(1) #so that the window will be open until we stop