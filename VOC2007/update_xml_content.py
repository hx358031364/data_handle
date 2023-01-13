# coding=utf-8
import os
import xml.dom.minidom
import cv2
import warnings
# warnings.filterwarnings('default')

import shutil
# jpg对应文件夹
jpg_path = r'E:\huangxin\logo_jiansuo\Open Brand\voc\annotations'
# 储存xml文件的文件夹的路径
path = r'E:\huangxin\logo_jiansuo\Open Brand\voc\annotations'
# 得到文件夹下所有文件名称
jpgs = os.listdir(jpg_path)
i = 1
# label = []
# with open('./labels.txt', 'r') as f:
#     names = f.read().split('\n')
# names_list = list(filter(None, names))
names_list = ['lv', 'tsingtao', 'beats', 'champion', 'headshoulder', 'paulfrank', 'mcm', 'wuliangye', 'adidas', 'newbalance', 'nike', 'chromehearts', 'michael_kors', 'playboy', 'chanel', 'kappa', 'armani', 'starbucks', 'loewe', 'anta', 'nba', 'shaxuan', 'darlie', 'cdgplay', 'eral', 'd_wolves', 'gillette', 'keds', 'sony', 'hellokitty', 'kipling', 'katespade', 'bull', 'erke', 'dior', 'peppapig', 'coach', 'audi', 'canon', 'anessa', 'givenchy', 'huawei', 'bosideng', 'pampers', 'vans', 'moschino', 'ralphlauren', 'camel', 'hollister', 'girdear', 'teenieweenie', 'lux', 'longchamp', 'abercrombiefitch', 'doraemon', 'toread', 'hengyuanxiang', 'underarmour', 'kenzo', 'diesel', 'jeanswest', 'zhejiangweishi', 'reddragonfly', 'omega', 'toryburch', 'fendi', 'ugg', 'dissona', 'toyota', 'pantene', 'goldlion', 'mac', 'lexus', 'disney', 'newera', 'tries', 'ferragamo', 'fjallraven', 'simon', 'jiangshuweishi', 'fresh', 'flyco', 'columbia', 'lee', 'marcjacobs', 'supor', 'bmw', 'celine', 'lacoste', 'samsung', 'septwolves', 'jeep', 'montagut', 'midea', 'dhc', 'hugoboss', 'bolon', 'hermes', 'lenovo', 'hikvision', 'moncler', 'burberry', 'safeguard', 'erdos', 'vatti', 'guess', 'loreal', 'yuantong', 'miumiu', 'sk2', 'benz', 'ck', 'ny', 'lanvin', 'miffy', 'only', 'airjordan', 'gucci', 'rejoice', 'oakley', 'jimmychoo', 'volcom', '361du', 'evisu', 'dove', 'nikon', 'suzuki', 'zippo', 'wanda', 'nanfu', 'amass', 'kiehls', 'toshiba', 'dolcegabbana', 'threesquirrels', 'xiaomi', 'walmart', 'hunanweishi', 'tissot', 'daphne', 'chenguang', 'gap', 'budweiser', 'levis', 'otterbox', 'titoni', 'apple', 'bosch', 'valentino', 'nestle', 'longines', 'durex', 'lincoln', 'cocacola', 'christianlouboutin', 'puma', 'inman', 'wodemeiliriji', 'stanley', 'thehistoryofwhoo']
a = {
    "lv": "louis_vuitton",
    "tsingtao": "tsingtao",
    "beats": "beats",
    "champion": "champion",
    "headshoulder": "heads&houlder",
    "paulfrank": "paulfrank",
    "mcm": "mcm",
    "wuliangye": "wuliangye",
    "adidas": "adidas",
    "newbalance": "new_balance",
    "nike": "nike",
    "chromehearts": "chromehearts",
    "michael_kors": "michael_kors",
    "playboy": "playboy",
    "chanel": "chanel",
    "kappa": "kappa",
    "armani": "armani",
    "starbucks": "starbucks_coffee",
    "loewe": "loewe",
    "anta": "anta",
    "nba": "nba",
    "shaxuan": "sassoon",
    "darlie": "darlie",
    "cdgplay": "comme_des_garcons",
    "eral": "eral",
    "d_wolves": "d_wolves",
    "gillette": "gillette",
    "keds": "keds",
    "sony": "sony",
    "hellokitty": "hello_kitty",
    "kipling": "kipling",
    "katespade": "kate_spade",
    "bull": "bull",
    "erke": "erke",
    "dior": "dior",
    "peppapig": "peppa",
    "coach": "coach",
    "audi": "audi",
    "canon": "canon",
    "anessa": "anessa",
    "givenchy": "givenchy",
    "huawei": "huawei",
    "bosideng": "bosideng",
    "pampers": "pampers",
    "vans": "vans",
    "moschino": "moschino",
    "ralphlauren": "ralph_lauren",
    "camel": "camel",
    "hollister": "hollister",
    "girdear": "girdear",
    "teenieweenie": "teenie_weenie",
    "lux": "lux",
    "longchamp": "longchamp",
    "abercrombiefitch": "abercrombie&fitch",
    "doraemon": "doraemon",
    "toread": "toread",
    "hengyuanxiang": "hengyuanxiang",
    "underarmour": "under_armour",
    "kenzo": "kenzo",
    "diesel": "diesel",
    "jeanswest": "jeanswest",
    "zhejiangweishi": "zhejiangweishi",
    "reddragonfly": "red_dragonfly",
    "omega": "omega",
    "toryburch": "tory_burch",
    "fendi": "fendi",
    "ugg": "ugg",
    "dissona": "dissona",
    "toyota": "toyota",
    "pantene": "pantene",
    "goldlion": "goldlion",
    "mac": "mac",
    "lexus": "lexus",
    "disney": "disney",
    "newera": "newera",
    "tries": "tries",
    "ferragamo": "salvatore_ferragamo",
    "fjallraven": "fjall_raven",
    "simon": "simon",
    "jiangshuweishi": "jiangshuweishi",
    "fresh": "fresh",
    "flyco": "flyco",
    "columbia": "columbia",
    "lee": "lee",
    "marcjacobs": "marc_jacobs",
    "supor": "supor",
    "bmw": "bmw",
    "celine": "celine",
    "lacoste": "lacoste",
    "samsung": "samsung",
    "septwolves": "septwolves",
    "jeep": "jeep",
    "montagut": "montagut",
    "midea": "midea",
    "dhc": "dhc",
    "hugoboss": "hugoboss",
    "bolon": "bolon",
    "hermes": "hermes",
    "lenovo": "lenovo",
    "hikvision": "hikvision",
    "moncler": "moncler",
    "burberry": "burberry",
    "safeguard": "safeguard",
    "erdos": "erdos",
    "vatti": "vatti",
    "guess": "guess",
    "loreal": "loreal",
    "yuantong": "yt_express",
    "miumiu": "miumiu",
    "sk2": "sk-ii",
    "benz": "benz",
    "ck": "calvin_klein",
    "ny": "ny",
    "lanvin": "lanvin",
    "miffy": "miffy",
    "only": "only",
    "airjordan": "airjordan",
    "gucci": "gucci",
    "rejoice": "rejoice",
    "oakley": "oakley",
    "jimmychoo": "jimmy_choo",
    "volcom": "volcom",
    "361du": "361",
    "evisu": "evisu",
    "dove": "dove",
    "nikon": "nikon",
    "suzuki": "suzuki",
    "zippo": "zippo",
    "wanda": "wanda",
    "nanfu": "nanfu",
    "amass": "amass",
    "kiehls": "kiehls",
    "toshiba": "toshiba",
    "dolcegabbana": "d&g",
    "threesquirrels": "three_squirrels",
    "xiaomi": "xiaomi",
    "walmart": "walmart",
    "hunanweishi": "hunanweishi",
    "tissot": "tissot",
    "daphne": "daphne",
    "chenguang": "chenguang",
    "gap": "gap",
    "budweiser": "budweiser",
    "levis": "levis",
    "otterbox": "otter_box",
    "titoni": "titoni",
    "apple": "apple",
    "bosch": "bosch",
    "valentino": "valentino",
    "nestle": "nestle",
    "longines": "longines",
    "durex": "durex",
    "lincoln": "lincoln",
    "cocacola": "cocacola",
    "christianlouboutin": "christian_louboutin",
    "puma": "puma",
    "inman": "inman",
    "wodemeiliriji": "wodemeiliriji",
    "stanley": "stanley",
    "thehistoryofwhoo": "the_history_of_fo"
  }

