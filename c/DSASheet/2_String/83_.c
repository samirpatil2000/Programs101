#include<stdio.h>
#include<string.h>

int main(){
    char num[]="0111";
    int len=strlen(num),i=0,ctr1=0,ctr2=0,current_num;
    while(num[i]!='\0'){
        // printf("current number%d\n",current_num);
        if(i%2==0 && num[i]=='1'){
            ctr1++;
        } 
        if(i%2!=0 && num[i]=='0'){
            ctr1++;
        } 
        if(i%2==0 && num[i]=='0'){
            ctr2++;
        } 
        if(i%2!=0 && num[i]=='1'){
            ctr2++;
        }
        i++;
    }
    int min=ctr1;
    if(ctr2<ctr1){
        min=ctr2;
    }
    printf("the flap %d %d\n",ctr1,ctr2);
    
}