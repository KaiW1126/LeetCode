def merge_two_lists(list1, list2)
    merged = []
    i = 0  # list1のポインタ
    j = 0  # list2のポインタ
    
    # 両方のリストに要素がある間
    while i < list1.size && j < list2.size
        if list1[i] <= list2[j]
            merged << list1[i] #<<は配列に要素を追加するコマンド
            i += 1
        else
            merged << list2[j]
            j += 1
        end
    end
    
    # 残りの要素を追加
    merged + list1[i..-1] + list2[j..-1] # -1は最後の要素を表す
end