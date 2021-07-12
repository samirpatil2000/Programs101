#include<stdio.h>
#include<stdlib.h>


struct node
{
    int data;
    struct node *link;
};

void printLinkedList(struct node *head){
    struct node *ptr;
    ptr=head;
    while (ptr->link !=NULL)
    {   
        printf("\t %d",ptr->data);
        ptr=ptr->link;
    }
    printf("\n");
}


struct node  *create_LinkedList(struct node *head){
    struct node *new_node ,*ptr;
    int num;
    printf("\nEnter the data in linked list ");
    printf("\n -1 for end ");
    printf("\n Enter the element : ");
    scanf("%d",&num);

    while(num != -1){
        if(head == NULL){
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            new_node->link=NULL;
            head=new_node;
        }
        else
        {
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            ptr=head;
            while(ptr->link != NULL){
                ptr=ptr->link;
            }
            ptr->link=new_node;
            new_node->link=NULL;
        }
        printf("\n Enter the element : ");
        scanf("%d",&num);
    }
    return head;
}


int main(){
    struct node *head=NULL, *new_node ,*ptr;
    
    head=create_LinkedList(head);
    /*
    int num;

    printf("\nEnter the data in linked list ");
    printf("\n -1 for end ");
    printf("\n Enter the element : ");
    scanf("%d",&num);

    while (num != -1)
    {
        new_node=malloc(sizeof(struct node));
        new_node->data=num;
        if (head==NULL)
        {
            new_node->link=NULL;
            head=new_node;
        }else
        {
            ptr=head;
            while (ptr->link != NULL)
            {
                ptr=ptr->link;
            }
            ptr->link=new_node;
            new_node->link=NULL;
        }

        printf("\n Enter the element : ");
        scanf("%d",&num);
        
    }
    */
    printLinkedList(head);
    
}