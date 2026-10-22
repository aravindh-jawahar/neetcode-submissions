class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):
            characters = {}

            for c in s:
                characters[c] = characters.get(c, 0) + 1
            
            for cs in t:
                if cs not in characters:
                    return False
                characters[cs] -= 1
        else:
            return False

        return all(value == 0 for value in characters.values())