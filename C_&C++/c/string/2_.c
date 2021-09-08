#include <stdio.h>
// to find the length of string 
int main(){
    char str[]="AEIOU";
    int i=0,length;
    // printf("\n Enter the string : \n");
    // // gets(str);
    // scanf("%s",str);
    while(str[i] != '\0'){
        printf("%c",str[i]);
        i++;
    }
    // length=i;
    // printf("The length of the string is : %d\n",length);
    return 0;

}