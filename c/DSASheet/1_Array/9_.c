#include<stdio.h>

void swap(int a,int b){
    int temp=a;
    a=b;
    b=temp;
}

void printArray(int arr[],int n){
    for(int i=0;i<n;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
}
int main(){
    // int arr[]={0, 2, 1, 2, 0};
    int arr[]={0, 2, 1, 2,1,2};
    int n=6,low=0,mid=0,high=n-1;
    printArray(arr,n);

    while (mid<=high)
    {
        if (arr[high] == 2 ){
            high--;
        }
        if(arr[mid]==1){
            mid++;
        }else
        {
            if (arr[mid]==0)
            {
                // swap(arr[low],arr[mid]);
                int temp = arr[low];
                arr[low]=arr[mid];
                arr[mid]=temp;
                mid++;low++;
            }else
            {
                // swap(arr[high],arr[mid]);
                int temp = arr[high];
                arr[high]=arr[mid];
                arr[mid]=temp;
                mid++;
                high--;
            }
        }
    }

    printArray(arr,n);

    
}