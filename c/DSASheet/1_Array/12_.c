#include<stdio.h>

void printArray(int arr[],int n){
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        printf("\t %d",arr[i]);
    }
    printf("\n");
}
int rotatedArray(int arr[],int n){ 
    //rotated by one at a time
    int i=0;
    int temp=arr[0];
    while (i<n-1){
        arr[i]=arr[i+1];
        i++;
    }
    arr[i]=temp;
    
}
int main(){
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr)/sizeof(arr[0]);
    printArray(arr,n);
    // rotatedArray(arr,n);    
    // printArray(arr,n);

    int temp=arr[n-1];
    for(int i=n-1;i>0;i--){
        arr[i]=arr[i-1];
    }
    arr[0]=temp;
    printArray(arr,n);
}