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
    textinput = event.message.text
    inputarr = textinput.split(' ')
    if (event.message.text == "usb test"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(textarr[0])
    elif (event.message.text == "menu") or (event.message.text == "Menu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Please type \n "install" \n "uninstall"'))
			
    elif (event.message.text == "install") or (event.message.text == "Install"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose product \n "install trend micro" \n "install symantec" \n "install vse8.8" \n "install ens10"'))  
    
    elif (event.message.text == "uninstall") or (event.message.text == "Uninstall"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose product \n "uninstall trend micro" \n "uninstall symantec" \n "uninstall vse8.8" \n "uninstall ens10"')) 
			
    elif (event.message.text == "install trend micro") or (event.message.text == "Install trend micro"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/6ycymsztz9k0l44/Trend_Micro_Server_Protect_Install_Manual.pdf/file')) 
			
    elif (event.message.text == "uninstall trend micro") or (event.message.text == "Uninstall trend micro"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/b8j1oegd6e25b73/Trend_Micro_Server_Protect_Uninstall_Manual.pdf/file')) 
			
    elif (event.message.text == "install symantec") or (event.message.text == "Install symantec"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/bxx2npxsoks5voi/Symantec_Endpoint_Protection_Install_Manual_for_WinXP-7.pdf/file'))  

    elif (event.message.text == "uninstall symantec") or (event.message.text == "Uninstall symantec"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/7hhpt6ujfpbwhaz/Symantec_Endpoint_Protection_Uninstall_Manual_for_WinXP-7.pdf/file'))  
			
    elif (event.message.text == "install vse8.8") or (event.message.text == "Install vse8.8"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/jrbv2bkjf187dbm/McAfee_VirusScan_Enterprise8.8_Install_Manual_for_WinXP.pdf/file'))  
			
    elif (event.message.text == "uninstall vse8.8") or (event.message.text == "Uninstall vse8.8"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/s6ha4ovai2vvscx/McAfee_VirusScan_Enterprise8.8_Uninstall_Manual_for_WinXP.pdf/file')) 
			
    elif (event.message.text == "install ens10") or (event.message.text == "Install ens10"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/fdbq3d3wwkby9tt/McAfee_Endpoint_Security_Install_Manual_for_Win_7.pdf/file')) 
			
    elif (event.message.text == "uninstall ens10") or (event.message.text == "Uninstall ens10"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/ohb1h1e9g3jfbm5/McAfee_Endpoint_Security_Uninstall_Manual_for_Win_7.pdf/file')) 
			
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='dont understand please type "menu"'))   
			


if __name__ == "__main__":
    app.run()
