import os
import numpy as np
import cv2
from keras.models import load_model
from keras import backend as K

def asymmetric_loss(y_true,y_pred):
	alpha=0.30
	return K.mean(K.abs(y_pred - y_true)*(alpha*y_true+(1-alpha)*(1-y_true)), axis=-1)

filename_image = 'data/images/test.png'	
model_filename = 'model/net.h5'
model = load_model(model_filename, custom_objects={'asymmetric_loss': asymmetric_loss})
img = cv2.imread(filename_image)
img = cv2.resize(img, (128, 128), interpolation = cv2.INTER_CUBIC)
lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
gray_img = lab_image[:,:,0]/255.0
x[i,:,:,0] = gray_img
y_pred = model.predict(x)
mask = 255*(y_pred[0,:,:,0])
cv2.imwrite('res.png',mask)




