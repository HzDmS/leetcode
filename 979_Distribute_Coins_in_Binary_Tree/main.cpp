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
    int distributeCoins(TreeNode* root) {
        int res = 0;
        traversal(root, res);
        return res;
    }
    
    int traversal(TreeNode* root, int &count) {
        if (!root) return 0;
        int left = traversal(root -> left, count);
        int right = traversal(root -> right, count);
        int residual = root -> val - 1;
        count += abs(left);
        count += abs(right);
        return left + residual + right;
    }
    
};
