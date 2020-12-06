#include<stdio.h>
#define N 5
/*
    THINK YOU CAN DO THIS 
    */



int reverseArray(int arr[N],int start,int end){
    while(start<end){
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++; 
        end--;
    }
}

int main(){
    int arr[N]={1,2,3,4,5};
    // int k=4; // rotate by

    // right rotation

    /*
    reverseArray(arr,0,N-k-1);
    reverseArray(arr,N-k,N-1);
    // for(int i=0;i<N;i++){
    //     printf("\t %d",arr[i]);
    // }
    // printf("\n");
    reverseArray(arr,0,N-1);
    for(int i=0;i<N;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
    */

    for(int i=0;i<N;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
    // left rotation 
    int k=1; // rotate by
    reverseArray(arr,0,k-1);
    reverseArray(arr,k,N-1);
    
    reverseArray(arr,0,N-1);
    for(int i=0;i<N;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");


}