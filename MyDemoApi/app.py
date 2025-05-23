from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your Flask API!"})

@app.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
