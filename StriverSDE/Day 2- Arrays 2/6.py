# https://www.codingninjas.com/codestudio/problems/615
# using merge sort and recursion

from sys import stdin

def f(nums, i, j):
    if i >= j:
        return 0
    mid = (i + j) // 2
    count = f(nums, i, mid) + f(nums, mid + 1, j)
    ii = i
    for k in range(mid + 1, j + 1):
        while(ii <= mid and nums[ii] < nums[k]):
            ii += 1
        count += (mid - ii + 1)
    nums[i:j + 1] = sorted(nums[i:j + 1])
    return count


def getInversions(arr, n):
    ans = f(arr, 0, n-1)
    return ans

# Taking inpit using fast I/O.


def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
