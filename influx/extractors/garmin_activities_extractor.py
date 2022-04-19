from influx.extractors.garmin_extractor import GarminExtractor


class GarminActivitiesExtractor(GarminExtractor):
    task = "get_activities(0, 3)"
