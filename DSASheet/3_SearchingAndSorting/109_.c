#include<stdio.h>

int max(int a,int b){
    if(a>b){
        return a;
    }
    return b;
}
int abs(int a){
    if(a<0){
        a=0-a;
        return a;
    }
    return a;
}

int main(){
    int arr[]={2, 4, 6, 8, 6,8};
    int target=6;
    int k=2;
    int len=sizeof(arr)/sizeof(arr[0]);
    int i=0;
    while(i<len){
        if(arr[i]==target){
            printf("%d is at %d\n",target,i);
            break;
        }
        int step=max(1,abs(arr[i]-target)/k);
        i=i+step;
        // printf("i %d\n",i);
    }
}