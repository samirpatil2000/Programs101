#include<stdio.h>
#define MAX 5

void readingMatrix(int arr[MAX][MAX],int row,int col){
    
    for (int i=0;i<row;i++){
        for (int j=0;j<col;j++){
            scanf("\t %d",&arr[j][i]);
        }
    }
    
}
void printingMatrix(int arr[MAX][MAX],int row,int col){
    
    for (int i=0;i<row;i++){
        for (int j=0;j<col;j++){
            printf("\t %d",arr[j][i]);
        }
        printf("\n");
    }
}

int main(){
    int A[MAX][MAX],B[MAX][MAX];

    int resultant[MAX][MAX];
    
    int arow,bcol,acol,brow;

    
    
    printf("\nEnter the number rows in A matrix : ");
    scanf("%d",&arow);
    printf("\nEnter the number column in A matrix : ");
    scanf("%d",&acol);
    printf("\nEnter the number rows in B matrix : ");
    scanf("%d",&brow);
    printf("\nEnter the number column in B matrix : ");
    scanf("%d",&bcol);


    int res_row=arow,res_col=bcol;

    if (arow != bcol){
        printf("Number of column of first should be equal to column of second array");
        // exit();
    }

    else{

        printf("\nEnter elements of matrix A\n");
        readingMatrix(A,arow,acol);
        printf("Enter elements of matrix B\n");
        readingMatrix(B,brow,bcol);

        printf(" \nMatrix A \n");
        printingMatrix(A,arow,acol);
        printf(" \nMatrix B \n");
        printingMatrix(B,brow,bcol);

        for (int i=0;i<arow;i++){
            
            for (int j=0;j<bcol;j++){
                int sum=0;
                for(int k=0;k<arow;k++){
                    sum+=A[k][i]*B[j][k];
                }
                resultant[j][i]=sum;
            }
        }

        printf(" \nMatrix A X B is \n");
        printingMatrix(resultant,res_row,res_col);

    }

    


    return 0;

}