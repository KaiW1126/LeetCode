# 🌳 木構造（Tree）

## どんなデータ構造？

ノード（節）とエッジ（枝）で構成される **階層的なデータ構造**。最も頻出なのは **二分木（Binary Tree）** で、各ノードが最大2つの子を持つ。

```
        1          ← ルート（根）
       / \
      2   3        ← 子ノード
     / \   \
    4   5   6      ← 葉ノード（子がない）

二分探索木（BST）の性質:
  ・左の子 < 親 < 右の子
  ・この性質がすべてのノードで成り立つ
```

**イメージ**: 「家系図」 — 一人の祖先（ルート）から子、孫と分岐していく構造。

---

## よく出るパターン

| パターン | 例題 |
|---|---|
| **再帰で木を走査** | Same Tree, Invert Binary Tree |
| **高さ/深さを求める** | Balanced Binary Tree, Diameter |
| **BSTの性質を利用** | Validate BST |
| **レベルごと探索（BFS）** | Level Order Traversal |
| **木の構築** | Construct from Preorder + Inorder |

---

## 走査の3パターン

```
        1
       / \
      2   3

前順（Preorder）:  ルート → 左 → 右  → 1, 2, 3
中順（Inorder）:   左 → ルート → 右  → 2, 1, 3  ← BSTでは昇順になる！
後順（Postorder）: 左 → 右 → ルート  → 2, 3, 1
```

---

## Python での書き方

### ノード定義
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 再帰テンプレート（ほぼ全ての木の問題で使う）
```python
def solve(root):
    # ベースケース: ノードがない
    if not root:
        return 0  # or None, True, [] など

    # 左右の部分木を再帰的に処理
    left_result = solve(root.left)
    right_result = solve(root.right)

    # 現在のノードでの計算
    return some_combination(left_result, right_result, root.val)
```

### 高さを求める
```python
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
```

### BST検証（範囲を引き継ぐ）
```python
def is_valid_bst(root, lower=float('-inf'), upper=float('inf')):
    if not root:
        return True
    if root.val <= lower or root.val >= upper:
        return False
    return (is_valid_bst(root.left, lower, root.val) and
            is_valid_bst(root.right, root.val, upper))
```

### 木の構築（Preorder + Inorder）
```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)  # ルートの位置

    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])

    return root
```

### Python 構文ポイント
```python
# None チェック（最重要！）
if not root:          # root が None なら True
if not root.left:     # 左の子がない

# 無限大
float('inf')          # 正の無限大
float('-inf')         # 負の無限大

# 再帰の返り値を and/or で組み合わせ
return solve(root.left) and solve(root.right)

# max/min で高さや直径を計算
return 1 + max(height(root.left), height(root.right))
```

---

## 解いた問題

### Validate Binary Search Tree（BST検証）
> **「有効なBSTか判定」→ 各ノードに有効範囲（lower, upper）を持たせて再帰**

左に進むとき upper を、右に進むとき lower を現在の値で更新。

📂 [ValidateBinarySearch.py](../Blind75/Python/Medium/ValidateBinarySearch.py)

---

### Binary Tree Level Order Traversal（BFSでレベルごと）
> **「各レベルのノードをリストで返す」→ BFS + キュー**

`deque` でキューを作り、各レベルのノード数分だけ処理して次レベルへ。

📂 [BinaryTreeLevelOrder.py](../Blind75/Python/Medium/BinaryTreeLevelOrder.py)

---

### Construct Binary Tree from Preorder and Inorder
> **「2つの走査結果から木を構築」→ preorder[0] がルート、inorder で左右を分割**

preorder の先頭がルート。inorder でルートの位置を見つけ、左右の部分木に分割して再帰。

📂 [ConstructBinaryTree.py](../Blind75/Python/Medium/ConstructBinaryTree.py)

---

### Diameter of Binary Tree（木の直径）
> **「最長パスの辺の数」→ 各ノードで左の高さ + 右の高さの最大値**

ポストオーダーで各ノードの高さを求めつつ、`左高さ + 右高さ` の最大値を追跡。

📂 [DiameterBinaryTree.py](../NeetCode150/easy/DiameterBinaryTree.py)

---

### Balanced Binary Tree（平衡木判定）
> **「左右の高さの差が1以下か」→ 再帰で高さを求めつつチェック**

📂 [BalancedBinary.py](../NeetCode150/easy/BalancedBinary.py)

---

### Clone Graph（グラフのディープコピー）
> **「グラフ全体を複製」→ DFS + 辞書でコピー済みノードを管理**

📂 [CloneGraph.py](../Blind75/Python/Medium/CloneGraph.py)
