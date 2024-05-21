import argparse
from flask import Flask
from flask_cors import CORS
from main.routes.routes import initialize_routes as initialize_main_routes
from test.routes.routes import initialize_routes as initialize_test_routes


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', help='Run this API in test mode.', action='store_true', required=False)

args = parser.parse_args()

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':  
    if not args.test:
        initialize_main_routes(app)
    else:
        initialize_test_routes(app)

    app.run()