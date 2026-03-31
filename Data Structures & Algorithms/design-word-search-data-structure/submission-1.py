class WordDictionary:

    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.eof = False

    def __init__(self):
        self.root = self.Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            character = word[i]
            index = ord(character) - ord("a")
            if (node.children[index]):
                node = node.children[index]
            else:
                temp = self.Node()
                node.children[index] = temp
                node = temp
        node.eof = True

    def search(self, word: str) -> bool:
        def helper(index: int, node: self.Node) -> bool:
            # the code will terminate if node doesnt exist or 
            # index is out of bounds
            if not node or index == len(word):
                return False
            character = word[index]
            if character == ".":
                # we should check if ANY of the letters work
                for child in node.children:
                    if index == len(word) - 1 and child:
                        if child.eof: return True
                    elif helper(index + 1, child):
                        return True
                # none of the letters worked => not found
                return False
            else:
                idx = ord(character) - ord("a")
                # check if that letter even exists
                if node.children[idx]:
                    if (node.children[idx].eof and index == len(word) - 1):
                        # node must be last letter of word
                        return True
                    elif (index == len(word) - 1):
                        # last letter but not eof, so not a word
                        return False
                    # it exists, now you can call recursively. 
                    return helper(index + 1, node.children[idx])
                else:
                    # the node doesnt exist, word not completed
                    return False


           
        
        return helper(0, self.root)
            

            

        
