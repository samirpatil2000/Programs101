#include<stdio.h>

int main(){
    int counter=0,a=1;
    int N=9;
    while(a*a<N){
        counter++;
        a++;
    }
    printf("Counter %d\n",counter);
}