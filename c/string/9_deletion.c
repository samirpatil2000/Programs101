#include<stdio.h>

int main(){
    char text[200],delete_str[50],new_str[200];
    int i=0,j=0,k=0;


    printf("\nEnter text : \n");
    gets(text);
    printf("\nEnter string to delete : \n");
    gets(delete_str);


    while(text[i] != '\0'){

        while(text[i]==delete_str[j] && delete_str[j] != '\0'){
            i++;
            j++;
        }
        if (delete_str[j] =='\0'){
            new_str[k]=text[i];
            k++;
            i++;
        }
    }
    
    printf("\n New String is : \n");
    puts(new_str);
    printf("\n");
}