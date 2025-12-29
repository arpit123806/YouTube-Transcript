from flask import Flask
from src.routes import lang_chain
from flask_cors import CORS
app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})
# app.register_blueprint(rag, url_prefix='/api/v1')

# @app.route('/',methods=['GET'])
# def home_page():
#     return "Its working"

    
if __name__ == '__main__':
    # app.run(host='0.0.0.0',debug=True)
    lang_chain()