#include<stdio.h>

int main(){
    char str[100],copyStr[100];
    char *pstr,*pcopyStr;
    pstr=str;
    pcopyStr=copyStr;

    printf("\nEnter the string :");
    gets(str);
    while (*pstr != '\0'){
        *pcopyStr = *pstr;
        pstr++;pcopyStr++;
    }
    *pcopyStr='\0';
    printf("\nThe copied text is \n");
    // pcopyStr=0;
    int i=0;
    printf("%c",*pcopyStr);
    while (*pcopyStr != '\0')
    {
        printf("%c\n",*pcopyStr);
        pcopyStr++;
        printf("%d\n",copyStr[i]);
        i++;
    }
    return 0;
    

    // puts(copyStr);
    // printf("\n");
    

}