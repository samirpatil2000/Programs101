#include<stdio.h>
#include<string.h>

int main(){
    char str[100];
    printf("Enter the string : ");
    gets(str);

    int len=strlen(str),start=0,end=len-1;
    while (start<end)
    {   char temp=str[start];
        str[start]=str[end];
        str[end]=temp;
        start++;
        
    }
    printf("\nThe reverse string is : ");
    puts(str);
    
}