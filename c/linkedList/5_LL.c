#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *link;
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
            new_node->data=num;
            new_node->link=NULL;
            start=new_node;
        }
        else
        {
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            ptr=start;
            while (ptr->link != NULL)
            {
                ptr=ptr->link;
            }
            ptr->link=new_node;
            new_node->link=NULL;
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
            new_node->data=num;
            new_node->link=NULL;
            start=new_node;
        }
        else
        {
            new_node=(struct node*)malloc(sizeof(struct node));
            new_node->data=num;
            ptr=start;
            while (ptr->link != NULL)
            {
                ptr=ptr->link;
            }
            ptr->link=new_node;
            new_node->link=NULL;
        }
        printf("\nEnter the data :");
        scanf("%d",&num);
    }
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

struct node *insert_beg(struct node *start){
    struct node *new_node;
    int num;
    printf("\nEnter the data : ");
    scanf("%d",&num);
    new_node=malloc(sizeof(struct node));
    new_node->data=num;
    new_node->link=start;
    start=new_node;

    return start;
}

struct node *insert_end(struct node *start){
    struct node *new_node ,*ptr;
    new_node=malloc(sizeof(struct node));
    int num;
    printf("\nEnter the data : ");
    scanf("%d",&num);
    ptr=start;
    while(ptr ->link != NULL){
        ptr=ptr->link;
    }
    ptr->link=new_node;
    new_node->data=num;
    new_node->link=NULL;

    return start;
}

struct node *insert_before(struct node *start){
    struct node *new_node ,*ptr,*preptr;
    new_node=malloc(sizeof(struct node));
    int number,num;
    printf("\nEnter the number whom before you wants to insert : ");
    scanf("%d",&number);
    printf("\nEnter the data : ");
    scanf("%d",&num);
    new_node->data=num;
    ptr=start;
    preptr=ptr;

    while(ptr -> data != number){
        preptr=ptr;
        ptr=ptr->link;
    }
    new_node->link=ptr;
    preptr->link=new_node;

    return start;

}

struct node *insert_after(struct node *start){
    struct node *new_node,*ptr,*preptr;
    new_node=malloc(sizeof(struct node));
    int number,num;
    printf("\nEnter the number whom after you wants to insert : ");
    scanf("%d",&number);
    printf("\nEnter the data : ");
    scanf("%d",&num);

    ptr=start;
    preptr=ptr;
    new_node->data=num;
    while(preptr ->data != number){
        preptr=ptr;
        ptr=ptr->link;
    }
    
    preptr->link=new_node;
    new_node->link=ptr;

    return start;
}

struct node *delete_beg(struct node *start){
    struct node *ptr;
    ptr=start;
    start=ptr->link;
    free(ptr);
    return start;
}

struct node *delete_end(struct node *start){
    struct node *ptr,*preptr;
    ptr=start;
    preptr=ptr;
    while(ptr->link != NULL){
        preptr=ptr;
        ptr=ptr->link;
    }
    preptr->link=NULL;
    free(ptr);
    return start;
}

struct node *delete_node(struct node *start){
    struct node *ptr,*preptr;
    ptr=start;
    preptr=ptr;
    int number;
    printf("\nEnter the number that node to be delete : ");
    scanf("%d",&number);
    if( ptr->data == number){
        start=delete_beg(start);
        return start;
    }
    else
    {
        while(ptr->data !=number){
            preptr=ptr;
            ptr=ptr->link;
        }
        preptr->link=ptr->link;
        free(ptr);
        return start;
    }
}

struct node *delete_after(struct node *start){
    struct node *ptr,*preptr;
    ptr=start;
    preptr=ptr;
    int number;
    printf("\nEnter the number that node to be delete : ");
    scanf("%d",&number);

    while(preptr->data != number){
        preptr=ptr;
        ptr=ptr->link;
    }
    preptr->link=ptr->link;
    free(ptr);
    return start;
}

struct node *deleteList(struct node *start){
    struct node *ptr;
    if(start != NULL){
        ptr=start;
        while (ptr != NULL){
            printf("\n %d is deleted ",ptr->data);
            start=delete_beg(ptr);
            ptr=start;
        }
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
        printf("\n 11 : Exit ");

        printf("\n Enter your option : ");
        scanf("%d",&option);

        switch (option)
        {
        case 0: 
            start=create_ll(start);
            printf("\nLinked List Creation");
            break;
        case 1:
            start=display(start);
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
            start=deleteList(start);
            break;
        default:
            break;
        }
    } while (option != 11);
    
}