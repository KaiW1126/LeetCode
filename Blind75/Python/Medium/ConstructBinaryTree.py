# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# preorderとは親（根） → 左の子 → 右の子 の順番でノードを記録したリスト
# inorderとは左の子 → 親（根） → 右の子 の順番でノードを記録したリスト
#この問題では、preorderとinorderから元の二分木を構築する問題です。
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder配列の値とそのインデックスを対応づけるハッシュマップ
        inorder_map = {} # val: index
        for i in range(len(inorder)):
            val = inorder[i] #valにinorderの値を代入
            inorder_map[val] = i #inorder_mapにvalとiを代入
        preorder_index = [0] 
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # 左右のインデックスが逆転したら、部分木は存在しない
            if left > right:
                return None
            
            # preorderの現在の要素が「根（Root）」になる
            root_val = preorder[preorder_index[0]]
            root = TreeNode(root_val)
            preorder_index[0] += 1
            
            # inorder内での根ノードの位置を取得し、左右に分割する境界線とする
            mid = inorder_map[root_val]
            
            # 左側の部分木を構築する（必ず左から先に処理すること）
            root.left = array_to_tree(left, mid - 1)
            # 右側の部分木を構築する
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        # 最初の呼び出し：inorder配列の全範囲を対象にする
        return array_to_tree(0, len(inorder) - 1)