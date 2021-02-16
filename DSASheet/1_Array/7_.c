#include<stdio.h>

struct pair{
    int max;
    int min;
};


struct pair findPair(int arr[],int left,int right){
    struct pair minmax,minmax_left,minmax_right;

    if(right==left){
        minmax.max=arr[left];
        minmax.min=arr[right];
        return minmax;
    }
    if(right==left+1){
        if(arr[right]>arr[left]){
            minmax.min=arr[left];
            minmax.max=arr[right];
        }else{
            minmax.max=arr[left];
            minmax.min=arr[right];
        }
        return minmax;
    }
    int mid=(left+right)/2;
    minmax_left=findPair(arr,left,mid);
    minmax_right=findPair(arr,mid,right);
    
    if(minmax_left.min<minmax_right.min){
        minmax.min=minmax_left.min;
    }else{
        minmax.min=minmax_right.min;
    }

    if(minmax_left.max>minmax_right.max){
        minmax.max=minmax_left.max;
    }else{
        minmax.max=minmax_right.max;
    }
    return minmax;
}


void Method_1(int arr[],int len){
    int min=arr[0],max=arr[1];
    if(arr[0]>arr[1]){
        min=arr[1];
        max=arr[0];
    }
    for(int i=2;i<len;i++){
        if(arr[i]>max){
            max=arr[i];
        }
        if(arr[i]<min){
            min=arr[i];
        }
    }
    printf("The min=%d & max=%d \n",min,max);
}


int main(){
    int arr[]={ 9, 2, 5, 6, -7, 8, 9 };
    int len=sizeof(arr)/sizeof(arr[0]);
    struct pair minmax;
    Method_1(arr,len);
    minmax=findPair(arr,0,len);
    printf("Using MINMAX min = %d and max = %d\n",minmax.min,minmax.max);
}