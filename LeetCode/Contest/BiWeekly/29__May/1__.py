class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count_=0
        for i in range(len(s)-2):
            set_=[]
            count_uniq=0
            for j in range(i,i+3):
                if s[j] not in set_:
                    count_uniq+=1
                set_.append(s[j])

            print(count_uniq,set_)
            if count_uniq==3:
                count_+=1
            set_.pop(0)
            print(s[i],set_)
            
            # print(s[i])
        return count_
    
    
sol=Solution()
s="xyzzaz"
print(sol.countGoodSubstrings(s))