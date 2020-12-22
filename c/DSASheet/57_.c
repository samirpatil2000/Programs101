#include<stdio.h>
#include<string.h>

int main(){
    char str[100];
    
    printf("\nEnter the string : ");
    gets(str);
    
    int len=strlen(str),start=0 ,end=len-1;

    while (start<end && str[start]==str[end])
    {
        start++;end--;
    }
    if (str[start]==str[end])
    {
        printf("\nString is palindrome : ");

    }else{
        
        printf("\n String is not palindrome : ");
    }
    puts(str);   
}