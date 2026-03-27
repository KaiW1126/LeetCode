# 🔲 行列操作（Matrix Manipulation）

## どんなアルゴリズム？

2次元配列（行列）を扱う問題の総称。特定のアルゴリズムというよりは、**行列特有のテクニック** の集まり。
回転、スパイラル走査、ゼロ埋めなど、行列の構造を理解してインデックスを操作する。

```
例: 行列の90度回転
  元:              回転後:
  [1, 2, 3]       [7, 4, 1]
  [4, 5, 6]  →    [8, 5, 2]
  [7, 8, 9]       [9, 6, 3]

  手順: ① 転置（行と列を入れ替え） → ② 各行を反転
```

---

## よく出るパターン

| パターン | 例題 |
|---|---|
| **回転** | Rotate Image |
| **スパイラル走査** | Spiral Matrix |
| **条件に基づくゼロ埋め** | Set Matrix Zeroes |

---

## Python での書き方

### 行列の転置（行 ↔ 列）
```python
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # 対角線より上だけ
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### 90度回転（転置 + 行反転）
```python
def rotate(matrix):
    n = len(matrix)

    # ① 転置
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # ② 各行を反転
    for row in matrix:
        row.reverse()
```

### スパイラル走査（境界を縮めていく）
```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # → 右へ
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # ↓ 下へ
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # ← 左へ
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        # ↑ 上へ
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```

### Python 構文ポイント
```python
# 行列のサイズ
rows = len(matrix)
cols = len(matrix[0])

# 全マスを走査
for i in range(rows):
    for j in range(cols):
        matrix[i][j]

# 行の反転
row.reverse()          # インプレース
reversed_row = row[::-1]  # 新しいリスト

# 多重代入でスワップ
matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# range の逆順
range(right, left - 1, -1)  # right から left まで（降順）
```

---

## 解いた問題

### Rotate Image（転置 + 行反転）
> **「行列を90度回転（インプレース）」→ 転置して各行を反転**

追加メモリなし（O(1)）で回転できるテクニック。

📂 [RotateImage.py](../Blind75/Python/Medium/RotateImage.py)

---

### Spiral Matrix（スパイラル走査）
> **「行列をスパイラル順に出力」→ 境界を管理して4方向に走査**

top, bottom, left, right の境界を縮めながら、右→下→左→上の順に走査。

📂 [SpiralMatrix.py](../Blind75/Python/Medium/SpiralMatrix.py)

---

### Set Matrix Zeroes（ゼロ位置の記録と埋め）
> **「0がある行と列を全て0にする」→ まず0の位置を記録してから一括処理**

📂 [SetMatrixZeros.py](../Blind75/Python/Medium/SetMatrixZeros.py)
