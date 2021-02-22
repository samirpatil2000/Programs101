#include<stdio.h>



void strFun(char A,char B,char,C){
    strFun(A,C,B);
    printf("%d%d%d",A,B,C);
    strFun(C,B,A);
}

int main(){
    strFun("A","B","C");
}