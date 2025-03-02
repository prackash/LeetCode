#include <iostream>
#include <bitset>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution{
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
            ListNode* dummyHead = new ListNode(0);
            ListNode* p = l1, *q = l2, *curr = dummyHead;
            int carry = 0;
            while(p != NULL || q != NULL || carry != 0){
                int x = (p != NULL) ? p->val : 0;
                int y = (q != NULL) ? q->val : 0;
                int sum = carry + x + y;
                carry = sum / 10;
                curr->next = new ListNode(sum % 10);
                curr = curr->next;
                if(p != NULL) p = p->next;
                if(q != NULL) q = q->next;
            }
            if(carry > 0){
                curr->next = new ListNode(carry);
            }
            return dummyHead->next;
        }
};

int main(){
    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);
    Solution s;
    ListNode* res = s.addTwoNumbers(l1, l2);
    while(res != NULL){
        cout << res->val << " ";
        res = res->next;
    }
    cout << endl;
    return 0;
}
// Time complexity: O(max(m, n))
// Space complexity: O(max(m, n))
// m is the length of l1, n is the length of l2