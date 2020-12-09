#include<stdio.h>
#include<string.h>


int main(){
    char str[100],output[100];
    printf("\nEnter string : ");
    gets(str);
    printf("\n");
    puts(str);

    int n,m;
    printf("\nEnter number from starting to end : ");
    scanf("%d",&n);
    scanf("%d",&m);



    int len=strlen(str);
    int i=n,j=m,o=0;
    while (i<j){
        output[o]=str[i];
        i++;
        o++;
    }
    output[o]='\0';
    puts(output);

}