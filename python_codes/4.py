from collections import deque
from math import prod

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        q = sorted(nums1+ nums2)
        if len(q)%2 == 0:
            return (q[int(len(q)/2)]+q[int((len(q)/2)-1)])/2
        else:
            return q[int(len(q)/2)]


if __name__ == "__main__":
    x = Solution()

    y = [1,3,4]
    z = [2]

    print(x.findMedianSortedArrays(y,z))