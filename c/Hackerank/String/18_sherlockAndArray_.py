
def sherlockAndArray(arr,n):
    i=0
    j=n-1
    left_sum=arr[0]
    right_sum=arr[j]
    while(i<j):
        print(left_sum,right_sum," i=",i," j=",j)
        if(left_sum<right_sum):
            i+=1
            left_sum+=arr[i]
            # if(i+1==j-1):
            #     return
            
        elif(left_sum>left_sum):
            j-=1
            right_sum+=arr[j]
            # if(i+1==j-1):
            #     return
            
        
            
        else:
            if(i+1==j-1):
                print("The anwser is",arr[i+1])
                print("Yes")
                return
            elif(i+1==j):
                print("The anwser is",arr[i])
                print("Yes🐶")
                return
            else:
                if(arr[i+1]==0):
                    i+=1
                elif(arr[j-1]==0):
                    j-=1
                else:
                    i+=1
                    j-=1
                    left_sum+=arr[i]
                    right_sum+=arr[j]
    print("No🐶")
           
           
           
def function(arr_):
    sum_=sum(arr_)
    x=0
    for i in range(len(arr_)):
        if(x*2==sum_-arr_[i]):
            return "Yes🐶"
        x+=arr_[i]
    
    return "No"

        
            
            
    
arr=[1,2,3]     
# sherlockAndArray(arr,len(arr))    
print(function(arr))