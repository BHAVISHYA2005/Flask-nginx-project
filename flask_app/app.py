from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(1)  # Simulate delay to show caching
    return {"message": "Welcome to DevOps!", "timestamp": time.ctime()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)