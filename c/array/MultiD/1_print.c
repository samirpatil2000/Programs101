#include<stdio.h>

int main(){
    int arr[2][2]={20,32,21,3};

    printf("Printing Array : \n");

    for (int i=0;i<2;i++){
        printf("\n");
        for (int j=0;j<2;j++){
            printf("%d\t",arr[i][j]);
        }
    }
    printf("\n");
}