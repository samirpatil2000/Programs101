#include<stdio.h>

int main(){
    int arr[]={11,14,15,99};
    int n=sizeof(arr)/sizeof(arr[0]);
    int ans=0,i=0,j=n-1;

    while(i<j){
        if(arr[i]==arr[j]){
            i++;j++;
        }
        if(arr[i]>arr[j]){
            arr[j-1]=arr[j-1]+arr[j];
            j--;
            ans++;
        }
        else
        {
            arr[i+1]=arr[i+1]+arr[i];
            i++;ans++;
        }
    }
    printf("\n %d \n",ans);
}