#include<stdio.h>

int main(){
    char text[100],string[100],newStr[100];
    int pos;

    printf("\nEnter text : \n");
    gets(text);
    printf("\nEnter string to insert : \n");
    gets(string);
    printf("\nEnter positon where to string insert : ");
    scanf("%d",&pos);

    int i=0,j=0,k=0;
    
    while(text[i] !='\0'){
        if(i==pos){
            while(string[k] != '\0'){
                newStr[j]=string[k];
                j++;k++;
            }
        }
        else{
            newStr[j]=text[i];
            j++;
        }
        i++;
        newStr[j]='\0';
    }
    printf("\n%s\n",newStr);
}