#include<stdio.h>
#include<ctype.h>
#define MAX 100



float st[MAX];
int top=-1;


void push(float st[],float num){
    if(top==MAX-1){
        printf("\nOVERFLOW CONDITION");
    }else{
        top++;
        st[top]=num;
    }
}

float pop(float st[]){
    float value;
    if(top==-1){
        printf("\nUNDERFLOW CONDITION");
    }else{
        value=st[top];
        top--;
        return value;
    }
}

float evaluteExpression(char exp[]){
    int i=0;
    float op1,op2,value;
    while(exp[i] !='\0'){
        if(isdigit(exp[i])){
            push(st,(float)(exp[i]));
        }else{
            op2=pop(st);
            op1=pop(st);
            switch (exp[i])
            {
                case '+':
                    value=op1+op2;
                    break;
                case '-':
                    value=op1-op2;
                    break;
                case '*':
                    value=op1*op2;
                    break;
                case '%':
                    value=(int)op1%(int)op2;
                    break;
                case '/':
                    value=op1/op2;
                    break;
                // case '^':
                //     value=op1**op2;
                //     break;
                default:
                    break;
            }
            push(st,value);
        }
        i++;
    }
    return pop(st);
}

int main(){
    char exp[MAX],temp;
    printf("\n Enter the expression");
    scanf("%s",exp);
    float val=evaluteExpression(exp);
    printf("\n Value of postfix expression = %.2f\n",val);


}