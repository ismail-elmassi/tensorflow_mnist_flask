import cv2
import numpy
from tensorflow.keras.models import load_model
model=load_model("dpl_model/mnist_model.h5")
def predict_image(input_image):
	img=cv2.imread(input_image)	
	img_bin=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_res = cv2.resize(img_bin, (28, 28))
	img_res=img_res/255.0
	img2=numpy.expand_dims(img_res,axis=0)
	classe=model.predict_classes(img2)
	return classe