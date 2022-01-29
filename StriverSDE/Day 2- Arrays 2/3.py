# https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1;j=n-1
        k=n+m-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                k-=1;i-=1
            elif nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                k-=1;j-=1
            else:
                nums1[k]=nums1[i]
                nums1[k-1]=nums2[j]
                k-=2;i-=1;j-=1
        while i>=0 or j>=0:
            if i>=0:
                nums1[k]=nums1[i]
                i-=1
            if j>=0:
                nums1[k]=nums2[j]
                j-=1
            k-=1
