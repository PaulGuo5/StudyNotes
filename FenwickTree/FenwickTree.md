# FenwickTree/Binary Indexed Tree
1. The idea is to store partial sum in each node and get total sum by traversing the tree from leaf to root. The tree has a height of log(n).
2. Mutable updating prefix sum problems
3. Leetcode 307(Range Sum Query - Mutable):[https://leetcode.com/problems/range-sum-query-mutable/](https://leetcode.com/problems/range-sum-query-mutable/)
4. Time complexity:
	- init O(nlogn)
	- query: O(logn)
    - update: O(logn)
5. Code:    
```Python3
class FenwickTree:
    def __init__(self, n):
        self.prefixSum = [0]*(n+1)
        self.n = len(self.prefixSum)
        
    def update(self, i, diff):
        while i < self.n:
            self.prefixSum[i] += diff
            i += i & -i
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.prefixSum[i]
            i -= i & -i
        return s
```