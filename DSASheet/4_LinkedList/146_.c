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

struct node *reverse_ll(struct node *start){
    struct node *new_start,*ptr;
    new_start=NULL;
    while(start!=NULL){
        ptr=start->link;
        start->link=new_start;
        new_start=start;
        start=ptr;
    }
    start=new_start;
    return start;
}

struct node *newNodeAtEnd(struct node *lastNode){
    struct node *ptr;
    ptr=malloc(sizeof(struct node));
    ptr->link=NULL;
    lastNode->link=ptr;
    lastNode=ptr;
    return lastNode;
    
}

struct node *addOne(struct node *head){
    struct node *ptr=head;
    while(ptr->data==9){
        if(ptr->link==NULL && ptr->data==9){
            struct node *newNode=malloc(sizeof(struct node));
            newNode->data=1;
            ptr->data=0;
            ptr->link=newNode;
            // ptr=newNode;
            return head;
        }
        ptr->data=0;
        if(ptr->link->data <= 8){
            break;
        }
        ptr=ptr->link;
    }
    ptr->link->data=ptr->link->data+1;
    // if(ptr->link!=NULL){
    //     if(ptr->link!=NULL && ptr->data==0){
    //         struct node *newNode=malloc(sizeof(struct node));
    //         newNode->data=1;
    //         ptr->link=newNode;
    //         ptr=newNode;
    //         return head;
    //     }
    // }
    return head;
}

int main(){
    struct node *head=NULL;
    head=create_LinkedList(head);
    head=display(head);
    head=reverse_ll(head);
    head=display(head);
    head=addOne(head);
    head=display(head);
    head=reverse_ll(head);
    printf("Solution: \n");
    head=display(head);
}
