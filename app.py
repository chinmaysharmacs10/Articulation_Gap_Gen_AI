from flask import Flask, request, render_template, jsonify
import json

from Flask_API.orchestrator import Orchestrator

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/predict', methods=['POST'])
def predict():
    query = request.form['query']

    orchestrator_app = Orchestrator("gpt-35-turbo-us", 30)
    image_urls, expanded_query_list, reformulated_query, lucene_query = orchestrator_app.generate_response(str(query))

    result = {'queries': expanded_query_list, 'imageUrls': image_urls, 'reformulatedQuery': reformulated_query,
              'luceneQuery': lucene_query}

    return jsonify(result)


@app.route('/predict_local', methods=['GET'])
def predict_local():
    query = request.args.get('input')

    orchestrator_app = Orchestrator("gpt-35-turbo-us", 30)
    image_urls, expanded_query_list, reformulated_query, lucene_query = orchestrator_app.generate_response(str(query))

    result = {'expanded_query_list': expanded_query_list, 'imageUrls': image_urls,
              'reformulatedQuery': reformulated_query, 'lucene_query': lucene_query}

    response = json.dumps({'results': result})
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)
