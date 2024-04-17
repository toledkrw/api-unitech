from ..controller.geminiAIController import gemini_bp
from ..controller.openAIController import openai_bp

def initialize_routes(app):
    app.register_blueprint(gemini_bp)
    app.register_blueprint(openai_bp)
    pass
