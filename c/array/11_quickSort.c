#include<stdio.h>
// sort array using QUICK Sort 


// I really don't know why hte hell is htis is not working

void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 

int partian(int arr[],int lb,int ub){
    int pivot=arr[0];
    int start=lb,end=ub;

    while(start<end){

        while(arr[start]<=pivot){
            start++;
        }
        while(arr[end]>pivot){
            end--;
        }
        swap(&arr[start],&arr[end]);
        // int temp=arr[start];
        // arr[start]=arr[end];
        // arr[end]=temp;
    }
    swap(&arr[0],&arr[end]);
    // arr[0]=arr[end];
    // arr[end]=pivot;

    return end;
}

int quickSort(int arr,int lb,int ub){
    if(lb<ub){
        int loc=partian(arr,lb,ub);
        quickSort(arr,lb,loc-1);
        quickSort(arr,loc+1,ub);
    }
}



int main(){
    int n=10,min,temp;
    int arr[10]={78,54,59,87,84,98,34,58,53,99};
    int lb=0,up=n-1;

    printf("\nPrinting the array before sorting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }
    quickSort(arr,lb,up);
    

    printf("\nPrinting the array after sorting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }



}