from influx.transformers.base_transformer import BaseTransformer


class VPNIPTransformer(BaseTransformer):
    def transform(self, feed):
        results = [{"vpnIP": feed.strip()}]

        return results
