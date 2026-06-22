class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            bucket = [0] * 26
            for i in range(len(str)):
                char = str[i]
                index = ord(str[i]) - ord('a')
                bucket[index] += 1
            bucket = tuple(bucket)
            if bucket in dict:
                dict[bucket].append(str)
            else:
                dict[bucket] = [str]
            

        
        ret = []
        for d in dict:
            ret.append(dict[d])
        
        return ret

            



        