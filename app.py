import os
from flask import Flask, jsonify
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
DATABASE_PATH = os.getenv('DATABASE_PATH', 'app.db')
@app.get('/health')
def health(): return jsonify(status='ok')
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
