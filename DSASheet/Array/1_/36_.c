#include<stdio.h>


int brute(int arr[],int length,int X){
    int min=999,cs=0;
    for(int i=0;i<length;i++){
        int current_sum=0,count=0;
        for(int j=i;j<length;j++){
            current_sum+=arr[j];
            count+=1;
            if(current_sum>X && count<min){
                min=count;
                cs=current_sum;
            }
        }
    }
    return min;
}

int optimuim(int arr[],int length,int X){
    int min=999,count=0,current_sum=0,left=0,right=0;
    while(left<=right && right<length){
        if(current_sum<=X){
            current_sum+=arr[right];
            right++;
            printf("%d\n",current_sum);
        }
        if(current_sum>X){
            count=right-left;
            if(min>count){
                min=count;
            }
            current_sum-=arr[left];
            left++;
        }
    }
    return min;
}

int main(){
    int arr[]={1, 10, 5, 2, 7}, X=9;
    int length=sizeof(arr)/sizeof(arr[0]);
    printf("The min length is subarray using brute : %d\n",brute(arr,length,X));
    printf("Using otp %d\n",optimuim(arr,length,X));
}