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
  #  inputarrt = textinput.split('	')

  #  rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
 #   print(rich_menu.rich_menu_id)

 #   rich_menu_to_create = RichMenu(
 #   size=RichMenuSize(width=2500, height=843),
 #   selected=False,
 #   name="menu2",
 #   chat_bar_text="Tap here",
#    areas=[RichMenuArea(
#        bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#        action=URIAction(label='Go to line.me', uri='https://line.me'))]
#    )
#    rich2 = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
#    print(rich2)
	   
    stop = 0
    j = 0
    #file = open('ListUseUSB.txt')
    line = open('ListUseUSB.txt').read().split('\n')
    LastArray =  len(line) - 1
    #for word in file:
     #   name = word.split('	')
      #  LastArray =  len(name) - 1
    while j <= LastArray:
      #  if inputarr[0].lower() == name[j].lower():
        if inputarr[0].lower() == line[j].lower():
            j = LastArray
            stop = 1
            result = 1
        else:
            j += 1
    if stop == 0 :
        result = 0
  #  return result
 #   if result == 1:
  #      line_bot_api.reply_message(
   #         event.reply_token,
    #        TextSendMessage(text='Use USB and CD-ROM'))
    stop2 = 0
    k = 0
 #   MDMName = inputarr[0] + ' ' + inputarr[1]
	
    line2 = open('MDMList.txt').read().split('\n')
    LastArray =  len(line2) - 1
    while k <= LastArray:
  #      if (MAMName.lower() == line2[k].lower()) or (inputarr[0] == line2[k].lower()) :
        if inputc == line2[k].lower():
            k = LastArray
            stop2 = 1
            result2 = 1
        else:
            k += 1
    if stop2 == 0 :
        result2 = 0

    if (result == 1) and (result2 == 1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='มีสิทธิการใช้งาน USB และ CD-ROM \n มีสิทธิการใช้งาน MDM '))		
			
    elif (result == 0) and (result2 == 1):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ไม่มีสิทธิใช้งาน USB \n มีสิทธิการใช้งาน MDM'))	
			
    elif (result == 1) and (result2 == 0):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='มีสิทธิการใช้งาน USB และ CD-ROM \n ไม่มีสิทธิการใช้งาน MDM'))	
			
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
 #   elif (inputc == "page2"):
	#or (event.message.text == "Menu"):
