class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_letters = [0] * 26
        for i in range (len (s1) ):
            char = s1[i]
            s1_letters[ord(char) - ord('a')] += 1;
        
        s2_letters = [0] * 26

        for i in range (len (s1) ):
            char = s2[i]
            s2_letters[ord(char) - ord('a')] += 1;

        if s2_letters == s1_letters:
            return True

        i = len(s1)
        while (i < len (s2)):
            char = s2[i]
            s2_letters[ord(char) - ord('a')] += 1
            first_char = s2[i - len(s1)]
            s2_letters[ord(first_char) - ord('a')] -= 1
            if s2_letters == s1_letters:
                return True
            i += 1
        
        return False
            

        