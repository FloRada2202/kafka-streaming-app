class KafkaStreamEvent:
    def __init__(self, uid, timestamp):
        self.uid = uid
        self.timestamp = timestamp
    
    def get_uid(self):
        return self.uid
    
    def get_timestamp(self):
        return self.timestamp
