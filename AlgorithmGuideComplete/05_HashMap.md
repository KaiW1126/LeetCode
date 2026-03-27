# ⚪ ハッシュマップ / ハッシュセット（Hash Map / Hash Set）

## どんなアルゴリズム？

**「キー → 値」の対応表** を使って、データの検索・追加・削除を **O(1)（一瞬）** で行うデータ構造。
Pythonでは `dict`（辞書）や `set` がこれにあたる。

```
ハッシュマップ（dict）: キーと値のペアを保存
  {"apple": 3, "banana": 1, "cherry": 2}
  → 「appleは何個？」→ 一瞬で 3 と分かる

ハッシュセット（set）: 値の存在だけを保存
  {1, 3, 5, 7, 9}
  → 「5は含まれる？」→ 一瞬で True と分かる
```

**イメージ**: 「名簿の索引」 — 名前の頭文字で引ける索引があれば、一瞬で該当者を見つけられる。

---

## こう聞かれたらハッシュ！

| キーワード | 例 |
|---|---|
| **「含まれるか？」**（O(1)で判定） | Two Sum, Contains Duplicate |
| **「頻度を数える」** | Group Anagrams, Top K Frequent Elements |
| **「重複を排除」** | Find Difference of Two Arrays |
| **「対応関係を記憶」** | Valid Anagram |

---

## 見分けるコツ

```
✅ ハッシュのサイン:
  1. 「ある値が存在するか」を高速に知りたい
  2. 出現回数を数えたい
  3. 値と値の対応関係を保存したい
```

---

## Python での書き方

### dict（ハッシュマップ）
```python
# 基本操作
d = {}
d[key] = value         # 追加・更新
key in d               # 存在確認 O(1)
d.get(key, default)    # デフォルト値付き取得

# 初期値付き辞書
from collections import defaultdict
count = defaultdict(int)   # 存在しないキーは0を返す
count['a'] += 1

# Counter（出現回数カウント）
from collections import Counter
counter = Counter("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
counter = Counter([1, 2, 2, 3])  # {2: 2, 1: 1, 3: 1}
```

### set（ハッシュセット）
```python
# 基本操作
s = set()
s.add(x)               # 追加
s.remove(x)            # 削除（なければエラー）
s.discard(x)           # 削除（なくてもエラーにならない）
x in s                 # 存在確認 O(1)

# リストから重複排除
unique = list(set(nums))

# 集合演算
a - b                  # 差集合（aにあってbにない）
a & b                  # 積集合（両方にある）
a | b                  # 和集合（どちらかにある）
```

### グルーピングパターン
```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # ソートした文字列をキーに
        groups[key].append(s)
    return list(groups.values())
```

---

## 解いた問題

### Group Anagrams（グルーピング）
> **「アナグラムごとにグループ化」→ ソートした文字列をキーにハッシュマップ**

各文字列をソートしてキーにし、`defaultdict(list)` でグループ化。

📂 [GroupAnagrams.py](../Blind75/Python/Medium/GroupAnagrams.py)

---

### Longest Consecutive Sequence（セットで高速検索）
> **「最長の連続数列の長さは？」→ setで前の数があるか O(1) 判定**

配列をsetに変換。`num - 1` が存在しない数 = 連続の開始点。そこから右に数えていく。

📂 [Longest ConsecutiveSequence.py](../Blind75/Python/Medium/Longest%20ConsecutiveSequence.py)

---

### Find Difference of Two Arrays（差集合）
> **「2つの配列の差分を求める」→ set の差集合演算**

両方をsetに変換し、`set1 - set2` と `set2 - set1` で差分を取得。

📂 [DifferentTwoArray.py](../Blind75/Python/Easy/DifferentTwoArray.py)

---

### Single Number（setで追跡）
> **「1つだけ出現する数を見つける」→ setで出現を追跡**

setに追加し、既にあれば削除。最後に残った1つが答え。（XOR解法もある）

📂 [SingleNumber.py](../NeetCode150/easy/SingleNumber.py)

---

### Happy Number（サイクル検出）
> **「各桁の2乗の和を繰り返して1になるか？」→ setで見た数を記録してサイクル検出**

📂 [HappyNumber.py](../NeetCode150/easy/HappyNumber.py)
