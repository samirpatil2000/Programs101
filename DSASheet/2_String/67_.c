#include<stdio.h>
#include<string.h>

int main(){
    char str[]="0100110101";
    int ptr0=0,ptr1=0,len=strlen(str),i=0,count=0;

    while(i<len){
        if(str[i] =='0'){
            ptr0++;
        }else{
            ptr1++;
        }
        if(ptr0==ptr1){
            count++;
        }
        i++;
    }
    if(ptr0 != ptr1){
        printf("Not found ..!\n");
    }
    printf("Count %d\n",count);
}