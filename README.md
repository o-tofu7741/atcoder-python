# メモ
## 問題解答関連
### 新規コンテスト用dir作成
- dirを作りたい場所でやる
```
acc new [abc000]
```
### 次の問題用dir作成
- コンテストdirで実行
```
acc add
```
### テストの実行
- 問題dirで実行
- `tpy`は`oj~`のエイリアス
  - エイリアスは`$PROFILE`に記載
```
t-py
```
```
oj t -c "python main.py"
```
### 提出
- 問題dirで実行
- 各種コマンドは`acc~`のエイリアス
#### pypy
```
s-pp
```
```
acc s main.py -- --guess-python-interpreter pypy -w 0 -y
```
#### CPython
```
s-py
```
```
acc s main.py -- -l 5055 -w 0 -y
```
5055 : CPythonの言語ID
#### Cython
```
s-cy
```
```
acc s main.py -- -l 5082 -w 0 -y
```
5082 : Cythonの言語ID
### オプション
- `-c [all,inquire,etc..]`を`acc new`,`acc add`とかでつけると問題の選択なりなんなりが出来る
## その他
### acc設定ファイルとかのパス表示
```
acc config-dir
```
### `acc config`実行結果
```
default-contest-dirname-format: {ContestID}
default-task-dirname-format: {tasklabel}
default-test-dirname-format: test
default-task-choice: next
default-template: python
```
### config.json
```
{
	"oj-path": "C:\\github\\atcoder-python\\.venv\\Scripts\\oj.exe",
	"default-contest-dirname-format": "{ContestID}",
	"default-task-dirname-format": "{tasklabel}",
	"default-test-dirname-format": "test",
	"default-task-choice": "inquire",
	"default-template": "python"
}
```
### テンプレート用設定
#### template.json
```
{
    "task": {
        "program": [
            "main.py"
        ],
        "submit": "main.py"
    }
}
```
#### main.py
```
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

# import numpy


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    


if __name__ == "__main__":
    main()
```
