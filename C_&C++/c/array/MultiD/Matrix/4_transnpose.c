#include<stdio.h>
#define N 4
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


void transform_(int arr[N][N]){
    int COL_=N-2;
    // printf("%d\n",i);
    // printf("sam\n");
    while(COL_>=0){
        // printf("s");
        int row=0;
        int col=COL_;
        int ROW_=N-COL_-1;
        while(row<=ROW_){
            printf("%d \t",arr[row][col]);
            row++;
            col++;
        }
        printf("\n");
        COL_--;
    }
    int ROW_x=1;
    while(ROW_x<N-1){
        int row=ROW_x;
        int col=0;
        int COL_x=N-1-ROW_x;
        while(col<=COL_x){
            printf("%d \t",arr[row][col]);
            row++;
            col++;
        }
        printf("\n");
        ROW_x++;
    }
    
}



int main(){
    int arr[N][N]={0};
    readingMatrix(arr);
    printingMatrix(arr);

    // tranposeMatrix(arr);

    
    transform_(arr);
    

    // printingMatrix(arr);

    
    

}