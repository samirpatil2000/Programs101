#include<stdio.h>

// void swap(int arr,int a,int b){
//     int A=a,B=b;
//     int temp;
//     arr[A]=arr[B];

// }
void printArray(int arr[],int n){
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        printf("\t %d",arr[i]);
    }
    printf("\n");
}

int main(){
    int arr[] = {-5, -3, 4, 5, -6, -2, 8, 9, -1, -4};
    int n=10;
    printArray(arr,n);
    int low=0,high=n-1;
    while (low<=high)
    {
        if(arr[low]<0 && arr[high]>=0){
            int temp=arr[low];
            arr[low]=arr[high];
            arr[high]=temp;
            low++;high--;
        }
        if(arr[low]>=0){low++;}
        if(arr[high]<0){high--;}
    }
    printArray(arr,n);
    printf("%d\n",low);
    int start=1;

    while (low<n-1)
    {
        int temp=arr[start];
        arr[start]=arr[low];
        arr[low]=temp;
        start+=2;low++;
    }
    printArray(arr,n);
    
    
}