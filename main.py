from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'deu certo'

@app.route('/numero')
def numero():
    return str(random.randint(1, 10))
#teste
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)