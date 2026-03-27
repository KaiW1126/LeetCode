# 🎯 Blind75 Easy 問題まとめ (Python版)

このファイルは Blind75 の Easy 問題の解き方、使用したアルゴリズム、Python の構文をまとめたものです。

---

## 📊 カテゴリ別一覧

| カテゴリ | 問題 | 進捗 |
|----------|------|------|
| **配列 (Array)** | Two Sum, Contains Duplicate, Best Time to Buy and Sell Stock, Missing Number | [ ] |
| **文字列 (String)** | Valid Anagram, Valid Palindrome, Longest Substring | [ ] |
| **リンクドリスト (Linked List)** | Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle | [ ] |
| **二分木 (Binary Tree)** | Invert Binary Tree, Same Tree, Subtree of Another Tree | [ ] |
| **動的計画法 (DP)** | Climbing Stairs | [ ] |
| **スタック (Stack)** | Valid Parentheses | [ ] |
| **ビット操作 (Bit Manipulation)** | Number of 1 Bits, Reverse Bits, Counting Bits | [ ] |

---

## 🔥 アルゴリズム別まとめ

### 1. ハッシュテーブル (dict)
**問題**: Two Sum, Valid Anagram, Contains Duplicate

```python
# 基本的な辞書の使い方
d = {}
d[key] = value
key in d          # キーが存在するか確認 O(1)

# 初期値付き辞書（collections.defaultdict）
from collections import defaultdict
count = defaultdict(int)  # 存在しないキーは0を返す
count['a'] += 1

# Counter（文字の出現回数カウントに便利）
from collections import Counter
counter = Counter("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

**ポイント**:
- 辞書の検索は O(1) で高速
- 「補数を探す」パターンが頻出（Two Sum）
- `Counter` で文字の出現回数カウントが簡単

---

### 2. スライディングウィンドウ (Sliding Window)
**問題**: Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    left = 0
    max_length = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

**ポイント**:
- 2つのポインタ（left, right）でウィンドウを管理
- 条件を満たさなくなったら left を縮める
- Ruby の `Set.new` → Python の `set()`

---

### 3. 二分木の再帰 (Tree Recursion)
**問題**: Same Tree, Invert Binary Tree, Subtree of Another Tree

```python
def is_same_tree(p, q):
    if not p and not q:       # 両方None → 同じ
        return True
    if not p or not q:        # 片方だけNone → 違う
        return False
    if p.val != q.val:        # 値が違う → 違う
        return False

    # 左右を再帰的にチェック
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```

**ポイント**:
- ベースケース: `None` のチェック（Ruby の `nil` → Python の `None`）
- 再帰: 左右の子ノードに同じ処理を適用
- `and` / `or` で結果を組み合わせる（Ruby の `&&` `||` → Python の `and` `or`）

---

### 4. リンクドリストの操作
**問題**: Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle

```python
# リバース（ポインタの付け替え）
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

**ポイント**:
- `prev`, `current`, `next_node` の3つのポインタ
- Dummy Node パターン（Merge用）

#### うさぎとかめ（Floyd's Cycle Detection）
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

