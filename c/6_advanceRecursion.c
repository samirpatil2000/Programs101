#include<stdio.h>
#define MAX 7

// the flood fill problem use recurssion

int printMatrix(int arr[MAX][MAX]){
    for(int i=0;i<MAX;i++){
        printf("\n");
        for(int j=0;j<MAX;j++){
            printf("\t%d",arr[i][j]);
        }
    }
    printf("\n");
}

int fillNumber(int arr[MAX][MAX],int r,int c,int toFill,int prevFill){
    // printf("Debug 1 \n");
    if( c<0 || r<0 || r>=MAX || c>=MAX ){
        // printf("Debug 2 \n");
        return 0;
    }
    if( arr[r][c] != prevFill){
        // printf("Debug 3 \n");
        return 0;
    }
    arr[r][c]=toFill;

    fillNumber(arr,c+1,r,toFill,prevFill);
    fillNumber(arr,c-1,r,toFill,prevFill);
    fillNumber(arr,c,r-1,toFill,prevFill);
    fillNumber(arr,c,r+1,toFill,prevFill);
    
}


int main(){
    int arr[MAX][MAX]={ 
                    {1,1,1,3,2,3,2},
                    {1,2,4,4,2,3,2},
                    {1,2,4,3,2,5,2},
                    {2,1,4,3,4,5,5},
                    {1,1,1,4,5,5,2},
                    {2,1,1,3,4,5,5},
                    {1,2,4,3,2,5,2},
                    };


    printMatrix(arr);
    fillNumber(arr,1,2,10,4);
    fillNumber(arr,0,0,00,1);
    printMatrix(arr);
    
}