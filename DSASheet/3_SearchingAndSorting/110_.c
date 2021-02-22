#include<stdio.h>



int search(int arr[],int low,int high,int target){
    int mid=(low+high)/2;
    if(arr[mid]==target){
        return mid;
    }else{
        if(arr[mid]>target){
            return search(arr,low,mid,target);
        }else{
            return search(arr,mid,high,target);
        }
    }
    if(low>=high){
        return -1;
    }
}

int main(){
    int arr[]={2,3,5,5,20,80};
    int len=sizeof(arr)/sizeof(arr[0]);
    int diff=78;
    
    for(int i=0;i<len;i++){
        int y=arr[i]+diff;
        if(search(arr,i,len,y)!=-1){
            printf("Pair is %d %d\n",arr[i],y);
            break;
        }
    }
}