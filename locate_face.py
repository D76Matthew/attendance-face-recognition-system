import cv2
import numpy as nppip
import face_recognition

imgelon_bgr = face_recognition.load_image_file('Images/elon.jpg')
imgelon_rgb = cv2.cvtColor(imgelon_bgr,cv2.COLOR_BGR2RGB)
imgelon = face_recognition.load_image_file('Images/elon.jpg')
imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
#----------Finding face Location for drawing bounding boxes-------
face = face_recognition.face_locations(imgelon_rgb)[0]
copy = imgelon.copy()
#-------------------Drawing the Rectangle-------------------------
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
cv2.imshow('copy', copy)
cv2.imshow('elon',imgelon)
cv2.waitKey(0)