# ⛰️ 優先度付きキュー / ヒープ（Heap / Priority Queue）

## どんなアルゴリズム？

データの中で **「常に一番大きい（または小さい）要素」** を高速に取り出せるようにする特殊なツリー構造（ヒープ木）。
追加・削除が O(log N)、最小/最大値の取得が O(1)。

```
例: K番目に大きい要素を追跡する
  常に「上位K個」だけを保存する最小ヒープ（Min-Heap）を作る。
  新しい数字が来たら入れ、サイズがKを超えたら一番小さいやつを捨てる。
  → ヒープの先頭には常に「K番目に大きい要素」が残る！
```

**イメージ**: 「トーナメント戦」 — 常に優勝者（最大・最小）が頂点に立ち、勝者が抜けても残りのメンバーですぐに次の優勝者を決める仕組み。

---

## こう聞かれたらヒープ！

| キーワード | 例 |
|---|---|
| **「K番目に大きい/小さい〇〇」** | Kth Largest Element in a Stream |
| **「出現頻度の上位K個」** | Top K Frequent Elements |
| **「最小/最大を常に追跡」** | Find Median from Data Stream |

---

## 見分けるコツ

```
✅ ヒープのサイン:
  1. 「K番目」や「Top K」というキーワードがある
  2. データを追加しながら、常に最大/最小を取り出したい（動的なデータ）
  3. 全てをソートする必要はなく、最上位の一部だけ分かればいい
```

---

## Python での書き方

### 基本操作（heapq = 最小ヒープ）
```python
import heapq

# リストからヒープを作る O(N)
nums = [4, 5, 8, 2]
heapq.heapify(nums)

# 要素の追加 O(log N)
heapq.heappush(nums, 3)

# 最小値の取り出し O(log N)
min_val = heapq.heappop(nums)

# 最小値の参照（取り出さない）O(1)
top = nums[0]
```

### 最大ヒープ（Pythonにはないので符号反転で代用）
```python
import heapq

# 最大ヒープ: 値にマイナスを掛けて入れる
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)

# 最大値の取り出し: 取り出してからマイナスを戻す
max_val = -heapq.heappop(max_heap)  # 8
```

### Top K パターン（クラス実装）
```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # サイズがkになるまで小さいものを捨てる
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # 最小を捨てる
        return self.heap[0]           # K番目に大きい = ヒープの先頭
```

### Python 構文ポイント
```python
import heapq

# heapq は最小ヒープのみ対応
# 最大ヒープが欲しい → 値に -1 を掛ける

# heapify は O(N) ← sort の O(N log N) より速い
# heappush / heappop は O(log N)

# クラスの self: メソッド間でデータを共有する「共有ポケット」
class MyClass:
    def __init__(self, k):
        self.k = k        # 他のメソッドからも self.k でアクセスできる
        self.heap = []
```

---

## 解いた問題

### Kth Largest Element in a Stream（Top K パターン）
> **「ストリームからK番目に大きい要素を常に返す」→ Top K → ヒープ！**

サイズkの最小ヒープを維持。新しい要素が来たら追加し、サイズがk超えたら最小を捨てる。先頭がK番目に大きい要素。

📂 [KthLargestElement.py](../NeetCode150/easy/KthLargestElement.py)

---

### Last Stone Weight（毎回最大2つを取る）
> **「最も重い2つの石をぶつけ続ける」→ 常に最大を取り出す → ヒープ！**

最大ヒープ（符号反転）で最大2つを取り出し、差を戻す。（ソートで解くこともできる）

📂 [LastStoneWeight.py](../NeetCode150/easy/LastStoneWeight.py)
