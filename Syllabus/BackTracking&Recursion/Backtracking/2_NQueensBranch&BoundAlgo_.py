def solve(Board,row,bool_cols,bool_nd,bool_rd,asf):
    if(row==len(Board)):
        print(asf+".")
        return
    for col in range(len(Board[0])):
        if(bool_cols[col]==False and 
           bool_nd[col+row]==False and 
           bool_rd[row-col+len(Board)-1]==False):
            
            Board[row][col]=1
            
            bool_cols[col]==True 
            bool_nd[col+row]==True
            bool_rd[row-col+len(Board)-1]==True
            
            solve(Board,row+1,bool_cols,bool_nd,bool_rd,asf+"--"+str(row)+","+str(col))
            
            Board[row][col]=0
            
            bool_cols[col]==False 
            bool_nd[col+row]==False
            bool_rd[row-col+len(Board)-1]==False
    

n=4
Board=[[ 0 for _ in range(n)] for _ in range(n)]

col=[False for _ in range(n)]
nd=[False for _ in range(2*n-1)]
rd=[False for _ in range(2*n-1)]

solve(Board=Board,row=0,bool_cols=col,bool_nd=nd,bool_rd=rd,asf="")

print(Board)