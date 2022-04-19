from influx.transformers.base_transformer import BaseTransformer


class IPGeoTransformer(BaseTransformer):
    def transform(self, feed):
        results = [feed]

        return results
