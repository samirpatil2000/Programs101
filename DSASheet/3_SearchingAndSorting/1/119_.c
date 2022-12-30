#include<stdio.h>


int searchIndex(int arr[],int left,int right,int val){
    int mid=(left+right)/2;
    if(arr[mid]==val){
        return mid;
    }
    if(arr[mid]>val && arr[mid-1]<=val){
        return mid-1;
    }else{
        if(arr[mid]>val){
            return searchIndex(arr,left,mid,val);
        }else{
            return searchIndex(arr,mid,right,val);
        }
    }
    if(left>right){
        return -1;
    }
}

int main(){
    int arr[]={1,2,3, 4, 5,6, 7};
    int len=sizeof(arr)/sizeof(arr[0]);

    int in=searchIndex(arr,0,len,3);
    printf("at index %d %d\n",in,arr[in]);
    int total_power=0,count=0;
    for(int i=0;i<=in;i++){
        total_power+=arr[i];
        count++;
    }
    printf("The total power of %d is %d\n",count,total_power);

}