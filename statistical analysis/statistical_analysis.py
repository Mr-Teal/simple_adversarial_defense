class StatisticalAnalysis:
    def analysis(self, image):
        features = extract_features(image)
        return detect_anomalies(features)