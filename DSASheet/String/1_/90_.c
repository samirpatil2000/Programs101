#include<stdio.h>
#include<string.h>

int main(){
    char str[]="ABC";
    int len=strlen(str),i=0,j=len-1,count=0;

    while(i < j){

        if(str[i]==str[j]){
            i++;j--;
        }else{
            j--;
            count++;
        }
    }
    printf("Ans : %d\n",count);
}