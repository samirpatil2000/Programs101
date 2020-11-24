#include<stdio.h>

// To find the smallest number from the array 

int main(){
    int n=5;
    int smallest;
    int arr[n],i=0;
    for(int i=0;i<n;i++){
        printf("\narr[%d]=",i);
        scanf("%d",&arr[i]);
        // arr[i]=i;
    }
    smallest=arr[0];
    for(int i=0;i<n;i++){
        printf("\narr[%d]=%d",i,arr[i]);
        if ( arr[i] < smallest ){
            smallest=arr[i];
        }
    }
    printf("\nSmallest in number in array is = %d \n",smallest);
}