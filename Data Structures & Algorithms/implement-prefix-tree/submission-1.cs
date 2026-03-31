
public class TrieNode {
    public Dictionary<char, TrieNode> children;
    public bool isEndOfWord;

    public TrieNode() {
        children = new Dictionary<char, TrieNode>();
        isEndOfWord = false;
    }
}

public class PrefixTree {
    private TrieNode root;

    public PrefixTree() {
        root = new TrieNode();
    }

    public void Insert(string word) {
        TrieNode node = root;
        foreach (char c in word) {
            if (!node.children.ContainsKey(c))
                node.children[c] = new TrieNode();
            node = node.children[c];
        }
        node.isEndOfWord = true;
    }

    public bool Search(string word) {
        TrieNode node = root;
        foreach (char c in word) {
            if (!node.children.ContainsKey(c))
                return false;
            node = node.children[c];
        }
        return node.isEndOfWord;
    }

    public bool StartsWith(string prefix) {
        TrieNode node = root;
        foreach (char c in prefix) {
            if (!node.children.ContainsKey(c))
                return false;
            node = node.children[c];
        }
        return true;
    }
}
