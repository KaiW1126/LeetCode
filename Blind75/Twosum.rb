# 1. 問題の概要
# 整数の配列 nums と整数 target が与えられたとき、足して target になる2つの数のインデックスを返す。
# 正確に1つの解があると仮定してよい。

# 2. アルゴリズムの選択
# ブルートフォース（総当たり）だと O(N^2) になり、Nが大きい場合に遅くなります。
# そこで、ハッシュマップ（RubyではHash）を使用して、一度見た数値を記憶しておくことで O(N) で解きます。
# 具体的には、`target - current_num` がハッシュに存在するかを確認しながら進めます。

# 3. Rubyコード
def two_sum(nums, target)
  seen = {} # 値 => インデックス を保存するハッシュ

  nums.each_with_index do |num, index|
    complement = target - num
    
    # 補数がすでに見つかっているか確認 (Hash#key? は O(1))
    if seen.key?(complement)
      return [seen[complement], index]
    end
    
    # 現在の数値をハッシュに保存
    seen[num] = index
  end
end

# 4. ステップバイステップのウォークスルー
# 入力: nums = [2, 7, 11, 15], target = 9
# 
# 1. index=0, num=2:
#    - complement = 9 - 2 = 7
#    - seenは空なので 7 はない。
#    - seen[2] = 0 を保存。 seen = {2 => 0}
#
# 2. index=1, num=7:
#    - complement = 9 - 7 = 2
#    - seenに 2 がある！ (index 0)
#    - [0, 1] を返す。

# 5. 重要なポイント
# - **Hash#key?**: キーの存在確認は O(1) です。
# - **One-pass Hash Table**: 配列を一度だけ走査するので、時間計算量は O(N) です。
# - **空間計算量**: 最悪の場合、すべての要素をハッシュに保存するので O(N) です。