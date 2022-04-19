from influx.transformers.base_transformer import BaseTransformer


class IPTransformer(BaseTransformer):
    def transform(self, feed):
        results = [{"internalIP": feed.strip()}]

        return results
