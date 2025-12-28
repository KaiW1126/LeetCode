# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(p, q)
  # 1. 両方とも空（nil）なら「同じ」とみなす
  return true if p.nil? && q.nil?
  
  # 2. どちらか片方だけ空なら「違う」
  return false if p.nil? || q.nil?
  
  # 3. ノードの値が違ったら「違う」
  return false if p.val != q.val
  
  # 4. 左の子同士、右の子同士も再帰的にチェックして、両方OKならtrue
  is_same_tree(p.left, q.left) && is_same_tree(p.right, q.right)
end