from cmath import log, sqrt




# x = (log(n)/log(2)).real
# x = round(x, 10)


# print(x)
# print(x == int(x))



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        # # base case
        # if(n == 1):
        #     return True
        
        # # break out case
        # if (n%2 == 0):
        #     return self.isPowerOfTwo(n/2)
        # return False

        if n < 0: return False
        return str(bin(n)).count('1')==1

        
      
if __name__ =="__main__":
    n = 9
    sol = Solution()
    y = sol.isPowerOfTwo(n)
    print(y)