xml_list = []
for jpg_name in jpgs:  # 遍历文件夹
    xml_name = jpg_name
    print('修改第' + str(i) + '个xml' + ' 名字是:' + xml_name)
    i = i + 1
    # 得到一个xml完整的路径
    # xml_name = jpg_name.split(".")[0]
    # xml_name = xml_name+'.xml'

    xml_path = os.path.join(path, xml_name)
    # 读取xml
    # dom = xml.dom.minidom.parse(xml_path)
    f = open(xml_path, "r", encoding='utf-8')
    r = f.read()
    text = str(r.encode('utf-8'), encoding="utf-8")
    # 使用minidom解析器打开 XML 文档
    dom = xml.dom.minidom.parseString(text)
    old_xml = dom.documentElement

    # 重命名folder,filename,path
    # if len(old_xml.getElementsByTagName("folder")) != 0:
    #     old_xml.getElementsByTagName("folder")[0].firstChild.data = 'JPEGImages'
    # if len(old_xml.getElementsByTagName("filename")) != 0:
    #     old_xml.getElementsByTagName("filename")[0].firstChild.data =jpg_name + '.jpg'
    # if len( old_xml.getElementsByTagName("path")) != 0:
    #     old_xml.getElementsByTagName("path")[0].firstChild.data = 'JPEGImages/'+jpg_name + '.jpg'

    # 图片宽高修改
    # img = cv2.imread(os.path.join(jpg_path, jpg_name))
    # h, w, _ = img.shape
    # size = old_xml.getElementsByTagName("size")
    # size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = w
    # size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = h

    # 修改object内容
    root = dom.documentElement
    object_root = root.getElementsByTagName('object')
    length = len(object_root)
    # print(length)
    for root_i in range(length):
        node_name = object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue
        if node_name.lower() in names_list:
            object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue = a[node_name.lower()]
        else:
            object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue = 'unknown'



    # 保存修改到xml文件中
    with open(xml_path, 'w') as f:
        dom.writexml(f)
    f.close()
# print('保存修改成功！！！')