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

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "menu":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Please type "install" "uninstall"'))
			
    elif event.message.text == "install":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose product "install trend micro" "install symantec" "install vse8.8" "install ens10"'))  
			
	elif event.message.text == "uninstall":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose product "uninstall trend micro" "uninstall symantec" "uninstall vse8.8" "uninstall ens10"')) 
			
	elif event.message.text == "install trend micro":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content1')) 
			
    elif event.message.text == "uninstall trend micro":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content2')) 
			
    elif event.message.text == "install symantec":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content3'))  

    elif event.message.text == "uninstall symantec":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content4'))  
			
    elif event.message.text == "install vse8.8":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content5'))  
			
    elif event.message.text == "uninstall vse8.8":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content6')) 
			
    elif event.message.text == "install ens10":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content7')) 
			
    elif event.message.text == "uninstall ens10":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='content8')) 
			
    else line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='dont understand please type "menu"'))   
			


if __name__ == "__main__":
    app.run()
