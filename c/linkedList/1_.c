#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *link;
};


void printingData(struct node *head){
    if(head==NULL){
        printf("Link List is empty");
    }
    struct node *ptr=NULL;
    ptr=head;
    while (ptr !=NULL)
    {
        printf("\t%d",ptr->data);
        ptr=ptr->link;
    }
    printf("\n");
}

void addAtEnd(struct node *head,int data){
    if(head==NULL){
        printf("Link List is empty");
    }
    struct node *ptr,*temp;
    ptr=head;
    temp=malloc(sizeof(struct node));
    temp->data=data;

    while (ptr->link !=NULL){
        ptr=ptr->link;
    }
    ptr->link=temp;
    
    
}

int main(){
    struct node *head=malloc(sizeof(struct node));
    head->data=45;
    head->link=NULL;

    struct node *current=malloc(sizeof(struct node));
    current->data=78;
    current->link=NULL;

    head->link=current;

    current=malloc(sizeof(struct node));
    current->data=89;
    current->link=NULL;

    head->link->link=current;


    printingData(head);

    addAtEnd(head,123);
    addAtEnd(head,123);
    addAtEnd(head,123);
    addAtEnd(head,123);
    addAtEnd(head,123);
    addAtEnd(head,123);
    printingData(head);

}




