#include<stdio.h>


// Common elements in all rows of a given matrix

void brute(int arr[4][5],int row,int col){
        int count[5]={};
        for(int i=0;i<col;i++){
            count[i]=1;
        }
        for (int i = 1; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                for (int k = 0; k < col; k++)
                {
                    if (arr[0][k]==arr[i][j])
                    {
                        count[k]+=1;
                    }
                    
                }
                
            }
            
        }
        for (int i = 0; i < col; i++)
        {
            if (count[i]==4)
            {
                printf("\t %d",arr[0][i]);
            }
            
            
        }
        printf("\n");
}

int main(){
    int row=4,col=5;
    
    int arr[4][5] ={{1, 2, 1, 4, 8},
                    {3, 7, 8, 5, 1},
                    {8, 7, 7, 3, 1},
                    {8, 1, 2, 7, 9},
            };

    brute(arr,row,col);
    
    
    

}