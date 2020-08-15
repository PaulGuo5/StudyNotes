# Counting sort
- Intro
	- Sorting special input in linear time
	- All non-negative nums
```Python
def countSort(nums):
    res = [0 for _ in range(len(nums))]
    cnt = [0 for _ in range(max(nums)+1)]
    for n in nums:
        cnt[n] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for n in nums:
        res[cnt[n]-1] = n
        cnt[n] -= 1
    return res
```
- cnt: represents the Last Position item can occur
- Complexity:
	- Time: O(n)
	- Space: O(n)