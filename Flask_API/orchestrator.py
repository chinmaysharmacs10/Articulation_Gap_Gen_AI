import random

from Flask_API.Models.llm_output_generator import LlmResponseGenerator
from Flask_API.Models.product_id_fetcher import ProductIdFetcher
from Flask_API.Models.image_url_fetcher import ImageUrlFetcher


class Orchestrator:
    def __init__(self, engine, product_count):
        self.engine = engine
        self.product_count = product_count

    def generate_response(self, query):
        # call llm to get tagging
        llm_response_generator = LlmResponseGenerator(self.engine)
        lucene_query, expanded_query_list, reformulated_query = llm_response_generator.process_end_to_end(query)

        # fetch product ids
        top_product_ids = self.get_top_product_ids(expanded_query_list)

        # fetch image urls for images
        image_urls = self.get_image_urls_list(top_product_ids)

        return image_urls, expanded_query_list, reformulated_query, lucene_query

    def get_top_product_ids(self, queries):
        max_products = 30//len(queries)
        top_product_ids = []
        product_id_fetcher_ = ProductIdFetcher(self.product_count)

        for query in queries:
            product_num_found, product_ids = product_id_fetcher_.get_product_ids(query)
            num_products = min(product_num_found, max_products)
            products = product_ids[:num_products]
            for product in products:
                top_product_ids.append(product)

        random.shuffle(top_product_ids)
        return top_product_ids

    def get_image_urls_list(self, product_ids):
        image_url_fetcher_ = ImageUrlFetcher()
        image_urls = []
        for product_id in product_ids:
            image_url = image_url_fetcher_.get_image_url(str(product_id))
            image_urls.append(image_url)
        return image_urls
