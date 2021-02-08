#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left;
    struct node *right;
}

struct node *createTree(struct node *tree){
    tree=NULL;
}

struct node *insertion(struct node *tree,int val){
    struct node *ptr,*parentptr,*nodeptr;

    ptr=malloc(sizeof(struct node));
    ptr->data=val;
    ptr->left=NULL;
    ptr->right=NULL;

    if(tree==NULL){
        tree=ptr;
    }else{
        parentptr=NULL;
        nodeptr=ptr;
        while(nodeptr != NULL){
            parentptr=nodeptr;
            if(nodeptr->data>val){
                nodeptr=nodeptr->left;
            }else{
                nodeptr=nodeptr->right;
            }
        }
        if(parentptr->data>val){
            parentptr->left=ptr;
        }else{
            parentptr->right=ptr;
        }
    }
    return tree;
}


void inorder(struct node *tree){
    if(tree != NULL{
        printf("%d \t",tree->data);
        in
    }
}

int main(){
    int option;
    struct node *tree;
    tree=create_tree(tree);
    do
    {
        printf("\n\n ** Main Menu **");
        // printf("\n 0 : Create BST");
        printf("\n 1 : Insertion");
        printf("\n 2 : InOrder Traversal");
        printf("\n 3 : PostOrder Traversal");
        printf("\n 4 : PreOrder Traversal");
        printf("\n 5 : Find Smallest element");
        printf("\n 6 : Find Largest element");
        printf("\n 7 : Delete element");
        printf("\n 8 : Count Total number of elements");
        printf("\n 9 : Count Total number of internal nodes");
        printf("\n 10 : Count Total number of external nodes");
        printf("\n 11 : Find Mirror image of tree");
        printf("\n 12 : Determine the height of BST");
        printf("\n 13 : Delete entire tree");
        printf("\n 14 : Exit");

        printf("\n Enter your option : ");
        scanf("%d",&option);

        switch (option)
        {
            case 1:
                tree=insertion(tree);
                break;
            case 2:
                tree=insert_beg(tree);
                break;
            // case 3:
            //     tree=insert_end(tree);
            //     break;
            // case 4:
            //     tree=insert_before(tree);
            //     break;
            // case 5:
            //     tree=insert_after(tree);
            //     break;
            // case 6:
            //     tree=delete_beg(tree);
            //     break;
            // case 7:
            //     tree=delete_end(tree);
            //     break;
            // case 8:
            //     tree=delete_node(tree);
            //     break;
            // case 9:
            //     tree=delete_after(tree);
            //     break;
            // case 10:
            //     tree=deleteList(tree);
            //     break;
            // case 11:
            //     tree=sortLinkedList(tree);
            //     break;
            default:
                break;
        }
    } while (option != 12);
    
}