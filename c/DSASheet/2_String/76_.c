#include<stdio.h>
#define MAX 20


char st[MAX];
int top=-1;


char pop(){
    if(top==-1){
        printf("UNDERFLOW");
        return 0;
    }else{
        char ch;
        ch=st[top];
        top--;
        return ch;
    }
}

void push(char ch){
    if(top==MAX-1){
        printf("OVERFLOW");
        return;
    }else{
        top++;
        st[top]=ch;
    }
}

int main(){
    char exp[]="}{{}}{{{";
    int i,ans=0;

    while(exp[i] != '\0'){
        if(exp[i]=='{'){
            push(exp[i]);
        }else if(exp[i]=='}' && st[top]=='{'){
            pop();
        }else{
            push(exp[i]);
        }
        i++;
    }
    while(top!=-1){
        if(st[top]=='{'){
            ans++;
        }
        top--;
    }
    printf("The ans %d\n",ans);
}