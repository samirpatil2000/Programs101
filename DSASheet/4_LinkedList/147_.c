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

struct node *insertAtEnd(struct node *start,int data){
    struct node *newNode,*ptr=start;
    newNode=malloc(sizeof(struct node));
    newNode->link=NULL;
    newNode->data=data;
    ptr->link=newNode;
    return start;

}

struct node *addTwoLL(struct node *head1,struct node *head2){
    struct node *head3;


}

int main(){
    struct node *head1=NULL,*head2=NULL,*ptr1,*ptr2,*ptr3;
    head1=create_LinkedList(head1);
    head1=display(head1);
    printf("Enter the element for second linked list : \n");
    head2=create_LinkedList(head2);
    head2=display(head2);
    ptr1=head1;
    ptr2=head2;
    
    ptr3=malloc(sizeof(struct node));
    ptr3->link=NULL;

    while(ptr1->link!=NULL && ptr2->link!=NULL){
        if(ptr1->data+ptr2->data<=9){
            ptr3->data=ptr1->data+ptr2->data;
            ptr1=ptr1->link;
            ptr2=ptr2->link;
            ptr3=ptr3->link;
        }else{
            ptr3->data=0;
            ptr1=ptr1->link;
            ptr1->data+=1;
            ptr2=ptr2->link;
            ptr3=ptr3->link;
        }
    }
}
