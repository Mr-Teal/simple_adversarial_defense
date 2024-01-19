from keras.datasets import cifar10
from keras.datasets import mnist
import random

random.seed()
r = random.randint(0, 1)
if r==0:
    x_train, y_train, x_test, y_test = cifar10.load_data()
else:
    x_train, y_train, x_test, y_test = mnist.load_data()
random.seed()
index = random.randint(0, len(y_train) - 1)
img = x_train[index, :]
