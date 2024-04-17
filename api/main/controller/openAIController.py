from flask import request, jsonify, Blueprint

from openai import OpenAI


openai_bp = Blueprint('openAI', __name__)
MAIN_ROUTE = '/opai'

client = OpenAI(api_key="credenciais")


@openai_bp.route(MAIN_ROUTE + '/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system",
                 "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": user_message},
            ]
        )

        return jsonify({'response': response.choices[0].message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500