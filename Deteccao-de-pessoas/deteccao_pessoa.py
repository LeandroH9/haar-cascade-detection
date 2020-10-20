import cv2

cap = cv2.VideoCapture('lab10-camera1-positivas.MP4')
img = cv2.imread('pessoas_juntas.jpg')

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

if cap.isOpened():
    while True:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            break
        
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        deteccoes = body_cascade.detectMultiScale(gray, scaleFactor=1.09, minNeighbors=5)

        print(len(deteccoes))

        for (x, y, w, h) in deteccoes: #caixas delimitadoras (left, top, width, height)

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        frame_rezided = cv2.resize(frame, (600, 400))
        
        cv2.imshow("Detector de pessoas em video", frame_rezided)
        cv2.imshow("Detector de pessoas em foto", img)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
