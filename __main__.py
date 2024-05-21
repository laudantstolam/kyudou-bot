from flask import Flask, request, abort

from linebot.v3 import WebhookHandler
# from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration

from dotenv import load_dotenv
import os

app = Flask(__name__)

# load .env
if os.path.isfile('.env'):
    load_dotenv()
    configuration = Configuration(access_token='ACCESS_TOKEN')
    handler = WebhookHandler('CHANNEL_SECRET')
else:
    print("Create your .env file to store data.")

# import route and API call back
import api.callback
import message.textMessage





if __name__ == "__main__":
    app.run()