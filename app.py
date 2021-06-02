from chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText = str(userText).lower()
    if str(chatbot.get_response(userText)).__contains__("The current time is "):
        return "Sorry I am unable to process you request can you more specific or if it help check out link share above"
    else:
        return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run() 