def printAbbreviations(str_,asf,count,pos):
    if(pos==len(str_)):
        if(count==0):
            print(asf)
        else:
            print(asf+str(count))
        return
    if(count>0):
        printAbbreviations(str_,asf+str(count)+str_[pos],0,pos+1)
    else:
        printAbbreviations(str_,asf+str_[pos],0,pos+1)
        
    printAbbreviations(str_,asf,count+1,pos+1)
    

printAbbreviations("pep","",0,0)