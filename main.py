import image_classifier
import normal_user
import query_monitor
import simple_attacker
import statistical_analysis
from keras.datasets import cifar10

def main():
    classifier = image_classifier.ImageClassifier()
    normalUser = normal_user.NormalUserInterface(cifar10)
    attacker = simple_attacker.AttackerInterface()
    queryMonitor = query_monitor.QueryMonitor(threshold = 10)
    statisticalAnalysis = statistical_analysis()


if __name__ == '__main__':
    main()