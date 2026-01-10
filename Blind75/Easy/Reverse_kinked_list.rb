# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
    prev = nil
    current = head
    
    while current
        next_node = current.next  # 次のノードを保存
        current.next = prev       # ポインタを逆向きに
        prev = current            # prevを進める
        current = next_node       # currentを進める
    end
    
    prev  # 新しいhead
end

#例えば1,2,3の時には1がcurrent
        #2がnextとなる。そこから初めはcurrent.nextが今度はnilになる
        #そして,prevにcurrent(1)が入る
        #そしてcurrentはnextつまり2になり
        #そして次のループでcurrent.nextつまり3がnextになる
        #prevは先ほどのループで１になったのでそれがcurrent.nextに入り1
        #そしてprevは今度は2になり
        #そしてcurrentはnextつまり3になる。