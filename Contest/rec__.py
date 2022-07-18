class Solution:
    
    def isprime(self, num):
        if num <= 1:
            return False
        for i in range(2, num + 1):
            if i * i > num:
                break
            if num % i == 0:
                return False
        return True
        
    max_ = 0
    
    def recursion(self, s, num = ""):
        print(num)
        if len(s) == 0:
            return
        if num != "":
            num_ = int(num ,2)
            if self.max_ < num_ and self.isprime(num_):
                
                self.max_ = max(self.max_, num_)
            
        self.recursion(s[1:], num + s[0])
        self.recursion(s[1:], num)
        
        return
    
    def call_(self, s):
        self.recursion(s)
        if self.max_ == 0:
            return -1
        return self.max_
    
sol = Solution()
print(sol.call_("1011"))