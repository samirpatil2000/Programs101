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

struct node *display(struct node *start,int length){
    struct node *ptr;
    ptr=start;
    int counter=0;
    while(ptr!= NULL && counter<length){
        printf(" %d -> ",ptr->data);
        counter++;
        ptr=ptr->link;
    }
    printf("\n");
    return start;
}

struct node *addCycle(struct node *start,int key){
    struct node *ptr,*lastNode=start;
    ptr=start;
    int counter;
    while(lastNode->link != NULL){
        lastNode=lastNode->link;
    }
    while(ptr->data != key && ptr!=NULL){
        ptr=ptr->link;
        counter++;
    }
    lastNode->link=ptr;
    return start;
}

void *detectCycle(struct node *ptr){
    struct node *slow_ptr=ptr,*fast_ptr=ptr;
    int couter=0;
    while(slow_ptr!=NULL){
        slow_ptr=slow_ptr->link;
        fast_ptr=fast_ptr->link->link;
        couter++;
        if(slow_ptr == fast_ptr){
            printf("We found the ptrs equal at %d\n",slow_ptr->data);
            break;
        }
        if(couter>40){
            printf("Loop Doesn't found \n");
            break;
        }
    }
}

struct node *removeCycle(struct node *start){
    struct node *slow_ptr=start,*fast_ptr=start;
    int couter=0;
    while(slow_ptr!=NULL){
        slow_ptr=slow_ptr->link;
        fast_ptr=fast_ptr->link->link;
        couter++;
        if(slow_ptr == fast_ptr){
            break;
        }
    }
    fast_ptr=start;
    while(fast_ptr->link != slow_ptr->link){
        fast_ptr=fast_ptr->link;
        slow_ptr=slow_ptr->link;
    }
    slow_ptr->link=NULL;
    return start;
}

int main(){
    struct node *head=NULL;
    head=create_LinkedList(head);
    // head=display(head,3);
    head=addCycle(head,3);
    head=display(head,12);
    detectCycle(head);
    head=removeCycle(head);
    head=display(head,12);

}