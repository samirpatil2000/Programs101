
def rotateTheBox(box):
    row=len(box)
    col=len(box[0])
    new_box=[["." for _ in range(row)] for _ in range(col)]
    # print(new_box)
    # print(box)
    for c in range(col-1,-1,-1):
        for r in range(row):
            new_row_=c
            new_col_=r
            
            if box[r][c]=="#": 
                print("sa",r,c,new_box[new_row_][new_col_],box[r][c],new_row_,new_col_)
                if new_box[new_row_][new_col_] == ".":
                    while(new_row_<len(new_box)-1 and new_box[new_row_][new_col_] == "." and new_box[new_row_][new_col_]!="#"):
                        # print("sad")
                        # print("x",new_box[new_row_][new_col_])
                        new_row_+=1
                    if new_box[new_row_-1][new_col_]==".":
                        new_box[new_row_-1][new_col_]="#" 
                        
                elif new_box[new_row_][new_col_]!="*" :
                    new_box[new_row_][new_col_]="#"
            else:
                new_box[new_row_][new_col_]=box[r][c]
    return new_box
            
                    
            
            
    
box = [["#",".","*","."],
              ["#","#","*","."]]
box=[["#",".","*","."],
     ["#","#","*","."]]

#correct 
[["#","."],
 ["#","#"],
 ["*","*"],
 [".","."]]

[['.', '#'], 
 ['#', '#'], 
 ['*', '*'], 
 ['.', '.']]
# box = [["#",".","#"]]
print(rotateTheBox(box))