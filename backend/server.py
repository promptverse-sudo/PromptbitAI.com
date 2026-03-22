# Backend Server

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/example', methods=['GET'])
def example():
    return jsonify({'message': 'Hello World'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)