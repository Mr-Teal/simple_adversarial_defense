class QueryMonitor:
    def __init__(self, threshold):
        self.threshold = threshold
        self.queries = []
    
    def record_queries(self, timestamp):
        self.queries.append(timestamp)
        self.clean_old_queries(timestamp)
    
    def clean_old_queries(self, timestamp):
        while timestamp - self.queries[0] > 60:
            self.queries.pop(0)

    def check_for_unusual_activity(self):
        return len(self.queries) > self.threshold