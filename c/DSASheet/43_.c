// Search in matrix
#include<stdio.h>
#define N 4
#define M 4


int bruteForce(int matrix[N][M],int target){
    // O(n*m)

    int found=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(matrix[i][j]==target){
                return found=1;
            }
        }
    }
}


// I don't why but it is not working
int linearSearch(int matrix[N][M],int target){

    // O(n+m)

    int found=0,target_row;
    int last_colomn=M-1;
    for(int i=0;i<N;i++){
        if(matrix[i][last_colomn] >= target){
            target_row=i;
            break;
        }
    }
    for(int j=0;j<M;j++){
        if(matrix[target_row][j]==target){
            printf("Element found at arr[%d][%d]",target_row,j);
            return found=1;
        }
    }
    return 0;
}


// use binary search 
int usingBinarySearch(int arr[N][M],int l,int r,int target){

    if(l>r){
        return 0;
    }
    int mid=(l+r)/2;
    
    if(arr[mid/M][mid%M]==target){
        return 1;
    }else{
        if(arr[mid/M][mid%M]>target){
            return usingBinarySearch(arr,l,mid-1,target);
        }else{
            return usingBinarySearch(arr,mid+1,r,target);
        }
    }
}





void readingMatrix(int arr[N][M]){
    int number=2;
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            arr[i][j]=number;
            number+=2;
        }
    }
    
}
void printingMatrix(int arr[N][M]){
    
    for (int i=0;i<N;i++){
        printf("\n");
        for (int j=0;j<M;j++){
            printf("\t %d",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}



int main(){
    int row=4,col=4;
    int matrix[row][col];
    int target;

    readingMatrix(matrix);

    printingMatrix(matrix);


    printf("Enter element to be search : ");
    scanf("%d",&target);

    int isFound=linearSearch(matrix,target);

    if(isFound==1){
        printf("%d is present \n",target);
    }else{
        printf("%d is not present  \n",target);
    }


    int l=0,r=row*col-1;
    printf("%d is present %d \n",target,usingBinarySearch(matrix,l,r,target));



}