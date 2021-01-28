#include<stdio.h>
#include<string.h>
#include<ctype.h>

#define MAX 100

int st[MAX],top=-1;


void push(int st[],int val){
    if(top== MAX-1){
        printf("\n Stack OverFlow");
    }else{
        top++;
        st[top]=val;
    }
}

int pop(int st[]){
    int val;
    if(top==-1){
        printf("\n Stack is Empty");
        return -1;
    }
    else{
        val=st[top];
        top--;
        return val;
    }
}

int getPriority(char ch){
    if(ch=='%' || ch=='*' || ch=='/'){
        return 1;
    }else if(ch=='+' || ch=='-'){
        return 0;
    }
}
// &&(getPriority(st[top])>getPriority(src[i]))

void infixToPostfix(char src[],char tar[]){
    int i=0,j=0;
    char temp;

    while(src[i] != '\0'){

        if(src[i]=='('){
            push(st,src[i]);
            i++;
        }
        else if(src[i]==')'){
            while((top!=-1)&&(st[top]!='(')){
                tar[j]=pop(st);
                j++;
            }
            if(top==-1){
                printf("\nInvalid Expression");
                exit(1);
            }
            temp=pop(st);
            i++;
        }
        else if(isdigit(src[i])|| isalpha(src[i])){
            tar[j]=src[i];
            j++;i++;
        }
        else if(src[i]=='+'|| src[i]=='-'|| src[i]=='*' ||src[i]=='/'||src[i]=='%'){
            while( (top!=-1)&&(st[top]!='(')
                    &&(getPriority(st[top])>getPriority(src[i]))){
                        tar[j]=pop(st);
                        j++;
            }
            push(st,src[i]);
            i++;
        }else{
            printf("\nINVALID ELEMENT");
            exit(1);
        }
    }
    while((top!=-1)&&(st[top]!='(')){
        tar[j]=pop(st);
        j++;
    }
    tar[j]='\0';
}



int main(){
    char infix[100],postfix[100];
    printf("\nEnter the expression : ");
    scanf("%s",infix);
    infixToPostfix(infix,postfix);
    printf("\ninfix to postfix : %s to %s\n",infix,postfix);

}