def climb_stairs(n)
  return 1 if n == 1
  return 2 if n == 2
  one_step_before = 2
  two_steps_before = 1
  current = 0
  (3..n).each do
    current = one_step_before + two_steps_before
    # 【重要】変数の更新（次のループのために枠をずらす）
  # 「今の1つ前」は「次の2つ前」になる
    two_steps_before = one_step_before
    one_step_before = current
  end
  current
end