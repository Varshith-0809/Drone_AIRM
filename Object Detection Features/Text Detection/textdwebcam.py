import cv2
import pytesseract
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture(r'C:\Users\varsh\PycharmProjects\droneod\text.mp4') # for video testing

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cannot open cam")

cntr = 0
while True:
    ret, frame = cap.read()
    cntr = cntr + 1;
    if (( cntr%20 )==0):
        imgH, imgW, _ = frame.shape
        x1, y1, w1, h1 = 0, 0, imgH, imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)

        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            #cv2.rectangle(frame, (x, imgH - y), (w, imgH-y), (0,0,255), 3)
            cv2.putText(frame, imgchar, (x1 + int(w1/50), y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.imshow('Result', frame)
            if cv2.waitKey(0) & 0xff == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()

