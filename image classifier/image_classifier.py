import keras
from keras.applications import resnet, vgg19, inception_v3
import numpy as np
import random

# randomly choose model(resnet, vgg19, or inception_v3)
random.seed()
r = random.randint(1, 3)
if r==1:
    model = resnet.ResNet50(weights="imagenet")
elif r==2:
    model = vgg19.VGG19(weights="imagenet")
else:
    model = inception_v3.InceptionV3(weights="imagenet")

# read image and predict
img = 
x = keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
if r==1:
    x = resnet.preprocess_input(x)
elif r==2:
    x = vgg19.preprocess_input(x)
else:
    x = inception_v3.preprocess_input(x)
y = model.predict(x)
pred = resnet.decode_predictions(y, top = 3)[0]

# output
#print(pred)