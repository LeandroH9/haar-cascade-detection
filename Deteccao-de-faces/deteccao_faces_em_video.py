import cv2

def main():

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if cap.isOpened() == False:
        print("Erro ao abrir a camera")

    while cap.isOpened():
        (ret, frame) = cap.read()

        if not ret:
            break
    
    
        #carrega um classificador de um arquivo

        #somente funciona com tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        '''
        detecta faces de diferentes tamanhos
        -> primeiro parametro: imagem em tons de cinza
        -> segundo parametro: especifica o quanto a imagem reduz de tamanho durante a verificacao
        -> terceiro parametro: especifica quantos vizinhos cada candidato a retangulo retêm
        retorna uma lista faces
        '''
        deteccoes = face_cascade.detectMultiScale(gray, scaleFactor=1.09, minNeighbors=5)
                                               #minSize=(30, 30))
                                               #maxSize=(40, 40))

        print(len(deteccoes))

        for(x, y, w, h) in deteccoes: #caixas delimitadoras (left, top, width, height)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Detector de faces", frame)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
