"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None #そもそも何もなかったらNone
        
        old_to_new = {} #元のノードと新しいノードを対応付けるための辞書

        def dfs(node):
            #すでにold_to_newに存在する場合は、それを返す
            if node in old_to_new:
                return old_to_new[node]
            #Nodeで新たにメモリ確保してcloneに代入
            clone = Node(node.val)
            #元のnodeをキーとして新しくcloneを値として代入する
            old_to_new[node] = clone # nodeというキーにcloneをvalueとしてる
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node)