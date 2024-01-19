import cv2
import numpy as np
import tensorflow as tf

#get a random image
img = 

def random_noise(img):
    #add random noise to the image
    mean = 0
    sd = 180
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, sd)
    noisy_img = cv2.add(img, noise)
    return noisy_img

def fgsm(img, label):
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