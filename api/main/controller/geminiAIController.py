from flask import request, jsonify, Blueprint

import google.generativeai as genai
import os


gemini_bp = Blueprint('geminiAI', __name__)
MAIN_ROUTE = '/gmni'

genai.configure(api_key=os.environ['GEMINI_KEY'])


@gemini_bp.route(MAIN_ROUTE + '/multiple_choice_question', methods=['POST'])
def generate_multiple_choice_question():
    data = request.get_json()

    try:
        if 'subject' not in data:
            raise ValueError('"Subject was not given".')
        if 'academic_level' not in data:
            raise ValueError('"Academic level was not given".')
        if 'theme' not in data:
            raise ValueError('"Theme was not given".')
        
        subject = data['subject']
        academic_level = data['academic_level']
        theme = data['theme']

        locale = 'pt-br' if 'locale' not in data else data['locale']

        prompt=\
            f"Generate a test question, with five options (A, B, C, D, E), about the subject of {subject} at the {academic_level} level, focusing on {theme} theme." + \
            "Please provide your response in Json format with the following structure: " + \
            "{question_statement:'question statement that you will generate', alternatives:[{a:'option'}, {b:'option'}, {c:'option'}, {d:'option'}, {e:'option'}]], correct_answer:'correct_option_letter'}" + \
            f"The question statement and alternatives must be in the following language: {locale}."
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)

        return jsonify({'response': response.text})
    except ValueError as e:
        return jsonify({'Error! ': f"An Error ocurred while processing your request: {str(e)}"}), 400
    except Exception as e:
        return jsonify({'Error! ': f"An Error ocurred while processing your request: {str(e)}"}), 500
