import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_json = json.loads(response.text)
    label = formatted_json['documentSentiment']['label']
    score = formatted_json['documentSentiment']['score']
    return {'label':label, 'score':score}

# result_1 = sentiment_analyzer('I love working with Python')
# print(result_1['label'], 'SENT_POSITIVE')
# result_2 = sentiment_analyzer('I hate working with Python')
# print(result_2['label'], 'SENT_NEGATIVE')
# result_3 = sentiment_analyzer('I am neutral on Python')
# print(result_3['label'], 'SENT_NEUTRAL')
