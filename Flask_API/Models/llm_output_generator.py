from ast import literal_eval

import openai
import json

openai.api_type = "azure"
openai.api_base = "https://fk-open-ai-resource1.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "5f2c3cb2ce784a8da0cf9c43538c8c96"

MAX_WORKERS = 25


class LlmResponseGenerator:
    def __init__(self, engine):
        self.engine = engine

    def get_llms_response(self, query):
        try:
            response = openai.ChatCompletion.create(
                engine=self.engine,
                messages=[
                    {
                        "role": "system",
                        # "content": "Given the below text, perform the following processing and generate the final result without any additional descriptive text. You can rephrase text results with what it is also known as?. Do not change brand tokens."
                        # "content": "Given the below text, perform the following preprocessing and generate the final result without any additional descriptive text in indian context. You can rephrase text results with what it is also called as?"
                        "content": "Identify the product, age group, and any other important details in the \
                                           input sentence. Use a popular synonym for the product name if the original one is uncommon. \
                                           Consider less than 1 year age as baby or newborn. \
                                           Generate a structured response. \
                                           Drop redundant or ambiguous terms."
                    },
                    {
                        "role": "user",
                        "content": "12 years kids shirt"
                    },
                    {
                        "role": "assistant",
                        "content": '"{"product": "shirt","age": "12 years", "gender": "any"}"'
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                temperature=0.0,
                max_tokens=800,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None)

            res = json.loads(str(response))
            res1 = res['choices'][0]['message']['content']
            return res1
        except Exception as e:
            print("Exception: ", e)
            return None

    def get_structured_response(self, query):
        # query = "0 years baby sweater"
        try:
            response = openai.ChatCompletion.create(
                engine="gpt-35-turbo-us",
                messages=[
                    {
                        "role": "system",
                        # "content": "Given the below text, perform the following processing and generate the final result without any additional descriptive text. You can rephrase text results with what it is also known as?. Do not change brand tokens."
                        # "content": "Given the below text, perform the following preprocessing and generate the final result without any additional descriptive text in indian context. You can rephrase text results with what it is also called as?"
                        "content": "Identify the product, age group, and any other important details in the \
                                           input sentence. Use a popular synonym for the product name if the original one is uncommon. \
                                           When age and word in the input do not match then drop the word and go by the age.  \
                                           Consider less than 1 year age as baby or newborn. \
                                           Generate a structured response. Do not generate unneccesary verbose.\
                                           Delete any redundant, adjective and ambiguous terms."},

                    {
                        "role": "user",
                        "content": "12 years kids shirt"
                    },
                    {
                        "role": "assistant",
                        "content": '<SEP>{"product": "shirt","age": "12 years", "gender": "any"}'
                    },
                    {
                        "role": "user",
                        "content": "20 years kids shirt"
                    },
                    {
                        "role": "assistant",
                        "content": '<SEP>{"product": "shirt","age": "20 years", "gender": "any"}'
                    },
                    {
                        "role": "user",
                        "content": "10 years baby jeans"
                    },
                    {
                        "role": "assistant",
                        "content": '<SEP>{"product": "jeans","age": "10 years", "gender": "any"}'
                    },

                    {
                        "role": "user",
                        "content": "5 years bacha clothes"
                    },
                    {
                        "role": "assistant",
                        "content": '<SEP>{"product": "clothes","age": "5 years", "gender": "boy"}'
                    },
                    {
                        "role": "user",
                        "content": "navari saree 15 years bachi"
                    },
                    {
                        "role": "assistant",
                        "content": '<SEP>{"product": "navari saree","age": "15 years", "gender": "girl"}'
                    },
                    {
                        "role": "user",
                        "content": query
                    }

                ],
                temperature=0.0,
                max_tokens=800,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None)

            # print(response)
            res = json.loads(str(response))
            res1 = res['choices'][0]['message']['content']
            # print(res1)
            if "sorry" in res1 or "unclear" in res1:
                # print("here")
                return query
            else:
                return res1
        except Exception as e:
            print("Exception")
            return query

    def get_phrase_replacement(self, query):
        try:
            response = openai.ChatCompletion.create(
                engine="gpt-35-turbo-us",
                messages=[
                    {
                        "role": "system",
                        "content": "Given the below text perform the following processing and \
                                generate the final result without any additional descriptive text. \
                                Rephrase text results with what it is popularly known as in the Indian fashion context. \
                                Do not change the text if it is already a popular phrase like dress, clothes, leave is unchanged. Do not change \
                                other attributes like color, age etc."
                        # "content": "Given the below text, translate text to English first.
                        # Then perform the following processing and generate the final result without any additional \
                        # descriptive text: Rephrase text results with what it is also called as in the Indian fashion \
                        # context. Do not change the text if it is already a popular word."
                    },

                    {
                        "role": "user",
                        "content": "rajasthani saree"
                    },
                    {
                        "role": "assistant",
                        "content": "bandhani saree"
                    },
                    {
                        "role": "user",
                        "content": "clothes"
                    },
                    {
                        "role": "assistant",
                        "content": "clothes"
                    },
                    {
                        "role": "user",
                        "content": "baby dress"
                    },
                    {
                        "role": "assistant",
                        "content": "baby dress"
                    },
                    {
                        "role": "user",
                        "content": "dress"
                    },
                    {
                        "role": "assistant",
                        "content": "dress"
                    },
                    {
                        "role": "user",
                        "content": "navari saree"
                    },
                    {
                        "role": "assistant",
                        "content": "marathi saree"
                    },
                    {
                        "role": "user",
                        "content": "dhavani saree"
                    },
                    {
                        "role": "assistant",
                        "content": "half saree"
                    },
                    {
                        "role": "user",
                        "content": "umbrella suit"
                    },
                    {
                        "role": "assistant",
                        "content": "anarkali suit"
                    },
                    {
                        "role": "user",
                        "content": "umbrella kurti"
                    },
                    {
                        "role": "assistant",
                        "content": "anarkali kurti"
                    },
                    {
                        "role": "user",
                        "content": "low neck tshirt for men"
                    },
                    {
                        "role": "assistant",
                        "content": "deep scoop neck"
                    },
                    {
                        "role": "user",
                        "content": "gujarati silk saree"
                    },
                    {
                        "role": "assistant",
                        "content": "kantha silk saree"
                    },
                    {
                        "role": "user",
                        "content": "punjabi suit men"
                    },
                    {
                        "role": "assistant",
                        "content": "pathani suit men"
                    },
                    {
                        "role": "user",
                        "content": "muslim cap"
                    },
                    {
                        "role": "assistant",
                        "content": "prayer cap"
                    },
                    {
                        "role": "user",
                        "content": "long frocks for ladies"
                    },
                    {
                        "role": "assistant",
                        "content": "gown for women"
                    },
                    {
                        "role": "user",
                        "content": "skin colored"
                    },
                    {
                        "role": "assistant",
                        "content": "biege"
                    },
                    {
                        "role": "user",
                        "content": "mens 3 4 shorts jeans"
                    },
                    {
                        "role": "assistant",
                        "content": "mens capri jeans"
                    },
                    {
                        "role": "user",
                        "content": "ground touching dress"
                    },
                    {
                        "role": "assistant",
                        "content": "maxi dress"
                    },
                    {
                        "role": "user",
                        "content": "wrangler scratch jeans for boy kids"
                    },
                    {
                        "role": "assistant",
                        "content": "wrangler distressed jeans for boy kids"
                    },
                    {
                        "role": "user",
                        "content": "men cap t shirt"
                    },
                    {
                        "role": "assistant",
                        "content": "men hoodie"
                    },
                    {
                        "role": "user",
                        "content": "double sided jacket"
                    },
                    {
                        "role": "assistant",
                        "content": "reversible jacket"
                    },
                    {
                        "role": "user",
                        "content": "boys sleeveless jacket"
                    },
                    {
                        "role": "assistant",
                        "content": "waist coat boys"
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                temperature=0.0,
                max_tokens=800,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None)

            # print(response)
            json_res = json.loads(str(response))
            return json_res['choices'][0]['message']['content']
        except Exception as e:
            print("Exception")
            return query

    def expand_query(self, query):
        # query = "0 years baby sweater"
        try:
            response = openai.ChatCompletion.create(
                engine="gpt-35-turbo-us",
                messages=[
                    {
                        "role": "system",
                        "content": "Give detailed product suggestions available in Indian markets. \
                                Do not give options if the input text if specific enough. Do not give brand suggestions. \
                                Just give the names of products in list format and not the definitions. Stay close to facts and do not add imaginary products."},

                    {
                        "role": "user",
                        "content": "summer clothes men"
                    },
                    {
                        "role": "assistant",
                        "content": '["tshirts", "shorts", "hat", "cargo pants"]'
                    },
                    {
                        "role": "user",
                        "content": "winter clothes"
                    },
                    {
                        "role": "assistant",
                        "content": '["shawl", "sweaters", "pullover", "woolen socks"]'
                    },
                    {
                        "role": "user",
                        "content": "lawn mover"
                    },
                    {
                        "role": "assistant",
                        "content": '["lawn mover"]'
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                temperature=0.0,
                max_tokens=800,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None)

            # print(str(response))
            res = json.loads(str(response))
            res1 = res['choices'][0]['message']['content']
            if "sorry" in res1 or "unclear" in res1:
                # print("here")
                return [query]
            # print(res1)
            else:
                return literal_eval(res1)
        except Exception as e:
            print("Exception")
            return [query]

    def process_end_to_end(self, query):
        res1 = self.get_structured_response(query)
        # print("original structured response: {}".format(res1))
        not_added_tokens = {}
        if "<SEP>" in res1:
            split_res = res1.split("<SEP>")
            # print(split_res)
            delim_idx = split_res[1].find('}')
            final_res = split_res[1][:delim_idx + 1]
            # print(final_res)
            final_res = json.loads(final_res)
            print("OUTPUT FOR PHASE 1: {}".format(final_res))
            query_for_stage2 = []
            if 'age' in final_res.keys() and final_res['age'] in ['newborn', 'baby', 'infant']:
                query_for_stage2.append(final_res['age'])
            for k, v in final_res.items():
                # print(k, v)
                if (k != 'gender' and k != 'age' and k != 'color'):
                    query_for_stage2.append(v)
                elif v != 'any' and v != 'adult':
                    not_added_tokens[k] = v
            # print(query_for_stage2)
            query_for_stage2 = " ".join(query_for_stage2)
        else:
            print("OUTPUT FOR PHASE 1: {}".format(query))
            query_for_stage2 = query

        print("INPUT FOR PHASE 2: {}".format(query_for_stage2))
        replaced = self.get_phrase_replacement(query_for_stage2)
        print("OUTPUT FOR PHASE 2: {}".format(replaced))
        print("INPUT FOR PHASE 3: {}".format(replaced))

        # convert age + gender to single token
        age_gender_str = ""
        if ("age" in not_added_tokens) and ("gender" in not_added_tokens):
            age_gender_str = self.convert_age_gender(not_added_tokens['age'], not_added_tokens['gender'])
            del not_added_tokens['age']
            del not_added_tokens['gender']

        if "gender" in not_added_tokens:
            if not_added_tokens['gender'] == "male":
                not_added_tokens['gender'] = "men"
            if not_added_tokens['gender'] == "female":
                not_added_tokens['gender'] = "women"

        expanded_q_list = self.expand_query(replaced)
        print("NOT ADDED TOKENS LIST: {}".format(not_added_tokens.values()))
        not_added_tokens_str = " ".join(not_added_tokens.values())
        expanded_queries = [age_gender_str + " " + not_added_tokens_str + " " + str(q) for q in expanded_q_list]
        print("EXPANDED QUERY LIST: {}".format(expanded_queries))

        if len(not_added_tokens) != 0:
            main_query = age_gender_str + " " + not_added_tokens_str + " (" + " OR ".join(expanded_q_list) + ") "
        else:
            main_query = age_gender_str + " (" + " OR ".join(expanded_q_list) + ")"

        reformulated_query = age_gender_str + " " + not_added_tokens_str + " " + replaced

        return main_query, expanded_queries, reformulated_query

    def convert_age_gender(self, age, gender):
        res = [int(i) for i in age.split() if i.isdigit()]
        age_ = 0
        if len(res) != 0:
            age_ = res[0]
        male_gender = ['male', 'men', 'man', 'boy']
        female_gender = ['female', 'women', 'woman', 'girl']
        if (age_>=18 and gender in male_gender):
            return "men"
        if (age_>=18 and gender in female_gender):
            return "women"
        if age == "baby":
            if gender == "male":
                return "boy"
            if gender == "female":
                return "girl"
            return gender
        if gender == "male":
            gender = "men"
        if gender == "female":
            gender = "women"
        return age + " " + gender
