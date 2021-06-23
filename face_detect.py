import cv2
#import sys

# Get user supplied values
#imagePath = 
#cascPath = 

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread('chicos.jpeg')
# Convierte la imagen a Blanco y Negro
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.1, 4)


                #faces = faceCascade.detectMultiScale(
                #    gray,
                #    scaleFactor=1.2,
                #    minNeighbors=5,
                #    minSize=(30, 30),
                #    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
                #)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Detectando Rostros by Charlie83CL", image)
cv2.waitKey(0)
