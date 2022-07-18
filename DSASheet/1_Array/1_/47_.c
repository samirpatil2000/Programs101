#include<stdio.h>


/*
    Given a boolean 2D array of n x m dimensions where each row is sorted. 
    Find the 0-based index of the first row that has the maximum number of 1's.
    // https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
*/

#define N 4
void printMatrix(int arr[N][N]){
    int number=1;
    for (int i=0;i<N;i++){
        printf("\n");
        for (int j=0;j<N;j++){
              printf("\t %d",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    
}

int rowWithMax1_1(int arr[N][N]){
    // O(N*M)  in worst chase 
    int max_row_with_1=0,row;
    for(int i=0;i<N;i++){
        int j=0,current_max_row;
        while (arr[i][j] != 1){
            j++;
        }
        current_max_row=N-j-1;
        if (current_max_row>max_row_with_1)
        {
            max_row_with_1=current_max_row;
            row=i;
        }    
    }
    return row;
}

int rowWithMax1_2(int arr[N][N]){
    // O(nlog(m))
    int max_row_with_1=0,row;
    for(int i=0;i<N;i++){
        int j=N-1,counter=0;
        while (arr[i][j] == 1 && j>=0){
            j--;
            counter++;

        }
        if (counter>max_row_with_1)
        {
            max_row_with_1=counter;
            row=i;
        }
        if(counter==N){
            break;
        }
    }
    return row;
}

// withMoreOptimisation

int rowWithMax1_3(int arr[N][N]){
    int row;
    int j=N-1;
    int i=0;
        while(i<N && j>=0){
            if(arr[i][j]==1){
                row=i;
                j--;
            }else{
                i++;
            }
        }
        return row;
}

int rowWithMax1_4(int arr[N][N]){
    int row;
    for(int j=0;j<N;j++){

        for(int i=0;i<N;i++){
            while (arr[i][j] == 1){
                row=i;
                goto x;
            }
        }
    }
    x:printf("");
    return row;
}





int main(){
    int mat[N][N]={ {0, 1, 1, 1},
                    {0, 0, 1, 1},
                    {0, 0, 1, 1},
                    {0, 0, 1, 1}};
    printMatrix(mat);

    printf("%d\n",rowWithMax1_1(mat));
    printf("%d\n",rowWithMax1_2(mat));

    printf("%d\n",rowWithMax1_3(mat));
    printf("%d\n",rowWithMax1_4(mat));


}