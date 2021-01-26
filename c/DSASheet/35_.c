#include<stdio.h>
#include<stdlib.h>

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main(){
    int M=5;
    int arr[]={3, 4, 1, 9, 56, 7, 9, 12};
    // int arr[]={7 ,3 ,2 ,4 ,9 ,12 ,56};
    int length=sizeof(arr)/sizeof(arr[0]);
    qsort(arr,length,sizeof(int),cmpfunc);

    printf("\nAfter sorting the list is: \n");
    for( int i = 0 ; i < length; i++ ) {   
        printf("%d ", arr[i]);
    }
    printf("\n");

    int min=arr[M-1]-arr[0],i=0;
    while(i+M-1<length){
        if(arr[i+M-1]-arr[i]<min){
            min=arr[i+M-1]-arr[i];
        }
        i++;
    }
    printf("The min is %d \n",min);

}