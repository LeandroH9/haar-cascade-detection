import cv2

def main():
    
    imagem1 = cv2.imread("imagens_teste_canecas/teste01.png");
    imagem2 = cv2.imread("imagens_teste_canecas/teste01.png");
    imagem3 = cv2.imread("imagens_teste_canecas/teste01.png");
    
    #carrega um classificador de um arquivo
    classificador1 = cv2.CascadeClassifier('cascade_caneca1.xml')
    classificador2 = cv2.CascadeClassifier('cascade_caneca2.xml')
    classificador3 = cv2.CascadeClassifier('cascade_caneca3.xml')
    
    #somente funciona com tons de cinza
    imagemcinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
    imagemcinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)
    imagemcinza3 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

    deteccoes1 = classificador1.detectMultiScale(imagemcinza1, scaleFactor=1.2, minNeighbors=4)
    deteccoes2 = classificador2.detectMultiScale(imagemcinza2, scaleFactor=1.2, minNeighbors=4)
    deteccoes3 = classificador3.detectMultiScale(imagemcinza3, scaleFactor=1.2, minNeighbors=4)


    for(x, y, w, h) in deteccoes1: #caixas delimitadoras (left, top, width, height)
        cv2.rectangle(imagem1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for(x, y, w, h) in deteccoes2: #caixas delimitadoras (left, top, width, height)
        cv2.rectangle(imagem2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for(x, y, w, h) in deteccoes3: #caixas delimitadoras (left, top, width, height)
        cv2.rectangle(imagem3, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imshow("Classificador 1", imagem1)
    cv2.imshow("Classificador 2", imagem2)
    cv2.imshow("Classificador 3", imagem3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
