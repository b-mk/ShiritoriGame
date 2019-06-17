var FIRST_WORD_ERROR = "先頭文字が正しい表記ではありません";
var FILE_NOT_FOUND = "ファイルが存在しません";
var LOSE_COMPUTER = "コンピュータの負け！";
var NOT_WORK_SERVER = "サーバが動いていません";
var INTERIOR_PROCESSING_ERROR = "内部処理のエラーです。<br/>制作者に問い合わせてください。"

function sendDataToPy(requestNum, mode, inputWord="", lastWord="") { 
    /**
     * sendDataToPy関数:サーバにリクエストを送り、その処理結果を受け取る関数。
     * requestNumによってリクエストの内容が異なる。
     * 
     * --------------------------------------------
     * 0の場合:
     *  入力された文字がしりとりの条件に反しているか確認し、
     *  大丈夫なら次の単語を、ダメならエラーコードを受け取る。
     * 1の場合:
     *  データの初期化
     *  しりとりの最初の単語を受け取る。
     * 2の場合:
     *  コンピュータが返事をする単語を受け取る。
     */

    var url = "http://localhost:8080/cgi-bin/server.py";
    var type = "post";
    var dataType = "text";

    if (requestNum == 0) {
        var otherData = mode + "," + inputWord + "," + lastWord;
        changeText("user_word", "判定中…");
        $.ajax({
            url: url,
            type: type,
            dataType : dataType,
            data: {
                request_num: requestNum,
                other_data: otherData
            }
        })
        .done(function(response) {
            console.log("res = " + response);
            response = response.split(",");
            if (response[0] == "0") {
                dispOKDialog(response[1] + "<br/>別の単語を選んでね！");
                changeText("user_word", "　");
            } else if(response.length >= 100) {
                dispOKDialog(INTERIOR_PROCESSING_ERROR);
            } else {
                var lastWord = response[2].trim();
                console.log("lastWord = " + lastWord);
                changeText("user_word", inputWord);
                changeText("user_kana", response[1]);
                changeLastWord(lastWord);
                calcScore(response[1]);
                getNextEnemyWord(lastWord);
            }
        })
        .fail(function() {
            dispOKDialog(NOT_WORK_SERVER);
        });
    } else if (requestNum == 1) {
        var startWord;
        $.ajax({
            url: url,
            type: type,
            dataType : dataType,
            data: {
                request_num: requestNum,
                mode: mode,
            }
        })
        .done(function(response) {
            console.log("res = " + response);
            if (response.length >= 100) {
                dispOKDialog(INTERIOR_PROCESSING_ERROR);
            }
            startWord = response.split(",");
            changeText("enemy_word", startWord[0]);
            changeText("enemy_kana", startWord[1]);
            lastWord = startWord[2];
            changeLastWord(lastWord);
        })
        .fail(function() {
            dispOKDialog(NOT_WORK_SERVER);
        });
    } else if (requestNum == 2) {
        var otherData = mode + "," + lastWord;
        console.log("req2で送るやつ = " + otherData);
        $.ajax({
            url: url,
            type: type,
            dataType : dataType,
            data: {
                request_num: requestNum,
                other_data: otherData
            }
        })
        .done(function(response) {
            console.log("res = " + response);
            if (response == LOSE_COMPUTER) {
                finishGame();
            } else if (response.length >= 100) {
                dispOKDialog(INTERIOR_PROCESSING_ERROR);
            } else {
                response = response.split(",");
                changeText("enemy_word", response[0]);
                changeText("enemy_kana", response[1]);
                lastWord = response[2];
                changeLastWord(lastWord);
            }
        })
        .fail(function() {
            dispOKDialog(NOT_WORK_SERVER);
        });
    }
}