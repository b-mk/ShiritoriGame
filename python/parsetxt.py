"""
YahooAPIを用いたテキスト解析を行う
"""

import requests
import xml.etree.ElementTree as ET

# 取得したYahooClientIDをここに入力する
appid = ""
pageurl = "https://jlp.yahooapis.jp/MAService/V1/parse?"

def is_entry_word(sentence="", results="ma", filter="1|9|10"):
    """
    sentenceが名詞・動詞・形容詞に当てはまっていればTrue、なければFalseを返す
    """
    ret = []
    proxies = { 'http':'http://cproxy.okinawa-ct.ac.jp:8080'}
    
    params = pageurl + 'appid=' + appid + '&results=' + results + '&filter=' + filter + '&sentence=' + sentence
    response = requests.post(params).text
    word_list = parse_xml(xml=response)
    
    if (len(word_list) <= 0):
        return False
    elif (sentence in word_list):
        return True
    else:
        return False

def parse_xml(xml=""):
    """
    YahooAPIから送られてきたxmlを解析し、最初の単語を返却する
    """
    root = ET.fromstring(xml)
    word_list = []
    for value in root.iter('{urn:yahoo:jp:jlp}surface'):
        word_list.append(value.text)
    
    return word_list