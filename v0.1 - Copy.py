import cv2 as cv
import serial

sobj = serial.Serial("COM10")
sobj.baudrate = 9600
sobj.bytesize = 8
sobj.parity = 'N'
sobj.stopbits = 1

cap = cv.VideoCapture(0)
d = cv.QRCodeDetector()

def func1(data):
    data = data.lower()
    if data == "on":
        sobj.write(b'A')
    if data == "off":
        sobj.write(b'B')

while True:
    ret, frame = cap.read()
    frame = cv.resize(frame, (400, 400))
    qtext, p1, _ = d.detectAndDecode(frame)

    if p1 is not None:
        func1(qtext)

    cv.imshow('WebCam Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

