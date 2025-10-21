import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the value from the environment variable set via ConfigMap
    message = os.environ.get("MESSAGE", "Hello, World!")
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

