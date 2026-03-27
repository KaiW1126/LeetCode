# 🟢 貪欲法（Greedy）

## どんなアルゴリズム？

各ステップで **「その瞬間の最善の選択」** を取り続ける手法。将来のことは考えず、今一番良いものを選ぶ。
それで全体の最適解が得られる場合に使える（得られない場合はDPが必要）。

```
例: Jump Game（各マスのジャンプ力で最後まで到達できるか？）
  nums = [2, 3, 1, 1, 4]

  貪欲法: 「今到達できる最も遠い地点」を毎回更新するだけ
    位置0: ジャンプ力2 → 最遠=2
    位置1: ジャンプ力3 → 最遠=max(2, 1+3)=4
    → 最遠4 >= 最後のインデックス4 → 到達可能！

❌ 貪欲法が使えない例: Coin Change（最少のコインで金額を作る）
  コイン [1, 3, 4] で 6 を作る
    貪欲法: 4+1+1=3枚 ← 間違い！
    正解:   3+3=2枚   ← DPで求める必要がある
```

**イメージ**: 「目の前の一番大きいお菓子を取る」 — 毎回一番良さそうなものを選ぶだけ。

---

## こう聞かれたら貪欲法！

| キーワード | 例 |
|---|---|
| **「最小の回数で〇〇」** | Jump Game, Jump Game II |
| **「区間のスケジューリング」** | Non-overlapping Intervals, Meeting Rooms |
| **「今の最適な選択 = 全体の最適」** | - |

---

## 見分けるコツ

```
✅ 貪欲法のサイン:
  1. 局所的に最適な選択が全体的にも最適
  2. 一度選んだら戻らない
  3. ソートしてから前から順に処理

⚠️ 注意: 貪欲法 vs DP の判断は難しい
  ・Jump Game → 貪欲法でOK（到達可能範囲を更新するだけ）
  ・Coin Change → 貪欲法はNG（小さい硬貨の組み合わせが必要な場合がある）
```

---

## Python での書き方

### 到達範囲の更新パターン
```python
def can_jump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False          # ここに到達できない
        max_reach = max(max_reach, i + nums[i])

    return True
```

### 区間スケジューリングパターン
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # 開始位置でソート
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:       # 重なっている
            merged[-1][1] = max(merged[-1][1], end)  # マージ
        else:
            merged.append([start, end])  # 新しい区間

    return merged
```

### Python 構文ポイント
```python
# lambda でソート
intervals.sort(key=lambda x: x[0])   # 第1要素でソート
intervals.sort(key=lambda x: x[1])   # 第2要素でソート

# max で最遠更新
max_reach = max(max_reach, i + nums[i])

# リスト末尾へのアクセス
merged[-1]     # 末尾の要素
merged[-1][1]  # 末尾の要素の第2要素
```

---

## 解いた問題

### Jump Game（到達範囲の更新）
> **「最後のインデックスに到達できるか？」→ 到達可能範囲を毎回更新 → 貪欲法！**

各位置で `max_reach` を更新。現在位置が `max_reach` を超えたら到達不可能。

📂 [JumpGame.py](../Blind75/Python/Medium/JumpGame.py)

---

### Merge Intervals（区間のマージ）
> **「重なる区間をマージ」→ ソートして前から順に処理 → 貪欲法！**

開始位置でソートし、前の区間と重なっていたらend を更新してマージ。

📂 [MergeIntervals.py](../Blind75/Python/Medium/MergeIntervals.py)

---

### Insert Interval（区間の挿入 + マージ）
> **「新しい区間を挿入してマージ」→ ソート + 区間マージ**

新しい区間を追加してソートし、Merge Intervals と同じ手法でマージ。

📂 [InsertInterval.py](../Blind75/Python/Medium/InsertInterval.py)

---

### Last Stone Weight（繰り返し最大値を取る）
> **「最も重い2つの石をぶつけ続ける」→ 毎回最大を選ぶ → 貪欲法！**

ソートして最大2つを取り出し、差を戻す。（ヒープでも解ける）

📂 [LastStoneWeight.py](../NeetCode150/easy/LastStoneWeight.py)

---

## よく間違えるパターン

| この問題 | 間違えやすい | 正解 | なぜ？ |
|---|---|---|---|
| Jump Game | DP | 🟢 貪欲法 | 到達可能範囲を更新するだけでOK |
| Coin Change | 貪欲法 | 🟣 DP | 貪欲だと最適解を逃す |
| Container With Most Water | DP | 🩷 2ポインタ | 両端から挟んで最大を探す |