### 5. 動的計画法 (Dynamic Programming)
**問題**: Climbing Stairs

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    one_step_before = 2
    two_steps_before = 1

    for _ in range(3, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before
```

**ポイント**:
- フィボナッチ数列と同じ考え方
- `f(n) = f(n-1) + f(n-2)`
- 空間を O(1) に最適化できる
- Ruby の `(3..n).each` → Python の `range(3, n + 1)`

---

### 6. スタック (Stack)
**問題**: Valid Parentheses

```python
stack = []
stack.append(item)   # 追加（Ruby の push）
stack.pop()          # 取り出し
len(stack) == 0      # 空かチェック（または not stack）
```

**ポイント**:
- LIFO (Last In, First Out)
- 括弧の対応チェックに最適
- Python ではリストをスタックとして使う

---

### 7. ビット操作 (Bit Manipulation)
**問題**: Number of 1 Bits, Reverse Bits, Counting Bits

```python
# 2進数変換
bin(n)                    # '0b1010' のような文字列に
bin(n).count('1')         # 1の数を数える

# 整数を2進数文字列に（接頭辞なし）
format(n, 'b')            # '1010'

# 32ビットに揃える
format(n, '032b')         # '00000000000000000000000000001010'

# 2進数文字列を整数に
int('1010', 2)            # 10
```

---

### 8. 数学的アプローチ
**問題**: Missing Number

```python
# 等差数列の和の公式
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing = expected_sum - actual_sum
```

---

### 9. 優先度付きキュー (Heap / Priority Queue)
**問題**: Kth Largest Element in a Stream

```python
import heapq

# 初期化（リストから最小ヒープを作る）O(N)
nums = [4, 5, 8, 2]
heapq.heapify(nums)

# 追加 O(log N)
heapq.heappush(nums, 3)

# 最小値の削除＆取得 O(log N)
min_val = heapq.heappop(nums)

# 最小値の参照 O(1)
top = nums[0]

# ※ Pythonには最大ヒープがないため、値にマイナスを掛けて代用する
```

**ポイント**:
- 常に最小値が先頭に来るように要素を管理
- 「Top K を探す」「K番目に大きいものを探す」問題で大活躍

---

## 📝 Python 構文まとめ

### リスト操作
```python
len(nums)              # 長さ
sum(nums)              # 合計
sorted(nums)           # ソート（新しいリストを返す）
nums.sort()            # インプレースソート
list(set(nums))        # 重複削除
x in nums              # 要素が含まれるか O(n)
min(nums) / max(nums)  # 最小/最大
min(a, b)              # 2つの値の最小
```

### リストの繰り返し `[値] * n`
```python
# 同じ初期値で埋めたリストを一発で作る構文
dp = [False] * (len(s) + 1)  # len(s)+1 個の False で初期化
[0] * 5        # → [0, 0, 0, 0, 0]
[True] * 3     # → [True, True, True]

# ⚠️ DP配列で +1 する理由:
#   dp[0]〜dp[len(s)] まで使うので、len(s)+1 個必要
#   dp[0] は「空文字列」= 基底ケース（Word Break など）
```

### 文字列操作
```python
list(s)                # 文字のリストに変換
for c in s:            # 1文字ずつ処理
import re
re.sub(r'[^a-zA-Z0-9]', '', s)  # 正規表現で置換
s.lower()              # 小文字に
s[::-1]                # 逆順
s.zfill(n)             # ゼロパディング
```

### 繰り返し
```python
for num in nums:                    # 各要素
for i, num in enumerate(nums):      # インデックス付き
for i in range(n + 1):              # 0からn（含む）
for i in range(n):                  # 0からn-1
```

### 辞書 (dict)
```python
d = {}
d = defaultdict(int)        # 初期値0
key in d                    # キー存在確認
d.values()                  # 値のビュー
all(v == 0 for v in d.values())  # 全て条件を満たすか
```

### よく使うパターン
```python
# ガード節
if not root:
    return None
if len(s) != len(t):
    return False

# 多重代入（スワップ）
a, b = b, a
root.left, root.right = root.right, root.left

# 三項演算子
result = value1 if condition else value2

# or でデフォルト値
x = x or default_value
```

### クラス定義と `self` の使い方
```python
class MyClass:
    # コンストラクタ（初期化メソッド）
    def __init__(self, k: int):
        self.k = k        # インスタンス変数として保存
        self.data = []    # 別のメソッドからもアクセス可能になる

    # インスタンスメソッド
    def add(self, val: int):
        self.data.append(val)
        if len(self.data) > self.k:
            self.data.pop(0)
```
**`self` とは？**:
- クラス自身のインスタンス（オブジェクト自体）を指す
- メソッドの第1引数には必ず `self` を書く決まりがある
- `self.変数名` と書くことで、メソッド（関数）の処理が終わってもデータが消えずに保持され、クラス内の他のメソッドからいつでも呼び出せる状態（共有ポケット）になる

### Ruby → Python 主な違い

| Ruby | Python | 説明 |
|------|--------|------|
| `nil` | `None` | 空を表す |
| `&&` / `||` | `and` / `or` | 論理演算子 |
| `.nil?` | `is None` | nil/Noneチェック |
| `Hash.new(0)` | `defaultdict(int)` | 初期値付き辞書 |
| `.key?(k)` | `k in d` | キー存在確認 |
| `.each { \|x\| }` | `for x in ...:` | ループ |
| `.each_with_index` | `enumerate()` | インデックス付きループ |
| `(0...n).each` | `range(n)` | 範囲ループ |
| `[a, b].max` | `max(a, b)` | 最大値 |
| `.include?(x)` | `x in list` | 要素の存在確認 |
| `.push` / `.pop` | `.append` / `.pop` | スタック操作 |
| `.empty?` | `not list` or `len(list) == 0` | 空チェック |
| `.to_s(2)` | `bin(n)` | 2進数変換 |
| `.to_i(2)` | `int(s, 2)` | 2進数→整数 |
| `Set.new` | `set()` | 集合 |

---

## ⏱️ 計算量まとめ

| 問題 | 時間 | 空間 | 理由 |
|------|------|------|------|
| Two Sum | O(n) | O(n) | ハッシュで1回走査 |
| Contains Duplicate | O(n) | O(n) | setで重複チェック |
| Valid Anagram | O(n) | O(1) | 文字種は固定なので |
| Valid Parentheses | O(n) | O(n) | スタック使用 |
| Climbing Stairs | O(n) | O(1) | 変数2つのみ |
| Best Time to Buy | O(n) | O(1) | 1回走査 |
| Linked List Cycle | O(n) | O(1) | ポインタ2つのみ |
| Tree系 | O(n) | O(h) | h=木の高さ（再帰） |

---

## 🎓 学んだこと

1. **辞書(dict)は最強**: 検索 O(1) を活用して計算量を下げる
2. **再帰はベースケースから**: `None` チェックを最初に
3. **ポインタの管理**: Linked List は `prev`, `current`, `next_node` の3つ
4. **数学的発想**: 公式を知っていると一発で解ける（Missing Number）
5. **スタックはLIFO**: 括弧の対応に最適
6. **ヒープ(heapq)**: Top K 系の問題や、常に最大・最小を追跡したい場合に O(log N) の威力を発揮する
7. **クラスの `self`**: 関数を跨いでデータを保持するための「共有ポケット」として活躍する
