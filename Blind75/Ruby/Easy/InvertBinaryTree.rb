# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {TreeNode}
def invert_tree(root)
    if root.nil?
        return nil
    end
    # ① このノードの左右を入れ替える
    root.left, root.right = root.right, root.left
    # ② 左の子ノードに対しても同じ処理を行う（再帰）
    invert_tree(root.left)
    # ③ 右の子ノードに対しても同じ処理を行う（再帰）
    invert_tree(root.right)

  return root
end