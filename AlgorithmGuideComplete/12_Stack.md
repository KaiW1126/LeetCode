# 📚 スタック（Stack）

## どんなデータ構造？

**LIFO（Last In, First Out）** — 最後に入れたものが最初に出てくるデータ構造。
皿を積み重ねたイメージ: 上に置いたものを先に取る。

```
push 1: [1]
push 2: [1, 2]
push 3: [1, 2, 3]
pop:    [1, 2]     ← 3が取り出される（最後に入れたもの）
pop:    [1]        ← 2が取り出される
```

**イメージ**: 「エレベーターの人」 — 最後に乗った人が最初に降りる。

---

## こう聞かれたらスタック！

| キーワード | 例 |
|---|---|
| **「括弧の対応」** | Valid Parentheses |
| **「直前の要素と比較」** | Monotonic Stack 系 |
| **「入れ子構造」** | ネストした括弧、HTML タグ |
| **「元に戻す（Undo）」** | - |

---

## Python での書き方

### 基本操作（リストで代用）
```python
stack = []
stack.append(item)    # push: 末尾に追加 O(1)
stack.pop()           # pop: 末尾を取り出し O(1)
stack[-1]             # peek: 末尾を参照（取り出さない）
not stack             # 空チェック（True なら空）
len(stack)            # サイズ
```

### 括弧チェックパターン
```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs:
            # 閉じ括弧 → スタックの先頭と対応するか確認
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            # 開き括弧 → スタックに追加
            stack.append(char)

    return not stack  # 空なら全て対応OK
```

### Python 構文ポイント
```python
# リストをスタックとして使う
# ※ .pop() は O(1)（末尾）
# ※ .pop(0) は O(n)（先頭）← これはキュー（deque を使うべき）

# 辞書で対応関係を定義
pairs = {')': '(', ']': '[', '}': '{'}

# not stack: スタックが空なら True
if not stack:
    return False
```

---

## 解いた問題

このリポジトリではスタックを使った問題はPythonGuideで解法を学習済み:

### Valid Parentheses（括弧チェック）
> **「括弧の対応が正しいか」→ 入れ子構造 → スタック！**

開き括弧をスタックに積み、閉じ括弧が来たら先頭と対応するか確認。最後にスタックが空なら正しい。

---

## スタック vs キュー

| | スタック | キュー |
|---|---|---|
| 順序 | LIFO（後入れ先出し） | FIFO（先入れ先出し） |
| Python | `list` | `collections.deque` |
| 用途 | 括弧チェック、DFS | BFS、レベルごと探索 |
