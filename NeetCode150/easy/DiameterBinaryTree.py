class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # 全ての再帰を通して「最大直径」を記録しておく場所
    
        def height(node):
            # ベースケース: 底（None）に到達したら深さ0（返り値0）を返す
            if not node: return 0
            
            # 左下と右下に限界まで潜っていく（行きは素通り）
            left = height(node.left)
            right = height(node.right)
            
            # ↓↓↓ ここから下（None）から戻ってきた「帰りがけ」の計算 ↓↓↓
            
            # 【直径の候補を更新 (self.ans)】
            # 「このノードを折り返し地点とするパスの長さ」= 左の高さ + 右の高さ
            # 常に過去の最大値と比べて大きい方を残す
            self.ans = max(self.ans, left + right)
            
            # 【親に自分の高さを返す (return)】
            # 親は「左か右の長い方」しか選べない
            # だから長い方に自分自身(1)を足して「俺の高さはこれだよ」と親に返す
            return 1 + max(left, right)
            
        height(root) # ルートから探索スタート
        return self.ans