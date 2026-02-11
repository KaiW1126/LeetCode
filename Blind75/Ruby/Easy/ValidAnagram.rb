# 方法1: ソートして比較する（シンプル）
# def is_anagram(s, t)
#     s.chars.sort == t.chars.sort
# end

# 方法2: ハッシュで文字の出現回数を数える（効率的）
def is_anagram(s, t)
    # 長さが違ったらアナグラムではない
    return false if s.length != t.length
    
    # 初期値0のハッシュを作成
    count = Hash.new(0)
    
    # sの各文字をカウント（+1）
    s.each_char { |c| count[c] += 1 }
    
    # tの各文字をカウント（-1）
    t.each_char { |c| count[c] -= 1 }
    
    # 全ての値が0ならアナグラム
    count.values.all? { |v| v == 0 }
end