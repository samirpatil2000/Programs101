#include<stdio.h>
#include<string.h>
int main(){

    char text[200],search_str[50];
    



    printf("\nEnter text : \n");
    gets(text);
    printf("\nEnter string to search index  : \n");
    gets(search_str);

    int lenMax=strlen(text),lenMin=strlen(search_str);

    for(int i=0; i<=lenMax-lenMin; i++){

        int j;
        
        for(j=0;j<lenMin;j++){
            if(text[i+j] != search_str[j]){
                break;
            }
        }
        // printf("%d\n",j);
        if(j==lenMin){
            printf("search is at %d\n",i);
        }
    }
}