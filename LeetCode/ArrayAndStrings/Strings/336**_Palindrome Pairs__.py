from typing import List

class Solution:
    # def reverse(self,string_:List[str]): 
    #     i=0
    #     j=len(string_)-1
    #     string_=list(string_)
    #     while i<j:
    #         temp=string_[i]
    #         string_[i]=string_[j]
    #         string_[j]=temp
    #         i+=1
    #         j-=1
    #     return ''.join(string_)
    
    # def isPalindrome(self,string_:str):
    #     i=0
    #     j=len(string_)-1
        
    #     while i<j:
    #         if string_[i]!=string_[j]:return False
    #         i+=1
    #         j-=1
    #     return True
    
        
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     dict_={word:i for i,word in enumerate(words)}
    #     result=set()
        
    #     def returnPairs(word):
    #         for i in range(1,len(word)):
    #             # x=self.reverse(word[i:])
    #             # print(word[:i],self.isPalindrome(word[:i]),x)
    #             # right part
    #             if self.isPalindrome(word[:i]):
    #                 x=self.reverse(word[i:])
                    
    #                 if x in dict_:
    #                     if (dict_[word],dict_[x]) not in result:
    #                         result.add((dict_[x],dict_[word]))
    #             # left part
    #             if self.isPalindrome(word[i:]):
    #                 x=self.reverse(word[:i])
    #                 if x in dict_:
    #                     if (dict_[word],dict_[x]) not in result:
    #                         result.add((dict_[word],dict_[x]))
                        
    #         x=self.reverse(word)
    #         if x in dict_ and x!=word:
    #             if (dict_[word],dict_[x]) not in result:
    #                 result.add((dict_[word],dict_[x]))
    #     if "" in dict_:
    #         index_=dict_[""]
    #         for i in range(len(words)):
    #             if i!=index_ and self.isPalindrome(words[i]):
    #                 result.add((index_,dict_[words[i]]))
    #                 result.add((dict_[words[i]],index_))
    #     for word in words:
    #         returnPairs(word)
    #     return [[u,v] for u,v in result]
    
        # something wrong
        def palindromePairs(self, words: List[str]) -> List[List[int]]:
            dict_={word[::-1]:i for i,word in enumerate(words)}
            result=[]
            for i in range(len(words)):
                if words[i] in dict_:
                    if i!=dict_[words[i]]:
                        result.append((i,dict_[words[i]]))
                        # print("X")
                for j in range(1,len(words)+1):
                    left=words[i][:-j]
                    right=words[i][-j:]
                    if right==right[::-1] and left in dict_:
                        if i!=dict_[left]:
                            result.append((i,dict_[left]))
                            
                    if left==left[::-1] and right in dict_:
                        if i!=dict_[right]:
                            result.append((dict_[right],i))
            
            return [[u,v] for u,v in result]
        
        # correct answer 
        def palindromePairs2(self, words: List[str]) -> List[List[int]]:
            rmap={w[::-1]:i for i,w in enumerate(words)}
            res=[]
            for i,wrd in enumerate(words):
                rev=wrd[::-1]
                if wrd in rmap:                        # same length pair
                    if rmap[wrd]!=i:                   # i and j should be distinct
                        res.append((i,rmap[wrd]))
                for j in range(1,len(wrd)+1): 
                    # first or last j characters as palindrome, other part has pair
                    # print(wrd[:j],wrd[:-j],wrd[j:],wrd[-j:])
                    if wrd[:-j] in rmap and wrd[-j:]==rev[:j]:
                      
                        res.append([i,rmap[wrd[:-j]]])
                    if wrd[j:] in rmap and wrd[:j]==rev[-j:]:
                        res.append([rmap[wrd[j:]],i])
            return res

sol=Solution()
words = ["abcd","dcba","lls","s","sssll"]
# words = ["a",""]
# words = ["bat","tab","cat"]
# d= dict([(w[::-1], i) for i, w in enumerate(words)])
# print(d)
words=["a","aa","aaa"]
print(sol.palindromePairs(words))
print(sol.palindromePairs2(words))


# s="samir"
# for i in range(len(s)+1):
#     print(s[i:],s[:i],i)
#     print(s[-i:],s[:-i],i)

                    
                    
                
                
                
                
            
        
        