from influx.extractors.garmin_extractor import GarminExtractor


class GarminSleepExtractor(GarminExtractor):
    task = "get_sleep_data('{extract_date}')"
