import cv2
import time
import matplotlib.pyplot as plt
from keras.preprocessing import image
import numpy as np
from keras.models import save_model, load_model
import os,subprocess
import pyttsx3
eng=pyttsx3.init()
volume = eng.getProperty('volume')
eng.setProperty('volume', volume-0.00)
rate = eng.getProperty('rate')
eng.setProperty('rate', rate-10)
print("Welcome to Smart Music System U have 3 sec for Capturing Image!! ")
eng.say("Welcome to Smart Music System U have 3 sec for Capturing Image ")
eng.runAndWait()
c=0
cv2.namedWindow("My_image")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, img = vc.read()
else:
    rval = False
while rval:
	
	cv2.imshow("My_image",img) # try to get the first frame
	rval, img= vc.read()
	key = cv2.waitKey(20)
	if c==40:
		break
	c=c+1
del(vc)
cv2.imwrite("Music.png",img)
cv2.destroyWindow("My_image")
print("Wait I am playing songs according your emotion !! ")
eng.say("Wait I am playing songs according your emotion ")
eng.runAndWait()

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
img = image.load_img("Music.png", grayscale=True, target_size=(64, 64))

x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)

x /= 255

model =load_model("fer2013_mini_XCEPTION.110-0.65.hdf5")
result=model.predict(x)
print (label_map)

b=result.ravel()
print(b)
m=max(b)
print(m)
for i in range(len(b)):
    if b[i]==m:
        index=i
name=label_map[index]
print(name)
eng.say("You are ")
eng.say(name)
eng.runAndWait()
sad_fold="/home/codesnow/Documents/techienest/sad_song"
other_fold="/home/codesnow/Documents/techienest/other_song"
happy_fold="/home/codesnow/Documents/techienest/happy_song"
if name=="Happy"or name=="Surprise":
	fold=happy_fold
elif name=="anger" or name=="Neutral":
	fold=other_fold
else:
	fold=sad_fold

subprocess.Popen(["vlc",fold])
