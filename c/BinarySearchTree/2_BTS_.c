#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left;
    struct node *right;
};

struct node *createTree(struct node *tree){
    tree=NULL;
    return tree;
}

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




struct node *findSmallestNode(struct node *tree){
    if(tree == NULL || tree->left == NULL){
        return tree;
    }else{
        return findSmallestNode(tree->left);
    }
}

struct node *findLargestNode(struct node *tree){
    if(tree == NULL || tree->right == NULL){
        return tree;
    }else{
        return findLargestNode(tree->right);
    }
}
struct node *minValueNode(struct node *tree){
    struct node *current=tree;
    while(current !=NULL && current->left !=NULL){
        current=current->left;
    }
    return current;
}

void *inorder(struct node *tree){
    if(tree != NULL){
        printf("%d \t",tree->data);
        inorder(tree->right);
        inorder(tree->left);
        
    }
}

void *preorder(struct node *tree){
    if(tree != NULL){
        printf("%d \t",tree->data);
        inorder(tree->left);
        inorder(tree->right);
        
    }
}


struct node *deleteElement(struct node *tree,int val){
    struct node *temp;
    if(tree==NULL){
        return tree;
    }else if(val<tree->data){
        return deleteElement(tree->left,val);
    }else if(val > tree->data){
        return deleteElement(tree->right,val);
    }else{
        if(tree->left == NULL){
            temp=tree->right;
            free(tree);
            return temp;
        }else if(tree->right == NULL){
            temp=tree->left;
            free(tree);
            return temp;
        }

        temp=minValueNode(tree->right);
        tree->data=temp->data;
        tree->right=deleteElement(tree->right,temp->data);
    }
    return tree;
}


int main(){
    int option;
    struct node *tree,*smallestNumber,*largestNumber;
    tree=NULL;
    do
    {
        printf("\n\n ** Main Menu **");
        // printf("\n 0 : Create BST");
        printf("\n 1 : Insertion");
        printf("\n 2 : InOrder Traversal");
        printf("\n * : PostOrder Traversal");
        printf("\n 3 : PreOrder Traversal");
        printf("\n 4 : Find Smallest element");
        printf("\n 5 : Find Largest element");
        printf("\n 6 : Delete element");
        printf("\n 8 : Count Total number of elements");
        printf("\n 9 : Count Total number of internal nodes");
        printf("\n 10 : Count Total number of external nodes");
        printf("\n 11 : Find Mirror image of tree");
        printf("\n 12 : Determine the height of BST");
        printf("\n 13 : Delete entire tree");
        printf("\n 14 : Exit");

        printf("\n Enter your option : ");
        scanf("%d",&option);
        int val,num,i=0;
        switch (option)
        {
            case 1:
                printf("Enter number of elements to be inserted :");
                scanf("%d",&num);
                while(i<=num){
                    printf("Enter number : ");
                    scanf("%d",&val);
                    tree=insertion(tree,val);
                    i++;
                }
                break;
            case 2:
                inorder(tree);
                break;
            case 3:
                preorder(tree);
                break;
            case 4:
                smallestNumber=findSmallestNode(tree);
                printf("The smallest element is %d\n",smallestNumber->data);
                break;
            case 5:
                largestNumber=findLargestNode(tree);
                printf("The largest element is %d\n",largestNumber->data);
                break;
            case 6:
                printf("Enter number of elements to be delete :");
                scanf("%d",&num);
                tree=deleteElement(tree,num);
                break;
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