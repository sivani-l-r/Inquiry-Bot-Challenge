import time
time.clock = time.time
import collections.abc
collections.Hashable = collections.abc.Hashable

from flask import Flask, render_template, request, trainingdata

app = Flask(__name__)

# Your ChatBot configuration
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatBot = ChatBot('AICSSYC Chat Bot')
training_data = trainingdata.data
trainer = ListTrainer(chatBot)
trainer.train(training_data)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = chatBot.get_response(userText)

    if response.confidence <= 0.9 and response.confidence >=0.8 :
        fallback_response = "Can you please elaborate further? I'm here to assist, but I need more details to provide a precise response. Feel free to provide more context or specific questions, and I'll do my best to assist you."
        return fallback_response
    elif response.confidence <= 0.8 and response.confidence >=0.7:
        second_response ="I apologize, but I couldn't find the answer to your question. For more information and details about AICSSYC, please visit our official website at https://aicssyc.org/."
        return second_response
    else:
        return str(response)


