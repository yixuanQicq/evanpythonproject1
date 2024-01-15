from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<body><p>hi</p><p style='color:red;'>hello</p><p style='color:blue;'>hello again</p><p style='font-size:50px;'>NICE TO MEET YOU</p></body>"