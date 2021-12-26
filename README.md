# 何ができるの
ファイルの再帰ダウンロードやhtmlから特定のタグなどを抽出することができます

# 基本的な使い方
```bash
$ prop [options] URL
```

# 基本的なオプション
## -o, --output [filename], -O
-o, --outputオプションでは出力先ファイルを指定することができます  
-Oオプションでは、ダウンロード元のファイルと同じ名前で保存します  
これらのオプションを指定しない場合、標準出力に出力されます

## -a, --fake-user-agent
UserAgentの値を偽装します

## -s, --search-words [検索ワード]
指定されたURLのhtmlコードから検索することができます  
検索ワードとして使えるのは以下の通りです

|  クエリ  |  値  |
|  ----  |  ---- |
|  tags  |  タグ名  |
|  class  |  クラス名  |
|  id  |  id  |
|  text  |  タグの値  |
|  href  |  参照先  |
|  src  |  画像などの参照先  |
|  limit  |  取得数  |

また、値を複数指定する場合は、%で区切って指定してください(空白はいれない)

Ex:
```bash
$ prop -s tags=a%script limit=5 URL

-> URLのソースコードからaタグとscriptタグを合計で5つ取得
```

## -r [下る階層の数]
指定されたURLを起点として再帰ダウンロードします  
再帰ダウンロードの対象はaタグのhref属性とimgのsrc属性に指定されているURLです  
また、-nEオプションが指定されていない場合、ダウンロード後に自動で参照先をローカルファイルに置き換えます

### -rオプションを指定した場合のみ使用できるオプション

#### -I, --interval [interval]
ダウンロードのインターバルを指定します  
再帰ダウンロードは対象のサイトに過剰な負荷をかけることがあるので、5秒以上の指定を推奨します  
また、robots.txtの指示よりも短い時間が指定されている場合は、robots.txtの数値に置き換えられます

### -M, --limit [limit]
ダウンロードするファイルの数を指定します

### -f, --format [format]
ダウンロードするファイルのファイル名のフォーマットを指定することができます  
特殊なフォーマットは以下の通りです

|  フォーマット  |  代入される値  |
|  ----  |  ----  |
|  %(file)s  |  ダウンロード元のファイル名  |
|  %(num)d  |  0から始まる連番  |


Ex:
```bash
$ prop -r -f %(num)dtest-%(file)s URL

-> 0test-[filename], 1test-[filename] ...という名前でダウンロード
```

### ダウンロード対象を制限(拡張)するオプション
|  短縮オプション名  |  長いオプション名  |  処理  |
|  ----  |  ----  |  ----  |
|  -np  |  --noparent  |  起点のURLより上の階層のURLは無視するオプション  |
|  -nc  |  --no-content  |  aタグのhref属性のURLのみ対象とするオプション  |
|  -nb  |  --no-body  |  imgタグのsrc属性のURLのみ対象とするオプション  |
|  -nd  | --no-downloaded  |  既にダウンロードしたファイルは無視するオプション  |
|  -dx  |  --download-external  |  外部サイトのURLもダウンロード対象とするオプション  |
|  -st  |  --start  |  ダウンロードを開始するファイル名を指定することができます  |

また、-ncオプションと-nbオプションの併用はできません

## ここに載っていないオプションについて
-h, --helpオプションを使用するとヘルプが表示されます  
ここに載っているオプションも含めて説明しているので、そちらをご覧ください

# 何故これを作ったのか
wgetの再帰ダウンロードって確かファイル名のフォーマット決められなかったんですよ  
なので作りました(せっかくなので自分が使う機能も詰め合わせた)
