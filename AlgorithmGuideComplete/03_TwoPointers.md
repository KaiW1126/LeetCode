# 🩷 2ポインタ（Two Pointers）

## どんなアルゴリズム？

配列上に **2つの指（ポインタ）を置き**、それぞれを独立に動かしながら目的の条件を探す手法。
主に2パターンある:

```
パターン①: 左右から挟む（向かい合わせ）
  [1, 2, 3, 4, 5, 6, 7]
   L→              ←R     L と R を中央に向けて近づける
  → 合計がXになるペアを探す、水の最大面積など

パターン②: 同じ方向に進む（追いかけっこ）
  [1, 1, 2, 2, 3, 3, 4]
   S→
   F→                     S（遅い）と F（速い）が同じ方向に進む
  → 重複の削除、リンクリストのサイクル検出など
```

**イメージ**: 「両手の指で挟んで探す」 — 本の両端にしおりを置いて、条件に合うページを探すように中央に向かって近づけていく。

---

## こう聞かれたら2ポインタ！

| キーワード | 例 |
|---|---|
| **「ペアを見つける」**（ソート済み配列） | Two Sum II, 3Sum |
| **「回文かどうか」** | Valid Palindrome |
| **「マージする」**（2つのソート済み配列） | Merge Sorted Array |
| **「水の量 / 面積」**（棒グラフ系） | Container With Most Water |

---

## 見分けるコツ

```
✅ 2ポインタの2つのサイン:
  1. ソート済み配列 or 両端から攻める
  2. O(n²) を O(n) に最適化したい

パターン:
  ・左右から挟む → Container With Most Water
  ・同じ方向に進む → Remove Duplicates
```

---

## Python での書き方

### パターン①: 左右から挟む
```python
def two_pointer_converge(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1       # 合計が小さい → 左を右へ
        else:
            right -= 1      # 合計が大きい → 右を左へ

    return []
```

### パターン②: ソート + 2ポインタ（3Sum）
```python
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # 重複スキップ

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1   # 重複スキップ
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # 重複スキップ
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

### Python 構文ポイント
```python
# ソート
nums.sort()                    # インプレース（元の配列を変更）
sorted_nums = sorted(nums)    # 新しいリストを返す

# 多重代入（スワップ）
a, b = b, a
left, right = 0, len(nums) - 1
```

---

## 解いた問題

### Container With Most Water（左右から挟む）
> **「最も多くの水を溜められる2本の線は？」→ 面積最大 → 2ポインタ！**

左右のポインタで面積を計算し、短い方のポインタを内側に移動。短い方を動かす理由: 高さが制約なので、幅を狭くしても高さが上がる可能性がある方を動かす。

📂 [ContainerWater.py](../Blind75/Python/Medium/ContainerWater.py)

---

### 3Sum（ソート + 2ポインタ）
> **「3つの数の和が0になる組み合わせは？」→ ペア探し → ソート + 2ポインタ！**

配列をソートし、1つ目の数を固定して残り2つを2ポインタで探す。重複スキップが重要。

📂 [3sum.py](../Blind75/Python/Medium/3sum.py)

---

### Remove Nth Node From End（2ポインタ - リンクドリスト）
> **「後ろからN番目のノードを削除」→ 2ポインタでN個分の差をつける**

fastポインタをN+1歩先に進め、fastとslowを同時に動かす。fastが末尾に到達したとき、slowが削除対象の前にいる。

📂 [RemoveNthNode.py](../Blind75/Python/Medium/RemoveNthNode.py)

---

### Merge Strings Alternately（同方向2ポインタ）
> **2つの文字列を交互にマージする**

2つのポインタを同時に進めながら、交互に文字を追加。残りがあれば末尾に追加。

📂 [MergeStrings.py](../Blind75/Python/Easy/MergeStrings.py)
