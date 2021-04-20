#include<stdio.h>

int main(){
    int arr[8]={1, 2, 3, -1, -2, -3, 0, 0};
    int n=8;
    
    float zero_counter=0,pos_counter=0,neg_counter=0;
    for(int i=0;i<n;i++){
        if(arr[i]==0){
            zero_counter+=1;
        }
        else if (arr[i]>0)
        {
            pos_counter+=1;
        }else
        {
            neg_counter+=1;
        }
    }
    printf(" %f\n %f\n %f \n",pos_counter/n,neg_counter/n,zero_counter/n);
}