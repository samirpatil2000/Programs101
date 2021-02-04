#include<stdio.h>
#include<string.h>
#define MAX 100

char st[MAX];
int top=-1;

void push(char st[],char ch){
    if(top==MAX-1){
        printf("\nOVERFLOW");
    }else{
        st[top]=ch;
        top++;
    }
}

char pop(char st[]){
    char ch;
    if(top==-1){
        printf("\nStack is UnderFlow");
    }else{
        ch=st[top];
        top--;
        return ch;
    }
}

int main(){
    char exp[MAX],temp;
    printf("\nENTER THE EXPRESSION : ");
    scanf("%s",exp);
    int i=0,flag=1;

    while(i<strlen(exp)){
        if(exp[i]=='{' || exp[i]=='['|| exp[i]=='('){
            push(st,exp[i]);
        }
        if(exp[i]==')' || exp[i] =='}' || exp[i]==']'){  

            if(top==-1){
                flag=0;
            }
            else
            {
                temp=pop(st);
                if(exp[i]=='}' &&(temp=='(' || temp=='[')){
                    flag=0;
                }
                if(exp[i]==']' &&(temp=='{' || temp=='(')){
                    flag=0;
                }
                if(exp[i]==')' &&(temp=='{' || temp=='[')){
                    flag=0;
                }
            }
        }
        i++;  
    }
    if(top>=0){
            flag=0;
        }
        
    if(flag==1){
        printf("VALID EXPRESSION\n");
    }else{
        printf("INVALID EXPRESSION\n");
    }

}