class Solution:
    def rob(self , n: List[int]) ->int:
        c = max(n[0],self.helper(n[1:]),self.helper(n[:-1]))
        return c
    def helper(self,n):

        rob1,rob2=0,0

        for i in n:
            temp = max(rob1+i,rob2)
            rob1=rob2
            rob2 = temp
        return rob2