#        line_bot_api.link_rich_menu_to_user(user_id, rich2)
	  
    elif (inputc == "menu"):
	#or (event.message.text == "Menu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Please type \n "install" \n "uninstall" \n "drive encryption" \n ตรวจสอบสิทธิการใช้ USB และ MDM พิมพ์ Username เช่น user.n หรือ Computer Name หรือ IP' ))
			
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
	
    elif (inputc == "drive encryption"):
		#or (event.message.text == "Uninstall"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='please chose topic you want to know \n "ePO deployment" \n "EETECH" \n "status check"')) 

	
    elif (inputc == "install trend micro"):
	#or (event.message.text == "Install trend micro"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/gsBuQkD.jpg',
	    preview_image_url='https://i.imgur.com/gsBuQkD.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/mLMZiO2.jpg',
	    preview_image_url='https://i.imgur.com/mLMZiO2.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/0fbQ1gs.jpg',
	    preview_image_url='https://i.imgur.com/0fbQ1gs.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/FnaEGQc.jpg',
	    preview_image_url='https://i.imgur.com/FnaEGQc.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/JEpJBv4.jpg',
	    preview_image_url='https://i.imgur.com/JEpJBv4.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "uninstall trend micro"):
	#or (event.message.text == "Uninstall trend micro"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/wwnJ397.jpg',
	    preview_image_url='https://i.imgur.com/wwnJ397.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/OR62GHF.jpg',
	    preview_image_url='https://i.imgur.com/OR62GHF.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "install symantec"): 
	#or (event.message.text == "Install symantec"):
      #  profile = line_bot_api.get_profile(event.source.user_id)
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/3ftXd6c.jpg',
	    preview_image_url='https://i.imgur.com/Wg4Shju.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/c92MnU7.jpg',
	    preview_image_url='https://i.imgur.com/54x4ero.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/w6Zfdgw.jpg',
	    preview_image_url='https://i.imgur.com/M0u2HS3.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/LdBek5A.jpg',
	    preview_image_url='https://i.imgur.com/lyADnLn.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/v0xUU9P.jpg',
	    preview_image_url='https://i.imgur.com/HsMf8a5.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/kCFVwdd.jpg',
	    preview_image_url='https://i.imgur.com/Q9DzQiZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/BJ8zJAC.jpg',
	    preview_image_url='https://i.imgur.com/XYKjunB.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/auT1CVa.jpg',
	    preview_image_url='https://i.imgur.com/auT1CVa.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/uEQFBHx.jpg',
	    preview_image_url='https://i.imgur.com/KqmQucB.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/WvEQLNV.jpg',
	    preview_image_url='https://i.imgur.com/7I3fuiQ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/aXU2brW.jpg',
	    preview_image_url='https://i.imgur.com/OWI6viZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/dT2CSmQ.jpg',
	    preview_image_url='https://i.imgur.com/B3pFR6A.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "uninstall symantec"):
	#or (event.message.text == "Uninstall symantec"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ONZGYe5.jpg',
	    preview_image_url='https://i.imgur.com/MkHtf99.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/i8YlhT0.jpg',
	    preview_image_url='https://i.imgur.com/OSzxIWs.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/RAujq9C.jpg',
	    preview_image_url='https://i.imgur.com/RAujq9C.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/J22RJWY.jpg',
	    preview_image_url='https://i.imgur.com/J22RJWY.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/siiLhhT.jpg',
	    preview_image_url='https://i.imgur.com/siiLhhT.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/jsphX5M.jpg',
	    preview_image_url='https://i.imgur.com/jsphX5M.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/4kQn5F7.jpg',
	    preview_image_url='https://i.imgur.com/4kQn5F7.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/8IQe6mM.jpg',
	    preview_image_url='https://i.imgur.com/8IQe6mM.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/DmvFCIJ.jpg',
	    preview_image_url='https://i.imgur.com/DmvFCIJ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
    elif (inputc == "install vse8.8"):
	#or (event.message.text == "Install vse8.8"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/7W7wXYh.jpg',
	    preview_image_url='https://i.imgur.com/7W7wXYh.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/pItv5hT.jpg',
	    preview_image_url='https://i.imgur.com/pItv5hT.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/bOvGauX.jpg',
	    preview_image_url='https://i.imgur.com/bOvGauX.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/2vRP4pC.jpg',
	    preview_image_url='https://i.imgur.com/2vRP4pC.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/rnrQT9m.jpg',
	    preview_image_url='https://i.imgur.com/rnrQT9m.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "uninstall vse8.8"):
	#or (event.message.text == "Uninstall vse8.8"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/qhguwnM.jpg',
	    preview_image_url='https://i.imgur.com/qhguwnM.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/pxX2HVk.jpg',
	    preview_image_url='https://i.imgur.com/pxX2HVk.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/FYjOMwS.jpg',
	    preview_image_url='https://i.imgur.com/FYjOMwS.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "install ens10"): 
	#or (event.message.text == "Install ens10"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/WBr1TGj.jpg',
	    preview_image_url='https://i.imgur.com/WBr1TGj.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/GvgT8LQ.jpg',
	    preview_image_url='https://i.imgur.com/GvgT8LQ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/utkMSES.jpg',
	    preview_image_url='https://i.imgur.com/utkMSES.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/P9F3DVr.jpg',
	    preview_image_url='https://i.imgur.com/P9F3DVr.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/UdG5CaW.jpg',
	    preview_image_url='https://i.imgur.com/UdG5CaW.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/fJhqnwj.jpg',
	    preview_image_url='https://i.imgur.com/fJhqnwj.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/uvhvWDx.jpg',
	    preview_image_url='https://i.imgur.com/uvhvWDx.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/wNaFYAM.jpg',
	    preview_image_url='https://i.imgur.com/wNaFYAM.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/wAmqVHa.jpg',
	    preview_image_url='https://i.imgur.com/wAmqVHa.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/kN87Ybn.jpg',
	    preview_image_url='https://i.imgur.com/kN87Ybn.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/U64Y6aa.jpg',
	    preview_image_url='https://i.imgur.com/U64Y6aa.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/6K3Z1r9.jpg',
	    preview_image_url='https://i.imgur.com/6K3Z1r9.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "uninstall ens10"):
	#or (event.message.text == "Uninstall ens10"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ynsasNL.jpg',
	    preview_image_url='https://i.imgur.com/ynsasNL.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/9R09HwZ.jpg',
	    preview_image_url='https://i.imgur.com/9R09HwZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/OV3qfRx.jpg',
	    preview_image_url='https://i.imgur.com/OV3qfRx.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Mqxq9Pk.jpg',
	    preview_image_url='https://i.imgur.com/Mqxq9Pk.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/U2ZBazn.jpg',
	    preview_image_url='https://i.imgur.com/U2ZBazn.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/5UvZvjZ.jpg',
	    preview_image_url='https://i.imgur.com/5UvZvjZ.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/jUqDyRc.jpg',
	    preview_image_url='https://i.imgur.com/jUqDyRc.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (event.message.text == "ข้าวเที่ยง"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/4D77SCC.jpg',
	    preview_image_url='https://i.imgur.com/hjKN0at.jpg')
        line_bot_api.reply_message(
            event.reply_token,image_message
            )
	
    elif (inputc == "epo deployment"):
	#or (event.message.text == "Install trend micro"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/GbnUB3W.jpg',
	    preview_image_url='https://i.imgur.com/GbnUB3W.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/sdTgT3g.jpg',
	    preview_image_url='https://i.imgur.com/sdTgT3g.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/TvK4Stu.jpg',
	    preview_image_url='https://i.imgur.com/TvK4Stu.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/R4AqyCM.jpg',
	    preview_image_url='https://i.imgur.com/R4AqyCM.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/QqVO8Kh.jpg',
	    preview_image_url='https://i.imgur.com/QqVO8Kh.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/x0614Mw.jpg',
	    preview_image_url='https://i.imgur.com/x0614Mw.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/k7EaEFu.jpg',
	    preview_image_url='https://i.imgur.com/k7EaEFu.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "eetech"):
	#or (event.message.text == "Install trend micro"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/NAeO8UU.jpg',
	    preview_image_url='https://i.imgur.com/NAeO8UU.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/k4h32EP.jpg',
	    preview_image_url='https://i.imgur.com/k4h32EP.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/nKS8WOG.jpg',
	    preview_image_url='https://i.imgur.com/nKS8WOG.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/maupzEV.jpg',
	    preview_image_url='https://i.imgur.com/maupzEV.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/lowujsB.jpg',
	    preview_image_url='https://i.imgur.com/lowujsB.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/8yVWdSa.jpg',
	    preview_image_url='https://i.imgur.com/8yVWdSa.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/lWhXB0A.jpg',
	    preview_image_url='https://i.imgur.com/lWhXB0A.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/uIlx1CY.jpg',
	    preview_image_url='https://i.imgur.com/uIlx1CY.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/nFaq6Ta.jpg',
	    preview_image_url='https://i.imgur.com/nFaq6Ta.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/A9INtLC.jpg',
	    preview_image_url='https://i.imgur.com/A9INtLC.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "status check"):
	#or (event.message.text == "Install trend micro"):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/NlmFZIj.jpg',
	    preview_image_url='https://i.imgur.com/NlmFZIj.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Yua4xrb.jpg',
	    preview_image_url='https://i.imgur.com/Yua4xrb.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/KD2QSRp.jpg',
	    preview_image_url='https://i.imgur.com/KD2QSRp.jpg')
        line_bot_api.push_message(
            profile.user_id,image_message
            )
	
    elif (inputc == "groupid"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(event.source.group_id)) 
	
    elif (inputarr[0].lower() == "de"):
        profile = line_bot_api.get_profile(event.source.user_id)
        logtxt = profile.user_id + ',' + profile.display_name + ',' + inputarr[0] + ',' + inputarr[1] + ',' + inputarr[2] + ',' + inputarr[3] + ',' + inputarr[4] + '\n'
        #logtxt = '1234'
        #logfile = open('Log.txt','a')        
        #logfile.write(logtxt)
        #logfile.close()
        DEmsg = 'Drive Encryption XML File request' + '\n' + 'Requester LINE ID : ' + profile.display_name + '\n' + 'Computer Name : ' + inputarr[1].upper() + '\n' + 'Send to : ' + inputarr[2] + '\n' + 'Tel. : ' + inputarr[3] + '\n' + 'Remark : ' + inputarr[4]
        line_bot_api.push_message(
            'Ccc45bdf03bf13fcebffbce390ff43012',
            TextSendMessage(logtxt)) 
        line_bot_api.push_message(
            'Ca1eed6eefec9ccb0382b34c99b7594a0',
            TextSendMessage(DEmsg)) 
	
    else:
        if (event.source.type != 'group'):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='ไม่มีสิทธิการใช้งาน USB และ MDM หรือถ้าไม่ใช่สิ่งที่ค้นหา กรุณาพิมพ์ "menu"'))   
        else:
            exit()
			


if __name__ == "__main__":
    app.run()
