#include<stdio.h>
#define MAX 6


// https://www.hackerrank.com/challenges/2d-array/problem


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

    int arr[MAX][MAX] ={ 
            {-9, -9, -9,  1, 1, 1 },
            {0 ,-9 , 0 , 4 ,3 ,2 },
            {-9, -9, -9,  1, 2, 3 },
            {0 , 0 , 8 , 6 ,6 ,0 },
            {0 , 0 , 0 ,-2 ,0 ,0 },
            {0 , 0 , 1 , 2 ,4 ,0 },
    };
    printMatrix(arr);

    int counter=1;

    int sum=0,max=-999;

    for(int row=0;row<MAX-2;row++){
        for(int col=0;col<MAX-2;col++){
            int upperEnd=0,lowerEnd=0,middleEnd=0;
            for(int i=0;i<3;i++){
                upperEnd+=arr[row][col+i];
                lowerEnd+=arr[row+2][col+i];
            }
            middleEnd=arr[row+1][col+1];
            sum=upperEnd+middleEnd+lowerEnd;
            printf("%d %d\n",counter,sum);
            counter+=1;

            if(sum>max){
                max=sum;
            }
        }
        
    }

    printf("The max sum is %d\n",max);

}