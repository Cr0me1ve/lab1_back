from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'lab1_front\index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('text', '')
    if data:
        with open('data.txt', 'a') as f:
            f.write(data + '\n')
        return jsonify({}), 200
    return jsonify({}), 400

if __name__ == '__main__':
    app.run(debug=True)
