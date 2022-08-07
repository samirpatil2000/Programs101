#include<stdio.h>


int main(){
    char str[]="geeksforgeeks",input_str[]="ge?ks*";
    int i=0,flag=0;

    while(str[i] != '\0'){
        if(str[i] != input_str[i]){
            if(input_str[i] == '*'){
                if(str[i] == str[i-1]){
                    flag=1;
                }else if(input_str[i+1] =='\0'){
                    flag=1;
                    break;
                    // printf("i == %d input_str[%d]=%c\n",i,i+1,input_str[i+1]);
                }else{
                    flag=0;
                    break;
                }
            }else if(input_str[i] =='?'){
                flag=1;
                // printf("i == %d input_str[%d]=%c\n",i,i,input_str[i]);
            }else{
                flag=0;
                break;
            }
        }
        i++;
    }
    printf("%d\n",flag);
}