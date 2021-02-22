#include<stdio.h>


void printArray(int arr[],int len){
    if(len==0){
        return;
    }
    printArray(arr,len-1);
    printf("%d \t",arr[len-1]);
}

int main(){
    int arr[]={1,23,4,5,43,26,54,87,65};
    int len=sizeof(arr)/sizeof(arr[0]);
    printf("%d\n",len);
    printArray(arr,len);
    printf("\n");
}