class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        characters_strings = {}
        for s in strs:
            i = 0
            characters = [0] * 26
            while i < len(s):
                character = s[i]
                characters [ord(character) - ord('a')] += 1
                i += 1
            if (tuple(characters) in characters_strings.keys()):
                strings = characters_strings[tuple(characters)]
                strings.append(s)
            else:
                characters_strings[tuple(characters)] = []
                characters_strings[tuple(characters)].append(s)
            print(characters_strings[tuple(characters)])

        result = []
        for ch, st in characters_strings.items():
            result.append(st)
        
        return result

        
        