def string_(items,ruleKey,ruleValue):
    items_= ["type", "color", "name"]
    ruleKey_index=items_.index(ruleKey)
    count=0
    for i in items:
        if(i[ruleKey_index]==ruleValue):
            count+=1
    return count
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"


print(string_(items,ruleKey,ruleValue))
        
    