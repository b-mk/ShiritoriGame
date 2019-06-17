"""
jsで受け取ったrequest_numをもとに必要な処理を判断し、
処理結果をjsにtextで返却する

request_numが
0の場合:入力文字がルール違反をしていないかの判定を行う
1の場合:データを初期化し、しりとりの最初の単語を返す
2の場合:コンピュータの返事を返す
"""

# -*- coding: utf-8 -*-
import sys, io, cgi, cgitb, random

sys.path.append('.')
from python import file, kana, parsetxt

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable()

form = cgi.FieldStorage()
request_num = form.getfirst("request_num")

print("Content-type: text/html\nAccess-Control-Allow-Origin: *\n")
if (request_num == "0"):
    other_data = form.getfirst("other_data")
    other_data = other_data.split(",")
    mode = str(other_data[0])
    input_word = str(other_data[1])
    last_word = str(other_data[2])

    INPUT_WORD_ERROR_NO0 = "3文字の単語じゃないよ！"
    INPUT_WORD_ERROR_NO1 = "1文字はダメ！2文字以上でお願いします"
    INPUT_WORD_ERROR_NO2 = "最初の文字が" + str(last_word) + "じゃないよ！"
    INPUT_WORD_ERROR_NO3 = "最後の文字が「ん」だよ！"
    INPUT_WORD_ERROR_NO4 = "最後の文字は平仮名でお願いします…"
    INPUT_WORD_ERROR_NO5 = "その単語はもう出たことあるよ"
    INPUT_WORD_ERROR_NO6 = "その単語は分かりません…"
    INPUT_WORD_ERROR_NO7 = "何も文字が入力されてないよ…"

    word_kana = str(kana.parse_kana(input_word))
    new_last_word = kana.search_last_word(word_kana)

    if (len(input_word) == 0):
        print("0," + INPUT_WORD_ERROR_NO7)
    
    elif((mode == "1") and len(word_kana) != 3):
        print("0," + INPUT_WORD_ERROR_NO0)

    elif (len(word_kana) == 1):
        print("0," + INPUT_WORD_ERROR_NO1)

    elif(word_kana[0] != last_word):
        print("0," + INPUT_WORD_ERROR_NO2)

    elif (new_last_word == kana.LAST_CHAR_ERROR):
        print("0," + INPUT_WORD_ERROR_NO3)

    elif(new_last_word == kana.UNSUPPORT_WORD_ERROR):
        print("0," + INPUT_WORD_ERROR_NO4)
    
    elif(not(file.is_word_unused(word_kana))):
        print("0," + INPUT_WORD_ERROR_NO5)
    
    elif ((mode == "2") and (file.is_unregistered(search_word=word_kana))):
        print("0," + INPUT_WORD_ERROR_NO6)
    
    elif((mode != "2") and (not(parsetxt.is_entry_word(sentence=input_word)))):
        print("0," + INPUT_WORD_ERROR_NO6)
    
    else:
        file.add_used_data(add_word=word_kana)
        print("1," + word_kana + "," + new_last_word)
        
elif(request_num == "1"):
    mode = form.getfirst("mode")
    file.init_used_data(mode=mode)
    start_word_kana = file.get_new_word(mode=mode).strip()
    file.add_used_data(add_word=start_word_kana)
    last_word = kana.search_last_word(start_word_kana.split(",")[1]).strip()
    print(start_word_kana + "," + last_word)

elif(request_num == "2"):
    other_data = form.getfirst("other_data")
    other_data = other_data.split(",")
    mode = str(other_data[0])
    first_word = str(other_data[1])

    while(True):
        pop_times = file.get_pop_times(mode=mode, word=first_word)
        enemy_word_kana = file.get_new_word(first_word=first_word, line_num=pop_times, mode=mode).strip()
        if enemy_word_kana == file.LOSE_COMPUTER:
            print(file.LOSE_COMPUTER)
            break
        else:
            file.add_pop_times(mode=mode, word=first_word)
            enemy_word_kana = enemy_word_kana.split(",")
            enemy_word = enemy_word_kana[0]
            enemy_kana = enemy_word_kana[1]
            if (file.is_word_unused(search_word=enemy_kana)):
                file.add_used_data(add_word=enemy_kana)
                new_last_word = str(kana.search_last_word(word=enemy_kana)).strip()
                print(str(enemy_word) + "," + str(enemy_kana) + "," + str(new_last_word) + "," + str(pop_times))
            break
        file.add_pop_times(mode=mode, word=first_word)