#include<stdio.h>
#define MAX 100

int main(){
    int arr[]={1,8,3,4,5,7,6,10,8,9};
    int len=sizeof(arr)/sizeof(arr[0]);
    int ptr_arr[MAX]={0};
    int mis,rep;


    for(int i=0;i<len;i++){
        if(ptr_arr[arr[i]-1]==1){
            rep=arr[i];
        }else{
            ptr_arr[arr[i]-1]=1;
        }
    }
    for(int j=0;j<len;j++){
        if(ptr_arr[j]==0){
            mis=j+1;
        }
    }
    printf("The missing = %d and repeated =%d \n",mis,rep);

}