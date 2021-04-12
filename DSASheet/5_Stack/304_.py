new_st=[]
min_st=[]



class Stack_():
    
    def __init__(self):
        self.st=[]
        self.min_=0
    
    def push(self,val):
        if(len(self.st)==0):
            self.st.append(val)
            self.min_=val
        elif(val>=self.min_):
            self.st.append(val)
        else:
            self.st.append((2*val-self.min_))
            self.min_=val
            
    def pop(self):
        if(len(self.st)==0):
            print("UnderFlow")
        elif(self.st[len(self.st)-1]>=self.min_):
            self.st.pop()
        else:
            self.min_=(2*self.min_-self.st[len(self.st)-1])
            self.st.pop()
            
    def getMin(self):
        if(len(self.st)==0):
            print("UnderFlow")
            return None
        return self.min_
                
    
            
                    
        

def func(st):
    # O(1) time and O(n) space 
    while(len(st)>0):
        temp=st.pop()
        new_st.append(temp)
        if(len(min_st)==0 or temp<min_st[len(min_st)-1]):
            min_st.append(temp)
        elif(temp>=min_st[len(min_st)-1]):
            min_st.append(min_st[len(min_st)-1])
            
            



st_=[18 ,19, 29, 15, 16]
# func(st_)
# print(new_st,"\n",min_st)


            
st_2=Stack_()
st_2.push(18)
st_2.push(12)
print(st_2.getMin())
    