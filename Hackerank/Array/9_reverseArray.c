#include<stdio.h>
#define N 2

// https://www.hackerrank.com/challenges/arrays-ds/problem


int reverseArray(int arr[N],int from,int upto){
    for(int i=from;i<upto/2;i++){
        int temp=arr[upto-i-1];
        arr[upto-i-1]=arr[i];
        arr[i]=temp;
    }
}

int reverseArray2(int arr[N],int start,int end){
    while(start<end){
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++; 
        end--;
    }
}

int main(){
    int arr[N]={1,2};
    int k=2; // rotate by

    reverseArray(arr,0,N);
    for(int i=0;i<N;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
    reverseArray2(arr,0,N-1);
    for(int i=0;i<N;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");


}