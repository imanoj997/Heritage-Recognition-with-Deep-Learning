#%%
from keras.models import load_model

import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

#%%
#Loading already trained model
model = load_model('trained_model.hdf5')
print("Trained model loaded")

#%%
# Testing a new image
from keras import backend as K
K.set_image_dim_ordering('th')
from tkinter import filedialog
from tkinter import *

temples = {0:"Bhandarkhal Tank", 1:"Bhimsen Temple", 2:"Char Narayan Temple", 3:"Chyasing Dewal",
           4: "Degu Taleju Temple", 5:"Garud Pillar", 6:"Keshav Narayan Temple", 7:"Kopeshvara Temple", 
           8:"Krishna Mandir",9:"Mani Chaitya", 10:"Mani Dhara", 11:"Maniganesh Temple",
           12:"Patan Museuem", 13:"Narasimha Temple", 14:"North Taleju Temple",
           15:"South Taleju Temple", 16:"Taleju Bell", 17:"Tushahiti", 
           18:"Yantaju Shrine", 19:"Yoganarendra Pillar"}
root = Tk()
root.withdraw()
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/Anima/Desktop/testHeritagesVGG16/test",title = "Select Image File",
                                            filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
root.destroy()
imagePath = root.filename

#%%
img = image.load_img(imagePath, target_size=(224, 224))
test_image = image.img_to_array(img)
#test_image = np.expand_dims(test_image, axis=0)
test_image = preprocess_input(test_image)
test_image=np.moveaxis(test_image,0,-1)
print('Input image shape:', test_image.shape)
test_image = np.expand_dims(test_image, axis=0)

		
# Predicting the test image
classProba = model.predict(test_image)
print((model.predict(test_image)))
recognisedClass = np.argmax(classProba)
print("This is " + temples[recognisedClass])

