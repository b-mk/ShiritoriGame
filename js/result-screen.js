var modes = ['普通', '３文字', 'IT用語'];
var enemyNames = ['たまごあし', 'ごろた', 'にゃんこ先生'];

var userName;
var modeNum;
var myIconNum;
var score;
var winnerName;

var comments = ["もっと頑張って…いけるやろ",
                "まあまあじゃないですかね",
                "大変良く頑張りました",
                "まじ？めちゃくちゃ頑張ったじゃん",
                "あの…もしかして勝ったの？コンピュータに？…やべえやつじゃん"];

$(function() {
    var data = location.search.split("&");
    userName = decodeURIComponent(data[0].split("=")[1]);
    modeNum = decodeURIComponent(data[1].split("=")[1]);
    myIconNum = decodeURIComponent(data[2].split("=")[1]);
    score = decodeURIComponent(data[3].split("=")[1]);
    var loserNum = decodeURIComponent(data[4].split("=")[1]);
    if (loserNum == 0) {
        winnerName = userName;
    } else {
        winnerName = enemyNames[modeNum];
    }
    
    initScreen();
    dispComment();
})

function initScreen() {
    changeText("mode", modes[modeNum] + "モード");
    changeElement("enemy_icon", "src", "../images/icon_" + modeNum + ".png");
    changeText("enemy_name", enemyNames[modeNum]);
    changeElement("user_icon", "src", "../images/icon_" + myIconNum + ".png");
    changeText("user_name", userName + "さん");
    changeText("winner", winnerName);
    changeText("score", score + "点");
}

function changeElement(id, element, val) {
    $("#" + id).attr(element, val);
}

function changeText(id, text) {
    document.getElementById(id).innerHTML = text;
}

function dispComment() {
    var comment;
    if (winnerName == userName) {
        comment = comments[4];
    } else if (score <= 1000) {
        comment = comments[0];
    } else if (score <= 3000) {
        comment = comments[1];
    } else if (score <= 5000) {
        comment = comments[2];
    } else {
        comment = comments[3];
    }

    changeText("comment", comment);
}