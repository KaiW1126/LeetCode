#文字列 s が与えられたとき、重複する文字を含まない最長の部分文字列の長さを返す
#入力: "abcabcbb"
#出力: 3  (答えは "abc")
def length_of_longest_substring(s)
    char_set = Set.new
    left = 0
    max_length = 0

    (0...s.length).each do |right|
        # 1. 重複解消ループ
        # 今見ている文字 s[right] ('a') がすでにセットにある場合、
        # 重複がなくなるまで左端 (left) を縮めます。
        while char_set.include?(s[right])
            char_set.delete(s[left])
            left += 1
        end

        char_set.add(s[right])
        max_length = [max_length, right - left + 1].max 
    end
    max_length
end
# right=0: [a]bcabcbb   → set={a}, len=1
# right=1: a[b]cabcbb   → set={a,b}, len=2
# right=2: ab[c]abcbb   → set={a,b,c}, len=3
# right=3: abc[a]bcbb   → set={a,b,c}, len=3
# right=4: abc[a]bcbb   → set={a,b,c}, len=3
# right=5: abc[b]cbb    → set={a,b,c}, len=3
# right=6: abc[c]bb     → set={a,b,c}, len=3
# right=7: abc[c]bb     → set={a,b,c}, len=3
# right=8: abc[c]bb     → set={a,b,c}, len=3