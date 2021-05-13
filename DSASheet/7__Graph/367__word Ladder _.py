
class Solution():
    
    def listToStr(self,list_):
        str_=""
        for i in list_:
            str_+=i 
        return str_
    def findEdge(self,str_,queue,wordlist,depth):
        str_=list(str_)
        for i in range(len(str_)):
            k=0
            temp=str_[i]
            while(k<26):
                if k != (ord(str_[i])-97):
                    str_[i]=chr(97+k)
                    x=self.listToStr(str_)
                    if x in wordlist:
                        queue.append([x,depth])
                k+=1
            str_[i]=temp
    def ladderLength(self, beginWord, endWord, wordList):
        visited=set()
        queue=[[beginWord,1]]
        while(queue):
            temp=queue.pop(0)
            print(temp[0])
            if temp[0] in visited:
                continue
            if temp[0]==endWord:
                print("We find it ",temp)
                return temp[1]
            visited.add(temp[0])
            self.findEdge(temp[0],queue,wordList,depth=temp[1]+1)
        return 0
    
sol=Solution()
q=[]
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
wordList=set(wordList)
print(sol.ladderLength(beginWord,endWord,wordList))