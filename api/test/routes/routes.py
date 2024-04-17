from ..controller.helloWorldController import test_bp

def initialize_routes(app):
    app.register_blueprint(test_bp)
    pass
