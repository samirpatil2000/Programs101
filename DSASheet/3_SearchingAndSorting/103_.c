#include<stdio.h>



int findTargetElement(int arr[],int left,int right,int target){
    int mid=(left+right)/2;

    if(arr[mid]==target){
        return mid;
    }else if(arr[left]<arr[mid]){
        if(arr[left]<=target && arr[mid]>=target){
            return findLargetElement(arr,left,mid,target);
        }else{
            return findLargetElement(arr,mid,right,target);
        }
    }else{
        if(arr[mid]<=target && arr[right]>=target){
            return findLargetElement(arr,mid,right,target);
        }else{
            return findLargetElement(arr,left,mid,target);
        }
    }
    if(left>right){
        printf("Element Does not exists :\n");
        return -1;
    }
}


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
    int target=4;

    printf("The pivot element is %d\n",findPivotElement(arr,0,len));
    printf("The element is at index %d\n",findTargetElement(arr,0,len,target));
}