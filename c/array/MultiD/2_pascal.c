#include<stdio.h>
#define N 10

void readMatrix(int arr[N][N]){
    for (int i=0;i<N;i++){
        printf("\n");
        for (int j=0;j<N;j++){
            arr[i][j]=0;
            printf("\t %d",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
void printingMatrix(int arr[N][N]){
    for (int i=0;i<N;i++){
        printf("\n");
        for (int j=0;j<N;j++){
            printf("\t%d",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main(){
    // int upto=1;
    // printf("Enter pascal triangle upto : ");
    // scanf("%d",&upto);
    int pascTri[N][N];
    printf("\n");
    readMatrix(pascTri);

    for(int i=0;i<N;i++){
        pascTri[i][i]=1;
        pascTri[i][0]=1;
    }

    for(int row=2;row<N;row++){
       
        for(int col=1;col<=row;col++){
            pascTri[row][col]=pascTri[row-1][col-1]+pascTri[row-1][col];
        }
    }
    printingMatrix(pascTri);

}