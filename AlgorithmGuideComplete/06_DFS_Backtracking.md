# 🔴 DFS（深さ優先探索）& 🟠 バックトラッキング

## どんなアルゴリズム？

**DFS（深さ優先探索）**: 1本の道を **行けるところまで深く進み**、行き止まりになったら **1歩戻って別の道** を試す探索法。

**バックトラッキング**: DFSの応用。途中で **「この道は条件を満たさない」と分かった時点で引き返す**（枝刈り）。

```
      A
     / \
    B   C
   / \   \
  D   E   F

DFS:   A → B → D（行き止まり）→ 戻る → E → 戻る → C → F
       → 「深く潜ってから戻る」動き

バックトラッキング（例: 「Fへのパスを探す」）:
  A → B → D（Fじゃない → 戻る）→ E（Fじゃない → 戻る）
    → C → F（見つけた！）
  → 条件に合わない枝を早めに切るので効率的
```

**イメージ**: 「迷路を片手で壁を触りながら進む」 — 行き止まりになったら来た道を戻って別の分岐を試す。

---

## こう聞かれたらDFS / バックトラッキング！

| キーワード | 例 |
|---|---|
| **「全パターン列挙」** | Subsets, Permutations, Combination Sum |
| **「パスが存在するか」**（グリッド/グラフ） | Word Search, Number of Islands |
| **「木の探索」** | Maximum Depth, Validate BST |

---

## DFS vs バックトラッキングの違い

```
DFS: 全ノードを訪問する
  → Number of Islands（全マスを見る）
  → Clone Graph（全ノードをコピー）

バックトラッキング: 条件に合わないルートを早めに切る
  → Word Search（文字が違ったら戻る）
  → Combination Sum（組み合わせを生成して戻す）
```

---

## Python での書き方

### DFS 基本テンプレート（グラフ）
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)

    # ノードの処理
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

### DFS（グリッド探索）
```python
def dfs(grid, i, j):
    # 範囲外チェック or 条件チェック
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j] == '0':  # 既に訪問済み or 条件外
        return

    grid[i][j] = '0'  # 訪問済みマーク

    # 上下左右を探索
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
```

### バックトラッキング テンプレート
```python
def backtrack(candidates, target, start, current, result):
    # ベースケース: 目標達成
    if target == 0:
        result.append(current.copy())  # ← .copy() が重要！
        return

    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break  # 枝刈り

        current.append(candidates[i])                        # 選ぶ
        backtrack(candidates, target - candidates[i],        # 探索
                  i, current, result)
        current.pop()                                        # 戻す（バックトラック）
```

### Python 構文ポイント（重要！）
```python
# .copy() vs 参照
result.append(current.copy())  # ✅ 現在の状態のコピーを保存
result.append(current)          # ❌ 参照なので後で変わってしまう！

# リスト操作
current.append(x)   # 末尾に追加
current.pop()        # 末尾を削除（バックトラック）

# ネスト関数（クロージャ）でresultを共有
def solve():
    result = []
    def backtrack(start, current):
        result.append(current.copy())  # 外側のresultにアクセス
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result
```

---

## 解いた問題

### Combination Sum（バックトラッキング）
> **「合計がtargetになる組み合わせを全て列挙」→ 全パターン → バックトラッキング！**

候補から数を選び、targetに達したらコピーを保存、超えたら戻る。同じ数を何度でも使える。

📂 [CombinationSum.py](../Blind75/Python/Medium/CombinationSum.py)

---

### Word Search（DFS + バックトラッキング）
> **「グリッドに単語が存在するか？」→ パス探索 → DFS + バックトラッキング！**

各マスからDFS開始。訪問済みを`#`でマークし、探索後に元に戻す（バックトラック）。

📂 [WordSearch.py](../Blind75/Python/Medium/WordSearch.py)

---

### Clone Graph（DFS + メモ化）
> **「グラフ全体を深いコピー」→ 全ノード訪問 → DFS！**

DFSで各ノードを訪問し、コピーを辞書に保存。既に訪問済みなら辞書から返す。

📂 [CloneGraph.py](../Blind75/Python/Medium/CloneGraph.py)

---

### Validate Binary Search Tree（DFS - 範囲チェック）
> **「有効なBSTか判定」→ 木の探索 → DFS（再帰）！**

各ノードに有効な範囲（lower, upper）を持たせて再帰的に検証。

📂 [ValidateBinarySearch.py](../Blind75/Python/Medium/ValidateBinarySearch.py)

---

### Diameter of Binary Tree（DFS - ポストオーダー）
> **「木の直径（最長パス）を求める」→ 木の探索 → DFS！**

各ノードで左右の高さを求め、`左の高さ + 右の高さ` の最大値が直径。

📂 [DiameterBinaryTree.py](../NeetCode150/easy/DiameterBinaryTree.py)

---

### Balanced Binary Tree（DFS - 高さチェック）
> **「平衡木か判定」→ 木の探索 → DFS！**

各ノードで左右の高さ差が1以下か再帰的にチェック。

📂 [BalancedBinary.py](../NeetCode150/easy/BalancedBinary.py)
