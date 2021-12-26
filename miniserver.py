from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello Service Management 2021. My name is Matthew Igbinehi'

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=20221)