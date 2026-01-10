# @param {Integer} n
# @return {Integer}
def hamming_weight(n)
    return n.to_s(2).count("1")
    # 2進数に変換して1の数を数える
end