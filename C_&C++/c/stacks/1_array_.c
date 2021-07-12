#include<stdio.h>
#define MAX 3

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
int peek(int st[]){
    int val;
    if(top==-1){
        printf("\n Stack is Empty");
        return -1;
    }
    else{
        val=st[top];
        return val;
    }
}

void display(int st[]){
    int i;
    if(top==-1){
        printf("\n Stack is Empty");
    }else{
        for(int i=top;i>=0;i--){
            printf("\n %d",st[i]);
            printf("\n");
        }
    }
}

int main(){
    int val,option;

    do{
        printf("\n Main Menu");
        printf("\n 1.PUSH");
        printf("\n 2.POP");
        printf("\n 3.PEEK");
        printf("\n 4.DISPLAY");
        printf("\n 5.EXIT");

        printf("\n Enter the option");
        scanf("%d",&option);

        switch (option)
        {
        case 1:
            printf("\n Enter the value to enter in the stack ");
            scanf("%d",&val);
            push(st,val);
            break;
        case 2:
            printf("\n %d element is popped out",pop(st));
            break;
        case 3:
            printf("\n %d element is peeked",peek(st));
            break;
        case 4:
            printf("\n STACK");
            display(st);
            break;
        default:
            break;
        }


    }while(option != 5);
}