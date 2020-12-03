#include<stdio.h>

int main(){
    int arr[7][7]={0};

    int row=2,col=0;

    arr[0][0]=arr[1][1]=arr[1][0]=1;

    while (row<=7)
    {
        arr[row][0]=1;
        for(col=1;col<row;col++){
            arr[row][col]=arr[row-1][col]+arr[row-1][col-1];

        }
        arr[row][col]=1;
        row++;
    }
    
    printf("Printing Pascal triangle : \n");

    for (int i=0;i<7;i++){
        printf("\n");
        for (int j=0;j<=i;j++){
            printf("\t %d",arr[i][j]);
        }
    }
    printf("\n");
}