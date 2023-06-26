import requests


class ProductIdFetcher:
    def __init__(self, product_count):
        self.product_count = product_count

    def get_aggregator_response(self, query, product_count):
        model_server_url = 'http://10.83.36.200:25280/sherlock/v1/stores/search.flipkart.com/iterator?debug=true&p13nCohort=null&pincode=560103&isCncUser=false&query-stub=true&enableNewHeaders=true&query-guide=true&geoBrowse=enabled&cache-disable=true&cache-get-false=false&mBucket[]=enableSemV2&flow-info=true'

        params = {
            'q': query,
            'products.count': product_count
        }

        r = requests.get(model_server_url, params=params).json()
        res = r['RESPONSE']
        return res

    def get_product_ids(self, query):
        aggregator_response = self.get_aggregator_response(query, self.product_count)
        product_num_found = aggregator_response['products']['num_found']
        product_ids = aggregator_response['products']['ids']
        return product_num_found, product_ids
