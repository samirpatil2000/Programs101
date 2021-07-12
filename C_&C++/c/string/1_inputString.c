#include<stdio.h>

int main(){
    char str[100];
    int i=0,word_count=1,line_count=1,char_count=1;
    printf("Enter the character : \n");

    scanf("%c",&str[i]);
    while(str[i] != '*'){
        i++;
        scanf("%c",&str[i]);
    }
    str[i]='\0';
    i=0;
    puts(str);
}