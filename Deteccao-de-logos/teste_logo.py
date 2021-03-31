import cv2

imagem = cv2.imread('teste/foo-fighters-logo-hoodie.jpg')
imagem2 = cv2.imread('teste/logoff.jpg')

classificador = cv2.CascadeClassifier('cascade_logo.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagemcinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
deteccoes2 = classificador.detectMultiScale(imagemcinza2, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))

for (x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

for (x, y, l, a) in deteccoes2:
    cv2.rectangle(imagem2, (x, y), (x + l, y + a), (0,255,0), 2)
    
cv2.imshow('Detector de logos 1', imagem)
cv2.imshow('Detector de logos 2', imagem2)
cv2.waitKey(0)
cv2.destroyAllWindows()
