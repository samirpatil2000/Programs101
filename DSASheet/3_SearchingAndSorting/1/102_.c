#include<stdio.h>


int main(){
    int arr[] = {15, 2, 45, 12, 7};
    int len=sizeof(arr)/sizeof(arr[0]);

    for(int i=0;i<len;i++){
        if(arr[i] == i+1){
            printf("arr[%d]=%d",i+1,arr[i]);
        }
    }
    printf("\n");

}