#include<stdio.h>

int max(int a,int b){
    if(a>b){
        return a;
    }
    return b;
}


int maxInArray(int arr[],int idx,int len){
    if(idx==0){
        return arr[idx];
    }
    int misa=maxInArray(arr,idx-1,len);
    return max(arr[idx],misa);
}

int main(){
    int arr[]={1,23,4,5,43,26,54,87,65};
    int len=sizeof(arr)/sizeof(arr[0]);
    printf("The max element in array is : %d\n" ,maxInArray(arr,len-1,len));
}