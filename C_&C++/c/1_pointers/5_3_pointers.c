#include<stdio.h>

int main(){
    int num1,num2,*ptr1,*ptr2;
    num1=10;
    num2=12;
    ptr1=&num1;

    ptr2=ptr1;
    printf("AFTER \n   ptr2=ptr1 \n     is %d\n",*ptr2);

    ptr2=&num2;
    printf("AFTER \n   ptr2=&num2 \n    is %d\n",*ptr2);

    *ptr2=*ptr1;
    printf("AFTER \n   *ptr2=*ptr1 \n   is %d\n",*ptr2);
}