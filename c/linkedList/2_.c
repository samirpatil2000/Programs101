#include<stdio.h>
#include<stdlib.h>

struct node
{
    int age;
    int num;
    // char name[20];
    struct node *link;
};

void printingData(struct node *head){
    struct node *ptr;
    ptr=head;

    while (ptr != NULL)
    {
        printf("age : %d , num : %d",ptr->age,ptr->num);
        ptr=ptr->link;
        printf("\n");
    }
    
}

struct node* addDataAtStart(struct node *head,int age,int num){
    struct node *ptr=malloc(sizeof(struct node));
    ptr->age=age;
    ptr->num=num;
    ptr->link=head;
    head=ptr;
    return head;
    
}


void addDataAtEnd(struct node *head,int age,int num){
    struct node *ptr,*temp;

    ptr=head;
    // temp=ptr->link;
    temp=malloc(sizeof(struct node));
    temp->age=age;
    temp->num=num;
    temp->link=NULL;

    while (ptr->link != NULL){
        ptr=ptr->link;
    }
    ptr->link=temp;
    
}


struct node *addNode(struct node ){
    struct node *current=malloc(sizeof(struct node));
    current->age=20;
    current->num=25;
    current->link=NULL;
}



int main(){

    struct node *head=malloc(sizeof(struct node));
    head->age=21;
    head->num=30;
    head->link=NULL;

    struct node *current=malloc(sizeof(struct node));
    current->age=20;
    current->num=25;
    current->link=NULL;

    head->link=current;

    current=malloc(sizeof(struct node));
    current->age=19;
    current->num=10;
    current->link=NULL;

    head->link->link=current;

    printingData(head);

    int m,n,p,q;
    printf("Enter the age and number : ");
    scanf("%d %d",&m,&n);
    addDataAtEnd(head,m,n);
    printingData(head);

    printf("Enter the age and number : ");
    scanf("%d %d",&p,&q);

    head=addDataAtStart(head,p,q);
    printingData(head);

}