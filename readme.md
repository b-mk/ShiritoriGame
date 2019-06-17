# しりとりゲームのコードについて

## 事前準備
- pykakasi( https://pypi.org/project/pykakasi/ )と、requests( https://pypi.org/project/requests/ )をインストールしておいてください。
- コンピュータをインターネットに接続してください。プロキシが自動設定でない場合は、「 python/parsetxt.py 」内に書かれているプロキシ設定を変更してください。
- 「 https://developer.yahoo.co.jp/webapi/jlp/ma/v1/parse.html 」よりYahooClientIDを取得し、「 python/pasetxt.py 」9行目のappidに代入してください。

## 起動方法
1. cgi-binの親のディレクトリで、PowerShellを管理者権限で開きます。
1. PowerShellに「python -m http.server 8080 --cgi」を入力します。
1. ブラウザで「localhost:8080/html/first-screen.html」を開きます。

## 補足
- 判定の基準については、PowerPointにあるルール説明をご覧ください。
- バグを発見した場合は、製作者に報告してください。

## 最終更新日
2019/6/17

## 制作者
びーまか