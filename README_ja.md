# 何ができるの
ファイルの再帰ダウンロードやhtmlから特定のタグなどを抽出することができます

# インストール
```bash
$ pip install prop-request
```

# 基本的な使い方
```bash
$ prop [options] URL
```

# 基本的なオプション
## -o, --output [path]
-o, --outputオプションでは出力先ファイル、ディレクトリを指定することができます  
ディレクトリを指定した場合、指定したディレクトリにダウンロード元と同じファイル名で保存されます  
また、-rオプションを使う際はこのオプションで保存先ディレクトリを指定してください

## -O
ダウンロード元のファイルと同じ名前で保存します  
-o, --output, 及びこのオプションを指定しない場合、標準出力に出力されます

## -a, --fake-user-agent
UserAgentの値を偽装します

## -U, --upgrade
propをアップデートします  
これはpip install --no-cache-dir --upgrade prop-request を実行しているだけなので、こちらを直接実行しても構いません

## -s, --search-words [検索ワード]
指定されたURLのhtmlコードから検索することができます  
以下は検索ワードとして使えるものの一例です(relやalt等での指定も可能ですが数が多いので主なもののみ)

|  クエリ  |  値  |
|  ----  |  ---- |
|  tags  |  タグ名  |
|  class  |  クラス名  |
|  id  |  id  |
|  text  |  タグの値  |
|  href  |  参照先  |
|  src  |  画像などの参照先  |
|  limit  |  取得数(-Mオプションでも指定可)  |

また、値を複数指定する場合は、','で区切って指定してください(空白はいれない)

Ex:

```bash
$ prop -s tags=a,script limit=5 URL

-> URLのソースコードからaタグとscriptタグを合計で5つ取得
```

## -M, --limit [limit]
再帰ダウンロードするファイルの数や、-s, --searchオプションの結果の取得数の指定

## -R, --read-file [file]
URLやオプションの指定を予め記述してあるファイルから読み込みます  
また、セッションは保持されるため、ログインしてからアクセスするといったことも可能です

Ex:  
instruct.txtの中身

```
-a -n -d name=hoge password=hogehoge -o /dev/null https://www.example.com/login.php
-O https://www.example.com/page.html
```

```bash
$ prop -R instruct.txt
>>> https://www.example.com/page.htmlをpage.htmlとしてダウンロード
```

## -r, --recursive [下る階層の数]
指定されたURLを起点として再帰ダウンロードします  
下る階層の数を指定しなかった場合は1が指定されたものとして実行します  
再帰ダウンロードの対象はaタグのhref属性とimgのsrc属性に指定されているURLです  
また、-nEオプションが指定されていない場合、ダウンロード後に自動で参照先をローカルファイルに置き換えます  


このオプションを使用する場合は、-o, --outputオプションで保存先ディレクトリを指定してください


### -rオプションを指定した場合のみ使用できるオプション

#### -I, --interval [interval]
ダウンロードのインターバルを指定します  
再帰ダウンロードは対象のサイトに過剰な負荷をかけることがあるので、5秒以上の指定を推奨します  
また、robots.txtの指示よりも短い時間が指定されている場合は、robots.txtの数値に置き換えられます

#### -f, --format [format]
ダウンロードするファイルのファイル名のフォーマットを指定することができます  
特殊なフォーマットは以下の通りです

|  フォーマット  |  代入される値  |
|  ----  |  ----  |
|  %(root)s  |  ダウンロード元のホスト名  |
|  %(file)s  |  ダウンロード元のファイル名  |
|  %(num)d  |  0から始まる連番  |
|  %(ext)s  |  拡張子  |


Ex:
```bash
$ prop -r -f "%(num)dtest-%(file)s" -o store_ directory URL

-> store_directory/0test-[filename], store_directory/1test-[filename] ...という名前でダウンロード

$ prop -r -f "test-%(num)d.%(ext)s" -o store_ directory URL

-> store_directory/test-0.[ext], store_directory/test-1[ext] ...という名前でダウンロード
```

※フォーマットに%(num)d、または%(file)sが含まれていない場合、反映されないので注意して下さい(保存名が動的に変化しないため)  
また、%(file)sと%(ext)sフォーマットは最後のみ、%(num)dの2個以上の使用、%(num)d%(file)sのように特殊フォーマットを連続させることは出来ないなどの制限があります(%(num)dの為の正確な連番の生成が不可能になるため)

## ダウンロード対象を制限(拡張)するオプション
|  短縮オプション名  |  長いオプション名  |  処理  |
|  ----  |  ----  |  ----  |
|  -np  |  --no-parent  |  起点のURLより上の階層のURLは無視するオプション  |
|  -nc  |  --no-content  |  aタグのhref属性のURLのみ対象とするオプション  |
|  -nb  |  --no-body  |  imgタグのsrc属性のURLのみ対象とするオプション  |
|  -nd  | --no-downloaded  |  既にダウンロードしたファイルは無視するオプション  |
|  -dx  |  --download-external  |  外部サイトのURLもダウンロード対象とするオプション  |
|  -st  |  --start  |  ダウンロードを開始するファイル名を指定するオプション  |

※ -ncオプションと-nbオプションの併用はできません

## ここに載っていないオプションについて
-h, --helpオプションを使用するとヘルプが表示されます  
ここに載っているオプションも含めて説明しているので、そちらをご覧ください

# 履歴、ログの保存先
履歴の保存場所は--history-directory、ログの書き込み先は--log-fileオプション、キャッシュの保存場所は--cache-directoryで見ることができます

```bash
# ログの簡単な見方
$ cat $(prop --log-file)

# 履歴一覧
$ ls $(prop --history-directory)

# キャッシュの保存場所
$ prop --cache-directory
```

また、これらを削除するオプションもあります

```bash
# ログの消し方
$ prop --purge-log

# 履歴の削除の仕方
$ prop --purge-history

# キャッシュの削除
$ prop --purge-cache
```

#  テスト
まず、pytestをインストールして下さい

```bash
$ pip install pytest
```

インストール済みの人、またはインストールした人はカレントディレクトリを'prop', または'prop/tests'にしてからpytestコマンドを実行してください

```bash
$ git clone https://github.com/mino-38/prop
$ cd prop
$ pytest
```

テスト中のpropコマンドの出力を見たい場合は、'-s'オプションを付けてpytestを実行してください

```bash
$ pytest -s
```

# 新機能
- --update-cacheオプションを使うことでローカルにキャッシュしたファイルをアップデートする事ができるようになりました

- ダウンロード中に進捗を表示するようにしました

# ライセンス
[MITライセンス](https://github.com/mino-38/prop/blob/main/LICENSE)です
