#include<stdio.h>

int main(){
    int prices[]= {7,1,5,3,6,4};
    // int prices[] ={7,6,4,3,1};
    int length=6;
    int max_diff=0;
    for(int i=0;i<length;i++){
        for(int j=i+1;j<length;j++){
            int diff=0;
            if(prices[i]<prices[j]){
                diff=prices[j]-prices[i];
            }
            if(max_diff<diff){
                max_diff=diff;
            }
        }
    }
    printf("%d\n",max_diff);

}