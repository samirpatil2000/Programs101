#include<stdio.h>
// sort array using Insertion Sort 
int main(){
    int n=10;
    int arr[10]={78,54,59,87,84,98,34,58,53,99};

    printf("\nPrinting the array before sorting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }
    for(int i=1;i<n;i++){
        int temp=arr[i];
        int j=i-1;
        while ( j>=0 && arr[j]>temp){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=temp;
    }

    printf("\nPrinting the array after sorting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }
}