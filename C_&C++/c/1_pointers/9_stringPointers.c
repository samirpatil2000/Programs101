#include<stdio.h>

int main(){
    char str[]="SamirPatil";
    char *pstr;
    pstr=str;

    printf("The string is \n ");
    while (*pstr != '\0'){
        printf("%c",*pstr);
        pstr++;
    }
    printf("\n");
    return 0;
    
}