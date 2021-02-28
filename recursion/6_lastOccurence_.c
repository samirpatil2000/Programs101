#include<stdio.h>


int listOcc(int arr[],int len,int n,int val){
    if(n==len){
        return -1;
    }
    if(arr[n]==val){
        return n;
    }
    int count=0;
    printf("Count %d\n",count++);
    return listOcc(arr,len,n-1,val);
}

int main(){
    int arr[]={1,23,4,5,43,26,5,87,65};
    int len=sizeof(arr)/sizeof(arr[0]);
    printf("The last occurence of the element in array is : %d\n" ,listOcc(arr,len,len-1,5));
}