def maxBallon(text):
    list_=['b','a','l','l','o','o','n']
    count_=0
    min_=9999999999
    if(len(text)<len(list_)):
        return 0
    for i in list_:
        count_=text.count(i)
        
        if(min_>count_):
            min_=count_
    l_count=text.count('l')
    o_count=text.count('o')
    if(l_count==count_*2 or o_count==count_*2):
        return count_
    else:
        return count_ // 2
        
    

s="balorn"
text="krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(maxBallon(text))


from collections import Counter
def maxNumberOfBalloons( text: st):
    a = Counter(text)
    min_ = 10000000
    for i in 'balon':
        if i == 'o' or i == 'l':
            if min_ > a[i]//2:
                min_ = a[i]//2
        else:
            if min_ > a[i]:
                min_ = a[i]
    return min_ 
    
print(maxNumberOfBalloons(text))