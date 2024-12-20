from flask import Flask, request, jsonify, send_from_directory, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('../lab1_front/index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('text', '')
    if data:
        with open('lab1_back\data.txt', 'a') as f:
            f.write(data + '\n')
        return jsonify({}), 200
    return jsonify({}), 400

@app.route('/get_info', methods=['GET'])
def get_info():
    with open('lab1_back\data.txt', 'r') as f:
        data = f.read()
    return jsonify({'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)
