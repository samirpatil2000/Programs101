#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    int height;
    struct node *left;
    struct node *right;
};


int height(struct node *node){
    if(node == NULL){
        return 0;
    }else{
        return node->height;
    }
}

int max(int a, int b)
{
    return (a > b)? a : b;
}


struct node *newNode(int data){
    struct node *n=malloc(sizeof(struct node));
    n->data=data;
    n->left=NULL;
    n->right=NULL;
    n->height=1;
    return n;
}


struct node *rightRotate(struct node *z){
    struct node *y,*T3;
    y=z->left;
    T3=y->right;

    y->right=z;
    z->left=T3;

    y->height=max(height(y->left),height(y->right))+1;
    z->height=max(height(z->left),height(z->right))+1;

    return y;
}

struct node *leftRotate(struct node *z){
    struct node *y,*T2;
    y=z->right;
    T2=y->left;

    y->left=z;
    z->right=T2;

    y->height=max(height(y->left),height(y->right))+1;
    z->height=max(height(z->left),height(z->right))+1;

    return y;
}

int getBalanceFactor(struct node *node){
    if(node==NULL){
        return 0;
    }else{
        return (height(node->left)-height(node->right));
    }
}

struct node *insertionAVLTree(struct node *node,int data){

    if(node==NULL){
        return newNode(data);
    }
    if(data > node->data){
        node->right=insertionAVLTree(node->right,data);
    }else if(data<node->data){
        node->left=insertionAVLTree(node->left,data);
    }else{
        return node;
    }
    node->height = 1 + max(height(node->left),
                           height(node->right));


    int balanceFactor=getBalanceFactor(node);

    // Left Left Case
    if (balanceFactor > 1 && data < node->left->data)
        return rightRotate(node);
 
    // Right Right Case
    if (balanceFactor < -1 && data > node->right->data)
        return leftRotate(node);
 
    // Left Right Case
    if (balanceFactor > 1 && data > node->left->data)
    {
        node->left =  leftRotate(node->left);
        return rightRotate(node);
    }
 
    // Right Left Case
    if (balanceFactor < -1 && data < node->right->data)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
 
    /* return the (unchanged) node pointer */
    return node;

}
void preOrder(struct node *root)
{
    if(root != NULL)
    {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }

}

int main(){
    struct node *root = NULL;
 
  /* Constructing tree given in the above figure */
  root = insertionAVLTree(root, 10);
  root = insertionAVLTree(root, 20);
  root = insertionAVLTree(root, 30);
  root = insertionAVLTree(root, 40);
  root = insertionAVLTree(root, 50);
  root = insertionAVLTree(root, 25);
 
  /* The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50
  */
 
  printf("Preorder traversal of the constructed AVL"
         " tree is \n");
  preOrder(root);
}