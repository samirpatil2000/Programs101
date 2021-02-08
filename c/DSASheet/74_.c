#include<stdio.h>
#include<string.h>

int main(){
    char str[]="asadssadla";
    int len=strlen(str);
    int j=len/2,i=0;

    printf("mid %d and str[%d] %c \n",j,j,str[j]);

    while(i<len/2 && j<len){
        printf("%c %d -- %c %d\n",str[i],i,str[j],j);
        if(str[i] == str[j]){
            j++;i++;
        }else{
            j++;
        }
        if(str[i] != str[j] && i!=0 && i!=len/2 && i!=1 && j!=len){
            i=0;
        }
    }
    printf("the length of prefix is from 0 to %d\n",i-1);
    for(int k=0;k<i;k++){
        printf("%c",str[k]);
    }
    printf("\n");

}