# メモ
## 問題解答関連
### 新規コンテスト用dir作成
- dirを作りたい場所でやる
```
acc new [abc000]
```
### 次の問題用dir作成
```
acc add
```
### テストの実行
- 問題dir内で実行
```
oj t -c "python main.py"
```
### 提出
- 問題dir内で実行
```
acc submit
```
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
### python用設定
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
# import bisect
# import collections
# import copy
# import heapq
# import itertools
# import math
# import string
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


N = inp_i()
A = [inp_li() for _ in range(N)]
```
