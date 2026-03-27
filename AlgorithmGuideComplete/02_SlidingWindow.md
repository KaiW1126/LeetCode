# 🩵 スライディングウィンドウ（Sliding Window）

## どんなアルゴリズム？

配列や文字列の上に **「窓（ウィンドウ）」** を置き、その窓を **右にスライド** させながら条件を満たす範囲を探す手法。
窓の右端を広げて要素を追加し、条件を満たさなくなったら左端を縮めて調整する。

```
例: "abcabcbb" から重複なしの最長部分文字列を探す
  [a]bcabcbb     → 窓: "a"（長さ1）
  [ab]cabcbb     → 窓: "ab"（長さ2）
  [abc]abcbb     → 窓: "abc"（長さ3）
  a[bca]bcbb     → 次の "a" が重複 → 左端を縮める → 窓: "bca"（長さ3）
  ...繰り返し
```

**イメージ**: 「電車の窓から景色を見る」 — 窓の大きさを伸び縮みさせながら、条件に合う一番良い景色（範囲）を見つける。

---

## こう聞かれたらスライディングウィンドウ！

| キーワード | 例 |
|---|---|
| **「連続する部分配列/部分文字列」** | Maximum Subarray, Min Window Substring |
| **「最長の〇〇な部分文字列」** | Longest Substring Without Repeating Characters |
| **「k個の連続する要素」** | - |

---

## 見分けるコツ

```
✅ スライディングウィンドウの2つのサイン:
  1. 「連続する」範囲を扱う
  2. 左端と右端を動かして「窓」のサイズを調整する

❌ スライディングウィンドウではないサイン:
  ・連続していない要素を選ぶ → DP
  ・順番を変えてもOK → ソート/ハッシュ
```

---

## Python での書き方

### 基本テンプレート（可変長ウィンドウ）
```python
def sliding_window(s):
    left = 0
    result = 0
    window = set()  # or dict() で状態管理

    for right in range(len(s)):
        # 1. 右端の要素を追加
        while s[right] in window:  # 条件違反
            # 2. 左端を縮めて条件を回復
            window.remove(s[left])
            left += 1
        window.add(s[right])

        # 3. 結果を更新
        result = max(result, right - left + 1)

    return result
```

### 固定長ウィンドウ
```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])  # 最初のk個
    result = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # 右を追加、左を削除
        result = max(result, window_sum)

    return result
```

### Python 構文ポイント
```python
# set で重複管理
char_set = set()
char_set.add(x)       # 追加
char_set.remove(x)    # 削除
x in char_set          # O(1) で存在確認

# dict で頻度管理
from collections import defaultdict
freq = defaultdict(int)
freq[x] += 1           # カウントアップ
freq[x] -= 1           # カウントダウン
```

---

## 解いた問題

### Longest Palindromic Substring（中心拡張法）
> 厳密にはスライディングウィンドウではないが、**「左右に窓を広げる」** という発想が共通。

各文字を中心に左右に拡張し、回文である限り広げ続ける。奇数長・偶数長の両方を試す。

📂 [LongestPlindromicSubstring.py](../Blind75/Python/Medium/LongestPlindromicSubstring.py)

---

### Longest Consecutive Sequence（ハッシュセット応用）
> setを使って連続する数列の開始点を見つけ、そこから連続する限りカウントする。

「前の数が存在しない」= 開始点として、右方向にウィンドウを広げていくイメージ。

📂 [Longest ConsecutiveSequence.py](../Blind75/Python/Medium/Longest%20ConsecutiveSequence.py)

---

## 関連アルゴリズム

- 2ポインタとの違い: スライディングウィンドウは **連続する範囲** を扱う。2ポインタは **ペアを探す** ことが多い
- DPとの違い: 連続しない要素を選ぶ場合はDP
