#include<stdio.h>

int main(){
    int arr[]={6,9,9};
    int length=sizeof(arr)/sizeof(arr[0]);

    int max_heigth=arr[0];
    if(arr[0]>arr[length-1]){
        max_heigth=arr[length-1];
    }
    int volume=0;
    for(int i=1;i<length-1;i++){
        if(arr[i]<max_heigth){
            int x=max_heigth-arr[i];
            volume+=x;
        }
    }
    printf("The volume of water trapped is %d\n",volume);
}