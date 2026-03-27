# 🔗 リンクドリスト（Linked List）

## どんなデータ構造？

各要素（ノード）が **値** と **次のノードへのポインタ** を持つ線形データ構造。
配列と違い、メモリ上で連続している必要がなく、挿入・削除が O(1) でできる。

```
配列:   [1] [2] [3] [4] [5]  ← メモリ上で連続
リスト:  1 → 2 → 3 → 4 → 5 → None  ← ポインタで繋がる

メリット: 挿入/削除が O(1)（ポインタ付け替えだけ）
デメリット: ランダムアクセスが O(n)（先頭から辿る必要がある）
```

**イメージ**: 「宝探しの手がかりカード」 — 各カードに次のカードの場所が書いてあり、順番に辿って最後の宝にたどり着く。

---

## よく使うパターン

| パターン | 用途 |
|---|---|
| **ポインタ付け替え** | リバース、ノード削除 |
| **ダミーノード** | 先頭が変わる操作を簡潔に |
| **2ポインタ（fast/slow）** | サイクル検出、N番目のノード |

---

## Python での書き方

### ノード定義
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### リバース（ポインタ付け替え）
```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next    # 次を保存
        current.next = prev         # ポインタを逆転
        prev = current              # prevを進める
        current = next_node         # currentを進める

    return prev  # 新しい先頭
```

### ダミーノード + 2ポインタ（N番目のノード削除）
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)  # ダミーノード
    fast = slow = dummy

    # fastをn+1歩先に進める
    for _ in range(n + 1):
        fast = fast.next

    # fastとslowを同時に進める
    while fast:
        fast = fast.next
        slow = slow.next

    # slowの次のノードを削除
    slow.next = slow.next.next

    return dummy.next
```

### サイクル検出（Floyd's Algorithm）
```python
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next            # 1歩
        fast = fast.next.next       # 2歩
        if slow == fast:
            return True             # 追いついた = サイクルあり

    return False
```

### Python 構文ポイント
```python
# None チェック
if not head:          # head が None なら True
if not head.next:     # 次がない = 末尾

# ダミーノードの使い方
dummy = ListNode(0, head)  # 本来の先頭の前にダミーを置く
return dummy.next           # ダミーの次 = 本当の先頭を返す

# 多重代入でスワップ
prev, current = current, next_node
```

---

## 解いた問題

### Remove Nth Node From End of List（ダミーノード + 2ポインタ）
> **「後ろからN番目のノードを削除」→ 2ポインタでN個の差をつける**

fastをN+1歩先に進め、fastとslowを同時に動かす。fastが末尾に到達したとき、slowが削除対象の前にいる。

📂 [RemoveNthNode.py](../Blind75/Python/Medium/RemoveNthNode.py)
