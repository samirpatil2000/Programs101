#include<stdio.h>


void reArrange(int arr[],int n){
    int start=0;
    int end=n-1;
    while (start < end)
    {
        if (arr[start] < 0 && arr[end] < 0)
        {
            start++;
        }
        else if (arr[end] >= 0 && arr[start] >=0)
        {
            end--;
        }
        // swapping
        else if (arr[start] > 0 && arr[end] < 0)
        {
            int temp=arr[end];
            arr[end]=arr[start];
            arr[start]=temp;
        }else{
            start++;
            end--;
        }
        
        // start++;
        // end--;
    }
    
}

void printArray(int arr[],int n){
    for (int i = 0; i < n; i++)
    {
        printf("\t %d",arr[i]);
    }
    printf("\n");
}


int main(){
    int arr[] = { 9, 2, 5, 6, -7, 8, 9 };
    int n = sizeof(arr) / sizeof(arr[0]);
    printArray(arr,n);
    reArrange(arr,n);
    printArray(arr,n);
}

//https://www.freelancer.in/projects/php/build-social-media-website-28680696/details