from flask import Flask, request, jsonify, make_response
import PyPDF2
import os
from flask_cors import CORS
# import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

import csv

app = Flask(__name__)
# Enable CORS for all routes with support for credentials and preflight
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)  # Updated to PdfReader
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()  # Updated method name
    return text


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/extract-text', methods=['POST', 'OPTIONS'])
def extract_text():
    print("Here")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    _, file_ext = os.path.splitext(file.filename)
    if file_ext.lower() != '.pdf':
        return jsonify({'error': 'Unsupported file format. Only PDF files are supported.'}), 400

    try:
        text = extract_text_from_pdf(file)
        print(text)
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_csv', methods=['POST'])
def generate_csv():
    data = request.json  # Assuming data is sent as JSON from the client
    if not data:
        return jsonify({'message': 'No data received'}), 400
    
    # Generate CSV file
    csv_data = []
    for item in data:
        csv_data.append({'question': item['question'], 'answer': item['answer']})

    # Create CSV file
    filename = 'data.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['question', 'answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in csv_data:
            writer.writerow(item)

    # Send the CSV file to the client
    response = make_response(open(filename, 'r').read())
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response

if __name__ == '__main__':
    # print(os.getenv("FLASK_RUN_HOST"))
    app.run(host=os.getenv("FLASK_RUN_HOST"), port=os.getenv("PORT") ,debug=True)
