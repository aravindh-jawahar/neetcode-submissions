class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # find the '#' to get the length prefix
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])           # number before '#'
            word = s[j + 1 : j + 1 + length]  # extract exactly `length` chars
            result.append(word)
            
            i = j + 1 + length              # move pointer past this word
        
        return result