def isPalindrome(s)
    lower_s = s.gsub(/[^a-zA-Z0-9]/, "").downcase
    for i in (0..lower_s.length / 2)
        if lower_s[i] != lower_s[lower_s.length - i - 1]
            return false
        end
    end
    return true
end
#gsub メソッドについて
 # gsub は "global substitution"（全体置換） の略で、文字列内のパターンに一致するすべての部分を置換するメソッドです。

    #基本構文
    #ruby
    #文字列.gsub(パターン, 置換文字列)
    # 基本的な置換
=begin
gsub メソッドについて
gsub は "global substitution"（全体置換）の略で、
文字列内のパターンに一致するすべての部分を置換するメソッドです。
例:
"hello world".gsub("o", "0")  => "hell0 w0rld"
"hello123".gsub(/[0-9]/, "X") => "helloXXX"
=end