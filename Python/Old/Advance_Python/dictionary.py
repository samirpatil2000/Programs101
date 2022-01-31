score={}
score["Test1"]={}
score["Test2"]={}

score['Test1']["Sam"]=65
score['Test1']["Sid"]=70
score["Test2"]["Sid"]=90
score["Test2"]["Sam"]=85
#
# print(score)
# print(score["Test1"].keys())
# print(score["Test1"].values())
#
# #
#
#
# d={}
# for i in "abcdefghijk":
#     d[i]=i
# print(d.keys(),"and",d.values())



#have have to add total score of sam and Sid
# for n in ["Sam","Sid"]:
#     ttl[n]=0
#     for i in score.keys():
#         if n in score[i].values(
#             ttl[n]=ttl[n]+score[i][n]
#



scores={'Blue':[32,3],'Bluish':[54,67]}
# scores['sam']=[35]
# scores['sam'].append(34)
def add_in_dict(b,list):
    if b in scores.keys():
        scores[b].extend(list)

    else:
        scores[b] = list
    return scores



s=add_in_dict('Blue',[21,23])
print(s)
s2=add_in_dict('Sam',[21,23])
print(s2)