# Python Syntax Guide (Backtracking)

Combination Sumの問題で活用した、Pythonの標準的なリスト操作と関数の書き方についてのガイドです。

## 1. リストの標準メソッド

### `.append(x)`
リストの**末尾**に要素を追加します。
```python
path = [2, 3]
path.append(5) # path は [2, 3, 5] になる
```

### `.pop()`
リストの**末尾**から要素を1つ取り除きます。バックトラッキングにおいて「一歩戻る」操作として使われます。
```python
path = [2, 3, 5]
path.pop() # path は [2, 3] に戻る
```

### `.copy()`
リストの「複製」を作成します。
```python
ans.append(path.copy())
```
> [!IMPORTANT]
> `ans.append(path)` と書くと、`path` の「場所」が保存されるため、後で `path` が変更されると `ans` の中身も変わってしまいます。`.copy()` はその瞬間の状態を固定して保存するために必須です。

---

## 2. 関数内関数（Nested Functions）

関数の中で別の関数を定義する手法です。

```python
def combinationSum(self, candidates, target):
    ans = [] # 全員で共有する答えの箱
    
    def backtrack(i, cur, total):
        # 1. 外側の変数 (ans, candidates, target) に直接アクセスできる
        # 2. この関数の中からしか呼び出せないので、安全
        ...
    
    # ここが着火ボタン！初期値を渡して呼び出す
    backtrack(0, [], 0) 
    return ans
```

### なぜわざわざ分けるの？
- **引数の「口」を増やすため**: LeetCodeの指定（`candidates`, `target`）以外の変数（`i`, `cur`, `total`）を管理したい。
- **リセットを防ぐため**: メイン関数を再帰させると、呼び出しのたびに `ans = []` が実行されて答えが消えてしまう。

---

## 3. 引数の動き（初期化と更新）

### 初期値の入り方
一番下の `backtrack(0, [], 0)` が実行された瞬間、各引数に最初の値がセットされます。
- `i` ← `0` (最初の数字からスタート)
- `cur` ← `[]` (中身は空っぽ)
- `total` ← `0` (合計は0)

### 引数の「進化」
再帰呼び出しの中で、引数を少しずつ変えて次へと繋いでいきます。
```python
# 「今の数字を使う」とき：合計 score を増やして、カゴはそのまま渡す
backtrack(i, cur, total + candidates[i])

# 「次の数字へ行く」とき：i を進めて、カゴも合計も今のまま渡す
backtrack(i + 1, cur, total)
```
この「呼び出すたびに値が更新される」仕組みによって、迷路を進むように探索が行われます。
