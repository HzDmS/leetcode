/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        
        // recursive solution by using stack.
        
        vector<int> res;
        
        if (root == nullptr)
            return res;
        
        stack<TreeNode*> s;
        TreeNode* p = root;
        while (!s.empty() || p != nullptr) {
            while (p != nullptr) {
                s.push(p);
                p = p -> left;
            }

            if (!s.empty()) {
                p = s.top();
                s.pop();
                res.push_back(p -> val);
                p = p -> right;
            }
        }

        return res;
    }
};
