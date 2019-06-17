var modes = ['普通', '３文字', 'IT用語'];
var modeNum;
var enemyNames = ['たまごあし', 'ごろた', 'にゃんこ先生'];
var words = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"];
var lastWord = "";
var score = 0;

var userName;
var modeNum;
var myIconNum;

$(function() {
    var data = location.search.split('&');
    userName = decodeURIComponent(data[0].split('=')[1]);
    modeNum = decodeURIComponent(data[1].split('=')[1]);
    myIconNum = decodeURIComponent(data[2].split('=')[1]);

    console.log("modeNum = " + modeNum);
    initScreen(userName, myIconNum);
    var introText = enemyNames[modeNum] + 'と一緒にしりとりをしよう！<br>下に20文字以内で文字を入力してね！';
    dispOKDialog(introText);

    sendDataToPy(1, modeNum, "", "");
})

function initScreen(userName, myIconNum) {
    changeText('mode', 'しりとり：' + modes[modeNum] + 'モード');
    changeElement('enemy_icon', 'src', '../images/icon_' + modeNum + '.png');
    changeText('enemy_name', enemyNames[modeNum]);
    changeElement('user_icon', 'src', '../images/icon_' + myIconNum + '.png');
    changeText('user_name', userName);
}

function changeElement(id, element, val) {
    $('#' + id).attr(element, val);
}

function changeText(id, text) {
    document.getElementById(id).innerHTML = text;
}

function judgeCorrectWord() {
    var inputWord = document.forms.form.input_word.value;
    changeText("user_word", "判定中…");
    changeText("user_kana", "　");
    document.forms.form.input_word.value = "";
    sendDataToPy(0, modeNum, inputWord, lastWord);
}

function dispOKDialog(message) {
    changeText("dialog_message", message);
    document.getElementById("dialog_parent").style.visibility = "visible";
    document.getElementById("filter").style.visibility = "visible";
}

function hideDialog() {
    document.getElementById("dialog_parent").style.visibility = "hidden";
    document.getElementById("filter").style.visibility = "hidden";
}

function changeLastWord(word) {
    word = word.trim();
    lastWord = word;
}

function getNextEnemyWord(word) {
    changeText("enemy_word", "考え中…");
    changeText("enemy_kana", "　");
    sendDataToPy(2, modeNum, "", word);
    setTimeout(function(){
        changeText("user_word", "　");
        changeText("user_kana", "　");
    },900);
}

function finishGame(loserNum=0) {
    var loserName = [enemyNames[modeNum], userName];
    if (loserNum == 0) {
        score += 10000;
    }
    dispOKDialog(loserName[loserNum] + "の負けです！<br >結果表示画面に移動します");
    query = '?name=' + encodeURIComponent(userName) + '&mode_num=' + encodeURIComponent(modeNum) + '&my_icon_num=' + encodeURIComponent(myIconNum) + "&score=" + encodeURIComponent(score) + "&loser=" + loserNum;
    document.getElementById("dialog_button").onclick = function() {
        window.location.href = '../html/result-screen.html' + query;
    }
}

function sleep(a){
    var dt1 = new Date().getTime();
    var dt2 = new Date().getTime();
    while (dt2 < dt1 + a){
      dt2 = new Date().getTime();
    }
    return;
}

function calcScore(inputWord) {
    var thisScore = inputWord.length * 100;
    score += thisScore;
    changeText("score", "スコア：" + score + "点");    
}