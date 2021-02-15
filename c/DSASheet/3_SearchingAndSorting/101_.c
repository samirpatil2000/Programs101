#include<stdio.h>


int findFirstOccurence(int arr[],int left,int right,int val){
    int mid=(left+right)/2;
    if(arr[mid]==val && arr[mid]!=arr[mid-1]){
        return mid;
    }else if(arr[mid]==val && arr[mid]==arr[mid-1]){
        return findFirstOccurence(arr,left,mid,val);
    }else{
        if(arr[mid]>val){
            return findFirstOccurence(arr,left,mid,val);
        }else{
            return findFirstOccurence(arr,mid,right,val);
        }
    }
    if(left>=right){
        return -1;
    }
}
int findLastOccurence(int arr[],int left,int right,int val){
    int mid=(left+right)/2;
    if(arr[mid]==val && arr[mid]!=arr[mid+1]){
        return mid;
    }else if(arr[mid]==val && arr[mid]==arr[mid+1]){
        return findLastOccurence(arr,mid,right,val);
    }else{
        if(arr[mid]>val){
            return findLastOccurence(arr,left,mid,val);
        }else{
            return findLastOccurence(arr,mid,right,val);
        }
    }
    if(left>=right){
        return -1;
    }
}
int main(){
    int arr[]={1 ,3, 5, 5, 5, 5, 67, 123, 125};
    int len=sizeof(arr)/sizeof(arr[0]);
    printf("The first occurence is : %d\n",findFirstOccurence(arr,0,len,5));
    printf("The first occurence is : %d\n",findLastOccurence(arr,0,len,5));

}