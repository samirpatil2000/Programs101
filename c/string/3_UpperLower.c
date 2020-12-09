#include<stdio.h>

int main(){
    char name[100];
    char upperSting[100];
    printf("Enter the string \n: ");
    scanf("%s",name);
    int i=0;
    while(name[i] != '\0'){
        if(name[i] >='a' && name[i]<='z'){
            upperSting[i]=name[i]-32;
        }
        else
        {
            upperSting[i]=name[i];
        }
        i++;
        
    }

    // set last char as null
    upperSting[i]='\0';
    printf("\n The string \n");
        puts(upperSting);


}