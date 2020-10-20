import cv2




def main():
    
    imagem = cv2.imread("pessoas.jpg");
    
    #carrega um classificador de um arquivo
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #somente funciona com tons de cinza
    imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    '''
    detecta faces de diferentes tamanhos 
    -> primeiro parametro: imagem em tons de cinza
    -> segundo parametro: especifica o quanto a imagem reduz de tamanho durante a verificacao
    -> terceiro parametro: especifica quantos vizinhos cada candidato a retangulo retêm
    '''
    deteccoes = face_cascade.detectMultiScale(imagemcinza, scaleFactor=1.3,
                                           minNeighbors=5,
                                           minSize=(30, 30))
                                           #maxSize=(40, 40))


    print(deteccoes)
    print(len(deteccoes))

    for(x, y, w, h) in deteccoes: #caixas delimitadoras (left, top, width, height)

        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Detector de faces", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
