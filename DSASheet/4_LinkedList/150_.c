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


struct node  *createLinkedList(struct node *lastNode,int num){
    struct node *new_node ,*ptr=lastNode;
    if(lastNode == NULL){
        new_node=malloc(sizeof(struct node));
        new_node->data=num;
        new_node->link=NULL;
        lastNode=new_node;
    }else{
        new_node=malloc(sizeof(struct node));
        new_node->data=num;
        lastNode->link=new_node;
        new_node->link=NULL;
        lastNode=new_node;
    }
    return lastNode;
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

struct node *insertAtEnd(struct node *start){
    struct node *newNode,*ptr=start;
    newNode=malloc(sizeof(struct node));
    newNode->link=NULL;
    ptr->link=newNode;
    return newNode;
}


struct node *intersection(struct node *head1,struct node *head2){
    struct node *head3,*ptr1,*ptr2;
    ptr1=head1;
    ptr2=head2;
    while(ptr1->link !=NULL && ptr2->link !=NULL){
        if(ptr1->data < ptr2->data ){
            ptr1=ptr1->link;
        }else if(ptr1->data > ptr2->data){
            ptr2=ptr2->link;
        }else{
            head3=createLinkedList(head3,ptr1->data);
            ptr2=ptr2->link;
            ptr1=ptr1->link;
        }
    }
    return head3;
}

int main(){
    struct node *head1=NULL,*head2=NULL,*head3=NULL;
    printf("The List one \n");
    head1=create_LinkedList(head1);
    head1=display(head1);
    printf("The List second \n");
    head2=create_LinkedList(head2);
    head2=display(head2);
    head3=intersection(head1,head2);
    printf("The answer \n");
    head3=display(head3);
}
