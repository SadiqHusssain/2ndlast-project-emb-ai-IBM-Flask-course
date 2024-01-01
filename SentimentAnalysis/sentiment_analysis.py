"""A simple sentiment analysis scipt that takes text as an input
and analyze the text by using Watson Ai NLP library"""
import json
import requests


def sentiment_analyzer(text_to_analyse):
    """the function that takes input text and return 
       the analyzed result based on that text"""
    url = ("https://sn-watson-sentiment-bert.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict")
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id":
    "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
    elif response.status_code == 500:
        label = None
        score = None
    return {"label": label, "score": score}

# result_1 = sentiment_analyzer('I love working with Python')
# print(result_1['label'], 'SENT_POSITIVE')
# result_2 = sentiment_analyzer('I hate working with Python')
# print(result_2['label'], 'SENT_NEGATIVE')
# result_3 = sentiment_analyzer('I am neutral on Python')
# print(result_3['label'], 'SENT_NEUTRAL')
