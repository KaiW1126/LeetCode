from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #存在しないキーにアクセスした時に空のリストを返す
        for s in strs:
            key = tuple(sorted(s)) #ソートした文字列をタプルに変換してキーにする
            anagrams[key].append(s) #キーに対応するリストに文字列を追加
        return list(anagrams.values()) #リストの値を返す

        # タプルとは、リストの値が変更できないもの
        
