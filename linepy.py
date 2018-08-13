from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('1WpfHfGGfcQ1fxfaEXVP4vx1IfhiUY6fZ/fXVERnTlYx3zaFklj8aECTNrU1D4iy3+MebJXlGYSuLU/93oJn4NNCN9GsSv9invPyphDycXQvzr2lHNUxWeqUBvK/MxJULr3XLGDH6BhHrjgaTinVMwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c87a65d916b043abe432e4eed6d689e2')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
     # get X-Line-Signature header value
  #   signature = request.headers['X-Line-Signature']

     # get request body as text
 #    body = request.get_data(as_text=True)
  #   app.logger.info("Request body: " + body)

    # handle webhook body
 #   try:
 #       handler.handle(body, signature)
 #   except InvalidSignatureError:
 #       abort(400)
    if request.method == 'POST':

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
