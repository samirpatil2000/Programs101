#include<stdio.h>

int main(){
    int num , *ptr;
    num=10;
    ptr=&num;
    
    printf("\n  *ptr  = %d\n",*ptr);
    printf("   num  = %d\n",num); 
    printf("   ptr  = %p\n",ptr);
    printf("   &num = %p\n",&num);


}