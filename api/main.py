import google.generativeai as genai
from flask import Flask, request, jsonify
import PIL.Image
import io
from flask_cors import CORS
from openai import OpenAI

client = OpenAI(api_key="credenciais")


app = Flask(__name__)
CORS(app)
genai.configure(api_key="credenciais")


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/analisar_codigo', methods=['POST'])
def gerar_resposta():
    dados = request.get_json()

    if 'code' not in dados or not isinstance(dados['code'], str):
        return jsonify({'erro': 'Por favor, forneça uma chave "pergunta" válida como uma string.'}), 400

    code = dados['code']
    prompt = dados['prompt']

    try:
        modelo = genai.GenerativeModel('gemini-pro')

        response = modelo.generate_content(prompt + code)

        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'erro': f"Ocorreu um erro ao processar a solicitação: {str(e)}"}), 500

@app.route('/chat', methods=['POST'])
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

@app.route('/gerar_imagem', methods=['POST'])
def gerar_imagem():
    try:
        uploaded_file = request.files['image']
        uploaded_text = request.form['text']
        img = PIL.Image.open(uploaded_file)

        image_bytes = io.BytesIO()
        img.save(image_bytes, format='PNG')  # Altere o formato conforme necessário
        image_bytes.seek(0)

        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([uploaded_text, img])
        response.resolve()
        return jsonify({'response': response.text})

    except Exception as e:
        return jsonify({'error': f"Ocorreu um erro ao processar a solicitação: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)