#include<stdio.h>


void readingMatrix(int arr[N][N]){
    int number=1;
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
              arr[i][j]=number;
              number++;
        }
    }   
}
void printingMatrix(int arr[N][N]){
    for (int i=0;i<N;i++){
        printf("\n");
        for (int j=0;j<N;j++){
            printf("\t %d",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

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