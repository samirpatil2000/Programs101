#include<stdio.h>
#include<stdlib.h>

struct stack{
    int data;
    struct stack *link;
};

struct stack *top=NULL;


struct stack *push(struct stack *top,int val){
    struct stack *ptr;
    ptr=malloc(sizeof(struct stack));
    ptr->data=val;
    if(top==NULL)
    {
        ptr->link=NULL;
        top=ptr;
    }
    else
    {
        ptr->link=top;
        top=ptr;
    }
    return top;
}

struct stack *pop(struct stack *top){
    struct stack *ptr;
    ptr=top;
    if(top == NULL){
        printf("\n STACK IS EMPTY");
        return -1;
    }else{
        int val;
        val=ptr->data;
        ptr=ptr->link;
        return val;
    }
}

struct stack *peek(struct stack )

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

                break;
            case 2:
                // printf("\n %d element is popped out",pop(st));
                break;
            case 3:
                // printf("\n %d element is peeked",peek(st));
                break;
            case 4:
                printf("\n STACK");
                break;
            default:
                break;
        }
    }while(option != 5);
}