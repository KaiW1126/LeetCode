# 🟤 ソート系（Sorting）

## どんなアルゴリズム？

データを **昇順や降順に並べ替える** ことで、問題を解きやすくする前処理テクニック。
ソートすると「隣り合う要素の比較」だけで重なりやマージの判定ができるようになる。

```
例: Merge Intervals（区間のマージ）
  入力: [[1,3], [8,10], [2,6], [15,18]]

  ソートなし: どの区間がどの区間と重なるか、全ペアを確認 → O(n²)

  ソート後:  [[1,3], [2,6], [8,10], [15,18]]
    → 隣の区間だけ比較すればOK
    → [1,3]と[2,6]は重なる → [1,6]にマージ
    → 結果: [[1,6], [8,10], [15,18]]
```

**イメージ**: 「バラバラのトランプを数字順に並べてから処理する」 — 並べるだけで問題がシンプルになる。

---

## こう聞かれたらソート！

| キーワード | 例 |
|---|---|
| **「区間をマージ」** | Merge Intervals, Insert Interval |
| **「重なりを検出」** | Meeting Rooms |
| **「並べ替えてから処理」** | 3Sum（ソート + 2ポインタ） |

---

## Python での書き方

### 基本ソート
```python
# インプレースソート（元の配列を変更）
nums.sort()                         # 昇順（デフォルト）
nums.sort(reverse=True)             # 降順

# 新しいリストを返す
sorted_nums = sorted(nums)          # 元は変わらない
sorted_nums = sorted(nums, reverse=True)
```

### カスタムソート（key指定）
```python
# 第1要素でソート（区間問題の定番）
intervals.sort(key=lambda x: x[0])

# 第2要素でソート
intervals.sort(key=lambda x: x[1])

# 文字列の長さでソート
words.sort(key=len)

# 複数条件でソート（第1要素昇順、第2要素降順）
data.sort(key=lambda x: (x[0], -x[1]))
```

### ソート + 貪欲法テンプレート
```python
def solve_with_sort(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for current in intervals[1:]:
        last = result[-1]
        if current[0] <= last[1]:   # 重なっている
            last[1] = max(last[1], current[1])
        else:
            result.append(current)

    return result
```

### Python 構文ポイント
```python
# sorted() は新しいリストを返す → 元を変えたくないとき
# .sort() はインプレース → メモリ節約

# タプルのソート: 自動的に第1要素 → 第2要素の順で比較
pairs = [(3, 'b'), (1, 'c'), (3, 'a')]
pairs.sort()  # [(1, 'c'), (3, 'a'), (3, 'b')]
```

---

## 解いた問題

### 3Sum（ソート + 2ポインタ）
> **配列をソートしてから2ポインタで効率的にペアを探す**

ソートすることで重複スキップが簡単になり、2ポインタの合計判定も可能になる。

📂 [3sum.py](../Blind75/Python/Medium/3sum.py)

---

### Merge Intervals（ソート + 区間マージ）
> **開始位置でソートして前から順にマージ**

📂 [MergeIntervals.py](../Blind75/Python/Medium/MergeIntervals.py)

---

### Insert Interval（ソート + 区間マージ）
> **新区間を追加してソートし、同じ手法でマージ**

📂 [InsertInterval.py](../Blind75/Python/Medium/InsertInterval.py)
