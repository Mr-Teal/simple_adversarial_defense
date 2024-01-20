import cv2
import numpy as np
import tensorflow as tf
import random

def random_noise(img):
    # add random noise to the image
    mean = 0
    sd = 180
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, sd)
    noisy_img = cv2.add(img, noise)
    return noisy_img

def fgsm(img, label):
    # use fgsm method
    loss_object = tf.keras.losses.CategoricalCrossentropy()
    model = tf.keras.model.vgg19.VGG19(weights='imagenet')

    with tf.GradientTape() as tape:
        tape.watch(img)
        prediction = model(img)
        loss = loss_object(label, prediction)

    # Get the gradients of the loss w.r.t to the input image.
    gradient = tape.gradient(loss, img)
    # Get the sign of the gradients to create the perturbation
    signed_grad = tf.sign(gradient)
    return signed_grad


# get a random image and randomly choose perturbation method to get the adversarial example
img = 

random.seed()
r = random.randint(1, 2)
if r == 1:
    adv_img = random_noise(img)
else:
    eps = 0.01
    perturbation = fgsm(img)
    adv_img = img + eps * perturbation

# submit the adversarial image
