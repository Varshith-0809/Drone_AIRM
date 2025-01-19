from ultralytics import YOLO
import cv2
import math
import cvzone

model = YOLO('../Yolo-weights/yolov8n.pt') #using nano model
classNames = ["person","bicycle","car","motorcycle",
"airplane",
"bus",
"train",
"truck",
"boat",
"traffic light",
"fire hydrant",
"street sign",
"stop sign",
"parking meter",
"bench",
"bird",
"cat",
"dog",
"horse",
"sheep",
"cow",
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
"tv",
"laptop",
"mouse",
"remote",
"keyboard",
"cell phone",
"microwave",
"oven",
"toaster",
"sink","refrigerator","blender","book","clock","vase",
"scissors","teddy bear","hair drier","toothbrush","hair brush"]


cap = cv2.VideoCapture(r"C:\Users\varsh\PycharmProjects\droneod\Cars Moving On Road Stock Footage - Free Download.mp4")

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

            cls = int(box.cls[0]) #class id
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1) #conf and classnames


    cv2.imshow("img", img)
    cv2.waitKey(1)