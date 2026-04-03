class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = []
        visited = set()
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        j = 0 # the index where the last subset was made
        i = 0
        while i < len(s):
            letter = s[i]
            visited.add(letter)
            count[letter] -= 1
            if count[letter] == 0:
                visited.remove(letter)
                if not visited:
                    ret.append(i - j + 1)
                    j = i + 1
            i += 1
        
        return ret




        