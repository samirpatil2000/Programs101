#include<stdio.h>

 
void printArray(int arr[]) 
{ 
	for (int i = 0; i < 6; i++) 
		printf("%d\t",arr[i]);
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

int findPivotElement(int arr[],int left,int right,int k){
    // printf("#findpivot\n");
    int mid=partition(arr,left,right);
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
	int arr[] = {10, 7, 8, 9, 1, 5}; 
	int n = sizeof(arr) / sizeof(arr[0]); 
    printf("the \n");
	// quickSort(arr, 0, n - 1); 

	// printArray(arr, n); 
    // printf("The partian\n");
    // partition(arr,0,n-1);
    int m=2;
    printf("The %dth smallest element is %d\n",m,findPivotElement(arr,0,n-1,m-1));

	return 0; 
}