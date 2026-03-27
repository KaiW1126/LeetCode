# 🔵 BFS（幅優先探索 / Breadth-First Search）

## どんなアルゴリズム？

スタート地点から **近い順に（1歩ずつ広がるように）** 全ノードを探索する手法。**キュー（FIFO: 先入れ先出し）** を使う。
最短経路を見つけるのに最適（重みなしグラフの場合）。

```
      A
     / \
    B   C
   / \   \
  D   E   F

BFS:
  レベル0: A
  レベル1: B, C         ← Aの隣を全部見る
  レベル2: D, E, F      ← B,Cの隣を全部見る
  → 「浅い層から順に全部見る」動き

※ DFSとの違い:
  DFS: A→B→D→E→C→F （深さ優先 = 1本の道を深く掘る）
  BFS: A→B→C→D→E→F （幅優先 = 各層を横に広く見る）
```

**イメージ**: 「池に石を投げたときの波紋」 — 中心から同心円状に広がるように、近い場所から順に探索する。

---

## こう聞かれたらBFS！

| キーワード | 例 |
|---|---|
| **「最短距離/最短手数」** | Shortest Path in Grid |
| **「レベルごと」**（木） | Binary Tree Level Order Traversal |
| **「近い順に探索」** | - |

---

## 見分けるコツ

```
✅ BFSのサイン:
  1. 「最短」を求める（重みなしグラフ）
  2. レベル（深さ）ごとに処理したい
  3. 「近い順」に広がる探索
```

---

## Python での書き方

### 基本テンプレート（レベルごと探索）
```python
from collections import deque

def bfs_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)  # 現在のレベルのノード数

        for _ in range(level_size):
            node = queue.popleft()     # キューの先頭から取り出し
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

### グラフのBFS
```python
from collections import deque

def bfs_graph(start, graph):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Python 構文ポイント
```python
from collections import deque

# deque（デック）= 両端キュー
queue = deque()
queue.append(x)      # 右端に追加 O(1)
queue.popleft()       # 左端から取り出し O(1)
# ※ list の pop(0) は O(n) なので deque を使う！

len(queue)            # キューのサイズ
```

---

## 解いた問題

### Binary Tree Level Order Traversal（レベルごと探索）
> **「木の各レベルのノードをリストで返す」→ レベルごと → BFS！**

キューを使い、各レベルのノード数分だけ取り出して処理。子ノードをキューに追加して次のレベルへ。

📂 [BinaryTreeLevelOrder.py](../Blind75/Python/Medium/BinaryTreeLevelOrder.py)

---

## DFS vs BFS の使い分け

| 状況 | DFS | BFS |
|---|---|---|
| 最短経路を求める | ❌ | ✅ |
| 全パターン列挙 | ✅ | ❌ |
| レベルごとの処理 | ❌ | ✅ |
| メモリ効率（深い木） | ✅ | ❌ |
| メモリ効率（広い木） | ❌ | ✅ |
