#include<stdio.h>

int main(){
    int num1,num2,*ptr1,*ptr2;
    num1=10;
    num2=12;
    ptr1=&num1;
    ptr2=&num2;
    int sum= *ptr1 + *ptr2;

    printf(" the sum is %d\n",sum);

    *ptr2 += 1;
    
    int mul=sum * (*ptr1);

    printf(" mul  is %d\n",mul);
    
    printf("the *ptr2 += 1 is %d\n",*ptr2);
}