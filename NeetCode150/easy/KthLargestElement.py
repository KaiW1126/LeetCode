class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #selfつける理由はこのクラスの変数として扱い二つの関数で併用できるようにするため

        self.minHeap = nums # minHeapは変数名
        self.k = k
        heapq.heapify(self.minHeap) #heapqは標準ライブラリでキューを実装してる

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
            #k個より多くなったら一番小さいものをpopさせて捨てる

    def add(self, val: int) -> int:
        #add関数が呼ばれた時にheapで一番小さいのが先頭に来ているのを維持したまま新しい数を追加
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)