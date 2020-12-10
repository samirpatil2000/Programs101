#include<stdio.h>
#define N 5
/*
    THINK YOU CAN DO THIS 
    */


void printArray(int arr[N]){
    for(int i=0;i<N;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
}


int reverseArray(int arr[N],int start,int end){
    while(start<end){
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++; 
        end--;
    }
}

int rotatedArray(int arr[N]){ 
    //rotated by one at a time
    int i=0;
    int temp=arr[0];
    while (i<N-1){
        arr[i]=arr[i+1];
        i++;
    }
    arr[i]=temp;
    
}

int main(){
    int arr[N]={1,2,3,4,5};

    int arr_2[N]={1,2,3,4,5};
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

    printf("\nRotation by direct reverse function by once : \n");
    printf("\n");
    // left rotation 
    int k=3; // rotate by
    reverseArray(arr,0,k-1);
    reverseArray(arr,k,N-1);
    reverseArray(arr,0,N-1);
    printArray(arr);



    rotatedArray(arr_2);
    // rotatedArray(arr_2);
    printf("Rotation by direct rotate function : \n");
    printArray(arr_2);



}