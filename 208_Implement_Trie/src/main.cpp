#include <iostream>
#include <string>

char START = 'a';

class TrieNode {
public:
    TrieNode();
    TrieNode* next[26];
    bool isString;
};

class Trie {
public:
    Trie();
    void insert(std::string s);
    bool search(std::string s);
    bool startsWith(std::string s);

private:
    TrieNode* root;
};

int main() {

    Trie* t = new Trie();

    t -> insert("apple");

    std::string s1 = "app";
    std::string s2 = "apple";

    std::cout << "Searching " << s1 << ": " << t -> search(s1) << std::endl;
    std::cout << "Searching " << s2 << ": " << t -> search(s2) << std::endl;
    std::cout << "StartsWith " << s1 << ": " << t -> startsWith(s1) << std::endl;
    std::cout << "StartsWith " << s2 << ": " << t -> startsWith(s2) << std::endl;

    return 0;
}

TrieNode::TrieNode() {
    for (int i = 0; i < 26; i++) {
        next[i] = nullptr;
    }
    isString = false;
}

Trie::Trie() {
    root = new TrieNode();
}

void Trie::insert(std::string s) {
    TrieNode* p = root;
    for (int i = 0; i < s.size(); i++) {
        // to prevent re-initializating the node in the case of inserting multiple words.
        if (p -> next[s[i] - START] == nullptr)
            p -> next[s[i] - START] = new TrieNode();
        p = p -> next[s[i] - START];
    }
    p -> isString = true;
}

bool Trie::search(std::string s) {
    TrieNode* p = root;
    for (int i = 0; i < s.size(); i++) {
        if (p -> next[s[i] - START] == nullptr)
            return false;
        p = p -> next[s[i] - START];
    }
    if (p == nullptr || p -> isString == false)
        return false;
    return true;
}

bool Trie::startsWith(std::string s) {
    TrieNode* p = root;
    for (int i = 0; i < s.size(); i++) {
        if (p -> next[s[i] - START] == nullptr)
            return false;
        p = p -> next[s[i] - START];
    }
    return true;
}
