from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import * #(MessageEvent, TextMessage, TextSendMessage,)
from usbcheck import usbc

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
    profile = line_bot_api.get_profile(event.source.user_id)
    #group_id=Ca1eed6eefec9ccb0382b34c99b7594a0
    #group = line_bot_api.get_group_member_profile(group_id, user_id)
    #groupid = event.source.group_id
    textinput = event.message.text
    inputc = event.message.text.lower()
    inputarr = textinput.split(' ')
    stop = 0
    j = 0
    file = open('ListUseUSB.txt')
    for word in file:
        name = word.split('	')
        LastArray =  len(name) - 1
    while j <= LastArray:
        if inputarr[0].lower() == name[j].lower():
            j = LastArray
            stop = 1
            result = 1
        else:
            j += 1
    if stop == 0 :
        result = 0
  #  return result
    if result == 1:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Use USB and CD-ROM'))
			
 #   if (inputarr[0] == "usb") or (inputarr[0] == "Usb"):
#        line_bot_api.reply_message(
 #           event.reply_token,
  #          TextSendMessage(text='USB TEST'))
    #      usbusername = inputarr[1]
  #      usbresult = usbc(inputarr[1])
  #      usbc(usbusername)
   #     line_bot_api.reply_message(
   #         event.reply_token,
