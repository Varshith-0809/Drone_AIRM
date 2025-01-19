import cv2
from djitellopy import tello
import cvzone

thres = 0.6
nmsThres = 0.2
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
print(classNames)

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold = thres , nmsThreshold = nmsThres)
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className.lower() == "knife":
                cvzone.cornerRect(img, box)
                cv2.rectangle(img, box, color=(0, 0, 255), thickness=2)
                cv2.putText(img, "Threat object detected", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 0, 255), 2)
            else:
                cvzone.cornerRect(img, box)
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                            (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

    except:
        pass
    cv2.imshow("image", img)
    cv2.waitKey(1)


