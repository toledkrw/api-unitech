from flask import request, jsonify, Blueprint

import google.generativeai as genai
import io, PIL.Image


gemini_bp = Blueprint('geminiAI', __name__)
MAIN_ROUTE = '/gmni'

genai.configure(api_key="credenciais")


@gemini_bp.route(MAIN_ROUTE + '/analisar_codigo', methods=['POST'])
def gerar_resposta():
    dados = request.get_json()

    if 'code' not in dados or not isinstance(dados['code'], str):
        return jsonify({'erro': 'Por favor, forneça uma chave "pergunta" válida como uma string.'}), 400

    code = dados['code']
    prompt = dados['prompt']

    try:
        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_content(prompt + code)

        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'erro': f"Ocorreu um erro ao processar a solicitação: {str(e)}"}), 500
    
@gemini_bp.route(MAIN_ROUTE + '/gerar_imagem', methods=['POST'])
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
