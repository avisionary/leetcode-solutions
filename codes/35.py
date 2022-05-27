class Solution:
    def searchInsert(self, nums, target: int) -> int:

        left = 0 
        right = len(nums)
        new_index = len(nums)
        mid = (left+right)//2
        def find_index(nums,left,right,mid):
                mid = (left+right)//2
                if target == nums[mid]:
                    return mid

                elif target < nums[mid]:
                    if right == mid:
                        return mid
                    right = mid
                    new_index = mid
                    return find_index(nums,left,right,mid)

                else:
                    if left == mid:
                        return mid+1
                    left = mid
                    new_index = mid
                    return find_index(nums,left,right,mid)
        return find_index(nums,left,right,mid)
         



if __name__ == "__main__":
    nums = [1,3,5,6]
    sol = Solution()
    y = sol.searchInsert(nums,7)
    print(y)