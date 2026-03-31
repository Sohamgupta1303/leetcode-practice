class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def isPalindrome(word: str) -> bool:
            return word == word[::-1]
        
        def helper(partitions: List[str], index: int, word: str):
            # Termination case
            # Terminate if we reach the nth element and 
            # previous str is either a partition or not
            if (index == len(s) and isPalindrome(word) and len(word) > 0):
                partitions.append(word)
                ret.append(partitions.copy())
                return
            elif (index == len(s)):
                return

            if len(word) == 0:
                helper(partitions, index + 1, s[index])
                return

            # last word is a palindrome, we have 2 options:
            # 1) we can add it to partitions and start with the next one
            # 2) we can continue editing this one trying to find a longer
            #    palindrome
            if isPalindrome(word) and len(word) > 0:
                new_word = word + s[index]
                helper(partitions.copy(), index + 1, new_word)
                new_partitions = partitions.copy()
                new_partitions.append(word)
                helper(new_partitions, index + 1, s[index])
            else:
                # if its not a palindrome, we have to keep adding onto
                # it so that it hopefully becomes one
                word += s[index]
                helper(partitions, index + 1, word)
        
        helper([], 0, "")
        return ret