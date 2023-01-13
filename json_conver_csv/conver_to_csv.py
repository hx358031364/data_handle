# coding: utf-8
import os
import pandas as pd
import json
filelist = os.listdir('./jsonfile')
jsonpath="./jsonfile/"


for item in filelist:
    content = {''}
    dataset=content
    # txt = open(jsonpath + 'predictions.json',encoding='utf-8')
    txt = open(jsonpath + 'instances_val.json',encoding='utf-8')
    json_txt = json.load(txt)
    label = []
    # print(json_txt['shapes'])
    labels = json_txt['shapes']
    for l in labels:
        label.append(l["label"])
        if l["label"] in content.keys():
            dataset[l["label"]] = 1
    dataset['id'] = item
    dataset['labels'] = str(label)
    print(content)
    data2=pd.DataFrame(dataset,index=[0])
    data2.to_csv("porn.csv",index=False,mode='+a',header=False,encoding='utf_8_sig')