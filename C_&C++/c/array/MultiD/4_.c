#include<stdio.h>

int main(){
    int row=3,col=5;
    int arr[5][3]={0};

    for (int i=0;i<col;i++){
        printf("\nEnter marks of student : %d \n",i+1);
        for (int j=0;j<row;j++){
            scanf("%d \t",&arr[i][j]);
        }
    }
    for (int i=0;i<row;i++){
        printf("\nMax Marks in subject %d",i+1);
        int max_marks=arr[0][i];
        for(int j=0;j<col;j++){
            if(arr[j][i]>max_marks){
                max_marks=arr[j][i];
            }
        }
        printf(" :%d",max_marks);
    }
    printf("\n");
    return 0;
}