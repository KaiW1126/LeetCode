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
# @return {Integer}
def max_depth(root)
    return 0 if root.nil?
    # left,rught は各ノードの左と右の子を指す
    # もう構文として子を表すものがあるから直感的に考えていい
    left = max_depth(root.left)
    right = max_depth(root.right)
    [left, right].max + 1
end