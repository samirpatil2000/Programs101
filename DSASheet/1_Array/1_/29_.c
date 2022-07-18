#include<stdio.h>

void bySorting(int arr[],int length){
    int max_count=0;
    int current_count=1;
    for(int i=0;i<length-1;i++){
        while(arr[i]==arr[i+1]-1){
            current_count++;
            i++;
        }
        if(current_count>max_count){
            max_count=current_count;
            current_count=1;
        }
    }
    printf("%d\n",max_count);
}

int main(){
    int arr[]={2,3,5,6,7,8};
    int length=sizeof(arr) / sizeof(arr[0]);
    bySorting(arr,length);
}