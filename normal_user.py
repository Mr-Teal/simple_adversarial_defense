import random

class NormalUserInterface:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def submit_query(self):
        # get random image from dataset(cifar10)
        random.seed()
        return random.choice(self.dataset)
