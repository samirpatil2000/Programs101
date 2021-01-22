#include<stdio.h>
#include<stdlib.h>

struct node
{
    struct node *next;
    int data;
    struct node *prev;
};


// struct node *create_ll(struct node *start);

struct node *create_ll(struct node *start){
    printf("\nCreate Linked List");
    struct node *new_node ,*ptr;
    int num;
    printf("\nEnter -1 to end : ");
    printf("\nEnter the data : ");
    scanf("%d",&num);
    while (num != -1)
    {
        if(start==NULL){
            new_node=malloc(sizeof(struct node));
            new_node->prev=NULL;
            new_node->data=num;
            new_node->next=start;
            start=new_node;
        }
        else
        {
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            ptr=start;
            while (ptr->next != start)
            {
                ptr=ptr->next;
            }
            new_node->prev=ptr;
            ptr->next=new_node;
            
            new_node->next=start;
            start->prev=new_node;
        }
        printf("\nEnter the data :");
        scanf("%d",&num);
    }
    return start;
    
}


void create_linkedList(struct node *start){
    struct node *new_node ,*ptr;
    int num;
    printf("\nEnter -1 to end : ");
    printf("\nEnter the data : ");
    scanf("%d",&num);
    while (num != -1)
    {
        if(start==NULL){
            new_node=(struct node*)malloc(sizeof(struct node));
            new_node->prev=NULL;
            new_node->data=num;
            new_node->next=start;
            start=new_node;
        }
        else
        {
            new_node=(struct node*)malloc(sizeof(struct node));
            new_node->data=num;
            ptr=start;
            while (ptr->next != start)
            {
                ptr=ptr->next;
            }
            new_node->prev=ptr;
            ptr->next=new_node;
            
            new_node->next=start;
            start->prev=new_node;
        }
        printf("\nEnter the data :");
        scanf("%d",&num);
    }
}

struct node *display(struct node *start){
    struct node *ptr;
    ptr=start;
    while(ptr->next != start){
        printf("\t -> %d",ptr->data);
        ptr=ptr->next;
    }
    printf("\t -> %d",ptr->data);
    return start;
}


int main(){
    struct node *start =NULL;
    int option;

    do
    {
        printf("\n\n ** Main MEnu **");
        printf("\n 0 : Create Circular Doubly Linked List");
        printf("\n 1 : Display Circular Doubly Linked List");
        printf("\n 2 : Add node at beg");
        printf("\n 3 : Add node at end");
        printf("\n 4 : Add node before given node ");
        printf("\n 5 : Add node after given node ");
        printf("\n 6 : Delete node from beg");
        printf("\n 7 : Delete node from end ");
        printf("\n 8 : Delete node from before the given node ");
        printf("\n 9 : Delete node from after the given node ");
        printf("\n 10 : Delete entire Linked List ");
        printf("\n 11 : Exit ");

        printf("\n Enter your option : ");
        scanf("%d",&option);

        switch (option)
        {
        case 0: 
            start=create_ll(start);
            printf("\n Doubly Linked List Creation");
            break;
        case 1:
            start=display(start);
            break;
        /*   
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
            start=delete_before(start);
            break;
        case 9:
            start=delete_after(start);
            break;
        case 10:
            start=delete_list(start);
            break;
            */
        default:
            break;
        }
    } while (option != 11);
    
}