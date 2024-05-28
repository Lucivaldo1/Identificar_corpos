import cv2

imagem = cv2.imread(r'C:\Users\luciv\OneDrive\Documents\Identificar corpos\corpos.png')

detector_corpos = cv2.CascadeClassifier(r'C:\Users\luciv\OneDrive\Documents\Identificar corpos\haarcascade_fullbody.xml')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccao = detector_corpos.detectMultiScale(imagem_cinza)

for (x, y, l, a) in deteccao:

    cv2.rectangle(imagem, (x,y), (x + l, y + a), (0,255,0), 1)

cv2.imshow('Deteccao de corpos', imagem)

cv2.waitKey(0)