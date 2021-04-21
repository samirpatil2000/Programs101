def sum_(nums):
    dict_={}
    sum_a=0
    for num in nums:
        if not num in dict_:
            dict_[num]=1
        else:
            dict_[num]+=1
    for key in dict_.keys():
        if dict_[key]==1:
            sum_a+=key
            
        
    print(dict_)
    print(sum_a)
    
nums = [1,2,3,4,5]
print(sum_(nums))