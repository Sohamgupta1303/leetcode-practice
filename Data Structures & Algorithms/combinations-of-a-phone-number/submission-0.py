class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        letters = {i : [] for i in range(2, 10)}
        letters[2] = ["a", "b", "c"]
        letters[3] = ["d", "e", "f"]
        letters[4] = ["g", "h", "i"]
        letters[5] = ["j", "k", "l"]
        letters[6] = ["m", "n", "o"]
        letters[7] = ["p", "q", "r", "s"]
        letters[8] = ["t", "u", "v"]
        letters[9] = ["w", "x", "y", "z"]

        def helper(index: int, s: str):
            if index == len(digits):
                if s != "":
                    ret.append(s)
                return
            
            number = int(digits[index])
            corresponding_letters = letters[number]
            for let in corresponding_letters:
                helper(index + 1, s + let)
            
        helper(0, "")
        return ret