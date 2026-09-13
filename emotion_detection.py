"""Emotion detection using IBM Watson Natural Language Understanding."""

import json
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions in the provided text using Watson NLP."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=input_json,
        timeout=30
    )

    data = json.loads(response.text)
    emotion = data["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotion, key=emotion.get)

    return {
        "anger": emotion["anger"],
        "disgust": emotion["disgust"],
        "fear": emotion["fear"],
        "joy": emotion["joy"],
        "sadness": emotion["sadness"],
        "dominant_emotion": dominant_emotion
    }
    