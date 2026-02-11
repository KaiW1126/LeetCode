# ============================================================
# Merge Two Sorted Lists - LinkedListのマージ
# ============================================================
# 
# 【データ構造】
# - LinkedList (単方向連結リスト)
# - 各ノード: val (値) と next (次のノードへの参照)
#
# 【アルゴリズム】
# - Two Pointer: 各リストの現在ノードを追跡
# - Dummy Node: 結果リストの先頭を簡単に扱うためのダミーノード
#
# 【時間計算量】O(n + m)
# - n: list1の長さ, m: list2の長さ
# - 各ノードを1回ずつ訪問
#
# 【空間計算量】O(1)
# - 新しいノードは作らず、既存のノードを繋ぎ変えるだけ
# - ダミーノード1つのみ追加
#
# ============================================================

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end

def merge_two_lists(list1, list2)
    # ダミーノード: 結果リストの先頭を簡単に扱うため
    # 最終的に dummy.next が結果の先頭になる
    dummy = ListNode.new(0)
    current = dummy  # 現在の位置を追跡するポインタ
    
    # 両方のリストにノードがある間
    while list1 && list2
        # 小さい方のノードを選択
        if list1.val <= list2.val
            current.next = list1  # list1のノードを繋ぐ
            list1 = list1.next    # list1を次へ進める
        else
            current.next = list2  # list2のノードを繋ぐ
            list2 = list2.next    # list2を次へ進める
        end
        current = current.next    # currentを次へ進める
    end
    
    # 残りのノードを繋ぐ
    # どちらか一方が nil になったら、もう一方の残り全てを繋ぐ
    current.next = list1 || list2
    
    # ダミーノードの次が結果の先頭
    dummy.next
end