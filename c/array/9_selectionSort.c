#include<stdio.h>
// sort array using Insertion Sort 
int main(){
    int n=10,min,temp;
    int arr[10]={78,54,59,87,84,98,34,58,53,99};

    printf("\nPrinting the array before sorting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }
    for(int i=0;i<n-1;i++){
        int temp=arr[i];
        int min=i;
        for (int j=i;j<n;j++){
            
            if(arr[j]<arr[min]){
                min=j;
            }
        }
        arr[i]=arr[min];
        arr[min]=temp;
    }

    printf("\nPrinting the array after sorting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }



}