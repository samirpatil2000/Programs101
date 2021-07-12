#include<stdio.h>




void printArray(int arr[]){
    for(int i=0;i<5;i++){
        printf("%d\t",arr[i]);
    }
    printf("\n");
}


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

void quickSort(int arr[], int low, int high) 
{ 
	if (low < high) 
	{ 
		int pi = partition(arr, low, high); 
		quickSort(arr, low, pi - 1); 
		quickSort(arr, pi + 1, high); 
	} 
}


int main(){
    int arr[]={5, 3, 8,6, 2};  
    int len=sizeof(arr)/sizeof(arr[0]);
    partition(arr,0,len);
}