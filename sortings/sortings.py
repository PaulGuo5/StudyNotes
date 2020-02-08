nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

if not nums: print(nums)

# 1. Quick sort: O(nlogn)
def partition(nums, left, right):
    pivot_idx = left
    pivot_val = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot_val:
            right -= 1
        while left < right and nums[left] <= pivot_val:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
    return left

def quickSort(nums, left, right):
    if left >= right: return
    pivot = partition(nums, left, right)
    quickSort(nums, left, pivot-1)
    quickSort(nums, pivot+1, right)

quickSort(nums, 0, len(nums)-1)
print("quick sort", nums)

# 2. Counting sort(Non-negative): O(n)
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
print(countSort(nums))

# 3. Bucket sort: O(n)
def bucketSort(nums):
    max_, min_ = max(nums), min(nums)
    buckets = [0 for _ in range(max_-min_+1)]
    for i in range(len(nums)):
        buckets[nums[i]-min_] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += buckets[i]*[i+min_]
    return res
print("Bucket sort: ", bucketSort(nums))


# 4. Radix sort: non-negative: O(n*m)
def radixSort(nums, d):
    for i in range(d):
        s = [[] for i in range(10)]
        for n in nums:
            s[n//(10**i)%10].append(n)
        nums = [a for b in s for a in b]
    return nums
print("Radix sort: ", radixSort(nums, len(str(max(nums)))))

# 5. Insertion sort: O(n^2)
def insertionSort(nums):
    for i in range(len(nums)):
        target = nums[i]
        j = i
        while j-1 >=0 and nums[j-1] > target:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        nums[j] = target
    return nums
print("Insertion sort: ", insertionSort(nums))

# 6. Selection sort: O(n^2)
def selectionSort(nums):
    for i in range(len(nums)-1):
        min_ = nums[i]
        j_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < min_:
                min_ = nums[j]
                j_idx = j
        nums[i], nums[j_idx] = nums[j_idx], nums[i]   
    return nums
print("Selection sort: ", selectionSort(nums))    

# 7. Bubble sort: O(n^2)
def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1, i, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums
print("Bubble sort: ", bubbleSort(nums))
