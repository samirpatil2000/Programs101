#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left;
    struct node *right;
};



struct node *insertion(struct node *tree,int val){
    struct node *ptr,*parentptr,*nodeptr;

    ptr=malloc(sizeof(struct node));
    ptr->data=val;
    ptr->left=NULL;
    ptr->right=NULL;
    if(tree == NULL){
        tree=ptr;
        tree->left=NULL;
        tree->right=NULL;
    }else{
        parentptr=NULL;
        nodeptr=tree;
        while(nodeptr != NULL){
            parentptr=nodeptr;
            if( val > nodeptr->data){
                nodeptr=nodeptr->right;
            }else{
                nodeptr=nodeptr->left;
            }
        }
        if(parentptr->data > val){
            parentptr->left=ptr;
        }else{
            parentptr->right=ptr;
        }
    }
    return tree;
}

void *preorder(struct node *tree){
    if(tree != NULL){
        printf("%d \t",tree->data);
        preorder(tree->left);
        preorder(tree->right);
    }
}

int main(){
    struct node *tree;
    tree=NULL;
    int num;
    printf("\nEnter the number -1 for end : ");
    scanf("%d",&num);
    while(num != -1){
        tree=insertion(tree,num);
        printf("\nEnter the number -1 for end : ");
        scanf("%d",&num);
    }
    preorder(tree);
    printf("\n");
}