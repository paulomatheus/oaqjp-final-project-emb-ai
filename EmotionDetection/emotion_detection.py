import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        return { 'anger': None, 'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None}
    
    if response.status_code != 200:
        return { 'anger': None, 'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None}

    formatted_response = json.loads(response.text)
    if 'emotionPredictions' not in formatted_response or not formatted_response['emotionPredictions']:
        return { 'anger': None, 'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None}
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_emotion = max(emotions_dict, key = emotions_dict.get)
    emotions_dict['dominant_emotion'] = dominant_emotion

    return emotions_dict