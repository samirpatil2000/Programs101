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

    int i=1,counter=1;
    while (text[i] !='\0')
    {
        if(text[i]>='A' && text[i]<='Z'){
            counter++;
        }
        i++;
        
    }
    
    printf("%d\n",counter);
    

}