#include<stdio.h>

int main(){
    int num , *ptr;
    num=10;
    ptr=&num;
    printf("the ptr is %d\n",ptr);
    printf("the *ptr is %d\n",*ptr);
}