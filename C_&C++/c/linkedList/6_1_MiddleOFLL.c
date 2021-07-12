#include<stdio.h>

struct node
{
    int data;
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
            new_node->next=NULL;
            start=new_node;
        }else{
            ptr=start;
            new_node=malloc(sizeof(struct node));
            new_node->data=num;
            while(ptr->next!=NULL){
                ptr=ptr->next;
            }
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
        printf(" %d -> ",ptr->data);
        ptr=ptr->next;
    }
}


void *middle_element(struct node *start){
    struct node *sptr,*fptr;
    if(start != NULL){
        sptr=start;
        fptr=start;
        while(fptr !=NULL && fptr->next !=NULL){
            sptr=sptr->next;
            fptr=fptr->next->next;
        }
        printf("\nThe Middle element is %d",sptr->data);
    }
    
}
struct node *reverse_ll(struct node *start){
    struct node *new_start,*ptr;
    new_start=NULL;
    while(start!=NULL){
        ptr=start->next;
        start->next=new_start;
        new_start=start;
        start=ptr;
    }
    start=new_start;
    return start;
}
int main(){
    struct node *start =NULL;
    int option;

    do
    {
        printf("\n\n ** Main Menu **");
        printf("\n 0 : Create Linked List");
        printf("\n 1 : Display Linked List");
        printf("\n 2 : Find Middle Element");
        printf("\n 3 : Reverse The linked List");
        printf("\n 4 : Exit");
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
                middle_element(start);
                break;
            case 3:
                start=reverse_ll(start);
                break;
            default:
                break;
        }
    } while (option != 4);
}