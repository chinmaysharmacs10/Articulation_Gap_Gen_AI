# Solving Articulation Gap using Generative AI

**Exploring the use cases of Large Language Models (LLMs) in search systems!**

* On e-commerce platforms, when users do not know the exact/catalog correct term for an item, they will use other related terms to describe what they require. 
These search queries are known as “Articulation Gap (AG)" queries.
* In a lexial index based retrieval system, AG queries result in low or irrelevant recall. This leads to bad customer experience and has an adverse effect on the business.
* We leverage the power of Large Language Model (**ChatGPT-3.5 Turbo**) to address the above problem.
* Our approach can be broken down into three stages. Each stage uses a separate prompt for its specified task:
  1. <ins>Attribute tagging</ins>: Identifying which token(s) map to which attribute, similar to Named Entity Recognition (NER). 
Example -> input: "0 year clothes winter", output: {"product": "winter clothes", "age":"newborn", "gender":"any"}
  2. <ins>Phrase replacement</ins>: Replacing AG affected attributes with catalog standard vocabulary. 
Example -> newborn is replaced with infant to reformulate the query to "infant winter clothes"
  3. <ins>Query expansion</ins>: Expanding the query by replacing the generic category in the query with specific verticals of that category. 
Example -> infant (onesies OR sleepsuits OR sweaters OR jackets)
* The expanded query is then used for retrieval from the search index, leading to higher and revelant recall.

## These slides will help you understand the details!
<img width="1342" alt="ag_gen_ai_1" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/ebe36145-d352-496b-9348-1be399718905">
<img width="1340" alt="ag_gen_ai_2" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/cca7be1c-b833-4c3e-b418-6a5e0dd36d5e">
<img width="1341" alt="ag_gen_ai_3" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/3e9a46b2-cdd5-4e8c-88c4-c49c31d52d1c">

## Checkout these examples!
In the below images, the left pane is [Flipkart](https://www.linkedin.com/company/flipkart/) (India's leading e-commerce platform) and the right pane is our web application.

<img width="1339" alt="ag_gen_ai_4" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/bd120404-5d5a-4649-85f5-2e43634e6d64">
<img width="1340" alt="ag_gen_ai_5" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/7c523122-7bee-4469-8918-3a5d58b67311">
<img width="1340" alt="ag_gen_ai_6" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/a2609c83-9900-4960-a405-c132c43c8779">
<img width="1339" alt="ag_gen_ai_7" src="https://github.com/chinmaysharmacs10/Articulation_Gap_Gen_AI/assets/35448762/e75465fd-3a0b-496f-bde3-655a20cb5cb4">
