from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    print(request)
    data = request.json.get('text', '')
    if data:
        with open('lab1_back/data.txt', 'a') as f:  # Use forward slashes for paths
            f.write(data + '\n')
        return jsonify({}), 200
    return jsonify({}), 400

@app.route('/get_info', methods=['GET'])
def get_info():
    if os.path.exists('lab1_back/data.txt'):
        with open('lab1_back/data.txt', 'r') as f:
            data = f.read()
        return jsonify({'data': data}), 200
    return jsonify({'data': ''}), 200  # Return empty data if file doesn't exist

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)