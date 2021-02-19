#include<stdio.h>
#include<stdlib.h>


struct node
{
    int data;
    struct node *link;
};

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

struct node *display(struct node *start){
    struct node *ptr;
    ptr=start;
    while(ptr->link != NULL){
        printf(" %d -> ",ptr->data);
        ptr=ptr->link;
    }
    printf(" %d \n",ptr->data);
    return start;
}

struct node *reverseLL(struct node *head){
    struct node *ptr=NULL,*new_node=NULL;
    new_node->link=NULL;
    while(head!=NULL){
        ptr=head->link;
        head->link=new_node;
        new_node=head;
        head=ptr;
    }
    head=new_node;
    return head;
}

struct node *usingRecursion(struct node *head){
    struct node *current;
    if(head==NULL){
        return;
    }
    if(head->link==NULL){
        return head;
    }
    current=usingRecursion(head->link);
    head->link->link==head;
    head->link=NULL;

    return current;


}

int main(){
    struct node *head=NULL;
    head=create_LinkedList(head);
    head=display(head);
    head=reverseLL(head);
    head=display(head);

}