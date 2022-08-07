#include<stdio.h>
#include<string.h>

int method_1(char str[]){

    int len=strlen(str),start=0 ,end=len-1;
    while (start<end && str[start]==str[end])
    {
        start++;end--;
    }
    if (str[start]==str[end]){return 1;}
    return 0;

}

int method_2(char str[]){
    int len=strlen(str),start=0,end=len-1,flag=1;
    while (start<end){
        if(str[start] != str[end]){
            flag=0;
            return 0;
        }
        start++;end--;
    }
    return 1;
    
}

int main(){
    char str[100];
    
    printf("\nEnter the string : ");
    gets(str);
    if (method_1(str)==1)
    {
        printf("\n Method 1 String is palindrome : ");

    }else{
        
        printf("\n Method 1 String is not palindrome : ");
    } 
    if (method_2(str)==1)
    {
        printf("\n Method 2 String is palindrome : ");

    }else{
        
        printf("\n Method 2 String is not palindrome : ");
    } 
    
    puts(str);  


    
}