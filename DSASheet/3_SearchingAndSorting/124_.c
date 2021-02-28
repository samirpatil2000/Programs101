#include<stdio.h>

void swap(int a,int b){
    int temp=a;
    a=b;
    b=temp;
}



int partian(int arr[],int left,int right){
    printf("#parti\n");
    int mid=left+right;
    while(left<right){
        while(arr[left]<=arr[mid]){
            left++;
        }
        while(arr[right]>arr[mid]){
            right--;
        }
        swap(arr[left],arr[right]);
    }
    swap(arr[right],arr[mid]);
    printf("right %d\n",right);
    return right;
}

int findPivotElement(int arr[],int left,int right,int k){
    printf("#findpivot\n");
    int mid=partian(arr,left,right);
    printf("Mid %d\n",mid);
    if(mid==k){
        return arr[mid];
    }else{
        if(mid<k){
            return findPivotElement(arr,mid+1,right,k);
        }else{
            return findPivotElement(arr,left,mid-1,k);
        }
    }
    if(left>right){return -1;}
}
int main(){ 
    int arr[]={10, 3, 8,6, 2};   // i
    int len=sizeof(arr)/sizeof(arr[0]);
    printf("#\n");
    printf("The %d\n",findPivotElement(arr,0,len-1,2));
}