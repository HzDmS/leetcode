/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> postorder(Node* root) {
        
        vector<int> res;
        postOrderTraversal(root, res);
        return res;
        
    }
    
    void postOrderTraversal(Node* root, vector<int>& res) {
        if (root == nullptr)
            return;
        for (auto node : root -> children) {
            postOrderTraversal(node, res);
        }
        res.push_back(root -> val);
    }
};
