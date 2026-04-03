class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = []
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        

        j = -1 # j is the index of last letter in partition
        i = 0

        end = last[s[0]]
        while i <= end:
            if i == end:
                ret.append(end - j )
                j = end
            end = max(last[s[i]], end)
            i += 1
            if i > end and i in range(len(s)):
                end = last[s[i]]
        
        return ret






        