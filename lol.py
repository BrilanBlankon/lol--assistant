

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import os
from bs4 import BeautifulSoup
import requests

global option_list,web_table_list,champion_dict
option_list = {'核心裝備':'items',
             '技能點法':'skills-orders',
             '符文點法':'runes'
            }
web_table_list = {'items':'data_table sortable_table',
             'skills-orders':'data_table skillsOrdersTable',
             'runes':'perksTableContainerTable'
            }
champion_dict = {'厄薩斯':'Aatrox',
                     '阿璃':'Ahri',
                     '阿卡莉':'Akali',
                     '亞歷斯塔':'Alistar',
                     '阿姆姆':'Amumu',
                     '艾妮維亞':'Anivia',
                     '安妮':'Annie',
                     '亞菲利歐':'Aphelios',
                     '艾希':'Ashe',
                     '翱銳龍獸':'AurelionSol',
                     '阿祈爾':'Azir',
                     '巴德':'Bard',
                     '布里茨':'Blitzcrank',
                     '布蘭德':'Brand',
                     '布郎姆':'Braum',
                     '凱特琳':'Caitlyn',
                     '卡蜜兒':'Camille',
                     '卡莎碧雅':'Cassiopeia',
                     '科加斯':'Chogath',
                     '庫奇':'Corki',
                     '達瑞斯':'Darius',
                     '黛安娜':'Diana',
                     '蒙多醫生':'DrMundo',
                     '達瑞文':'Draven',
                     '艾克':'Ekko',
                     '伊莉絲':'Elise',
                     '伊芙琳':'Evelynn',
                     '伊澤瑞爾':'Ezreal',
                     '費德提克':'Fiddlesticks',
                     '菲歐拉':'Fiora',
                     '飛斯':'Fizz',
                     '加里歐':'Galio',
                     '剛普朗克':'Gangplank',
                     '蓋倫':'Garen',
                     '吶兒':'Gnar',
                     '古拉格斯':'Gragas',
                     '葛雷夫':'Graves',
                     '赫克林':'Hecarim',
                     '漢默丁格':'Heimerdinger',
                     '伊羅旖':'Illaoi',
                     '伊瑞莉雅':'Irelia',
                     '埃爾文':'Ivern',
                     '珍娜':'Janna',
                     '嘉文四世':'JarvanIV',
                     '賈克斯':'Jax',
                     '杰西':'Jayce',
                     '燼':'Jhin',
                     '吉茵珂絲':'Jinx',
                     '凱莎':'Kaisa',
                     '克黎思妲':'Kalista',
                     '卡瑪':'Karma',
                     '卡爾瑟斯':'Karthus',
                     '卡薩丁':'Kassadin',
                     '卡特蓮娜':'Katarina',
                     '凱爾':'Kayle',
                     '慨影':'Kayn',
                     '凱能':'Kennen',
                     '卡力斯':'Khazix',
                     '鏡爪':'Kindred',
                     '克雷德':'Kled',
                     '寇格魔':'KogMaw',
                     '勒布朗':'Leblanc',
                     '李星':'LeeSin',
                     '雷歐娜':'Leona',
                     '莉莉亞':'Lillia',
                     '麗珊卓':'Lissandra',
                     '路西恩':'Lucian',
                     '露璐':'Lulu',
                     '拉克絲':'Lux',
                     '墨菲特':'Malphite',
                     '馬爾札哈':'Malzahar',
                     '茂凱':'Maokai',
                     '易大師':'MasterYi',
                     '好運姐':'MissFortune',
                     '魔鬥凱薩':'Mordekaiser',
                     '魔甘娜':'Morgana',
                     '娜米':'Nami',
                     '納瑟斯':'Nasus',
                     '納帝魯斯':'Nautilus',
                     '妮可':'Neeko',
                     '奈德麗':'Nidalee',
                     '夜曲':'Nocturne',
                     '努努':'Nunu',
                     '歐拉夫':'Olaf',
                     '奧莉安娜':'Orianna',
                     '鄂爾':'Ornn',
                     '潘森':'Pantheon',
                     '波比':'Poppy',
                     '派克':'Pyke',
                     '姬亞娜':'Qiyana',
                     '葵恩':'Quinn',
                     '銳空':'Rakan',
                     '拉姆斯':'Rammus',
                     '雷珂煞':'RekSai',
                     '銳兒':'Rell',
                     '雷尼克頓':'Renekton',
                     '雷葛爾':'Rengar',
                     '雷玟':'Riven',
                     '藍寶':'Rumble',
                     '雷茲':'Ryze',
                     '煞蜜拉':'Samira',
                     '史瓦妮':'Sejuani',
                     '姍娜':'Senna',
                     '瑟菈紛':'Seraphine',
                     '賽特':'Sett',
                     '薩科':'Shaco',
                     '慎':'Shen',
                     '希瓦娜':'Shyvana',
                     '辛吉德':'Singed',
                     '賽恩':'Sion',
                     '希維爾':'Sivir',
                     '史加納':'Skarner',
                     '索娜':'Sona',
                     '索拉卡':'Soraka',
                     '斯溫':'Swain',
                     '賽勒斯':'Sylas',
                     '星朵拉':'Syndra',
                     '貪啃奇':'TahmKench',
                     '塔莉雅':'Taliyah',
                     '塔隆':'Talon',
                     '塔里克':'Taric',
                     '提摩':'Teemo',
                     '瑟雷西':'Thresh',
                     '崔絲塔娜':'Tristana',
                     '特朗德':'Trundle',
                     '泰達米爾':'Tryndamere',
                     '逆命':'twistedFate',
                     '圖奇':'Twitch',
                     '烏迪爾':'Udyr',
                     '烏爾加特':'Urgot',
                     '法洛士':'Varus',
                     '汎':'Vayne',
                     '維迦':'Veigar',
                     '威寇茲':'Velkoz',
                     '菲艾':'Vi',
                     '維克特':'Viktor',
                     '弗拉迪米爾':'Vladimir',
                     '弗力貝爾':'Volibear',
                     '沃維克':'Warwick',
                     '悟空':'MonkeyKing',
                     '剎雅':'Xayah',
                     '齊勒斯':'Xerath',
                     '趙信':'XinZhao',
                     '犽宿':'Yasuo',
                     '犽凝':'Yone',
                     '約瑞科':'Yorick',
                     '悠咪':'Yuumi',
                     '札克':'Zac',
                     '劫':'Zed',
                     '希格斯':'Ziggs',
                     '極靈':'Zilean',
                     '柔依':'Zoe',
                     '枷蘿':'Zyra',
                    }


