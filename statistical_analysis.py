class StatisticalAnalysis:
    def analysis(self, image):
        features = extract_features(image)
        return detect_anomalies(features)
    
    def extract_features(self, image):


    def detect_anomalies(self, features):