"""
日本語文字列に対する操作を行う
"""

from pykakasi import kakasi

LAST_CHAR_ERROR = "最後の文字が「ん」です"
UNSUPPORT_WORD_ERROR = "対応していない文字が含まれています"

words = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"]
special_words = {"ゃ":"や", "ゅ":"ゆ", "ょ":"よ", "ぁ":"あ", "ぃ":"い", "ぅ":"う", "ぇ":"え", "ぉ":"お", "っ":"つ"}

def parse_kana(word=""):
    """
    wordを平仮名に変換する
    """

    conv_kana = kakasi()
    conv_kana.setMode("J", "H")
    conv_kana.setMode("K", "H")
    return conv_kana.getConverter().do(word)

def search_last_word(word=""):
    """
    wordの最後の文字を返却する
    """
    if len(word) == 0:
        return UNSUPPORT_WORD_ERROR
    elif word[-1] == "ー":
        return (search_last_word(word=word[-2]))
    elif word[-1] == "ん":
        return LAST_CHAR_ERROR
    elif (word[-1] not in words) and (word[-1] not in special_words.keys()):
        return UNSUPPORT_WORD_ERROR
    elif word[-1] in words:
        return word[-1]
    else:
        return special_words[word[-1]]
