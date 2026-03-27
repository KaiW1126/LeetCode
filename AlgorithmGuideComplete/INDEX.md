# 🧠 アルゴリズム＆データ構造 完全ガイド

> 各アルゴリズムの解説 × Pythonの書き方 × 解いた問題の実例をまとめた完全ガイド

---

## 📋 目次

### アルゴリズム
| # | ファイル | 解いた問題数 |
|---|---|---|
| 01 | [🟣 動的計画法（DP）](./01_DP.md) | 5問 |
| 02 | [🩵 スライディングウィンドウ](./02_SlidingWindow.md) | 2問 |
| 03 | [🩷 2ポインタ](./03_TwoPointers.md) | 4問 |
| 04 | [🟡 二分探索](./04_BinarySearch.md) | 2問 |
| 05 | [⚪ ハッシュマップ / ハッシュセット](./05_HashMap.md) | 5問 |
| 06 | [🔴 DFS & 🟠 バックトラッキング](./06_DFS_Backtracking.md) | 6問 |
| 07 | [🔵 BFS（幅優先探索）](./07_BFS.md) | 1問 |
| 08 | [🟢 貪欲法](./08_Greedy.md) | 4問 |
| 09 | [🟤 ソート系](./09_Sort.md) | 3問 |

### データ構造
| # | ファイル | 解いた問題数 |
|---|---|---|
| 10 | [⛰️ ヒープ（優先度付きキュー）](./10_Heap.md) | 2問 |
| 11 | [🔗 リンクドリスト](./11_LinkedList.md) | 1問 |
| 12 | [📚 スタック](./12_Stack.md) | 1問（学習済み） |
| 13 | [🔢 ビット操作](./13_BitManipulation.md) | 2問 |
| 14 | [🔲 行列操作](./14_Matrix.md) | 3問 |
| 15 | [🌳 木構造](./15_Tree.md) | 6問 |

---

## 🔀 問題 → アルゴリズム逆引き

> 「この問題、どのアルゴリズム？」と迷ったらここを見る

| 問題文のキーワード | → まず試すアルゴリズム |
|---|---|
| 何通り / 方法の数 | [🟣 DP](./01_DP.md) |
| 最大/最小（累積） | [🟣 DP](./01_DP.md) or [🟢 貪欲法](./08_Greedy.md) |
| 可能か？(True/False) | [🟣 DP](./01_DP.md) or [🟢 貪欲法](./08_Greedy.md) |
| 連続する部分配列/部分文字列 | [🩵 スライディングウィンドウ](./02_SlidingWindow.md) |
| 最長の / 最短の部分文字列 | [🩵 スライディングウィンドウ](./02_SlidingWindow.md) |
| ペアを探す / 合計がXになる | [🩷 2ポインタ](./03_TwoPointers.md) or [⚪ ハッシュ](./05_HashMap.md) |
| ソート済み配列で探す | [🟡 二分探索](./04_BinarySearch.md) |
| O(log n)で解け | [🟡 二分探索](./04_BinarySearch.md) |
| K番目に大きい/小さい、Top K | [⛰️ ヒープ](./10_Heap.md) |
| 含まれるか / 重複 | [⚪ ハッシュ](./05_HashMap.md) |
| 出現回数 / 頻度 | [⚪ ハッシュ](./05_HashMap.md) |
| 全パターン列挙 | [🟠 バックトラッキング](./06_DFS_Backtracking.md) |
| グリッド探索 / 島の数 | [🔴 DFS](./06_DFS_Backtracking.md) |
| 最短距離 / 最短手数 | [🔵 BFS](./07_BFS.md) |
| 区間問題 / スケジューリング | [🟤 ソート](./09_Sort.md) → [🟢 貪欲法](./08_Greedy.md) |
| 木の探索 | [🔴 DFS](./06_DFS_Backtracking.md) or [🔵 BFS](./07_BFS.md) |
| 括弧の対応 | [📚 スタック](./12_Stack.md) |

---

## 📂 解いた問題 一覧（アルゴリズム別）