def check_champions(champion_name):
    return champion_name in champion_dict.keys()

def get_lol_champions_detail(champion_name,option):
    #基礎設定
    options = Options()
    #防止網頁跳出式框
    options.add_argument("--disable-notifications")
    #chromes 無頭模式
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    #網頁大小 -為了劫到完整圖片
    options.add_argument("window-size=1280,1024")
    #Chrome的webdriver
    chrome = webdriver.Chrome('./chromedriver_win32/chromedriver.exe', options=options)
    
    #判斷是否輸入正確
    if champion_name not in champion_dict.keys() or option not in option_list:
        print('請確認輸入是否正確')
        return False
    else:
        #搜尋leagueofgraphs
        chrome.get("https://www.leagueofgraphs.com/champions/{}/{}".format(option_list[option],champion_dict[champion_name].lower()))
        #設置delay防止request過快
        time.sleep(2)
        
        #截圖
        chrome.save_screenshot(r'temp.png')
        web_table = web_table_list[option_list[option]]
        #抓取web中特定table
        baidu = chrome.find_element_by_css_selector("table[class='"+web_table+"']")
        print(baidu)
        #設定截圖範圍
        left = baidu.location['x'] 
        top = baidu.location['y'] 
        elementWidth = baidu.location['x'] + baidu.size['width']
        elementHeight = baidu.location['y'] + baidu.size['height'] 
        picture = Image.open(r'temp.png')
        #將想要的範圍裁切下來
        picture = picture.crop((left, top, elementWidth, elementHeight))
        picture.save(champion_dict[champion_name]+'_'+option_list[option]+'.png')
        os.remove("temp.png")
        chrome.quit()
        print('finish')
        return True

def get_champions_icon_url(champion_name):
    name = champion_dict[champion_name]
    response = requests.get("https://lol.garena.tw/game/champion/{}".format(name))
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find(id='champion_icon').get("src")

def get_champions_story(champion_name):
    name = champion_dict[champion_name].lower()
    response = requests.get("https://universe.leagueoflegends.com/zh_TW/story/champion/{}/".format(name))
    response.encoding = 'utf-8'
    node = response.text.split('"').index('description')
    all_content = response.text.split('"')[node+2].split('。')
    content =''
    for index in range(len(all_content)-1):
        content += all_content[index]
        content += '。\n\n'
    return content
