# { i, like, sam, sung, samsung, mobile, ice, 
#   cream, icecream, man, go, mango}
class Solution:
  
  def wordBreak(self,wordList,word,memo={}):
    # if word in memo:return memo[word]
    if word=="":return True
    print(word)
    for i in range(1,len(word)+1):
      if word[:i] in wordList and self.wordBreak(wordList,word[i:],memo):
        # memo[word]=True
        return True
    # memo[word]=False
    return False

sol=Solution()
wordList=["i","like","sam","sung","samsung","mobile","icecream","mango","and","man","go"]
word="samsungandmango"
print(sol.wordBreak(set(wordList),word))