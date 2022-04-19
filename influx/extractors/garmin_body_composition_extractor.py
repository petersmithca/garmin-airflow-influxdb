from influx.extractors.garmin_extractor import GarminExtractor


class GarminBodyCompositionExtractor(GarminExtractor):
    task = "get_body_composition('{extract_date}')"
