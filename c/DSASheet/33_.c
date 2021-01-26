#include<stdio.h>

int main(){
    int arr[]={1,2,3,4,6};
    int length=sizeof(arr)/sizeof(arr[0]);
    int ans=10,flag=0;
    printf("%d\n",length);
    for(int i=0;i<length;i++){
        int current_sum=0,j=i+1,k=length-1;
        while(j<length && k >= i+1){
            current_sum=0;
            current_sum+=arr[i];
            current_sum+=arr[j];
            current_sum+=arr[k];
            // printf("%d\n",current_sum);
            if(current_sum==ans){
                flag=1;
                break;
            }else{
                if(current_sum<ans){
                    j++;
                }else if(current_sum>ans){
                    k--;
                }
            }
        }
    }
    if(flag==1){
        printf("Found..!\n");
    }else{
        printf("Not Found..!\n");
    }
}