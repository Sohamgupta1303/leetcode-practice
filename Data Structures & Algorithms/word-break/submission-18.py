class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set()
        for word in wordDict:
            dictionary.add(word)
        print(dictionary)

        memo = [None] * len(s)

        def helper(index: int) -> bool:
            if index == len(s):
                return True
            if memo[index] is not None:
                return memo[index]

            for i in range(index, len(s) + 1):
                if s[index: i] in dictionary:
                    if helper(i): 
                        memo[index] = True
                        return True
            
            memo[index] = False
            return False
        
        return helper(0)
            

        
        