from flask import request, jsonify, Blueprint
from openai import OpenAI
import os

MAIN_ROUTE = '/opai'
CURRENT_MODEL = 'gpt-3.5-turbo-0125'

openai_bp = Blueprint('openAI', __name__)

client = OpenAI(api_key=os.environ['OPENAI_KEY'])


@openai_bp.route(MAIN_ROUTE + '/chat', methods=['POST'])
def chat():
    pass