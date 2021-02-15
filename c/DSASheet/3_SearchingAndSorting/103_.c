#include<stdio.h>



int findPivotElement(int arr[],int left,int right){
    int mid=(left+right)/2;

    if(arr[mid]>arr[mid+1]){
        return arr[mid];
    }else{
        if(arr[mid]>arr[0]){
            return findPivotElement(arr,mid,right);
        }else{
            return findPivotElement(arr,left,mid);
        }
    }
    if(left>=right){return -1;}
}

int main(){
    int arr[]={4,5,6,7,8,0,1,2,3};
    int len=sizeof(arr)/sizeof(arr[0]);

    printf("The pivot element is %d\n",findPivotElement(arr,0,len));
}