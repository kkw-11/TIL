from flask import Flask

app = Flask(__name__)

@app.route("/<data>")
def hello(data):
    return "hello" + data

app.run(port=3000)

