#include<stdio.h>
#include<string.h>
int main(){
    char str[20];
    printf("Enter the string : \n");
    gets(str);
    int len=strlen(str);
    int start=0,end=len-1,flag=1;
    printf("%d\n",len);
    while (start<=end){
        if (str[start] != str[end]){
            flag=0;
            break;
        }
        start++;
        end--;
    }
    if(flag==1){
        printf("PALINDROME \n");
    }else{
        printf("not PALINDROME \n");
    }
}