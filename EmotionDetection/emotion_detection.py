import requests
import json

def emotions_detector(text_to_analyze):   
    #URL of the emotion detection service
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   
    # Custom header specifying the model ID for the emotion detector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #Constructing the request payload in the expected format
    payload = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion service
    response = requests.post(url, json=payload, headers=header)


    # Checking if the response is successful
    if response.status_code == 200:
        # Parsing the response
        response_data = response.json()
        
        # Extrating the emotion scores
        emotions = response_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        # Formating result
        result = {'anger': emotions['anger'],'disgust': emotions['disgust'],'fear': emotions['fear'],'joy': emotions['joy'],'sadness': emotions['sadness'],'dominant_emotion': dominant_emotion}
        return result 
    else:
        # Handling errors and returning the response code and text
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }


