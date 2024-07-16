import time
import requests
import os
import json


def text_to_speech(text):
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTQ1ZjJjN2MtY2E1Yi00ZTk5LWEyZTUtOTJkNzY4MDRlYjE5IiwidHlwZSI6ImFwaV90b2tlbiJ9.8CC7FMq-Gr8Uw8e7T14rQOwxeRxakDhTTZtRh9wVpIs"}
    url = "https://api.edenai.run/v2/audio/text_to_speech"

    payload = {
        "providers": "openai",
        "language": "ru",
        "option": "FEMALE",
        "openai": "ru_shimmer",
        "text": f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result =json.loads(response.text)
    unx_time = int(time.time())

    with open(f'{unx_time}.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    
    #audio_url = result.get('lovoai').get('audio_resource_url')


def main():
    text_to_speech(text = "В современном мире технологий, искусственный интеллект продолжает продвигаться вперед, открывая новые возможности для улучшения жизни людей.")


if __name__ == '__main__':
    main()