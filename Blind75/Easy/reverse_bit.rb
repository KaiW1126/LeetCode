# @param {Integer} n
# @return {Integer}
def reverse_bits(n)
    n_bit = n.to_s(2) #2進数に変換
    n_bit_32 = n_bit.rjust(32, '0') #右側に下の数字を置き左に0を揃えて32桁にする
    n_bit_32 = n_bit_32.reverse #逆順にする
    n_bit_32 = n_bit_32.to_i(2) #入力2進数をintに戻す
    return n_bit_32
end