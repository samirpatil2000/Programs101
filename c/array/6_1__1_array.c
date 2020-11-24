#include<stdio.h>

int main(){
    int n=10;
    int arr[n],i=0,sum=0;
    for(int i=0;i<n;i++){
        // printf("\narr[%d]=",i);
        // scanf("%d",&arr[i]);
        arr[i]=i;
    }
    for(int i=0;i<n;i++){
        printf("\narr[%d]=%d",i,arr[i]);
        sum+=arr[i];

    }
    int mean=(float)sum/n;
    printf("\n Sum of elements is array = %d",sum);
    printf("\n Mean of array = %d\n",mean);
}