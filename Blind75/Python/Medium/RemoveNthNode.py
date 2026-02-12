# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head は「リストの先頭（入り口）」を指す
        # ダミーノードを作成し、その次(next)に先頭(head)を繋ぐ
        # これで [Dummy] -> [1号車(head)] -> [2号車] ... という列ができる
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n-=1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
        