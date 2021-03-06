#include<stdio.h>
// sort array using QUICK Sort 


// I really don't know why hte hell is htis is not working


int partition(int arr[],int lb,int ub){
    int pivot=arr[lb];
    int left=lb;
    int right=ub;
    while(left<right){
        while(arr[left]<=pivot){
            left++;
        }
        while(arr[right]>pivot){
            right--;
        }
        if(left<right){
            int temp=arr[right];
            arr[right]=arr[left];
            arr[left]=temp;
        }
    }
    int temp=arr[right];
    arr[right]=arr[lb];
    arr[lb]=temp;
    printf("right %d\n",right);
    printArray(arr);
    return right;
}

int quickSort(int arr[],int lb,int ub){
    if(lb<ub){
        int loc=partition(arr,lb,ub);
        quickSort(arr,lb,loc-1);
        quickSort(arr,loc+1,ub);
    }
}


void printArray(int arr[],int len){
    for(int i=0;i<len;i++){
        printf("%d\t",arr[i]);
    }
    printf("\n");
}

int main(){
    int arr[]={78,54,59,87,84,98,34,58,53,99};
    int len=sizeof(arr)/sizeof(arr[0]);
    quickSort(arr,0,len);
    printArray(arr,len);
}