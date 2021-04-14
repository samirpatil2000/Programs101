

def smallerNumbersThanCurrent(nums):
    dict_={} 
    for i in range(len(nums)):
        if nums[i] not in dict_:
            dict_[nums[i]]=[i]
        else:
            dict_[nums[i]].append(i)
    x=sorted(dict_)
    result_list=[None for _ in range(len(nums))]
    for i in range(len(x)):
        count=0
        for j in range(i):
            count+=len(dict_[x[j]])
        for elemen_index in dict_[x[i]]:
            result_list[elemen_index]=count
            
    
    print(dict_)
    print(result_list)
    return result_list
    
n =nums = [7,7,7,7]
smallerNumbersThanCurrent(n)
        
           