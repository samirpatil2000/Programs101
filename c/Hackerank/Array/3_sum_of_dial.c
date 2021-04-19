#include<stdio.h>
#define MAX 3

int diagonalDifference(int arr_rows, int arr_columns, int arr[3][3]) {
    int i=0,j=0;
    int sum_1=0 , sum_2=0,diff;
    while(i<MAX && j<MAX){
        sum_1+=arr[i][j];
        sum_2+=arr[i][MAX-j-1];
        i++;
        j++;
    }
    if(sum_1>sum_2){
        return sum_1;
    }
    return sum_2;
}
int printMatrix(int arr[MAX][MAX]){
    for(int i=0;i<MAX;i++){
        printf("\n");
        for(int j=0;j<MAX;j++){
            printf("\t%d",arr[i][j]);
        }
    }
    printf("\n");
}


int main(){
    int arr[MAX][MAX]={0};
    
    printf("%d\n",diagonalDifference(3,3,arr));


}