# 🎯 Blind75 Easy 問題まとめ

このファイルは Blind75 の Easy 問題の解き方、使用したアルゴリズム、Ruby の構文をまとめたものです。

---

## 📊 カテゴリ別一覧

| カテゴリ | 問題 |
|----------|------|
| **配列 (Array)** | Two Sum, Contains Duplicate, Best Time to Buy and Sell Stock, Missing Number |
| **文字列 (String)** | Valid Anagram, Valid Palindrome, Longest Substring |
| **リンクドリスト (Linked List)** | Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle |
| **二分木 (Binary Tree)** | Invert Binary Tree, Same Tree, Subtree of Another Tree |
| **動的計画法 (DP)** | Climbing Stairs |
| **スタック (Stack)** | Valid Parentheses |
| **ビット操作 (Bit Manipulation)** | Number of 1 Bits, Reverse Bits, Counting Bits |

---

## 🔥 アルゴリズム別まとめ

### 1. ハッシュテーブル (Hash)
**問題**: Two Sum, Valid Anagram, Contains Duplicate

```ruby
# 基本的なハッシュの使い方
hash = {}
hash[key] = value
hash.key?(key)  # キーが存在するか確認 O(1)

# 初期値付きハッシュ
count = Hash.new(0)  # 存在しないキーは0を返す
count['a'] += 1
```

**ポイント**:
- ハッシュの検索は O(1) で高速
- 「補数を探す」パターンが頻出（Two Sum）
- 文字の出現回数カウントに便利

---

### 2. スライディングウィンドウ (Sliding Window)
**問題**: Longest Substring Without Repeating Characters

```ruby
left = 0
max_length = 0
char_set = Set.new

(0...s.length).each do |right|
    while char_set.include?(s[right])
        char_set.delete(s[left])
        left += 1
    end
    char_set.add(s[right])
    max_length = [max_length, right - left + 1].max
end
```

**ポイント**:
- 2つのポインタ（left, right）でウィンドウを管理
- 条件を満たさなくなったら left を縮める

---

### 3. 二分木の再帰 (Tree Recursion)
**問題**: Same Tree, Invert Binary Tree, Subtree of Another Tree

```ruby
def is_same_tree(p, q)
    return true if p.nil? && q.nil?   # 両方nil → 同じ
    return false if p.nil? || q.nil?  # 片方だけnil → 違う
    return false if p.val != q.val    # 値が違う → 違う
    
    # 左右を再帰的にチェック
    is_same_tree(p.left, q.left) && is_same_tree(p.right, q.right)
end
```

**ポイント**:
- ベースケース: `nil` のチェック
- 再帰: 左右の子ノードに同じ処理を適用
- `&&` や `||` で結果を組み合わせる

---

### 4. リンクドリストの操作
**問題**: Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle

```ruby
# リバース（ポインタの付け替え）
def reverse_list(head)
    prev = nil
    current = head
    while current
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    end
    prev
end
```

**ポイント**:
- `prev`, `current`, `next_node` の3つのポインタ
- Dummy Node パターン（Merge用）

#### うさぎとかめ（Floyd's Cycle Detection）
```ruby
def hasCycle(head)
    slow = fast = head
    while fast && fast.next
        slow = slow.next
        fast = fast.next.next
        return true if slow == fast
    end
    false
end
```

---

### 5. 動的計画法 (Dynamic Programming)
**問題**: Climbing Stairs

```ruby
def climb_stairs(n)
    return n if n <= 2
    one_step_before = 2
    two_steps_before = 1
    
    (3..n).each do
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current
    end
    one_step_before
end
```

**ポイント**:
- フィボナッチ数列と同じ考え方
- `f(n) = f(n-1) + f(n-2)`
- 空間を O(1) に最適化できる

---

### 6. スタック (Stack)
**問題**: Valid Parentheses

```ruby
stack = []
stack.push(item)   # 追加
stack.pop          # 取り出し
stack.empty?       # 空かチェック
```

**ポイント**:
- LIFO (Last In, First Out)
- 括弧の対応チェックに最適

---

### 7. ビット操作 (Bit Manipulation)
**問題**: Number of 1 Bits, Reverse Bits, Counting Bits

```ruby
# 2進数変換
n.to_s(2)              # 整数を2進数文字列に
"1010".to_i(2)         # 2進数文字列を整数に

# 1の数を数える
n.to_s(2).count('1')

# 32ビットに揃える
n.to_s(2).rjust(32, '0')
```

---

### 8. 数学的アプローチ
**問題**: Missing Number

```ruby
# 等差数列の和の公式
expected_sum = n * (n + 1) / 2
actual_sum = nums.sum
missing = expected_sum - actual_sum
```

---

## 📝 Ruby 構文まとめ

### 配列操作
```ruby
nums.length           # 長さ
nums.sum              # 合計
nums.sort             # ソート
nums.uniq             # 重複削除
nums.include?(x)      # 要素が含まれるか
nums.min / nums.max   # 最小/最大
[a, b].min            # 2つの値の最小
```

### 文字列操作
```ruby
s.chars               # 文字の配列に変換
s.each_char { |c| }   # 1文字ずつ処理
s.gsub(/pattern/, "") # 正規表現で置換
s.downcase            # 小文字に
s.reverse             # 逆順
s.rjust(n, '0')       # 右寄せでパディング
```

### 繰り返し
```ruby
nums.each { |num| }              # 各要素
nums.each_with_index { |num, i| }# インデックス付き
(0..n).each { |i| }              # 0からn（含む）
(0...n).each { |i| }             # 0からn-1
```

### ハッシュ
```ruby
hash = {}
hash = Hash.new(0)    # 初期値0
hash.key?(k)          # キー存在確認
hash.values           # 値の配列
hash.values.all? { |v| v == 0 }  # 全て条件を満たすか
```

### よく使うパターン
```ruby
# ガード節
return nil if root.nil?
return false if s.length != t.length

# 多重代入（スワップ）
a, b = b, a
root.left, root.right = root.right, root.left

# 三項演算子的な使い方
result = condition ? value1 : value2

# ||= (nilなら代入)
x ||= default_value
```

---

## ⏱️ 計算量まとめ

| 問題 | 時間 | 空間 | 理由 |
|------|------|------|------|
| Two Sum | O(n) | O(n) | ハッシュで1回走査 |
| Contains Duplicate | O(n) | O(n) | uniqで重複チェック |
| Valid Anagram | O(n) | O(1) | 文字種は固定なので |
| Valid Parentheses | O(n) | O(n) | スタック使用 |
| Climbing Stairs | O(n) | O(1) | 変数2つのみ |
| Best Time to Buy | O(n) | O(1) | 1回走査 |
| Linked List Cycle | O(n) | O(1) | ポインタ2つのみ |
| Tree系 | O(n) | O(h) | h=木の高さ（再帰） |

---

## 🎓 学んだこと

1. **ハッシュは最強**: 検索 O(1) を活用して計算量を下げる
2. **再帰はベースケースから**: `nil` チェックを最初に
3. **ポインタの管理**: Linked List は `prev`, `current`, `next` の3つ
4. **数学的発想**: 公式を知っていると一発で解ける（Missing Number）
5. **スタックはLIFO**: 括弧の対応に最適
