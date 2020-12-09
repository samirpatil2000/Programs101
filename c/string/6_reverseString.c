#include<stdio.h>
#include<string.h>


int main(){
    char str[100],reverse[100];
    printf("\nEnter string : ");
    gets(str);

    int len=strlen(str);
    int i=0,j=len-1;
    while (i<j){
        char temp=str[i];
        str[i]=str[j];
        str[j]=temp;
        i++;
        j--;
    }
    puts(str);

}