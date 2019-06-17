"""
file.py
csvファイルへの操作を行う
"""

import random
import csv
import os

first_words = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"]
FIRST_WORD_ERROR = "先頭文字が正しい表記ではありません"
FILE_NOT_FOUND = "ファイルが存在しません"
LOSE_COMPUTER = "コンピュータの負け！"

def init_used_data(mode=0):
    """
    使用した単語・単語の使用回数を初期化し、wordsをランダムで並び替える
    """
    for w in first_words:
        path = "./used-word/" + w + ".txt"
        path = os.path.abspath(path)
        with open(path, "w") as used_file:
           used_file.write("")

        path = "./pop-times/" + w + ".txt"
        path = os.path.abspath(path)
        with open(path, "w") as pop_times_file:
            if w == "り":
                pop_times_file.write("1")
            else:
                pop_times_file.write("0")

    for first_word in first_words:
        path = "./words/mode" + mode + "/" + first_word + ".csv"
        path = os.path.abspath(path)
        word_data = []
        if not(os.path.isfile(path)):
            return FILE_NOT_FOUND
        
        with open(path, "r") as file:
            for row in csv.reader(file):
                word_data.append(row[0] + "," + row[1] + "\n")
        
        random.shuffle(word_data)
        with open(path, "w") as file:
            for data in word_data:
                file.write(data)
            word_data = []
    return 

def add_used_data(add_word=""):
    """
    add_wordを、使用済単語としてused_word内のファイルに登録する
    """
    if (word_not_found(add_word[0])):
        return FIRST_WORD_ERROR
    
    path = "./used-word/" + add_word[0] + ".txt"
    path = os.path.abspath(path)
    if not(os.path.isfile(path)):
        FILE_NOT_FOUND
    
    with open(path, "a") as used_file:
       used_file.write(add_word + "\n")
    return

def is_word_unused(search_word=""):
    """
    search_wordで与えられた単語が使用済みだったらFalse、そうでなかったらTrueを返す
    """
    search_word = search_word.strip()

    if (word_not_found(search_word[0])):
        return FIRST_WORD_ERROR

    path = "./used-word/" + search_word[0] + ".txt"
    path = os.path.abspath(path)
    if not(os.path.isfile(path)):
        return FILE_NOT_FOUND
    
    with open(path, "r") as used_file:
        for used_word in used_file:
            used_word = used_word.strip()
            if search_word in used_word:
                return False
    return True

def get_new_word(first_word="り", line_num = 0, mode=0):
    """
    first_wordから始まり、まだ出ていない単語を返す
    """
    path = "./words/mode" + mode + "/" + first_word + ".csv"
    path = os.path.abspath(path)
    if not(os.path.isfile(path)):
        return FILE_NOT_FOUND
    
    words = []
    with open(path, "r") as file:
        for line in file:
            words.append(line)
    
    words_len = len(words)
    line_num = int(line_num)
    if (words_len <= line_num):
        return LOSE_COMPUTER
    else:
        for i in range(line_num, words_len):
            words[i] = words[i].split(",")
            if is_word_unused(words[i][1]):
                return (words[i][0] + "," + words[i][1])
        
        return LOSE_COMPUTER

def word_not_found(word):
    """
    word(先頭文字)のファイルが存在するならTrue、無ければFalseを返す
    """
    if (word not in first_words):
        return True
    else:
        return False
        
def get_pop_times(mode, word):
    """
    先頭がwordの単語をコンピュータが何回使ったかを返す
    """
    path = "./pop-times/" + word[0] + ".txt"
    path = os.path.abspath(path)
    if not(os.path.isfile(path)):
        return FILE_NOT_FOUND
    
    cnt = 0
    with open(path, "r") as pop_times_file:
        for pop_times in pop_times_file:
            cnt = cnt + int(pop_times)
    return int(cnt)

def add_pop_times(mode, word):
    """
    コンピュータが、先頭wordの単語を使った回数を1増やす
    """
    path = "./pop-times/" + word + ".txt"
    path = os.path.abspath(path)
    if not(os.path.isfile(path)):
        return FILE_NOT_FOUND
    
    cnt = get_pop_times(mode, word) + 1
    with open(path, "w") as pop_times_file:
        pop_times_file.write(str(cnt))

def is_unregistered(search_word=""):
    """
    IT用語モードで引数で与えられた単語が登録されていなかったらTrue、されていたらFalseを返す
    """
    search_word = search_word.strip()

    if (word_not_found(search_word[0])):
        return FIRST_WORD_ERROR

    path = "./words/mode2/" + search_word[0] + ".csv"
    path = os.path.abspath(path)
    if not(os.path.isfile(path)):
        return FILE_NOT_FOUND
    
    res = "search = " + search_word + "\n"
    with open(path, "r") as words_file:
        for word in words_file:
            w = word.split(",")
            w = w[1].strip()
            res = res + "w = " + str(w) + "\n"
            if w in search_word:
                return False
    return True