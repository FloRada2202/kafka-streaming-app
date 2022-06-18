import logging

from datetime import datetime

logging.basicConfig(level=logging.INFO)

class KafkaEventsProcessor:
    def __init__(self):
        self.distinct_uids_mapping = set()
        self.current_time_processing = None

    def add_event(self, event):
        event_timestamp_to_time = self.convert_unix_timestamp_to_time(unix_timestamp=event.get_timestamp())

        if self.current_time_processing is None:
            self.current_time_processing = event_timestamp_to_time
            self.distinct_uids_mapping.add(event.get_uid())
        elif event_timestamp_to_time != self.current_time_processing:
            self.print_unique_uids_count_per_minute(event_time=self.current_time_processing)
            self.current_time_processing = event_timestamp_to_time
            self.distinct_uids_mapping.add(event.get_uid())
        else:
            self.distinct_uids_mapping.add(event.get_uid())

    def convert_unix_timestamp_to_time(self, unix_timestamp):
        return datetime.fromtimestamp(unix_timestamp).strftime('%H:%M')
    
    def print_unique_uids_count_per_minute(self, event_time):
        logging.info(len(self.distinct_uids_mapping))
        self.distinct_uids_mapping.clear()
