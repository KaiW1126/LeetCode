# 🟡 二分探索（Binary Search）

## どんなアルゴリズム？

**ソート済みのデータ** を半分ずつ切り捨てながら目的の値を探す手法。毎回データを半分にするので **O(log n)** という超高速な探索ができる。

```
例: ソート済み配列 [1, 3, 5, 7, 9, 11, 13] から「9」を探す
  → 真ん中は 7。9 > 7 なので右半分だけ見る → [9, 11, 13]
  → 真ん中は 11。9 < 11 なので左半分だけ見る → [9]
  → 見つかった！（たった3回の比較）

※ 全部見る場合: 最大7回 → 二分探索: 最大3回
  要素が100万個でも → 二分探索: 最大20回！
```

**イメージ**: 「辞書で単語を引く」 — 真ん中のページを開き、探す単語がそれより前か後かで半分に絞る。

---

## こう聞かれたら二分探索！

| キーワード | 例 |
|---|---|
| **「ソート済み配列で探す」** | Search in Rotated Sorted Array |
| **「O(log n) で解け」** | Find Minimum in Rotated Sorted Array |
| **「〇〇の最小値/最大値を探せ」**（答えに対する二分探索） | Koko Eating Bananas |

---

## 見分けるコツ

```
✅ 二分探索のサイン:
  1. ソート済み（or 部分的にソート済み）
  2. 「探す」がメイン
  3. O(log n) が求められる

💡 ソートされてなくても:
  「答えの範囲」が分かっていて、答えに対して二分探索できる場合もある
```

---

## Python での書き方

### 基本テンプレート
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1    # 右半分を探す
        else:
            right = mid - 1   # 左半分を探す

    return -1  # 見つからなかった
```

### 回転ソート配列の二分探索
```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # 左半分がソート済みか判定
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1   # 左半分にある
            else:
                left = mid + 1    # 右半分にある
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1    # 右半分にある
            else:
                right = mid - 1   # 左半分にある

    return -1
```

### Python 構文ポイント
```python
# 整数除算（切り捨て）
mid = (left + right) // 2

# while left <= right: ← 「=」を忘れるとバグる！
# left = mid + 1, right = mid - 1: ← mid自体は除外する
```

---

## 解いた問題

### Binary Search（基本）
> **ソート済み配列からターゲットを探す → 基本の二分探索**

left, right, mid の3ポインタで半分ずつ絞り込む。O(log n)。

📂 [BinarySearch.py](../NeetCode150/easy/BinarySearch.py)

---

### Search in Rotated Sorted Array（応用）
> **回転したソート済み配列から探す → 「どちらがソート済みか」を判定して二分探索**

`nums[left] <= nums[mid]` で左半分がソート済みか判定し、targetがその範囲内かで探索方向を決める。

📂 [SearchRotatedSortedArray.py](../Blind75/Python/Medium/SearchRotatedSortedArray.py)
