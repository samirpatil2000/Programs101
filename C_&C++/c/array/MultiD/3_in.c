#include<stdio.h>

int main(){
    int row=3,col=5;
    int arr[5][3]={0};

    for (int i=0;i<col;i++){
        printf("\nEnter sales of %d Empolyee ",i+1);
        for (int j=0;j<row;j++){
            scanf(" %d\t",&arr[i][j]);
        }
    }
    for (int i=0;i<col;i++){
        printf("\nTotal sales of empolyee %d",i+1);
        int total=0;
        for(int j=0;j<row;j++){
            total=total+arr[i][j];
        }
        printf(" :%d",total);
    }
    printf("\nTotal sales of each item:\n");
    for(int i=0;i<row;i++){
        int total_sales=0;
        for (int j=0;j<col;j++){
            total_sales+=arr[j][i];
        }
        printf("Total sales of %d item : %d\n",i+1,total_sales);

    }
}