class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        
        track = defaultdict(int)
        for i,n in enumerate(nums):
            if n in track:
                if abs(i-track[n]) <=k:
                    return True
                else:
                    track[n]=i
            else:
                track[n]=i
        return False
                
                    