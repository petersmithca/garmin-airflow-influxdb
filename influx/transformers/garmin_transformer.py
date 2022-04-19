import pandas as pd

from influx.transformers.base_transformer import BaseTransformer


class GarminTransformer(BaseTransformer):
    def transform(self, feed):
        return self.flatten_dicts(feed)

    def flatten_dicts(self, feed):
        dicts = []
        if isinstance(feed, dict):
            feed["tag"] = self.tag
            df = pd.json_normalize(feed, sep="_")
            dicts.append(df.to_dict(orient="records")[0])
        else:
            for dictfeed_item in feed:
                dicts.extend(self.flatten_dicts(dictfeed_item))
        print(dicts)
        return dicts


class GarminActivitiesTransformer(GarminTransformer):
    tag = "activityId"


class GarminBodyCOmpositionTransformer(GarminTransformer):
    tag = "samplePk"

    def transform(self, feed):
        return self.flatten_dicts(feed["dateWeightList"][-1])


class GarminStatsTransformer(GarminTransformer):
    tag = "wellnessEndTimeGmt"


class GarminSleepTransformer(GarminTransformer):
    tag = "dailySleepDTO_id"
