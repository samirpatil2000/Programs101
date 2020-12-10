#include<stdio.h>
#define N 6

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
    printf("\n");
    for (int i=0;i<N;i++){ // row
        for (int j=0;j<N;j++){ // col
            printf("\t %d",arr[i][j]);
        }
        printf("\n\n");
    }
}
int main(){
    int arr[N][N]={0};
    
    int top=0,left=0,down=N-1,right=N-1;
    int dir=0;
    int round=0;

    readingMatrix(arr);
    printingMatrix(arr);

    printf("\n");
    int element=0;

    // while(top<=down && left<=right){
    while(element<N*N){
        
        if(dir==0){
            for(int i=left;i<=right;i++){
                printf("\t %d",arr[top][i]);
                element++;
                
            }
            dir++;
            top++;
            
        }
        else if(dir==1){
            for(int i=top;i<=down;i++){
                printf("\t %d",arr[i][right]);
                element++;
            }
            dir++;
            right--;
            
        }
        else if(dir==2){
            for(int i=right;i>=left;i--){
                printf("\t %d",arr[down][i]);
                element++;
            }
            dir++;
            down--;
            
        }
        else if(dir==3){
            for(int i=down;i>=top;i--){
                printf("\t %d",arr[i][left]);
                element++;
        
            }
            dir=0;
            left++;
            
        }
    }
    printf("\n\n");
}