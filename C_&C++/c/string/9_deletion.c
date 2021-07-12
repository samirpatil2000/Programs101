#include<stdio.h>

int main(){
    char text[200],delete_str[50],new_str[200];
    int i=0,copyloop=0,n=0;


    printf("\nEnter text : \n");
    gets(text);
    printf("\nEnter string to delete : ");
    gets(delete_str);


    while(text[i] != '\0'){

        int k=i,j=0;
        while(text[k]==delete_str[j] && delete_str[j] != '\0'){
            k++;
            j++;
        }
        if (delete_str[j] =='\0'){
            copyloop=k;
        }
        new_str[n]=text[copyloop];
        i++;
        copyloop++;
        n++;
    }
    
    printf("\nNew String is : \n");
    puts(new_str);
    printf("\n");
}