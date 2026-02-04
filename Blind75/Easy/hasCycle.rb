# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val 自分の値
#         @next = nil 次の値
#     end
# end

# @param {ListNode} head
# @return {Boolean}


# うさぎとかめのアルゴリズムを使用
#うさぎは２歩進み、亀は1歩進む
# 連結リスト（Linked List）が与えられたとき、サイクルがあるか確認する問題
def hasCycle(head)
    return false if head.nil? || head.next.nil?
# サイクルがない時にfastがnullになる
    slow = head
    fast = head
#サイクルがある時はfastとslowが同じ場所に到達する
    while fast && fast.next # fastがnullでないかつfast.nextがnullでない限り
        slow = slow.next  #headを一個進める
        fast = fast.next.next #headを二個進める

        return true if slow == fast #もし同じ場所にいたらサイクルがあるということ
    end

    false


end