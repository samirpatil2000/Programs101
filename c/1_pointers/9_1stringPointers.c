#include<stdio.h>

int main(){
    char str[]="SamirPatil";
    char *pstr;
    pstr=str;
    int upper=0,lower=0;

    printf("The string is \n ");
    while (*pstr != '\0'){
        if (*pstr >='A' && *pstr <='Z'){
            upper++;
        }else if (*pstr >= 'a' && *pstr <='z'){
            lower++;
        }
        pstr++;
    }
    printf("\n");
    printf("Upper and Lower : %d , %d\n",upper,lower);
    
    return 0;
    
}