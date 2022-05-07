#include <stdio.h>
#define MAX_SIZE 256

int cnt =0;
int Node_Num= 14;
struct Tree_Node{
    int key;
};

void Add_Tree(struct Tree_Node * Target_Tree, int item){
    if(cnt == MAX_SIZE){
        printf("Tree is full\n");
        return;
    }
    cnt++;
    Target_Tree->key= item;
};

void main(){
    struct Tree_Node ahn[MAX_SIZE];
    int tree_items[14][2] = {{1,55},{2,15},{3,60},{4,8},{5,28},{7,90},{8,3},{11,30},{23,48},{46,38},{47,50},{92,33},{184,32},{185,36}};
    for (int i=0; i<Node_Num; i++){

        for (cnt; cnt< tree_items[i][0];){
            Add_Tree(&ahn[cnt], 0);
        }
        Add_Tree(&ahn[cnt], tree_items[i][1]);
    }

    for (int i=0; i<186; i++){
        if (ahn[i].key == 48){
            printf("48. left: %d, right: %d\n", ahn[2*i].key, ahn[2*i+1].key);
            break;

        }
    }
    for (int i=0; i<186; i++){
        if (ahn[i].key == 30){
            printf("30. left: %d, right: %d\n", ahn[2*i].key, ahn[2*i+1].key);
            break;
        }
    }
    printf("root: %d\n", ahn[1].key);
}