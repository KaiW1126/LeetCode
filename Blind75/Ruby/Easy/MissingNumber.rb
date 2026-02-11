def missing_number(nums)
    n = nums.length
    expected_sum = (n*(n+1))/2
    actual_sum = nums.sum
    expected_sum - actual_sum
end

# 欠けてる数字を探すために、合計で比較する。
#マジで賢い
#  return i unless nums.include?(i)