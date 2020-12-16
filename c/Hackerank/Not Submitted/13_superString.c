#include<stdio.h>

/*
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. 
In each operation, select a pair of adjacent letters that match, and delete them.
Delete as many characters as possible using this method and return the resulting string.
 If the final string is empty, return Empty String

 // https://www.hackerrank.com/challenges/reduced-string/problem
*/

int main(){
    char new_str[200],text[200];
    printf("Enter the text : ");
    gets(text);

    int i=0,j=0;
    while (text[i] !='\0')
    {
        while(text[i]==text[i+1]){
            i+=2;
        }
        new_str[j]=text[i];
        j++;i++;
    }
    new_str[j]='\0';
    printf("%s\n",new_str);
    

}