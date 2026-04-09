#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

void deleteNode(struct Node* head){
    if(head == NULL || head->next == NULL){
        return; // nothing to delete
    }

    struct Node* temp = head->next;
    head->next = temp->next;
    free(temp);
}