| 問題名 | アルゴリズム | ファイル |
|---|---|---|
| Decode Ways | DP | [DecodeWays.py](../Blind75/Python/Medium/DecodeWays.py) |
| Word Break | DP | [WordBreak.py](../Blind75/Python/Medium/WordBreak.py) |
| Maximum Subarray | DP (Kadane's) | [MaxSubarray.py](../Blind75/Python/Medium/MaxSubarray.py) |
| Unique Paths | DP / 数学 | [UniquePaths.py](../Blind75/Python/Medium/UniquePaths.py) |
| Min Cost Climbing Stairs | DP | [MInCostStairs.py](../NeetCode150/easy/MInCostStairs.py) |
| Longest Palindromic Substring | 中心拡張 | [LongestPlindromicSubstring.py](../Blind75/Python/Medium/LongestPlindromicSubstring.py) |
| Longest Consecutive Sequence | ハッシュセット | [Longest ConsecutiveSequence.py](../Blind75/Python/Medium/Longest%20ConsecutiveSequence.py) |
| Container With Most Water | 2ポインタ | [ContainerWater.py](../Blind75/Python/Medium/ContainerWater.py) |
| 3Sum | ソート + 2ポインタ | [3sum.py](../Blind75/Python/Medium/3sum.py) |
| Remove Nth Node | 2ポインタ | [RemoveNthNode.py](../Blind75/Python/Medium/RemoveNthNode.py) |
| Merge Strings Alternately | 2ポインタ | [MergeStrings.py](../Blind75/Python/Easy/MergeStrings.py) |
| Binary Search | 二分探索 | [BinarySearch.py](../NeetCode150/easy/BinarySearch.py) |
| Search in Rotated Sorted Array | 二分探索 | [SearchRotatedSortedArray.py](../Blind75/Python/Medium/SearchRotatedSortedArray.py) |
| Group Anagrams | ハッシュマップ | [GroupAnagrams.py](../Blind75/Python/Medium/GroupAnagrams.py) |
| Find Difference of Two Arrays | ハッシュセット | [DifferentTwoArray.py](../Blind75/Python/Easy/DifferentTwoArray.py) |
| Single Number | ハッシュセット / XOR | [SingleNumber.py](../NeetCode150/easy/SingleNumber.py) |
| Happy Number | ハッシュセット | [HappyNumber.py](../NeetCode150/easy/HappyNumber.py) |
| Combination Sum | バックトラッキング | [CombinationSum.py](../Blind75/Python/Medium/CombinationSum.py) |
| Word Search | DFS + バックトラッキング | [WordSearch.py](../Blind75/Python/Medium/WordSearch.py) |
| Clone Graph | DFS + メモ化 | [CloneGraph.py](../Blind75/Python/Medium/CloneGraph.py) |
| Validate BST | DFS (再帰) | [ValidateBinarySearch.py](../Blind75/Python/Medium/ValidateBinarySearch.py) |
| Diameter of Binary Tree | DFS | [DiameterBinaryTree.py](../NeetCode150/easy/DiameterBinaryTree.py) |
| Balanced Binary Tree | DFS | [BalancedBinary.py](../NeetCode150/easy/BalancedBinary.py) |
| Binary Tree Level Order | BFS | [BinaryTreeLevelOrder.py](../Blind75/Python/Medium/BinaryTreeLevelOrder.py) |
| Construct Binary Tree | 再帰 + ハッシュ | [ConstructBinaryTree.py](../Blind75/Python/Medium/ConstructBinaryTree.py) |
| Jump Game | 貪欲法 | [JumpGame.py](../Blind75/Python/Medium/JumpGame.py) |
| Merge Intervals | ソート + 貪欲法 | [MergeIntervals.py](../Blind75/Python/Medium/MergeIntervals.py) |
| Insert Interval | ソート + 貪欲法 | [InsertInterval.py](../Blind75/Python/Medium/InsertInterval.py) |
| Last Stone Weight | ソート / ヒープ | [LastStoneWeight.py](../NeetCode150/easy/LastStoneWeight.py) |
| Kth Largest Element | ヒープ | [KthLargestElement.py](../NeetCode150/easy/KthLargestElement.py) |
| Rotate Image | 行列操作 | [RotateImage.py](../Blind75/Python/Medium/RotateImage.py) |
| Spiral Matrix | 行列操作 | [SpiralMatrix.py](../Blind75/Python/Medium/SpiralMatrix.py) |
| Set Matrix Zeroes | 行列操作 | [SetMatrixZeros.py](../Blind75/Python/Medium/SetMatrixZeros.py) |
| Shuffle Array | ビット操作 | [ShuffleArray.py](../Blind75/Python/Easy/ShuffleArray.py) |
| Array Sign | 数学 | [ArraySign.py](../Blind75/Python/Easy/ArraySign.py) |
| GCD of Strings | 文字列操作 | [DivisorStrings.py](../Blind75/Python/Easy/DivisorStrings.py) |
| Parking System | クラス設計 | [Parkingsystem.py](../Blind75/Python/Easy/Parkingsystem.py) |
| Plus One | 配列操作 | [PlusOne.py](../NeetCode150/PlusOne.py) |

---

## 🔥 迷ったときの判断基準

```
1. 「何通り？」「最大/最小？」→ まずDPを疑う
2. 配列がソート済み → 二分探索 or 2ポインタ
3. 「連続する」が条件 → スライディングウィンドウ
4. 全列挙 → バックトラッキング
5. 存在確認・頻度 → ハッシュ
6. グラフ/グリッド → DFS or BFS
7. K番目 / Top K → ヒープ
```
