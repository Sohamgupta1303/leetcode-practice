class PrefixTree:
    # Node class 
    class Node:
        children = []
        endOfWord = False
        def __init__(self):
            self.children = [None] * 26
            self.endOfWord = False

    # implement PrefixTree
    root = None;
    def __init__(self):
        self.root = self.Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            character = word[i]
            index = ord(character) - ord("a")
            print(node.children)
            if node.children[index]:
                node = node.children[index]
                if i == len(word) - 1:
                    node.endOfWord = True
            else:
                temp = self.Node()
                node.children[index] = temp
                node = temp
                if i == len(word) - 1:
                    node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            character = word[i]
            index = ord(character) - ord("a")

            if node.children[index]:
                node = node.children[index]
                if i == len(word) - 1 and node.endOfWord:
                    return True
                elif i == len(word) - 1:
                    return False
            else:
                return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            character = prefix[i]
            index = ord(character) - ord("a")

            if node.children[index]:
                node = node.children[index]
                if i == len(prefix) - 1:
                    return True
            else:
                return False
        
        