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