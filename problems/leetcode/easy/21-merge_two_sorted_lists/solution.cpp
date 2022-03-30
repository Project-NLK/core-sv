#include<iostream>
#include "solution.h"

using namespace std;

int main(int argc, char *argv[]) {
    ListNode *a3 = new ListNode(4);
    ListNode *a2 = new ListNode(2, a3);
    ListNode *a1 = new ListNode(1, a2);

    ListNode *b3 = new ListNode(4);
    ListNode *b2 = new ListNode(3, b3);
    ListNode *b1 = new ListNode(1, b2);

    ListNode *result = Solution().mergeTwoLists(a1, b1);


    cout << "[";

    while (result->next) {
        cout << result->val << ",";
        result = result->next;
    }
    cout << result->val << "]" << endl;

    return 0;
}