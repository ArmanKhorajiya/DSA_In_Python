#include <stdio.h>   // Required to fix "NULL is undefined" and use printf

struct Node {
    int data;
    struct Node *next;
};

int main() {
    // 1. Initialize nodes
    struct Node a = {10, NULL};
    struct Node b = {20, NULL};
    struct Node c = {30, NULL};

    // 2. Link nodes together
    a.next = &b;
    b.next = &c;

    // 3. Set up pointers for traversal
    struct Node *head = &a;
    struct Node *p = head;

    // 4. Advance pointers
    head = head->next;
    p->next = p->next->next;

    // 5. Print out the data
    printf("%d %d %d\n", head->data, p->data, p->next->data);

    return 0;
}
