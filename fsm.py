from transitions.extensions import GraphMachine
from utils import send_text_message,send_image_url,push_message
import lol
import os
import pyimgur

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.champion_name = ""
        self.CLIENT_ID = os.getenv("Client_ID", None)

    def get_img_url(self,path):
        im = pyimgur.Imgur(self.CLIENT_ID)
        uploaded_image = im.upload_image(path)
        return uploaded_image.link

    def is_going_to_lobby(self,event):
        return True 

    def on_enter_lobby(self, event):
        print("In lobby")
        userid = event.source.user_id
        push_message(userid,"歡迎使用{},請輸入欲查詢的英雄名稱(目前僅限中文名稱)".format(" LOL小助手 "))
        

    def on_exit_lobby(self,event):
        print("Leaving lobby")

    def is_going_to_champions(self,event):
        text = event.message.text
        if(lol.check_champions(text)):
            self.champion_name = text
            return True
        else:
            return False

    def reselect_champion(self,event):
        text = event.message.text
        return text == "離開" or text.lower() == "exit"
      
    
    def on_enter_champions(self,event):
        print("In champions")
        userid = event.source.user_id
        reply_token = event.reply_token
        send_image_url(reply_token, lol.get_champions_icon_url(self.champion_name))
        push_message(userid, "您選擇的英雄是 {}\n\n目前有四種功能:\n\n1.查詢推薦核心裝備\n\n2.查詢推薦符文\n\n3.查詢推薦技能點法\n\n4.閱讀傳記故事\n\n請輸入\"核心裝備\"、\"符文點法\"、\"技能點法\"、\"傳記故事\"，來查詢，或者輸入\"1\"、\"2\"、\"3\"、\"4\"\n若要重新選擇英雄，請輸入\"離開\"或是\"exit\"".format(self.champion_name))

    def on_exit_champions(self,event):
        print("Leaving champions")

    
    def is_going_to_items(self,event):
        text = event.message.text
        return text == "核心裝備" or text == "1"   

    def is_going_to_runes(self,event):
        text = event.message.text
        return text == "符文點法" or text == "2"
    
    def is_going_to_skills(self,event):
        text = event.message.text
        return text == "技能點法" or text == "3"

    def is_going_to_story(self,event):
        text = event.message.text
        return text == "傳記故事" or text == "4"

    def on_enter_items(self,event):
        print("In items")
        userid = event.source.user_id
        push_message(userid,"查詢中請稍後")
        lol.get_lol_champions_detail(self.champion_name,"核心裝備")
        
        img_url = lol.champion_dict[self.champion_name]+'_'+lol.option_list["核心裝備"]+'.png'
        print(img_url)
        reply_token = event.reply_token
        send_image_url(reply_token, self.get_img_url(img_url))
        os.remove(img_url)
        self.go_back_to_lobby(event)

    def on_enter_runes(self,event):
        print("In runes")
        userid = event.source.user_id
        push_message(userid,"查詢中請稍後")
        lol.get_lol_champions_detail(self.champion_name,"符文點法")
        reply_token = event.reply_token
        img_url = lol.champion_dict[self.champion_name]+'_'+lol.option_list["符文點法"]+'.png'
        send_image_url(reply_token, self.get_img_url(img_url))
        os.remove(img_url)
        self.go_back_to_lobby(event)
    
    def on_enter_skills(self,event):
        print("In skills")
        userid = event.source.user_id
        push_message(userid,"查詢中請稍後")
        lol.get_lol_champions_detail(self.champion_name,"技能點法")
        reply_token = event.reply_token
        img_url = lol.champion_dict[self.champion_name]+'_'+lol.option_list["技能點法"]+'.png'
        send_image_url(reply_token, self.get_img_url(img_url))
        os.remove(img_url)
        self.go_back_to_lobby(event)
        
    def on_enter_story(self,event):
        print("In story")
        reply_token = event.reply_token
        send_text_message(reply_token, lol.get_champions_story(self.champion_name))
        self.go_back_to_lobby(event)
    
    
    def on_exit_items(self,event):
        print("Leaving items")

    def on_exit_runes(self,event):
        print("Leaving runes")

    def on_exit_skills(self,event):
        print("Leaving skills")