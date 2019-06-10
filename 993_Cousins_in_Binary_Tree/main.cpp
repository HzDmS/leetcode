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
    
    // time complexity: O(n)
    // space complexity: O(1)
    bool isCousins(TreeNode* root, int x, int y) {
        vector<int> a({x}), b({y});
        if (root == nullptr)
            return false;
        
        traversal(root, a, b, 1, 0);

        if (a[1] == b[1] && a[2] != b[2])
            return true;
        return false;
        
    }
    
    void traversal(
        TreeNode* root,
        vector<int>& a,
        vector<int>& b,
        int level,
        int parent
    ) {
        if (root == nullptr)
            return;
        if (root -> val == a[0]) {
            a.push_back(level);
            a.push_back(parent);
        }
        if (root -> val == b[0]) {
            b.push_back(level);
            b.push_back(parent);
        }
        
        traversal(root -> left, a, b, level + 1, root -> val);
        traversal(root -> right, a, b, level + 1, root -> val);
    }
    
};
