class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        # i: 何番目の数字を検討中か, cur: 現在の組み合わせ, current_total: 箱の中の合計点
        def backtrack(i, cur, current_total): 
            # 【正解】合計がターゲットと一致したら、今の組み合わせを答えに保存
            if current_total == target:
                # cur.copy() で「今のスナップショット」をコピーして保存（参照渡し防止）
                ans.append(cur.copy()) 
                return
            
            # 【失敗】ターゲットを超えた、または全数字を調べ終わったら戻る（枝刈り）
            if current_total > target or i >= len(candidates):
                return
            
            # --- 選択肢1：今の数字を使う ---
            cur.append(candidates[i]) # カゴに今の数字を入れる
            # 同じ数字を何度でも使えるので、i は増やさずに再帰
            backtrack(i, cur, current_total + candidates[i])
            
            # --- 戻ってきた時のリセット処理 ---
            cur.pop() # さっき入れた数字を取り出して、カゴを空に戻す（これがバックトラッキング！）
            
            # --- 選択肢2：今の数字を諦めて、次の数字に進む ---
            backtrack(i + 1, cur, current_total)
            
        backtrack(0, [], 0) # インデックス0番目から、空のカゴ、合計0でスタート
        return ans