import keras
from keras.applications import resnet, vgg19, inception_v3
import numpy as np
import random

class ImageClassifier:
    def __init__(self):
        # randomly choose model(resnet, vgg19, or inception_v3)
        random.seed()
        self.modelNum = random.randint(1, 3)
        if self.modelNum == 1:
            self.model = resnet.ResNet50(weights="imagenet")
        elif self.modelNum == 2:
            self.model = vgg19.VGG19(weights="imagenet")
        else:
            self.model = inception_v3.InceptionV3(weights="imagenet")

    def classify(self, image):
        # read image and predict
        x = keras.utils.img_to_array(image)
        x = np.expand_dims(x, axis=0)
        if self.modelNum == 1:
            x = resnet.preprocess_input(x)
            y = self.model.predict(x)
            predictions = resnet.decode_predictions(y, top = 3)[0]
        elif self.modelNum == 2:
            x = vgg19.preprocess_input(x)
            y = self.model.predict(x)
            predictions = vgg19.decode_predictions(y, top = 3)[0]
        else:
            x = inception_v3.preprocess_input(x)
            y = self.model.predict(x)
            predictions = inception_v3.decode_predictions(y, top = 3)[0]

        return predictions
