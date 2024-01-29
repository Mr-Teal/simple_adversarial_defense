import cv2
import numpy as np
import tensorflow as tf
import random

class AttackerInterface:
    def __init__(self):
        random.seed()
        methodNum = random.randint(1, 2)
        if methodNum == 1:
            self.attack_method = self.random_noise()
        elif methodNum == 2:
            self.attack_method = self.fgsm()
    
    def generate_adversarial_sample(self, image, label):
        return self.attack_method(image, label)

    def random_noise(self, image, label):
        # add random noise to the image
        mean = 0
        sd = 180
        noise = np.zeros(image.shape, np.uint8)
        cv2.randn(noise, mean, sd)
        noisy_img = cv2.add(image, noise)
        return noisy_img

    def fgsm(self, image, label):
        # use fgsm method; assume the model being vgg19
        loss_object = tf.keras.losses.CategoricalCrossentropy()
        model = tf.keras.model.vgg19.VGG19(weights='imagenet')

        with tf.GradientTape() as tape:
            tape.watch(image)
            prediction = model(image)
            loss = loss_object(label, prediction)

        # Get the gradients of the loss w.r.t to the input image.
        gradient = tape.gradient(loss, image)
        # Get the sign of the gradients to create the perturbation
        signed_grad = tf.sign(gradient)
        
        adv_image = image + signed_grad[0] * .5 + .5
        return adv_image

    def submit_query(self, image, label):
        adversarial_image = self.generate_adversarial_sample(image, label)
        return adversarial_image
