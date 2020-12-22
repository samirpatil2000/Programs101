#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *link;
};

struct node *start = NULL;
struct node *create_ll(struct node*);
struct node *display(struct node*);
struct node *insert_beg(struct node*);
struct node *insert_end(struct node*);
struct node *insert_before(struct node*);
struct node *insert_after(struct node*);
struct node *delete_beg(struct node*);
struct node *delete_end(struct node*);
struct node *delete_before(struct node*);
struct node *delete_after(struct node*);
struct node *delete_list(struct node*);
struct node *sort_list(struct node*);


void printingData(struct node *head){
    struct node *ptr;
    ptr=head;

    while (ptr != NULL)
    {
        printf("num : %d",ptr->data);
        ptr=ptr->link;
        printf("\n");
    }
    
}

int main(){
    start = create_ll(start);
    printingData(start);

    /*
    int option;
    do{
        printf("\n 1: Create LL");
        printf("\n 2: Insert at beg LL");
        printf("\n 3: Insert at end LL");
        printf("\n 4: Insert before the element of LL");
        printf("\n 5: Insert after the element of  LL");
        printf("\n 6: Delete begining node of  LL");
        printf("\n 7: Delete end node of  LL");
        printf("\n 8: Delete node after the element of  LL");
        printf("\n 9: Delete node before the element of  LL");
        printf("\n 10: Delete LL");
        printf("\n 11: Sort the LL");
        printf("\n 12: Exit ");
        
        switch (option)
        {
        case 1:
            start=create_ll(start);
            printf("\n LL is created ");
            break;
        case 2:
            start=display(start);
            break;
        case 3:
            start=insert_beg(start);
            break;
        case 4:
            start=insert_end(start);
            break;
        case 5:
            start=insert_before(start);
            break;
        case 6:
            start=insert_after(start);
            break;
        case 7:
            start=delete_beg(start);
            break;
        case 8:
            start=delete_end(start);
            break;
        case 9:
            start=delete_before(start);
            break;
        case 10:
            start=delete_after(start);
            break;
        case 11:
            start=delete_list(start);
            break;
        case 12:
            start=sort_list(start);
            printf("\n LL is created ");
            break;
        
        default:
            break;
        }
    }while (option != 13);
    
    */
}

struct node *create_ll(struct node *start)
{
    struct node *new_node,*ptr;
    int num;
    printf("\nEnter -1 to end");
    printf("\nEnter data : ");
    scanf("%d",&num);

    while (num !=-1 )
    {
        new_node=malloc(sizeof(struct node));
        new_node->data=num;    
    }
    if(start==NULL){
        new_node->link =NULL;
        start = new_node;
    }
    else
    {
        ptr=start;
        while (ptr->link != NULL)
        {
            ptr=ptr->link;
            ptr->link=new_node;
            new_node->link=NULL;
        }

    printf("\nEnter data : ");
    scanf("%d",&num);
        
        
    }
    return start;
    
    
}
