# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    min_price = Float::INFINITY #minpriceには今まで配列でみた中で一番小さいものを入れたいからとりあえずこの世で一番でかいもの入れとく
    max_profit = 0

    prices.each do |price|
        min_price = [min_price, price].min
        #.minしたら初期値無限大なんだから絶対priceが一回めに入るようになる
        max_profit = [max_profit, price - min_price].max
    end
    max_profit
end