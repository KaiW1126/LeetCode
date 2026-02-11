# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    nums.uniq.length != nums.length
    # uniqは重複を削除するメソッド
    # lengthは配列の長さを返す
    # したがって、重複を削除した配列の長さが元の配列の長さと異なれば、重複が存在する
end