#include<stdio.h>
#define N 14

int main(){
    
    int arr[N]={1,-3,4,-2,4,0,1,-3,5,6,10,-2};

    int max_sum=arr[0];
    int current_sum=0;

    for (int i=0;i<N;i++){
        current_sum+=arr[i];

        if (current_sum>max_sum){
            max_sum=current_sum;
        }
        if(current_sum<0){
            current_sum=0;
        }
    }
    printf("%d\n",max_sum);
}