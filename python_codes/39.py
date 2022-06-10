import copy
class Solution:
    def combinationSum(self,candidates,target):
        if target == 0:
            return []
        elif target < 0:
            return None
        
        shortest = None

        for num in candidates:
            rem = target - num
            rem_res = self.combinationSum(candidates,rem)
            if rem_res != None:
                path = rem_res + [num]
                if (shortest == None or len(path)<len(shortest)):
                    shortest = path
                
        
        return shortest

        


if __name__ == "__main__":
    target = 6
    candidates = [2,3,5,7]
    sol = Solution()
    z = sol.combinationSum(candidates,target)
    print(z)