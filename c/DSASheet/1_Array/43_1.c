#include<stdio.h>

// Search in a row wise and column wise sorted matrix

// Using recursion

int recursionSearch(int arr[4][4],int i,int j,int target){
    if(i>3 || j<0){
        return 0;
    }
    if(target==arr[i][j]){
        return 1;
    }else{
        if(target< arr[i][j]){
            return recursionSearch(arr,i,j-1,target);
        }else{
            return recursionSearch(arr,i+1,j,target);
        }
    }
}

int usingLoop(int arr[4][4],int target){
    int i=0,j=4-1;
    while(i<4 && j>=0){    
        if(target==arr[i][j]){
            return 1;
        }else{
            if(target< arr[i][j]){
                j--;
            }else{
                i++;
            }
        }
        
    }
}



void printingMatrix(int arr[4][4]){
    
    for (int i=0;i<4;i++){
        printf("\n");
        for (int j=0;j<4;j++){
            printf("\t %d",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


int main(){
    int target;
    int mat[4][4] = { 
        { 10, 20, 30, 40 }, 
        { 15, 25, 35, 45 }, 
        { 27, 29, 37, 48 }, 
        { 32, 33, 39, 50 }, 
    };

    printingMatrix(mat);

    printf("Enter the number that to be search : ");
    scanf("%d",&target);


    int i=0,j=4-1;
    int recursion_search=recursionSearch(mat,i,j,target);
    int using_loop=usingLoop(mat,target);

    printf("%d\n",recursion_search);
    printf("%d\n",using_loop);

}