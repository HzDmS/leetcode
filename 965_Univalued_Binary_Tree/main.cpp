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
    bool isUnivalTree(TreeNode* root) {
        if (root == nullptr) return true;
        bool res = true;
        int value = root -> val;
        preorder(root, value, res);
        return res;
    }
    
    void preorder(TreeNode* root, int& value, bool& res) {
        if (!root || !res) return;
        if (root -> val != value)
            res = false;
        preorder(root -> left, value, res);
        preorder(root -> right, value, res);
    }
    
};
