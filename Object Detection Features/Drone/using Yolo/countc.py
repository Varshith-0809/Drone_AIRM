from ultralytics import YOLO
import cv2
import math
import cvzone
from sort import *

model = YOLO('../Yolo-weights/yolov8n.pt') #using nano model
classNames = ["person","bicycle","car","motorcycle",
"airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "street sign", "stop sign",
"parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
"elephant",
"bear",
"zebra",
"giraffe",
"hat",
"backpack",
"umbrella",
"shoe",
"eye glasses",
"handbag",
"tie",
"suitcase",
"frisbee",
"skis",
"snowboard",
"sports ball",
"kite",
"baseball bat",
"baseball glove",
"skateboard",
"surfboard",
"tennis racket",
"bottle",
"plate",
"wine glass",
"cup",
"fork",
"knife",
"spoon",
"bowl",
"banana",
"apple",
"sandwich",
"orange",
"broccoli",
"carrot",
"hot dog",
"pizza",
"donut",
"cake",
"chair",
"couch",
"potted plant",
"bed",
"mirror",
"dining table",
"window",
"desk",
"toilet",
 "door",
 "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven",
 "toaster", "sink", "refrigerator", "blender", "book", "clock", "vase",
 "scissors" , "teddy bear", "hair drier", "toothbrush", "hair brush"]

#cap = cv2.VideoCapture(0)
#cap.set(3, 480) # the size of the screen width
#cap.set(4, 480) # the size of the screen height

cap = cv2.VideoCapture(r"C:\Users\varsh\PycharmProjects\droneod\Cars Moving On Road Stock Footage - Free Download.mp4")
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)
limits = [433,297,673,297]
totalCount = []

while True:
    success, img = cap.read()
    results = model(img, stream = True)

    detections = np.empty((0, 5))
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2-y1

            conf = math.ceil(box.conf[0]*100)/100 #confidence values
            print(conf)

            cls = int(box.cls[0]) #class id
            currentClass = classNames[cls]

            if currentClass == "car" or currentClass == "truck" or currentClass == "bus" \
                    or currentClass == "motorbike" and conf > 0.3:
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update(detections)
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5) #for line
    for result in resultsTracker:
        x1,y1,x2,y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 255))
        cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)
        cx, cy = x1+w//2, y1+h//2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        if limits[0] < cx < limits[2] and limits[1] - 20 < cy < limits[1] + 20:
            if totalCount.count(id) == 0:
                totalCount.append(id)
    cvzone.putTextRect(img, f'Count:{len(totalCount)}', (50, 50))

    cv2.imshow("img", img)
    cv2.waitKey(0)