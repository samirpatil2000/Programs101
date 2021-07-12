#include<stdio.h>

int main(){
    char str[100];
    int i=0,word_count=1,line_count=1,char_count=1;
    printf("Enter the character : \n");

    scanf("%c",&str[i]);
    while(str[i] != '*'){
        i++;
        scanf("%c",&str[i]);
    }
    str[i]='\0';
    int j=0;
    puts(str);
    while (str[j]!='\0')
    {
        if(str[j]=='\n'|| str[j]==79){
            line_count++;
        }
        if(str[j]==' ' && str[j+1] !=' '){
            word_count++;
        }
        char_count++;
        j++;
    }
    printf("line_count : %d\n",line_count);
    printf("word_count : %d\n",word_count);
    printf("char_count : %d\n",char_count);

    




}