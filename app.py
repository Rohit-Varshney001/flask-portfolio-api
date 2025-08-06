from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_parser.parser import parse_pdf_resume, parse_docx_resume
import os
from translation.translator import mock_translate
from currency.converter import convert_price


app = Flask(__name__)
CORS(app)

@app.route('/api/parse-resume', methods=['POST'])
def parse_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'Resume file is required'}), 400
    
    resume = request.files['resume']
    filename = resume.filename

    if filename.endswith('.pdf'):
        data = parse_pdf_resume(resume)
    elif filename.endswith('.docx'):
        data = parse_docx_resume(resume)
    else:
        return jsonify({'error': 'Unsupported file format'}), 400

    return jsonify(data)

@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.get_json()
    if not data or 'content' not in data or 'lang' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    content = data['content']
    lang = data['lang']
    translated = mock_translate(content, lang)
    return jsonify(translated)

@app.route('/api/get-price', methods=['GET'])
def get_price():
    base_price = 1000  # INR as base
    country = request.args.get('country', 'IN')
    local_price = convert_price(base_price, country)
    return jsonify({
        'base_price_INR': base_price,
        'local_price': local_price,
        'currency': country
    })
    
@app.route('/')
def index():
    return 'Flask API is running! Use endpoints like /api/parse-resume'

if __name__ == '__main__':
    app.run(debug=True)
