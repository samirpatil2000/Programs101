#include<stdio.h>
#define N 3
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

// take a transpose and reverse each row
void tranposeMatrix(int arr[N][N]){
    for (int i=0;i<N;i++){
        for (int j=0;j<i;j++){
            int temp=arr[i][j];
            arr[i][j]=arr[j][i];
            arr[j][i]=temp;
        }
    }
}



int main(){
    int arr[N][N]={0};
    readingMatrix(arr);
    printingMatrix(arr);

    tranposeMatrix(arr);
    

    

    printingMatrix(arr);

    
    

}