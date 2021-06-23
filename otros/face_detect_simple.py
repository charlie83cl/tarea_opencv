import cv2

#aca se invoca un archivo xml que tiene todo el analisis de las imagenes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#aca se selecciona la fuente de la imagen
img = cv2.imread('abba.png')
#en el siguiente  proceso se convierte la imagen de color a BN
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#aca se crean los rectangulos de color en las caras
for (x, y , w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
#aca se muestra el producto final y la muestra funcionando
cv2.imshow('Detector_Facial_by_Charlie', img)
cv2.waitKey()
