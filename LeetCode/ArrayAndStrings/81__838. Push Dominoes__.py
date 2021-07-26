class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        left_force=[-1]*n
        if dominoes[-1]=='.' or dominoes[-1]=='R':
            left_force[-1]=-1
        else:
            left_force[-1]=n-1
            
        for i in range(n-2,-1,-1):
            if dominoes[i]=='.':
                left_force[i]=left_force[i-1]
            elif dominoes[i]=='L':
                left_force[i]=i
            else:
                left_force[i]=-1
                
        right_force=[-1]*n
        if dominoes[0]=='.' or dominoes[0]=='L':
            right_force[-1]=-1
        else:
            right_force[-1]=0
            
        for i in range(1,n):
            if dominoes[i]=='.':
                right_force[i]=right_force[i-1]
            elif dominoes[i]=='R':
                right_force[i]=i
            else:
                right_force[i]=-1
        
        print(left_force,right_force)
        
sol=Solution()
s=".L.R...LR..L.."
print(sol.pushDominoes(s))