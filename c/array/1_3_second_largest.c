#include<stdio.h>
// To find the second largest element from the array

int main(){
    int n=5;
    int second_largest,large;
    int arr[n],i=0;
    for(int i=0;i<n;i++){
        printf("\narr[%d]=",i);
        scanf("%d",&arr[i]);
        // arr[i]=i;
    }
    
    for(int i=0;i<n;i++){
        printf("\narr[%d]=%d",i,arr[i]);
        if ( arr[i] > large ){
            large=arr[i];
        }
    }
    for (int i=0;i<n;i++){
        if (arr[i] != large){
            if(second_largest<arr[i]){
                second_largest=arr[i];
                printf("%d",second_largest);
            }
        }
    }
    printf("\nLargest in number in array is = %d \n",large);
    printf("\nSecond Largest in number in array is = %d \n",second_largest);
}