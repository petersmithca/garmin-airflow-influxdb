from influx.extractors.garmin_extractor import GarminExtractor


class GarminStatsExtractor(GarminExtractor):
    task = "get_stats('{extract_date}')"
