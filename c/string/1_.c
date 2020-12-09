#include<stdio.h>

char str[100];
int i=0,n;





void readingString(){
    printf("Enter letters in string :\n");
    char ch=getchar;
    while(ch != '*' ){
        str[i]=ch;
        i++;
        ch=getchar();
    }
    str[i]='\0';

}

void printString(){
    while(str[i] !='\0'){
        putchar(str[i]);
        i++;
    }
}

int main(){
    /*
    printf("Enter the string : \n");
    scanf("%s",str);
    printf(" this the string you entered : %s\n",str);
    */
    readingString();
    printString();
}