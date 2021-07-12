#include<stdio.h>
#include<stdlib.h>

struct node
{
    int num;
    struct node *link;
};


// insert new node after the after given value

void insertionAtGivenValue(struct node *head,int number,int data){

    struct node *ptr,*temp;

    temp=malloc(sizeof(struct node));
    temp->num=data;
    temp->link=NULL;

    ptr=head;

    while (ptr->num != number)
    {
        ptr=ptr->link;
    }
     
    
}

void printingLinkedList(struct node *head){
    struct node *ptr;
    ptr=head;
    if (ptr==NULL)
    {
        printf("List is empty\n");
    }
    else
    {
        while (ptr != NULL)
        {
            printf("%d\n",ptr->num);
            ptr=ptr->link;
        }
    }
    
    
}

int main(){
    struct node *head=malloc(sizeof(struct node));
    head->num=29;
    head->link=NULL;

    struct node *current=malloc(sizeof(struct node));
    current->num=89;
    current->link=NULL;

    head->link=current;

    current = malloc(sizeof(struct node));
    current->num=54;
    current->link=NULL;

    head->link->link=current;

    printingLinkedList(head);


}