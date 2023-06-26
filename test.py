from Flask_API import orchestrator

if __name__ == '__main__':
    #llm_response_generator = llm_output_generator.LlmResponseGenerator("gpt-35-turbo-us")
    #x = llm_response_generator.get_llms_response("0 size warm suit for kids")
    #print(x)

    #product_id_fetcher_ = product_id_fetcher.ProductIdFetcher(30)
    #x = product_id_fetcher_.get_product_ids("nike shoes")
    #print(x)

    #image_url_fetcher_ = image_url_fetcher.ImageUrlFetcher()
    #x = image_url_fetcher_.get_image_url("SHOFYFTZUKJF7GMY")
    #print(x)

    orchestrator_app = orchestrator.Orchestrator("gpt-35-turbo-us")
    x = orchestrator_app.generate_response("0 size warm suit for kids")
    print(x)
