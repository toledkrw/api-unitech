import argparse
from flask import Flask
from flask_cors import CORS

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', help='Run this API in test mode.', action='store_true', required=False)

args, unknown = parser.parse_known_args()

app = Flask(__name__)
CORS(app)

if __name__ in ['__main__', 'app']:  
    if not args.test:
        from main.routes.routes import initialize_routes as initialize_main_routes
        initialize_main_routes(app)
    else:
        from test.routes.routes import initialize_routes as initialize_test_routes
        initialize_test_routes(app)

    app.run(port=5000)