#	    TextSendMessage(usbresult))	
	
    elif (inputc == "menu"):
	#or (event.message.text == "Menu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Please type \n "install" \n "uninstall" \n ต้องการทราบสิทธิในการใช้ USB พิมพ์ชื่อผู้ใช้งาน เช่น abc.d หรือ computer name หรือ IP'))
			
    elif (inputc == "install"): 
	#or (event.message.text == "Install"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose product \n "install trend micro" \n "install symantec" \n "install vse8.8" \n "install ens10"'))  
    
    elif (inputc == "uninstall"):
		#or (event.message.text == "Uninstall"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose product \n "uninstall trend micro" \n "uninstall symantec" \n "uninstall vse8.8" \n "uninstall ens10"')) 
			
    elif (inputc == "install trend micro"):
	#or (event.message.text == "Install trend micro"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/6ycymsztz9k0l44/Trend_Micro_Server_Protect_Install_Manual.pdf/file')) 
			
    elif (inputc == "uninstall trend micro"):
	#or (event.message.text == "Uninstall trend micro"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/b8j1oegd6e25b73/Trend_Micro_Server_Protect_Uninstall_Manual.pdf/file')) 
			
    elif (inputc == "install symantec"): 
	#or (event.message.text == "Install symantec"):
      #  profile = line_bot_api.get_profile(event.source.user_id)
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/3ftXd6c.jpg',
	    preview_image_url='https://imgur.com/Wg4Shju.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/c92MnU7.jpg',
	    preview_image_url='https://imgur.com/54x4ero.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/w6Zfdgw.jpg',
	    preview_image_url='https://imgur.com/M0u2HS3.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/LdBek5A.jpg',
	    preview_image_url='https://imgur.com/lyADnLn.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/v0xUU9P.jpg',
	    preview_image_url='https://imgur.com/HsMf8a5.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/kCFVwdd.jpg',
	    preview_image_url='https://imgur.com/Q9DzQiZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/BJ8zJAC.jpg',
	    preview_image_url='https://imgur.com/XYKjunB.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/auT1CVa.jpg',
	    preview_image_url='https://imgur.com/XYxDUnxB.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/uEQFBHx.jpg',
	    preview_image_url='https://imgur.com/KqmQucB.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/WvEQLNV.jpg',
	    preview_image_url='https://imgur.com/7I3fuiQ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/aXU2brW.jpg',
	    preview_image_url='https://imgur.com/OWI6viZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/dT2CSmQ.jpg',
	    preview_image_url='https://imgur.com/B3pFR6A.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "uninstall symantec"):
	#or (event.message.text == "Uninstall symantec"):
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/ONZGYe5.jpg',
	    preview_image_url='https://imgur.com/MkHtf99.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/i8YlhT0.jpg',
	    preview_image_url='https://imgur.com/OSzxIWs.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/RAujq9C.jpg',
	    preview_image_url='https://imgur.com/RAujq9C.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/J22RJWY.jpg',
	    preview_image_url='https://imgur.com/J22RJWY.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/siiLhhT.jpg',
	    preview_image_url='https://imgur.com/siiLhhT.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/jsphX5M.jpg',
	    preview_image_url='https://imgur.com/jsphX5M.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/4kQn5F7.jpg',
	    preview_image_url='https://imgur.com/4kQn5F7.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/8IQe6mM.jpg',
	    preview_image_url='https://imgur.com/8IQe6mM.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/DmvFCIJ.jpg',
	    preview_image_url='https://imgur.com/DmvFCIJ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
    elif (inputc == "install vse8.8"):
	#or (event.message.text == "Install vse8.8"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/jrbv2bkjf187dbm/McAfee_VirusScan_Enterprise8.8_Install_Manual_for_WinXP.pdf/file'))  
			
    elif (inputc == "uninstall vse8.8"):
	#or (event.message.text == "Uninstall vse8.8"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='http://www.mediafire.com/file/s6ha4ovai2vvscx/McAfee_VirusScan_Enterprise8.8_Uninstall_Manual_for_WinXP.pdf/file')) 
			
    elif (inputc == "install ens10"): 
	#or (event.message.text == "Install ens10"):
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/WBr1TGj.jpg',
	    preview_image_url='https://imgur.com/WBr1TGj.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/GvgT8LQ.jpg',
	    preview_image_url='https://imgur.com/GvgT8LQ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/utkMSES.jpg',
	    preview_image_url='https://imgur.com/utkMSES.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/P9F3DVr.jpg',
	    preview_image_url='https://imgur.com/P9F3DVr.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/UdG5CaW.jpg',
	    preview_image_url='https://imgur.com/UdG5CaW.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/fJhqnwj.jpg',
	    preview_image_url='https://imgur.com/fJhqnwj.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/uvhvWDx.jpg',
	    preview_image_url='https://imgur.com/uvhvWDx.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/wNaFYAM.jpg',
	    preview_image_url='https://imgur.com/wNaFYAM.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/wAmqVHa.jpg',
	    preview_image_url='https://imgur.com/wAmqVHa.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/kN87Ybn.jpg',
	    preview_image_url='https://imgur.com/kN87Ybn.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/U64Y6aa.jpg',
	    preview_image_url='https://imgur.com/U64Y6aa.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/6K3Z1r9.jpg',
	    preview_image_url='https://imgur.com/6K3Z1r9.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "uninstall ens10"):
	#or (event.message.text == "Uninstall ens10"):
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/ynsasNL.jpg',
	    preview_image_url='https://imgur.com/ynsasNL.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/9R09HwZ.jpg',
	    preview_image_url='https://imgur.com/9R09HwZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/OV3qfRx.jpg',
	    preview_image_url='https://imgur.com/OV3qfRx.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/Mqxq9Pk.jpg',
	    preview_image_url='https://imgur.com/Mqxq9Pk.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/U2ZBazn.jpg',
	    preview_image_url='https://imgur.com/U2ZBazn.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/5UvZvjZ.jpg',
	    preview_image_url='https://imgur.com/5UvZvjZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/jUqDyRc.jpg',
	    preview_image_url='https://imgur.com/jUqDyRc.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (event.message.text == "ข้าวเที่ยง"):
        image_message = ImageSendMessage(
            original_content_url='https://imgur.com/4D77SCC.jpg',
	    preview_image_url='https://imgur.com/hjKN0at.jpg')
        line_bot_api.reply_message(
            event.reply_token,image_message
            ) 
	
    elif (inputc == "groupid"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(event.source.group_id)) 
	
    elif (inputarr[0].lower() == "de"):
        logfile = open('log.txt')
        profile = line_bot_api.get_profile(event.source.userid)
        logtxt = profile.user_id + ',' + profile.display_name + ',' + inputarr[0] + ',' + inputarr[1] + ',' + inputarr[2] + ',' + inputarr[3] + ',' + inputarr[4] + '\n'
        logfile.write(logtxt)
        logfile.close()
        DEmsg = 'Drive Encryption XML File request' + '\n' + 'Computer Name : ' + inputarr[1].upper() + '\n' + 'Send to : ' + inputarr[2] + '\n' + 'Tel. : ' + inputarr[3] + '\n' + 'Remark : ' + inputarr[4]
	#+'\n' inputarr[4]
        line_bot_api.push_message(
            'Ua6751e3b8340b1b849c4826ad27ddcdd',
            TextSendMessage(DEmsg)) 
	
    else:
        if (event.source.type != 'group'):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='ไม่มีสิทธิในการใช้งาน USB หรือถ้าไม่ใช่สิ่งที่ค้นหา กรุณาพิมพ์ "menu"'))   
        else:
            exit()
			


if __name__ == "__main__":
    app.run()
