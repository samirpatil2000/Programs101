class Solution:
    
    def printPairing(self,num):
        
        def dfs(str,out):    
            if len(str)==0:
                # print(out)
                return
            if out=="":
                dfs(str[1:],str[0])
            else:
                dfs(str[1:],out+"-"+str[0])
            for i in range(1,len(str)):
                if out=="":
                    dfs(str[1:i]+str[i+1:],str[0]+str[i])
                else:
                    dfs(str[1:i]+str[i+1:],out+"-"+str[0]+str[i])
        dfs(str(num),"")
        return
    def countPairing(self,num):
            
        def dfs(str,memo={}):
            if str in memo:return memo[str]
            if len(str)==0:
                return 1
            # print(str)
            count_=dfs(str[1:])
            for i in range(1,len(str)):
                count_+=dfs(str[1:i]+str[i+1:])
            memo[str]=count_
            return count_
        
        return dfs(str(num))
    def optimumBetter(self,str):
        if len(str)==0:
            return 1
        count_=self.optimumBetter(str[1:])
        count_=count_+(self.optimumBetter(str[2:]))*(len(str)-1)
        return count_
    def best(self,len_,memo={}):
        if len_ in memo:return memo[len_]
        if len_==0:return 1
        if len_<0:return 0
        len_-=1
        x=self.best(len_)+self.best(len_-1)*len_
        memo[len_]=x
        return memo[len_]
        
sol=Solution()
num=123456789034567889764900000000032453312235342131
# sol.printPairing(num)
# print(sol.countPairing(num))
# print(sol.optimumBetter(str(num)))
print(sol.best(len(str(num))))
        