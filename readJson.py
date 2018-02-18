#-*- coding: utf-8 -*-import oauth2
import json
from collections import OrderedDict
from pprint import pprint

with open('윤성빈_twitter.json', encoding="utf-8") as data_file: 
#with open('jtbc_news_twitter.json', encoding="utf-8") as data_file:    
    data = json.load(data_file, object_pairs_hook=OrderedDict)
 
#pprint(data)
print(len(data))
result =[]
for i in range(len(data)):
    #print(data[i]["message"])
    result.append(data[i]["message"])

thefile = open('result_윤성빈.txt', 'w',encoding= 'UTF-8')
for item in result:
  thefile.write("%s\n" % item)
thefile.close()  