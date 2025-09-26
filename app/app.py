from flask import Flask, jsonify
app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def hello():
    return jsonify({'message': 'Hello from CI app'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
