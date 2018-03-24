from flask import Flask
from rapper.generate_song import sing
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/rap")
def rap():
    return sing()

if __name__ == "__main__":
    app.run()
