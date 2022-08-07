#include<stdio.h>
#include<string.h>


void usingFunction(char str[]){
    
}

int main(){
    char str[]="aabb";
    int len=strlen(str);
    int i=0;
    while (str[i+1] != '\0'){
        if(str[i] != str[i+1]){
            printf("%c%c",str[i],str[i+1]);
            i+=2;
        }else{
            printf("%c",str[i]);
            i+=2;
        }
    }
    printf("\n");
}