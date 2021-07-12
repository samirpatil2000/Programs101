#include<stdio.h>
#include<stdlib.h>


struct node{
    int data;
    struct node *prev;
    struct node *next;
};

struct node *create_ll(struct node *start){
    struct node *new_node,*ptr;
    
    int num;
    printf("\nEnter -1 to end : ");
    printf("\nEnter the data : ");
    scanf("%d",&num);
    while (num !=-1)
    {
        if(start == NULL){
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            new_node->prev=NULL;
            new_node->next=NULL;
            start=new_node;
        }else{
            ptr=start;
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            while(ptr->next!=NULL){
                ptr=ptr->next;
            }
            new_node->prev=ptr;
            ptr->next=new_node;
            new_node->next=NULL;
        }
        printf("\nEnter the data : ");
        scanf("%d",&num);
    }
    return start;
    
}

void display(struct node *start){
    struct node *ptr;
    ptr=start;
    while(ptr !=NULL){
        printf(" %d <=> ",ptr->data);
        ptr=ptr->next;
    }
}

struct node *insert_beg(struct node *start){
    struct node *new_node;
    int num;
    printf("\nEnter the data to insert AT beginning : ");
    scanf("%d",&num);
    new_node=malloc(sizeof(struct node));
    new_node->data=num;
    new_node->prev=NULL;
    new_node->next=start;
    start->prev=new_node;
    start=new_node;

    return start;
}

struct node *insert_end(struct node *start){
    struct node *new_node,*ptr;
    ptr=start;
    int num;
    printf("\nEnter the data to insert AT end : ");
    scanf("%d",&num);
    new_node=malloc(sizeof(struct node));
    new_node->data=num;

    while(ptr->next!=NULL){
        ptr=ptr->next;
    }
    new_node->prev=ptr;
    ptr->next=new_node;
    new_node->next=NULL;

    return start;
}

struct node *insert_before(struct node *start){
    struct node *new_node,*ptr,*preptr;
    
    int num,number;
    printf("\nEnter the number whom before insert new data : ");
    scanf("%d",&number);
    printf("\nEnter the data to insert AT end : ");
    scanf("%d",&num);
    new_node=malloc(sizeof(struct node));
    new_node->data=num;

    ptr=start;
    preptr=ptr;
    while(ptr->data!=number){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=new_node;
    new_node->prev=preptr;
    ptr->prev=new_node;
    new_node->next=ptr;

    return start;
}



struct node *insert_after(struct node *start){
    struct node *new_node,*ptr,*preptr;
    
    int num,number;
    printf("\nEnter the number whom after insert new data : ");
    scanf("%d",&number);
    printf("\nEnter the data to insert AT end : ");
    scanf("%d",&num);
    new_node=malloc(sizeof(struct node));
    new_node->data=num;

    ptr=start;
    preptr=ptr;
    while(preptr->data!=number){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=new_node;
    new_node->prev=preptr;
    ptr->prev=new_node;
    new_node->next=ptr;

    return start;
}



struct node *delete_beg(struct node *start){
    struct node *ptr;
    ptr=start;
    ptr=ptr->next;
    ptr->prev=NULL;
    start=ptr;
    free(ptr);

    return start;
}
struct node *delete_end(struct node *start){
    struct node *ptr;
    ptr=start;
    while(ptr-> next!= NULL){
        ptr=ptr->next;
    }
    ptr->prev->next=NULL;

    return start;
}


struct node *delete_node(struct node *start){
    struct node *ptr,*preptr;
    int num;
    printf("\nEnter the number to delete that node : ");
    scanf("%d",&num);
    ptr=start;preptr=ptr;
    while(ptr-> data!= num){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=ptr->next;
    ptr->next->prev=preptr;
    free(ptr);

    return start;
}

struct node *delete_after(struct node *start){
    struct node *ptr,*preptr;
    int num;
    printf("\nEnter the number whom after node to be delete : ");
    scanf("%d",&num);

    ptr=start;preptr=ptr;
    while(preptr->data!=num){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=ptr->next;
    ptr->next->prev=preptr;
    free(ptr);

    return start;
}

struct node *delete_entire_ll(struct node *start){

    while(start !=NULL){
            start=delete_beg(start);
    }
    return start;
}
int main(){
    struct node *start =NULL;
    int option;

    do
    {
        printf("\n\n ** Main Menu **");
        printf("\n 0 : Create Circular Doubly Linked List");
        printf("\n 1 : Display Circular Doubly Linked List");
        printf("\n 2 : Add node at beg");
        printf("\n 3 : Add node at end");
        printf("\n 4 : Add node before given node ");
        printf("\n 5 : Add node after given node ");
        printf("\n 6 : Delete node from beg");
        printf("\n 7 : Delete node from end ");
        printf("\n 8 : Delete given node ");
        printf("\n 9 : Delete node from after the given node ");
        printf("\n 10 : Delete entire Linked List ");
        printf("\n 11 : Sort the linked list ");
        printf("\n 12 : Exit ");

        printf("\n Enter your option : ");
        scanf("%d",&option);

        switch (option)
        {
            case 0: 
                start=create_ll(start);
                printf("\nLinked List Creation");
                break;
            case 1:
                display(start);
                break;
            case 2:
                start=insert_beg(start);
                break;
            case 3:
                start=insert_end(start);
                break;
            case 4:
                start=insert_before(start);
                break;
            case 5:
                start=insert_after(start);
                break;
            case 6:
                start=delete_beg(start);
                break;
            case 7:
                start=delete_end(start);
                break;
            case 8:
                start=delete_node(start);
                break;
            case 9:
                start=delete_after(start);
                break;
            case 10:
                start=delete_entire_ll(start);
                break;
            // case 11:
            //     start=sortLinkedList(start);
            //     break;
            default:
                break;
        }
    } while (option != 12);
}