#include<stdio.h>

void swap(int a,int b){
    int temp=a;
    a=b;
    b=temp;
}

int main(){
    int arr[]={6,3,2,1,5},a=3,b=4;
    int length=sizeof(arr)/sizeof(arr[0]);

    int left=0,i=0,right=length-1;

    while(i<=right){
        if(arr[i]<a){
            int temp=arr[i];
            arr[i]=arr[left];
            arr[left]=temp;
            i++;left++;
        }
        else if(arr[i]>b){
            int temp=arr[i];
            arr[i]=arr[right];
            arr[right]=temp;
            right--;
        }else{
            i++;
        }
        
    }

    for(int j=0;j<length;j++){
        printf("\t %d",arr[j]);
        
    }
    printf("\n");
}